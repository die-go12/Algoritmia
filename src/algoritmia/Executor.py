from .AlgoritmiaVisitor import AlgoritmiaVisitor
from .AlgoritmiaParser import AlgoritmiaParser
import subprocess
import os
import copy
import shutil
import re

class AlgoritmiaExecutor(AlgoritmiaVisitor):
    def __init__(self):
            # Estado
            self.variables = {}        # Scope actual
            self.procedimientos = {}   # Tabla de procedimientos
            self.output_notes = []     # Acumulador de notas
            self.output_filename = "salida"  # Nombre por defecto
            # Configuración de ejecución
            self.entry_point = "Main"  
            
            # Depuración / estadísticas
            self.DEBUG = False         # Poner False para silencio
            self.note_calls = 0        # cuantas veces se llamó (:)
            self.note_added = 0        # cuántas notas válidas fueron agregadas

            # ---------------------------------------------------------
            # RUTAS 
            # ---------------------------------------------------------
            self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # src/algoritmia
            self.PROJECT_DIR = os.path.dirname(self.BASE_DIR)           # src/
            self.MUSIC_DIR = os.path.join(self.PROJECT_DIR, "music")    # src/music
            self.OUTPUT_DIR = os.path.join(self.PROJECT_DIR, "media")   # src/media

            os.makedirs(self.OUTPUT_DIR, exist_ok=True)

            # Archivos de sonido
            self.CFG_PATH = os.path.normpath(os.path.join(self.MUSIC_DIR, "timgm6mb.cfg"))
            self.SF2_PATH = os.path.normpath(os.path.join(self.MUSIC_DIR, "TimGM6mb.sf2"))

            # Límites de seguridad
            self.MAX_RECURSION = 500
            self._call_depth = 0
            self.MAX_WHILE_ITERS = 200_000

    # -----------------------------
    # PROGRAMA
    # -----------------------------
    # --- NUEVOS HELPERS PARA ARITMÉTICA MUSICAL ---
    def _nota_a_int(self, nota_str):
        """Convierte 'A0' a 0, 'B0' a 1... para poder sumarles números"""
        m = re.match(r'^([A-Ga-g])([#b]?)(\d*)$', nota_str)
        if not m: return None 

        letra, alter, oct_str = m.groups()
        letra = letra.upper()
        octava = int(oct_str) if oct_str else 4 
        
        # A=0, B=1, C=2...
        offsets = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
        base_val = offsets[letra]
        
        # En Algoritmia la octava cambia en C (A0, B0 -> C1)
        if letra in ['A', 'B']:
            return (octava * 7) + base_val
        else:
            return ((octava - 1) * 7) + base_val

    def _int_a_nota(self, valor_int):
        """Convierte un entero (ej: 0) de vuelta a nota ('A0')"""
        if not isinstance(valor_int, int): return str(valor_int)
        
        residuo = valor_int % 7
        octava_base = valor_int // 7
        
        letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        letra = letras[residuo]
        
        if letra in ['A', 'B']:
            octava_visual = octava_base
        else:
            octava_visual = octava_base + 1
            
        return f"{letra}{octava_visual}"
    
    def visitPrograma(self, ctx: AlgoritmiaParser.ProgramaContext):
            # 1. Registrar procedimientos
            print("--- Registrando Procedimientos ---")
            for p in ctx.procedimiento():
                if p.ID_MAYUS():
                    name = p.ID_MAYUS().getText()
                    self.procedimientos[name] = p
                    # Solo imprimimos si es DEBUG para no ensuciar la salida estándar
                    if self.DEBUG: print(f" - Registrado: {name}")

            # 2. Ejecutar el Entry Point seleccionado (Dinámico)
            target = self.entry_point  # <--- USAMOS LA VARIABLE, NO "Main" FIJO

            if target in self.procedimientos:
                print(f"\n--- Ejecutando: {target} ---")
                try:
                    self.visitProcedimiento(self.procedimientos[target])
                except Exception as e:
                    print(f"\n Error en ejecución: {e}")
                    if self.DEBUG: import traceback; traceback.print_exc()
                    return 

                # imprimir estadísticas si DEBUG
                if self.DEBUG:
                    print(f"\n[STATS] llamadas a (:): {self.note_calls}, notas válidas: {self.note_added}")

                # 3. Generar Salida Multimedia
                if self.output_notes:
                    # CAMBIAR: Usamos la variable self.output_filename
                    print(f"\n--- Generando Archivos ({self.output_filename}) ---")
                                
                    # Nombre dinámico para el .ly
                    ly_name = f"{self.output_filename}.ly"
                    ly_path = os.path.join(self.OUTPUT_DIR, ly_name)
                                
                    # Nombre base dinámico para midi/wav
                    base = os.path.join(self.OUTPUT_DIR, self.output_filename)
                                
                    self.generar_lilypond(ly_path)
                    self.render_musica(base)
                else:
                    print("No hay notas musicales para procesar.")
            else:
                print(f"Error: No se encontró el procedimiento '{target}'.")
                print(f"   Procedimientos disponibles: {', '.join(self.procedimientos.keys())}")
            
            return None

    # -----------------------------
    # PROCEDIMIENTO
    # -----------------------------
    def visitProcedimiento(self, ctx: AlgoritmiaParser.ProcedimientoContext, args=None):
        """
        Ejecuta un procedimiento. Firma compatible con:
            visitLlamada_proc(...) -> visitProcedimiento(proc_ctx, args=args_vals)
        Semántica:
        - Parámetros: pasados por referencia si son listas (según tu regla).
        - Asignaciones (x <- expr): hacen deepcopy cuando expr es lista (se mantiene).
        """
        # controlar profundidad y overflow
        self._call_depth += 1
        if self._call_depth > self.MAX_RECURSION:
            raise RecursionError("Stack Overflow: Recursión excesiva.")

        # Guardar frame del caller (REFERENCIA, no deepcopy)
        prev_vars = self.variables

        # Nuevo frame para el callee
        self.variables = {}

        if self.DEBUG and ctx.ID_MAYUS():
            pname = ctx.ID_MAYUS().getText()
            print(f"[DEBUG] -> Entrando a procedimiento {pname} (depth {self._call_depth})")

        try:
            # Asignar parámetros formales (si se pasaron)
            if args and ctx.parametros() is not None:
                params_nodes = ctx.parametros().ID_MINUSCULA()
                for i, pnode in enumerate(params_nodes):
                    pname = pnode.getText()
                    val = args[i] if i < len(args) else 0
                    # según regla: pasar listas por referencia (no deepcopy aquí)
                    self.variables[pname] = val

                # Impresión segura de params (sin f-strings anidados)
                if self.DEBUG:
                    params_text = []
                    for p in params_nodes:
                        pname = p.getText()
                        params_text.append(f"{pname}: {self.variables[pname]}")
                    print(f"[DEBUG] params -> {{ {', '.join(params_text)} }}")

            # Ejecutar cuerpo
            if ctx.instrucciones() is not None:
                self.visit(ctx.instrucciones())

        finally:
            # Restaurar frame del caller
            self.variables = prev_vars
            self._call_depth -= 1
            if self.DEBUG and ctx.ID_MAYUS():
                pname = ctx.ID_MAYUS().getText()
                print(f"[DEBUG] <- Saliendo de procedimiento {pname} (depth {self._call_depth})")

        return None


    # -----------------------------
    # INSTRUCCIONES
    # -----------------------------
    def visitInstrucciones(self, ctx: AlgoritmiaParser.InstruccionesContext):
        for ins in ctx.instruccion():
            self.visit(ins)
        return None

    def visitInstructions_block(self, ctx):
        # Helper para bloques anidados (if/while)
        if ctx is None: return
        for ins in ctx.instruccion():
            self.visit(ins)

    # -----------------------------
    # ASIGNACIÓN
    # -----------------------------
    def visitAsignacion(self, ctx: AlgoritmiaParser.AsignacionContext):
        name = ctx.ID_MINUSCULA().getText()
        val = self.visit(ctx.expr())
        
        # REGLA DEL PDF: "En el caso de asignar listas, copiar los valores"
        if isinstance(val, list):
            self.variables[name] = copy.deepcopy(val)
        else:
            self.variables[name] = val

        if self.DEBUG:
            print(f"[DEBUG] asignacion: {name} <- {val}")
        return val

    # -----------------------------
    # LECTURA
    # -----------------------------
    def visitLectura(self, ctx: AlgoritmiaParser.LecturaContext):
        name = ctx.ID_MINUSCULA().getText()
        entrada = input(f"<?> {name}: ").strip()
        
        # Intentar convertir a Entero (según PDF base)
        # Opcional: soportar listas en input como {1,2}
        if entrada.startswith("{") and entrada.endswith("}"):
            # Parseo básico de lista en input
            inner = entrada[1:-1].replace(',', ' ').split()
            lista = []
            for x in inner:
                if x.lstrip('-').isdigit(): lista.append(int(x))
            self.variables[name] = lista
        elif entrada.lstrip('-').isdigit():
            self.variables[name] = int(entrada)
        else:
            self.variables[name] = entrada # String fallback

    # -----------------------------
    # ESCRITURA 
    # -----------------------------
    def visitEscritura(self, ctx: AlgoritmiaParser.EscrituraContext):
        # CAMBIO: Ya no iteramos porque la gramática es estricta (1 ítem por <w>)
        
        # 1. Obtenemos el único ítem
        item = ctx.escritura_item()
        
        # 2. Procesamos según tipo
        if item.STRING():
            # Caso texto: "Hola" -> quitamos comillas
            texto = item.STRING().getText()[1:-1]
            print(texto)
        else:
            # Caso expresión: variable o número
            val = self.visit(item.expr())
            
            # Formateo de listas
            if isinstance(val, list):
                s = str(val).replace(',', '') # [1 2 3]
                print(s)
            else:
                print(str(val))
        
        return None



    # -----------------------------
    # EXPRESIONES Y COMPARACIÓN
    # -----------------------------
    def visitExpr(self, ctx):
        return self.visit(ctx.comparacion())

    def visitComparacion(self, ctx: AlgoritmiaParser.ComparacionContext):
        # Evaluar aritmética base
        val = self.visit(ctx.aritmetica(0))
        
        # Procesar operadores encadenados si existen
        count = 1
        children = ctx.getChildren()
        it = iter(children)
        next(it) # Skip primer aritmetica

        # Nota: Iteramos manualmente porque ANTLR genera lista plana en getChildren
        # pero ctx.aritmetica() da acceso directo a los operandos.
        
        # Simplemente iteramos sobre el número de operadores
        num_ops = (ctx.getChildCount() - 1) // 2
        
        for i in range(num_ops):
            # El operador está en posición impar: 1, 3, 5...
            op_token = ctx.getChild(2*i + 1).getText()
            right = self.visit(ctx.aritmetica(i+1))
            
            result = False
            if op_token == "=": result = (val == right)
            elif op_token == "/=": result = (val != right)
            elif op_token == "<": result = (val < right)
            elif op_token == ">": result = (val > right)
            elif op_token == "<=": result = (val <= right)
            elif op_token == ">=": result = (val >= right)
            
            # Actualizar val para la siguiente comparación (si fuera encadenada a < b < c)
            # Pero Algoritmia devuelve 0/1. Convertimos resultado a entero.
            val = 1 if result else 0
            
        return val

    def visitAritmetica(self, ctx: AlgoritmiaParser.AritmeticaContext):
        res = self.visit(ctx.termino(0))
        for i in range(1, len(ctx.termino())):
            op = ctx.getChild(2*i - 1).getText()
            der = self.visit(ctx.termino(i))
            if op == "+": 
                # Concatenación si ambos son listas
                if isinstance(res, list) and isinstance(der, list): res = res + der
                else: res += der
            elif op == "-": res -= der
        return res

    def visitTermino(self, ctx: AlgoritmiaParser.TerminoContext):
        res = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(2*i - 1).getText()
            der = self.visit(ctx.factor(i))
            if op == "*": res *= der
            elif op == "/": res //= der # División entera
            elif op == "%": res %= der
        return res

    # -----------------------------
    # FACTOR
    # -----------------------------
 
    def visitFactor(self, ctx: AlgoritmiaParser.FactorContext):
        # 1. CASO NEGATIVO
        # Si el primer hijo es un guion '-', es un negativo.
        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == '-':
            
            val = self.visit(ctx.factor()) 
            return -val

        # 2. Entero normal
        if ctx.INT(): 
            return int(ctx.INT().getText())
        
        # 3. Lista literal { ... }
        if ctx.lista(): 
            return self.visit(ctx.lista())

        # 4. Variable
        if ctx.ID_MINUSCULA() and ctx.getChildCount() == 1:
            name = ctx.ID_MINUSCULA().getText()
            return self.variables.get(name, 0)

        # 5. Longitud #v
        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == '#':
            name = ctx.ID_MINUSCULA().getText()
            val = self.variables.get(name)
            if isinstance(val, list):
                return len(val)
            return 0

        # 6. Acceso índice v[expr]
        if ctx.getChildCount() == 4 and ctx.getChild(1).getText() == '[':
            name = ctx.ID_MINUSCULA().getText()
            idx = self.visit(ctx.expr())
            lista = self.variables.get(name)
            
            if not isinstance(lista, list): return 0

            try:
                idx_int = int(idx)
            except:
                return 0

            # Conversión Base-1 (Algoritmia) a Base-0 (Python)
            idx_py = idx_int - 1
            if idx_py < 0 or idx_py >= len(lista):
                if self.DEBUG: print(f"⚠️ Índice fuera de rango: {idx_int}")
                return 0
            return lista[idx_py]

        # 7. Nota Musical o Constante (ID_MAYUS)
        if ctx.ID_MAYUS(): 
            texto = ctx.ID_MAYUS().getText()
            val_int = self._nota_a_int(texto)
            if val_int is not None:
                return val_int
            return texto 

        # 8. Paréntesis ( expr )
        if ctx.expr(): 
            return self.visit(ctx.expr())

        return 0

    def visitLista(self, ctx: AlgoritmiaParser.ListaContext):
        if ctx.elementos_lista():
            return [self.visit(e) for e in ctx.elementos_lista().expr()]
        return []

    # -----------------------------
    # LISTAS: ADD y POP
    # -----------------------------
    def visitAddlista(self, ctx: AlgoritmiaParser.AddlistaContext):
        name = ctx.ID_MINUSCULA().getText()
        val = self.visit(ctx.expr())
        
        if name not in self.variables: self.variables[name] = []
        if not isinstance(self.variables[name], list):
             raise RuntimeError(f"'{name}' no es lista.")

        # Al insertar en lista, copiamos para evitar referencias circulares complejas
        if isinstance(val, list):
            self.variables[name].append(copy.deepcopy(val))
        else:
            self.variables[name].append(val)

        if self.DEBUG:
            print(f"[DEBUG] addlista: {name} << {val}  (tam {len(self.variables[name])})")

    def visitPoplista(self, ctx: AlgoritmiaParser.PoplistaContext):
        name = ctx.ID_MINUSCULA().getText()
        idx = self.visit(ctx.expr())
        lista = self.variables.get(name)
        
        if not isinstance(lista, list):
            if self.DEBUG:
                print(f"[DEBUG] poplista: '{name}' no es lista (valor: {lista})")
            return 0
        
        try:
            idx_int = int(idx)
        except Exception:
            if self.DEBUG:
                print(f"[DEBUG] poplista: índice no entero para {name}[{idx}]")
            return 0

        # Base-1 -> convertimos y validamos
        pos = idx_int - 1
        if idx_int <= 0 or pos < 0 or pos >= len(lista):
            if self.DEBUG:
                print(f" poplista: índice fuera de rango: {idx_int} en lista '{name}' de tam {len(lista)}")
            return 0

        val = lista.pop(pos)
        if self.DEBUG:
            print(f"[DEBUG] poplista: {name}[{idx_int}] -> {val}  (nuevo tam {len(lista)})")
        return val

    # -----------------------------
    # CONTROL: IF / WHILE
    # -----------------------------
    def visitCondicional(self, ctx: AlgoritmiaParser.CondicionalContext):
        cond = self.visit(ctx.expr())
        # PDF: 0 es Falso, 1 (o cualquier otro) es Verdadero
        if cond != 0:
            self.visit(ctx.instrucciones(0))
        elif len(ctx.instrucciones()) > 1:
            self.visit(ctx.instrucciones(1))

    def visitWhile(self, ctx: AlgoritmiaParser.WhileContext):
        iter_count = 0
        while self.visit(ctx.expr()) != 0:
            self.visit(ctx.instrucciones())
            iter_count += 1
            if iter_count > self.MAX_WHILE_ITERS:
                raise RuntimeError("Bucle infinito detectado.")

    # -----------------------------
    # LLAMADA PROCEDIMIENTO
    # -----------------------------
    def visitLlamada_proc(self, ctx: AlgoritmiaParser.Llamada_procContext):
        name = ctx.ID_MAYUS().getText()
        if name not in self.procedimientos:
            raise RuntimeError(f"Procedimiento no definido: {name}")
        
        if self.DEBUG:
            print(f"[DEBUG] Llamada a procedimiento: {name} con {len(ctx.expr())} args")
        args_vals = [self.visit(e) for e in ctx.expr()]
        return self.visitProcedimiento(self.procedimientos[name], args=args_vals)

    # -----------------------------
    # MÚSICA 
    # -----------------------------
    def visitReproduccion(self, ctx: AlgoritmiaParser.ReproduccionContext):
        # CAMBIO: Ya no hay bucle "for" porque la gramática ahora es estricta (solo 1 expresión)
        
        # 1. Obtenemos la única expresión
        expr_node = ctx.expr() 
        
        # 2. La evaluamos
        val = self.visit(expr_node)

        # 3. Procesamos el resultado (igual que antes)
        if isinstance(val, list):
            # Si la expresión era una lista { C4 E4 }, tocamos todos sus elementos
            for v in val:
                self._agregar_nota(v)
        else:
            # Si era una nota simple o variable, la tocamos
            self._agregar_nota(val)

    def _agregar_nota(self, val):
            # Contador de llamadas a (:)
            self.note_calls += 1

            # --- NUEVA VALIDACIÓN: Bloquear negativos explícitamente ---
            if isinstance(val, int) and val < 0:
                if self.DEBUG: 
                    print(f" [MÚSICA] Nota negativa detectada ({val}). Se ignorará porque no existe sonido negativo.")
                return  # <--- Detenemos la ejecución aquí
            # -----------------------------------------------------------

            # Si llega un entero positivo, convertir a nota string
            if isinstance(val, int):
                val = self._int_a_nota(val)

            if not isinstance(val, str):
                if self.DEBUG: print(f"[DEBUG] nota inválida ignorada: {val}")
                return
                    
            val = val.strip()
            
            # Validar formato con Regex
            if re.match(r'^[A-Ga-g][#b]?\d*$', val):
                self.output_notes.append(val)
                self.note_added += 1
                if self.DEBUG: print(f"[DEBUG] Nota agregada: {val}")
            else:
                if self.DEBUG: print(f"[DEBUG] formato nota inválido: {val}")
    # -----------------------------
    # LILYPOND & TIMIDITY
    # -----------------------------
    def nota_a_lilypond(self, nota: str) -> str:
        nota = nota.strip()
        m = re.match(r'^([A-Ga-g])([#b]?)(\d*)$', nota)
        if not m: return "c" # fallback
        
        letra, alter, oct_str = m.groups()
        octava = int(oct_str) if oct_str else 4
        
        base = letra.lower()
        alter_map = {'#': 'is', 'b': 'es'}
        alter_str = alter_map.get(alter, "")
        
        diff = octava - 3 # Lilypond base c' es C4 (una octava sobre 3)
        suffix = ""
        if diff > 0: suffix = "'" * diff
        elif diff < 0: suffix = "," * abs(diff)
        
        return f"{base}{alter_str}{suffix}"

    def generar_lilypond(self, ruta_ly_abs):
        notas_lp = [self.nota_a_lilypond(n) for n in self.output_notes]
        contenido = r"""\version "2.24.0"
\score {
  \new Staff {
    \tempo 4 = 120
    \absolute {
      %s
    }
  }
  \layout {}
  \midi {}
}
""" % " ".join(notas_lp)
        
        with open(ruta_ly_abs, "w", encoding="utf-8") as f:
            f.write(contenido)
        print(f" LilyPond generado: {ruta_ly_abs}")

    def render_musica(self, base_path_abs):
            """
            Genera audio separando la ruta del directorio del archivo para
            que Timidity no falle con las barras de Windows.
            """
            # 1. Validaciones iniciales
            if not shutil.which("lilypond"):
                print(" Lilypond no instalado.")
                return

            if not shutil.which("timidity"):
                print(" Timidity no instalado.")
                return

            # 2. Generar Partitura (LilyPond)
            try:
                subprocess.run(
                    ["lilypond", os.path.basename(base_path_abs) + ".ly"], 
                    check=True, 
                    cwd=self.OUTPUT_DIR,
                    stdout=subprocess.DEVNULL, # Limpiamos consola
                    stderr=subprocess.DEVNULL
                )
            except Exception as e:
                print(f" Error LilyPond: {e}")
                return

            # 3. Preparar nombres de archivo
            midi_name = os.path.basename(base_path_abs) + ".midi"
            # Lilypond a veces genera .mid o .midi
            if not os.path.exists(os.path.join(self.OUTPUT_DIR, midi_name)):
                midi_name = os.path.basename(base_path_abs) + ".mid"
            
            midi_full = os.path.join(self.OUTPUT_DIR, midi_name)
            wav_full = base_path_abs + ".wav"

            if not os.path.exists(midi_full):
                print(f" MIDI no generado.")
                return

            # 4. VALIDAR Y PREPARAR SOUNDFONT (LA CORRECCIÓN)
            if not os.path.exists(self.SF2_PATH):
                print(f" Error Crítico: No existe {self.SF2_PATH}")
                return

            # --- MAGIA PARA WINDOWS ---
            # Convertimos las barras '\' a '/'
            sf2_dir = os.path.dirname(self.SF2_PATH).replace("\\", "/")
            sf2_file = os.path.basename(self.SF2_PATH)

            # Creamos un archivo de configuración temporal
            # Esto le dice a Timidity explícitamente dónde buscar
            cfg_content = f'dir "{sf2_dir}"\nsoundfont "{sf2_file}"'
            temp_cfg_path = os.path.join(self.OUTPUT_DIR, "temp_timidity.cfg")

            try:
                with open(temp_cfg_path, "w", encoding="utf-8") as f:
                    f.write(cfg_content)
                
                # Ejecutamos Timidity usando ese archivo de configuración (-c)
                subprocess.run(
                    ["timidity", midi_full, "-Ow", "-o", wav_full, "-c", temp_cfg_path], 
                    check=True,
                    stdout=subprocess.DEVNULL, # Silencio si todo va bien
                    stderr=subprocess.PIPE     # Capturamos error si falla
                )
                print(f" WAV generado correctamente: {wav_full}")

            except subprocess.CalledProcessError as e:
                # Si falla, imprimimos el error real de Timidity
                err_msg = e.stderr.decode('utf-8', errors='ignore')
                print(f" Error Timidity: {err_msg}")
            finally:
                # Borramos el archivo temporal
                if os.path.exists(temp_cfg_path):
                    try: os.remove(temp_cfg_path)
                    except: pass

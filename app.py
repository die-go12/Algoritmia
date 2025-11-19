from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
import sys
import os
import io
import uuid
import shutil
import time  # <-- 1. IMPORTAMOS time

# --- IMPORTACIONES DE TU PROYECTO ---
from antlr4 import *
from src.algoritmia.AlgoritmiaLexer import AlgoritmiaLexer
from src.algoritmia.AlgoritmiaParser import AlgoritmiaParser
from src.algoritmia.Executor import AlgoritmiaExecutor 

app = Flask(__name__)
CORS(app) 

# Configuración de carpetas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# -----------------------------------------------------------------
# 2. FUNCIÓN DE MOVIMIENTO SEGURO (A PRUEBA DE RACE CONDITIONS)
# -----------------------------------------------------------------
def safe_move_file(src, dst, max_retries=5, delay=0.3):
    """
    Intenta mover un archivo de forma robusta, reintentando si está bloqueado 
    por otro proceso (Ej: [WinError 32]).
    """
    if not os.path.exists(src):
        return False # El archivo de origen no existe
        
    for i in range(max_retries):
        try:
            # Intento de mover el archivo
            shutil.move(src, dst)
            return True # ¡Éxito!
            
        except PermissionError:
            # [WinError 32] El archivo está bloqueado
            print(f"⚠️ Archivo bloqueado '{os.path.basename(src)}', reintento {i+1}/{max_retries}...")
            time.sleep(delay) # Esperamos un momento a que se libere
            
        except Exception as e:
            # Otro error (ej: disco lleno, etc.)
            print(f"❌ Error crítico moviendo archivo: {e}")
            break # No seguir intentando
            
    # Si se agotan los reintentos
    print(f"❌ No se pudo mover el archivo '{os.path.basename(src)}' después de {max_retries} intentos.")
    return False
# -----------------------------------------------------------------


@app.route("/")
def home():
    return render_template("algoritmia.html")


@app.route("/compile", methods=["POST"])
def compile_algoritmia():
    data = request.get_json()
    code = data.get("code", "")

    if not code.strip():
        return jsonify({"error": "Código vacío"}), 400

    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    try:
        input_stream = InputStream(code)
        lexer = AlgoritmiaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = AlgoritmiaParser(stream)
        tree = parser.programa()

        executor = AlgoritmiaExecutor()
        executor.OUTPUT_DIR = OUTPUT_FOLDER
        executor.DEBUG = False 
        
        executor.visit(tree)
        
        # NOTA: No necesitamos un time.sleep(0.5) aquí
        # porque la función safe_move lo maneja de forma inteligente.

        file_id = str(uuid.uuid4())[:8]
        generated_files = {}
        extensions = ['.pdf', '.wav', '.mid', '.ly']
        
        for ext in extensions:
            src_name = "salida" + ext
            dst_name = file_id + ext
            src_path = os.path.join(OUTPUT_FOLDER, src_name)
            dst_path = os.path.join(OUTPUT_FOLDER, dst_name)
            
            # -----------------------------------------------------------------
            # 3. USAMOS LA FUNCIÓN ROBUSTA EN LUGAR DE shutil.move
            # -----------------------------------------------------------------
            if os.path.exists(src_path):
                # Intentamos mover el archivo de forma segura
                if safe_move_file(src_path, dst_path):
                    # Solo si se movió con éxito, generamos la URL
                    generated_files[ext.replace('.', '')] = f"/download/{dst_name}"
                else:
                    # Si falla después de reintentos, lo marcamos como None
                    generated_files[ext.replace('.', '')] = None
            else:
                generated_files[ext.replace('.', '')] = None

        console_output = new_stdout.getvalue()

        response = {
            "stdout": console_output,
            "pdf": generated_files.get('pdf'),
            "wav": generated_files.get('wav'),
            "midi": generated_files.get('mid'),
            "ly": generated_files.get('ly')
        }
        return jsonify(response)

    except Exception as e:
        sys.stdout = old_stdout
        print(f"Error interno: {e}")
        # Si el error fue al mover, new_stdout puede estar vacío
        return jsonify({"error": str(e), "stdout": new_stdout.getvalue() or "Error en el backend"}), 500
        
    finally:
        sys.stdout = old_stdout

@app.route("/download/<path:filename>")
def download_file(filename):
    # Esto ya está CORRECTO (as_attachment=False)
    return send_from_directory(OUTPUT_FOLDER, filename, as_attachment=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
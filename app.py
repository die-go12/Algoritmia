from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
import sys
import os
import io
import uuid
import shutil
import time 

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
# 2. FUNCIÓN DE MOVIMIENTO SEGURO
# -----------------------------------------------------------------
def safe_move_file(src, dst, max_retries=5, delay=0.3):
    if not os.path.exists(src):
        return False 
    for i in range(max_retries):
        try:
            shutil.move(src, dst)
            return True
        except PermissionError:
            print(f"⚠️ Archivo bloqueado '{os.path.basename(src)}', reintento {i+1}...")
            time.sleep(delay)
        except Exception as e:
            print(f"❌ Error crítico moviendo archivo: {e}")
            break
    return False

@app.route("/")
def home():
    return render_template("algoritmia.html")

@app.route("/compile", methods=["POST"])
def compile_algoritmia():
    data = request.get_json()
    code = data.get("code", "")
    
    # 1. CAPTURAR PARÁMETROS
    entry_point = data.get("entryPoint", "Main").strip()
    if not entry_point: entry_point = "Main"
    
    # --- NUEVO: Capturar el modo debug (booleano) ---
    debug_mode = data.get("debug", False) 
    # ------------------------------------------------

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
        
        # --- NUEVO: Configurar Debug dinámicamente ---
        executor.DEBUG = debug_mode
        if debug_mode:
            print(f"🔧 MODO DEBUG ACTIVADO")
            print(f"⚙️ Entry Point: {entry_point}")
        # ---------------------------------------------
        
        executor.entry_point = entry_point
        executor.output_filename = "salida"
        
        executor.visit(tree)
        
        file_id = str(uuid.uuid4())[:8]
        generated_files = {}
        extensions = ['.pdf', '.wav', '.mid', '.ly']
        
        for ext in extensions:
            src_name = "salida" + ext
            dst_name = f"{entry_point}_{file_id}{ext}"
            
            src_path = os.path.join(OUTPUT_FOLDER, src_name)
            dst_path = os.path.join(OUTPUT_FOLDER, dst_name)
            
            if os.path.exists(src_path):
                if safe_move_file(src_path, dst_path):
                    generated_files[ext.replace('.', '')] = f"/download/{dst_name}"
                else:
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
        # Si hay error en debug, mostramos el stack trace en consola del servidor
        if debug_mode:
            import traceback
            traceback.print_exc()
            
        print(f"Error interno: {e}")
        return jsonify({"error": str(e), "stdout": new_stdout.getvalue() or "Error en el backend"}), 500
        
    finally:
        sys.stdout = old_stdout

@app.route("/download/<path:filename>")
def download_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename, as_attachment=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
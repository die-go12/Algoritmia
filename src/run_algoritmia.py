import os
import subprocess
import shutil

# Directorios base
SRC_DIR = os.path.dirname(__file__)
TEMP_DIR = os.path.join(SRC_DIR, "temp")
MUSIC_DIR = os.path.join(SRC_DIR, "music")
ALGORITMIA_MAIN = os.path.join(SRC_DIR, "algoritmia", "Algoritmia.py")

os.makedirs(MUSIC_DIR, exist_ok=True)

def ejecutar_algoritmia(nombre_alg):
    archivo_alg = os.path.join(TEMP_DIR, nombre_alg)

    if not os.path.isfile(archivo_alg):
        print(f"❌ El archivo {archivo_alg} no existe.")
        return

    # 1️⃣ Ejecutar intérprete de Algoritmia
    try:
        subprocess.run(
            ["python", "-m","algoritmia.main", archivo_alg],
            check=True
        )
    except subprocess.CalledProcessError:
        print("❌ Error al ejecutar el intérprete de Algoritmia.")
        return

    # 2️⃣ Mover archivos generados (.ly, .midi, .pdf)
    base = os.path.splitext(nombre_alg)[0]
    generados = [f"{base}.ly", f"{base}.midi", f"{base}.pdf"]

    for archivo in generados:
        origen = os.path.join(SRC_DIR, archivo)
        destino = os.path.join(MUSIC_DIR, archivo)

        if os.path.exists(origen):
            shutil.move(origen, destino)
            print(f"✔ Movido {archivo} → music/")
        else:
            print(f"⚠ No se generó {archivo}")

    # 3️⃣ Convertir MIDI a WAV
    midi_file = os.path.join(MUSIC_DIR, f"{base}.midi")
    wav_file = os.path.join(MUSIC_DIR, f"{base}.wav")

    if os.path.exists(midi_file):
        try:
            subprocess.run(
                ["timidity", midi_file, "-Ow", "-o", wav_file],
                check=True
            )
            print(f"🎵 WAV generado: {wav_file}")
        except subprocess.CalledProcessError:
            print("❌ Error al generar WAV con Timidity++")
    else:
        print("⚠ No hay MIDI para convertir.")

    print("\n📁 Contenido final en /music:")
    print(os.listdir(MUSIC_DIR))


if __name__ == "__main__":
    print("📄 Archivos .alg disponibles en temp/:")
    for f in os.listdir(TEMP_DIR):
        if f.endswith(".alg"):
            print(" -", f)

    archivo = input("\nIngrese el nombre del archivo .alg a ejecutar: ")
    ejecutar_algoritmia(archivo)

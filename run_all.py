"""
run_all.py
Ejecuta los scripts del proyecto en el orden apropiado:
 - script.py               -> genera comparacion_metodos_swapface_whatsapp.csv
 - script_1.py             -> genera requisitos_sistema_swapface.csv
 - chart_script.py         -> genera swapface_flowchart.png y .svg

Uso: python run_all.py

El script comprueba que las dependencias principales estén instaladas antes de ejecutar.
"""
import subprocess
import sys

REQUIRED = ["pandas", "plotly", "kaleido"]


def check_imports():
    missing = []
    for pkg in REQUIRED:
        try:
            __import__(pkg)
        except Exception:
            missing.append(pkg)
    return missing


def run_script(name):
    print(f"--- Ejecutando {name} ---")
    try:
        res = subprocess.run([sys.executable, name], check=True)
        print(f"{name} finalizó con código {res.returncode}")
    except subprocess.CalledProcessError as e:
        print(f"ERROR: {name} devolvió código {e.returncode}")
        raise
    except FileNotFoundError:
        print(f"ERROR: No se encontró el script {name}")
        raise


def main():
    missing = check_imports()
    if missing:
        print("Faltan paquetes en el entorno actual:", ", ".join(missing))
        print("Instálalos con: python -m pip install -r requirements.txt")
        sys.exit(2)

    # Ejecutar scripts en orden
    try:
        run_script("script.py")
        run_script("script_1.py")
        run_script("chart_script.py")
    except Exception as e:
        print("Ejecución detenida por error:", e)
        sys.exit(1)

    print("\nTodos los scripts se ejecutaron correctamente. Archivos generados:")
    print(" - comparacion_metodos_swapface_whatsapp.csv")
    print(" - requisitos_sistema_swapface.csv")
    print(" - swapface_flowchart.png")
    print(" - swapface_flowchart.svg")


if __name__ == '__main__':
    main()

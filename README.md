# Swapface + WhatsApp — Guía y Scripts

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub repo](https://img.shields.io/badge/GitHub-Swapface--WhatsApp-181717?logo=github)](https://github.com/Joseluiscruz-hub/Swapface-WhatsApp)

Proyecto que genera tablas comparativas, requisitos del sistema y diagramas de flujo para usar Swapface con WhatsApp Desktop.

> **⚠️ Disclaimer:** Este proyecto es solo con fines educativos e informativos. Úsalo de manera responsable y ética. No promovemos el uso de esta tecnología para suplantación de identidad, fraude o cualquier actividad ilegal.

## 🎯 Casos de uso

- **Privacidad:** Mantener anonimato en videollamadas profesionales o personales
- **Entretenimiento:** Crear contenido divertido para redes sociales o streaming
- **Creadores de contenido:** Usar avatares o personajes en videos/streams
- **Pruebas y experimentación:** Explorar tecnologías de face-swap en tiempo real

## 📊 Preview

![Diagrama de flujo Swapface](swapface_flowchart.png)

---

---

## 📁 Archivos principales

- `script.py` — Crea `comparacion_metodos_swapface_whatsapp.csv` (usa pandas)
- `script_1.py` — Crea `requisitos_sistema_swapface.csv` (usa pandas)
- `chart_script.py` — Crea `swapface_flowchart.png` y `swapface_flowchart.svg` (usa plotly + kaleido)
- `requirements.txt` — Dependencias (pandas, plotly, kaleido) con versiones fijadas
- `run_all.py` — Ejecuta los tres scripts en orden (comprobando dependencias)

## ⚙️ Requisitos previos

- Python 3.8+ (recomendado 3.11)
- Windows (instrucciones aquí para cmd.exe / PowerShell)

## 🚀 Instalación y uso (cmd.exe)

**1. Abrir una ventana de cmd y situarse en la carpeta del proyecto:**

```cmd
cd /d "C:\Users\XxGol\Downloads\exported-assets"
```

**2. Crear y activar un entorno virtual (recomendado):**

```cmd
python -m venv .venv
.venv\Scripts\activate
```

**3. Instalar dependencias:**

```cmd
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

**4. Ejecutar todo (genera CSVs y diagramas):**

```cmd
python run_all.py
```

**5. Verificar archivos generados:**

```cmd
dir /b
start comparacion_metodos_swapface_whatsapp.csv
start swapface_flowchart.png
```

## 💻 Instalación y uso (PowerShell)

```powershell
cd "C:\Users\XxGol\Downloads\exported-assets"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python run_all.py
```

## 📝 Notas importantes

- `chart_script.py` utiliza Plotly y `kaleido` para exportar imágenes. Asegúrate de instalar `kaleido` en el mismo entorno virtual donde ejecutas los scripts.
- Si ves errores de "ModuleNotFoundError", activa el venv correcto o instala las dependencias con `python -m pip install -r requirements.txt`.

## � Recursos y referencias

- [Swapface (oficial)](https://swapface.org/) — Software de intercambio de rostros en tiempo real
- [OBS Studio](https://obsproject.com/) — Software de grabación y streaming de código abierto
- [DroidCam](https://www.dev47apps.com/) — Convierte tu teléfono en una cámara web
- [ManyCam](https://manycam.com/) — Software de cámara virtual con efectos
- [Deep Live Cam](https://github.com/hacksider/Deep-Live-Cam) — Alternativa open-source de face-swap

## �📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

**Desarrollado por** [Joseluiscruz-hub](https://github.com/Joseluiscruz-hub)

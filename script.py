
# Crear una tabla comparativa de métodos para usar Swapface con WhatsApp
import pandas as pd

# Datos de comparación
data = {
    'Método': [
        'Swapface + SwapfaceCam (Directo)',
        'Swapface + OBS + DroidCam',
        'Swapface + ManyCam',
        'Deep Live Cam + OBS + DroidCam',
        'WhatsApp Web (Navegador)'
    ],
    'Dificultad': [
        'Fácil',
        'Media',
        'Fácil',
        'Difícil',
        'No compatible'
    ],
    'Compatibilidad WhatsApp Desktop': [
        'Sí (versiones antiguas)',
        'Sí',
        'Sí',
        'Sí',
        'No'
    ],
    'Requiere software adicional': [
        'Solo Swapface',
        'OBS + DroidCam plugin',
        'ManyCam (de pago)',
        'Python + OBS + DroidCam',
        'N/A'
    ],
    'Marca de agua': [
        'Sí (versión gratuita)',
        'Sí (versión gratuita)',
        'Sí (ManyCam gratuito)',
        'No',
        'N/A'
    ],
    'Costo': [
        'Gratis con limitaciones / $39-69 mes',
        'Gratis con limitaciones / $39-69 mes',
        'ManyCam adicional',
        'Gratis',
        'N/A'
    ]
}

df = pd.DataFrame(data)

# Guardar como CSV
df.to_csv('comparacion_metodos_swapface_whatsapp.csv', index=False, encoding='utf-8-sig')

print("Tabla comparativa creada exitosamente")
print(df.to_string(index=False))

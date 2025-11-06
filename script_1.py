
# Crear datos para requisitos del sistema de Swapface
import pandas as pd

requisitos_data = {
    'Componente': [
        'Sistema Operativo',
        'Procesador (Mínimo)',
        'Procesador (Recomendado)',
        'RAM (Mínimo)',
        'RAM (Recomendado)',
        'Tarjeta Gráfica (Mínimo)',
        'Tarjeta Gráfica (Recomendado)',
        'Cámara Web',
        'DirectX'
    ],
    'Especificación': [
        'Windows 10 Anniversary Update o superior',
        'Intel Core i5 9400 o AMD Ryzen 5 2600',
        'Intel Core i5 11400 o AMD Ryzen 5 3600',
        '8 GB',
        '16 GB',
        'NVIDIA GeForce GTX 1060 o AMD Radeon RX 580',
        'NVIDIA GeForce RTX 2070 o AMD Radeon RX 5700',
        '1080p (recomendado para mejores resultados)',
        'DirectX 12 compatible'
    ]
}

df_requisitos = pd.DataFrame(requisitos_data)
df_requisitos.to_csv('requisitos_sistema_swapface.csv', index=False, encoding='utf-8-sig')

print("Requisitos del sistema guardados")
print(df_requisitos.to_string(index=False))

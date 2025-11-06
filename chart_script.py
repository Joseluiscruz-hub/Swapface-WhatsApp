import plotly.graph_objects as go
import plotly.io as pio

# Create a flowchart using Plotly since mermaid service is unavailable
fig = go.Figure()

# Define positions for each step
positions = {
    # Start and common steps
    'inicio': (5, 12),
    'instalar_swapface': (5, 11),
    'decision': (5, 10),
    
    # Method 1 (left path) - SwapfaceCam
    'method1_start': (2, 9),
    'install_swapface_cam': (2, 8),
    'open_swapface': (2, 7),
    'start_virtual_cam': (2, 6),
    'open_whatsapp1': (2, 5),
    'select_swapface_cam': (2, 4),
    
    # Method 2 (right path) - OBS + DroidCam
    'method2_start': (8, 9),
    'install_obs': (8, 8),
    'install_droidcam': (8, 7),
    'configure_swapface': (8, 6),
    'activate_droidcam': (8, 5),
    'open_whatsapp2': (8, 4),
    'select_droidcam': (8, 3),
    
    # Final steps
    'video_call': (5, 2),
    'finish': (5, 1)
}

# Define text labels
labels = {
    'inicio': 'Inicio',
    'instalar_swapface': 'Instalar Swapface en PC',
    'decision': '¿Qué método usar?',
    'method1_start': 'Método 1:<br>SwapfaceCam Directo',
    'install_swapface_cam': 'Instalar SwapfaceCam<br>Virtual Camera',
    'open_swapface': 'Abrir Swapface y<br>seleccionar cara',
    'start_virtual_cam': 'Iniciar cámara<br>virtual',
    'open_whatsapp1': 'Abrir WhatsApp<br>Desktop',
    'select_swapface_cam': 'Seleccionar<br>SwapfaceCam',
    'method2_start': 'Método 2:<br>OBS + DroidCam',
    'install_obs': 'Instalar OBS<br>Studio',
    'install_droidcam': 'Instalar DroidCam<br>plugin',
    'configure_swapface': 'Configurar<br>Swapface',
    'activate_droidcam': 'Activar DroidCam<br>en OBS',
    'open_whatsapp2': 'Abrir WhatsApp<br>Desktop',
    'select_droidcam': 'Seleccionar<br>DroidCam',
    'video_call': 'Realizar videollamada<br>en WhatsApp',
    'finish': '¡Tu cara está<br>intercambiada!'
}

# Define colors for different types of nodes
colors = {
    'start_end': '#DB4545',      # Bright red
    'decision': '#D2BA4C',       # Moderate yellow  
    'method1': '#1FB8CD',        # Strong cyan
    'method2': '#2E8B57',        # Sea green
    'common': '#5D878F'          # Cyan
}

# Define node types
node_types = {
    'inicio': 'start_end',
    'finish': 'start_end',
    'decision': 'decision',
    'instalar_swapface': 'common',
    'video_call': 'common',
    'method1_start': 'method1',
    'install_swapface_cam': 'method1',
    'open_swapface': 'method1',
    'start_virtual_cam': 'method1',
    'open_whatsapp1': 'method1',
    'select_swapface_cam': 'method1',
    'method2_start': 'method2',
    'install_obs': 'method2',
    'install_droidcam': 'method2',
    'configure_swapface': 'method2',
    'activate_droidcam': 'method2',
    'open_whatsapp2': 'method2',
    'select_droidcam': 'method2'
}

# Add boxes for each step
for step, (x, y) in positions.items():
    node_type = node_types[step]
    color = colors[node_type]
    
    # Add rectangle
    fig.add_shape(
        type="rect",
        x0=x-0.8, y0=y-0.4, x1=x+0.8, y1=y+0.4,
        fillcolor=color,
        line=dict(color="black", width=2),
        opacity=0.8
    )
    
    # Add text
    fig.add_annotation(
        x=x, y=y,
        text=labels[step],
        showarrow=False,
        font=dict(color="white", size=11, family="Arial Black"),
        align="center"
    )

# Define arrows
arrows = [
    ('inicio', 'instalar_swapface'),
    ('instalar_swapface', 'decision'),
    ('decision', 'method1_start'),
    ('decision', 'method2_start'),
    
    # Method 1 flow
    ('method1_start', 'install_swapface_cam'),
    ('install_swapface_cam', 'open_swapface'),
    ('open_swapface', 'start_virtual_cam'),
    ('start_virtual_cam', 'open_whatsapp1'),
    ('open_whatsapp1', 'select_swapface_cam'),
    ('select_swapface_cam', 'video_call'),
    
    # Method 2 flow
    ('method2_start', 'install_obs'),
    ('install_obs', 'install_droidcam'),
    ('install_droidcam', 'configure_swapface'),
    ('configure_swapface', 'activate_droidcam'),
    ('activate_droidcam', 'open_whatsapp2'),
    ('open_whatsapp2', 'select_droidcam'),
    ('select_droidcam', 'video_call'),
    
    ('video_call', 'finish')
]

# Add arrows
for start, end in arrows:
    x1, y1 = positions[start]
    x2, y2 = positions[end]
    
    # Calculate arrow position
    if start == 'decision' and end == 'method1_start':
        # Decision to method 1 (diagonal left)
        x1, y1 = x1-0.4, y1-0.4
        x2, y2 = x2+0.4, y2+0.4
    elif start == 'decision' and end == 'method2_start':
        # Decision to method 2 (diagonal right)
        x1, y1 = x1+0.4, y1-0.4
        x2, y2 = x2-0.4, y2+0.4
    elif start == 'select_swapface_cam' and end == 'video_call':
        # Method 1 to final (diagonal right)
        x1, y1 = x1+0.4, y1-0.4
        x2, y2 = x2-0.4, y2+0.4
    elif start == 'select_droidcam' and end == 'video_call':
        # Method 2 to final (diagonal left)
        x1, y1 = x1-0.4, y1-0.4
        x2, y2 = x2+0.4, y2+0.4
    else:
        # Vertical arrows
        if y1 > y2:  # Downward
            y1 -= 0.4
            y2 += 0.4
        else:  # Upward
            y1 += 0.4
            y2 -= 0.4
    
    fig.add_annotation(
        x=x2, y=y2,
        ax=x1, ay=y1,
        xref="x", yref="y",
        axref="x", ayref="y",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="black",
        showarrow=True
    )

# Add method labels
fig.add_annotation(
    x=2, y=9.5,
    text="MÉTODO 1",
    showarrow=False,
    font=dict(color="#1FB8CD", size=14, family="Arial Black"),
    align="center"
)

fig.add_annotation(
    x=8, y=9.5,
    text="MÉTODO 2",
    showarrow=False,
    font=dict(color="#2E8B57", size=14, family="Arial Black"),
    align="center"
)

# Update layout
fig.update_layout(
    title="Proceso Swapface con WhatsApp Desktop",
    xaxis=dict(range=[0, 10], showgrid=False, showticklabels=False, zeroline=False),
    yaxis=dict(range=[0, 13], showgrid=False, showticklabels=False, zeroline=False),
    showlegend=False,
    plot_bgcolor='white',
    font=dict(size=12)
)

# Save as PNG and SVG
fig.write_image("swapface_flowchart.png")
fig.write_image("swapface_flowchart.svg", format="svg")

print("Flowchart created successfully!")
print("Files saved: swapface_flowchart.png, swapface_flowchart.svg")
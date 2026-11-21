# -*- coding: utf-8 -*-
"""
Generador de la imagen ejecutiva del Diagrama de Ishikawa (6M) para Taranis Black
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import textwrap

def render_ishikawa():
    fig, ax = plt.subplots(figsize=(18, 11), dpi=300)
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')

    # Title
    fig.text(0.04, 0.95, "TARANIS BLACK | DIAGRAMA DE ISHIKAWA (CAUSA Y EFECTO — LAS 6M)", 
             fontsize=18, fontweight='bold', color='#ffffff', family='sans-serif')
    fig.text(0.04, 0.92, "Análisis Causal del Retraso de 5 Días en Facturación y Cierre Contable  |  Ruta 4: Finanzas & Operaciones", 
             fontsize=11, color='#f59e0b', family='sans-serif')

    # Spine (Central Arrow)
    ax.annotate('', xy=(9.2, 5.0), xytext=(0.5, 5.0),
                arrowprops=dict(arrowstyle="-|>", color='#64748b', lw=5, mutation_scale=25))

    # Effect Box (Fish Head)
    head_box = patches.FancyBboxPatch((9.2, 4.0), 2.5, 2.0, boxstyle="round,pad=0.1",
                                      fc='#450a0a', ec='#ef4444', lw=2.5)
    ax.add_patch(head_box)
    
    fig.text(0.795, 0.53, "EFECTO CRÍTICO:", fontsize=10, fontweight='bold', color='#fca5a5', family='sans-serif')
    ef_text = "Retraso crónico de 5 días en cierre contable y facturación.\nErosión de USD 4.08M en EBITDA anual."
    fig.text(0.795, 0.46, ef_text, fontsize=8.5, color='#ffffff', family='sans-serif', wrap=True)

    # 6 Branches (3 Top, 3 Bottom)
    # Top: Método (x=2.2), Máquina (x=5.0), Mano de Obra (x=7.8)
    # Bottom: Material (x=2.2), Medición (x=5.0), Medio Ambiente (x=7.8)
    
    categories = [
        # Top 3
        {
            "name": "1. METODO (Procesos)",
            "x_start": 1.2, "y_start": 8.6, "x_end": 2.6, "y_end": 5.0,
            "color": "#f59e0b",
            "causes": [
                "- Flujo 100% dependiente de emails informales.",
                "- Ausencia de POP documentado y auditable.",
                "- Sin matriz de alzada automatica (todo a gerencia).",
                "- Regla CIF/FOB no verificada al cierre comercial."
            ]
        },
        {
            "name": "2. MAQUINA (Sistemas)",
            "x_start": 4.0, "y_start": 8.6, "x_end": 5.4, "y_end": 5.0,
            "color": "#38bdf8",
            "causes": [
                "- ERP legado obsoleto y sin integracion por APIs.",
                "- Cero tecnologia OCR/IA para lectura de PDFs.",
                "- Dependencia critica de 3 Excels locales.",
                "- Consulta manual externa al portal Serasa (40 min)."
            ]
        },
        {
            "name": "3. MANO DE OBRA (Personas)",
            "x_start": 6.8, "y_start": 8.6, "x_end": 8.2, "y_end": 5.0,
            "color": "#10b981",
            "causes": [
                "- Asistentes sobrecargados con copiar y pegar.",
                "- Sindrome de burnout y rotacion en fin de mes.",
                "- Gerente ausente por comites (embudo de alzada).",
                "- Tareas mecanicas que impiden analisis de riesgo."
            ]
        },
        # Bottom 3
        {
            "name": "4. MATERIAL (Insumos)",
            "x_start": 1.2, "y_start": 1.4, "x_end": 2.6, "y_end": 5.0,
            "color": "#a855f7",
            "causes": [
                "- Propuestas con campos vacios de vendedores.",
                "- Codigos divergentes entre catalogo y ERP.",
                "- Domicilios fiscales no actualizados del cliente.",
                "- Fichas tecnicas desactualizadas en ventas."
            ]
        },
        {
            "name": "5. MEDICION (Metricas)",
            "x_start": 4.0, "y_start": 1.4, "x_end": 5.4, "y_end": 5.0,
            "color": "#ec4899",
            "causes": [
                "- Cero monitoreo de SLAs en tiempo real.",
                "- Direccion General se entera a mes cerrado.",
                "- Falta de visibilidad de pedidos retenidos.",
                "- Sin alertas tempranas de morosidad B2B."
            ]
        },
        {
            "name": "6. MEDIO AMBIENTE (Cultura)",
            "x_start": 6.8, "y_start": 1.4, "x_end": 8.2, "y_end": 5.0,
            "color": "#6366f1",
            "causes": [
                "- Distancia fisica y friccion Sao Paulo vs. CD Joinville.",
                "- Cultura reactiva de 'apagar incendios'.",
                "- Culpas cruzadas entre Finanzas, Ventas y CD.",
                "- Presion comercial extrema en cierre de trimestre."
            ]
        }
    ]

    for cat in categories:
        # Branch line
        ax.annotate('', xy=(cat["x_end"], cat["y_end"]), xytext=(cat["x_start"] + 1.0, cat["y_start"]),
                    arrowprops=dict(arrowstyle="-|>", color=cat["color"], lw=3.0, mutation_scale=15))
        
        # Header Box
        h_box = patches.FancyBboxPatch((cat["x_start"] - 0.2, cat["y_start"] - 0.15), 2.5, 0.45,
                                       boxstyle="round,pad=0.04", fc='#1e293b', ec=cat["color"], lw=1.5)
        ax.add_patch(h_box)
        ax.text(cat["x_start"] + 1.05, cat["y_start"] + 0.08, cat["name"], 
                fontsize=9.5, fontweight='bold', color='#ffffff', ha='center', va='center', family='sans-serif')
        
        # Causes text block
        text_y = cat["y_start"] - 0.5 if cat["y_start"] > 5 else cat["y_start"] + 0.5
        y_step = -0.26 if cat["y_start"] > 5 else 0.26
        
        for c_idx, cause in enumerate(cat["causes"]):
            cy = text_y + c_idx * y_step
            ax.text(cat["x_start"] - 0.1, cy, cause, fontsize=8, color='#cbd5e1', family='sans-serif')

    ax.set_xlim(0, 12)
    ax.set_ylim(0.5, 9.5)
    ax.axis('off')

    # Footer
    fig.text(0.04, 0.02, "Estudiante: Francisco Israel Mesillas Hernández  |  israel.mecillas@gmail.com  |  Ruta 4: Finanzas & Operaciones  |  Alura & Oracle Next Education (G11)", 
             fontsize=8.5, color='#64748b', family='sans-serif')

    out1 = r"C:\Users\52477\Desktop\challengeAIbuilder\diagrama_ishikawa_taranis_black.png"
    out2 = r"C:\Users\52477\Desktop\challengeAIbuilder\02_Diagnostico_Lean_Operaciones\diagrama_ishikawa_taranis_black.png"
    plt.savefig(out1, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.savefig(out2, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print("Ishikawa Image generated successfully!")

if __name__ == '__main__':
    render_ishikawa()

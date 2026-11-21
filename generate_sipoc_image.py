# -*- coding: utf-8 -*-
"""
Generador de la imagen de alta resolución para la Matriz SIPOC de Taranis Black
(Ruta 4: Finanzas y Operaciones - ONE G11)
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def generate_sipoc():
    fig, ax = plt.subplots(figsize=(15, 9.5), dpi=300)
    fig.patch.set_facecolor('#0f172a') # Dark slate background
    ax.set_facecolor('#0f172a')
    
    # Header Information
    fig.text(0.05, 0.94, "TARANIS BLACK | MATRIZ SIPOC DEL MACROPROCESO (LEAN SIX SIGMA)", 
             fontsize=16, fontweight='bold', color='#f8fafc', family='sans-serif')
    fig.text(0.05, 0.91, "Flujo As-Is: Aprobación de Pedidos, Facturación y Expedición B2B  |  Especialización: Finanzas & Operaciones (ONE G11)", 
             fontsize=10.5, color='#38bdf8', family='sans-serif')

    # Top KPI Diagnostic Bar
    kpi_bar = patches.FancyBboxPatch((0.05, 0.82), 0.90, 0.065, boxstyle="round,pad=0.01",
                                     fc='#1e293b', ec='#334155', transform=fig.transFigure)
    fig.patches.append(kpi_bar)
    
    fig.text(0.08, 0.84, "TIEMPO DE CICLO ACTUAL (LEAD TIME): >5 Días Hábiles (~2,400 min)", 
             fontsize=9.5, fontweight='bold', color='#f43f5e', family='sans-serif')
    fig.text(0.42, 0.84, "TIEMPO DE VALOR AGREGADO: ~65 min", 
             fontsize=9.5, fontweight='bold', color='#10b981', family='sans-serif')
    fig.text(0.68, 0.84, "EFICIENCIA DEL FLUJO (PCE): 2.7% (97.3% Desperdicio/Muda)", 
             fontsize=9.5, fontweight='bold', color='#f59e0b', family='sans-serif')

    # 5 Column Definitions
    col_width = 1.82
    gap = 0.15
    start_x = 0.1
    y_top = 8.0
    
    columns_data = [
        {
            "letter": "S",
            "name": "Suppliers\n(Proveedores)",
            "color": "#6366f1",
            "header_bg": "#312e81",
            "items": [
                ("Consultores B2B & SDRs (São Paulo)", "Emiten y envían propuestas comerciales firmadas en PDF vía email manual."),
                ("Clientes Corporativos (Compradores B2B)", "Facilitan datos fiscales (CNPJ, IE, Dirección fiscal de entrega)."),
                ("Buró de Crédito (Serasa Experian)", "Proveedor de score crediticio, deudas activas y protestas comerciales."),
                ("Gerente Financiero (Aprobador)", "Valida discrecionalmente los límites de crédito de cada orden de compra.")
            ]
        },
        {
            "letter": "I",
            "name": "Inputs\n(Entradas)",
            "color": "#0ea5e9",
            "header_bg": "#075985",
            "items": [
                ("Propuesta Comercial en PDF Escaneado", "No estructurada, enviada por correo informal sin validación previa."),
                ("Ficha Fiscal y Padrón Tributario", "Tarjeta de CNPJ, comprobante de domicilio e Inscripción Estatal."),
                ("Score y Reporte Serasa", "Consulta manual externa de 40 min en el portal web de Serasa."),
                ("Excel 'Controle_Limites_2026.xlsx'", "Hoja de cálculo local desincronizada utilizada para verificar cupos.")
            ]
        },
        {
            "letter": "P",
            "name": "Process\n(Macroproceso As-Is)",
            "color": "#f59e0b",
            "header_bg": "#78350f",
            "items": [
                ("Paso 1: Recepción en Email", ">40 correos/día sin prioridad ni validación de inventario. (Espera: 2-4h)."),
                ("Paso 2: Consulta Manual Crédito", "Asistente alterna entre 3 ventanas (ERP, Serasa, Excel). (Ciclo: 40 min)."),
                ("Paso 3-4: Espera Gerente (CUELLO)", "Retención en bandeja de entrada por comités y viajes. (Retención: 24h-48h)."),
                ("Paso 5: Facturación & Picking", "Copia manual al ERP (6.8% error) y correo manual al CD Joinville. (Espera: 24h).")
            ]
        },
        {
            "letter": "O",
            "name": "Outputs\n(Salidas)",
            "color": "#10b981",
            "header_bg": "#064e3b",
            "items": [
                ("Orden en Cola no Estructurada", "Correo en bandeja de entrada sin prioridad comercial clara."),
                ("Dossier Preliminar en Excel Local", "Resumen de crédito en hoja no sincronizada con el ERP core."),
                ("Autorización por Email ('De acuerdo')", "Respuesta informal del gerente sin registro auditable."),
                ("NF-e, Boletos y Picking List", "DANFE, XML, boletos a 30/60/90 y orden de expedición al CD Joinville.")
            ]
        },
        {
            "letter": "C",
            "name": "Customers\n(Clientes)",
            "color": "#a855f7",
            "header_bg": "#581c87",
            "items": [
                ("Asistente Financiero de Crédito", "Cliente interno del correo inicial de ventas."),
                ("Gerente Financiero (Alzada)", "Cliente interno que recibe el resumen para autorizar crédito."),
                ("Equipo de Facturación y Contabilidad", "Cliente interno que emite la factura y concilia los asientos."),
                ("Cliente Corporativo & CD Joinville", "Clientes finales que reciben la mercancía y padecen los retrasos.")
            ]
        }
    ]

    for idx, col in enumerate(columns_data):
        cx = start_x + idx * (col_width + gap)
        
        # Column Header Box
        head_box = patches.FancyBboxPatch((cx, y_top), col_width, 1.1, boxstyle="round,pad=0.08",
                                          fc=col["header_bg"], ec=col["color"], lw=2)
        ax.add_patch(head_box)
        
        # Badge Letter
        badge = patches.Circle((cx + 0.35, y_top + 0.55), 0.28, fc=col["color"], ec='#ffffff', lw=1.5)
        ax.add_patch(badge)
        ax.text(cx + 0.35, y_top + 0.55, col["letter"], fontsize=13, fontweight='bold', 
                color='#0f172a', ha='center', va='center', family='sans-serif')
        
        # Header Text
        ax.text(cx + 0.75, y_top + 0.55, col["name"], fontsize=10.5, fontweight='bold', 
                color='#ffffff', va='center', family='sans-serif')

        # Cards inside Column
        card_y = y_top - 0.25
        card_height = 1.45
        card_gap = 0.22
        
        for item_title, item_desc in col["items"]:
            card_y -= card_height
            
            # Determine card background (highlight process bottlenecks)
            is_bottleneck = "CUELLO" in item_title
            bg_color = "#3b1318" if is_bottleneck else "#1e293b"
            border_color = "#f43f5e" if is_bottleneck else "#334155"
            
            card_box = patches.FancyBboxPatch((cx, card_y), col_width, card_height - 0.05, 
                                              boxstyle="round,pad=0.06",
                                              fc=bg_color, ec=border_color, lw=1.2)
            ax.add_patch(card_box)
            
            # Card Title
            title_color = "#fb7185" if is_bottleneck else "#f8fafc"
            ax.text(cx + 0.1, card_y + card_height - 0.28, item_title, 
                    fontsize=8.5, fontweight='bold', color=title_color, family='sans-serif')
            
            # Card Description
            ax.text(cx + 0.1, card_y + card_height - 0.55, item_desc, 
                    fontsize=7.3, color='#94a3b8', family='sans-serif', wrap=True)
            
            card_y -= card_gap

    # Flow arrows connecting columns
    for i in range(4):
        arrow_x = start_x + (i + 1) * col_width + i * gap + gap/2
        ax.annotate('', xy=(arrow_x + 0.06, y_top + 0.55), xytext=(arrow_x - 0.06, y_top + 0.55),
                    arrowprops=dict(arrowstyle="->", color='#64748b', lw=2.5))

    # Axis Limits
    ax.set_xlim(0, 10)
    ax.set_ylim(0.5, 9.5)
    ax.axis('off')

    # Footer Metadata
    fig.text(0.05, 0.03, "Estudiante: Francisco Israel Mesillas Hernández  |  israel.mecillas@gmail.com  |  Ruta 4: Finanzas & Operaciones  |  Alura & Oracle Next Education (G11)", 
             fontsize=8.5, color='#64748b', family='sans-serif')

    # Save PNG files
    out_root = r"C:\Users\52477\Desktop\challengeAIbuilder\matriz_sipoc_taranis_black.png"
    out_lean = r"C:\Users\52477\Desktop\challengeAIbuilder\02_Diagnostico_Lean_Operaciones\matriz_sipoc_taranis_black.png"
    out_art = r"C:\Users\52477\.gemini\antigravity\brain\65b23f9f-a310-40e5-923f-54f1f937153f\matriz_sipoc_taranis_black.png"

    plt.savefig(out_root, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.savefig(out_lean, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.savefig(out_art, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    
    print(f"SIPOC Image generated at:\n- {out_root}\n- {out_lean}\n- {out_art}")

if __name__ == '__main__':
    generate_sipoc()

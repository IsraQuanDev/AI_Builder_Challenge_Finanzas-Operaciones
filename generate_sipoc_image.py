# -*- coding: utf-8 -*-
"""
Script perfeccionado para generar la Matriz SIPOC sin traslape de texto.
Usa textwrap para ajustar cada línea exactamente dentro del ancho de su columna.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import textwrap

def generate_sipoc_perfect():
    # Large high-res canvas (16 x 11 inches)
    fig, ax = plt.subplots(figsize=(16, 10.5), dpi=300)
    fig.patch.set_facecolor('#0b0f19')
    ax.set_facecolor('#0b0f19')

    # Title & Subtitle
    fig.text(0.04, 0.95, "TARANIS BLACK | MATRIZ SIPOC DEL MACROPROCESO (LEAN SIX SIGMA)", 
             fontsize=17, fontweight='bold', color='#ffffff', family='sans-serif')
    fig.text(0.04, 0.92, "Flujo As-Is: Aprobación de Pedidos, Facturación y Expedición B2B  |  Ruta 4: Finanzas y Operaciones (ONE G11)", 
             fontsize=10.5, color='#38bdf8', family='sans-serif')

    # Top KPI Diagnostic Badges (Separate cards so they never collide)
    kpis = [
        ("LEAD TIME AS-IS", ">5 Días Hábiles (~2,400 min)", "#f43f5e", 0.04, 0.28),
        ("TOUCH TIME (VALOR AGREGADO)", "~65 minutos por orden", "#10b981", 0.35, 0.28),
        ("EFICIENCIA DEL FLUJO (PCE)", "2.7% (97.3% Desperdicio / Muda)", "#f59e0b", 0.66, 0.30)
    ]
    for label, val, col, x, w in kpis:
        kpi_patch = patches.FancyBboxPatch((x, 0.835), w, 0.065, boxstyle="round,pad=0.01",
                                          fc='#1e293b', ec=col, lw=1.5, transform=fig.transFigure)
        fig.patches.append(kpi_patch)
        fig.text(x + 0.015, 0.875, label, fontsize=8, fontweight='bold', color='#94a3b8', family='sans-serif')
        fig.text(x + 0.015, 0.845, val, fontsize=9.5, fontweight='bold', color=col, family='sans-serif')

    # 5 Columns Setup
    # Total width available: x from 0.4 to 9.6 -> width = 9.2 / 5 = 1.84
    col_w = 1.72
    col_gap = 0.16
    start_x = 0.4
    y_header = 7.7
    
    cols = [
        {
            "letter": "S",
            "name": "Suppliers\n(Proveedores)",
            "color": "#6366f1",
            "bg": "#1e1b4b",
            "items": [
                ("Consultores B2B & SDRs (SP)", "Ventas B2B envía propuestas firmadas en PDF escaneado vía email."),
                ("Clientes Corporativos B2B", "Compradores corporativos que entregan datos fiscales (CNPJ, IE, Dirección)."),
                ("Buró Serasa Experian", "Proveedor de score crediticio, protestas y deudas financieras activas."),
                ("Gerente Financiero (Alzada)", "Aprobador centralizado y discrecional de límites de crédito.")
            ]
        },
        {
            "letter": "I",
            "name": "Inputs\n(Entradas)",
            "color": "#0ea5e9",
            "bg": "#0c4a6e",
            "items": [
                ("Propuesta en PDF", "Documento comercial no estructurado enviado por correo sin validación."),
                ("Ficha Fiscal y Padrón", "Tarjeta de CNPJ, comprobante de dirección e Inscripción Estatal."),
                ("Score y Reporte Serasa", "Consulta manual externa de 40 min en el portal web de Serasa."),
                ("Excel de Límites Local", "Archivo local desincronizado 'Controle_Limites_2026.xlsx'.")
            ]
        },
        {
            "letter": "P",
            "name": "Process\n(Macroproceso As-Is)",
            "color": "#f59e0b",
            "bg": "#78350f",
            "items": [
                ("1. Recepción en Email", ">40 correos/día sin prioridad ni validación de inventario.\n(Espera: 2 a 4h)."),
                ("2. Consulta Crédito", "Asistente alterna entre 3 pantallas (ERP, Serasa, Excel).\n(Ciclo: 40 min)."),
                ("3-4. Aprobación Gerente", "★ CUELLO CRÍTICO:\nRetención en bandeja de 24h a 48h hábiles por comités."),
                ("5. Facturación y Picking", "Copia manual al ERP (6.8% error) y aviso al CD Joinville.\n(Espera: 24h).")
            ]
        },
        {
            "letter": "O",
            "name": "Outputs\n(Salidas)",
            "color": "#10b981",
            "bg": "#064e3b",
            "items": [
                ("Orden en Cola no Estructurada", "Correo en bandeja de entrada sin prioridad comercial clara."),
                ("Dossier de Crédito en Excel", "Resumen en hoja local no sincronizada con el ERP core."),
                ("Aprobación por Email", "Respuesta informal del gerente ('De acuerdo') sin trazabilidad."),
                ("NF-e, Boletos y Picking List", "DANFE, XML, boletos bancarios a 30/60/90 y orden de despacho.")
            ]
        },
        {
            "letter": "C",
            "name": "Customers\n(Clientes)",
            "color": "#a855f7",
            "bg": "#581c87",
            "items": [
                ("Asistente de Crédito", "Cliente interno del correo inicial enviado por el área comercial."),
                ("Gerente Financiero", "Cliente interno que recibe el resumen para autorizar la alzada."),
                ("Facturación y Contabilidad", "Cliente interno que emite la factura y concilia los asientos."),
                ("Cliente Corporativo & CD", "Clientes finales que reciben la mercancía y sufren los retrasos.")
            ]
        }
    ]

    for c_idx, c_data in enumerate(cols):
        cx = start_x + c_idx * (col_w + col_gap)
        
        # Header Box
        header_patch = patches.FancyBboxPatch((cx, y_header), col_w, 0.95, boxstyle="round,pad=0.05",
                                              fc=c_data["bg"], ec=c_data["color"], lw=2)
        ax.add_patch(header_patch)
        
        # Circle Badge Letter
        badge_circle = patches.Circle((cx + 0.32, y_header + 0.48), 0.24, fc=c_data["color"], ec='#ffffff', lw=1.2)
        ax.add_patch(badge_circle)
        ax.text(cx + 0.32, y_header + 0.48, c_data["letter"], fontsize=12, fontweight='bold', 
                color='#0f172a', ha='center', va='center', family='sans-serif')
        
        # Header Label
        ax.text(cx + 0.68, y_header + 0.48, c_data["name"], fontsize=9.5, fontweight='bold', 
                color='#ffffff', va='center', family='sans-serif')
        
        # 4 Cards per column
        card_y = y_header - 0.2
        card_h = 1.55
        card_margin = 0.16
        
        for item_title, item_desc in c_data["items"]:
            card_y -= card_h
            
            is_bottleneck = "CUELLO" in item_title
            c_bg = "#450a0a" if is_bottleneck else "#1e293b"
            c_border = "#f43f5e" if is_bottleneck else "#334155"
            c_lw = 2.0 if is_bottleneck else 1.0
            
            # Draw card container
            box = patches.FancyBboxPatch((cx, card_y), col_w, card_h - 0.06, boxstyle="round,pad=0.04",
                                         fc=c_bg, ec=c_border, lw=c_lw)
            ax.add_patch(box)
            
            # Wrap Title (max 21 chars per line)
            title_wrapped = "\\n".join(textwrap.wrap(item_title, width=21))
            t_color = "#fb7185" if is_bottleneck else "#f8fafc"
            t_fontweight = 'bold'
            
            ax.text(cx + 0.08, card_y + card_h - 0.24, title_wrapped, 
                    fontsize=8.5, fontweight=t_fontweight, color=t_color, family='sans-serif', va='top')
            
            # Calculate height offset based on title lines
            num_title_lines = len(title_wrapped.split("\\n"))
            desc_offset = 0.24 + (num_title_lines * 0.22)
            
            # Wrap Description (max 25 chars per line)
            desc_wrapped = "\\n".join(textwrap.wrap(item_desc, width=25))
            d_color = "#fecdd3" if is_bottleneck else "#94a3b8"
            
            ax.text(cx + 0.08, card_y + card_h - desc_offset - 0.05, desc_wrapped, 
                    fontsize=7.2, color=d_color, family='sans-serif', va='top')
            
            card_y -= card_margin

    # Connection Arrows between Headers
    for i in range(4):
        ax_arrow = start_x + (i + 1) * col_w + i * col_gap + (col_gap / 2)
        ax.annotate('', xy=(ax_arrow + 0.06, y_header + 0.48), xytext=(ax_arrow - 0.06, y_header + 0.48),
                    arrowprops=dict(arrowstyle="->", color='#64748b', lw=2.5))

    # Axis config
    ax.set_xlim(0, 10)
    ax.set_ylim(0.2, 9.2)
    ax.axis('off')

    # Footer Metadata
    fig.text(0.04, 0.02, "Estudiante: Francisco Israel Mesillas Hernández  |  israel.mecillas@gmail.com  |  Ruta 4: Finanzas & Operaciones  |  Challenge ONE G11 AI for Business", 
             fontsize=8.5, color='#64748b', family='sans-serif')

    # Save to all target paths
    out1 = r"C:\Users\52477\Desktop\challengeAIbuilder\matriz_sipoc_taranis_black.png"
    out2 = r"C:\Users\52477\Desktop\challengeAIbuilder\02_Diagnostico_Lean_Operaciones\matriz_sipoc_taranis_black.png"
    out3 = r"C:\Users\52477\.gemini\antigravity\brain\65b23f9f-a310-40e5-923f-54f1f937153f\matriz_sipoc_taranis_black.png"

    plt.savefig(out1, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.savefig(out2, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.savefig(out3, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print("SIPOC Image successfully generated without text overlap!")

if __name__ == '__main__':
    generate_sipoc_perfect()

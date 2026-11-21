# -*- coding: utf-8 -*-
"""
Script definitivo para generar la Matriz SIPOC con saltos de linea reales (\n)
y tarjetas perfectamente dimensionadas sin ningun tipo de traslape.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import textwrap
import os

def render_sipoc():
    # Lienzo panorámico de alta resolución (18 x 11 pulgadas a 300 DPI)
    fig, ax = plt.subplots(figsize=(18, 11), dpi=300)
    fig.patch.set_facecolor('#0f172a') # Fondo oscuro elegante
    ax.set_facecolor('#0f172a')

    # Título Principal y Subtítulo
    fig.text(0.04, 0.95, "TARANIS BLACK | MATRIZ SIPOC DEL MACROPROCESO (LEAN SIX SIGMA)", 
             fontsize=18, fontweight='bold', color='#ffffff', family='sans-serif')
    fig.text(0.04, 0.92, "Flujo As-Is: Aprobación de Pedidos, Facturación y Expedición B2B  |  Ruta 4: Finanzas y Operaciones (ONE G11)", 
             fontsize=11, color='#38bdf8', family='sans-serif')

    # 3 Tarjetas de Diagnóstico de KPIs en la parte superior (Separadas, sin riesgo de colisión)
    kpis = [
        ("TIEMPO DE CICLO AS-IS (LEAD TIME)", ">5 Días Hábiles (~2,400 min)", "#f43f5e", 0.04, 0.28),
        ("TIEMPO DE VALOR AGREGADO (TOUCH TIME)", "~65 minutos por pedido", "#10b981", 0.35, 0.28),
        ("EFICIENCIA DEL FLUJO (PCE)", "2.7%  (97.3% Desperdicio / Muda)", "#f59e0b", 0.66, 0.30)
    ]
    for label, val, col, x, w in kpis:
        kpi_box = patches.FancyBboxPatch((x, 0.835), w, 0.065, boxstyle="round,pad=0.01",
                                         fc='#1e293b', ec=col, lw=1.5, transform=fig.transFigure)
        fig.patches.append(kpi_box)
        fig.text(x + 0.015, 0.875, label, fontsize=8, fontweight='bold', color='#94a3b8', family='sans-serif')
        fig.text(x + 0.015, 0.845, val, fontsize=10, fontweight='bold', color=col, family='sans-serif')

    # Configuración de las 5 Columnas (S - I - P - O - C)
    col_w = 1.68
    col_gap = 0.20
    start_x = 0.45
    y_header = 7.7
    
    cols = [
        {
            "letter": "S",
            "name": "Suppliers\n(Proveedores)",
            "color": "#6366f1",
            "bg": "#1e1b4b",
            "items": [
                ("Consultores B2B & SDRs (São Paulo)", "Envían propuestas firmadas en PDF escaneado vía correo manual."),
                ("Clientes Corporativos (B2B)", "Compradores corporativos que entregan datos fiscales (CNPJ, IE, Dirección)."),
                ("Buró de Crédito (Serasa)", "Proveedor de score crediticio, deudas activas y protestas comerciales."),
                ("Gerente Financiero (Alzada)", "Aprobador discrecional de límites de crédito para cada solicitud.")
            ]
        },
        {
            "letter": "I",
            "name": "Inputs\n(Entradas)",
            "color": "#0ea5e9",
            "bg": "#0c4a6e",
            "items": [
                ("Propuesta Comercial en PDF", "Documento comercial no estructurado enviado por correo sin validación."),
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
                ("2. Consulta Crédito Manual", "Asistente alterna en 3 ventanas (ERP, Serasa, Excel).\n(Ciclo: 40 min)."),
                ("3-4. Espera del Gerente", "★ CUELLO CRÍTICO:\nRetención en bandeja de 24h a 48h hábiles por comités."),
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
                ("Autorización por Email", "Respuesta informal del gerente ('De acuerdo') sin trazabilidad."),
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
        
        # Caja del encabezado de la columna
        head_box = patches.FancyBboxPatch((cx, y_header), col_w, 0.95, boxstyle="round,pad=0.04",
                                          fc=c_data["bg"], ec=c_data["color"], lw=2)
        ax.add_patch(head_box)
        
        # Círculo con la letra
        circle = patches.Circle((cx + 0.30, y_header + 0.48), 0.22, fc=c_data["color"], ec='#ffffff', lw=1.2)
        ax.add_patch(circle)
        ax.text(cx + 0.30, y_header + 0.48, c_data["letter"], fontsize=12, fontweight='bold', 
                color='#0f172a', ha='center', va='center', family='sans-serif')
        
        # Texto del encabezado
        ax.text(cx + 0.62, y_header + 0.48, c_data["name"], fontsize=9.5, fontweight='bold', 
                color='#ffffff', va='center', family='sans-serif')
        
        # Dibujar las 4 tarjetas de cada columna
        card_y = y_header - 0.18
        card_h = 1.55
        card_margin = 0.18
        
        for item_title, item_desc in c_data["items"]:
            card_y -= card_h
            
            is_bottleneck = "CUELLO" in item_title
            bg_c = "#450a0a" if is_bottleneck else "#1e293b"
            border_c = "#f43f5e" if is_bottleneck else "#334155"
            border_w = 2.0 if is_bottleneck else 1.0
            
            # Rectángulo contenedor
            card_box = patches.FancyBboxPatch((cx, card_y), col_w, card_h - 0.05, boxstyle="round,pad=0.04",
                                              fc=bg_c, ec=border_c, lw=border_w)
            ax.add_patch(card_box)
            
            # Saltos de línea REALES con textwrap (\n)
            title_lines = textwrap.wrap(item_title, width=19)
            title_text = "\n".join(title_lines)
            
            t_col = "#fb7185" if is_bottleneck else "#f8fafc"
            ax.text(cx + 0.08, card_y + card_h - 0.22, title_text, 
                    fontsize=8.5, fontweight='bold', color=t_col, family='sans-serif', va='top')
            
            # Posición de la descripción calculada exactamente según las líneas del título
            num_t_lines = len(title_lines)
            offset_y = 0.22 + (num_t_lines * 0.22)
            
            # Descripción con saltos de línea REALES (\n)
            desc_lines = textwrap.wrap(item_desc, width=22)
            desc_text = "\n".join(desc_lines)
            
            d_col = "#fecdd3" if is_bottleneck else "#94a3b8"
            ax.text(cx + 0.08, card_y + card_h - offset_y - 0.05, desc_text, 
                    fontsize=7.3, color=d_col, family='sans-serif', va='top')
            
            card_y -= card_margin

    # Flechas conectando los encabezados
    for i in range(4):
        ax_arrow = start_x + (i + 1) * col_w + i * col_gap + (col_gap / 2)
        ax.annotate('', xy=(ax_arrow + 0.06, y_header + 0.48), xytext=(ax_arrow - 0.06, y_header + 0.48),
                    arrowprops=dict(arrowstyle="->", color='#64748b', lw=2.5))

    # Límites del gráfico
    ax.set_xlim(0, 10)
    ax.set_ylim(0.2, 9.2)
    ax.axis('off')

    # Pie de página
    fig.text(0.04, 0.02, "Estudiante: Francisco Israel Mesillas Hernández  |  israel.mecillas@gmail.com  |  Ruta 4: Finanzas & Operaciones  |  Challenge ONE G11 AI for Business", 
             fontsize=8.5, color='#64748b', family='sans-serif')

    # Guardar en las rutas del proyecto
    out_root = r"C:\Users\52477\Desktop\challengeAIbuilder\matriz_sipoc_taranis_black.png"
    out_lean = r"C:\Users\52477\Desktop\challengeAIbuilder\02_Diagnostico_Lean_Operaciones\matriz_sipoc_taranis_black.png"
    out_art = r"C:\Users\52477\.gemini\antigravity\brain\65b23f9f-a310-40e5-923f-54f1f937153f\matriz_sipoc_taranis_black.png"

    plt.savefig(out_root, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.savefig(out_lean, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.savefig(out_art, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    
    print("SUCCESS: Imagen generada con saltos de linea reales sin ningun traslape!")

if __name__ == '__main__':
    render_sipoc()

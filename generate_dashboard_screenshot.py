# -*- coding: utf-8 -*-
"""
Generador de una captura visual en alta resolución del Dashboard Financiero de Taranis Black
para insertarla en Google Docs en la celda 'Panel o informe generado'.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def render_dashboard_capture():
    fig, ax = plt.subplots(figsize=(16, 10.5), dpi=300)
    fig.patch.set_facecolor('#0b0f19')
    ax.set_facecolor('#0b0f19')

    # Top Brand Header
    fig.text(0.04, 0.95, "TARANIS BLACK | PANEL FINANCIERO INTELIGENTE & LIVE ARTIFACT", 
             fontsize=17, fontweight='bold', color='#ffffff', family='sans-serif')
    fig.text(0.04, 0.92, "Análisis de Variaciones Presupuesto vs. Real y Simulación Predictiva T1 2027 (Ruta 4: Finanzas)", 
             fontsize=10.5, color='#38bdf8', family='sans-serif')

    # KPI Banner (EBITDA Brecha)
    banner = patches.FancyBboxPatch((0.04, 0.81), 0.92, 0.08, boxstyle="round,pad=0.01",
                                    fc='#1e293b', ec='#f59e0b', lw=2, transform=fig.transFigure)
    fig.patches.append(banner)
    
    fig.text(0.06, 0.855, "DIAGNÓSTICO EJECUTIVO:", fontsize=9, fontweight='bold', color='#f59e0b', family='sans-serif')
    fig.text(0.06, 0.825, "Ventas Reales: USD 48.50M (99.8%)  |  EBITDA Presupuesto: USD 9.85M  |  EBITDA Real: USD 5.77M (-41.4%)  |  Margen Perdido: -USD 4,078,000",
             fontsize=10, fontweight='bold', color='#ffffff', family='sans-serif')

    # 4 Top KPI Cards
    cards = [
        ("INGRESOS BRUTOS REALES", "USD 48.50M", "99.8% de Meta", "#10b981", 0.04),
        ("FLETES DE EMERGENCIA CD", "USD 3.74M", "+57.1% Desvío (+USD 1.36M)", "#f43f5e", 0.28),
        ("CANCELACIONES X RETRASO", "USD 1.23M", "+120.5% Desvío (+USD 675k)", "#f43f5e", 0.52),
        ("MOROSIDAD B2B (PDD)", "USD 1.11M", "3.4% Receta (+2.2 p.p.)", "#f43f5e", 0.76)
    ]
    
    for title, val, sub, col, x in cards:
        c_box = patches.FancyBboxPatch((x, 0.67), 0.20, 0.11, boxstyle="round,pad=0.01",
                                       fc='#1e293b', ec='#334155', lw=1.2, transform=fig.transFigure)
        fig.patches.append(c_box)
        fig.text(x + 0.015, 0.75, title, fontsize=8, fontweight='bold', color='#94a3b8', family='sans-serif')
        fig.text(x + 0.015, 0.705, val, fontsize=14, fontweight='bold', color='#ffffff' if col == '#10b981' else '#f43f5e', family='sans-serif')
        fig.text(x + 0.015, 0.68, sub, fontsize=7.5, color=col, family='sans-serif')

    # Left Section: Quarterly Collapse Bar/Line Chart
    # We will create sub-axes inside figure
    ax_chart1 = fig.add_axes([0.05, 0.28, 0.42, 0.33])
    ax_chart1.set_facecolor('#1e293b')
    ax_chart1.set_title("Evolución Trimestral: Ingresos vs. Colapso de EBITDA (USD M)", fontsize=9.5, fontweight='bold', color='#ffffff', pad=10)
    
    quarters = ['T1', 'T2', 'T3', 'T4']
    revenues = [10.85, 11.75, 12.50, 13.40]
    ebitda = [1.78, 1.83, 1.16, 1.00]
    
    ax_chart1.bar(quarters, revenues, color='#0284c7', width=0.45, label='Ingresos (USD M)')
    ax_chart1.set_ylabel("Ingresos (USD M)", color='#94a3b8', fontsize=8)
    ax_chart1.tick_params(colors='#94a3b8', labelsize=8)
    ax_chart1.grid(color='#334155', linestyle='--', alpha=0.5)
    
    ax_chart1_twin = ax_chart1.twinx()
    ax_chart1_twin.plot(quarters, ebitda, color='#f43f5e', marker='o', linewidth=2.5, label='EBITDA (USD M)')
    ax_chart1_twin.set_ylabel("EBITDA (USD M)", color='#f43f5e', fontsize=8)
    ax_chart1_twin.tick_params(colors='#f43f5e', labelsize=8)
    
    # Right Section: Sobrecostos Operativos (Fricción)
    ax_chart2 = fig.add_axes([0.53, 0.28, 0.42, 0.33])
    ax_chart2.set_facecolor('#1e293b')
    ax_chart2.set_title("Desglose de Sobrecostos Operativos (Total: USD 3.89M)", fontsize=9.5, fontweight='bold', color='#ffffff', pad=10)
    
    causes = ['Fletes Urgentes', 'Cancelaciones', 'Morosidad PDD', 'Reentregas/Multas', 'Horas Extras']
    losses = [1.36, 0.675, 0.670, 0.515, 0.260]
    colors = ['#e11d48', '#f97316', '#d97706', '#eab308', '#64748b']
    
    y_pos = range(len(causes))
    ax_chart2.barh(y_pos, losses, color=colors, height=0.55)
    ax_chart2.set_yticks(y_pos)
    ax_chart2.set_yticklabels(causes, color='#cbd5e1', fontsize=8)
    ax_chart2.set_xlabel("Sobrecosto en Millones de USD", color='#94a3b8', fontsize=8)
    ax_chart2.tick_params(colors='#94a3b8', labelsize=8)
    ax_chart2.grid(color='#334155', linestyle='--', alpha=0.5)
    
    for i, v in enumerate(losses):
        ax_chart2.text(v + 0.03, i, f"USD {v*1000:.0f}k", va='center', color='#ffffff', fontweight='bold', fontsize=7.5)

    # Bottom Simulation Box
    sim_box = patches.FancyBboxPatch((0.04, 0.07), 0.92, 0.16, boxstyle="round,pad=0.01",
                                    fc='#111827', ec='#10b981', lw=1.5, transform=fig.transFigure)
    fig.patches.append(sim_box)
    
    fig.text(0.06, 0.19, "SIMULADOR PREDICTIVO T1 2027 (CON INTERVENCION DE IA):", fontsize=9.5, fontweight='bold', color='#10b981', family='sans-serif')
    sim_details = (
        "• Reducción de fletes de emergencia: -60% (baja del 2.8% al 1.0% de ventas al erradicar errores de picking)\n"
        "• Reducción de cancelaciones comerciales por lentitud: -75% (aprobación en 15 min desactiva cancelaciones)\n"
        "• Proyección EBITDA T1 2027: USD 2,520,000 (Margen 17.7%) vs. Escenario Inercial Sin IA de USD 950,000 (6.9%)\n"
        "• Impacto Neto Trimestral Atribuible a IA: +USD 1,570,000 de EBITDA  |  ROI Estimado: 1,510%  |  Payback: 22 días"
    )
    fig.text(0.06, 0.09, sim_details, fontsize=8.5, color='#cbd5e1', family='sans-serif')

    ax.axis('off')
    
    # Save image
    out_root = r"C:\Users\52477\Desktop\challengeAIbuilder\captura_dashboard_financiero.png"
    out_fin = r"C:\Users\52477\Desktop\challengeAIbuilder\03_Panel_Financiero_y_Predictivo\captura_dashboard_financiero.png"
    
    plt.savefig(out_root, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.savefig(out_fin, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print("Captura del dashboard financiero generada exitosamente!")

if __name__ == '__main__':
    render_dashboard_capture()

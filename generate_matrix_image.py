# -*- coding: utf-8 -*-
"""
Generador de la imagen ejecutiva de la Matriz de Esfuerzo x Impacto
para Taranis Black (Ruta 4: Finanzas y Operaciones)
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def generate_matrix():
    # Setup Figure
    fig, ax = plt.subplots(figsize=(13, 8.5), dpi=300)
    fig.patch.set_facecolor('#0f172a') # Dark modern canvas
    ax.set_facecolor('#0f172a')
    
    # Quadrant background boxes
    # Top-Left: Quick Wins (Greenish)
    rect_qw = patches.Rectangle((0, 5), 5, 5, linewidth=1.5, edgecolor='#10b981', facecolor='#064e3b', alpha=0.35)
    ax.add_patch(rect_qw)
    
    # Top-Right: Estratégicos (Blueish)
    rect_st = patches.Rectangle((5, 5), 5, 5, linewidth=1.5, edgecolor='#3b82f6', facecolor='#1e3a8a', alpha=0.35)
    ax.add_patch(rect_st)
    
    # Bottom-Left: Fill-ins (Yellowish/Slate)
    rect_fi = patches.Rectangle((0, 0), 5, 5, linewidth=1.5, edgecolor='#64748b', facecolor='#1e293b', alpha=0.45)
    ax.add_patch(rect_fi)
    
    # Bottom-Right: Descartados (Reddish)
    rect_no = patches.Rectangle((5, 0), 5, 5, linewidth=1.5, edgecolor='#ef4444', facecolor='#450a0a', alpha=0.35)
    ax.add_patch(rect_no)
    
    # Central Cross Axes
    ax.axhline(5, color='#475569', linestyle='--', linewidth=1.5, alpha=0.8)
    ax.axvline(5, color='#475569', linestyle='--', linewidth=1.5, alpha=0.8)
    
    # Quadrant Title Badges
    # 1. Quick Wins
    ax.text(0.3, 9.5, '★ CUADRANTE 1: QUICK WINS (Ganancias Rápidas)', 
            fontsize=12, fontweight='bold', color='#34d399', family='sans-serif')
    ax.text(0.3, 9.15, 'Bajo Esfuerzo / Alto Impacto Financiero Inmediato', 
            fontsize=9, color='#94a3b8', family='sans-serif', style='italic')
    
    # 2. Estratégicos
    ax.text(5.3, 9.5, '⚡ CUADRANTE 2: ESTRATÉGICOS (Grandes Apuestas)', 
            fontsize=12, fontweight='bold', color='#60a5fa', family='sans-serif')
    ax.text(5.3, 9.15, 'Alto Impacto / Requiere Integración de Procesos', 
            fontsize=9, color='#94a3b8', family='sans-serif', style='italic')
    
    # 3. Fill-ins
    ax.text(0.3, 4.5, '○ CUADRANTE 3: SECUNDARIOS (Fill-ins)', 
            fontsize=11, fontweight='bold', color='#94a3b8', family='sans-serif')
    ax.text(0.3, 4.15, 'Bajo Esfuerzo / Bajo Impacto Relativo', 
            fontsize=9, color='#64748b', family='sans-serif', style='italic')
    
    # 4. Descartados
    ax.text(5.3, 4.5, '✕ CUADRANTE 4: DESCARTADOS (Trampas de Recursos)', 
            fontsize=11, fontweight='bold', color='#f87171', family='sans-serif')
    ax.text(5.3, 4.15, 'Esfuerzo Extremo / Alto Riesgo Operativo', 
            fontsize=9, color='#64748b', family='sans-serif', style='italic')
    
    # Helper to draw Initiative Cards
    def draw_card(x, y, title, subtitle, bullets, badge, badge_color, card_bg='#1e293b', border_col='#334155'):
        card = patches.FancyBboxPatch((x, y), 4.3, 1.85, boxstyle="round,pad=0.15", 
                                      fc=card_bg, ec=border_col, lw=1.5, alpha=0.95)
        ax.add_patch(card)
        # Badge
        ax.text(x + 0.15, y + 1.6, badge, fontsize=7.5, fontweight='bold', 
                color=badge_color, family='sans-serif',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#0f172a', edgecolor=badge_color, lw=1))
        # Title
        ax.text(x + 0.15, y + 1.25, title, fontsize=10.5, fontweight='bold', color='#ffffff', family='sans-serif')
        # Subtitle
        ax.text(x + 0.15, y + 0.95, subtitle, fontsize=8.5, color='#cbd5e1', family='sans-serif')
        # Bullets
        ax.text(x + 0.15, y + 0.25, bullets, fontsize=8, color='#94a3b8', family='sans-serif')

    # Cards Content
    # Card 1: Quick Win (Order to ERP)
    draw_card(0.35, 6.6,
              "1. Ingesta Inteligente OCR+LLM (Order-to-ERP)",
              "Extracción documental de PDFs y validación contra stock/precios",
              "• Tiempo de ciclo: de 40 min a 3 min por propuesta\n• Erradica tasa de error de 6.8% en NF-e\n• Ahorro: USD 960k fletes urgentes + USD 390k multas",
              "PRIORIDAD 1 | FASE 1 (MES 1)", "#10b981",
              card_bg='#064e3b', border_col='#059669')

    # Card 2: Scoring Predictivo (Estratégico)
    draw_card(5.35, 7.1,
              "2. Motor Predictivo de Scoring Crediticio B2B",
              "Machine Learning + Integración API Serasa Experian",
              "• Aprobación en 15 min para órdenes <USD 50k (Banda Verde)\n• Desactiva cuello de botella de 48h del Gerente Financiero\n• Ahorro: Rescata USD 1.25M en pedidos cancelados",
              "PRIORIDAD 2 | FASE 2 (MES 2)", "#3b82f6",
              card_bg='#1e3a8a', border_col='#2563eb')

    # Card 3: Conciliador Continuo (Estratégico)
    draw_card(5.35, 5.15,
              "3. Conciliador Financiero y Cierre Continuo",
              "Analítica multi-fuente (3 Excels + Bancos + ERP legado)",
              "• Cierre contable mensual se reduce de 7 a 2 días hábiles\n• Asientos contables asistidos bajo supervisión del Controller\n• Ahorro: USD 180k horas extras + USD 650k morosidad",
              "PRIORIDAD 3 | FASE 3 (MES 3)", "#818cf8",
              card_bg='#312e81', border_col='#6366f1')

    # Card 4: Secondary (Fill-in)
    draw_card(0.35, 1.8,
              "4. Asistente Preventivo de Cobranza Multicanal",
              "Generación automatizada de recordatorios vía WhatsApp / Email",
              "• Automatiza avisos 5 días antes del vencimiento a clientes B2B\n• Soporte operativo para analistas de crédito\n• Ayuda a contener cartera vencida",
              "COMPLEMENTARIO | MES 4", "#eab308",
              card_bg='#422006', border_col='#ca8a04')

    # Card 5: Descartado
    draw_card(5.35, 1.8,
              "5. Reemplazo Integral del ERP Legado Monolítico",
              "Sustitución completa del software de gestión empresarial",
              "• Costo estimado: >USD 1.5M | Plazo: >18 meses\n• Severo riesgo de parálisis operativa y disrupción comercial\n• Motivo: La IA resuelve la integración sin sustituir el core",
              "DESCARTADO | ALTO RIESGO", "#ef4444",
              card_bg='#450a0a', border_col='#dc2626')

    # Axis Labels and Limits
    ax.set_xlim(-0.2, 10.2)
    ax.set_ylim(-0.2, 10.2)
    ax.axis('off') # Hide default box
    
    # Custom Axis Arrows and Titles
    # Arrow X
    ax.annotate('', xy=(10, 0.2), xytext=(0, 0.2),
                arrowprops=dict(arrowstyle="->", color='#94a3b8', lw=2))
    ax.text(5, -0.15, "ESFUERZO TÉCNICO & COMPLEJIDAD DE IMPLEMENTACIÓN  ──►", 
            ha='center', va='center', fontsize=10, fontweight='bold', color='#cbd5e1', family='sans-serif')
    ax.text(0.2, 0.45, "Bajo Esfuerzo", fontsize=8.5, color='#94a3b8', family='sans-serif')
    ax.text(9.8, 0.45, "Alto Esfuerzo", fontsize=8.5, color='#94a3b8', ha='right', family='sans-serif')

    # Arrow Y
    ax.annotate('', xy=(0.2, 10), xytext=(0.2, 0),
                arrowprops=dict(arrowstyle="->", color='#94a3b8', lw=2))
    ax.text(-0.15, 5, "◄──  IMPACTO EN EL NEGOCIO & RETORNO FINANCIERO (EBITDA)", 
            ha='center', va='center', rotation=90, fontsize=10, fontweight='bold', color='#cbd5e1', family='sans-serif')
    ax.text(0.45, 0.6, "Bajo Impacto", fontsize=8.5, color='#94a3b8', family='sans-serif')
    ax.text(0.45, 9.8, "Alto Impacto", fontsize=8.5, color='#94a3b8', family='sans-serif')

    # Header Box
    plt.subplots_adjust(top=0.88, bottom=0.08, left=0.06, right=0.96)
    fig.text(0.06, 0.95, "TARANIS BLACK | MATRIZ DE PRIORIZACIÓN ESFUERZO × IMPACTO", 
             fontsize=16, fontweight='bold', color='#f8fafc', family='sans-serif')
    fig.text(0.06, 0.915, "Hoja de Ruta de Inteligencia Artificial — Ruta 4: Finanzas y Operaciones (ONE AI for Business - Cohorte G11)", 
             fontsize=10, color='#f59e0b', family='sans-serif')

    # Footer Metadata
    fig.text(0.06, 0.02, "Estudiante: Francisco Israel Mesillas Hernández  |  israel.mecillas@gmail.com  |  ROI Estimado: 1,510.8%  |  Payback: 22 días  |  Ahorro Anual: USD 2.98M", 
             fontsize=8.5, color='#64748b', family='sans-serif')

    # Save outputs
    out1 = r"C:\Users\52477\Desktop\challengeAIbuilder\matriz_esfuerzo_impacto_taranis_black.png"
    out2 = r"C:\Users\52477\Desktop\challengeAIbuilder\01_Estrategia_Ruta0_Corporativa\matriz_esfuerzo_impacto_taranis_black.png"
    out_artifact = r"C:\Users\52477\.gemini\antigravity\brain\65b23f9f-a310-40e5-923f-54f1f937153f\matriz_esfuerzo_impacto_taranis_black.png"
    
    plt.savefig(out1, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.savefig(out2, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.savefig(out_artifact, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    
    print(f"Imagen generada con éxito en:\n- {out1}\n- {out2}\n- {out_artifact}")

if __name__ == '__main__':
    generate_matrix()

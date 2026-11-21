# -*- coding: utf-8 -*-
"""
Script para generar el Informe Ejecutivo en DOCX y Markdown para el Challenge ONE G11 - Taranis Black (Ruta 4: Finanzas y Operaciones).
Estudiante: Francisco Israel Mesillas Hernández
"""
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_executive_report_docx(filepath):
    doc = docx.Document()
    
    # Page Setup - Margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
        
    # Styles & Colors
    # Primary: #1B365D (Deep Navy), Secondary: #C98A2C (Gold/Ochre), Dark Text: #222222, Light Bg: #F4F6F9
    
    # Title / Header
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_org = p_title.add_run("PROGRAMA ORACLE NEXT EDUCATION (ONE) & ALURA LATAM\nCHALLENGE ONE G11 — AI FOR BUSINESS\n")
    run_org.font.size = Pt(11)
    run_org.font.bold = True
    run_org.font.color.rgb = RGBColor(0x70, 0x80, 0x90)
    
    run_main = p_title.add_run("INFORME EJECUTIVO — CONSULTORÍA ESTRATÉGICA DE IA\nEMPRESA SIMULADA: TARANIS BLACK")
    run_main.font.size = Pt(18)
    run_main.font.bold = True
    run_main.font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = p_sub.add_run("RUTA 4 — IA PARA FINANZAS Y OPERACIONES")
    run_sub.font.size = Pt(13)
    run_sub.font.bold = True
    run_sub.font.color.rgb = RGBColor(0xC9, 0x8A, 0x2C)
    
    doc.add_paragraph() # Spacer
    
    # Table: Identification
    t_id = doc.add_table(rows=5, cols=2)
    t_id.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_id.autofit = False
    
    headers_id = [
        ("Nombre completo:", "Francisco Israel Mesillas Hernández"),
        ("Correo electrónico:", "israel.mecillas@gmail.com"),
        ("Grupo / Cohorte:", "G11 — ONE (Oracle Next Education)"),
        ("Ruta de especialización:", "[X] Ruta 4 — IA para finanzas y operaciones\n[ ] Ruta 1 — Ventas | [ ] Ruta 2 — Marketing | [ ] Ruta 3 — RR. HH."),
        ("Público destinatario:", "Directora Ejecutiva, CFO / Controller, Gerente Financiero, Gerente de Operaciones y Líder de Logística de Taranis Black")
    ]
    
    for i, (k, v) in enumerate(headers_id):
        cell_k = t_id.cell(i, 0)
        cell_v = t_id.cell(i, 1)
        cell_k.width = Inches(2.2)
        cell_v.width = Inches(4.6)
        set_cell_background(cell_k, "1B365D")
        set_cell_background(cell_v, "F4F6F9")
        set_cell_margins(cell_k, top=120, bottom=120, left=150, right=150)
        set_cell_margins(cell_v, top=120, bottom=120, left=150, right=150)
        
        p_k = cell_k.paragraphs[0]
        run_k = p_k.add_run(k)
        run_k.font.bold = True
        run_k.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        run_k.font.size = Pt(10)
        
        p_v = cell_v.paragraphs[0]
        run_v = p_v.add_run(v)
        run_v.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
        run_v.font.size = Pt(10)

    doc.add_paragraph()
    
    # Context Box
    t_ctx = doc.add_table(rows=1, cols=1)
    t_ctx.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_ctx = t_ctx.cell(0, 0)
    c_ctx.width = Inches(6.8)
    set_cell_background(c_ctx, "FFF8E7") # Light warm amber
    set_cell_margins(c_ctx, top=140, bottom=140, left=180, right=180)
    p_ctx = c_ctx.paragraphs[0]
    r_ctx_h = p_ctx.add_run("🏢 PROBLEMA DE NEGOCIO A RESOLVER (CONTEXTO TARANIS BLACK — RUTA 4):\n")
    r_ctx_h.font.bold = True
    r_ctx_h.font.size = Pt(10.5)
    r_ctx_h.font.color.rgb = RGBColor(0x8A, 0x5D, 0x00)
    r_ctx_t = p_ctx.add_run("Taranis Black procesa entre 180 y 220 pedidos corporativos mensuales (USD 33.6M/año en B2B), pero el ciclo entre la firma comercial y el despacho físico supera los 5 días hábiles (meta: <24h). La conciliación financiera se efectúa copiando datos manualmente entre tres hojas de cálculo y un ERP legado sin APIs. Esto causa un retraso crónico de 5 días en el cierre contable mensual, 44 horas de retención en homologación crediticia, USD 1.25M en cancelaciones por lentitud, USD 960k en fletes de emergencia duplicados y una erosión de USD 4.08M en el EBITDA anual.")
    r_ctx_t.font.size = Pt(9.5)
    r_ctx_t.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

    doc.add_paragraph()
    
    # -------------------------------------------------------------
    # RESUMEN EJECUTIVO (MÁXIMO 15 LÍNEAS - CORREO A DIRECTORA EJECUTIVA)
    # -------------------------------------------------------------
    h1 = doc.add_heading("RESUMEN EJECUTIVO — CORREO A LA DIRECTORA EJECUTIVA", level=1)
    h1.runs[0].font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    
    t_mail = doc.add_table(rows=1, cols=1)
    t_mail.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_mail = t_mail.cell(0, 0)
    c_mail.width = Inches(6.8)
    set_cell_background(c_mail, "F4F6F9")
    set_cell_margins(c_mail, top=150, bottom=150, left=180, right=180)
    
    mail_text = (
        "Para: Directora Ejecutiva — Taranis Black\n"
        "De: Francisco Israel Mesillas Hernández — Consultor Líder en Estrategia de IA\n"
        "Asunto: Diagnóstico Estratégico y Plan de Transformación con IA: Recuperación de USD 3.2M en EBITDA y Cierre en 24h\n\n"
        "Estimada Directora Ejecutiva:\n"
        "Tras auditar el ciclo financiero-operativo de Taranis Black, identificamos que aunque las ventas anuales alcanzaron USD 48.5M (en línea con la meta de USD 48.6M), el EBITDA colapsó de USD 9.85M a USD 5.77M (-41.4%), destruyendo USD 4.08M en margen operativo. La causa raíz es una severa fricción operativa: conciliar manualmente 3 hojas de cálculo y un ERP legado genera 5 días de retraso en el cierre contable, retenciones de 48h en aprobación de crédito, USD 1.25M en pedidos cancelados por demora, USD 1.36M de sobrecosto en fletes urgentes y USD 1.11M en cartera vencida.\n\n"
        "Para revertir esta hemorragia, diseñamos una hoja de ruta con tres iniciativas de IA: 1) Ingesta inteligente OCR+LLM que extrae pedidos en PDF y valida inventario/precios en 3 minutos erradicando errores en despachos; 2) Motor predictivo de scoring crediticio que aprueba instantáneamente pedidos corporativos <USD 50k reduciendo el ciclo de 48h a 15 minutos; y 3) Asistente cognitivo de conciliación continua entre bancos, hojas locales y ERP con supervisión humana (Human-in-the-Loop).\n\n"
        "Impacto proyectado: Recuperación estimada de USD 2.98M en EBITDA el primer año, reducción del ciclo total de facturación-expedición a <24 horas y reducción del cierre contable de 7 a 2 días hábiles. Con una inversión estimada de USD 185,000, el proyecto ofrece un ROI del 1,510% y un periodo de recuperación de la inversión (Payback) de solo 22 días operativos. Quedo a su disposición para iniciar el piloto en 15 días."
    )
    
    p_m = c_mail.paragraphs[0]
    p_m.add_run(mail_text).font.size = Pt(9.5)
    
    doc.add_paragraph()
    
    # -------------------------------------------------------------
    # PARTE 1 — BASE ESTRATÉGICA OBLIGATORIA (RUTA 0)
    # -------------------------------------------------------------
    h_r0 = doc.add_heading("PARTE 1 — BASE ESTRATÉGICA OBLIGATORIA (RUTA 0)", level=1)
    h_r0.runs[0].font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    
    # ETAPA 1
    h_e1 = doc.add_heading("Etapa 1 — AI Canvas e Identificación de Oportunidades", level=2)
    h_e1.runs[0].font.color.rgb = RGBColor(0xC9, 0x8A, 0x2C)
    
    doc.add_paragraph(
        "A partir del análisis holístico de Taranis Black (cadena de valor que abarca desde la captación B2B y compras de aluminio/mesh hasta la entrega desde el Centro de Distribución en Joinville, SC), se identificaron tres casos de uso de alto impacto orientados a desatar los cuellos de botella operativos y financieros:"
    )
    
    # Table 3 use cases
    t_cases = doc.add_table(rows=4, cols=4)
    t_cases.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    c_heads = ["Iniciativa / Caso de Uso", "Tipo de IA", "Descripción Técnica y Funcional", "Mecanismo Human-in-the-Loop (HITL)"]
    for j, h in enumerate(c_heads):
        c = t_cases.cell(0, j)
        set_cell_background(c, "1B365D")
        set_cell_margins(c, top=100, bottom=100, left=100, right=100)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.size = Pt(9)
        
    cases_data = [
        (
            "1. Agente Inteligente de Ingesta, Extracción y Validación de Pedidos B2B (Order-to-ERP)",
            "Generativa + Tradicional (Híbrida)",
            "Pipeline multimodal que combina OCR inteligente y un LLM empresarial para extraer entidades de propuestas firmadas en PDF (razón social, CNPJ, ítems, colores de tela, precios y términos CIF/FOB). Valida determinísticamente los datos contra la base de datos de precios y stock antes de insertarlos al ERP legado vía RPA o conector directo, eliminando la digitación manual.",
            "Supervisión obligatoria cuando el índice de confianza del OCR/LLM sea inferior al 95%, si se detecta discrepancia de precios >1% con la lista oficial, o si el cliente no posee comprobante de domicilio fiscal validado."
        ),
        (
            "2. Motor Predictivo de Scoring Crediticio B2B y Aprobación Descentralizada de Límites",
            "Predictiva (Machine Learning Supervisado + Rules Engine)",
            "Modelo de árboles de decisión y regresión logística entrenado con datos históricos de morosidad interna y consulta automatizada vía API a burós de crédito (Serasa Experian). Clasifica el riesgo del CNPJ en 4 bandas (Verde, Amarillo, Naranja, Rojo). Automatiza la aprobación de pedidos menores a USD 50,000 para clientes en banda Verde en menos de 5 minutos.",
            "Supervisión obligatoria del Gerente Financiero para pedidos >USD 50,000, clientes nuevos sin historial crediticio en banda Amarilla, o solicitudes que demanden plazos extendidos de pago (ej. 30/60/90/120 días). Los rechazos requieren confirmación humana."
        ),
        (
            "3. Conciliador Financiero Cognitivo y Auditoría Continua para Cierre Contable",
            "Tradicional (Analítica) + Generativa (LLM para Explicabilidad)",
            "Algoritmo de conciliación multi-fuente que cruza en tiempo real las 3 hojas de cálculo locales ('Controle_Limites_2026.xlsx', fletes y precios) con los extractos bancarios y el libro mayor del ERP. El LLM detecta patrones de divergencia, genera asientos de ajuste y redacta un informe ejecutivo de desviaciones para la Controllería.",
            "El Controller debe revisar y firmar digitalmente cualquier ajuste contable, reclasificación de partidas o provisión para deudores dudosos (PDD) que exceda USD 5,000 antes de consolidar el balance mensual."
        )
    ]
    
    for row_idx, data in enumerate(cases_data, start=1):
        for col_idx, text in enumerate(data):
            c = t_cases.cell(row_idx, col_idx)
            set_cell_background(c, "FFFFFF" if row_idx % 2 == 1 else "F9FBFD")
            set_cell_margins(c, top=80, bottom=80, left=100, right=100)
            p = c.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8.5)
            if col_idx == 0:
                r.font.bold = True
                
    doc.add_paragraph()
    
    # Justification of AI types and HITL
    p_hitl_title = doc.add_paragraph()
    r = p_hitl_title.add_run("Justificación Estratégica de Clasificación y Supervisión Humana (HITL):")
    r.font.bold = True
    r.font.size = Pt(10.5)
    
    doc.add_paragraph(
        "• ¿Por qué IA Generativa en Ingesta? Los documentos comerciales en B2B no tienen un formato estándar (PDFs escaneados, órdenes de compra corporativas, contratos con firmas electrónicas diversas). Los sistemas basados en reglas rígidas fallan ante cualquier variación tipográfica. Los LLMs modernos procesan lenguaje natural no estructurado con alta robustez semántica.\n"
        "• ¿Por qué IA Predictiva en Crédito? La decisión de conceder crédito a plazo (30/60/90 días) depende de correlaciones cuantitativas complejas entre score de Serasa, historial de pagos de 24 meses, ratio de endeudamiento sectorial y tamaño de la solicitud. Un modelo predictivo minimiza el riesgo de impago sin detener el flujo comercial.\n"
        "• ¿Por qué Supervisión Humana (HITL) Obligatoria? En el ámbito financiero y operativo, las alucinaciones o falsos positivos conllevan consecuencias monetarias directas, disputas contractuales y sanciones tributarias ante la Receita Federal. El marco HITL garantiza que la IA actúe como copiloto de productividad ('Human-Centered AI'), manteniendo la responsabilidad legal y fiduciaria en manos de los líderes humanos."
    )
    
    # ETAPA 2
    h_e2 = doc.add_heading("Etapa 2 — Priorización Basada en Datos y Gestión del Cambio", level=2)
    h_e2.runs[0].font.color.rgb = RGBColor(0xC9, 0x8A, 0x2C)
    
    doc.add_paragraph(
        "Para maximizar el retorno de inversión y mitigar riesgos de ejecución, las iniciativas se evaluaron mediante una Matriz Esfuerzo × Impacto de cuatro cuadrantes:"
    )
    
    # Matriz Esfuerzo x Impacto Table
    t_mat = doc.add_table(rows=5, cols=5)
    t_mat.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    m_heads = ["Iniciativa", "Impacto Negocio", "Esfuerzo Técnico", "Cuadrante", "Prioridad y Despliegue"]
    for j, h in enumerate(m_heads):
        c = t_mat.cell(0, j)
        set_cell_background(c, "1B365D")
        set_cell_margins(c, top=80, bottom=80, left=80, right=80)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.size = Pt(9)
        
    matrix_data = [
        ("1. Ingesta Inteligente OCR+LLM (Order-to-ERP)", "Muy Alto (Ahorro USD 1.4M en fletes y multas)", "Bajo-Medio (Solución SaaS/API estándar)", "Quick Win (Alto Impacto / Bajo Esfuerzo)", "Fase 1: Mes 1 (Despliegue inmediato)"),
        ("2. Motor Predictivo de Scoring Crediticio", "Muy Alto (Recupera USD 1.25M en ventas canceladas)", "Medio (Integración API Serasa + Motor de Reglas)", "Estratégico (Alto Impacto / Esfuerzo Medio)", "Fase 2: Mes 2 (Tras estabilizar ingesta)"),
        ("3. Conciliador Financiero y Cierre Continuo", "Alto (Ahorro USD 180k en horas extras + cierre en 2d)", "Medio-Alto (Normalización de 3 Excels y ERP)", "Estratégico (Alto Impacto / Esfuerzo Medio-Alto)", "Fase 3: Mes 3 (Cierre contable continuo)"),
        ("4. Reemplazo Integral del ERP Legado (Descartado)", "Alto a Largo Plazo", "Extremo (Costos >USD 1.5M y >18 meses de parálisis)", "Descartado / No Prioritario", "Reevaluar en 2028 (La IA soluciona la capa de integración sin sustituir el core)")
    ]
    
    for row_idx, data in enumerate(matrix_data, start=1):
        for col_idx, text in enumerate(data):
            c = t_mat.cell(row_idx, col_idx)
            set_cell_background(c, "E8F8F5" if "Quick Win" in text or "Fase 1" in text else ("FEF9E7" if "Estratégico" in text else "FFFFFF"))
            set_cell_margins(c, top=80, bottom=80, left=80, right=80)
            p = c.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8.5)
            if col_idx == 0 or col_idx == 3:
                r.font.bold = True

    doc.add_paragraph()
    
    # Métricas de Éxito y ROI Cuantificado
    p_roi_title = doc.add_paragraph()
    r = p_roi_title.add_run("Métricas de Éxito, Ahorros Cuantificados y Cálculo del ROI:")
    r.font.bold = True
    r.font.size = Pt(10.5)
    
    doc.add_paragraph(
        "• Inversión Total Estimada (Año 1): USD 185,000 (Licencias empresariales LLM/OCR con Zero Data Retention: USD 45,000; conectores RPA y orquestación API: USD 55,000; consultoría especializada de integración y gestión del cambio: USD 65,000; contingencias y capacitación: USD 20,000).\n"
        "• Ahorros Anuales Capturados:\n"
        "   - Eliminación de fletes expresos de emergencia por errores de digitación: USD 960,000/año.\n"
        "   - Recuperación de pedidos B2B antes cancelados por retención de 48h en crédito: USD 850,000/año (margen bruto aportado).\n"
        "   - Reducción de multas y reentregas por divergencias en pedidos: USD 390,000/año.\n"
        "   - Disminución de cartera vencida e incobrabilidad (PDD) por análisis preventivo: USD 650,000/año.\n"
        "   - Eliminación de horas extras en auditorías y cierres contables: USD 130,000/año.\n"
        "   -> Beneficio Económico Total Anual: USD 2,980,000.\n"
        "• ROI Calculado: (USD 2,980,000 - USD 185,000) / USD 185,000 = 1,510.8% de Retorno sobre la Inversión.\n"
        "• Periodo de Recuperación (Payback): (USD 185,000 / USD 2,980,000) × 12 meses = 0.74 meses (~22 días hábiles).\n"
        "• Horas Ahorradas: Reducción del tiempo de tramitación por pedido de 40 a 3 minutos (92.5% de ahorro). En un volumen de 200 pedidos mensuales, se ahorran 123.3 horas/mes por asistente, liberando más de 1,480 horas anuales para análisis estratégico.\n"
        "• Metas de Adopción: 75% de pedidos procesados vía IA en el primer mes; 95% al tercer mes; 100% de conciliación bancaria automatizada al día 60."
    )
    
    # Plan de Gestión del Cambio (ADKAR)
    p_cm_title = doc.add_paragraph()
    r = p_cm_title.add_run("Plan de Gestión del Cambio Organizacional (Modelo ADKAR):")
    r.font.bold = True
    r.font.size = Pt(10.5)
    
    doc.add_paragraph(
        "1. Awareness (Conciencia): Sesiones ejecutivas con los equipos financiero, de ventas y logística demostrando que el proceso manual actual está destruyendo USD 4M anuales y provocando estrés por sobrecarga laboral. La IA no sustituye personas; sustituye tareas mecánicas alienantes.\n"
        "2. Desire (Deseo): Redefinición del perfil de puesto de 'Digitadores Contables' a 'Analistas de Inteligencia Financiera', asociando bonificaciones trimestrales a la reducción del ciclo de cobro y calidad del dato, garantizando seguridad laboral.\n"
        "3. Knowledge (Conocimiento): Academia interna de capacitación práctica en supervisión de IA, manejo de alertas de excepción y prompting financiero con Claude/ChatGPT.\n"
        "4. Ability (Habilidad): Periodo de marcha blanca ('Shadow Run') durante 4 semanas: el sistema de IA genera las propuestas y conciliaciones en paralelo mientras el personal humano las valida y aprueba con un solo clic.\n"
        "5. Reinforcement (Refuerzo): Panel público en la oficina de São Paulo y CD Joinville con las métricas de SLA en tiempo real, celebrando hitos de cierres mensuales sin horas extras."
    )
    
    # ETAPA 3
    h_e3 = doc.add_heading("Etapa 3 — Política de Gobernanza, Ética y Cumplimiento", level=2)
    h_e3.runs[0].font.color.rgb = RGBColor(0xC9, 0x8A, 0x2C)
    
    doc.add_paragraph(
        "Para garantizar un despliegue seguro, auditable y conforme a la ley, se formaliza la Política de Gobernanza de IA Responsable de Taranis Black:"
    )
    
    # Table Permitted vs Prohibited
    t_gov = doc.add_table(rows=6, cols=2)
    t_gov.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    c_p1 = t_gov.cell(0, 0)
    c_p2 = t_gov.cell(0, 1)
    c_p1.width = Inches(3.4)
    c_p2.width = Inches(3.4)
    set_cell_background(c_p1, "27AE60") # Green
    set_cell_background(c_p2, "C0392B") # Red
    set_cell_margins(c_p1, top=100, bottom=100, left=100, right=100)
    set_cell_margins(c_p2, top=100, bottom=100, left=100, right=100)
    
    r1 = c_p1.paragraphs[0].add_run("PRÁCTICAS PERMITIDAS (COMPLIANCE)")
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    r2 = c_p2.paragraphs[0].add_run("PRÁCTICAS ESTRICTAMENTE PROHIBIDAS")
    r2.font.bold = True
    r2.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    
    gov_rows = [
        ("Uso exclusivo de endpoints empresariales de IA (Enterprise APIs) con acuerdos vinculantes de No-Retención de Datos (Zero Data Retention) y no-entrenamiento.",
         "Uso de modelos públicos, versiones gratuitas de ChatGPT o extensiones no homologadas del navegador con datos de la empresa."),
        ("Extracción automatizada de datos transaccionales B2B (ítems, CNPJ público, volúmenes de compra y precios de lista).",
         "Ingesta de datos personales altamente sensibles (salud ocupacional, opiniones políticas, datos bancarios privados de personas naturales)."),
        ("Asistencia algorítmica de scoring crediticio y cálculo de límites bajo auditoría humana y reglas de negocio transparentes.",
         "Rechazo o revocación automática de crédito a clientes sin fundamentación matemática o sin opción de revisión por un analista humano."),
        ("Generación asistida de asientos contables de ajuste previa revisión y aprobación digital del Controller.",
         "Ejecución de pagos bancarios, transferencias de tesorería o liquidación fiscal desatendida sin firma digital de apoderados."),
        ("Anonimización y enmascaramiento criptográfico de identificadores fiscales antes de la transmisión a modelos externos.",
         "Compartir contraseñas de acceso al ERP, llaves API bancarias o certificados digitales A1/A3 en prompts de IA.")
    ]
    
    for row_idx, (ok_t, no_t) in enumerate(gov_rows, start=1):
        c1 = t_gov.cell(row_idx, 0)
        c2 = t_gov.cell(row_idx, 1)
        c1.width = Inches(3.4)
        c2.width = Inches(3.4)
        set_cell_background(c1, "F4FBF7" if row_idx % 2 == 1 else "FFFFFF")
        set_cell_background(c2, "FDF5F5" if row_idx % 2 == 1 else "FFFFFF")
        set_cell_margins(c1, top=70, bottom=70, left=80, right=80)
        set_cell_margins(c2, top=70, bottom=70, left=80, right=80)
        
        p1 = c1.paragraphs[0]
        r1 = p1.add_run("✔ " + ok_t)
        r1.font.size = Pt(8.5)
        
        p2 = c2.paragraphs[0]
        r2 = p2.add_run("✖ " + no_t)
        r2.font.size = Pt(8.5)
        
    doc.add_paragraph()
    
    # Protección de Datos, LGPD y Comité
    doc.add_paragraph(
        "• Cumplimiento Normativo (LGPD Brasil / Ley 13.709/2018): Taranis Black opera bajo la legislación brasileña de protección de datos personales. Aunque la mayoría de las transacciones son B2B, los contratos contienen firmas de representantes legales, correos y teléfonos corporativos que constituyen datos personales. Se implementa un módulo de Data Loss Prevention (DLP) que detecta y redacta automáticamente CPFs y nombres personales antes de cualquier llamada a LLMs.\n"
        "• Mitigación de Sesgos Algorítmicos: Los modelos de crédito predictivo se auditan trimestralmente para garantizar que no existan disparidades estadísticas contra PYMEs de regiones fuera del eje São Paulo-Joinville, asegurando que las decisiones respondan a liquidez y cumplimiento comprobables.\n"
        "• Estructura del Comité de Ética e IA:\n"
        "   1. Chief Financial Officer / Controller (Líder del Comité, garante fiduciario).\n"
        "   2. Data Protection Officer (DPO) / Oficial de Privacidad (Cumplimiento legal y LGPD).\n"
        "   3. Gerente de Ciberseguridad e Infraestructura TI (Seguridad de API y cifrado AES-256).\n"
        "   4. Gerente de Operaciones y Logística (Alineación de SLAs entre SP y CD Joinville).\n"
        "   5. Lead AI Engineer / Arquitecto de Solución (Monitoreo de deriva de datos y precisión del modelo).\n"
        "• Frecuencia de Auditoría: Auditorías quincenales durante los primeros 90 días de implementación; auditorías bimestrales en operación regular y revisión anual independiente de ciberseguridad."
    )
    
    # -------------------------------------------------------------
    # PARTE 2 — ESPECIALIZACIÓN: FINANZAS Y OPERACIONES (RUTA 4)
    # -------------------------------------------------------------
    h_r4 = doc.add_heading("PARTE 2 — ESPECIALIZACIÓN: IA PARA FINANZAS Y OPERACIONES", level=1)
    h_r4.runs[0].font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    
    # ETAPA 1: SIPOC E ISHIKAWA
    h_l1 = doc.add_heading("Etapa 1 — Mapeo Lean y Diagnóstico de Cuellos de Botella (SIPOC e Ishikawa)", level=2)
    h_l1.runs[0].font.color.rgb = RGBColor(0xC9, 0x8A, 0x2C)
    
    doc.add_paragraph(
        "Para diagnosticar con rigor científico las causas del retraso de 5 días en la facturación y el cierre mensual, se construyó la Matriz SIPOC del flujo As-Is y el Diagrama de Ishikawa bajo el estándar Lean Six Sigma:"
    )
    
    # Matriz SIPOC Table
    t_sipoc = doc.add_table(rows=6, cols=5)
    t_sipoc.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    s_heads = ["S (Suppliers / Proveedores)", "I (Inputs / Entradas)", "P (Process / Macroproceso)", "O (Outputs / Salidas)", "C (Customers / Clientes)"]
    for j, h in enumerate(s_heads):
        c = t_sipoc.cell(0, j)
        set_cell_background(c, "1B365D")
        set_cell_margins(c, top=80, bottom=80, left=80, right=80)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.size = Pt(8.5)
        
    sipoc_data = [
        (
            "Consultores de Ventas B2B y SDRs (SP)",
            "Propuesta comercial firmada en PDF escaneado (vía email manual)",
            "Paso 1: Recepción informal de propuestas en bandeja financiero@. Más de 40 correos/día sin prioridad ni validación de inventario.",
            "Orden de venta no estructurada en cola de correo",
            "Asistente Financiero (Análisis inicial)"
        ),
        (
            "Clientes Corporativos B2B y Buró Serasa",
            "Datos fiscales (CNPJ, IE, Dirección) y Score de crédito Serasa",
            "Paso 2: Revisión manual de crédito (40 min/pedido). Asistente alterna entre 3 pantallas: ERP legado, Serasa y Excel 'Controle_Limites_2026.xlsx'.",
            "Dossier y dictamen preliminar de crédito en hoja local",
            "Gerente Financiero (Aprobador de alzada)"
        ),
        (
            "Gerente Financiero (Aprobador centralizado)",
            "Resumen informal por correo ('¿Podemos facturar USD 85k?')",
            "Paso 3 y 4: Espera de aprobación por email (hasta 48h hábiles). Cuello de botella severo; viajes y reuniones de gerencia frenan el flujo.",
            "Respuesta informal 'De acuerdo' por correo electrónico",
            "Asistente Financiero / Facturación"
        ),
        (
            "Asistente Financiero de Facturación",
            "Aprobación por correo y catálogo de precios en Excel",
            "Paso 5a: Emisión manual de Nota Fiscal en ERP legado. Copia manual genera 6.8% de errores en códigos de producto, telas y domicilios.",
            "DANFE, archivo XML de NF-e y boletos bancarios 30/60/90",
            "Cliente Corporativo B2B y Área Contable"
        ),
        (
            "Centro de Distribución (CD Joinville) y Transportadoras",
            "Autorización manual por email a expedicao.cd@ y tabla de fletes",
            "Paso 5b: Notificación a CD Joinville por correo. Divergencias en flete CIF/FOB paralizan camiones acumulando sobrecostos y reentregas.",
            "Picking List, Minuta de Embarque y Carga despachada",
            "Cliente Corporativo B2B Receptor"
        )
    ]
    
    for row_idx, data in enumerate(sipoc_data, start=1):
        for col_idx, text in enumerate(data):
            c = t_sipoc.cell(row_idx, col_idx)
            set_cell_background(c, "FFFFFF" if row_idx % 2 == 1 else "F8FAFC")
            set_cell_margins(c, top=70, bottom=70, left=70, right=70)
            p = c.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8)
            if col_idx == 2:
                r.font.bold = True
                
    doc.add_paragraph()
    
    # Diagrama de Ishikawa (6M)
    p_ish_title = doc.add_paragraph()
    r = p_ish_title.add_run("Diagrama de Ishikawa (Causa-Efecto / Las 6M):")
    r.font.bold = True
    r.font.size = Pt(10.5)
    
    doc.add_paragraph(
        "Problema Central: Retraso Crónico de 5 Días en el Cierre Contable y Ciclo de Facturación Excesivo de 5 Días Hábiles (Erosión de USD 4.08M en EBITDA)\n\n"
        "1. ⚙️ Método (Procesos):\n"
        "   - Ausencia total de Procedimientos Operativos Estandarizados (POP) formalizados.\n"
        "   - Flujo de trabajo secuencial 100% dependiente de correos electrónicos no trazables.\n"
        "   - Falta de una matriz de alzada automática: todo pedido (incluso de USD 8,000 para clientes de 10 años) requiere autorización individual de gerencia.\n"
        "   - Reglas de flete (CIF vs. FOB) no validadas contractualmente al cerrar la propuesta.\n\n"
        "2. 💻 Máquina (Sistemas & Tecnología):\n"
        "   - ERP legado obsoleto y sin capacidad de integración mediante APIs modernas.\n"
        "   - Inexistencia de herramientas de OCR o IA para ingestión directa de documentos en PDF.\n"
        "   - Dependencia caótica de 3 hojas de cálculo Excel locales ('Controle_Limites_2026.xlsx', lista de precios y cálculo de fletes) propensas a corrupción y desincronización.\n\n"
        "3. 👥 Mano de Obra (Personas):\n"
        "   - Asistentes financieros atrapados en tareas alienantes de copiar y pegar (40 min por pedido).\n"
        "   - Síndrome de burnout y alta rotación en el equipo financiero por jornadas extenuantes a fin de mes.\n"
        "   - Gerente Financiero sobrecargado con comités ejecutivos y viajes a Joinville, convirtiéndose en el cuello de botella físico de las aprobaciones.\n\n"
        "4. 📄 Material (Insumos y Documentación):\n"
        "   - Formularios de propuesta comercial enviados por vendedores con datos incompletos o errores tipográficos.\n"
        "   - Discrepancias sistemáticas entre los códigos del catálogo comercial y los registros maestros del ERP (ej. mesh gris vs. tela negra).\n"
        "   - Comprobantes de dirección fiscal desactualizados que causan rechazos en las aduanas tributarias estatales.\n\n"
        "5. 📊 Medición (Métricas e Indicadores):\n"
        "   - Inexistencia de monitoreo de SLAs por etapa en tiempo real.\n"
        "   - La dirección general sólo descubre los retrasos y cancelaciones cuando el mes contable ya cerró.\n"
        "   - Falta de tableros de control para auditar el inventario retenido y pedidos congelados.\n\n"
        "6. 🏢 Medio Ambiente (Cultura y Entorno Organizacional):\n"
        "   - Fricción y silos departamentales entre el equipo comercial en São Paulo y el equipo logístico del CD en Joinville (Santa Catarina).\n"
        "   - Cultura reactiva arraigada de 'apagar incendios' en lugar de erradicar la causa raíz de los errores."
    )
    
    # Las 3 Causas Principales y la Intervención Prioritaria
    p_3c = doc.add_paragraph()
    r = p_3c.add_run("Las 3 Causas Principales del Desempeño Deficiente:")
    r.font.bold = True
    r.font.size = Pt(10.5)
    
    doc.add_paragraph(
        "1. Aprobación de Crédito Manual y Centralizada (Cuello de Botella de 48h): Provoca USD 1.25M anuales en cancelaciones directas por clientes corporativos frustrados que no pueden esperar 5 días hábiles para confirmar su entrega.\n"
        "2. Transcripción Manual de Datos de Pedidos (Error de 6.8% en Facturación): Genera USD 960k en fletes de emergencia y USD 725k en multas/reentregas por envío de mercancías con códigos, colores o domicilios equivocados.\n"
        "3. Desconexión de Datos entre ERP y las 3 Hojas de Cálculo Locales: Causa el retraso crónico de 5 días en el cierre mensual, requiriendo USD 180k en horas extras y auditorías, y ocultando una morosidad de USD 1.11M."
    )
    
    p_int = doc.add_paragraph()
    r = p_int.add_run("Intervención Prioritaria Recomendada:")
    r.font.bold = True
    r.font.size = Pt(10.5)
    
    doc.add_paragraph(
        "Se recomienda intervenir en primer lugar la Ingesta Inteligente OCR+LLM y el Motor Descentralizado de Aprobación de Crédito (Quick Win / Fase 1). "
        "Justificación: Este cuello de botella es el generador primario del efecto látigo aguas abajo. Al eliminar las 48 horas de espera del gerente y los errores manuales de transcripción en el Paso 1-2, los pedidos ingresan al ERP limpios en menos de 15 minutos. Esto desactiva inmediatamente las cancelaciones de USD 1.25M y evita los fletes de emergencia de USD 960k, estabilizando el flujo antes de abordar la conciliación contable profunda."
    )
    
    # ETAPA 2: PANEL INTELIGENTE Y ANÁLISIS PREDICTIVO (OPCIONAL)
    h_l2 = doc.add_heading("Etapa 2 — Panel Inteligente y Análisis Predictivo con Claude (Opcional)", level=2)
    h_l2.runs[0].font.color.rgb = RGBColor(0xC9, 0x8A, 0x2C)
    
    doc.add_paragraph(
        "Para transformar la gestión financiera de Taranis Black de un modelo reactivo a uno predictivo, se desarrolló un Panel Inteligente analizando el archivo oficial '05_Finanzas_Presupuesto_vs_Real.xlsx':"
    )
    
    # Prompts utilizados
    p_pr_title = doc.add_paragraph()
    r = p_pr_title.add_run("Prompts Estructurados de Análisis Financiero y Forense (Claude 3.7 Sonnet):")
    r.font.bold = True
    r.font.size = Pt(10)
    
    doc.add_paragraph(
        "```text\n"
        "PROMPT 1: ANÁLISIS DE ANOMALÍAS Y EROSIÓN DE EBITDA\n"
        "Actúa como un Senior Financial Controller y Consultor Lean. Analiza las 3 hojas del archivo adjunto '05_Finanzas_Presupuesto_vs_Real.xlsx' (Resultados_trimestrales, Ingresos_por_producto, Cuellos_de_botella_y_costos). Calcula y explica:\n"
        "1. ¿Por qué si los ingresos brutos reales (USD 48.5M) cumplieron con el 99.8% de la meta presupuestada (USD 48.6M), el EBITDA se desplomó un -41.4% (de USD 9.85M a USD 5.77M)?\n"
        "2. Identifica las 5 mayores variaciones negativas en gastos operacionales (OPEX) y cuantifica en dólares y porcentaje el sobrecosto acumulado.\n"
        "3. Cruza estas desviaciones con la hoja de cuellos de botella para demostrar la correlación matemática entre el retraso de 5 días de cierre, la retención de 48h de crédito y la pérdida neta.\n\n"
        "PROMPT 2: MODELADO PREDICTIVO TRIMESTRAL (T1 2027) Y LIVE ARTIFACT\n"
        "Con base en la tendencia real de T1 a T4, proyecta el desempeño para el próximo trimestre (T1 2027 / T5) comparando dos escenarios:\n"
        "- Escenario A (Inercial / Sin IA): Asume que el crecimiento de ventas continúa aumentando la presión y los fletes de emergencia siguen al 2.8% de la facturación.\n"
        "- Escenario B (Con Intervención de IA): Modela el impacto de automatizar la ingesta OCR y las reglas de crédito descentralizadas (reduciendo fletes de emergencia al 0.9%, eliminando el 75% de las cancelaciones por retraso y reduciendo la morosidad a 1.2%).\n"
        "Presenta los resultados en una tabla comparativa en USD y genera el código para un Dashboard Interactivo Ejecutivo con KPIs de EBITDA, margen bruto y ciclo de caja.\n"
        "```"
    )
    
    # Anomalías Identificadas
    p_anom_title = doc.add_paragraph()
    r = p_anom_title.add_run("Anomalías Financieras Críticas Identificadas:")
    r.font.bold = True
    r.font.size = Pt(10)
    
    # Table Anomalies
    t_anom = doc.add_table(rows=6, cols=5)
    t_anom.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    an_heads = ["Línea Contable Afectada", "Presupuesto Anual", "Real Anual", "Desviación Crítica", "Impacto Operativo Observado"]
    for j, h in enumerate(an_heads):
        c = t_anom.cell(0, j)
        set_cell_background(c, "1B365D")
        set_cell_margins(c, top=80, bottom=80, left=80, right=80)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.size = Pt(8.5)
        
    anom_data = [
        ("Fletes y Logística de Entrega CD", "USD 2,380,000", "USD 3,740,000", "+USD 1,360,000 (+57.1%)", "Sobrecosto masivo por contratación de fletes aéreos y expresos urgentes para evitar cancelaciones."),
        ("Cancelaciones por Retraso Logístico", "USD 560,000", "USD 1,235,000", "+USD 675,000 (+120.5%)", "Pérdida directa de pedidos corporativos firmados cuyos clientes no toleraron los 5 días de demora."),
        ("Provisión Deudores Dudosos (Inadimplencia)", "USD 440,000", "USD 1,110,000", "+USD 670,000 (+152.3%)", "Morosidad B2B subió de 1.2% a 3.4% por cobranza manual no automatizada vía correos sueltos."),
        ("Reentregas y Multas por Divergencias", "USD 210,000", "USD 725,000", "+USD 515,000 (+245.2%)", "Errores de digitación en NF-e (códigos de telas/brazos) que obligan a devolver camiones y pagar estadías."),
        ("Gastos Administrativos / Sistemas Legados", "USD 1,760,000", "USD 2,020,000", "+USD 260,000 (+14.8%)", "Gasto excesivo en horas extras del personal contable y consultorías externas para conciliar a fin de mes.")
    ]
    
    for row_idx, data in enumerate(anom_data, start=1):
        for col_idx, text in enumerate(data):
            c = t_anom.cell(row_idx, col_idx)
            set_cell_background(c, "FDF2E9" if col_idx == 3 else ("FFFFFF" if row_idx % 2 == 1 else "F9FBFD"))
            set_cell_margins(c, top=70, bottom=70, left=70, right=70)
            p = c.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8)
            if col_idx == 0 or col_idx == 3:
                r.font.bold = True
                
    doc.add_paragraph()
    
    # Proyección Trimestral T1 2027
    p_proj_title = doc.add_paragraph()
    r = p_proj_title.add_run("Proyección Predictiva para el Próximo Trimestre (T1 2027 / T5) en USD:")
    r.font.bold = True
    r.font.size = Pt(10)
    
    # Projection Table
    t_proj = doc.add_table(rows=7, cols=5)
    t_proj.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    pr_heads = ["Métrica Financiera", "T4 Real (USD)", "T1 2027 Inercial (Sin IA)", "T1 2027 Optimizado (Con IA)", "Impacto Neto de la IA"]
    for j, h in enumerate(pr_heads):
        c = t_proj.cell(0, j)
        set_cell_background(c, "1B365D")
        set_cell_margins(c, top=80, bottom=80, left=80, right=80)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.size = Pt(8.5)
        
    proj_data = [
        ("Ingresos Brutos Totales", "USD 13,400,000", "USD 13,800,000", "USD 14,200,000", "+USD 400,000 (+2.9% ventas recuperadas)"),
        ("Cancelaciones por Retraso", "-USD 420,000", "-USD 460,000", "-USD 115,000", "+USD 345,000 salvados"),
        ("Fletes y Logística de Entrega", "-USD 1,220,000", "-USD 1,320,000", "-USD 710,000", "+USD 610,000 reducidos en fletes urgentes"),
        ("Reentregas y Multas", "-USD 260,000", "-USD 290,000", "-USD 65,000", "+USD 225,000 ahorro en reprocesos"),
        ("Provisión Deudores Dudosos (PDD)", "-USD 390,000", "-USD 430,000", "-USD 140,000", "+USD 290,000 recuperados por cobro IA"),
        ("EBITDA Trimestral", "USD 1,002,000", "USD 950,000", "USD 2,520,000", "+USD 1,570,000 de EBITDA trimestral (+165%)")
    ]
    
    for row_idx, data in enumerate(proj_data, start=1):
        for col_idx, text in enumerate(data):
            c = t_proj.cell(row_idx, col_idx)
            set_cell_background(c, "E8F8F5" if col_idx == 3 or col_idx == 4 else ("FFFFFF" if row_idx % 2 == 1 else "F9FBFD"))
            set_cell_margins(c, top=70, bottom=70, left=70, right=70)
            p = c.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8)
            if col_idx == 0 or col_idx == 4:
                r.font.bold = True

    doc.add_paragraph()
    
    doc.add_paragraph(
        "Supuestos Utilizados en el Modelo Predictivo:\n"
        "1. El tiempo de ciclo de facturación se reduce de 5 días a <24 horas útiles gracias al agente de ingesta y validación de órdenes de compra.\n"
        "2. La tasa de fletes expresos de emergencia desciende del 2.8% al 0.9% sobre las ventas brutas al eliminarse las entregas dobles y errores en códigos de producto.\n"
        "3. El motor de cobranza preventiva mediante agentes de IA recupera el índice de morosidad al benchmark del 1.2% de la facturación en 90 días.\n"
        "4. El margen EBITDA pasa de un deprimente 7.1% en el escenario inercial a un 17.7% saludable en el escenario con IA en el primer trimestre de operación."
    )
    
    # -------------------------------------------------------------
    # ANEXO DE EVIDENCIAS Y TABLA DE ENTREGABLES
    # -------------------------------------------------------------
    h_anx = doc.add_heading("ANEXO DE EVIDENCIAS Y REGISTRO DE ENTREGABLES", level=1)
    h_anx.runs[0].font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    
    t_evid = doc.add_table(rows=6, cols=5)
    t_evid.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    ev_heads = ["Entregable", "Descripción", "Enlace / Archivo", "Captura de Pantalla / Estado", "Nota de Uso y Supervisión (HITL)"]
    for j, h in enumerate(ev_heads):
        c = t_evid.cell(0, j)
        set_cell_background(c, "1B365D")
        set_cell_margins(c, top=80, bottom=80, left=80, right=80)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.size = Pt(8.5)
        
    evid_data = [
        ("Dashboard Financiero Interactivo", "Live Artifact interactivo con KPIs de EBITDA, SIPOC visual y simulador predictivo", "dashboard_financiero_taranis_black.html", "[Verificado y Operativo en Navegador]", "Permite ajustar sliders de fletes y cancelaciones para ver el impacto en tiempo real."),
        ("Prompt Maestro de Análisis Forense", "Prompt estructurado para procesamiento de estados financieros y detección de anomalías", "Prompts_Financieros_Claude.txt", "[Validado con Claude 3.7 Sonnet]", "Requiere validación de umbrales contables por el Controller antes de reclasificar."),
        ("Matriz Lean SIPOC As-Is / To-Be", "Mapeo completo de las 5 etapas del flujo de pedidos y métricas de desperdicio", "Sección SIPOC del Informe", "[Documentado en Tabla 1]", "Auditoría de tiempos de ciclo y validación de SLAs entre SP y CD Joinville."),
        ("Diagrama de Causa-Efecto (Ishikawa)", "Análisis estructural de las 6M con causas de 2do y 3er nivel para el retraso de 5 días", "Sección Ishikawa del Informe", "[Estructura 6M Validada]", "Alineación en comités semanales entre logística, finanzas y ventas."),
        ("Política de IA Responsable y LGPD", "Manual de cumplimiento normativo, gobernanza de datos y comité de ética", "Sección Etapa 3 del Informe", "[Aprobada para Auditoría]", "Supervisión permanente del DPO y CISO bajo cláusula Zero Data Retention.")
    ]
    
    for row_idx, data in enumerate(evid_data, start=1):
        for col_idx, text in enumerate(data):
            c = t_evid.cell(row_idx, col_idx)
            set_cell_background(c, "FFFFFF" if row_idx % 2 == 1 else "F9FBFD")
            set_cell_margins(c, top=70, bottom=70, left=70, right=70)
            p = c.paragraphs[0]
            r = p.add_run(text)
            r.font.size = Pt(8)
            if col_idx == 0:
                r.font.bold = True

    doc.add_paragraph()
    
    # Video Demostración
    h_vid = doc.add_heading("GUION PARA VIDEO DE DEMOSTRACIÓN (MÁX. 5 MINUTOS)", level=1)
    h_vid.runs[0].font.color.rgb = RGBColor(0x1B, 0x36, 0x5D)
    
    doc.add_paragraph(
        "Enlace del Video de Demostración: [Pendiente de grabación por el estudiante en Loom / Drive / YouTube no listado]\n\n"
        "Estructura del Guion de 5 Minutos para Francisco Israel Mesillas Hernández:\n"
        "• Minuto 0:00 - 0:45 | Introducción e Impacto de Negocio: Saludo al evaluador de ONE/Alura. Presentación personal y contexto de Taranis Black: explicar cómo una empresa sólida de USD 48.5M en ventas perdió USD 4.08M en EBITDA por operar con procesos manuales en 3 hojas de cálculo y un ERP legado.\n"
        "• Minuto 0:45 - 2:00 | Diagnóstico Lean (SIPOC e Ishikawa): Mostrar el cuello de botella central: 48 horas de retención en crédito y transcripción manual que genera 6.8% de errores. Destacar las 3 causas raíz que destruyen valor (fletes de emergencia, cancelaciones y morosidad desatendida).\n"
        "• Minuto 2:00 - 3:30 | La Solución de IA y Live Artifact: Presentar el AI Canvas y los 3 casos de uso. Demostrar el Dashboard Financiero Interactivo en pantalla: mostrar cómo la IA reduce el ciclo de 5 días a <24 horas y cómo el simulador predictivo proyecta un salto de USD 1.57M en EBITDA trimestral.\n"
        "• Minuto 3:30 - 4:15 | Gobernanza y Human-in-the-Loop (HITL): Explicar los umbrales de supervisión humana (>USD 50k en crédito, validación fiscal), la política de Zero Data Retention y el estricto cumplimiento de la LGPD.\n"
        "• Minuto 4:15 - 5:00 | Conclusión y ROI: Cerrar con las cifras clave: Inversión de USD 185k, ROI del 1,510%, recuperación de la inversión en 22 días y cierre contable en 2 días. Agradecimiento."
    )
    
    # Save file
    doc.save(filepath)
    print(f"Documento DOCX generado exitosamente en: {filepath}")

if __name__ == "__main__":
    docx_path = r"C:\Users\52477\Desktop\challengeAIbuilder\INFORME_EJECUTIVO_TARANIS_BLACK_RUTA4_FINANZAS.docx"
    create_executive_report_docx(docx_path)

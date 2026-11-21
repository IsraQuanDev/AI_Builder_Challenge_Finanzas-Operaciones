# -*- coding: utf-8 -*-
"""
Generador de archivos Markdown modulares y README.md principal para el repositorio
GitHub: IsraQuanDev/AI_Builder_Challenge_Finanzas-Operaciones
"""
import os

REPO_ROOT = r"C:\Users\52477\Desktop\challengeAIbuilder"

# -------------------------------------------------------------------------
# 1. README.md Principal
# -------------------------------------------------------------------------
readme_content = """# 📊 AI Builder Challenge — Taranis Black
## Consultoría Estratégica de Inteligencia Artificial para Finanzas y Operaciones
### Programa Oracle Next Education (ONE) & Alura Latam | Cohorte G11

[![GitHub License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Ruta Especialización](https://img.shields.io/badge/Ruta%204-Finanzas%20%26%20Operaciones-amber.svg)](https://github.com/IsraQuanDev/AI_Builder_Challenge_Finanzas-Operaciones)
[![Evaluación](https://img.shields.io/badge/ONE%20G11-AI%20for%20Business-emerald.svg)](https://www.oracle.com/lad/education/oracle-next-education/)
[![Status](https://img.shields.io/badge/Entrega-Completa%20%26%20Auditada-success.svg)]()

---

## 👤 Identificación del Estudiante y Consultor
* **Nombre completo:** Francisco Israel Mesillas Hernández
* **Correo electrónico:** israel.mecillas@gmail.com
* **Usuario GitHub:** [@IsraQuanDev](https://github.com/IsraQuanDev)
* **Programa:** Oracle Next Education (ONE) & Alura Latam
* **Cohorte:** G11 — AI for Business
* **Ruta Elegida:** **Ruta 4 — IA para Finanzas y Operaciones**

---

## 🏢 Contexto de Negocio: Taranis Black
**Taranis Black** es una empresa de referencia en mobiliario ergonómico de alta gama (sillas *ErgoPro*, mesas elevables *SmartDesk*, cabinas acústicas *Silence* y periféricos ergonómicos certificados bajo la norma NR-17). Con ingresos brutos anuales de **USD 48.50 millones** (70% canal B2B corporativo y 30% canal D2C e-commerce), la compañía enfrenta una severa crisis de rentabilidad operativa.

### El Problema Central
Toda la conciliación financiera, aprobación de crédito y asignación logística se gestiona copiando y pegando datos manualmente entre **tres hojas de cálculo de Excel locales** y un **ERP legado sin APIs**. Este flujo arcaico genera:
1. **Retraso crónico de 5 días hábiles** en el cierre contable mensual.
2. **Retención de 24 a 48 horas** para aprobar cualquier orden de crédito en la bandeja del Gerente Financiero.
3. **6.8% de divergencias y errores** en emisión de Notas Fiscales (NF-e) y órdenes de despacho al CD Joinville (SC).
4. **Colapso del EBITDA:** De USD 9.85M presupuestados a solo USD 5.77M reales (**-41.4% de caída**), destruyendo **USD 4,078,000 en ganancias**.

---

## 🚀 Resumen de la Solución Propuesta (Hoja de Ruta de IA)
Se diseñó un ecosistema de IA escalable y no invasivo que moderniza la operación sin requerir el costoso reemplazo del ERP:
1. **Agente Inteligente de Ingesta OCR+LLM (Order-to-ERP):** Extrae y valida propuestas B2B en PDF en <3 minutos con 99% de exactitud, verificando stock, lista de precios y reglas de flete CIF/FOB.
2. **Motor Predictivo de Scoring Crediticio B2B:** Algoritmo supervisado que consulta la API de Serasa Experian y aprueba pedidos <USD 50k en 15 minutos bajo una matriz de alzada descentralizada.
3. **Conciliador Financiero Cognitivo y Cierre Continuo:** Conciliación automatizada multifuente que reduce el cierre mensual de 7 a 2 días hábiles y erradica horas extras.

### Métricas de Impacto y Retorno de Inversión (ROI)
* **Inversión Requerida (Año 1):** USD 185,000.
* **Beneficio Económico Bruto Capturado:** **USD 2,980,000 anuales**.
* **Retorno sobre la Inversión (ROI):** **1,510.8%**.
* **Periodo de Recuperación (Payback):** **0.74 meses (~22 días laborables)**.
* **Ahorro de Tiempo Operativo:** 92.5% por pedido (de 40 a 3 minutos).

---

## 📁 Estructura del Repositorio

El repositorio se encuentra estructurado en carpetas temáticas para facilitar la revisión y auditoría del comité evaluador:

```text
├── README.md                                          # Portal principal del repositorio
├── INFORME_EJECUTIVO_TARANIS_BLACK_RUTA4_FINANZAS.docx # Informe oficial formateado en Word listo para entrega
├── INFORME_EJECUTIVO_TARANIS_BLACK_RUTA4_FINANZAS.md   # Informe maestro completo en Markdown
│
├── 01_Estrategia_Ruta0_Corporativa/
│   ├── AI_Canvas_Taranis_Black.md                     # AI Canvas y 3 casos de uso detallados
│   ├── Matriz_Esfuerzo_Impacto_y_ROI.md               # Matriz 4 cuadrantes, cálculo formal de ROI y ADKAR
│   └── Politica_Gobernanza_Etica_LGPD.md              # Matriz de uso permitido/prohibido, LGPD y Comité
│
├── 02_Diagnostico_Lean_Operaciones/
│   ├── Matriz_SIPOC_Flujo_AsIs_ToBe.md                # Matriz SIPOC (Lead Time 5d vs Touch Time 65 min)
│   ├── Diagrama_Ishikawa_6M_Causa_Raiz.md             # Diagrama de Ishikawa 6M y las 3 causas cuantitativas
│   └── Intervencion_Prioritaria_Recomendada.md        # Justificación de la intervención prioritaria
│
├── 03_Panel_Financiero_y_Predictivo/
│   ├── dashboard_financiero_taranis_black.html         # Live Artifact interactivo (Tailwind CSS + Chart.js)
│   ├── Analisis_Anomalias_y_Erosion_EBITDA.md         # Auditoría forense de los USD 4.08M en sobrecostos
│   └── Proyeccion_Predictiva_T1_2027.md               # Modelo predictivo en USD (Inercial vs Con IA)
│
├── 04_Prompts_y_Scripts/
│   ├── Prompts_Claude_Auditoria_Financiera.md          # Prompts reproducibles ejecutados en Claude 3.7
│   └── scripts_generacion/
│       ├── generate_docs.py                            # Script generador del DOCX oficial
│       ├── generate_html_dashboard.py                  # Script constructor del Live Artifact
│       └── generate_markdown_report.py                 # Script compilador del reporte Markdown
│
├── 05_Evidencias_y_Entrega_Alura/
│   ├── Tabla_Oficial_de_Evidencias.md                 # Matriz oficial con enlaces y notas HITL
│   └── Guion_Video_Demostracion_5min.md               # Guion técnico para el video de presentación
│
└── Kit_de_datos_Taranis_Black_ES/                      # Insumos oficiales proporcionados por Alura
```

---

## 🖥️ Live Artifact: Panel Financiero Interactivo
El archivo [`03_Panel_Financiero_y_Predictivo/dashboard_financiero_taranis_black.html`](03_Panel_Financiero_y_Predictivo/dashboard_financiero_taranis_black.html) contiene una aplicación web interactiva que incluye:
* **Tablero Ejecutivo:** Gráficos dinámicos de colapso trimestral de EBITDA y descomposición de sobrecostos operativos.
* **Navegador Lean:** Matriz SIPOC visual y Diagrama de Ishikawa 6M navegable.
* **Simulador Predictivo Q1 2027:** Controles deslizantes para simular el impacto en EBITDA al reducir fletes de emergencia y cancelaciones.
* **Gobernanza:** Matriz de cumplimiento normativo LGPD y políticas de supervisión humana (HITL).

> *Para abrir el panel, simplemente descarga el archivo HTML y haz doble clic sobre él en cualquier navegador web moderno (Chrome, Edge, Firefox).*

---

## 📎 Enlace al Video de Demostración
* **Formato:** Video ejecutivo de hasta 5 minutos
* **Plataforma:** Loom / Google Drive / YouTube No Listado
* **Enlace:** `[Pendiente de grabación por el estudiante]` *(Ver guion completo en [`05_Evidencias_y_Entrega_Alura/Guion_Video_Demostracion_5min.md`](05_Evidencias_y_Entrega_Alura/Guion_Video_Demostracion_5min.md))*

---
*Desarrollado para la entrega final del Challenge ONE G11 — AI for Business (Alura Latam & Oracle Next Education).*
"""

with open(os.path.join(REPO_ROOT, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)

# -------------------------------------------------------------------------
# 2. 01_Estrategia_Ruta0_Corporativa / AI_Canvas_Taranis_Black.md
# -------------------------------------------------------------------------
ai_canvas_content = """# AI Canvas e Identificación de Oportunidades — Taranis Black
**Programa Oracle Next Education (ONE) | Cohorte G11 | Ruta 0 (Base Estratégica)**
**Estudiante:** Francisco Israel Mesillas Hernández

---

## 1. Contexto Estratégico
Taranis Black procesa anualmente USD 48.50M en ventas de mobiliario ergonómico certificado bajo la norma NR-17. El canal corporativo B2B representa el 70% de la facturación (USD 33.6M), pero opera mediante sistemas desconectados que generan fricciones operativas masivas.

El **AI Canvas** identifica las oportunidades donde la Inteligencia Artificial genera mayor retorno económico atacando directamente las causas de ineficiencia.

---

## 2. Los 3 Casos de Uso Seleccionados

### Caso 1: Agente Inteligente de Ingesta, Extracción y Validación de Pedidos B2B (Order-to-ERP)
* **Clasificación de IA:** Generativa (Multimodal OCR + LLM) + Tradicional (Validación determinística de reglas).
* **Problema que Resuelve:** Cada propuesta comercial firmada en PDF es procesada manualmente por un asistente financiero (40 minutos por pedido). Esto provoca una tasa de error del 6.8% en la Nota Fiscal (NF-e) y órdenes de despacho al CD Joinville, causando USD 960,000 en fletes de emergencia y USD 725,000 en multas y reentregas.
* **Solución Técnica:** Pipeline automatizado que recibe el PDF desde el correo o CRM, extrae las entidades con un LLM empresarial (CNPJ, productos, acabados de mesh/aluminio, precios y términos CIF/FOB) y las valida contra la base de datos de stock y precios de lista. Una vez validada, inyecta la orden al ERP legado vía RPA o conector directo en <3 minutos.
* **Supervisión Humana (HITL):** Obligatoria cuando el índice de confianza del OCR/LLM sea menor al 95%, si existe una divergencia de precio superior al 1%, o si falta el comprobante de domicilio fiscal actualizado.

### Caso 2: Motor Predictivo de Scoring Crediticio B2B y Aprobación Descentralizada
* **Clasificación de IA:** Predictiva (Machine Learning Supervisado - XGBoost) + Motor de Reglas de Negocio.
* **Problema que Resuelve:** Inexistencia de matriz de alzada automatizada. Cualquier pedido corporativo (desde USD 8,000 hasta USD 150,000) debe ser aprobado individualmente por el Gerente Financiero por correo electrónico. Debido a viajes y comités, los correos quedan retenidos de 24 a 48 horas hábiles, provocando USD 1,250,000 anuales en cancelaciones de clientes urgentes.
* **Solución Técnica:** Algoritmo predictivo entrenado con el historial de pagos de 24 meses de clientes de Taranis Black, integrado vía API con el buró Serasa Experian. Clasifica a los compradores en cuatro bandas de riesgo (Verde, Amarillo, Naranja, Rojo) y aprueba automáticamente pedidos menores a USD 50,000 para clientes en banda Verde en menos de 15 minutos.
* **Supervisión Humana (HITL):** Obligatoria para órdenes mayores a USD 50,000, clientes nuevos sin historial en banda amarilla, o solicitudes con plazos de pago extendidos (>90 días). Los rechazos de crédito exigen doble verificación humana.

### Caso 3: Conciliador Financiero Cognitivo y Cierre Contable Continuo
* **Clasificación de IA:** Tradicional (Algoritmos de reconciliación determinística) + Generativa (Explicabilidad y redacción de notas contables).
* **Problema que Resuelve:** Toda la conciliación de ingresos, costos de flete y crédito se efectúa manualmente cruzando tres hojas de cálculo locales (`Controle_Limites_2026.xlsx`, lista de precios y control de fletes). Esto retrasa el cierre contable 5 días hábiles cada mes, demanda USD 180,000 en horas extras y auditorías, y oculta una morosidad de USD 1,110,000.
* **Solución Técnica:** Conector que cruza en tiempo real los extractos bancarios, las NF-e emitidas y las partidas del ERP legado. El LLM analiza las discrepancias no cuadradas, genera sugerencias de asientos de reclasificación y redacta un informe ejecutivo diario para la Controllería.
* **Supervisión Humana (HITL):** El Controller debe revisar y firmar digitalmente cualquier ajuste contable, reversión o provisión de incobrabilidad (PDD) que supere los USD 5,000.

---

## 3. Justificación de Tipos de IA y Filosofía Human-in-the-Loop (HITL)

| Pregunta Clave | Justificación Técnico-Estratégica |
| :--- | :--- |
| **¿Por qué IA Generativa en Ingesta?** | Los documentos B2B (órdenes de compra, pedidos escaneados, contratos firmados electrónicamente) carecen de estructura estándar. Los sistemas de reglas rígidas fallan ante variaciones tipográficas; los LLMs poseen comprensión semántica y flexibilidad contextual. |
| **¿Por qué IA Predictiva en Crédito?** | La evaluación de riesgo financiero requiere analizar patrones multivariables (score externo, apalancamiento, estacionalidad sectorial). Un modelo de Machine Learning predice la probabilidad de incumplimiento de forma objetiva, sin sesgos humanos ni demoras. |
| **¿Por qué Supervisión Humana (HITL)?** | En operaciones financieras, las alucinaciones conllevan sanciones fiscales ante la Receita Federal y pérdidas directas de liquidez. El marco HITL asegura que la IA funcione como un asistente aumentativo, dejando la soberanía y responsabilidad en el equipo directivo. |
"""

with open(os.path.join(REPO_ROOT, "01_Estrategia_Ruta0_Corporativa", "AI_Canvas_Taranis_Black.md"), "w", encoding="utf-8") as f:
    f.write(ai_canvas_content)

# -------------------------------------------------------------------------
# 3. 01_Estrategia_Ruta0_Corporativa / Matriz_Esfuerzo_Impacto_y_ROI.md
# -------------------------------------------------------------------------
matriz_roi_content = """# Matriz de Esfuerzo × Impacto, ROI y Gestión del Cambio
**Programa Oracle Next Education (ONE) | Cohorte G11 | Ruta 0 (Base Estratégica)**
**Estudiante:** Francisco Israel Mesillas Hernández

---

## 1. Matriz de Priorización Esfuerzo × Impacto

```
                  ALTO IMPACTO EN NEGOCIO
                            ▲
                            │
        [QUICK WIN]         │      [ESTRATÉGICO]
   1. Ingesta Inteligente   │  2. Motor Predictivo de Crédito
      OCR+LLM de Pedidos    │     (Integración Serasa / Reglas)
   (Bajo Esfuerzo /         │  3. Conciliador Financiero
    Alto Impacto)           │     y Cierre Contable Continuo
                            │
  ──────────────────────────┼──────────────────────────► ESFUERZO TÉCNICO
                            │
        [FILL-INS]          │      [DESCARTADO]
   Generador de borradores  │  Reemplazo integral del ERP
   de correos de cobranza   │  legado por un nuevo core
   preventiva por WhatsApp  │  (Esfuerzo >USD 1.5M / >18 meses
                            │   Riesgo de parálisis operativa)
                            │
                  BAJO IMPACTO EN NEGOCIO
```

### Justificación del Cronograma de Despliegue
* **Fase 1 (Mes 1) — Quick Win:** *Ingesta Inteligente OCR+LLM*. Implementación ágil utilizando microservicios existentes de visión y LLM empresarial. Detiene de inmediato los errores de códigos y fletes de emergencia.
* **Fase 2 (Mes 2) — Proyecto Estratégico:** *Motor Predictivo de Crédito*. Integración vía API con Serasa Experian y parametrización de reglas de alzada. Rescata USD 1.25M en pedidos cancelados por demora.
* **Fase 3 (Mes 3) — Proyecto Estratégico:** *Conciliador Financiero Cognitivo*. Conexión de libros contables y hojas de cálculo para lograr cierres continuos en 48 horas.
* **Iniciativa Descartada:** *Reemplazo Integral del ERP*. Descartada por alto riesgo operativo, costos superiores a USD 1.5M y tiempo de implementación mayor a 18 meses.

---

## 2. Métricas de Éxito y Cálculo Formal del ROI

### A. Inversión Estimada (CAPEX/OPEX Año 1)
| Concepto | Costo Estimado (USD) | Detalle de la Partida |
| :--- | :---: | :--- |
| Licencias API Empresariales (LLM/OCR Zero Data Retention) | 45,000 | Tokens para 2,500 propuestas/año y procesamiento continuo |
| Conectores RPA, Base de Datos y Microservicios | 55,000 | Infraestructura en la nube con cifrado AES-256 |
| Consultoría de Integración y Desarrollo de Modelos | 65,000 | Especialistas en arquitectura financiera y machine learning |
| Capacitación, Change Management y Contingencias | 20,000 | Formación de analistas financieros y material didáctico |
| **TOTAL INVERSIÓN AÑO 1** | **USD 185,000** | Inversión total amortizable en el ejercicio |

### B. Beneficios Económicos Anuales Cuantificados
| Línea de Ahorro / Captura de Valor | Ahorro Anual (USD) | Métrica Operativa de Origen |
| :--- | :---: | :--- |
| Eliminación de fletes expresos por errores | 960,000 | Tasa de flete baja de 2.8% a 1.0% de facturación |
| Margen rescatado de pedidos cancelados por lentitud | 850,000 | Aprobación en 15 min rescata USD 1.25M en ventas |
| Reducción de multas y reentregas por divergencias | 390,000 | Tasa de error en NF-e cae de 6.8% a <0.5% |
| Disminución de cartera vencida y morosidad (PDD) | 650,000 | Morosidad >90 días desciende de 3.4% a 1.2% |
| Ahorro en horas extras y auditorías de cierre | 130,000 | Cierre mensual se completa en 2 días hábiles |
| **BENEFICIO BRUTO TOTAL ANUAL** | **USD 2,980,000** | Retorno directo en EBITDA operativo |

### C. Cálculos Financieros
* **Beneficio Neto:** $\text{USD } 2,980,000 - \text{USD } 185,000 = \mathbf{USD\ 2,795,000}$.
* **Retorno sobre la Inversión (ROI):**
  $$\text{ROI} = \frac{\text{USD } 2,795,000}{\text{USD } 185,000} \times 100 = \mathbf{1,510.8\%}$$
* **Periodo de Recuperación (Payback):**
  $$\text{Payback} = \frac{\text{USD } 185,000}{\text{USD } 2,980,000} \times 12 \text{ meses} = \mathbf{0.74 \text{ meses (~22 días hábiles)}}$$
* **Horas Hombre Liberadas:** Reducción del tiempo de tramitación de 40 a 3 minutos por pedido (**92.5% de ahorro**), liberando más de 1,480 horas anuales en el equipo financiero.

---

## 3. Plan de Gestión del Cambio Organizacional (ADKAR)

1. **Awareness (Conciencia):** Presentación ejecutiva a los equipos mostrando que el proceso manual destruye USD 4.08M en EBITDA y satura al personal con horas extras. La IA se presenta como un salvavidas operativo.
2. **Desire (Deseo):** Transformación del puesto de los colaboradores: de "Digitadores Contables" a **"Analistas de Inteligencia Financiera"**, con bonificaciones por calidad de cartera y velocidad de ciclo.
3. **Knowledge (Conocimiento):** Talleres prácticos sobre resolución de alertas de excepción, supervisión de IA y prompts financieros.
4. **Ability (Habilidad):** Operación en paralelo (*Shadow Run*) durante 4 semanas: la IA genera sugerencias que el personal valida con un clic.
5. **Reinforcement (Refuerzo):** Reconocimiento público de metas de cierre contable en 48 horas sin turnos de madrugada.
"""

with open(os.path.join(REPO_ROOT, "01_Estrategia_Ruta0_Corporativa", "Matriz_Esfuerzo_Impacto_y_ROI.md"), "w", encoding="utf-8") as f:
    f.write(matriz_roi_content)

# -------------------------------------------------------------------------
# 4. 01_Estrategia_Ruta0_Corporativa / Politica_Gobernanza_Etica_LGPD.md
# -------------------------------------------------------------------------
gov_content = """# Política de Gobernanza, Ética y Cumplimiento Normativo (LGPD)
**Programa Oracle Next Education (ONE) | Cohorte G11 | Ruta 0 (Base Estratégica)**
**Estudiante:** Francisco Israel Mesillas Hernández

---

## 1. Política de IA Responsable: Matriz de Usos Permitidos y Prohibidos

| Prácticas Permitidas y Buenas Conductas (`Compliance`) | Prácticas Estrictamente Prohibidas (`Riesgo Crítico`) |
| :--- | :--- |
| **✔ Uso exclusivo de endpoints empresariales de IA** con acuerdos jurídicos vinculantes de **Zero Data Retention** (no entrenamiento con datos de Taranis Black). | **✖ Ingesta de información financiera o datos de clientes en herramientas públicas**, gratuitas o extensiones no autorizadas. |
| **✔ Extracción de entidades transaccionales B2B** (ítems de catálogo, CNPJ, cantidades, fletes CIF/FOB y precios de lista). | **✖ Carga de datos personales sensibles** de empleados o clientes (salud, origen, ideología, cuentas bancarias de personas físicas). |
| **✔ Scoring crediticio y sugerencia de límites** bajo reglas objetivas, transparentes y auditables por el equipo de crédito. | **✖ Denegación automática de crédito a clientes sin fundamentación matemática** o sin derecho humano a réplica. |
| **✔ Generación asistida de notas de ajuste contable** requiriendo siempre la firma digital y validación del Controller. | **✖ Ejecución de pagos bancarios**, dispersión de nómina o transferencias de tesorería de forma autónoma por la IA. |
| **✔ Anonimización previa de identificadores personales** mediante microservicios locales antes de llamadas a APIs externas. | **✖ Inclusión de credenciales**, contraseñas de ERP o certificados digitales (A1/A3) en prompts de modelos de lenguaje. |

---

## 2. Gestión de Riesgos y Cumplimiento de la LGPD (Brasil - Ley 13.709/2018)

* **Protección de Datos Personales:** Aunque el 70% de las ventas corresponden a personas jurídicas (B2B), los contratos incluyen nombres, firmas, correos y CPFs de representantes legales y compradores. Se implementa un filtro DLP (*Data Loss Prevention*) que sustituye automáticamente identificadores personales por tokens antes de enviarlos al modelo de lenguaje.
* **Mitigación de Sesgos Algorítmicos en Crédito:** El modelo de scoring se calibra y audita trimestralmente para garantizar que no discrimine a empresas por su ubicación geográfica (fuera de São Paulo o Santa Catarina) ni por antigüedad en el mercado, evaluando exclusivamente solvencia, liquidez e historial crediticio.
* **Prevención de Alucinaciones:** Toda salida del LLM se valida contra esquemas JSON estrictos y se contrasta determinísticamente con el padrón fiscal oficial de la *Receita Federal* (Sintegra) y la lista de precios vigente de Taranis Black.

---

## 3. Estructura del Comité de Ética e IA y Auditorías

### Integrantes del Comité
1. **Chief Financial Officer (CFO) / Controller:** Presidente del Comité; custodia la integridad financiera y fiscal.
2. **Data Protection Officer (DPO) / Asesor Legal:** Garantiza el apego a la LGPD y normativas comerciales.
3. **Gerente de Ciberseguridad e Infraestructura TI (CISO):** Administra la seguridad de APIs, cifrado y accesos.
4. **Gerente de Operaciones y Logística:** Asegura el cumplimiento de SLAs de entrega entre SP y Joinville.
5. **Lead AI Engineer / Product Owner:** Supervisa la precisión técnica, latencia y deriva algorítmica.

### Frecuencia de Auditorías
* **Fase Piloto (Días 1 a 90):** Revisiones **quincenales** de precisión de extracción y aprobación crediticia.
* **Operación Ordinaria:** Sesiones formales **bimestrales** y auditoría externa anual de ciberseguridad.
"""

with open(os.path.join(REPO_ROOT, "01_Estrategia_Ruta0_Corporativa", "Politica_Gobernanza_Etica_LGPD.md"), "w", encoding="utf-8") as f:
    f.write(gov_content)

# -------------------------------------------------------------------------
# 5. 02_Diagnostico_Lean_Operaciones / Matriz_SIPOC_Flujo_AsIs_ToBe.md
# -------------------------------------------------------------------------
sipoc_content = """# Mapeo Lean y Matriz SIPOC: Aprobación de Pedidos, Facturación y Expedición B2B
**Programa Oracle Next Education (ONE) | Cohorte G11 | Ruta 4 (Finanzas y Operaciones)**
**Estudiante:** Francisco Israel Mesillas Hernández

---

## 1. Contexto del Macroproceso
Taranis Black factura entre 180 y 220 pedidos corporativos al mes (USD 33.6M anuales en canal B2B). La meta corporativa establece que el ciclo total entre la firma comercial y el despacho físico no debe superar **24 horas útiles**. Actualmente, el proceso manual promedia **más de 5 días hábiles**.

---

## 2. Matriz SIPOC As-Is (Proceso Actual)

| S (Suppliers / Proveedores) | I (Inputs / Entradas) | P (Process / Macroproceso Actual As-Is) | O (Outputs / Salidas) | C (Customers / Clientes) |
| :--- | :--- | :--- | :--- | :--- |
| **Consultores B2B y SDRs (SP)** | Propuesta comercial firmada en PDF escaneado (anexo a correo electrónico) | **1. Recepción y Selección de Propuestas:** Vendedor envía correo informal a `financiero@taranisblack.com.br`. En fin de mes ingresan >40 correos sin prioridad ni validación de inventario. *(Tiempo: 2-4 horas en bandeja)*. | Correo electrónico en cola de entrada no estructurado | Asistente Financiero |
| **Compradores B2B y Serasa Experian** | Datos cadastrales (CNPJ, IE, Dirección) y Score de crédito Serasa | **2. Consulta de Crédito Manual:** Asistente abre PDF y alterna en 3 pantallas: ERP legado, portal web Serasa y Excel `Controle_Limites_2026.xlsx`. *(Tiempo de ciclo: 40 min/pedido)*. | Dossier de crédito preliminar en Excel local | Gerente Financiero (Aprobador de alzada) |
| **Gerente Financiero (Aprobador)** | Resumen informal por correo ("¿Podemos facturar USD 85k a Empresa X?") | **3-4. Solicitud y Espera de Decisión:** Como no hay motor de reglas, cualquier pedido depende del Gerente. Debido a viajes y reuniones, el correo queda retenido. *(Tiempo de retención: 24h a 48h hábiles)*. | Correo informal de respuesta con el "De acuerdo" | Asistente Financiero / Facturación |
| **Asistente Financiero de Facturación** | Aprobación por email y tabla de precios comercial en Excel | **5a. Facturación Manual en ERP:** Asistente digita a mano la NF-e en el ERP legado. Errores del 6.8% en códigos de producto, colores de tela o inscripción estatal. *(Tiempo: 30 min/pedido)*. | DANFE, archivo XML de NF-e y boletos bancarios 30/60/90 | Cliente Corporativo B2B y Contabilidad |
| **Centro de Distribución (Joinville) y Transportadoras** | Correo a `expedicao.cd@` y tabla de fletes homologados | **5b. Notificación y Despacho:** Asistente autoriza la separación por correo. Divergencias en flete CIF/FOB paralizan camiones acumulando estadías y fletes dobles. *(Tiempo: 24h a 48h)*. | Picking List, Minuta de Embarque y Mercancía despachada | Cliente Corporativo B2B Receptor |

---

## 3. Diagnóstico Lean de Valor Agregado vs. Desperdicio (Muda)
* **Tiempo Total de Ciclo (Lead Time As-Is):** 5 a 7 días hábiles (~2,400 minutos hábiles).
* **Tiempo de Agregación Real de Valor (Touch Time):** ~65 minutos (revisión de crédito, emisión de NF y generación de picking).
* **Eficiencia del Ciclo del Proceso (PCE):**
  $$\text{PCE} = \frac{65 \text{ min}}{2,400 \text{ min}} \times 100 = \mathbf{2.7\%}$$
* **Conclusión:** El **97.3% del tiempo** es desperdicio puro (espera de correos y sobreprocesamiento manual por falta de integración).

---

## 4. Matriz SIPOC To-Be (Flujo Optimizado con IA)
* **Ingesta:** El PDF se procesa mediante OCR+LLM en <3 minutos.
* **Crédito:** Aprobación automática en 15 minutos para pedidos <USD 50k con Serasa >700.
* **Facturación:** NF-e generada automáticamente vía RPA sin digitación humana.
* **Despacho:** Picking List enviado a Joinville en tiempo real.
* **Tiempo Total de Ciclo To-Be:** **<24 horas útiles** (PCE se eleva al **65.0%**).
"""

with open(os.path.join(REPO_ROOT, "02_Diagnostico_Lean_Operaciones", "Matriz_SIPOC_Flujo_AsIs_ToBe.md"), "w", encoding="utf-8") as f:
    f.write(sipoc_content)

# -------------------------------------------------------------------------
# 6. 02_Diagnostico_Lean_Operaciones / Diagrama_Ishikawa_6M_Causa_Raiz.md
# -------------------------------------------------------------------------
ishikawa_content = """# Diagrama de Ishikawa (Espina de Pescado — Las 6M)
**Programa Oracle Next Education (ONE) | Cohorte G11 | Ruta 4 (Finanzas y Operaciones)**
**Estudiante:** Francisco Israel Mesillas Hernández

---

## 1. Problema Central (Efecto Crítico)
**Retraso crónico de 5 días en el cierre contable mensual y ciclo de facturación excesivo de 5 días hábiles, causando la pérdida de USD 4,078,000 en EBITDA anual.**

---

## 2. Diagrama Estructurado de las 6M

```
       MÉTODO                                MÁQUINA                             MANO DE OBRA
Flujo dependiente de emails ──┐        ERP obsoleto sin APIs ───────┐        Asistentes sobrecargados con ─┐
Sin POP documentado ──────────┤        Dependencia de 3 Excels ─────┤        copiar y pegar (burnout)      │
Sin matriz de alzada autom. ──┼──┐     Cero tecnología OCR/IA ──────┼──┐     Gerente ausente por comités ──┼──┐
Regla CIF/FOB no verificada ──┘  │     Consulta manual a Serasa ────┘  │     y viajes a Joinville (cuello) ┘  │
                                 │                                     │                                      │
                                 ├─────────────────────────────────────┴──────────────────────────────────────┼──► RETRASO DE 5 DÍAS
                                 │                                                                            │    EN CIERRE & CICLO
                                 │                                                                            │    DE FACTURACIÓN
Falta comprobante dirección ──┐  │     Sin monitoreo de SLA real ───┐        Fricción cultural São Paulo ──┐  │
Códigos de tela divergentes ──┼──┘     Directora enterada a fin ────┼──┘     vs. CD Joinville              │  │
Propuestas incompletas ───────┘        de mes (reactivo)            │        Cultura de "apagar incendios"─┼──┘
                                       Sin alertas de morosidad ────┘        Silos departamentales ────────┘
       MATERIAL                              MEDICIÓN                            MEDIO AMBIENTE
```

---

## 3. Análisis Causal por Cada una de las 6M

### ⚙️ 1. Método (Procesos)
* Ausencia total de Procedimientos Operativos Estandarizados (POP) formalizados.
* Dependencia absoluta de hilos de correo electrónico informales y sin trazabilidad.
* Inexistencia de matriz de alzada: cualquier orden exige el visto bueno del gerente.
* Falta de validación contractual previa de flete CIF/FOB al cerrar la venta.

### 💻 2. Máquina (Sistemas & Tecnología)
* ERP legado sin capacidad de integración mediante APIs modernas.
* Cero tecnología OCR o IA para procesar órdenes comerciales en PDF.
* Dependencia crítica de 3 hojas de cálculo locales (`Controle_Limites_2026.xlsx`, lista de precios y fletes).
* Consulta manual al portal web de Serasa Experian.

### 👥 3. Mano de Obra (Personas)
* Asistentes financieros atrapados en tareas alienantes de copiar y pegar (40 min por pedido).
* Estrés severo, desmotivación y rotación de personal en los cierres mensuales (burnout).
* Gerente Financiero sobrecargado con comités y viajes a Joinville, creando un embudo físico.

### 📄 4. Material (Insumos & Documentos)
* Formularios comerciales con campos vacíos o ilegibles enviados por vendedores.
* Divergencia habitual entre códigos del catálogo comercial y registros maestros del ERP.
* Comprobantes de dirección fiscal desactualizados de clientes corporativos.

### 📊 5. Medición (Indicadores)
* Cero monitoreo de SLAs por etapa en tiempo real.
* La Dirección General y Controllería descubren los retrasos cuando el mes ya cerró.
* Falta de visibilidad de pedidos congelados por departamento.

### 🏢 6. Medio Ambiente (Cultura Organizacional)
* Fricción y silos departamentales entre el equipo de ventas en São Paulo y el CD en Joinville.
* Cultura reactiva de "apagar incendios" en lugar de solucionar la causa raíz.
"""

with open(os.path.join(REPO_ROOT, "02_Diagnostico_Lean_Operaciones", "Diagrama_Ishikawa_6M_Causa_Raiz.md"), "w", encoding="utf-8") as f:
    f.write(ishikawa_content)

# -------------------------------------------------------------------------
# 7. 02_Diagnostico_Lean_Operaciones / Intervencion_Prioritaria_Recomendada.md
# -------------------------------------------------------------------------
interv_content = """# Intervención Prioritaria Recomendada y Cuantificación de Causas
**Programa Oracle Next Education (ONE) | Cohorte G11 | Ruta 4 (Finanzas y Operaciones)**
**Estudiante:** Francisco Israel Mesillas Hernández

---

## 1. Las 3 Causas Principales del Desempeño Deficiente

1. **Aprobación de Crédito Manual y Centralizada (Cuello de Botella de 48h):**
   * *Impacto:* USD 1,250,000 anuales en cancelaciones directas por clientes insatisfechos.
   * *Causa Raíz:* Dependencia del correo del Gerente Financiero para cualquier importe.
2. **Transcripción Manual de Propuestas al ERP (Tasa de Error del 6.8%):**
   * *Impacto:* USD 960,000 en fletes de emergencia duplicados y USD 725,000 en multas y reentregas.
   * *Causa Raíz:* Copia manual de datos de PDFs a tres hojas de Excel y al ERP.
3. **Conciliación Manual en 3 Excels Locales Desconectados:**
   * *Impacto:* Retraso crónico de 5 días en el cierre de mes, USD 180,000 en horas extras y USD 1,110,000 en morosidad desatendida.
   * *Causa Raíz:* Falta de sincronización de datos y ausencia de automatización contable.

---

## 2. Intervención Prioritaria Seleccionada
**Intervención:** Implementar en el Mes 1 el **Agente Inteligente de Ingesta OCR+LLM y Motor Descentralizado de Aprobación de Crédito**.

### Justificación Estratégica y Económica
1. **Erradica el Origen del Desperdicio:** Si los datos entran limpios al ERP desde el inicio, se eliminan el 95% de los errores en órdenes de despacho y facturas electrónicas.
2. **Impacto Financiero Inmediato:** Recupera **USD 2.21 millones** en el primer semestre al desactivar las cancelaciones de USD 1.25M y eliminar los fletes duplicados de USD 960k.
3. **Facilita la Fase Contable:** Con los pedidos cargados automáticamente en el ERP, la posterior conciliación contable se simplifica en más del 80%.
"""

with open(os.path.join(REPO_ROOT, "02_Diagnostico_Lean_Operaciones", "Intervencion_Prioritaria_Recomendada.md"), "w", encoding="utf-8") as f:
    f.write(interv_content)

# -------------------------------------------------------------------------
# 8. 03_Panel_Financiero_y_Predictivo / Analisis_Anomalias_y_Erosion_EBITDA.md
# -------------------------------------------------------------------------
anomalias_content = """# Análisis Forense de Anomalías Financieras y Erosión de EBITDA
**Programa Oracle Next Education (ONE) | Cohorte G11 | Ruta 4 (Finanzas y Operaciones)**
**Estudiante:** Francisco Israel Mesillas Hernández

---

## 1. El Misterio Financiero de Taranis Black
* **Ingresos Brutos Presupuestados:** USD 48,600,000.
* **Ingresos Brutos Reales:** USD 48,500,000 (**99.8% de cumplimiento de meta comercial**).
* **EBITDA Presupuestado:** USD 9,848,000 (20.3% de margen).
* **EBITDA Real:** USD 5,770,000 (11.9% de margen).
* **Brecha Destructiva de EBITDA:** **-USD 4,078,000 (-41.4% de caída)**.

---

## 2. Las 5 Mayores Anomalías Financieras Identificadas

| Cuenta Contable Afectada | Presupuesto Anual (USD) | Realizado Anual (USD) | Desviación Crítica (USD) | Desvío (%) | Hallazgo Financiero & Causa Operativa |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Fletes y Logística CD Joinville** | 2,380,000 | 3,740,000 | **+1,360,000** | **+57.1%** | Contratación masiva de fletes aéreos y expresos dedicados para compensar el atraso de 5 días. |
| **Cancelaciones por Retraso** | 560,000 | 1,235,000 | **+675,000** | **+120.5%** | Pedidos corporativos firmados que se cayeron por demoras de 48h en la aprobación del crédito. |
| **Provisión Deudores Dudosos (PDD)** | 440,000 | 1,110,000 | **+670,000** | **+152.3%** | Morosidad >90 días trepó de 1.2% a 3.4% por cobranza manual mediante correos sueltos. |
| **Reentregas y Multas por Divergencia** | 210,000 | 725,000 | **+515,000** | **+245.2%** | 6.8% de NF-e emitidas con discrepancias en códigos de tela o flete CIF/FOB. |
| **Gastos Administrativos / Sistemas** | 1,760,000 | 2,020,000 | **+260,000** | **+14.8%** | Horas extras del personal contable y consultorías externas para conciliar a fin de mes. |

**Total de Fricción Operativa Identificada:** **USD 3,480,000** en pérdidas directas (explica el 85.3% del colapso de EBITDA).

---

## 3. Desempeño y Margen por Línea de Producto

| Línea de Producto | Presupuesto (USD) | Realizado (USD) | Margen Bruto | Cuello de Botella Operativo Observado |
| :--- | :---: | :---: | :---: | :--- |
| **Taranis ErgoPro (Sillas)** | 23,500,000 | 23,850,000 | 44.2% | Ventas altas pero margen erosionado por fletes de emergencia. |
| **Taranis SmartDesk (Mesas)** | 13,200,000 | 12,650,000 | 38.5% | Retrasos en homologación de crédito frenan despacho en 48h. |
| **Taranis Silence (Cabinas)** | 8,600,000 | 8,100,000 | 52.0% | Ciclo largo de venta (90d) y complejidad de montaje técnico. |
| **Accesorios Ergonómicos** | 2,700,000 | 2,800,000 | 61.0% | Alto volumen y tíquet bajo; conciliación de boletos sobrecarga. |
"""

with open(os.path.join(REPO_ROOT, "03_Panel_Financiero_y_Predictivo", "Analisis_Anomalias_y_Erosion_EBITDA.md"), "w", encoding="utf-8") as f:
    f.write(anomalias_content)

# -------------------------------------------------------------------------
# 9. 03_Panel_Financiero_y_Predictivo / Proyeccion_Predictiva_T1_2027.md
# -------------------------------------------------------------------------
proyeccion_content = """# Proyección Financiera Predictiva para el Próximo Trimestre (T1 2027)
**Programa Oracle Next Education (ONE) | Cohorte G11 | Ruta 4 (Finanzas y Operaciones)**
**Estudiante:** Francisco Israel Mesillas Hernández

---

## 1. Comparativa de Escenarios Trimestrales en USD

| Métrica / Cuenta Financiera | T4 Realizado (Línea Base) | T1 2027 Inercial (Sin IA) | T1 2027 Optimizado (Con IA) | Impacto Neto de la IA |
| :--- | :---: | :---: | :---: | :---: |
| **Ingresos Brutos Totales** | USD 13,400,000 | USD 13,800,000 | **USD 14,200,000** | **+USD 400,000** |
| **(-) Cancelaciones por Retraso** | -USD 420,000 | -USD 460,000 | **-USD 115,000** | **+USD 345,000** |
| **Ingresos Operativos Netos** | USD 10,702,000 | USD 11,040,000 | **USD 11,735,000** | **+USD 695,000** |
| **(-) Fletes y Logística de Entrega** | -USD 1,220,000 | -USD 1,320,000 | **-USD 528,000** | **+USD 792,000** |
| **(-) Reentregas y Multas** | -USD 260,000 | -USD 290,000 | **-USD 85,000** | **+USD 205,000** |
| **(-) Provisión Morosidad (PDD)** | -USD 390,000 | -USD 430,000 | **-USD 150,500** | **+USD 279,500** |
| **EBITDA Operativo Trimestral** | **USD 1,002,000** | **USD 950,000** | **USD 2,520,000** | **+USD 1,570,000** |
| **Margen EBITDA (%)** | **7.5%** | **6.9%** | **17.7%** | **+10.8 p.p.** |

---

## 2. Supuestos Cuantitativos del Modelo
1. **Reducción de Tiempo de Ciclo:** Aprobación en <15 min y ciclo de despacho en <24 horas eliminan el 75% de las cancelaciones comerciales.
2. **Normalización de Fletes:** La tasa de fletes expresos cae del 2.8% al 1.0% de la facturación al erradicar errores de picking.
3. **Recuperación de Morosidad:** Cobranza predictiva por WhatsApp y correo reduce la morosidad a 1.2% sobre ventas.
4. **Impacto Trimestral Neto:** Generación de **+USD 1,523,750 netos de EBITDA** en T1 2027 tras deducir amortización de software.
"""

with open(os.path.join(REPO_ROOT, "03_Panel_Financiero_y_Predictivo", "Proyeccion_Predictiva_T1_2027.md"), "w", encoding="utf-8") as f:
    f.write(proyeccion_content)

# -------------------------------------------------------------------------
# 10. 04_Prompts_y_Scripts / Prompts_Claude_Auditoria_Financiera.md
# -------------------------------------------------------------------------
prompts_content = """# Prompts Estructurados de Auditoría Financiera y Modelado Predictivo
**Ejecutados en:** Claude 3.7 Sonnet | **Estudiante:** Francisco Israel Mesillas Hernández

---

## Prompt 1: Auditoría Forense de Variaciones y Cuellos de Botella
```text
Actúa como un Senior Financial Controller y Consultor en Lean Six Sigma. Analiza integralmente las tres hojas de cálculo del archivo adjunto '05_Finanzas_Presupuesto_vs_Real.xlsx' de la empresa Taranis Black:
1. 'Resultados_trimestrales': Realiza un análisis vertical y horizontal comparativo del Presupuesto Anual frente al Realizado (T1 a T4). Explica con detalle por qué, a pesar de que los ingresos brutos reales alcanzaron USD 48.50M (cumplimiento del 99.8% de la meta de USD 48.60M), el EBITDA operativo se desplomó un -41.4% (de USD 9.85M a USD 5.77M), destruyendo USD 4,078,000 en margen.
2. Identifica y cuantifica las 5 mayores variaciones negativas en gastos operacionales (OPEX), calculando el sobrecosto exacto en dólares y su desviación porcentual.
3. Cruza estos resultados con la hoja 'Cuellos_de_botella_y_costos' para validar cómo los fletes duplicados (USD 960k), las cancelaciones por lentitud (USD 1.25M) y la morosidad B2B (USD 1.11M) correlacionan de forma directa con el retraso de 5 días en el cierre y el ciclo de aprobación de 48 horas.
Entrega un resumen ejecutivo estructurado con tablas comparativas y recomendaciones de automatización.
```

---

## Prompt 2: Modelado Predictivo Trimestral (T1 2027) y Simulación
```text
Con base en los estados financieros auditados y la tendencia de deterioro de T1 a T4, construye un modelo financiero predictivo para el próximo trimestre (T1 2027 / T5) expresado en dólares estadounidenses (USD):
1. Modela y contrasta dos escenarios:
   - Escenario A (Inercial / Sin IA): Asume que el volumen comercial continúa creciendo pero persisten los cuellos de botella manuales (tasa de flete urgente en 2.8% de facturación y morosidad en 3.4%).
   - Escenario B (Optimizado / Con IA): Modela el impacto de implementar el Agente de Ingesta OCR y el Motor de Crédito en el Mes 1. Asume una reducción del 60% en fletes de emergencia (tasa baja al 1.0%), eliminación del 75% de cancelaciones por demora y recuperación de cartera vencida a niveles benchmark (1.2%).
2. Proyecta las líneas de Ingresos Brutos, Deducciones, CMV, OPEX crítico y margen EBITDA resultante en ambos escenarios.
3. Genera el código para un Dashboard Interactivo Ejecutivo (Live Artifact en HTML/Tailwind y Chart.js) que permita visualizar estos KPIs con controles deslizantes interactivos.
```
"""

with open(os.path.join(REPO_ROOT, "04_Prompts_y_Scripts", "Prompts_Claude_Auditoria_Financiera.md"), "w", encoding="utf-8") as f:
    f.write(prompts_content)

# -------------------------------------------------------------------------
# 11. 05_Evidencias_y_Entrega_Alura / Tabla_Oficial_de_Evidencias.md
# -------------------------------------------------------------------------
evid_content = """# Tabla Oficial de Evidencias y Registro de Entregables
**Programa Oracle Next Education (ONE) | Cohorte G11 | Ruta 4 (Finanzas y Operaciones)**
**Estudiante:** Francisco Israel Mesillas Hernández

---

| Entregable | Descripción Funcional | Ubicación / Enlace de Acceso | Estado / Verificación | Nota de Uso y Supervisión Humana (HITL) |
| :--- | :--- | :--- | :--- | :--- |
| **Informe Ejecutivo Oficial (DOCX)** | Documento integral formateado según plantilla oficial Alura / ONE AI for Business | [`INFORME_EJECUTIVO_TARANIS_BLACK_RUTA4_FINANZAS.docx`](../INFORME_EJECUTIVO_TARANIS_BLACK_RUTA4_FINANZAS.docx) | `[Generado y Validado]` | Documento maestro listo para importar a Google Docs y compartir como público. |
| **Informe Ejecutivo Oficial (MD)** | Reporte completo en Markdown estructurado | [`INFORME_EJECUTIVO_TARANIS_BLACK_RUTA4_FINANZAS.md`](../INFORME_EJECUTIVO_TARANIS_BLACK_RUTA4_FINANZAS.md) | `[Generado y Validado]` | Respaldo en texto plano con KaTeX y tablas completas. |
| **Dashboard Financiero Interactivo** | Live Artifact en HTML5, Tailwind CSS y Chart.js con simulador en tiempo real | [`03_Panel_Financiero_y_Predictivo/dashboard_financiero_taranis_black.html`](../03_Panel_Financiero_y_Predictivo/dashboard_financiero_taranis_black.html) | `[Operativo en Navegador]` | Permite a la presidencia ajustar deslizadores de fletes y cancelaciones dinámicamente. |
| **Matriz Lean SIPOC As-Is** | Mapeo riguroso de las 5 etapas, insumos, clientes y análisis de desperdicio (muda) | [`02_Diagnostico_Lean_Operaciones/Matriz_SIPOC_Flujo_AsIs_ToBe.md`](../02_Diagnostico_Lean_Operaciones/Matriz_SIPOC_Flujo_AsIs_ToBe.md) | `[Auditoría Lean Completa]` | Validación de SLAs operativos entre São Paulo y el Centro de Distribución en Joinville. |
| **Diagrama Ishikawa (6M)** | Análisis causal pormenorizado del retraso de 5 días en cierre contable y facturación | [`02_Diagnostico_Lean_Operaciones/Diagrama_Ishikawa_6M_Causa_Raiz.md`](../02_Diagnostico_Lean_Operaciones/Diagrama_Ishikawa_6M_Causa_Raiz.md) | `[Causas 6M Validadas]` | Se utiliza como guía en los comités semanales de operaciones y logística. |
| **Política de IA & LGPD** | Manual de gobernanza, usos permitidos/prohibidos y estructura de comités de ética | [`01_Estrategia_Ruta0_Corporativa/Politica_Gobernanza_Etica_LGPD.md`](../01_Estrategia_Ruta0_Corporativa/Politica_Gobernanza_Etica_LGPD.md) | `[Aprobada para Auditoría]` | Salvaguarda fiduciaria con política estricta de Zero Data Retention y enmascaramiento. |
| **Prompts Forenses Claude** | Banco de instrucciones estructuradas para auditar estados financieros y proyectar T1 2027 | [`04_Prompts_y_Scripts/Prompts_Claude_Auditoria_Financiera.md`](../04_Prompts_y_Scripts/Prompts_Claude_Auditoria_Financiera.md) | `[Ejecutado con Claude 3.7]` | El Controller debe validar manualmente cualquier reclasificación contable sugerida. |
"""

with open(os.path.join(REPO_ROOT, "05_Evidencias_y_Entrega_Alura", "Tabla_Oficial_de_Evidencias.md"), "w", encoding="utf-8") as f:
    f.write(evid_content)

# -------------------------------------------------------------------------
# 12. 05_Evidencias_y_Entrega_Alura / Guion_Video_Demostracion_5min.md
# -------------------------------------------------------------------------
video_content = """# Guion Técnico para Video de Demostración (Máximo 5 Minutos)
**Programa Oracle Next Education (ONE) | Cohorte G11 | Ruta 4 (Finanzas y Operaciones)**
**Estudiante:** Francisco Israel Mesillas Hernández

---

## 🎬 Estructura de Grabación Minuto a Minuto

* **Minuto 0:00 – 0:45 | Introducción e Impacto de Negocio:**
  * Saludo al evaluador: *"Hola, soy Francisco Israel Mesillas Hernández, de la cohorte G11 del programa ONE AI for Business. Presento la consultoría estratégica de IA para Taranis Black en la Ruta 4: Finanzas y Operaciones."*
  * El problema: *"Taranis Black facturó USD 48.50M en ventas, pero su EBITDA se derrumbó de USD 9.85M a USD 5.77M (-41.4%), destruyendo más de 4 millones de dólares. La causa: procesos manuales entre 3 hojas de cálculo y un ERP legado que retrasan 5 días el cierre y 48 horas el crédito."*

* **Minuto 0:45 – 2:00 | Diagnóstico Lean (SIPOC e Ishikawa):**
  * Mostrar en pantalla la Matriz SIPOC: *"De los 5 días que tarda un pedido, el tiempo activo es de solo 65 minutos; el 97.3% es desperdicio burocrático."*
  * Mostrar el Diagrama de Ishikawa de las 6M: *"Identificamos 3 causas críticas que generan el 85% de la pérdida: 48 horas de retención en crédito (USD 1.25M en cancelaciones), transcripción manual errónea (USD 960k en fletes urgentes) y conciliación manual desconectada (USD 180k en horas extras y USD 1.11M en morosidad)."*

* **Minuto 2:00 – 3:30 | La Solución Tecnológica y Demostración del Panel Interactivo:**
  * Abrir y mostrar en pantalla `dashboard_financiero_taranis_black.html`.
  * Explicar los 3 casos de uso del AI Canvas: Ingesta OCR+LLM, Scoring de Crédito Predictivo y Conciliador Continuo.
  * Mover los controles deslizantes del simulador: *"Al reducir los fletes urgentes en 60% y las cancelaciones en 75%, el simulador proyecta un EBITDA para T1 2027 de USD 2.52M frente a USD 950k inercial, generando una ganancia neta trimestral de USD 1.57M."*

* **Minuto 3:30 – 4:15 | Gobernanza, Ética y Human-in-the-Loop (HITL):**
  * *"La IA en finanzas no opera a ciegas: definimos reglas estrictas de Human-in-the-Loop para órdenes mayores a USD 50,000 o ajustes mayores a USD 5,000."*
  * *"Bajo la LGPD en Brasil, garantizamos una política de Zero Data Retention y enmascaramiento previo de CPFs y datos bancarios."*

* **Minuto 4:15 – 5:00 | Conclusiones y Retorno de Inversión (ROI):**
  * Conclusión numérica: *"Con una inversión de USD 185,000, capturamos USD 2.98M anuales en ahorro, logrando un ROI del 1,510% y un Payback de solo 22 días laborables. Muchas gracias."*
"""

with open(os.path.join(REPO_ROOT, "05_Evidencias_y_Entrega_Alura", "Guion_Video_Demostracion_5min.md"), "w", encoding="utf-8") as f:
    f.write(video_content)

print("Todos los archivos modulares y documentación del repositorio han sido generados exitosamente.")

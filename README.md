# 📊 AI Builder Challenge — Taranis Black
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

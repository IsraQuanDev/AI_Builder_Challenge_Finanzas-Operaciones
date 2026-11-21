# Prompts Estructurados de Auditoría Financiera y Modelado Predictivo
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

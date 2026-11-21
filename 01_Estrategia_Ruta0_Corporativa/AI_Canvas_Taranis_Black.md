# AI Canvas e Identificación de Oportunidades — Taranis Black
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

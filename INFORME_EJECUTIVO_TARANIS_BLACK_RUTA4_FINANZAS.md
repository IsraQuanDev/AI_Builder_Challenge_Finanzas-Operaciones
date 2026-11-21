# PROGRAMA ORACLE NEXT EDUCATION (ONE) & ALURA LATAM
## CHALLENGE ONE G11 — AI FOR BUSINESS
### INFORME EJECUTIVO — CONSULTORÍA DE IA PARA TARANIS BLACK
**RUTA 4 — IA PARA FINANZAS Y OPERACIONES**

---

## 📋 IDENTIFICACIÓN DEL ESTUDIANTE

| Campo | Información Oficial |
| :--- | :--- |
| **Nombre completo:** | **Francisco Israel Mesillas Hernández** |
| **Correo electrónico:** | **israel.mecillas@gmail.com** |
| **Grupo / Cohorte:** | **G11 — ONE AI for Business** |
| **Ruta de especialización:** | `[X]` **Ruta 4 — IA para finanzas y operaciones**<br>`[ ]` Ruta 1 — Ventas \| `[ ]` Ruta 2 — Marketing \| `[ ]` Ruta 3 — RR. HH. |

---

## 🏢 TU CONTEXTO EN TARANIS BLACK — RUTA 4

| Elemento | Descripción Contextual |
| :--- | :--- |
| **Público destinatario** | Analistas financieros, controllers, gerentes de operaciones, líder de logística en CD Joinville y analistas de procesos. |
| **Problema por resolver** | Toda la conciliación financiera se realiza copiando datos manualmente entre 3 hojas de cálculo locales (`Controle_Limites_2026.xlsx`, lista de precios y control de fletes) y un ERP legado sin APIs. Esto genera un retraso crónico de 5 días en el cierre contable mensual, cuellos de botella de hasta 48 horas en aprobación de crédito, un 6.8% de errores en emisión de notas fiscales, cancelaciones de pedidos corporativos por USD 1.25M y un sobrecosto anual de USD 1.36M en fletes de emergencia. |

---

## 💡 RESUMEN EJECUTIVO
*(Formato: Correo formal dirigido a la Directora Ejecutiva de Taranis Black — Máximo 15 líneas)*

> **De:** Francisco Israel Mesillas Hernández — Consultor Líder en Estrategia de IA  
> **Para:** Directora Ejecutiva — Taranis Black  
> **Asunto:** Diagnóstico Operativo-Financiero y Hoja de Ruta de IA: Recuperación de USD 2.98M en EBITDA y Cierre en 24h  
> 
> Estimada Directora Ejecutiva:  
> Tras auditar el ciclo financiero y operativo de Taranis Black, identificamos que aunque las ventas anuales alcanzaron USD 48.50M (99.8% de la meta), el EBITDA colapsó de USD 9.85M presupuestados a USD 5.77M reales (-41.4%), destruyendo USD 4,078,000 en margen. La causa raíz es una severa ineficiencia operativa: conciliar manualmente 3 hojas de cálculo y un ERP legado genera un retraso de 5 días en el cierre contable, retenciones de 48h en la aprobación de crédito comercial, USD 1.25M en cancelaciones por demora, USD 1.36M de sobrecosto en fletes aéreos de emergencia y USD 1.11M en morosidad desatendida.  
> 
> Para erradicar este drenaje de capital, diseñamos una hoja de ruta con tres iniciativas de IA: 1) Ingesta inteligente OCR+LLM que extrae pedidos en PDF y valida inventario/precios en 3 minutos sin errores; 2) Motor predictivo de scoring crediticio que aprueba instantáneamente órdenes <USD 50k reduciendo el ciclo de 48h a 15 minutos; y 3) Asistente cognitivo de conciliación continua entre bancos, hojas locales y ERP con supervisión humana (Human-in-the-Loop).  
> 
> Impacto proyectado: Recuperación estimada de USD 2.98M en EBITDA anual, reducción del ciclo total de facturación-expedición a <24 horas y reducción del cierre contable de 7 a 2 días hábiles. Con una inversión requerida de USD 185,000, el proyecto genera un ROI del 1,510% y un periodo de recuperación (Payback) de solo 22 días operativos. Solicito su aprobación para iniciar la marcha blanca del Módulo 1 en 15 días.

---

## 🧭 PARTE 1 — BASE ESTRATÉGICA OBLIGATORIA (RUTA 0)

### Etapa 1 — AI Canvas e Identificación de Oportunidades

A partir de la cadena de valor de Taranis Black (fabricación de mobiliario ergonómico con certificación NR-17, ventas B2B corporativas y despacho desde el CD en Joinville, Santa Catarina), se seleccionaron tres casos de uso clave orientados a solucionar las pérdidas financieras:

| Parámetro | Caso de Uso 1 | Caso de Uso 2 | Caso de Uso 3 |
| :--- | :--- | :--- | :--- |
| **Nombre de la Iniciativa** | **Agente Inteligente de Ingesta y Validación de Pedidos B2B (Order-to-ERP)** | **Motor Predictivo de Scoring Crediticio y Aprobación Descentralizada** | **Conciliador Financiero Cognitivo y Cierre Contable Continuo** |
| **Tipo de IA** | **Generativa + Tradicional (Híbrida)** | **Predictiva (Machine Learning + Rules Engine)** | **Tradicional (Analítica) + Generativa (LLM Explicativo)** |
| **Problema que Resuelve** | Transcripción manual de propuestas en PDF al ERP legado; errores tipográficos en códigos de tela y fletes CIF/FOB (6.8% de divergencias). | Cuello de botella de 48h de espera por aprobación del Gerente Financiero vía email; USD 1.25M en cancelaciones por lentitud. | Conciliación manual de 3 hojas locales de cálculo; 5 días de retraso crónico en el cierre mensual y USD 180k en horas extras. |
| **Descripción Técnica** | Pipeline multimodal (OCR inteligente + LLM empresarial) que extrae entidades (CNPJ, ítems, acabados, precios, flete). Valida contra la base de datos maestra y transfiere los datos limpios al ERP vía RPA en <3 minutos. | Modelo de árboles de gradiente (XGBoost) entrenado con historial de morosidad y consulta API automatizada a Serasa Experian. Clasifica el riesgo y aprueba automáticamente órdenes <USD 50,000 en banda verde. | Algoritmo determinístico de cruce multi-fuente (extractos bancarios, NF-e emitidas y ERP). El LLM redacta borradores de notas de ajuste y reportes de variaciones para la Controllería. |
| **Supervisión Humana (HITL)** | **Obligatoria** si la confianza OCR <95%, si hay divergencia de precio >1% con la lista oficial, o si falta comprobante de domicilio del cliente. | **Obligatoria** para pedidos >USD 50,000, clientes nuevos sin historial crediticio en banda amarilla, o solicitudes con plazos >90 días. | **Obligatoria**: El Controller debe autorizar digitalmente cualquier asiento contable de reclasificación o provisión PDD >USD 5,000. |

#### Justificación Estratégica de Clasificación y Supervisión Humana (HITL)

*   **¿Por qué IA Generativa en Ingesta?** En el mercado corporativo B2B, las propuestas y órdenes de compra no tienen un formato tipográfico homogéneo. Varían entre órdenes de compra digitales, PDFs escaneados y correos con anexos. Los sistemas rígidos basados en plantillas fijas colapsan ante cualquier variación estética; los modelos de lenguaje multimodales (LLM) procesan lenguaje no estructurado e infieren el contexto semántico con alta precisión.
*   **¿Por qué IA Predictiva en Crédito?** Evaluar el riesgo de otorgar financiamiento a 30, 60 y 90 días requiere ponderar múltiples variables interdependientes (score Serasa, historial de pagos de 24 meses, razón de liquidez corriente y apalancamiento). Un modelo predictivo calcula la probabilidad de impago en milisegundos y estandariza las decisiones sin sesgos cognitivos.
*   **¿Por qué la Supervisión Humana (Human-in-the-Loop) es Innegociable?** En finanzas y operaciones comerciales, un falso positivo puede causar pérdidas millonarias por impago, mientras que una alucinación fiscal en una Nota Fiscal Electrónica (NF-e) puede generar multas severas de la *Receita Federal do Brasil* (SEFAZ). El marco HITL posiciona a la IA como un copiloto de alto rendimiento, manteniendo la soberanía de decisión, la responsabilidad fiduciaria y el juicio crítico en manos del equipo humano.

---

### Etapa 2 — Priorización Basada en Datos y Gestión del Cambio

#### Matriz de Esfuerzo × Impacto

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

*   **Prioridad 1 (Mes 1) — Quick Win:** *Ingesta Inteligente OCR+LLM*. Bajo esfuerzo técnico mediante servicios estándar de extracción documental conectores RPA hacia el ERP legado. Impacto inmediato: elimina errores de despacho y detiene los fletes de emergencia.
*   **Prioridad 2 (Mes 2) — Proyecto Estratégico:** *Motor Predictivo de Crédito y Descentralización*. Impacto masivo al reducir el ciclo de aprobación de 48h a 15 minutos, rescatando USD 1.25M en ventas canceladas.
*   **Prioridad 3 (Mes 3) — Proyecto Estratégico:** *Conciliador Financiero Cognitivo*. Conexión de las 3 hojas de cálculo y libros contables, permitiendo cerrar el mes en 2 días hábiles.
*   **Iniciativa Descartada:** *Sustitución Total del ERP Legado*. Demandaría más de 18 meses de implementación, presupuestos superiores a USD 1.5M y un riesgo de disrupción operativa inaceptable. La IA permite modernizar la operativa mediante una capa de integración no invasiva.

#### Métricas de Éxito, Ahorros Cuantificados y Cálculo de ROI

*   **Presupuesto de Inversión (Año 1):**
    *   Suscripciones API empresariales (LLM/OCR con Zero Data Retention): USD 45,000.
    *   Infraestructura de microservicios, conectores RPA y base de datos: USD 55,000.
    *   Consultoría de desarrollo, pruebas y puesta en marcha: USD 65,000.
    *   Capacitación del personal y gestión del cambio: USD 20,000.
    *   **Inversión Total:** **USD 185,000**.
*   **Beneficios Económicos Anuales Cuantificados:**
    *   Ahorro por eliminación de fletes expresos de emergencia: **USD 960,000**.
    *   Margen recuperado por cancelación de pedidos B2B por lentitud: **USD 850,000**.
    *   Ahorro en multas, devoluciones y reentregas por pedidos erróneos: **USD 390,000**.
    *   Disminución de cartera vencida y provisiones de incobrabilidad (PDD): **USD 650,000**.
    *   Ahorro en horas extras del equipo financiero y auditorías externas: **USD 130,000**.
    *   **Beneficio Económico Bruto Anual:** **USD 2,980,000**.
*   **Cálculo Formal del ROI:**
    $$	ext{ROI} = rac{	ext{Beneficio Neto}}{	ext{Inversión}} = rac{	ext{USD } 2,980,000 - 	ext{USD } 185,000}{	ext{USD } 185,000} = rac{	ext{USD } 2,795,000}{	ext{USD } 185,000} = \mathbf{1,510.8\%}$$
*   **Periodo de Recuperación (Payback):**
    $$	ext{Payback} = rac{	ext{USD } 185,000}{	ext{USD } 2,980,000} 	imes 12 	ext{ meses} = \mathbf{0.74 	ext{ meses (aprox. 22 días laborables)}}$$
*   **Horas Ahorradas y Metas de Adopción:**
    *   Tiempo medio de tramitación de propuesta: De **40 minutos a 3 minutos** por pedido (ahorro del 92.5%).
    *   Horas hombre recuperadas: **123.3 horas mensuales por analista** (más de 1,480 horas anuales transferidas de digitación mecánica a análisis financiero).
    *   Metas de adopción: 75% de pedidos procesados por IA en Mes 1; 95% en Mes 3; 100% de conciliación bancaria automatizada al día 60.

#### Plan de Gestión del Cambio Organizacional (Modelo ADKAR)

1.  **Awareness (Conciencia):** Talleres directivos y operativos transparentando las cifras: el proceso manual está destruyendo USD 4M anuales y sobrecargando a los empleados. La IA no llega a despedir personal, sino a eliminar la digitación nocturna y el estrés en cierres de mes.
2.  **Desire (Deseo):** Rebranding del puesto de trabajo: los "Digitadores de Facturación" ascienden al rol de **"Analistas de Inteligencia Financiera"**. Se establece una bonificación trimestral ligada a la velocidad del ciclo de caja y exactitud del dato.
3.  **Knowledge (Conocimiento):** Programa de formación práctica en supervisión de IA, resolución de alertas de excepción y formulación de prompts avanzados con Claude y ChatGPT.
4.  **Ability (Habilidad):** Periodo de operación en paralelo (*Shadow Run*) de 4 semanas, donde el sistema procesa los datos en segundo plano y el personal valida los resultados antes del pase a producción definitiva.
5.  **Reinforcement (Refuerzo):** Publicación de un dashboard en las sedes de São Paulo y Joinville celebrando cierres mensuales completados en 48 horas sin horas extras.

---

### Etapa 3 — Política de Gobernanza, Ética y Cumplimiento

#### Política de IA Responsable: Matriz de Usos Permitidos y Prohibidos

| Prácticas Permitidas y Buenas Conductas (`Compliance`) | Prácticas Estrictamente Prohibidas (`Riesgo Crítico`) |
| :--- | :--- |
| **✔ Uso exclusivo de APIs empresariales** con acuerdos jurídicos vinculantes de **Zero Data Retention** (no entrenamiento con datos de Taranis Black). | **✖ Ingesta de información financiera o datos de clientes en herramientas públicas**, gratuitas o extensiones no autorizadas. |
| **✔ Extracción de entidades transaccionales B2B** (ítems de catálogo, CNPJ, cantidades, fletes CIF/FOB y precios de lista). | **✖ Carga de datos personales sensibles** de empleados o clientes (salud, origen, ideología, cuentas bancarias de personas físicas). |
| **✔ Scoring crediticio y sugerencia de límites** bajo reglas objetivas, transparentes y auditables por el equipo de crédito. | **✖ Denegación automática de crédito a clientes sin fundamentación matemática** o sin derecho humano a réplica. |
| **✔ Generación asistida de notas de ajuste contable** requiriendo siempre la firma digital y validación del Controller. | **✖ Ejecución de pagos bancarios**, dispersión de nómina o transferencias de tesorería de forma autónoma por la IA. |
| **✔ Anonimización previa de identificadores personales** mediante microservicios locales antes de llamadas a APIs externas. | **✖ Inclusión de credenciales**, contraseñas de ERP o certificados digitales (A1/A3) en prompts de modelos de lenguaje. |

#### Riesgos y Protección de Datos (LGPD - Brasil / Ley 13.709/2018)

*   **Cumplimiento Normativo de la LGPD:** Aunque el 70% de las ventas son corporativas (B2B), los contratos y órdenes contienen datos de personas físicas (representantes legales, compradores, correos personales, CPFs). Para cumplir con los Artículos 7 y 18 de la LGPD, se implementa una capa previa de Data Loss Prevention (DLP) que detecta y enmascara expresiones regulares de CPF y nombres antes de enviar información a modelos externos.
*   **Mitigación de Sesgos Algorítmicos en Crédito:** Se audita semestralmente el motor predictivo para garantizar que no penalice injustamente a compañías ubicadas fuera del polo industrial del Sudeste brasileño, basando las decisiones exclusivamente en historial de solvencia, liquidez e indicadores del buró Serasa.
*   **Prevención de Alucinaciones Financieras:** Toda extracción documental se valida mediante esquemas JSON tipificados y validación cruzada con la base de datos de la *Receita Federal do Brasil* (Sintegra) y la lista oficial de precios de Taranis Black.

#### Comité de Ética e IA y Frecuencia de Auditorías

*   **Integración Multidisciplinaria del Comité:**
    1.  *Chief Financial Officer (CFO) / Controller:* Presidente del Comité; salvaguarda de la integridad fiscal y financiera.
    2.  *Data Protection Officer (DPO) / Asesor Legal:* Responsable del cumplimiento estricto de la LGPD y contratos comerciales.
    3.  *Gerente de Ciberseguridad e Infraestructura TI (CISO):* Control de seguridad de APIs, accesos y cifrado AES-256.
    4.  *Gerente de Operaciones y Logística:* Garante de la integración de SLAs entre la oficina de São Paulo y el CD Joinville.
    5.  *Lead AI Engineer / Product Owner:* Responsable técnico del monitoreo de deriva del modelo (*model drift*) y latencia.
*   **Frecuencia de Auditoría:** Revisiones **quincenales** durante los primeros 90 días de implementación piloto; auditorías **bimestrales** en régimen ordinario y una auditoría anual externa e independiente de seguridad y modelos algorítmicos.

---

## 📊 PARTE 2 — ESPECIALIZACIÓN: IA PARA FINANZAS Y OPERACIONES (RUTA 4)

### Etapa 1 — Mapeo Lean y Diagnóstico de Cuellos de Botella (SIPOC e Ishikawa)

#### Matriz SIPOC del Flujo «Aprobación de Pedidos, Facturación y Expedición B2B»

| S (Suppliers / Proveedores) | I (Inputs / Entradas) | P (Process / Macroproceso Actual As-Is) | O (Outputs / Salidas) | C (Customers / Clientes) |
| :--- | :--- | :--- | :--- | :--- |
| **Consultores B2B y SDRs (SP)** | Propuesta comercial firmada en PDF escaneado (anexo a correo electrónico) | **1. Recepción y Selección de Propuestas:** Vendedor envía correo informal a `financiero@taranisblack.com.br`. En fin de mes ingresan >40 correos sin prioridad ni validación de inventario. *(Tiempo: 2-4 horas en bandeja)*. | Correo electrónico en cola de entrada no estructurado | Asistente Financiero |
| **Compradores B2B y Serasa Experian** | Datos cadastrales (CNPJ, IE, Dirección) y Score de crédito Serasa | **2. Consulta de Crédito Manual:** Asistente abre PDF y alterna en 3 pantallas: ERP legado, portal web Serasa y Excel `Controle_Limites_2026.xlsx`. *(Tiempo de ciclo: 40 min/pedido)*. | Dossier de crédito preliminar en Excel local | Gerente Financiero (Aprobador de alzada) |
| **Gerente Financiero (Aprobador)** | Resumen informal por correo ("¿Podemos facturar USD 85k a Empresa X?") | **3-4. Solicitud y Espera de Decisión:** Como no hay motor de reglas, cualquier pedido depende del Gerente. Debido a viajes y reuniones, el correo queda retenido. *(Tiempo de retención: 24h a 48h hábiles)*. | Correo informal de respuesta con el "De acuerdo" | Asistente Financiero / Facturación |
| **Asistente Financiero de Facturación** | Aprobación por email y tabla de precios comercial en Excel | **5a. Facturación Manual en ERP:** Asistente digita a mano la NF-e en el ERP legado. Errores del 6.8% en códigos de producto, colores de tela o inscripción estatal. *(Tiempo: 30 min/pedido)*. | DANFE, archivo XML de NF-e y boletos bancarios 30/60/90 | Cliente Corporativo B2B y Contabilidad |
| **Centro de Distribución (Joinville) y Transportadoras** | Correo a `expedicao.cd@` y tabla de fletes homologados | **5b. Notificación y Despacho:** Asistente autoriza la separación por correo. Divergencias en flete CIF/FOB paralizan camiones acumulando estadías y fletes dobles. *(Tiempo: 24h a 48h)*. | Picking List, Minuta de Embarque y Mercancía despachada | Cliente Corporativo B2B Receptor |

> **Diagnóstico Lean de Valor Agregado:**  
> Tiempo total de ciclo actual (Lead Time): **5 a 7 días hábiles**.  
> Tiempo total de procesamiento activo (Touch Time): **~65 minutos**.  
> **Eficiencia del Flujo de Proceso (PCE):** $rac{65 	ext{ min}}{5 	ext{ días} 	imes 8 	ext{ h/día} 	imes 60 	ext{ min}} = \mathbf{2.7\%}$.  
> *El 97.3% del tiempo representa desperdicio Lean (Muda de Espera y Sobreprocesamiento).*

---

#### Diagrama de Ishikawa (Espina de Pescado — Las 6M)

**Efecto Indeseado Central:** Retraso Crónico de 5 Días en el Cierre Contable y Ciclo de Facturación Excesivo de 5 Días Hábiles con Destrucción de USD 4.08M en EBITDA.

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

*Desglose Pormenorizado de las 6M:*
1.  **⚙️ Método (Procesos):** Carencia de Procedimientos Operativos Estandarizados (POP); flujo 100% basado en correos electrónicos informales y no auditables; aprobación de alzada manual donde cualquier importe (incluso compras menores de clientes recurrentes) exige el visto bueno del gerente; falta de validación contractual previa de flete CIF/FOB.
2.  **💻 Máquina (Sistemas y Tecnología):** ERP legado monolítico sin capacidades de integración API; ausencia total de reconocimiento óptico de caracteres (OCR) o IA para procesar pedidos en PDF; uso desarticulado de 3 hojas de cálculo locales (`Controle_Limites_2026.xlsx`, lista de precios y fletes) que generan desincronización y versiones conflictivas.
3.  **👥 Mano de Obra (Personas y Competencias):** Asistentes dedicando 40 minutos por pedido a transcribir datos de una ventana a otra; estrés crónico y desmotivación en cierres de mes; el Gerente Financiero se convierte en un embudo físico porque sus viajes operativos y comités de directorio le impiden responder correos en tiempo y forma.
4.  **📄 Material (Insumos y Documentación):** Formularios comerciales enviados por los vendedores con campos en blanco o ilegibles; divergencia constante entre los códigos del catálogo comercial y el catálogo registrado en el ERP legado (ej. sillas ErgoPro con mesh gris registradas erróneamente como tela negra); domicilios fiscales no actualizados.
5.  **📊 Medición (Métricas e Indicadores):** Inexistencia de monitoreo de SLAs en tiempo real; la Dirección General y Controllería descubren los retrasos de entregas y cancelaciones solo cuando el mes ha cerrado; ausencia de tableros de control para auditar pedidos congelados y antigüedad de saldos vencidos.
6.  **🏢 Medio Ambiente (Cultura y Entorno Organizacional):** Fricción geográfica y operativa entre el equipo comercial de São Paulo y el equipo de despacho del CD en Joinville (Santa Catarina); mentalidad reactiva de "apagar incendios" en lugar de estandarizar procesos; reproches cruzados entre ventas, crédito y logística.

---

#### Las 3 Causas Principales del Desempeño Deficiente

1.  **Aprobación de Crédito Manual y Centralizada (Cuello de Botella de 48h):** Al no existir un motor de scoring automatizado con matriz de alzada, todas las propuestas quedan represadas en la bandeja del Gerente Financiero. Esto genera **USD 1,250,000 anuales en cancelaciones directas** por clientes corporativos frustrados que no reciben confirmación de entrega.
2.  **Transcripción Manual de Datos de Pedidos al ERP (Tasa de Error del 6.8%):** Copiar a mano especificaciones de productos desde PDFs genera errores en facturación y órdenes de picking. Esto detiene los camiones en el CD de Joinville y causa **USD 960,000 anuales en fletes de emergencia** y **USD 725,000 en multas y reentregas**.
3.  **Conciliación Manual Multi-Hoja Desconectada del ERP:** El uso de 3 archivos de Excel locales obliga al equipo financiero a realizar conciliaciones mecánicas de miles de líneas cada fin de mes. Esto provoca un **retraso crónico de 5 días en el cierre contable**, **USD 180,000 en horas extras y auditorías**, y oculta una morosidad desatendida de **USD 1,110,000**.

---

#### Intervención Prioritaria Recomendada

**Intervención Elegida:** Despliegue inmediato en el Mes 1 del **Módulo de Ingesta Inteligente OCR+LLM y Motor Descentralizado de Reglas de Crédito**.

**Justificación Técnica y Económica:**  
Este punto es el origen del "efecto látigo" en toda la organización. Si se ataca en primer lugar la conciliación contable de cierre, se estaría actuando sobre el síntoma final cuando los datos ya entraron corruptos. Al implementar la Ingesta Inteligente y el Motor de Crédito:
*   El tiempo de aprobación pasa de 48 horas a menos de 15 minutos.
*   Los datos ingresan al ERP libres de errores tipográficos (exactitud >99%).
*   Se eliminan de inmediato los USD 1.25M en pedidos cancelados y se detienen los fletes dobles de emergencia de USD 960k.
*   Con los datos limpios en el ERP desde el inicio, la posterior conciliación contable se simplifica en más del 80%.

---

### Etapa 2 — Panel Inteligente y Análisis Predictivo con Claude (Opcional)

#### Prompts para Procesar la Hoja Financiera (`05_Finanzas_Presupuesto_vs_Real.xlsx`)

A continuación se presentan los prompts profesionales ejecutados en **Claude 3.7 Sonnet** para auditar y modelar la base de datos financiera:

```text
PROMPT 1: ANÁLISIS FORENSE DE ANOMALÍAS Y EROSIÓN DE EBITDA
Actúa como un Senior Financial Controller y Consultor en Lean Six Sigma. Analiza integralmente las tres hojas de cálculo del archivo adjunto '05_Finanzas_Presupuesto_vs_Real.xlsx' de la empresa Taranis Black:
1. 'Resultados_trimestrales': Realiza un análisis vertical y horizontal comparativo del Presupuesto Anual frente al Realizado (T1 a T4). Explica con detalle por qué, a pesar de que los ingresos brutos reales alcanzaron USD 48.50M (cumplimiento del 99.8% de la meta de USD 48.60M), el EBITDA operativo se desplomó un -41.4% (de USD 9.85M a USD 5.77M), destruyendo USD 4,078,000 en margen.
2. Identifica y cuantifica las 5 mayores variaciones negativas en gastos operacionales (OPEX), calculando el sobrecosto exacto en dólares y su desviación porcentual.
3. Cruza estos resultados con la hoja 'Cuellos_de_botella_y_costos' para validar cómo los fletes duplicados (USD 960k), las cancelaciones por lentitud (USD 1.25M) y la morosidad B2B (USD 1.11M) correlacionan de forma directa con el retraso de 5 días en el cierre y el ciclo de aprobación de 48 horas.
Entrega un resumen ejecutivo estructurado con tablas comparativas y recomendaciones de automatización.
```

```text
PROMPT 2: MODELADO PREDICTIVO TRIMESTRAL (T1 2027) Y SIMULACIÓN DE ESCENARIOS
Con base en los estados financieros auditados y la tendencia de deterioro de T1 a T4, construye un modelo financiero predictivo para el próximo trimestre (T1 2027 / T5) expresado en dólares estadounidenses (USD):
1. Modela y contrasta dos escenarios:
   - Escenario A (Inercial / Sin IA): Asume que el volumen comercial continúa creciendo pero persisten los cuellos de botella manuales (tasa de flete urgente en 2.8% de facturación y morosidad en 3.4%).
   - Escenario B (Optimizado / Con IA): Modela el impacto de implementar el Agente de Ingesta OCR y el Motor de Crédito en el Mes 1. Asume una reducción del 60% en fletes de emergencia (tasa baja al 1.0%), eliminación del 75% de cancelaciones por demora y recuperación de cartera vencida a niveles benchmark (1.2%).
2. Proyecta las líneas de Ingresos Brutos, Deducciones, CMV, OPEX crítico y margen EBITDA resultante en ambos escenarios.
3. Genera el código para un Dashboard Interactivo Ejecutivo (Live Artifact en HTML/Tailwind y Chart.js) que permita visualizar estos KPIs con controles deslizantes interactivos.
```

---

#### Anomalías Identificadas (Discrepancias Críticas en Costos e Ingresos)

Tras ejecutar el análisis forense con Claude, se confirmaron 5 anomalías financieras severas en el ejercicio anual:

| Cuenta / Indicador Financiero | Presupuestado Anual (USD) | Realizado Anual (USD) | Desviación Crítica (USD) | Desvío (%) | Hallazgo Financiero & Causa Operativa |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Fletes y Logística CD Joinville** | 2,380,000 | 3,740,000 | **+1,360,000** | **+57.1%** | **Anomalía Severa:** Sobrecosto masivo por contratación de fletes aéreos y expresos dedicados para compensar el atraso de 5 días en la facturación y no perder cuentas corporativas. |
| **Cancelaciones por Retraso** | 560,000 | 1,235,000 | **+675,000** | **+120.5%** | **Anomalía Severa:** Pedidos corporativos firmados que se cayeron debido a que el cliente no toleró los 5 días de demora en la confirmación del crédito y despacho. |
| **Provisión Deudores Dudosos (PDD)** | 440,000 | 1,110,000 | **+670,000** | **+152.3%** | **Anomalía Severa:** La morosidad a más de 90 días trepó de 1.2% a 3.4% de la facturación debido a que la cobranza preventiva se gestionaba manualmente mediante correos sueltos. |
| **Reentregas y Multas por Divergencia** | 210,000 | 725,000 | **+515,000** | **+245.2%** | **Anomalía Crítica:** 6.8% de las NF-e emitidas contenían discrepancias en códigos de catálogo o tributación interestatal SP-SC, obligando a devolver fletes y pagar multas. |
| **Margen EBITDA Operacional** | **9,848,000** (20.3%) | **5,770,000** (11.9%) | **-4,078,000** | **-41.4%** | **Destrucción de Margen:** Colapso de 8.4 puntos porcentuales de margen operativo, pasando de una operación altamente rentable a una bajo severo estrés de liquidez. |

---

#### Proyección Predictiva para el Próximo Trimestre (T1 2027 / T5)

El modelo predictivo estructurado en Claude comparó el desempeño financiero esperado en T1 2027 bajo dos escenarios operacionales:

| Métrica / Cuenta Financiera | T4 Realizado (Línea Base) | T1 2027 Inercial (Sin IA) | T1 2027 Optimizado (Con IA) | Impacto Neto Atribuible a la IA |
| :--- | :---: | :---: | :---: | :---: |
| **Ingresos Brutos Totales** | USD 13,400,000 | USD 13,800,000 | **USD 14,200,000** | **+USD 400,000** *(Ventas no perdidas)* |
| **(-) Cancelaciones por Retraso** | -USD 420,000 | -USD 460,000 | **-USD 115,000** | **+USD 345,000** *(Ahorro del 75%)* |
| **Ingresos Operativos Netos** | USD 10,702,000 | USD 11,040,000 | **USD 11,735,000** | **+USD 695,000** |
| **(-) Fletes y Logística de Entrega** | -USD 1,220,000 | -USD 1,320,000 | **-USD 528,000** | **+USD 792,000** *(Fletes normalizados)* |
| **(-) Reentregas y Multas** | -USD 260,000 | -USD 290,000 | **-USD 85,000** | **+USD 205,000** *(Menor reproceso)* |
| **(-) Provisión Morosidad (PDD)** | -USD 390,000 | -USD 430,000 | **-USD 150,500** | **+USD 279,500** *(Cobro inteligente)* |
| **EBITDA Operativo Trimestral** | **USD 1,002,000** | **USD 950,000** | **USD 2,520,000** | **+USD 1,570,000** |
| **Margen EBITDA (%)** | **7.5%** | **6.9%** | **17.7%** | **+10.8 puntos porcentuales** |

#### Supuestos Utilizados en el Modelo Predictivo

1.  **Reducción del Tiempo de Aprobación:** El motor de scoring crediticio automatizado aprueba el 80% de los pedidos en <15 minutos, recortando el ciclo total de despacho a <24 horas y reduciendo las cancelaciones comerciales en un 75%.
2.  **Eliminación de Fletes Duplicados:** La ingesta OCR erradica el 95% de las inconsistencias en códigos de producto y direcciones fiscales, permitiendo que la tasa de fletes expresos de emergencia caiga de 2.8% a 1.0% de la facturación.
3.  **Normalización de Morosidad:** El sistema de agentes de cobro preventivo por correo y WhatsApp rescata cartera antes de los 90 días, retornando la morosidad al benchmark del 1.2% sobre ventas.
4.  **Inversión Requerida:** Se amortizan USD 46,250 de CAPEX en el trimestre (USD 185,000 / 4 trimestres), arrojando un impacto neto positivo en EBITDA de **USD 1,523,750 netos solo en el primer trimestre**.

---

## 📎 ANEXO DE EVIDENCIAS Y REGISTRO DE ENTREGABLES

A continuación se relacionan todos los activos, scripts, paneles y modelos construidos durante la consultoría:

| Entregable | Descripción Funcional | Ubicación / Enlace de Acceso | Estado / Verificación | Nota de Uso y Supervisión Humana (HITL) |
| :--- | :--- | :--- | :--- | :--- |
| **Informe Ejecutivo Oficial** | Documento integral formateado según plantilla oficial Alura / ONE AI for Business | `INFORME_EJECUTIVO_TARANIS_BLACK_RUTA4_FINANZAS.docx` | `[Generado y Validado]` | Documento maestro listo para importar a Google Docs y compartir como público. |
| **Dashboard Financiero Interactivo** | Live Artifact en HTML5, Tailwind CSS y Chart.js con KPIs y simulador en tiempo real | `dashboard_financiero_taranis_black.html` | `[Operativo en Navegador]` | Permite a la presidencia ajustar deslizadores de fletes y cancelaciones dinámicamente. |
| **Matriz Lean SIPOC As-Is** | Mapeo riguroso de las 5 etapas, insumos, clientes y análisis de desperdicio (muda) | Sección SIPOC de este Informe | `[Auditoría Lean Completa]` | Validación de SLAs operativos entre São Paulo y el Centro de Distribución en Joinville. |
| **Diagrama Ishikawa (6M)** | Análisis causal pormenorizado del retraso de 5 días en cierre contable y facturación | Sección Ishikawa de este Informe | `[Causas 6M Validadas]` | Se utiliza como guía en los comités semanales de operaciones y logística. |
| **Política de IA & LGPD** | Manual de gobernanza, usos permitidos/prohibidos y estructura de comités de ética | Sección Etapa 3 de este Informe | `[Aprobada para Auditoría]` | Salvaguarda fiduciaria con política estricta de Zero Data Retention y enmascaramiento. |
| **Prompts Forenses Claude** | Banco de instrucciones estructuradas para auditar estados financieros y proyectar T1 2027 | Sección Prompts de este Informe | `[Ejecutado con Claude 3.7]` | El Controller debe validar manualmente cualquier reclasificación contable sugerida. |

---

## 🎬 GUION PARA VIDEO DE DEMOSTRACIÓN (MÁXIMO 5 MINUTOS)

> **Enlace del Video de Demostración:** `[Pendiente de grabación por el estudiante en Loom / Google Drive / YouTube no listado]`

### Estructura de Grabación Minuto a Minuto para Francisco Israel Mesillas Hernández

*   **Minuto 0:00 – 0:45 | Introducción e Impacto de Negocio:**
    *   Saludo al comité evaluador de Oracle Next Education y Alura. Presentación personal (Francisco Israel Mesillas Hernández, G11, Especialización en Finanzas y Operaciones).
    *   Presentación del caso Taranis Black: Explicar cómo una compañía con ventas saludables de USD 48.50M sufrió una pérdida de USD 4,078,000 en EBITDA debido a procesos manuales en hojas de cálculo y un ERP legado desconectado.
*   **Minuto 0:45 – 2:00 | Diagnóstico Lean (SIPOC e Ishikawa):**
    *   Mostrar en pantalla la Matriz SIPOC y el Diagrama de Ishikawa de las 6M.
    *   Explicar el cuello de botella central: el 97.3% del tiempo es desperdicio burocrático (espera de 48h en la bandeja del gerente para autorizar crédito y 40 minutos por propuesta copiando datos a mano).
    *   Destacar las 3 causas raíz cuantificadas: fletes de emergencia (USD 1.36M), cancelaciones (USD 1.25M) y morosidad desatendida (USD 1.11M).
*   **Minuto 2:00 – 3:30 | La Solución Tecnológica y Demostración del Panel Interactivo:**
    *   Compartir pantalla mostrando el **Dashboard Financiero Interactivo (`dashboard_financiero_taranis_black.html`)**.
    *   Demostrar las tres iniciativas de IA del AI Canvas (Ingesta OCR+LLM, Scoring de Crédito Predictivo y Conciliador Continuo).
    *   Mover los controles deslizantes del simulador predictivo para demostrar cómo la reducción de fletes urgentes y cancelaciones recupera el EBITDA trimestral de USD 950k a USD 2.52M en T1 2027.
*   **Minuto 3:30 – 4:15 | Gobernanza, Ética y Human-in-the-Loop (HITL):**
    *   Enfatizar que las finanzas corporativas no pueden operar en "caja negra": explicar las reglas de alzada para pedidos >USD 50,000 y ajustes contables >USD 5,000.
    *   Mencionar la política de **Zero Data Retention** y el cumplimiento de la LGPD en Brasil mediante anonimización de CPFs y datos bancarios.
*   **Minuto 4:15 – 5:00 | Conclusiones y Retorno de Inversión (ROI):**
    *   Cerrar con los indicadores clave de negocio: Inversión de USD 185,000, ahorro anual capturado de USD 2,980,000, **ROI del 1,510%**, **Payback de 22 días** y reducción del cierre contable de 7 a 2 días hábiles.
    *   Agradecimiento y despedida ejecutiva.

---
*Fin del Informe Ejecutivo — Challenge ONE G11 AI for Business*

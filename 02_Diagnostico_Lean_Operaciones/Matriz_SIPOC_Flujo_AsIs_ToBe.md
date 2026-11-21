# Mapeo Lean y Matriz SIPOC: Aprobación de Pedidos, Facturación y Expedición B2B
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
  $$	ext{PCE} = rac{65 	ext{ min}}{2,400 	ext{ min}} 	imes 100 = \mathbf{2.7\%}$$
* **Conclusión:** El **97.3% del tiempo** es desperdicio puro (espera de correos y sobreprocesamiento manual por falta de integración).

---

## 4. Matriz SIPOC To-Be (Flujo Optimizado con IA)
* **Ingesta:** El PDF se procesa mediante OCR+LLM en <3 minutos.
* **Crédito:** Aprobación automática en 15 minutos para pedidos <USD 50k con Serasa >700.
* **Facturación:** NF-e generada automáticamente vía RPA sin digitación humana.
* **Despacho:** Picking List enviado a Joinville en tiempo real.
* **Tiempo Total de Ciclo To-Be:** **<24 horas útiles** (PCE se eleva al **65.0%**).

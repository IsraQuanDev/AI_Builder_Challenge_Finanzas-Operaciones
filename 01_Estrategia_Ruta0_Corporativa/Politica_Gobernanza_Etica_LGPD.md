# Política de Gobernanza, Ética y Cumplimiento Normativo (LGPD)
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

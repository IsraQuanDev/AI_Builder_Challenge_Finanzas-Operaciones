# Matriz de Esfuerzo × Impacto, ROI y Gestión del Cambio
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
* **Beneficio Neto:** $	ext{USD } 2,980,000 - 	ext{USD } 185,000 = \mathbf{USD\ 2,795,000}$.
* **Retorno sobre la Inversión (ROI):**
  $$	ext{ROI} = rac{	ext{USD } 2,795,000}{	ext{USD } 185,000} 	imes 100 = \mathbf{1,510.8\%}$$
* **Periodo de Recuperación (Payback):**
  $$	ext{Payback} = rac{	ext{USD } 185,000}{	ext{USD } 2,980,000} 	imes 12 	ext{ meses} = \mathbf{0.74 	ext{ meses (~22 días hábiles)}}$$
* **Horas Hombre Liberadas:** Reducción del tiempo de tramitación de 40 a 3 minutos por pedido (**92.5% de ahorro**), liberando más de 1,480 horas anuales en el equipo financiero.

---

## 3. Plan de Gestión del Cambio Organizacional (ADKAR)

1. **Awareness (Conciencia):** Presentación ejecutiva a los equipos mostrando que el proceso manual destruye USD 4.08M en EBITDA y satura al personal con horas extras. La IA se presenta como un salvavidas operativo.
2. **Desire (Deseo):** Transformación del puesto de los colaboradores: de "Digitadores Contables" a **"Analistas de Inteligencia Financiera"**, con bonificaciones por calidad de cartera y velocidad de ciclo.
3. **Knowledge (Conocimiento):** Talleres prácticos sobre resolución de alertas de excepción, supervisión de IA y prompts financieros.
4. **Ability (Habilidad):** Operación en paralelo (*Shadow Run*) durante 4 semanas: la IA genera sugerencias que el personal valida con un clic.
5. **Reinforcement (Refuerzo):** Reconocimiento público de metas de cierre contable en 48 horas sin turnos de madrugada.

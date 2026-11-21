# Diagrama de Ishikawa (Espina de Pescado — Las 6M)
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

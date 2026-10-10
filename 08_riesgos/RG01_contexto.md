# RG01: Contexto y Criterios de Gestión de Riesgos del PETI (2026 - 2028)
**Organización:** Municipalidad Distrital de Alto Selva  
**Documento marco:** Plan Estratégico de Tecnologías de la Información (PETI)  
**Normativa de referencia:** ISO 31000:2018, ISO/IEC 27005:2022, Marco de Gobierno y Transformación Digital (PCM-SGTD / D.L. 1412)  
**Fecha de formalización y acuerdo:** 10 de octubre de 2026  
**Aprobado por:** Gerencia Municipal y Comité de Gobierno y Transformación Digital  

---

## 1. Alcance del Análisis
El presente documento y análisis de riesgos aplica exclusivamente a los riesgos que amenazan la **ejecución, cumplimiento de objetivos y entrega de proyectos del PETI Año 1 – Año 3 (2026 – 2028)** de la Municipalidad Distrital de Alto Selva.
- **Se excluyen expresamente:**
  - Riesgos operativos cotidianos de TI (fallas menores de hardware usuario, tickets de mesa de ayuda, tratados en la operación regular y en el proyecto de Mesa de Servicios ITIL).
  - Riesgos estratégicos y políticos institucionales generales (competencia del Plan Estratégico Institucional - PEI y del Plan de Desarrollo Concertado - PDC).

---

## 2. Horizonte Temporal
- **Periodo:** 3 años (2026 – 2028), cubriendo la Ola 1 (Estabilización e Integración Base), Ola 2 (Digitalización de Servicios y Gobierno de Datos) y Ola 3 (Interoperabilidad y Analítica Predictiva Municipal).

---

## 3. Escalas de Evaluación con Definición Operativa

### 3.1. Escala de Probabilidad (P)
| Nivel | Descriptor | Frecuencia esperada en el ciclo del PETI | Criterio operativo observable |
|---|---|---|---|
| **1** | Muy Baja | Evento excepcional (< 10 % de probabilidad) | No ha ocurrido en administraciones previas; requiere una conjunción improbable de eventos externos desfavorables. |
| **2** | Baja | Raro pero posible (10 % – 30 %) | Ha ocurrido de manera aislada en municipalidades similares o en una ocasión en los últimos 5 años. |
| **3** | Media | Posible y previsible (31 % – 60 %) | Existen antecedentes en la entidad en proyectos anteriores (p. ej. retrasos en compras públicas o rotación de personal CAS). |
| **4** | Alta | Muy probable (61 % – 85 %) | Se observan factores activos de vulnerabilidad documentados (p. ej. sistemas sin código fuente, políticas no aplicadas, observaciones de Contraloría/PCM). |
| **5** | Muy Alta | Prácticamente seguro (> 85 %) | Ocurre con regularidad en cada ejercicio fiscal o hito presupuestal/político sin control de mitigación vigente. |

### 3.2. Escala de Impacto (I)
| Nivel | Descriptor | Impacto en Objetivos del PETI | Desviación Presupuestal / Cronograma | Impacto Legal / Continuidad de Servicios Ciudadanos |
|---|---|---|---|---|
| **1** | Insignificante | Desviación imperceptible en metas del PETI. | Afectación < 5 % del presupuesto del proyecto; retraso < 2 semanas. | Sin impacto legal ni afectación de atención en mesa de partes o recaudación. |
| **2** | Menor | Afecta metas secundarias de un proyecto no crítico. | Afectación 5 % – 10 % del presupuesto; retraso entre 2 y 4 semanas. | Reclamaciones aisladas de usuarios internos; subsanable sin escalamiento. |
| **3** | Moderado | Compromete un Objetivo Digital específico (OD) o pospone un proyecto de la ola actual. | Afectación 11 % – 25 % del presupuesto anual de TI; retraso de 1 a 2 meses en hitos clave. | Suspensión temporal (< 24 h) de servicios tributarios o trámite; apercibimiento administrativo leve. |
| **4** | Mayor | Afecta múltiples proyectos de la hoja de ruta o paraliza una ola completa. | Sobrecosto 26 % – 50 %; retraso > 3 meses que compromete el cierre del ejercicio fiscal. | Pérdida de datos tributarios/civiles con afectación legal directa; multas de PCM/ANPDP; paralización de recaudación > 72 h. |
| **5** | Catastrófico | Fracaso total del PETI, abandono de plataformas estratégicas o paralización institucional. | Sobrecosto > 50 % o recorte presupuestal que obliga a cancelar el portafolio; retraso > 6 meses. | Sanción penal o administrativa a funcionarios; revocación de acreditaciones; pérdida irreparable de datos sin respaldo; colapso de atención ciudadana. |

---

## 4. Fórmula de Valoración y Criterios de Aceptación del Riesgo

### 4.1. Fórmula Clásica
$$\text{Valor del Riesgo} = \text{Probabilidad (P)} \times \text{Impacto (I)}$$
Rango resultante: **1 a 25**.

### 4.2. Criterio de Aceptación y Niveles de Decisión
| Rango de Valor | Nivel de Riesgo | Criterio de Aceptación y Acción Mandatoria | Nivel de Aprobación |
|---|---|---|---|
| **1 – 6** | **Bajo** | **Aceptable.** Se asume el riesgo con monitoreo de rutina y documentación de control interno. | Subgerente de Tecnologías de la Información |
| **7 – 11** | **Medio** | **Tolerable condicionado.** Requiere plan de tratamiento específico, asignación formal de responsable y monitoreo bimestral. | Gerente de Administración y Finanzas / Gerente del Área Usuaria |
| **12 – 14** | **Alto** | **No aceptable en condiciones actuales.** Requiere tratamiento obligatorio con acciones inmediatas, plazos definidos y reducción obligatoria de riesgo residual. | Comité de Gobierno y Transformación Digital |
| **15 – 25** | **Crítico** | **Inaceptable.** Amenaza la viabilidad del plan. Requiere decisión, asignación de fondos de contingencia y firma formal de Gerencia Municipal y Alcaldía antes de aprobar el PETI. | Alcaldía y Gerencia Municipal |

---

## 5. Dueños de Riesgo por Cargo Estructural
De acuerdo con las buenas prácticas de gestión pública y control interno (CGR / ISO 31000), los dueños del riesgo se asignan estrictamente por **cargo estructural**, nunca por nombre personal:
1. **Presupuestal:** Gerente de Administración y Finanzas / Subgerente de Presupuesto y Planificación.
2. **Patrocinio y Dirección:** Gerente Municipal / Comité de Gobierno y Transformación Digital.
3. **Personal Clave y Talento:** Subgerente de Recursos Humanos / Subgerente de Tecnologías de la Información.
4. **Capacidad de Ejecución:** Subgerente de Tecnologías de la Información.
5. **Resistencia al Cambio:** Gerente de Administración Tributaria / Subgerente de Atención al Ciudadano y Trámite Documentario.
6. **Proveedor y Terceros:** Subgerente de Logística y Control Patrimonial / Subgerente de Tecnologías de la Información.
7. **Técnico y Arquitectura:** Subgerente de Tecnologías de la Información.
8. **Normativo y Cumplimiento:** Gerente de Asesoría Jurídica / Oficial de Seguridad de la Información / Oficial de Datos Personales.
9. **De Alcance y Gobernanza:** Comité de Gobierno y Transformación Digital.
10. **Ejecución del Plan:** Gerente Municipal (como máximo patrocinador ejecutivo).

---

## 6. Frecuencia de Revisión y Gobernanza
- **Revisión Ordinaria:** Trimestral, en sesión del Comité de Gobierno y Transformación Digital.
- **Revisión Extraordinaria:** Obligatoria ante:
  1. Cambio de Alcalde o Gerente Municipal.
  2. Modificaciones mayores a la Ley de Presupuesto del Sector Público o recortes del Canon/FONCOMUN $> 15\%$.
  3. Ocurrencia de un riesgo con impacto calificado como Mayor o Catastrófico.
  4. Auditoría de la Contraloría General de la República o supervisión de PCM-SGTD.
- **Fecha de fijación de criterios:** 10 de octubre de 2026 (fijado previo a la matriz de evaluación para garantizar trazabilidad e imparcialidad).

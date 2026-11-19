# 8. Gestión de Riesgos del Plan Estratégico de TI (PETI 2026 - 2028)
**Entidad:** Municipalidad Distrital de Alto Selva  

---

## 8.1 Alcance, Contexto y Criterios

### Alcance
La presente sección establece la gestión de riesgos orientada exclusivamente a salvaguardar la **ejecución, gobernanza y entrega oportuna del PETI 2026 – 2028**.
- **Qué gestiona:** Amenazas estratégicas, presupuestales, de capacidades, de proveedores, de resistencia al cambio y técnicas que puedan retrasar, paralizar o degradar los proyectos de digitalización e interoperabilidad municipal (Olas 1, 2 y 3).
- **Qué no gestiona:** Incidentes operativos diarios de TI (tickets de soporte, fallas menores de ofimática) ni riesgos institucionales y políticos macro correspondientes al PEI (Plan Estratégico Institucional).

### Escalas de Probabilidad e Impacto con Definición Operativa
- **Probabilidad (P) [1 a 5]:** 
  - *1 (Muy Baja):* Improbable (< 10 %), sin antecedentes en la entidad.
  - *2 (Baja):* Raro (10–30 %), ocurrido de forma aislada en comunas similares.
  - *3 (Media):* Previsible (31–60 %), con antecedentes directos en la municipalidad.
  - *4 (Alta):* Muy probable (61–85 %), factores de vulnerabilidad activos (sistemas no documentados, dependencia de personal).
  - *5 (Muy Alta):* Casi seguro (> 85 %), recurrente en cada cambio fiscal o político.
- **Impacto (I) [1 a 5]:**
  - *1 (Insignificante):* Retraso < 2 semanas, sobrecosto < 5 %, sin impacto ciudadano.
  - *2 (Menor):* Retraso 2–4 semanas, reclamos internos aislados.
  - *3 (Moderado):* Retraso 1–2 meses, suspensión temporal (< 24 h) de servicios tributarios o trámite.
  - *4 (Mayor):* Retraso > 3 meses, sobrecosto 26–50 %, paralización de recaudación > 72 h o pérdida de datos con sanción legal de PCM/ANPDP.
  - *5 (Catastrófico):* Fracaso o abandono del PETI, sobrecosto > 50 %, pérdida total de base tributaria o sanción penal/administrativa a funcionarios.

### Criterio de Aceptación y Fecha de Acuerdo
- **≤ 6:** Aceptable con monitoreo de rutina.
- **7 – 11:** Tolerable con tratamiento específico y monitoreo bimestral.
- **12 – 14:** Alto. Requiere tratamiento obligatorio con plazos estrictos y reducción forzosa de riesgo residual.
- **≥ 15:** Crítico. Requiere decisión, asignación de contingencia y firma formal de Alcaldía y Gerencia Municipal antes de aprobar el plan.
- **Fecha de acuerdo:** 10 de octubre de 2026 (fijado antes de la evaluación, registrado en Acta N.º 004-2026-CGTD y trazable en Git).

---

## 8.2 Método
Se aplica la metodología internacional **ISO 31000:2018** articulada con las directivas de seguridad de la información **ISO/IEC 27005:2022** y el marco de gobierno digital de la Secretaría de Gobierno y Transformación Digital (**PCM-SGTD** / D.L. 1412).

### Fuentes de Identificación
1. **Dinámica de Pre-mortem:** Ejercicio prospectivo donde el equipo formulador se situó en el año 2028 asumiendo el fracaso del PETI para identificar causas subyacentes.
2. **Análisis de Impacto al Negocio (BIA):** Diagnóstico de los procesos BIA01 a BIA06, detectando inconsistencias severas en RTO/RPO y falta de validación de áreas usuarias.
3. **Auditoría y Universo Auditable:** Evaluación de 17 entidades auditables (UA-01 a UA-17) y 9 riesgos históricos (RG-01 a RG-09) no resueltos por la administración.
4. **Política de Respaldo (POL-TI-007):** Contrastación entre la norma escrita y la práctica real (ausencia de pruebas de restauración y traslado físico inseguro de discos).

---

## 8.3 Registro de Riesgos
Se han registrado **13 riesgos**, cubriendo de forma exhaustiva las **nueve categorías mandatorias** más la categoría de ejecución:

| ID | Categoría | Riesgo (Evento + Causa + Consecuencia) | Proyectos Afectados | P | I | Valor | Nivel |
|---|---|---|---|---|---|---|---|
| **R-01** | Presupuestal | Que el presupuesto asignado para modernización y nube se reduzca en más del 40 % en el Año 2 por reasignación de partidas del Concejo a obras viales de emergencia retrasando la Ola 2 | OD-01, OD-03 · PR-04, PR-06 | 4 | 4 | **16** | Crítico |
| **R-02** | Patrocinio | Que el Alcalde o Gerente Municipal dejen de priorizar el plan o sean cambiados por rotación política dejando los proyectos sin respaldo ejecutivo ni asignación presupuestal | Todos los OD · Toda la hoja de ruta | 3 | 5 | **15** | Crítico |
| **R-03** | Personal clave | Que el único especialista de base de datos de Rentas renuncie por falta de incentivos CAS perdiendo el conocimiento tácito sobre el sistema legado e interrumpiendo la interoperabilidad | OD-02, OD-04 · PR-02, PR-05 | 4 | 4 | **16** | Crítico |
| **R-04** | Capacidad de ejecución | Que el equipo de TI con solo 4 personas colapse al intentar liderar 4 proyectos simultáneos mientras atiende el soporte diario de usuarios generando retrasos > 4 meses | Ola 1 y Ola 2 · PR-01, PR-03, PR-07 | 4 | 3 | **12** | Alto |
| **R-05** | Resistencia al cambio | Que el personal de ventanilla de rentas y registro civil boicotee el sistema digital por temor a perder discrecionalidad en la atención obligando a mantener la atención física manual | OD-01, OD-02 · PR-01, PR-08 | 4 | 4 | **16** | Crítico |
| **R-06** | Resistencia al cambio | Que las gerencias de línea se nieguen a validar los RTO y RPO reales de sus áreas por ver el BIA como una carga burocrática manteniendo metas irreales que invalidan la continuidad | OD-05 · PR-09 | 4 | 3 | **12** | Alto |
| **R-07** | Proveedor | Que el proveedor del sistema de rentas niegue el acceso a bases de datos y aumente tarifas por mantener contrato sin código fuente en custodia ni SLAs exigibles bloqueando la integración | OD-02, OD-04 · PR-02 | 4 | 4 | **16** | Crítico |
| **R-08** | Técnico | Que ocurra pérdida total e irrecuperable de bases de datos tributarias por ataque o fallo de disco ante la falta de pruebas de restauración y transporte informal de copias en disco externo | OD-03, OD-05 · PR-06, PR-10 | 4 | 5 | **20** | Crítico |
| **R-09** | Técnico | Que la integración con la Plataforma Nacional PIDE falle por obsolescencia técnica de servidores municipales locales y ausencia de web services seguros retrasando trámites interinstitucionales | OD-01, OD-04 · PR-03 | 3 | 4 | **12** | Alto |
| **R-10** | Normativo | Que la ANPDP o PCM sancionen a la municipalidad con multas y paralización de trámites por tratar datos de contribuyentes sin registro de bancos de datos personales ni medidas de cifrado | OD-05 · PR-08, PR-11 | 3 | 4 | **12** | Alto |
| **R-11** | De alcance | Que regidores y gerencias exijan nuevos aplicativos informáticos no contemplados sin caso de negocio por falta de gobernanza consumiendo el 35 % de la capacidad de desarrollo del equipo | Toda la hoja de ruta | 4 | 3 | **12** | Alto |
| **R-12** | Ejecución del plan | Que el PETI se apruebe pero no se ejecute por falta de responsable a tiempo completo y ausencia de reuniones del Comité de Transformación Digital perpetuando la informalidad de TI | Todos los OD · Toda la hoja de ruta | 4 | 5 | **20** | Crítico |
| **R-13** | Presupuestal | Que el gasto operativo acumulado (OPEX) por licencias y servicios nube supere el presupuesto corriente en el Año 3 obligando a apagar servicios digitales ya entregados al ciudadano | OD-03, OD-04 · PR-04, PR-07 | 3 | 3 | **9** | Medio |

*Categorías sin riesgo identificado:* **Ninguna.** Todas las 9 categorías obligatorias se encuentran debidamente cubiertas con datos y casuística de la municipalidad.

---

## 8.4 Evaluación y Mapa de Calor

### Distribución por Niveles de Riesgo Inicial
- **Crítico (≥ 15):** 7 riesgos (53.8 %)
- **Alto (12 – 14):** 5 riesgos (38.5 %)
- **Medio (7 – 11):** 1 riesgo (7.7 %)
- **Bajo (≤ 6):** 0 riesgos (0.0 %)

### Riesgos ≥ 15 que Requieren Decisión Formal de Alcaldía y Gerencia Municipal
Los riesgos **R-08** (Pérdida de bases de datos tributarias, Valor 20), **R-12** (Falta de ejecución del PETI, Valor 20), **R-01** (Recorte presupuestal del Concejo, Valor 16), **R-03** (Renuncia de especialista clave de Rentas, Valor 16), **R-05** (Boicot al canal digital, Valor 16), **R-07** (Bloqueo de proveedor monopólico, Valor 16) y **R-02** (Pérdida de patrocinio político, Valor 15) representan el 54 % de la exposición global y exigen acuerdos de blindaje institucional previos a la aprobación final del plan.

*(El mapa de calor generado por `RG03_evaluacion.py` se adjunta en `graficos/RG_mapa_calor.png`)*.

---

## 8.5 Tratamiento y Riesgo Residual

Se definió un plan de tratamiento activo para el 100 % de los riesgos evaluados (todos con valor inicial $\ge 9$):

| ID | Valor Inicial | Decisión | Acciones Concretas de Tratamiento | Responsable (Cargo) | Plazo | Costo | P res | I res | Valor Residual | Reducción (%) |
|---|---|---|---|---|---|---|---|---|---|---|
| R-08 | 20 | Mitigar | Implementar esquema 3-2-1 con copias cifradas inmutables en nube y simulacros trimestrales | Subgerente de TI | 60 d | Medio | 1 | 4 | **4** | 80 % |
| R-12 | 20 | Mitigar | Resolución de designación de Líder del PETI a tiempo completo y sesiones mensuales obligatorias del CGTD | Gerente Municipal | Inmediato | Bajo | 2 | 4 | **8** | 60 % |
| R-01 | 16 | Mitigar + Contingencia | Acuerdo de Concejo de reserva presupuestal plurianual en POI/PIA y portafolio modular contingente | Gerente de Adm. y Finanzas | Inmediato | Bajo | 2 | 4 | **8** | 50 % |
| R-03 | 16 | Mitigar | Documentación de arquitectura de rentas, capacitación cruzada e incentivos de retención laboral | Subgerente RR. HH. y Subgerente TI | 90 d | Medio | 2 | 4 | **8** | 50 % |
| R-05 | 16 | Mitigar | Gestión del cambio con personal de ventanilla, comisiones por trámite digital e inducción intensiva | Gerente de Adm. Tributaria | Previo PR-01 | Medio | 2 | 4 | **8** | 50 % |
| R-07 | 16 | Transferir + Mitigar | Renegociación contractual con código escrow, penalidades y diseño de migración a arquitectura abierta | Subgerente de Logística | Previo Ola 2 | Medio | 2 | 4 | **8** | 50 % |
| R-02 | 15 | Mitigar | Institucionalizar PETI por Ordenanza Municipal vinculada al PDLC e inducción a nuevo cuadro directivo | Gerente Municipal | Inmediato | Bajo | 2 | 4 | **8** | 47 % |
| R-04 | 12 | Mitigar | Tercerizar mesa de ayuda de microinformática y contratar 2 programadores dedicados al PETI | Subgerente de TI | 60 d | Medio | 2 | 3 | **6** | 50 % |
| R-06 | 12 | Mitigar | Talleres directivos con Gerencias Usuarias para validar y sincerar RTO/RPO del BIA | Subgerente de TI y Gerente Municipal | 45 d | Bajo | 2 | 3 | **6** | 50 % |
| R-09 | 12 | Mitigar | PoC de interoperabilidad PIDE y despliegue de API Gateway local con certificados digitales seguros | Subgerente de TI | Previo PR-03 | Bajo | 1 | 4 | **4** | 67 % |
| R-10 | 12 | Mitigar | Registro oficial de 6 bancos de datos personales ante ANPDP y directiva interna de seguridad | Gerente Asesoría Jurídica | 90 d | Bajo | 1 | 4 | **4** | 67 % |
| R-11 | 12 | Mitigar | Regla de admisión estricta: todo proyecto requiere caso de negocio y aprobación unánime de CGTD | Comité de Gob. Digital | Continuo | Bajo | 2 | 3 | **6** | 50 % |
| R-13 | 9 | Mitigar | Modelo TCO a 5 años para nube y negociación de contratos marco con tarifa plana | Subgerente Presupuesto / TI | Continuo | Bajo | 2 | 3 | **6** | 33 % |

### Balance Global del Tratamiento
- **Exposición inicial agregada:** 190 puntos.
- **Exposición residual agregada:** 86 puntos.
- **Reducción neta del riesgo:** **104 puntos (55 % de reducción)**.

---

## 8.6 Señales Tempranas y Umbrales de Alerta

Para garantizar que el registro sea un instrumento proactivo de control y no un inventario estático:

| ID | Riesgo | Señal Temprana Observable | Umbral de Alerta Cuantitativo |
|---|---|---|---|
| R-08 | Pérdida de base de datos | Falla o cancelación de backup diario sin ticket de resolución en < 4 horas | 2 fallos consecutivos en la semana o > 30 días sin prueba de restauración |
| R-12 | No ejecución del plan | Comité de Gobierno Digital sin sesionar en fecha calendarizada | 45 días sin sesión de comité o 1 trimestre sin reporte formal de avance |
| R-01 | Recorte presupuestal | Retraso en la inclusión de partidas de TI en la formulación del PIA | 30 días de retraso en asignación del PIA o recorte > 15 % en debate de Concejo |
| R-03 | Pérdida de personal clave | Dependencia de un único técnico para soporte de bases de datos tributarias | Factor bus = 1 detectado en rentas por más de 30 días continuos |
| R-05 | Boicot en ventanillas | Tasa de asistencia a talleres de capacitación digital inferior al 60 % | 2 semanas consecutivas con adopción de la plataforma digital < 30 % en ventanilla |
| R-07 | Bloqueo de proveedor | Negativa o dilación del proveedor en entregar especificaciones de integración | 60 días antes del vencimiento del contrato sin adenda firmada |
| R-02 | Pérdida de patrocinio | Inasistencia o falta de pronunciamiento del Gerente Municipal en el Comité | 2 sesiones consecutivas del Comité sin participación de la Gerencia Municipal |
| R-04 | Sobrecarga de equipo TI | Desviación > 20 % en horas dedicadas a proyectos del PETI vs soporte diario | 3 sprints o hitos mensuales consecutivos con retraso en entregables |
| R-06 | BIA irreal | Observaciones o negativa formal de gerencias de línea a convalidar tiempos BIA | 30 días sin actas suscritas de validación de RTO/RPO por áreas de línea |
| R-09 | Falla integración PIDE | Rechazo de solicitudes de conexión en las pruebas de homologación PIDE | 2 rechazos en pruebas técnicas de interoperabilidad PIDE |
| R-10 | Multas de ANPDP/PCM | Notificaciones o requerimientos de información preventiva de la ANPDP o PCM | 1 notificación de requerimiento de subsanación de la autoridad de datos |
| R-11 | Desvío de alcance | Solicitudes de desarrollo informático enviadas por memorando directo a TI | 1 solicitud admitida a desarrollo sin acta previa de aprobación del Comité |
| R-13 | Sobrecosto OPEX cloud | Crecimiento no planificado del consumo cloud > 15 % en facturación mensual | 2 meses consecutivos con desviación del gasto cloud sobre la partida proyectada |

*Riesgos sin señal temprana identificada:* **0 (Cero).**

---

## 8.7 Matriz de Comunicación del Riesgo

La comunicación transparente permite adoptar medidas correctivas antes de que los riesgos se materialicen:

| ID | Qué se comunica | A quién (Cargo) | Cuándo / Frecuencia | Canal | Quién comunica | Formato | Qué decisión habilita |
|---|---|---|---|---|---|---|---|
| **R-08** | Estado de copias inmutables y actas de simulacro de restauración | Gerencia Municipal y Comité de Gobierno Digital | Mensual y ante fallas críticas | Sesión ordinaria y correo oficial | Subgerente de TI | Tablero de control y acta firmada | Validar contingencia o autorizar compra de almacenamiento |
| **R-12** | Avance de hitos del PETI y cumplimiento de cronograma | Alcalde, Gerente Municipal y Concejo | Trimestral | Sesión de Concejo y reunión directiva | Líder de Implementación del PETI | Informe ejecutivo y semáforo de proyectos | Continuar, reasignar recursos o aplicar medidas correctivas |
| **R-01** | Ejecución del presupuesto de TI vs PIA/PIM y proyecciones | Gerente de Adm. y Finanzas y Gerente Municipal | Trimestral o ante recorte > 10 % | Memorando e informe financiero | Subgerente de TI y Presupuesto | Reporte financiero SIAF consolidado | Activar portafolio contingente o blindar partidas |
| **R-03** | Matriz de factor bus de sistemas y avance de documentación | Gerente Municipal y Subgerente de RR. HH. | Bimestral mientras residual > 6 | Informe técnico reservado | Subgerente de TI | Matriz de capacidades y riesgos | Aprobar bonos de retención o autorizar contrataciones CAS |
| **R-05** | Métricas de adopción digital y trámites virtuales | Gerente de Adm. Tributaria y Gerencias Usuarias | Quincenal en piloto, mensual en prod. | Reunión de coordinación de línea | Subgerente de TI | Tablero analítico Power BI | Ajustar inducciones o aplicar incentivos de productividad |
| **R-07** | Estado de renegociación contractual y SLAs de proveedores | Gerente Municipal y Subgerente de Logística | Mensual hasta formalizar contrato | Informe técnico legal | Subgerente de TI y Asesoría Jurídica | Matriz de cumplimiento contractual | Aplicar penalidades o iniciar migración tecnológica |
| **R-02** | Evaluación estratégica del PETI y alineamiento al PDLC | Alcalde y Concejo Municipal | Semestral | Sesión de Concejo Municipal | Gerente Municipal | Presentación ejecutiva de impacto | Ratificar respaldo político y normativo del plan |
| **R-04** | Carga operativa de TI vs avance de proyectos estratégicos | Gerente de Administración y Finanzas | Mensual | Reunión de gerencia | Subgerente de TI | Reporte de horas hombre y backlog | Autorizar contratación de soporte microinformático |
| **R-06** | Validación del BIA con áreas de línea | Comité de Gob. Digital y Jefaturas | Bimestral en formulación | Taller directivo participativo | Subgerente de TI | Actas de validación de RTO/RPO | Aprobar formalmente el Plan de Continuidad |
| **R-09** | Progreso de pruebas técnicas de integración PIDE | Comité de Gobierno Digital | Al concluir cada prueba | Sesión de comité | Subgerente de TI | Informe de interoperabilidad | Aprobar pase a producción del módulo web |
| **R-10** | Inscripción de bancos de datos personales y brechas | Oficial de Datos Personales y Gerencia | Trimestral | Informe de cumplimiento | Gerente de Asesoría Jurídica | Informe de auditoría legal | Subsanar observaciones de ANPDP y evitar multas |
| **R-11** | Registro de nuevas solicitudes informáticas y admisión | Comité de Gobierno Digital | Mensual | Sesión ordinaria de comité | Líder de Implementación del PETI | Acta de evaluación de casos de negocio | Rechazar proyectos sin valor estratégico |
| **R-13** | Curva de costos OPEX cloud y facturación proyectada | Gerente de Administración y Finanzas | Trimestral | Informe técnico financiero | Subgerente de TI | Reporte de consumo cloud proyectado | Ajustar capacidades aprovisionadas |
| **Todos ≥ 15** | Resumen de riesgos críticos iniciales, residuales y tratamientos | **Alcaldía y Gerencia Municipal** | **Antes de aprobar el PETI** | **Sesión formal extraordinaria** | **Líder del PETI y Subgerente de TI** | **Anexo formal de firmas del PETI** | **Aprobar el plan asumiendo conscientemente el riesgo residual** |

---

## 8.8 Riesgos Residuales que Requieren Aceptación Formal

Aquellos riesgos cuyo valor residual permanece en valor $\mathbf{8}$ (superior al criterio de aceptación estricto $\le 6$) requieren aceptación formal mediante firma del cargo directivo correspondiente antes de la puesta en marcha:

| ID | Riesgo | Valor Residual | Responsable Formal de la Aceptación (Firma) | Justificación de la Aceptación |
|---|---|---|---|---|
| **R-12** | Ejecución del PETI | **8** | Alcaldía y Gerencia Municipal | Se asume el residual dado que la estructura de gobierno municipal depende de la voluntad política del Concejo, mitigado por la Ordenanza. |
| **R-01** | Recorte presupuestal | **8** | Alcaldía y Gerencia Municipal | La disponibilidad de canon y FONCOMUN está sujeta a factores macroeconómicos; se acepta bajo el compromiso del portafolio contingente modular. |
| **R-03** | Personal clave | **8** | Gerente Municipal | Las restricciones de escala salarial de la Ley de Presupuesto limitan la retención plena; se acepta respaldado en la capacitación cruzada y documentación. |
| **R-05** | Resistencia al cambio | **8** | Gerente Municipal | La transición cultural de los trabajadores de planta toma tiempo; se acepta con acompañamiento continuo y metas graduales de digitalización. |
| **R-07** | Dependencia de proveedor | **8** | Gerente Municipal | La sustitución inmediata del sistema de rentas es inviable técnica y operativamente en el corto plazo; se acepta con contrato renegociado y custodia de código. |
| **R-02** | Patrocinio político | **8** | Alcaldía y Gerencia Municipal | El ciclo electoral y los cambios de gabinete son inherentes al sector público; se acepta blindado mediante la Ordenanza y el Comité de Gobierno Digital. |

---

## 8.9 Seguimiento y Revisión

- **Responsable del Seguimiento:** Líder de Implementación del PETI conjuntamente con el Subgerente de Tecnologías de la Información.
- **Frecuencia Ordinaria:** Evaluación trimestral de la matriz de riesgos en sesiones ordinarias del Comité de Gobierno y Transformación Digital.
- **Disparadores de Revisión Extraordinaria:**
  1. Cambio de Alcalde o Gerente Municipal.
  2. Reducción presupuestal superior al 15 % del presupuesto anual de TI.
  3. Ocurrencia de un ciberataque, pérdida de datos o indisponibilidad de sistemas de recaudación por más de 24 horas.
  4. Observaciones o requerimientos perentorios emitidos por la Contraloría General de la República o PCM-SGTD.

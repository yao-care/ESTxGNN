---
layout: default
title: Eribulin
parent: Solo predicción del modelo (L5)
nav_order: 304
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-25
description: "Eribulin: nueva indicación predicha, Fiebre mediterránea familiar autosómica recesiva (nivel de evidencia L5). Indicación original: Liposarcoma (según la base de conocimiento del modelo"
monitor_inn: "eribulin"
predicted_indications: ["autosomal recessive familial Mediterranean fever", "dermatofibrosarcoma protuberans", "pleural mesothelioma", "malignant peritoneal mesothelioma", "pleural adenomatoid tumor", "pleural biphasic mesothelioma", "fibroblastic neoplasm", "pleural epithelioid mesothelioma", "heart fibrosarcoma"]
---

# Eribulin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Eribulina: De Liposarcoma a Fiebre Mediterránea Familiar Autosómica Recesiva
{: .text-alpha }

## Resumen en Una Frase

Eribulina es un inhibidor de la dinámica de los microtúbulos, utilizado originalmente en oncología para el tratamiento del **liposarcoma**.
El modelo TxGNN predice que podría ser efectivo para la **fiebre mediterránea familiar autosómica recesiva**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: la predicción se basa solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Liposarcoma (según la base de conocimiento del modelo; los textos de indicación de las autorizaciones no están disponibles) |
| Nueva Indicación Predicha | Fiebre mediterránea familiar autosómica recesiva |
| Puntaje de Predicción TxGNN | 0.9982 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 7 de 12; autorizadas no comercializadas: 4; revocadas o suspendidas: 1) |
| Número de Autorizaciones | 12 (comercializadas: 7) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Eribulina inhibe la dinámica de los microtúbulos y tiene efecto antimitótico. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Eribulin (traducción no oficial): «La eribulina inhibe la fase de crecimiento de los microtúbulos sin afectar la fase de acortamiento y secuestra la tubulina en agregados no productivos. La eribulina ejerce sus efectos mediante un mecanismo antimitótico basado en la tubulina que conduce al bloqueo del ciclo celular en G 2 /M, a la desorganización de los husos mitóticos y, en última instancia, a la muerte celular por apoptosis tras un bloqueo mitótico prolongado.» Texto original en inglés: "Eribulin inhibits the growth phase of microtubules without affecting the shortening phase and sequesters tubulin into nonproductive aggregates. Eribulin exerts its effects via a tubulin-based antimitotic mechanism leading to G 2 /M cell-cycle block, disruption of mitotic spindles, and, ultimately, apoptotic cell death after prolonged mitotic blockage." ([DailyMed: Halaven (eribulin mesylate) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=31ce4750-ded5-4a0b-95e9-f229fa6bc822), versión del 2025-11-07; consultado el 2026-11-19). Su uso se centra en tumores de crecimiento rápido, como el liposarcoma.

La fiebre mediterránea familiar, en cambio, es una enfermedad autoinflamatoria causada por la desregulación del inflamasoma de pirina, y no es una neoplasia. La puntuación alta probablemente se explica porque la colchicina, otro fármaco que actúa sobre los microtúbulos, es el tratamiento estándar de esta enfermedad. Esto crea una cercanía en la red de conocimiento del modelo.

No se identificó un mecanismo que respalde esta indicación. El perfil citotóxico de eribulina (mielosupresión, neuropatía) la hace poco adecuada para una enfermedad inflamatoria crónica no maligna. La predicción es, con alta probabilidad, un artefacto de la red y no tiene respaldo clínico ni bibliográfico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Los textos de indicación aprobada no figuran en los datos compilados.

<!-- review:begin es-lic-20261105-eribulin-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Se muestran 5 de las 11 autorizaciones vigentes (todas de principio activo único, ninguna cancelada). Los textos de indicación aprobada no figuran en los datos compilados." Eliminado: afirmaba que el medicamento no está autorizado o comercializado en España, o que sus autorizaciones están revocadas o suspendidas, lo que no coincide con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-eribulin-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 89127 | ERIBULINA STADA 0,44 MG/ML SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Laboratorio Stada S.L. | Comercializada |
| 89251 | ERIBULINA GLENMARK 0,44 MG/ML SOLUCIÓN INYECTABLE EFG | SOLUCIÓN INYECTABLE | Glenmark Arzneimittel Gmbh | Comercializada |
| 11678001 | HALAVEN 0,44 MG/ML SOLUCION INYECTABLE | SOLUCIÓN INYECTABLE | Eisai Gmbh | Comercializada |
| 89176 | ERIBULINA ADVANZ PHARMA 0,44 MG/ML SOLUCIÓN INYECTABLE EFG | SOLUCIÓN INYECTABLE | Advanz Pharma Limited | Comercializada |
| 1241819001 | ERIBULINA BAXTER 0,44 MG/ML SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Baxter Holding B.V. | Comercializada |
| 89838 | ERIBULINA EVER PHARMA 0,44 MG/ML SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Ever Valinject Gmbh | Comercializada |
| 89728 | ERIBULINA ZENTIVA 0,44 MG/ML SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Zentiva K.S. | Comercializada |
| 111678003 | HALAVEN 0,44 MG/ML SOLUCION INYECTABLE | SOLUCIÓN INYECTABLE | Eisai Gmbh | Autorizada, no comercializada |
| 90846 | ERIBULINA CTTQ 0,44 MG/ML SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Chia Tai Tian Qing Europe S.L. | Autorizada, no comercializada |
| 90823 | ERIBULINA HIKMA 0,44 MG/ML SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Hikma Farmaceutica (Portugal) S.A. | Autorizada, no comercializada |

Se muestran 10 de 12 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimicrotúbulo, inhibidor de la dinámica de microtúbulos) |
| Riesgo de Mielosupresión | Alto (neutropenia, agranulocitosis y trombocitopenia figuran entre las relaciones de contraindicación del grafo de conocimiento) |
| Clasificación de Emetogenicidad | Baja (según la categoría habitual del fármaco; confirmar en el prospecto) |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, electrolitos (potasio), ECG por riesgo de QT prolongado, vigilancia de neuropatía periférica |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

Las advertencias y contraindicaciones del prospecto no están disponibles en los datos compilados. Consultar el prospecto para esa información.

- **Contraindicaciones o precauciones según el grafo de conocimiento** (no proceden del texto del prospecto): síndrome de QT largo (incluido el familiar), trombocitopenia, deficiencia de potasio, neutropenia, agranulocitosis, enfermedad del sistema nervioso periférico, neuropatía periférica y estreñimiento.
- **Interacciones farmacológicas**: se registraron 375 interacciones. Entre las principales:
  - **Mayores**: dolasetrón y cisaprida (riesgo asociado a la prolongación del QT).
  - **Moderadas** (ejemplos): ondansetrón, palonosetrón, claritromicina, levofloxacino, metronidazol, tinidazol, famotidina, loperamida, rosuvastatina, simvastatina, y varios laxantes (bisacodilo, lactulosa, lactitol, polietilenglicol, aceite de ricino, picosulfato).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene una puntuación alta, pero solo se apoya en el modelo (nivel L5), sin ensayos ni literatura. Además, no hay un mecanismo plausible y el perfil de toxicidad de eribulina es difícil de justificar en una enfermedad autoinflamatoria crónica no maligna.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones) para completar el cribado de seguridad.
- Evidencia preclínica o clínica que vincule la inhibición de microtúbulos por eribulina con la vía de la pirina, si se quisiera seguir explorando esta indicación.
- Priorizar otras indicaciones predichas con más respaldo. En especial, la de **neoplasia fibroblástica** (tumor fibroso solitario y fibrosarcoma) cuenta con un ensayo de fase 2 completado (NCT03840772, n=16) y datos preclínicos. Tiene un nivel de evidencia L2 y justifica una evaluación independiente.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Eliminado: "Se muestran 5 de las 11 autorizaciones vigentes (todas de principio activo único, ninguna cancelada)" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Halaven (eribulin mesylate) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=31ce4750-ded5-4a0b-95e9-f229fa6bc822) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


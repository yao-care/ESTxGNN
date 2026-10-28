---
layout: default
title: Eribulin
parent: Solo predicción del modelo (L5)
nav_order: 304
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
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
| Estado de Mercado en España | Comercializado (registros vigentes: 7 de 11) |
| Número de Autorizaciones | 11 (vigentes: 7) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Eribulina inhibe la dinámica de los microtúbulos y tiene efecto antimitótico. No se dispone de datos detallados del mecanismo de acción en las fuentes consultadas, pero esta es su clase farmacológica conocida. Su uso se centra en tumores de crecimiento rápido, como el liposarcoma.

La fiebre mediterránea familiar, en cambio, es una enfermedad autoinflamatoria causada por la desregulación del inflamasoma de pirina, y no es una neoplasia. La puntuación alta probablemente se explica porque la colchicina, otro fármaco que actúa sobre los microtúbulos, es el tratamiento estándar de esta enfermedad. Esto crea una cercanía en la red de conocimiento del modelo.

No se identificó un mecanismo que respalde esta indicación. El perfil citotóxico de eribulina (mielosupresión, neuropatía) la hace poco adecuada para una enfermedad inflamatoria crónica no maligna. La predicción es, con alta probabilidad, un artefacto de la red y no tiene respaldo clínico ni bibliográfico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 11 autorizaciones vigentes (todas de principio activo único, ninguna cancelada). Los textos de indicación aprobada no figuran en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 89127 | Eribulina Stada 0,44 mg/ml solución inyectable EFG | Solución inyectable | Laboratorio Stada S.L. |
| 89659 | Eribulina Viatris 0,44 mg/ml solución inyectable EFG | Solución inyectable | Viatris Limited |
| 89251 | Eribulina Glenmark 0,44 mg/ml solución inyectable EFG | Solución inyectable | Glenmark Arzneimittel GmbH |
| 11678001 | Halaven 0,44 mg/ml solución inyectable | Solución inyectable | Eisai GmbH |
| 89176 | Eribulina Advanz Pharma 0,44 mg/ml solución inyectable EFG | Solución inyectable | Advanz Pharma Limited |

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


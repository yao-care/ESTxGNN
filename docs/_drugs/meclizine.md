---
layout: default
title: Meclizine
parent: Solo predicción del modelo (L5)
nav_order: 497
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "meclizine"
predicted_indications: ["allergic urticaria", "common cold", "nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "cold urticaria"]
description: "Meclizine: nueva indicación predicha, Urticaria alérgica (allergic urticaria) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 4 (comercializadas: 2)"
---

# Meclizine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Meclizine: Urticaria alérgica (allergic urticaria)
{: .text-alpha }

## Resumen en Una Frase

Meclizina es un antihistamínico H1 de primera generación con actividad anticolinérgica, originalmente utilizado para el vértigo de origen en el sistema nervioso central y el mareo por movimiento.
El modelo TxGNN predice que podría ser efectivo para **urticaria alérgica**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Urticaria alérgica (allergic urticaria) |
| Puntaje de Predicción TxGNN | 0.9967 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 4; revocadas o suspendidas: 2) |
| Número de Autorizaciones | 4 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Meclizine (traducción no oficial): «Se desconoce el mecanismo preciso por el cual la meclizina ejerce su efecto terapéutico, pero se presume que implica el antagonismo del receptor H1 de la histamina.» Texto original en inglés: "The precise mechanism by which meclizine exerts its therapeutic effect is unknown but is presumed to involve antagonism of the histamine H1 receptor." ([DailyMed: Meclizine Hydrochloride (meclizine) prescribing information, St. Mary's Medical Park Pharmacy](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5d2ff762-041d-74ed-e063-6394a90ac588), versión del 2026-10-06; consultado el 2026-11-19). Según la información conocida, la meclizina es un antihistamínico H1 de primera generación con actividad anticolinérgica. Su eficacia en el vértigo y el mareo por movimiento es conocida, y mecanísticamente podría ser aplicable a la urticaria alérgica.

La urticaria alérgica es una enfermedad mediada por histamina, por lo que el bloqueo de los receptores H1 es un mecanismo biológicamente plausible. Sin embargo, este vínculo se apoya en el conocimiento de la clase farmacológica y en la predicción de TxGNN, no en datos clínicos específicos de meclizina.

Conviene señalar que ya existen antihistamínicos H1 con mejor respaldo de evidencia para esta indicación, en particular los de segunda generación, que causan menos sedación. Esto limita el interés práctico del reposicionamiento.

Otras indicaciones predichas, todas con nivel L5 y decisión Hold: resfriado común (0.9949), enfermedad de la cavidad nasal (0.9948), faringitis (0.9945), laringofaringitis aguda (0.9937) y urticaria por frío (0.9922). En las afecciones de vías respiratorias altas el beneficio sería solo sintomático, y el efecto secante anticolinérgico podría ser contraproducente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 57907 | CHICLIDA 25 mg COMPRIMIDOS PARA CHUPAR | PASTILLA PARA CHUPAR | Fleer Española S.L. | Comercializada |
| 33924 | CHICLIDA 25 mg CHICLES MEDICAMENTOSOS | CHICLE MEDICAMENTOSO | Fleer Española S.L. | Comercializada |
| 59406 | NAVICALM 5 MG/5 ML JARABE | JARABE | Arafarma Group S.A. | Revocada |
| 59405 | NAVICALM 25 MG COMPRIMIDOS | COMPRIMIDO | Arafarma Group S.A. | Revocada |

Se muestran las 4 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto)**: hiperplasia prostática benigna, glaucoma de ángulo cerrado, estenosis pilórica y obstrucción del cuello vesical.
- **Interacciones Farmacológicas**: se identificaron 252 interacciones en total. Entre las principales:
  - **Mayores**: cloruro de potasio y citrato de potasio.
  - **Moderadas**: otros anticolinérgicos (atropina, hiosciamina, glicopirronio, diciclomina, trospio, clidinio, mepenzolato, metescopolamina), opioides (morfina, opio), loperamida, metoclopramida, nabilona, eliglustat, eluxadolina y fenilbutirato de glicerol.
  - Es esperable un efecto aditivo anticolinérgico y sedante con varios de ellos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura. Además, existen alternativas mejor establecidas y menos sedantes para la urticaria, y el perfil anticolinérgico de la meclizina añade carga de seguridad.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre meclizina en urticaria y comparación con antihistamínicos de segunda generación.
- Datos detallados del mecanismo de acción (MOA), por ejemplo desde DrugBank.
- Advertencias y contraindicaciones del prospecto de la AEMPS.
- Textos de indicación aprobada de las autorizaciones españolas.
- Evaluación de la carga sedante y anticolinérgica en la población objetivo, y de la compatibilidad de vías de administración.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Meclizine Hydrochloride (meclizine) prescribing information, St. Mary's Medical Park Pharmacy](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5d2ff762-041d-74ed-e063-6394a90ac588) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


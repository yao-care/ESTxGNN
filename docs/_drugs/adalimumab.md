---
layout: default
title: Adalimumab
parent: Solo predicción del modelo (L5)
nav_order: 23
evidence_level: L5
indication_count: 3
monitor_inn: "ADALIMUMAB"
predicted_indications: ["hypermobility of coccyx", "Kummell disease", "vertebral disease"]
last_modified_at: 2026-11-05
description: "Adalimumab: nueva indicación predicha, hipermovilidad del cóccix (hypermobility of coccyx) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Adalimumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Adalimumab: inhibidor del factor de necrosis tumoral alfa (TNF-α) → hipermovilidad del cóccix (hypermobility of coccyx)
{: .text-alpha }

## Resumen en Una Frase

Adalimumab es un anticuerpo monoclonal que bloquea el TNF-α y se comercializa en España con múltiples marcas y biosimilares.
El modelo TxGNN predice que podría ser efectivo para **hipermovilidad del cóccix (hypermobility of coccyx)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | hipermovilidad del cóccix (hypermobility of coccyx) |
| Puntaje de Predicción TxGNN | 0,9977 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 7; autorizadas no comercializadas: 9; revocadas o suspendidas: 4) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Adalimumab (traducción no oficial): «Los productos de adalimumab se unen específicamente al TNF-alfa y bloquean su interacción con los receptores de TNF p55 y p75 de la superficie celular. Los productos de adalimumab también lisan in vitro las células que expresan TNF en su superficie en presencia del complemento.» Texto original en inglés: "Adalimumab products bind specifically to TNF-alpha and block its interaction with the p55 and p75 cell surface TNF receptors. Adalimumab products also lyse surface TNF expressing cells in vitro in the presence of complement." ([DailyMed: Simlandi (adalimumab-ryvk) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12f609c9-2088-bb05-e063-6394a90a9ecc), versión del 2026-11-11; consultado el 2026-11-19). Por su clase, adalimumab es un inhibidor del TNF-α, una citocina central en varios procesos inflamatorios crónicos mediados por el sistema inmunitario.

Para la hipermovilidad del cóccix no se ha establecido un mecanismo inflamatorio dependiente del TNF. Se trata de una condición generalmente mecánica o traumática. La puntuación elevada parece reflejar la proximidad en la red del modelo con términos de espondiloartropatía, y no una relación biológica demostrada.

Por tanto, la predicción debe considerarse una hipótesis para generar preguntas de investigación, no una base para uso clínico. No hay estudios que evalúen directamente esta enfermedad, por lo que el nivel de evidencia es L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Según los datos compilados, hay 8 autorizaciones vigentes y 4 canceladas, y el listado puede ser parcial. Los textos de indicación aprobada no figuran en los registros locales.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1171216014 | IMRALDI 40 MG solución inyectable en pluma precargada | Solución inyectable en pluma precargada |
| 03256003 | HUMIRA 40 mg solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada |
| 1171216001 | IMRALDI 40 MG solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada |
| 1211589001 | HUKYNDRA 40 MG solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada |
| 1181286010 | HYRIMOZ 80 MG solución inyectable en pluma precargada | Solución inyectable en jeringa precargada |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las principales:
  - **Gravedad mayor**: corticoides (betametasona, budesonida, dexametasona, hidrocortisona, prednisolona, prednisona, triamcinolona), deferiprona, ibritumomab tiuxetán, iobenguano (I-131) y tositumomab.
  - **Gravedad moderada**: metronidazol, tinidazol, rosuvastatina y simvastatina.
  - **Gravedad menor**: sales de zinc (acetato, gluconato y sulfato).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo computacional (puntaje 0,9977), sin ensayos ni publicaciones que estudien esta enfermedad y sin un mecanismo biológico plausible basado en el TNF-α.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de adalimumab y un fundamento biológico que vincule el TNF-α con la hipermovilidad del cóccix
- Revisión bibliográfica dirigida que busque estudios directos sobre esta condición
- Obtención de las advertencias y contraindicaciones del prospecto de la AEMPS antes de cualquier evaluación de seguridad

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Simlandi (adalimumab-ryvk) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12f609c9-2088-bb05-e063-6394a90a9ecc) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


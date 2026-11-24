---
layout: default
title: Trastuzumab Deruxtecan
parent: Solo predicción del modelo (L5)
nav_order: 816
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Trastuzumab Deruxtecan: nueva indicación predicha, Osteoporosis inducida por fármacos (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de …"
monitor_inn: "trastuzumab deruxtecan"
predicted_indications: ["drug-induced osteoporosis"]
---

# Trastuzumab Deruxtecan
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Trastuzumab Deruxtecán: De Indicación Original No Especificada a Osteoporosis Inducida por Fármacos
{: .text-alpha }

## Resumen en Una Frase

Trastuzumab deruxtecán es un conjugado anticuerpo-fármaco dirigido a HER2 que lleva como carga citotóxica un inhibidor de la topoisomerasa I (deruxtecán, derivado de la exatecán). En los datos compilados para este informe no consta el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **osteoporosis inducida por fármacos**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Osteoporosis inducida por fármacos |
| Puntaje de Predicción TxGNN | 0,9931 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 3 de 3) |
| Número de Autorizaciones | 3 (comercializadas: 3) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Trastuzumab Deruxtecan (traducción no oficial): «El fam-trastuzumab deruxtecán-nxki es un conjugado anticuerpo-fármaco dirigido contra HER2. El anticuerpo es una IgG1 anti-HER2 humanizada. La molécula pequeña, DXd, es un inhibidor de la topoisomerasa I unido al anticuerpo mediante un conector escindible.» Texto original en inglés: "Fam-trastuzumab deruxtecan-nxki is a HER2-directed antibody-drug conjugate. The antibody is a humanized anti-HER2 IgG1. The small molecule, DXd, is a topoisomerase I inhibitor attached to the antibody by a cleavable linker." ([DailyMed: Enhertu (fam-trastuzumab deruxtecan-nxki) prescribing information, Daiichi Sankyo Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7e67e73e-ddf4-4e4d-8b50-09d7514910b6), versión del 2026-05-15; consultado el 2026-11-19). Según la información conocida, trastuzumab deruxtecán es un conjugado anticuerpo-fármaco: un anticuerpo dirigido a HER2 unido a un inhibidor de la topoisomerasa I (deruxtecán). Es un fármaco de uso oncológico.

La única base de la predicción es la puntuación muy alta del modelo TxGNN (aprendizaje profundo) de TxGNN (0,9931). No se identifica una vía mecanística establecida que relacione la diana HER2 o la inhibición de la topoisomerasa I con la prevención o el tratamiento de la pérdida ósea causada por fármacos (por ejemplo, glucocorticoides o inhibidores de la aromatasa).

Al contrario, los efectos del tratamiento oncológico (como la supresión de la función ovárica o la coadministración de esteroides) podrían asociarse con pérdida ósea y no con protección. La puntuación elevada proviene del modelo TxGNN (aprendizaje profundo) y probablemente refleja similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica, por lo que la predicción debe interpretarse con mucha cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 1201508001IP1 | ENHERTU 100 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Daiichi Sankyo Europe Gmbh | Comercializada |
| 1201508001 | ENHERTU 100 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Daiichi Sankyo Europe Gmbh | Comercializada |
| 1201508001IP | ENHERTU 100 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Daiichi Sankyo Europe Gmbh | Comercializada |

Se muestran las 3 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Las tres autorizaciones están vigentes, corresponden a monofármaco y su titular es Daiichi Sankyo Europe GmbH.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Conjugado anticuerpo-fármaco con carga citotóxica (inhibidor de la topoisomerasa I); terapia dirigida a HER2 |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto (como mínimo, hemograma y funciones hepática y renal) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto; se recomienda seguir las normas de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

No se dispone de advertencias principales ni de contraindicaciones del prospecto en los datos compilados.

- **Interacciones Farmacológicas**: se identificaron 42 interacciones en total. Entre las de nivel **Mayor** figuran deferiprona, samario (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribina, leflunomida y natalizumab. Entre las de nivel **Moderado** figuran palifermina, cloruro de estroncio Sr-89, roflumilast, cloranfenicol (también oftálmico), alefacept, alemtuzumab, anakinra, azatioprina, canakinumab, dimetilfumarato y niraparib. Se muestran las 20 primeras de las 42 interacciones; la mayoría involucra fármacos inmunosupresores o mielosupresores.

Para el resto de la información de seguridad, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en una puntuación del modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible; además, el tratamiento oncológico podría favorecer la pérdida ósea. Tampoco se dispone de datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones del prospecto de la AEMPS (descargar y analizar el PDF)
- Completar los datos del mecanismo de acción desde DrugBank
- Confirmar la indicación aprobada de las autorizaciones españolas
- Realizar una revisión de literatura y estudios preclínicos que respalden un posible vínculo con el metabolismo óseo
- Reevaluar la predicción antes de cualquier avance, dado que la puntuación proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes aprendidas entre enfermedades relacionadas, no evidencia biológica

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Enhertu (fam-trastuzumab deruxtecan-nxki) prescribing information, Daiichi Sankyo Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7e67e73e-ddf4-4e4d-8b50-09d7514910b6) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


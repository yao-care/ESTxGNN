---
layout: default
title: Trastuzumab Deruxtecan
parent: Solo predicción del modelo (L5)
nav_order: 816
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Trastuzumab Deruxtecan: nueva indicación predicha, Osteoporosis inducida por fármacos (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de …"
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Trastuzumab Deruxtecán: De Indicación Original No Especificada a Osteoporosis Inducida por Fármacos

## Resumen en Una Frase

Trastuzumab deruxtecán es un conjugado anticuerpo-fármaco dirigido a HER2 que lleva como carga citotóxica un inhibidor de la topoisomerasa I (deruxtecán, derivado de la exatecán). En los datos compilados para este informe no consta el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **osteoporosis inducida por fármacos**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Osteoporosis inducida por fármacos |
| Puntaje de Predicción TxGNN | 99,31 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este fármaco. Según la información conocida, trastuzumab deruxtecán es un conjugado anticuerpo-fármaco: un anticuerpo dirigido a HER2 unido a un inhibidor de la topoisomerasa I (deruxtecán). Es un fármaco de uso oncológico.

La única base de la predicción es la puntuación muy alta del grafo de conocimiento de TxGNN (0,993). No se identifica una vía mecanística establecida que relacione la diana HER2 o la inhibición de la topoisomerasa I con la prevención o el tratamiento de la pérdida ósea causada por fármacos (por ejemplo, glucocorticoides o inhibidores de la aromatasa).

Al contrario, los efectos del tratamiento oncológico (como la supresión de la función ovárica o la coadministración de esteroides) podrían asociarse con pérdida ósea y no con protección. La puntuación elevada probablemente refleja artefactos de la topología del grafo más que una relevancia terapéutica real, por lo que la predicción debe interpretarse con mucha cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1201508001IP1 | ENHERTU 100 MG polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No especificada |
| 1201508001 | ENHERTU 100 MG polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No especificada |
| 1201508001IP | ENHERTU 100 MG polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No especificada |

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
- Reevaluar la predicción antes de cualquier avance, dado que probablemente se trate de un artefacto del grafo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Prednicarbate
parent: Solo predicción del modelo (L5)
nav_order: 657
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Prednicarbate: nueva indicación predicha, Queratosis folicular invertida vulvar (nivel de evidencia L5). Indicación original: Dermatosis inflamatorias cutáneas (dermatitis atópica…"
monitor_inn: "Prednicarbate"
predicted_indications: ["vulvar inverted follicular keratosis", "lichen planus pigmentosus", "hypertrophic lichen planus", "annular atrophic lichen planus", "lichen planus pemphigoides", "2-hydroxyethyl methacrylate sensitization", "primary cutaneous B-cell lymphoma"]
---

# Prednicarbate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Prednicarbato: De Dermatosis Inflamatorias Cutáneas a Queratosis Folicular Invertida Vulvar
{: .text-alpha }

## Resumen en Una Frase

Prednicarbato es un corticosteroide tópico, utilizado originalmente para tratar dermatitis (atópica, de contacto, seborreica), enfermedades liquenoides y otras dermatosis inflamatorias.
El modelo TxGNN predice que podría ser efectivo para **queratosis folicular invertida vulvar**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dermatosis inflamatorias cutáneas (dermatitis atópica, de contacto y seborreica, enfermedad liquenoide, entre otras). Los textos de indicación de las autorizaciones españolas no están disponibles; la información procede del grafo de conocimiento |
| Nueva Indicación Predicha | Queratosis folicular invertida vulvar |
| Puntaje de Predicción TxGNN | 99,88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone actualmente de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, prednicarbato es un corticosteroide tópico de potencia media, con efectos antiinflamatorios y antiproliferativos, y su eficacia en dermatosis inflamatorias ha sido establecida. Mecanísticamente, podría ser aplicable a la nueva indicación.

La relación con la indicación original es la queratosis seborreica, una lesión queratinocítica benigna relacionada, para la cual el prednicarbato ya figura como indicado en el grafo de conocimiento. Este es el principal vínculo que sustenta la predicción.

Sin embargo, la queratosis folicular invertida se trata habitualmente mediante escisión, y no existe evidencia que respalde un papel de los corticosteroides tópicos. El puntaje elevado (99,88%) es solo una predicción del modelo y debe interpretarse con cautela.

### Otras Predicciones del Modelo

Todas con nivel de evidencia L5, sin ensayos ni literatura, y recomendación Hold:

| Posición | Indicación Predicha | Puntaje TxGNN | Comentario |
|------|------|------|------|
| 2 | Liquen plano pigmentoso | 99,64% | Dermatosis liquenoide inflamatoria; plausible por la indicación existente en enfermedad liquenoide |
| 3 | Liquen plano hipertrófico | 99,64% | Vínculo biológico fuerte, pero un agente de potencia media podría ser insuficiente en lesiones gruesas |
| 4 | Liquen plano atrófico anular | 99,64% | La atrofia es un efecto adverso conocido de los corticosteroides; consideración de seguridad |
| 5 | Penfigoide liquenoide (liquen plano penfigoide) | 99,53% | Plausibilidad moderada; los casos graves suelen requerir inmunosupresión sistémica |
| 6 | Sensibilización a metacrilato de 2-hidroxietilo | 99,47% | Manejo sintomático de dermatitis de contacto ya indicada; no es un uso nuevo |
| 7 | Linfoma cutáneo primario de células B | 99,40% | Extrapolación por analogía con el linfoma cutáneo de células T; poco probable que modifique la enfermedad |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 60371 | PEITEL 2,5 MG/G UNGUENTO (Ferrer Internacional S.A.) | Pomada | No disponible |
| 60458 | BATMEN 2,5 MG/G CREMA (A. Menarini Latin America S.L.) | Crema | No disponible |
| 60459 | BATMEN SOLUCION (Laboratorios Menarini S.A.) | Solución cutánea | No disponible |
| 60370 | PEITEL 2,5 MG/G POMADA (Galenicum Derma S.L.) | Pomada | No disponible |
| 60372 | PEITEL 2,5 MG/G CREMA (Galenicum Derma S.L.) | Crema | No disponible |

Se muestran 5 de las 8 autorizaciones vigentes (todas de medicamento con un único principio activo, ninguna cancelada).

## Consideraciones de Seguridad

- **Enfermedades con contraindicación o precaución según el grafo de conocimiento** (no proviene del texto del prospecto): insuficiencia suprarrenal, enfermedad de Addison, atrofia cutánea, telangiectasia, enfermedad capilar, telangiectasia hemorrágica hereditaria, enfermedad vascular periférica, claudicación vascular intermitente y enfermedad arterial periférica.
- **Interacciones farmacológicas**: no se encontraron interacciones registradas en la consulta realizada.

Consultar el prospecto para información de seguridad completa sobre advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y el tratamiento estándar de la queratosis folicular invertida es quirúrgico. Aunque el fármaco está comercializado en España, no hay evidencia que justifique avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) para analizar el vínculo mecanístico
- Advertencias y contraindicaciones del prospecto de la AEMPS, así como los textos de indicación aprobada
- Revisión sistemática de la literatura y de registros de ensayos sobre corticosteroides tópicos en queratosis folicular invertida
- Evaluación de compatibilidad de vía de administración y de la potencia necesaria para la localización vulvar, dado el riesgo de atrofia cutánea
- Valorar de forma prioritaria las indicaciones relacionadas con liquen plano, que tienen mayor plausibilidad biológica, antes de invertir en la indicación principal
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


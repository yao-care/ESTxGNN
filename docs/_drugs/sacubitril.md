---
layout: default
title: Sacubitril
parent: Solo predicción del modelo (L5)
nav_order: 720
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-20
description: "Sacubitril: nueva indicación predicha, Enfermedad de pequeño vaso cerebral tipo 1 con o sin anomalías oculares (nivel de evidencia L5). Indicación original: No disponible en los datos de autorización …"
monitor_inn: "sacubitril"
predicted_indications: ["brain small vessel disease 1 with or without ocular anomalies", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "diabetic nephropathy", "rheumatoid arthritis", "hemoglobinopathy"]
---

# Sacubitril
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Sacubitrilo: De Indicación No Especificada en la Ficha a Enfermedad de pequeño vaso cerebral tipo 1 con o sin anomalías oculares
{: .text-alpha }

## Resumen en Una Frase

Sacubitrilo es un inhibidor de la neprilisina que se comercializa en España combinado con valsartán (Entresto, Neparvis y genéricos); los datos compilados para este informe no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de pequeño vaso cerebral tipo 1 con o sin anomalías oculares**, pero la evidencia es solo predictiva: **0 ensayos clínicos** y **1 publicación** no directamente relacionada.
Entre las predicciones evaluadas, **nefropatía diabética** muestra mucho más respaldo (1 ensayo de Fase 4 y numerosas publicaciones) y se comenta como alternativa en la conclusión.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de autorización (el texto de indicación está vacío) |
| Nueva Indicación Predicha | Enfermedad de pequeño vaso cerebral tipo 1 con o sin anomalías oculares |
| Puntaje de Predicción TxGNN | 0,9958 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 4; autorizadas no comercializadas: 16) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para sacubitril and valsartan (combinación que contiene Sacubitril) (traducción no oficial): «Sacubitrilo y valsartán contiene un inhibidor de la neprilisina, el sacubitrilo, y un antagonista del receptor de angiotensina, el valsartán. Sacubitrilo y valsartán inhibe la neprilisina (endopeptidasa neutra; NEP) a través de LBQ657, el metabolito activo del profármaco sacubitrilo, y bloquea el receptor de angiotensina II de tipo 1 (AT 1 ) a través del valsartán.» Texto original en inglés: "Sacubitril and valsartan contains a neprilysin inhibitor, sacubitril, and an angiotensin receptor blocker, valsartan. Sacubitril and valsartan inhibits neprilysin (neutral endopeptidase; NEP) via LBQ657, the active metabolite of the prodrug sacubitril, and blocks the angiotensin II type-1 (AT 1 ) receptor via valsartan." ([DailyMed: sacubitril and valsartan prescribing information, Novadoz Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=44db8114-622e-41f6-96a1-447d47b0267c), versión del 2026-10-30; consultado el 2026-11-19). Según la información conocida, sacubitrilo es un profármaco inhibidor de la neprilisina que se administra junto con valsartán (bloqueador del receptor AT1 de angiotensina II). Esta combinación eleva los péptidos natriuréticos y bloquea el sistema renina-angiotensina, con efectos sobre el tono vascular y la presión arterial.

La enfermedad predicha es un trastorno monogénico raro (relacionado con COL4A1) causado por un defecto estructural de la membrana basal vascular. Teóricamente, el fármaco podría influir en el tono vascular y la presión arterial, pero no hay evidencia de que modifique la patología subyacente. No se ha establecido un vínculo mecanístico directo.

El puntaje TxGNN es muy alto (0,9958), pero proviene del modelo TxGNN (aprendizaje profundo) y probablemente refleja similitudes que el modelo aprendió entre enfermedades relacionadas con COL4A1, no evidencia biológica ni una farmacología validada. La única publicación recuperada trata sobre insuficiencia del ventrículo derecho sistémico, no sobre enfermedad de pequeño vaso cerebral.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37169551](https://pubmed.ncbi.nlm.nih.gov/37169551/) | 2023 | Cohorte | Heart | Tolerabilidad y efectos de sacubitrilo/valsartán en insuficiencia del ventrículo derecho sistémico en adultos. No guarda relación directa con la enfermedad de pequeño vaso cerebral. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 151058003IP | ENTRESTO 49 mg/51 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 161103006IP | NEPARVIS 97 mg/103 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 151058006IP1 | ENTRESTO 97 mg/103 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 1151058001 | ENTRESTO 24 mg/26 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 90633 | BIDCOR 24 mg/26 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |

Hay 20 autorizaciones vigentes en total, todas de producto único (sacubitrilo/valsartán), incluidos genéricos (EFG).

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (6 interacciones de nivel moderado): nitisinona, rosuvastatina, simvastatina, cobicistat, revefenacina y alpelisib.

Para advertencias y contraindicaciones, consultar el prospecto. Con otras indicaciones evaluadas se mencionan además riesgos de hiperpotasemia e hipotensión.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5): no hay ensayos clínicos, la única publicación no es pertinente y no existe un vínculo mecanístico creíble con una enfermedad estructural de la membrana basal.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del texto de indicaciones, advertencias y contraindicaciones del prospecto de la AEMPS
- Evidencia preclínica en modelos de enfermedad relacionada con COL4A1
- Valorar priorizar **nefropatía diabética** (nivel L3, ensayo de Fase 4 NCT06501651 en curso con estado desconocido y sin resultados, y estudios preclínicos consistentes), que ofrece una base mucho más sólida para reposicionamiento

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: sacubitril and valsartan prescribing information, Novadoz Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=44db8114-622e-41f6-96a1-447d47b0267c) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


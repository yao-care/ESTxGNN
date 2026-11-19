---
layout: default
title: Avelumab
parent: Solo predicción del modelo (L5)
nav_order: 80
evidence_level: L5
indication_count: 9
monitor_inn: "AVELUMAB"
predicted_indications: ["human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "adenosine deaminase deficiency", "reticular dysgenesis", "Immunoerythromyeloid hypoplasia", "non-severe combined immunodeficiency", "kidney pelvis sarcomatoid transitional cell carcinoma"]
last_modified_at: 2026-11-05
description: "Avelumab: nueva indicación predicha, Tumor relacionado con el herpesvirus humano 8 (human herpesvirus 8-related tumor) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 3 (comercializadas: 3)"
---

# Avelumab
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

## Avelumab: anticuerpo anti-PD-L1 (inhibidor del punto de control inmunitario) → tumor relacionado con el herpesvirus humano 8 (human herpesvirus 8-related tumor)
{: .text-alpha }

## Resumen en Una Frase

Avelumab es un anticuerpo monoclonal que bloquea PD-L1 y se comercializa en España como Bavencio.
El modelo TxGNN predice que podría ser efectivo para el **tumor relacionado con el herpesvirus humano 8 (human herpesvirus 8-related tumor)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** en los datos compilados para este informe que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Tumor relacionado con el herpesvirus humano 8 (human herpesvirus 8-related tumor) |
| Puntaje de Predicción TxGNN | 0,9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 3 de 3) |
| Número de Autorizaciones | 3 (comercializadas: 3) |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Avelumab (traducción no oficial): «PD-L1 puede expresarse en las células tumorales y en las células inmunitarias infiltrantes del tumor, y puede contribuir a la inhibición de la respuesta inmunitaria antitumoral en el microambiente tumoral. La unión de PD-L1 a los receptores PD-1 y B7.1 presentes en los linfocitos T y en las células presentadoras de antígenos suprime la actividad de los linfocitos T citotóxicos, la proliferación de los linfocitos T y la producción de citocinas. […] El avelumab se une a PD-L1 y bloquea la interacción entre PD-L1 y sus receptores PD-1 y B7.1.» Texto original en inglés: "PD-L1 may be expressed on tumor cells and tumor-infiltrating immune cells and can contribute to the inhibition of the anti-tumor immune response in the tumor microenvironment. Binding of PD-L1 to the PD-1 and B7.1 receptors found on T cells and antigen presenting cells suppresses cytotoxic T-cell activity, T-cell proliferation, and cytokine production. […] Avelumab binds PD-L1 and blocks the interaction between PD-L1 and its receptors PD-1 and B7.1." ([DailyMed: Bavencio (avelumab) prescribing information, EMD Serono, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5cd725a1-2fa4-408a-a651-57a7b84b2118), versión del 2026-09-22; consultado el 2026-11-19). Según la información conocida, avelumab es un anticuerpo anti-PD-L1: al bloquear la interacción entre PD-L1 y su receptor PD-1, puede reactivar la respuesta de los linfocitos T frente a células tumorales.

Los tumores asociados al herpesvirus humano 8 (por ejemplo, el sarcoma de Kaposi) son tumores de origen viral. En ellos se ha descrito agotamiento inmunitario relacionado con el eje PD-1/PD-L1, lo que ofrece una justificación biológica plausible para el bloqueo de PD-L1.

No obstante, este vínculo se apoya únicamente en la predicción del modelo y en razonamiento biológico general. No se aportaron ensayos ni literatura que lo confirmen, por lo que debe considerarse una hipótesis.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 171214001IP | BAVENCIO 20 MG/ML CONCENTRADO PARA SOLUCION PARA PERFUSION | Concentrado para solución para perfusión | No registrada en los datos locales |
| 1171214001 | BAVENCIO 20 MG/ML CONCENTRADO PARA SOLUCION PARA PERFUSION | Concentrado para solución para perfusión | No registrada en los datos locales |
| 171214001IP1 | BAVENCIO 20 MG/ML CONCENTRADO PARA SOLUCION PARA PERFUSION | Concentrado para solución para perfusión | No registrada en los datos locales |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo monoclonal anti-PD-L1) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (3 interacciones de nivel Mayor registradas):
  - Lenalidomida (Mayor)
  - Pomalidomida (Mayor)
  - Talidomida (Mayor)

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje TxGNN alto (0,9997), pero no cuenta con ensayos clínicos ni literatura que estudien directamente esta enfermedad (nivel de evidencia L5). Por ahora solo puede considerarse una hipótesis.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre bloqueo de PD-1/PD-L1 en tumores asociados al herpesvirus humano 8 (p. ej., sarcoma de Kaposi)
- Datos de expresión de PD-L1 en este tipo de tumores
- Datos detallados del mecanismo de acción (MOA)
- Advertencias y contraindicaciones del prospecto de la AEMPS
- Evaluación de la relevancia clínica de las interacciones mayores con lenalidomida, pomalidomida y talidomida
- Si los datos lo respaldan, diseño de un estudio exploratorio de fase 2

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Bavencio (avelumab) prescribing information, EMD Serono, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5cd725a1-2fa4-408a-a651-57a7b84b2118) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


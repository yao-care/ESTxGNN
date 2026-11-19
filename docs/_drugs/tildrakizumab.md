---
layout: default
title: Tildrakizumab
parent: Solo predicción del modelo (L5)
nav_order: 794
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-05
description: "Tildrakizumab: nueva indicación predicha, Retinopatía diabética no proliferativa grave (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (el texto de indicación de l…"
monitor_inn: "TILDRAKIZUMAB"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract", "drug-induced osteoporosis"]
---

# Tildrakizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Tildrakizumab: De Indicación Original No Registrada a Retinopatía Diabética No Proliferativa Grave
{: .text-alpha }

## Resumen en Una Frase

Tildrakizumab es un anticuerpo monoclonal dirigido contra la subunidad p19 de la IL-23, comercializado en España como ILUMETRI; los datos compilados para este informe no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **retinopatía diabética no proliferativa grave**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.
Se trata de una predicción puramente computacional (nivel de evidencia L5).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (el texto de indicación de las autorizaciones está vacío) |
| Nueva Indicación Predicha | Retinopatía diabética no proliferativa grave |
| Puntaje de Predicción TxGNN | 0,9963 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 3 de 4; autorizadas no comercializadas: 1) |
| Número de Autorizaciones | 4 (comercializadas: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Tildrakizumab (traducción no oficial): «Tildrakizumab es un anticuerpo monoclonal IgG1/k humanizado que se une selectivamente a la subunidad p19 de la IL-23 e inhibe su interacción con el receptor de la IL-23. La IL-23 es una citocina de origen natural que participa en las respuestas inflamatorias e inmunitarias.» Texto original en inglés: "Tildrakizumab is a humanized IgG1/k monoclonal antibody that selectively binds to the p19 subunit of IL-23 and inhibits its interaction with the IL-23 receptor. IL-23 is a naturally occurring cytokine that is involved in inflammatory and immune responses." ([DailyMed: Ilumya (tildrakizumab-asmn) prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c6a322bb-51b9-4f0e-8642-62a9682ffcde), versión del 2026-11-02; consultado el 2026-11-19). Según la información conocida, tildrakizumab es un anticuerpo monoclonal anti-IL-23 p19, que bloquea el eje inflamatorio IL-23/IL-17.

La hipótesis es que la inflamación crónica de bajo grado, incluido el eje IL-23/IL-17, podría contribuir al daño vascular retiniano en la retinopatía diabética. Este vínculo es **especulativo**: no hay ensayos ni literatura que lo respalden, y el puntaje de 0,9963 es solo una predicción del modelo.

Además, plantea dudas adicionales de seguridad y viabilidad: la administración intravítrea de un anticuerpo de gran tamaño, o bien la inmunosupresión sistémica en una población diabética. Las terapias establecidas (anti-VEGF, láser, control glucémico y de la presión arterial) actúan por mecanismos distintos, y no hay una justificación demostrada para preferir el bloqueo de IL-23.

### Otras indicaciones predichas (para referencia)

| Indicación predicha | Puntaje TxGNN | Nivel de evidencia | Comentario |
|------|------|------|------|
| Retinopatía diabética | 0,9953 | L5 | Misma hipótesis inflamatoria; sin ensayos ni publicaciones |
| Catarata diabética | 0,9921 | L5 | Vínculo débil: predominan la vía de los polioles, el estrés oxidativo y la glicación; la cirugía es el tratamiento definitivo |
| Osteoporosis inducida por fármacos | 0,9920 | L5 | Vínculo plausible pero indirecto (IL-17 favorece la osteoclastogénesis vía RANKL); ya existen bisfosfonatos, denosumab y teriparatida |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1181323002 | ILUMETRI 100 mg solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No disponible |
| 1181323001 | ILUMETRI 100 mg solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No disponible |
| 1181323004 | ILUMETRI 100 mg solución inyectable en pluma precargada | Solución inyectable en pluma precargada | No disponible |
| 1181323003 | ILUMETRI 200 mg solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No disponible |

Titular: Almirall S.A. Las cuatro autorizaciones son de monofármaco y están vigentes.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 78 interacciones en total; a continuación se listan algunas de las principales (de la muestra disponible):
  - **Mayor**: adalimumab, baricitinib, certolizumab pegol, cladribina.
  - **Moderada**: roflumilast, tacrolimus, azatioprina, ciclosporina, alefacept, alemtuzumab, anakinra, canakinumab, denosumab, toxoide tetánico y vacunas (carbunco, cólera vivo).
  - **Menor**: sales de zinc (sulfato, acetato, gluconato, cloruro).

  En general, destacan la combinación con otros inmunosupresores o biológicos y las vacunas, por riesgo de inmunosupresión aditiva.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo TxGNN (nivel L5), sin ensayos clínicos ni literatura, con un vínculo mecanístico especulativo y alternativas terapéuticas establecidas para la retinopatía diabética.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción y de la indicación original aprobada.
- Estudios preclínicos que respalden un papel de IL-23/IL-17 en el daño vascular retiniano.
- Revisión sistemática de la literatura y de registros de ensayos.
- Evaluación de la vía de administración (intravítrea frente a sistémica) y de su viabilidad.
- Análisis de seguridad con el prospecto (advertencias y contraindicaciones), especialmente en pacientes diabéticos e inmunosuprimidos.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Ilumya (tildrakizumab-asmn) prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c6a322bb-51b9-4f0e-8642-62a9682ffcde) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


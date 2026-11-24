---
layout: default
title: Reslizumab
parent: Solo predicción del modelo (L5)
nav_order: 693
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "RESLIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets"]
description: "Reslizumab: nueva indicación predicha, Trombocitopenia por destrucción inmune (thrombocytopenia due to immune destruction) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 1)"
---

# Reslizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Reslizumab: Trombocitopenia por destrucción inmune (thrombocytopenia due to immune destruction)
{: .text-alpha }

## Resumen en Una Frase

Reslizumab es un anticuerpo monoclonal anti-IL-5, asociado originalmente a enfermedades eosinofílicas pulmonares (neumonía eosinofílica y eosinofilia pulmonar).
El modelo TxGNN predice que podría ser efectivo para **trombocitopenia por destrucción inmune**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Trombocitopenia por destrucción inmune (thrombocytopenia due to immune destruction) |
| Puntaje de Predicción TxGNN | 0.9953 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Reslizumab (traducción no oficial): «Reslizumab es un antagonista de la interleucina 5 (IgG4, kappa). La IL-5 es la principal citocina responsable del crecimiento y la diferenciación, el reclutamiento, la activación y la supervivencia de los eosinófilos. Reslizumab se une a la IL-5 con una constante de disociación de 81 pM e inhibe la bioactividad de la IL-5 al bloquear su unión a la cadena alfa del complejo del receptor de IL-5 expresado en la superficie de los eosinófilos.» Texto original en inglés: "Reslizumab is an interleukin-5 antagonist (IgG4, kappa). IL-5 is the major cytokine responsible for the growth and differentiation, recruitment, activation, and survival of eosinophils. Reslizumab binds to IL-5 with a dissociation constant of 81 pM, inhibiting the bioactivity of IL-5 by blocking its binding to the alpha chain of the IL-5 receptor complex expressed on the eosinophil surface." ([DailyMed: Cinqair (reslizumab) prescribing information, Teva Respiratory, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=053b9158-2a5b-48b9-bf47-5fa78a35ec33), versión del 2020-02-29; consultado el 2026-11-19). Según la información conocida, reslizumab es un anticuerpo monoclonal que bloquea la interleucina-5 (IL-5), la principal señal de supervivencia de los eosinófilos, y su uso se relaciona con enfermedades eosinofílicas.

No existe un mecanismo establecido que vincule el bloqueo de IL-5 con la destrucción inmune de plaquetas. La trombocitopenia inmune (por ejemplo, la PTI) se debe principalmente a autoanticuerpos, desregulación de linfocitos T y aclaramiento mediado por macrófagos. Una posible conexión, de carácter especulativo, sería la reducción de la inflamación asociada a eosinófilos en trombocitopenias inmunes secundarias con eosinofilia.

Por tanto, el elevado puntaje de TxGNN (0,9953) es solo una predicción computacional, sin respaldo clínico ni bibliográfico en los datos compilados. La similitud con la indicación original no ha sido evaluada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal predicha.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 1161125001 | CINQAERO 10 MG/ML CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Teva B.V. | Comercializada |

Se muestra la única autorización con este principio activo en los datos de CIMA (AEMPS).

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre el bloqueo de IL-5 y la destrucción inmune de plaquetas.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), requisito bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisión de literatura específica sobre IL-5/eosinófilos en trombocitopenia inmune.
- Evaluar hipótesis mecanística (p. ej., trombocitopenia inmune secundaria con eosinofilia) y, de ser plausible, estudios preclínicos o de mecanismo.
- Evaluar la compatibilidad de la vía de administración (actualmente pendiente).

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Cinqair (reslizumab) prescribing information, Teva Respiratory, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=053b9158-2a5b-48b9-bf47-5fa78a35ec33) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


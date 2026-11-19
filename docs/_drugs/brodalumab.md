---
layout: default
title: Brodalumab
parent: Solo predicción del modelo (L5)
nav_order: 115
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
description: "Brodalumab: nueva indicación predicha, Estrongiloidiasis (nivel de evidencia L5). Indicación original: No disponible en los datos de la autorización de AEMPS"
monitor_inn: "BRODALUMAB"
predicted_indications: ["strongyloidiasis", "eye disease", "vitamin deficiency disorder", "von Hippel anomaly", "recurrent idiopathic neuroretinitis", "chronic relapsing inflammatory optic neuropathy", "optic perineuritis", "isolated optic neuritis", "episcleritis periodica fugax", "nodular episcleritis"]
---

# Brodalumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Brodalumab: De Indicación Original No Especificada a Enfermedad Ocular (Estrongiloidiasis como predicción principal)
{: .text-alpha }

> Nota: la predicción de mayor puntaje del modelo es **estrongiloidiasis**, pero carece de toda evidencia. Se muestra también la predicción con mayor soporte documental (**enfermedad ocular**), de forma informativa.

## Resumen en Una Frase

Brodalumab es un anticuerpo monoclonal antagonista del receptor A de la interleucina-17 (IL-17RA), comercializado en España como Kyntheum, cuya indicación aprobada no figura en los datos compilados para este informe.
El modelo TxGNN predice que podría ser efectivo para **estrongiloidiasis**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; la segunda predicción, **enfermedad ocular**, cuenta con **3 publicaciones** indirectas y ningún ensayo clínico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de la autorización de AEMPS |
| Nueva Indicación Predicha | Estrongiloidiasis |
| Puntaje de Predicción TxGNN | 0,9984 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Brodalumab bloquea el receptor IL-17RA, una vía compartida por varias isoformas de IL-17. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Brodalumab (traducción no oficial): «El brodalumab es un anticuerpo monoclonal IgG2 humano que se une selectivamente a la IL-17RA humana e inhibe sus interacciones con las citocinas IL-17A, IL-17F, IL-17C, el heterodímero IL-17A/F e IL-25. La IL-17RA es una proteína expresada en la superficie celular y es un componente necesario de los complejos receptores utilizados por múltiples citocinas de la familia IL-17.» Texto original en inglés: "Brodalumab is a human monoclonal IgG2 antibody that selectively binds to human IL-17RA and inhibits its interactions with cytokines IL-17A, IL-17F, IL-17C, IL-17A/F heterodimer, and IL-25. IL-17RA is a protein expressed on the cell surface and is a required component of receptor complexes utilized by multiple IL-17 family cytokines." ([DailyMed: Siliq (brodalumab) prescribing information, Bausch Health US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1a550c33-456a-4833-814e-8591aea7c688), versión del 2026-05-28; consultado el 2026-11-19).

Para la estrongiloidiasis, no se identificó ningún vínculo clínico ni bibliográfico. La IL-17 participa en la defensa del huésped frente a algunos patógenos, por lo que bloquearla podría, en teoría, aumentar el riesgo de infección en lugar de tratarla. El puntaje alto del modelo es solo una predicción sin datos de respaldo, y la predicción no resulta mecanísticamente razonable con la información disponible.

Como referencia, la predicción de **enfermedad ocular** (puntaje 0,9982) tiene una justificación plausible, ya que la vía IL-17 se ha implicado en inflamación ocular como la uveítis. Sin embargo, la literatura recuperada es indirecta y en parte contradictoria, y "enfermedad ocular" es una categoría demasiado amplia para ser accionable. El resto de predicciones (deficiencia vitamínica, anomalía de von Hippel, neuropatías ópticas inflamatorias, epiescleritis) carecen de evidencia y, en su mayoría, de vínculo mecanístico claro.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para estrongiloidiasis (ni para enfermedad ocular).

## Evidencia de Literatura

Para estrongiloidiasis, actualmente no hay literatura relacionada disponible. Como referencia, la literatura para la segunda predicción (enfermedad ocular) es:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41916603](https://pubmed.ncbi.nlm.nih.gov/41916603/) | 2026 | Farmacovigilancia (mundo real) | Canadian Journal of Ophthalmology | Análisis de fármacos sistémicos asociados desproporcionadamente con eventos de uveítis; se trata de un evento adverso, no de eficacia |
| [41770262](https://pubmed.ncbi.nlm.nih.gov/41770262/) | 2026 | Reporte de caso | Rheumatology International | Primer caso de enfermedad de Behçet como reacción paradójica tras iniciar brodalumab en un paciente con osteítis no bacteriana crónica |
| [42576218](https://pubmed.ncbi.nlm.nih.gov/42576218/) | 2026 | Preclínico (modelo animal) | Journal of Translational Medicine | El bloqueo de IL-17R con brodalumab limita la periodontitis experimental; no es un estudio de enfermedad ocular |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1161155001 | KYNTHEUM 210 MG SOLUCIÓN INYECTABLE EN JERINGA PRECARGADA | Solución inyectable | No especificada en los datos |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento TxGNN, no el prospecto)**: enfermedad de Crohn, enfermedad inflamatoria intestinal y colitis de Crohn.
- **Advertencia adicional señalada en el análisis**: se menciona una advertencia de ideación y conducta suicida, que pesaría sobre cualquier nuevo uso neurológico u oftálmico; debe confirmarse con el prospecto.
- **Interacciones farmacológicas**: se identificaron 68 interacciones en total. Entre las principales:
  - **Mayor**: adalimumab, baricitinib, certolizumab pegol, vacuna BCG (cepa Tice, viva).
  - **Moderada**: roflumilast, alefacept, alemtuzumab, anakinra, canakinumab, y diversas vacunas vivas o antígenos (ántrax, adenovirus tipo 4, cólera, *Candida albicans*, toxoide tetánico).
  - **Menor**: sales de zinc (acetato, gluconato, sulfato, cloruro).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de estrongiloidiasis tiene un puntaje alto del modelo, pero ninguna evidencia clínica ni bibliográfica (L5), y el bloqueo de IL-17 podría aumentar el riesgo de infección. La predicción de enfermedad ocular (L4) tiene una justificación plausible, pero la evidencia es indirecta y no demuestra beneficio terapéutico.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS (indicaciones, advertencias y contraindicaciones), lo cual es un requisito bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Para estrongiloidiasis: evidencia preclínica o clínica que justifique la hipótesis frente al riesgo infeccioso teórico.
- Para el ámbito ocular: acotar a una entidad específica (por ejemplo, uveítis no infecciosa) y buscar estudios dirigidos.
- Evaluar la compatibilidad de la vía de administración (pendiente) y el perfil de seguridad, incluido el riesgo de ideación suicida y las contraindicaciones en enfermedad inflamatoria intestinal.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Siliq (brodalumab) prescribing information, Bausch Health US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1a550c33-456a-4833-814e-8591aea7c688) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


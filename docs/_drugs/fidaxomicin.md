---
layout: default
title: Fidaxomicin
parent: Solo predicción del modelo (L5)
nav_order: 335
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Fidaxomicin: nueva indicación predicha, Síndrome de la piel escaldada estafilocócica (nivel de evidencia L5). Indicación original: Colitis por Clostridium difficile"
monitor_inn: "fidaxomicin"
predicted_indications: ["staphylococcal scalded skin syndrome", "bullous impetigo", "inhalational botulism", "impetigo", "toxin-mediated infectious botulism", "vulvovaginal candidiasis", "hordeolum", "staphylococcus aureus pneumonia", "punctate epithelial keratoconjunctivitis"]
---

# Fidaxomicin
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

## Fidaxomicina: De Colitis por Clostridium difficile a Síndrome de la Piel Escaldada Estafilocócica
{: .text-alpha }

## Resumen en Una Frase

Fidaxomicina es un antibiótico macrocíclico de espectro estrecho, originalmente utilizado para la colitis por *Clostridium difficile*.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de la piel escaldada estafilocócica**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Colitis por *Clostridium difficile* |
| Nueva Indicación Predicha | Síndrome de la piel escaldada estafilocócica |
| Puntaje de Predicción TxGNN | 0.9971 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 2) |
| Número de Autorizaciones | 2 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Fidaxomicin (traducción no oficial): «La fidaxomicina es un fármaco antibacteriano. […] La fidaxomicina es un producto de fermentación obtenido del actinomiceto Dactylosporangium aurantiacum. La fidaxomicina es un fármaco antibacteriano macrólido que inhibe la síntesis de ARN mediante su unión a las ARN polimerasas. La fidaxomicina es bactericida frente a C. difficile in vitro y presenta un efecto posantibiótico frente a C. difficile de 6-10 h.» Texto original en inglés: "Fidaxomicin is an antibacterial drug. […] Fidaxomicin is a fermentation product obtained from the Actinomycete Dactylosporangium aurantiacum. Fidaxomicin is a macrolide antibacterial drug that inhibits RNA synthesis by binding to RNA polymerases. Fidaxomicin is bactericidal against C. difficile in vitro, and demonstrates a post-antibiotic effect vs. C. difficile of 6-10 hrs." ([DailyMed: Dificid (fidaxomicin) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dd966338-c820-4270-b704-09ef75fa3ceb), versión del 2024-10-16; consultado el 2026-11-19). Según la información conocida, fidaxomicina es un antibiótico macrocíclico de espectro estrecho que inhibe la ARN polimerasa bacteriana. Su actividad *in vitro* se dirige principalmente contra organismos grampositivos, incluidas algunas cepas de *Staphylococcus aureus*, por lo que existe un vínculo plausible.

El síndrome de la piel escaldada estafilocócica es una enfermedad mediada por toxinas exfoliativas que se trata habitualmente con antibióticos sistémicos antiestafilocócicos. Aquí aparece la principal limitación: fidaxomicina tiene una absorción sistémica mínima, por lo que es poco adecuada para una enfermedad cutánea tóxica de origen sistémico.

El alto puntaje de TxGNN es solo una predicción computacional, sin datos clínicos de apoyo. Por ello, la razonabilidad mecanística es débil.

### Otras predicciones del modelo (todas de nivel L5, decisión Hold)

| Indicación Predicha | Puntaje TxGNN | Comentario |
|------|------|------|
| Impétigo ampolloso | 0.9970 | Exposición cutánea insignificante; existen alternativas tópicas y sistémicas eficaces |
| Botulismo por inhalación | 0.9969 | Tratamiento basado en antitoxina; los antibióticos no tienen papel establecido |
| Impétigo | 0.9968 | No está formulado para uso cutáneo; hay agentes tópicos establecidos |
| Botulismo infeccioso mediado por toxina | 0.9966 | Vínculo especulativo; los antibióticos generalmente no se recomiendan por el riesgo de liberar más toxina |
| Candidiasis vulvovaginal | 0.9965 | Sin actividad antifúngica; la puntuación proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica |
| Orzuelo | 0.9964 | Solo vínculo teórico; sin formulación oftálmica |
| Neumonía por *Staphylococcus aureus* | 0.9921 | Exposición pulmonar no esperable por absorción mínima; existen alternativas establecidas |
| Queratoconjuntivitis epitelial punteada | 0.9902 | Sin mecanismo plausible ni datos clínicos |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (síndrome de la piel escaldada estafilocócica).

Para la quinta predicción en términos de interés clínico (neumonía por *S. aureus*) solo se identificó una revisión general, sin evidencia directa para fidaxomicina:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31634096](https://pubmed.ncbi.nlm.nih.gov/31634096/) | 2019 | Revisión | Journal of Hospital Medicine | Actualización de literatura de alto impacto en medicina hospitalaria; menciona vancomicina o fidaxomicina como tratamiento de primera línea para la infección por *C. difficile*, sin evidencia directa en neumonía estafilocócica |

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 11733004 | DIFICLIR 200 MG COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Tillotts Pharma Gmbh | Comercializada |
| 1110733005 | DIFICLIR 40 MG/ML GRANULADO PARA SUSPENSION ORAL | GRANULADO PARA SUSPENSIÓN ORAL | Tillotts Pharma Gmbh | Comercializada |

Se muestran las 2 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 79 interacciones en total. Entre las principales:
  - **Mayor**: vacuna viva contra el cólera (*Vibrio cholerae* CVD 103-HgR).
  - **Moderada**: alpelisib, apalutamida, binimetinib, ácido picosulfúrico.
  - **Menor** (entre otras): nifedipino, amiodarona, diltiazem, verapamilo, espironolactona, ciclosporina, claritromicina, eritromicina, dronedarona.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Todas las indicaciones predichas se apoyan únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura directa. Además, la absorción sistémica mínima de fidaxomicina contradice el mecanismo necesario para tratar enfermedades cutáneas o sistémicas mediadas por toxinas.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados y análisis de vínculo mecanístico.
- Advertencias y contraindicaciones del prospecto de la AEMPS (actualmente sin datos).
- Estudios preclínicos de actividad frente a cepas de *S. aureus* productoras de toxinas exfoliativas.
- Datos de exposición tisular o de una formulación adecuada (tópica o sistémica) que justifique la vía de administración.
- Evaluación de la compatibilidad de vía de administración para cada indicación candidata.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Dificid (fidaxomicin) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dd966338-c820-4270-b704-09ef75fa3ceb) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


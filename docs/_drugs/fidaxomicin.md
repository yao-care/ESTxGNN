---
layout: default
title: Fidaxomicin
parent: Solo predicción del modelo (L5)
nav_order: 335
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Fidaxomicin: nueva indicación predicha, Síndrome de la piel escaldada estafilocócica (nivel de evidencia L5). Indicación original: Colitis por Clostridium difficile"
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Fidaxomicina: De Colitis por Clostridium difficile a Síndrome de la Piel Escaldada Estafilocócica

## Resumen en Una Frase

Fidaxomicina es un antibiótico macrocíclico de espectro estrecho, originalmente utilizado para la colitis por *Clostridium difficile*.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de la piel escaldada estafilocócica**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Colitis por *Clostridium difficile* |
| Nueva Indicación Predicha | Síndrome de la piel escaldada estafilocócica |
| Puntaje de Predicción TxGNN | 99.71% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, fidaxomicina es un antibiótico macrocíclico de espectro estrecho que inhibe la ARN polimerasa bacteriana. Su actividad *in vitro* se dirige principalmente contra organismos grampositivos, incluidas algunas cepas de *Staphylococcus aureus*, por lo que existe un vínculo plausible.

El síndrome de la piel escaldada estafilocócica es una enfermedad mediada por toxinas exfoliativas que se trata habitualmente con antibióticos sistémicos antiestafilocócicos. Aquí aparece la principal limitación: fidaxomicina tiene una absorción sistémica mínima, por lo que es poco adecuada para una enfermedad cutánea tóxica de origen sistémico.

El alto puntaje de TxGNN es solo una predicción computacional, sin datos clínicos de apoyo. Por ello, la razonabilidad mecanística es débil.

### Otras predicciones del modelo (todas de nivel L5, decisión Hold)

| Indicación Predicha | Puntaje TxGNN | Comentario |
|------|------|------|
| Impétigo ampolloso | 99.70% | Exposición cutánea insignificante; existen alternativas tópicas y sistémicas eficaces |
| Botulismo por inhalación | 99.69% | Tratamiento basado en antitoxina; los antibióticos no tienen papel establecido |
| Impétigo | 99.68% | No está formulado para uso cutáneo; hay agentes tópicos establecidos |
| Botulismo infeccioso mediado por toxina | 99.66% | Vínculo especulativo; los antibióticos generalmente no se recomiendan por el riesgo de liberar más toxina |
| Candidiasis vulvovaginal | 99.65% | Sin actividad antifúngica; probable artefacto del grafo |
| Orzuelo | 99.64% | Solo vínculo teórico; sin formulación oftálmica |
| Neumonía por *Staphylococcus aureus* | 99.21% | Exposición pulmonar no esperable por absorción mínima; existen alternativas establecidas |
| Queratoconjuntivitis epitelial punteada | 99.02% | Sin mecanismo plausible ni datos clínicos |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (síndrome de la piel escaldada estafilocócica).

Para la quinta predicción en términos de interés clínico (neumonía por *S. aureus*) solo se identificó una revisión general, sin evidencia directa para fidaxomicina:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31634096](https://pubmed.ncbi.nlm.nih.gov/31634096/) | 2019 | Revisión | Journal of Hospital Medicine | Actualización de literatura de alto impacto en medicina hospitalaria; menciona vancomicina o fidaxomicina como tratamiento de primera línea para la infección por *C. difficile*, sin evidencia directa en neumonía estafilocócica |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 11733004 | DIFICLIR 200 MG comprimidos recubiertos con película | Comprimido recubierto con película | Titular: Tillotts Pharma GmbH |
| 1110733005 | DIFICLIR 40 MG/ML granulado para suspensión oral | Granulado para suspensión oral | Titular: Tillotts Pharma GmbH |

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


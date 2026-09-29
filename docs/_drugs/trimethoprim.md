---
layout: default
title: Trimethoprim
parent: Solo predicción del modelo (L5)
nav_order: 547
evidence_level: L5
indication_count: 2
---

# Trimethoprim
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Trimetoprima: De Infecciones Bacterianas a Queratoconjuntivitis Epitelial Punctata

## Resumen en Una Frase

La trimetoprima es un antibacteriano que inhibe la dihidrofolato reductasa bacteriana. El texto de indicación de sus autorizaciones en España no está disponible, así que su uso original se deduce de su mecanismo antibacteriano.
El modelo TxGNN predice que podría ser efectiva para **queratoconjuntivitis epitelial punctata**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción específica.
La indicación alternativa **conjuntivitis** (2.ª predicción) sí tiene 3 ensayos clínicos y 20 publicaciones, aunque solo 1 ensayo y 2 publicaciones son directamente relevantes.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punctata |
| Puntaje de Predicción TxGNN | 99.57% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, la trimetoprima bloquea la síntesis bacteriana de folato al inhibir la dihidrofolato reductasa. Se usa contra bacterias que causan infecciones oculares y, por vía tópica, suele combinarse con polimixina B.

La queratoconjuntivitis epitelial punctata suele ser de origen viral (por ejemplo, adenovirus) o inmunomediado. Un antibacteriano no tiene un vínculo mecanístico claro con esa patología. El puntaje alto probablemente refleja la cercanía en el grafo de conocimiento con la conjuntivitis bacteriana, donde la trimetoprima sí se usa. Su posible utilidad se limitaría a un componente bacteriano secundario, que aquí no está demostrado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para queratoconjuntivitis epitelial punctata.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para queratoconjuntivitis epitelial punctata.

## Indicación Alternativa con Evidencia: Conjuntivitis (2.ª predicción)

Esta predicción tiene un puntaje TxGNN de 99.17%, nivel de evidencia **L2** y decisión sugerida **Proceed with Guardrails**. El mecanismo encaja con la conjuntivitis bacteriana aguda, y la evidencia directa es solo para esa etiología, no para la viral, alérgica o clamidial. Parece un uso tópico ya establecido, por lo que el término "reposicionamiento" podría reflejar una laguna en los datos de indicación original.

### Ensayos clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00581542](https://clinicaltrials.gov/study/NCT00581542) | Fase 4 | Completado | 124 | Compara Polytrim (trimetoprima/polimixina B) oftálmico con moxifloxacino en conjuntivitis pediátrica. Relevancia directa (A), pero con simple ciego y combinación fija |
| [NCT00168532](https://clinicaltrials.gov/study/NCT00168532) | Fase 3 | Completado | 218 | Antibióticos profilácticos en sarampión (Guinea-Bisáu) para reducir neumonía y hospitalización. Evidencia indirecta (C) |
| [NCT03187834](https://clinicaltrials.gov/study/NCT03187834) | Fase 4 | Completado | 252 | Efecto de los antibióticos sobre resistencia y microbioma en niños de Burkina Faso. Evidencia indirecta (C) |

### Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/) | 2008 | ECA | J Pediatr Ophthalmol Strabismus | Compara la rapidez de eficacia clínica de polimixina B/trimetoprima frente a moxifloxacino 0.5% en conjuntivitis bacteriana |
| [30007329](https://pubmed.ncbi.nlm.nih.gov/30007329/) | 2018 | Revisión sistemática/Metaanálisis | J Pediatric Infect Dis Soc | Antibióticos (eritromicina, azitromicina y trimetoprima) en conjuntivitis clamidial neonatal |
| [16491721](https://pubmed.ncbi.nlm.nih.gov/16491721/) | 2006 | Revisión | J Pediatr Ophthalmol Strabismus | Control de la conjuntivitis bacteriana contagiosa y uso de antimicrobianos para reducir el periodo infeccioso |
| [20084257](https://pubmed.ncbi.nlm.nih.gov/20084257/) | 2001 | Revisión | Paediatr Child Health | Etiología, clínica y manejo de la conjuntivitis infecciosa aguda en niños |
| [10537781](https://pubmed.ncbi.nlm.nih.gov/10537781/) | 1999 | Revisión | Curr Opin Ophthalmol | Manifestaciones oculares de la enfermedad por arañazo de gato (*Bartonella henselae*) |
| [8595639](https://pubmed.ncbi.nlm.nih.gov/8595639/) | 1995 | Encuesta/Cohorte | Clin Ther | Encuesta en niños con conjuntivitis bacteriana aguda tratados con solución oftálmica de trimetoprima-polimixina B |
| [6204534](https://pubmed.ncbi.nlm.nih.gov/6204534/) | 1984 | Estudio clínico | Am J Ophthalmol | Eficacia y seguridad de soluciones oftálmicas con trimetoprima (con sulfacetamida y polimixina B) en conjuntivitis bacteriana o blefaritis |
| [34943657](https://pubmed.ncbi.nlm.nih.gov/34943657/) | 2021 | Cohorte | Antibiotics (Basel) | Características clínicas y moleculares de infecciones oculares por *S. aureus* sensible a meticilina en Taiwán |
| [21988450](https://pubmed.ncbi.nlm.nih.gov/21988450/) | 2011 | Estudio clínico | Curr Eye Res | Alta proporción de *S. pneumoniae* no tipificable en casos esporádicos de conjuntivitis bacteriana |
| [24892274](https://pubmed.ncbi.nlm.nih.gov/24892274/) | 2015 | Reporte de caso | Ophthalmic Plast Reconstr Surg | Conjuntivitis crónica por *Nocardia nova* asociada a stent de silicona, sensible a trimetoprima/sulfametoxazol |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 52548 | TEDIPRIMA 160 MG CÁPSULAS DURAS | Cápsula dura |
| 52547 | TEDIPRIMA 16 MG/ML SUSPENSIÓN ORAL | Suspensión oral |

Ambas autorizaciones pertenecen a Laboratorio Estedi S.L. y son de vía **oral**. Los estudios de conjuntivitis usaron formulaciones **tópicas oftálmicas**, que no figuran entre las autorizaciones locales.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold** (para queratoconjuntivitis epitelial punctata)

**Justificación:**
El puntaje TxGNN es muy alto (99.57%), pero no hay ensayos ni literatura que lo respalden. El mecanismo antibacteriano tampoco explica bien una enfermedad de origen mayormente viral o inmunomediado.

**Para avanzar se necesita:**
- Evidencia clínica o preclínica directa en queratoconjuntivitis epitelial punctata; sin ella no debería avanzar.
- Datos del mecanismo de acción y del texto de indicación aprobada, desde DrugBank y el prospecto de la AEMPS.
- Información de seguridad del prospecto (advertencias, contraindicaciones e interacciones), que hoy bloquea el cribado de seguridad.
- Para la indicación alternativa de conjuntivitis (Proceed with Guardrails): confirmar la indicación en la ficha técnica vigente, limitar el análisis a etiología bacteriana y formulaciones tópicas, y considerar la combinación con polimixina B y los patrones locales de resistencia.
- Verificar la compatibilidad de vía, ya que las autorizaciones españolas son orales y la evidencia es tópica oftálmica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


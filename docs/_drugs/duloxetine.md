---
layout: default
title: Duloxetine
parent: Solo predicción del modelo (L5)
nav_order: 186
evidence_level: L5
indication_count: 10
---

# Duloxetine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Duloxetina: De Trastorno Depresivo Mayor a Tortícolis Paroxística Benigna de la Infancia

## Resumen en Una Frase

La duloxetina es un inhibidor de la recaptación de serotonina y noradrenalina (IRSN), utilizado originalmente para el trastorno depresivo mayor y el trastorno de ansiedad generalizada.
El modelo TxGNN predice que podría ser efectiva para la **tortícolis paroxística benigna de la infancia**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno depresivo mayor y trastorno de ansiedad generalizada (según los datos farmacológicos; los textos de indicación de las autorizaciones de AEMPS vienen vacíos) |
| Nueva Indicación Predicha | Tortícolis paroxística benigna de la infancia |
| Puntaje de Predicción TxGNN | 99,85 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados de mecanismo de acción en DrugBank. Los datos farmacológicos disponibles indican que la duloxetina actúa sobre el transportador de serotonina (SERT) y el de noradrenalina (NET). También interactúa con los receptores 5-HT2A, 5-HT2C y 5-HT6. Este perfil corresponde a su uso en depresión, ansiedad y dolor crónico.

La tortícolis paroxística benigna de la infancia es un trastorno autolimitado, considerado un equivalente migrañoso infantil. La única conexión plausible es indirecta: los IRSN tienen un apoyo débil en la profilaxis de la migraña del adulto. No hay un vínculo mecanístico directo. La condición se resuelve espontáneamente y no existen datos de seguridad de la duloxetina en lactantes.

El puntaje alto de TxGNN (99,85 %) es solo una predicción del modelo. No está respaldado por estudios reales, por lo que debe interpretarse con mucha cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Otras Indicaciones Predichas con Evidencia

Otras predicciones del mismo modelo sí tienen datos, y son más prometedoras que la principal:

| Indicación | Puntaje TxGNN | Nivel de Evidencia | Comentario |
|------|------|------|------|
| Trastorno obsesivo-compulsivo | 99,84 % | L2 | Ensayo de Fase 4 completado ([NCT00464698](https://clinicaltrials.gov/study/NCT00464698), n=20). Estudio abierto ([PMID 25637377](https://pubmed.ncbi.nlm.nih.gov/25637377/)). ECA doble ciego de aumento en TOC resistente ([PMID 27811556](https://pubmed.ncbi.nlm.nih.gov/27811556/)). Las muestras son pequeñas y no hay confirmación en Fase 3. |
| Agorafobia | 99,84 % | L4 | La evidencia corresponde a trastorno de pánico y ansiedad generalizada, no a agorafobia en sí (p. ej. [PMID 19228176](https://pubmed.ncbi.nlm.nih.gov/19228176/), estudio abierto). |

Las demás predicciones (trastornos de personalidad histriónico, paranoide, esquizoide y esquizotípico; síndrome de Ohdo y variantes; conjuntivitis leñosa) tienen nivel L5. No tienen vínculo mecanístico plausible y probablemente son artefactos del grafo de conocimiento.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 82593 | DULOTEX 30 MG COMPRIMIDOS GASTRORRESISTENTES | Comprimido gastrorresistente |
| 3400930020609 | XERISTAR 30 MG CÁPSULAS DURAS GASTRORRESISTENTES EFG | Cápsula dura gastrorresistente |
| 04296006 | CYMBALTA 30 MG CÁPSULAS DURAS GASTRORRESISTENTES | Cápsula gastrorresistente |
| 04296002IP2 | CYMBALTA 60 MG CÁPSULAS DURAS GASTRORRESISTENTES | Cápsula dura gastrorresistente |
| 79731 | DULOXETINA PHARMAKERN 30 MG CÁPSULAS DURAS GASTRORRESISTENTES EFG | Cápsula dura gastrorresistente |

Se muestran 5 de las 20 autorizaciones. Los datos recibidos no incluyen el texto de indicación aprobada.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Las contraindicaciones y advertencias principales no están disponibles en los datos recibidos. La consulta de interacciones solo devolvió dianas farmacológicas (SERT, NET, 5-HT2A, 5-HT2C, 5-HT6, ZC3H14), no interacciones con otros fármacos. Además, no existen datos de seguridad de la duloxetina en lactantes, que es la población de la indicación predicha.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción solo cuenta con el puntaje del modelo, sin ensayos ni literatura (L5). No hay un vínculo mecanístico directo. La condición es autolimitada y afecta a lactantes, para quienes no hay datos de seguridad de la duloxetina.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones).
- Consultar el mecanismo de acción en DrugBank.
- Priorizar la evaluación del trastorno obsesivo-compulsivo (L2), que tiene evidencia directa, en lugar de esta indicación.
- Aportar cualquier dato clínico o preclínico específico de esta indicación antes de reconsiderar la decisión.

*Los resultados de este informe son solo de referencia para la investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


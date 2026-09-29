---
layout: default
title: Selpercatinib
parent: Solo predicción del modelo (L5)
nav_order: 488
evidence_level: L5
indication_count: 3
---

# Selpercatinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Selpercatinib: De Tumores con Alteraciones de RET a Hipertensión Pulmonar

## Resumen en Una Frase

Selpercatinib es un inhibidor selectivo de la quinasa RET, comercializado en España como Retsevmo. La literatura aportada lo sitúa en cáncer de pulmón no microcítico con fusión de RET y carcinoma medular de tiroides; los datos de autorización no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar**, pero actualmente hay **0 ensayos clínicos** y **3 publicaciones**, ninguna de ellas sobre esta enfermedad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de las 4 autorizaciones están vacíos) |
| Nueva Indicación Predicha | Hipertensión pulmonar |
| Puntaje de Predicción TxGNN | 99.18% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, selpercatinib es un inhibidor selectivo de la quinasa RET, y la literatura aportada describe su uso en tumores con alteraciones de RET. Con los datos suministrados no se puede evaluar más a fondo la plausibilidad mecanística.

No se ha documentado un vínculo entre RET y la remodelación vascular pulmonar. El puntaje alto de TxGNN (0.992) proviene solo de la proximidad en el grafo de conocimiento, no de estudios reales. Además, la hipertensión sistémica es un efecto adverso conocido del fármaco, lo que no respalda un beneficio en hipertensión pulmonar.

En conjunto, esta predicción debe considerarse una hipótesis sin respaldo experimental o clínico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Ninguna publicación aborda la hipertensión pulmonar. Son estudios sobre el fármaco en su contexto oncológico o de seguridad.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Cohorte retrospectiva | Ther Adv Med Oncol | Análisis retrospectivo (SIREN) de pacientes con CPNM con fusión de RET tratados con selpercatinib en un programa de acceso. Evalúa su eficacia en la práctica real. |
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Estudio de farmacovigilancia | Front Pharmacol | Compara los eventos adversos de pralsetinib y selpercatinib con datos reales del sistema FAERS. |
| [41918669](https://pubmed.ncbi.nlm.nih.gov/41918669/) | 2026 | Reporte de caso | Cureus | Carcinoma medular de tiroides metastásico en MEN 2B con mutación RET M918T. Describe los retos del tratamiento dirigido a largo plazo. |

---

## Información de Mercado en España

Los datos de autorización no incluyen el texto de la indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1201527016 | RETSEVMO 80 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 1201527001 | RETSEVMO 40 mg cápsulas duras | Cápsula dura |
| 1201527002 | RETSEVMO 80 mg cápsulas duras | Cápsula dura |
| 1201527013 | RETSEVMO 40 mg comprimidos recubiertos con película | Comprimido recubierto con película |

Titular: Eli Lilly Nederland B.V.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor selectivo de quinasa RET), no citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura sobre hipertensión pulmonar. La hipertensión sistémica como efecto adverso conocido va en contra de un posible beneficio. Las otras dos predicciones (migraña y migraña con aura de tronco encefálico, ambas L5 y también Hold) tampoco tienen evidencia y no son independientes entre sí.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (indicaciones, advertencias y contraindicaciones), ya que es un bloqueo para el cribado de seguridad.
- Obtener el mecanismo de acción desde DrugBank.
- Buscar evidencia preclínica que relacione la vía RET con la vasculopatía pulmonar.
- Evaluar el perfil cardiovascular del fármaco, en especial la hipertensión, antes de considerar cualquier estudio en esta población.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


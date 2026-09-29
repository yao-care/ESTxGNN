---
layout: default
title: Lenvatinib
parent: Solo predicción del modelo (L5)
nav_order: 311
evidence_level: L5
indication_count: 10
---

# Lenvatinib
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

# Lenvatinib: Hacia Liposarcoma

## Resumen en Una Frase

Lenvatinib es un inhibidor multiquinasa (VEGFR/FGFR) comercializado en España como Lenvima y Kisplyx. El registro disponible no incluye el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **liposarcoma**, con **1 ensayo clínico** completado (fase Ib/II, un solo brazo, 30 pacientes) y **4 publicaciones**, de las cuales solo una es clínica prospectiva.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.51% |
| Nivel de Evidencia | L2 (con reservas: el único estudio clínico es de un solo brazo, no aleatorizado) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, lenvatinib inhibe múltiples quinasas, entre ellas VEGFR y FGFR, y por esa vía puede reducir la angiogénesis tumoral. Esa lógica puede aplicarse a los sarcomas de tejidos blandos, que dependen de la formación de vasos sanguíneos.

El respaldo clínico procede del estudio LEADER (fase Ib/II, un solo brazo). En él, lenvatinib se combinó con eribulina, un quimioterápico que actúa durante la mitosis, en sarcoma adipocítico (liposarcoma) y leiomiosarcoma avanzados. Además, la literatura preclínica sugiere que eribulina se combina bien con otros antineoplásicos, y que la biología de CDK4 está ligada al liposarcoma.

La evidencia no permite confirmar eficacia. El estudio no fue aleatorizado, no tiene comparador y es pequeño. El caso clínico de liposarcoma desdiferenciado con metástasis pulmonar es solo anecdótico. Se necesita evidencia aleatorizada antes de cualquier recomendación.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03526679](https://clinicaltrials.gov/study/NCT03526679) | Fase 1/2 | Completado | 30 | Estudio LEADER, de un solo brazo. Evalúa la seguridad y eficacia de lenvatinib más eribulina en sarcoma adipocítico y leiomiosarcoma inoperables o metastásicos. Evidencia directa del fármaco en la enfermedad, pero no aleatorizada y pequeña. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36129471](https://pubmed.ncbi.nlm.nih.gov/36129471/) | 2022 | Ensayo fase Ib/II de un solo brazo | Clin Cancer Res | Resultados del estudio LEADER (NCT03526679): seguridad y eficacia de lenvatinib más eribulina en liposarcoma y leiomiosarcoma avanzados, una población con pocas opciones de tratamiento. |
| [39103896](https://pubmed.ncbi.nlm.nih.gov/39103896/) | 2024 | Preclínico/biomarcador | Exp Hematol Oncol | CDK4 como biomarcador pronóstico en sarcoma de tejidos blandos, con efecto sinérgico de su inhibición en liposarcoma desdiferenciado. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclínico | Anticancer Res | Actividad antitumoral preclínica de amplio espectro de eribulina en combinación con agentes de distinto mecanismo. |
| [34326745](https://pubmed.ncbi.nlm.nih.gov/34326745/) | 2021 | Reporte de caso | Case Rep Oncol | Reducción notable del tumor en un paciente con liposarcoma desdiferenciado y metástasis pulmonar, con tratamiento individualizado (dirigido, cirugía y quimioterapia). |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 1151002001 | LENVIMA 4 MG CAPSULAS DURAS | Cápsula dura | Eisai GmbH |
| 1151002002 | LENVIMA 10 MG CAPSULAS DURAS | Cápsula dura | Eisai GmbH |
| 1161128001 | KISPLYX 4 MG CAPSULAS DURAS | Cápsula dura | Eisai GmbH |
| 1161128002 | KISPLYX 10 MG CAPSULAS DURAS | Cápsula dura | Eisai GmbH |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor multiquinasa). Cuando se combina con eribulina, esta aporta un componente citotóxico convencional. |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Presión arterial, proteinuria y función hepática. Ajustar la dosis en insuficiencia renal o diálisis. |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción del modelo es muy alta (99.51%), pero la evidencia clínica se limita a un estudio de fase Ib/II de un solo brazo con 30 pacientes, sin comparador. El resto de las publicaciones son preclínicas o un caso aislado, por lo que por ahora es una pregunta de investigación y no una recomendación de uso.

**Para avanzar se necesita:**
- Un ensayo aleatorizado que compare lenvatinib más eribulina con el tratamiento estándar en liposarcoma.
- Las indicaciones aprobadas y los datos de seguridad (advertencias, contraindicaciones) del prospecto de AEMPS.
- Los datos detallados del mecanismo de acción (MOA) desde DrugBank.
- La confirmación de cuánto se aplican los datos a los distintos subtipos de liposarcoma.

Como nota aparte, para carcinoma renal (predicción n.º 7) la evidencia es L1, con ensayos de fase 3 como CLEAR. Parece un uso ya establecido más que un reposicionamiento, y conviene confirmarlo con la ficha técnica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


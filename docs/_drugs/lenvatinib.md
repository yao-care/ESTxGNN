---
layout: default
title: Lenvatinib
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 10
---

# Lenvatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Usando conocimiento de dominio en reposicionamiento de fármacos para redactar el informe (tarea de generación de contenido, no requiere skill de código).

# LENVATINIB: De Cáncer de Tiroides a Liposarcoma

## Resumen en Una Frase

Lenvatinib es un inhibidor multiquinasa (VEGFR1-3, FGFR1-4, PDGFRα, KIT, RET) utilizado internacionalmente en cáncer diferenciado de tiroides, carcinoma hepatocelular y carcinoma de células renales.
El modelo TxGNN predice que podría ser efectivo para **Liposarcoma**,
con **1 ensayo clínico** y **4 publicaciones** que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de tiroides, carcinoma hepatocelular, carcinoma de células renales (indicaciones aprobadas a nivel internacional; sin datos de autorización específicos en España en este Evidence Pack) |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.51% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Lenvatinib actúa como inhibidor multiquinasa dirigido principalmente contra VEGFR1-3, FGFR1-4, PDGFRα, KIT y RET, es decir, un fármaco fundamentalmente antiangiogénico. Los liposarcomas, en particular el subtipo desdiferenciado, presentan con frecuencia dependencia de la angiogénesis tumoral y activación de las vías VEGFR/FGFR/PDGFR, lo que ofrece una base mecanística razonable para el uso de un antiangiogénico en este contexto.

Esta hipótesis ya cuenta con validación clínica directa: el estudio LEADER (NCT03526679) combinó lenvatinib con eribulina —un inhibidor de microtúbulos ya aprobado para liposarcoma— en sarcoma adipocítico y leiomiosarcoma avanzados, con la lógica de que el efecto antiangiogénico de lenvatinib potencia el efecto citotóxico de eribulina sobre la mitosis celular. Los resultados publicados (Chen et al., 2022) respaldan la seguridad y eficacia de esta combinación en un contexto de opciones terapéuticas limitadas.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03526679](https://clinicaltrials.gov/study/NCT03526679) | Fase 1b/2 | Completado | 30 | Estudio de un solo brazo que evalúa seguridad y eficacia de lenvatinib (antiangiogénico) combinado con eribulina (quimioterapia antimitótica) en sarcoma adipocítico y leiomiosarcoma inoperables o metastásicos |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36129471](https://pubmed.ncbi.nlm.nih.gov/36129471/) | 2022 | Ensayo Fase 1b/2 | Clinical Cancer Research | Publicación principal del estudio LEADER: seguridad y eficacia de lenvatinib + eribulina en liposarcoma y leiomiosarcoma avanzados |
| [39103896](https://pubmed.ncbi.nlm.nih.gov/39103896/) | 2024 | Cohorte | Experimental Hematology & Oncology | CDK4 como biomarcador pronóstico en sarcoma de tejidos blandos y efecto sinérgico de su inhibición en el tratamiento secuencial del liposarcoma desdiferenciado |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclínico | Anticancer Research | Actividad antitumoral preclínica de amplio espectro de eribulina en combinación con agentes de mecanismo distinto |
| [34326745](https://pubmed.ncbi.nlm.nih.gov/34326745/) | 2021 | Reporte de Caso | Case Reports in Oncology | Reducción notable del tamaño tumoral en liposarcoma desdiferenciado con metástasis pulmonar mediante tratamiento individualizado |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor multiquinasa antiangiogénico: VEGFR1-3, FGFR1-4, PDGFRα, KIT, RET) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia actual se limita a un único ensayo Fase 1b/2 de un solo brazo (n=30) y 4 publicaciones, sin ensayos aleatorizados que confirmen el beneficio en liposarcoma. Aunque el mecanismo antiangiogénico es plausible y los resultados preliminares son alentadores, el nivel de evidencia (L2) y la ausencia de comercialización en España no justifican avanzar más allá de la fase de investigación.

**Para avanzar se necesita:**
- Datos del prospecto/TFDA-AEMPS sobre advertencias, contraindicaciones e interacciones (actualmente bloqueante según Data Gap DG001)
- Confirmación del mecanismo de acción mediante ficha técnica de DrugBank (DG002)
- Ensayos aleatorizados o de mayor tamaño muestral en liposarcoma específicamente (no solo sarcoma adipocítico agrupado)
- Evaluación de vía de administración y disponibilidad de formulación para el mercado español
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


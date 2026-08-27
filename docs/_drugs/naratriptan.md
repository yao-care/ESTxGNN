---
layout: default
title: Naratriptan
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 3
---

# Naratriptan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Naratriptán: De Migraña a Migraña con Aura del Tronco Encefálico

## Resumen en Una Frase

Naratriptán es un agonista selectivo de los receptores 5-HT1B/1D (clase triptán), utilizado habitualmente para el tratamiento agudo de la migraña. El modelo TxGNN predice que podría ser efectivo para **Migraña con Aura del Tronco Encefálico**, pero actualmente **no hay ensayos clínicos** dirigidos específicamente a este subtipo y las **19 publicaciones** recuperadas tratan sobre naratriptán y migraña en general, sin abordar directamente esta variante.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Migraña (tratamiento agudo, uso general de la clase triptán) |
| Nueva Indicación Predicha | Migraña con Aura del Tronco Encefálico |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados detallados sobre el mecanismo de acción (DrugBank no devolvió esta información). Según lo conocido públicamente, naratriptán es un agonista selectivo de los receptores serotoninérgicos 5-HT1B/1D (clase triptán), cuya eficacia en el tratamiento agudo de la migraña común está ampliamente documentada frente a sumatriptán y placebo.

La migraña con aura del tronco encefálico (antes llamada "migraña basilar") es un subtipo específico de migraña, por lo que a nivel de mecanismo el modelo TxGNN encuentra una asociación muy fuerte (puntaje 99.98%) con la migraña en general. Sin embargo, esta cercanía mecanicista es precisamente lo que genera una señal de seguridad importante: los triptanes se han considerado tradicionalmente **contraindicados o de uso relativo** en la migraña con aura del tronco encefálico, debido al riesgo teórico de vasoconstricción vertebrobasilar. Es decir, la predicción es razonable desde el punto de vista mecanístico, pero el problema no es de eficacia sino de **seguridad**: el mismo mecanismo que trata la migraña común podría ser riesgoso en este subtipo concreto.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados específicamente para naratriptán en migraña con aura del tronco encefálico.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10972634](https://pubmed.ncbi.nlm.nih.gov/10972634/) | 2000 | ECA | Clinical Therapeutics | Comparación cruzada, doble ciego, de naratriptán vs. sumatriptán en pacientes con recurrencia frecuente de migraña |
| [10961768](https://pubmed.ncbi.nlm.nih.gov/10961768/) | 2000 | ECA | Cephalalgia | Naratriptán administrado durante el pródromo para prevenir la crisis de migraña |
| [11264684](https://pubmed.ncbi.nlm.nih.gov/11264684/) | 2001 | ECA | Headache | Naratriptán 1 mg y 2.5 mg dos veces al día vs. placebo como profilaxis corta de la migraña menstrual |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Revisión/Guía | Headache | Evaluación actualizada de la American Headache Society sobre farmacoterapias para migraña aguda |
| [27910087](https://pubmed.ncbi.nlm.nih.gov/27910087/) | 2017 | Revisión | Headache | Revisión de opciones de tratamiento para la migraña menstrual |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohorte/Comparativo | Neurology | Eficacia reducida de sumatriptán en migraña con aura vs. sin aura (relevante para diferencias de respuesta según subtipo de aura) |
| [22337860](https://pubmed.ncbi.nlm.nih.gov/22337860/) | 2013 | Revisión | Cephalalgia | Revisión sobre la fase premonitoria de la migraña y su manejo |
| [25100506](https://pubmed.ncbi.nlm.nih.gov/25100506/) | 2014 | Revisión | Expert Opinion on Pharmacotherapy | Revisión actualizada sobre causas hormonales, profilaxis y tratamiento de la migraña menstrual |
| [17578540](https://pubmed.ncbi.nlm.nih.gov/17578540/) | 2007 | Estudio abierto/tolerabilidad | Headache | Tolerabilidad a largo plazo de naratriptán en uso intermitente como profilaxis de migraña menstrual |
| [14511276](https://pubmed.ncbi.nlm.nih.gov/14511276/) | 2003 | Reporte de caso | Headache | Manejo de migraña intratable con naratriptán |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad específica (no disponible en esta evaluación: advertencias, contraindicaciones e interacciones farmacológicas quedaron como vacío/no encontrado en las fuentes consultadas). No obstante, cabe reiterar la señal mecanística ya descrita: los triptanes se consideran clásicamente contraindicados o de uso cauteloso en la migraña con aura del tronco encefálico por riesgo teórico de vasoconstricción vertebrobasilar.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje de predicción de TxGNN es muy alto, la nueva indicación corresponde a un subtipo de migraña en el que la propia clase farmacológica (triptanes) tiene una señal de seguridad reconocida (riesgo vasoconstrictivo vertebrobasilar), no existen ensayos clínicos dirigidos a esta indicación específica, y falta información regulatoria bloqueante (仿單/禁忌) que impide siquiera completar la evaluación de seguridad inicial (S1).

**Para avanzar se necesita:**
- Obtener el prospecto/仿單 de TFDA con advertencias y contraindicaciones (DG001, bloqueante)
- Datos detallados del mecanismo de acción vía DrugBank (DG002)
- Evidencia clínica o de casos dirigida específicamente a migraña con aura del tronco encefálico (no solo migraña general)
- Datos de interacciones farmacológicas (DDI), actualmente no encontrados
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Artemether
parent: Evidencia alta (L1-L2)
nav_order: 66
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Artemether: nueva indicación predicha, Malaria por Plasmodium falciparum (nivel de evidencia L1). Indicación original: No disponible en los datos de la autorización (probablemente malaria…"
---

# Artemether
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
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

# Artemeter: De Indicación Original No Registrada a Malaria por *Plasmodium falciparum*

## Resumen en Una Frase

Artemeter es un antipalúdico derivado de la artemisinina, comercializado en España como RIAMET (combinado con lumefantrina), cuya indicación original no figura en los datos de la autorización.
El modelo TxGNN predice que podría ser efectivo para **malaria por Plasmodium falciparum**, con **30 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección. Se trata de un uso ya establecido, no de un reposicionamiento propiamente dicho.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de la autorización (probablemente malaria no complicada, según el uso conocido del producto) |
| Nueva Indicación Predicha | Malaria por *Plasmodium falciparum* |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Artemeter se convierte en el metabolito activo dihidroartemisinina. Su puente endoperóxido es activado por el hierro del grupo hemo dentro del parásito y genera radicales libres que dañan las proteínas parasitarias. Esto elimina rápidamente las formas asexuales sanguíneas de *Plasmodium*. Se combina con lumefantrina para cubrir las recrudescencias.

La información estructurada de mecanismo de acción no estaba disponible en los datos compilados; la descripción anterior se basa en el conocimiento farmacológico aceptado y en la justificación mecanística incluida en el análisis.

Hay que subrayar que la malaria por *P. falciparum* es un uso ya aprobado y consolidado, por lo que la predicción de TxGNN confirma una indicación existente más que proponer una nueva. Otras indicaciones con puntaje alto (por ejemplo, angioedema, escleroderma o conjuntivitis) carecen de ensayos, literatura y vínculo mecanístico identificable, por lo que quedan en espera (Hold).

---

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes (de 30 registrados para esta indicación).

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00422084](https://clinicaltrials.gov/study/NCT00422084) | Fase 3 | Completado | 1272 | Pironaridina-artesunato frente a artemeter-lumefantrina (Coartem), doble ciego, en niños y adultos con malaria no complicada |
| [NCT01082705](https://clinicaltrials.gov/study/NCT01082705) | Fase 3 | Completado | 323 | Eficacia de terapias combinadas con artemisinina en niños de 6-59 meses en Tanzania |
| [NCT00677833](https://clinicaltrials.gov/study/NCT00677833) | Fase 2/3 | Completado | 361 | Azitromicina + cloroquina frente a artemeter-lumefantrina (comparador) en niños africanos |
| [NCT02020330](https://clinicaltrials.gov/study/NCT02020330) | Fase 3 | Completado | 150 | Pauta de 3 días frente a 5 días de artemeter-lumefantrina en Myanmar |
| [NCT00529867](https://clinicaltrials.gov/study/NCT00529867) | Fase 4 | Completado | 267 | Suspensión frente a comprimidos de artemeter-lumefantrina en niños menores de 5 años en Kenia |
| [NCT03453840](https://clinicaltrials.gov/study/NCT03453840) | Fase 4 | Completado | 305 | Pauta prolongada en niños con VIH tratados con efavirenz; optimización de la dosis |
| [NCT01017770](https://clinicaltrials.gov/study/NCT01017770) | Fase 4 | Completado | 340 | Artemeter-lumefantrina frente a artesunato-amodiaquina en Burkina Faso |
| [NCT02637128](https://clinicaltrials.gov/study/NCT02637128) | Fase 4 | Completado | 452 | Eficacia in vivo de artemeter-lumefantrina y artesunato-amodiaquina en Malaui |
| [NCT01755559](https://clinicaltrials.gov/study/NCT01755559) | Fase 4 | Completado | 663 | Eficacia de tres terapias combinadas con artemisinina en niños de Maradi, Níger |
| [NCT05951595](https://clinicaltrials.gov/study/NCT05951595) | Fase 3 | En reclutamiento | 1680 | Triple combinación fija artemeter-lumefantrina-amodiaquina frente a terapias estándar |

Además, el estudio de fase 1 [NCT01103830](https://clinicaltrials.gov/study/NCT01103830) (n=287) comparó el efecto sobre el intervalo QT/QTc de Eurartesim frente a Riamet, lo que es relevante para la seguridad cardíaca.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31210357](https://pubmed.ncbi.nlm.nih.gov/31210357/) | 2019 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Artemeter intramuscular frente a quinina y artesunato en malaria grave |
| [25209020](https://pubmed.ncbi.nlm.nih.gov/25209020/) | 2014 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Versión anterior de la revisión sobre artemeter en malaria grave |
| [35271592](https://pubmed.ncbi.nlm.nih.gov/35271592/) | 2022 | Metaanálisis | PloS one | Eficacia terapéutica de artemeter-lumefantrina, artesunato-amodiaquina y dihidroartemisinina-piperaquina en África subsahariana |
| [33957925](https://pubmed.ncbi.nlm.nih.gov/33957925/) | 2021 | Revisión sistemática y metaanálisis | Malaria Journal | Eficacia y seguridad de artemeter-lumefantrina en Etiopía |
| [22548983](https://pubmed.ncbi.nlm.nih.gov/22548983/) | 2012 | Revisión sistemática | Malaria Journal | Seguridad y eficacia de artemeter-lumefantrina durante el embarazo |
| [34983552](https://pubmed.ncbi.nlm.nih.gov/34983552/) | 2022 | Revisión sistemática y metaanálisis de ECA | Malaria Journal | Seguridad comparada de dihidroartemisinina-piperaquina y artemeter-lumefantrina en niños africanos |
| [40845863](https://pubmed.ncbi.nlm.nih.gov/40845863/) | 2026 | ECA fase 4 | Lancet Infect Dis | Eficacia de cuatro terapias combinadas con artemisinina en niños de Uganda; posible pérdida de eficacia en África oriental |
| [1346408](https://pubmed.ncbi.nlm.nih.gov/1346408/) | 1992 | ECA | Lancet | Artemeter frente a cloroquina en malaria grave en niños gambianos |
| [40138574](https://pubmed.ncbi.nlm.nih.gov/40138574/) | 2025 | Estudio molecular/de resistencia | J Infect Dis | El tratamiento con artemeter-lumefantrina selecciona un mayor número de copias de pfmdr1 en África |
| [40660279](https://pubmed.ncbi.nlm.nih.gov/40660279/) | 2025 | Estudio de eficacia | Malaria Journal | Eficacia de cuatro terapias combinadas con artemisinina en Mozambique, 2022 |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 63764 | RIAMET 20 mg/120 mg COMPRIMIDOS (Novartis Farmacéutica S.A.) | Comprimido | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proceden del prospecto):** síndrome de QT largo, síndrome de QT largo familiar, torsades de pointes y déficit de potasio.
- **Interacciones farmacológicas:** se identificaron 95 interacciones; entre las 20 revisadas, las de gravedad **mayor** incluyen claritromicina, cobicistat, amprenavir, apalutamida, atazanavir y boceprevir. Entre las de gravedad **moderada** figuran dexametasona, miconazol, troglitazona, deferasirox, bosentán, bexaroteno y armodafinilo, entre otras.
- Se recomienda vigilar la prolongación del intervalo QT y revisar las interacciones, especialmente con antirretrovirales.

Para las advertencias y contraindicaciones del prospecto, consultar la ficha técnica de AEMPS.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen múltiples ensayos de fase 3 y 4 completados, además de revisiones sistemáticas, que respaldan la eficacia de artemeter (en combinación con lumefantrina) en la malaria por *P. falciparum*, por lo que la evidencia es de nivel L1. Al tratarse de un uso ya establecido, la cautela se centra en la seguridad y la resistencia, no en la eficacia.

**Para avanzar se necesita:**
- Obtener la ficha técnica de AEMPS (advertencias, contraindicaciones e indicación aprobada), cuyo análisis queda bloqueado para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Plan de vigilancia de la resistencia parcial a la artemisinina y de la selección de pfmdr1.
- Control del riesgo de QT y de interacciones (antirretrovirales, macrólidos, inductores e inhibidores del CYP3A4).
- Las demás indicaciones predichas (angioedema, angioedema hereditario, escleroderma, conjuntivitis, entre otras) permanecen en **Hold** por ausencia de evidencia y de vínculo mecanístico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


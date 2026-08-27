---
layout: default
title: Sofosbuvir
parent: 僅模型預測 (L5)
nav_order: 261
evidence_level: L5
indication_count: 8
---

# Sofosbuvir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Sofosbuvir: De Hepatitis C Crónica a Infección por el Virus de la Hepatitis B

## Resumen en Una Frase

Sofosbuvir es un antiviral de acción directa desarrollado originalmente para el tratamiento de la hepatitis C crónica (VHC).
El modelo TxGNN predice que también podría ser efectivo frente a la **infección por el virus de la hepatitis B (VHB)**,
con **50 ensayos clínicos** y **19 publicaciones** localizados en la búsqueda automatizada; sin embargo, al revisar el contenido
real de esos estudios, la gran mayoría corresponde en realidad a tratamiento de hepatitis C (incluida coinfección VHC/VHB), no a un efecto antiviral directo sobre el VHB.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hepatitis C crónica (uso farmacológico establecido; no hay ficha técnica española disponible en este informe) |
| Nueva Indicación Predicha | Infección por el virus de la hepatitis B (VHB) |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados y verificados sobre el mecanismo de acción (MOA) de sofosbuvir en esta base de datos (brecha de datos de severidad alta). Según la información farmacológica conocida, sofosbuvir es un profármaco nucleotídico que se activa a su forma trifosfato y actúa como inhibidor de la ARN polimerasa dependiente de ARN (RdRp) codificada por la proteína no estructural NS5B del virus de la hepatitis C, bloqueando así su replicación.

El VHC y el VHB son ambos virus hepatotropos que causan hepatitis viral crónica y frecuentemente coexisten en los mismos pacientes (coinfección VHC/VHB), lo que probablemente explica por qué el modelo TxGNN —que aprende asociaciones a partir de redes de conocimiento biomédico— vincula a sofosbuvir con el VHB: ambas enfermedades comparten población de pacientes, contexto clínico y numerosos ensayos conjuntos.

Sin embargo, desde el punto de vista mecanístico esta predicción es débil. El VHB es un virus de ADN parcialmente bicatenario que se replica mediante transcriptasa inversa, no mediante una ARN polimerasa dependiente de ARN; por tanto, el mecanismo de acción de sofosbuvir no tiene un blanco molecular directo en el ciclo replicativo del VHB. Al revisar en detalle los 50 ensayos clínicos y 19 artículos recuperados, la inmensa mayoría corresponde a tratamiento de la hepatitis C (incluyendo pacientes coinfectados con VHB) o a estudios sobre **reactivación** del VHB durante el tratamiento de la hepatitis C con antivirales de acción directa —no a ensayos que evalúen un efecto antiviral directo de sofosbuvir sobre el VHB—. Esto sugiere que la señal de TxGNN es, con alta probabilidad, un artefacto de similitud clínica entre dos hepatitis virales, más que una hipótesis mecanística sólida.

## Evidencia de Ensayos Clínicos

De los 50 ensayos recuperados por la búsqueda automatizada, solo 3 mencionan explícitamente al VHB en su diseño; el resto son ensayos de hepatitis C sin relación directa con VHB y se excluyeron de esta tabla.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Fase 2 | Completado | 21 | Único ensayo dirigido específicamente a pacientes con infección por VHB (ledipasvir/sofosbuvir, 12 semanas); evalúa reducción de HBsAg y ADN-VHB, sin garantía de cura funcional |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Fase 3 | Completado | 111 | LDV/SOF en coinfección VHC (genotipo 1/2) + VHB en Taiwán; el criterio de eficacia primario es la respuesta antiviral frente a VHC, no frente a VHB |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Fase 2/3 | Completado | 23 | Estudio sobre la reactivación del VHB durante el tratamiento antiviral directo del VHC en pacientes coinfectados VHC/VHB |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Fase 2 abierto | Journal of Medical Virology | LDV/SOF en monoinfección por VHB; el propio conjunto de evidencia señala que el estudio trata en realidad de VHD (hepatitis D), no de VHB puro — posible error de indexación |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Cohorte | Journal of Clinical Gastroenterology | Riesgo de reactivación de VHB en pacientes tratados con ledipasvir-sofosbuvir para VHC |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Reporte de caso | Medicine | Reactivación de VHB tras tratamiento exitoso de VHC con sofosbuvir + ribavirina |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | Cohorte | Infection and Drug Resistance | Manejo de la reactivación de VHB post-DAA en pacientes coinfectados VHC/VHB |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Observacional prospectivo | Journal of Viral Hepatitis | Reactivación de VHB en pacientes oncológicos que reciben DAA para VHC |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Reporte de caso | Journal of Medical Case Reports | Reactivación de VHB por variante de escape inmunológico durante tratamiento con sofosbuvir/velpatasvir para VHC |
| [27621502](https://pubmed.ncbi.nlm.nih.gov/27621502/) | 2015 | Farmacovigilancia | Hospital Pharmacy | Reactivación de VHB asociada al tratamiento de VHC con simeprevir y sofosbuvir |
| [37517414](https://pubmed.ncbi.nlm.nih.gov/37517414/) | 2023 | Modelización epidemiológica | Lancet Gastroenterology & Hepatology | Prevalencia global y cascada de atención del VHB (contexto epidemiológico; no evalúa sofosbuvir) |
| [26904396](https://pubmed.ncbi.nlm.nih.gov/26904396/) | 2016 | Revisión | Acta Pharmaceutica Sinica B | Revisión de antivirales de acción directa anti-VHC, contrasta su mecanismo con el de VHB/VIH |
| [39914746](https://pubmed.ncbi.nlm.nih.gov/39914746/) | 2025 | Análisis de tendencias | Journal of Hepatology | Lecciones del tratamiento de VHC aplicables al desarrollo de futuras terapias para VHB/VHD |

## Consideraciones de Seguridad

No se dispone de información de seguridad verificada para sofosbuvir en esta evaluación (advertencias, contraindicaciones e interacciones farmacológicas no fueron localizadas; la obtención del prospecto TFDA/AEMPS está marcada como brecha bloqueante para el análisis de seguridad). Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN para VHB no cuenta con respaldo mecanístico directo (VHB depende de transcriptasa inversa, no de la RdRp que inhibe sofosbuvir), y la evidencia clínica/bibliográfica recuperada refleja mayoritariamente tratamiento de hepatitis C o riesgo de reactivación de VHB durante dicho tratamiento, no un efecto antiviral directo sobre el VHB. La señal parece un artefacto derivado de la similitud clínica entre ambas hepatitis virales.

**Para avanzar se necesita:**
- Ensayos in vitro que evalúen directamente la actividad de sofosbuvir frente a la polimerasa/transcriptasa inversa del VHB
- Ficha técnica/prospecto de TFDA con advertencias y contraindicaciones (brecha bloqueante actual)
- Confirmación del mecanismo de acción vía DrugBank (brecha de alta severidad actual)
- Como alternativa de mayor potencial dentro de este mismo Evidence Pack, considerar priorizar la hipótesis de **hepatitis E (VHE)** (rank 2), que cuenta con evidencia mecanística in vitro más directa (inhibición de la RdRp del VHE) y un ensayo clínico específico ya completado (NCT03282474)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


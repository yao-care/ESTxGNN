---
layout: default
title: Sofosbuvir
parent: Evidencia alta (L1-L2)
nav_order: 741
evidence_level: L2
indication_count: 8
last_modified_at: 2026-10-28
monitor_inn: "SOFOSBUVIR"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis, viral, animal", "hepatitis A virus infection", "Omsk hemorrhagic fever", "chronic hepatitis B virus infection", "Kyasanur forest disease", "HIV infectious disease"]
description: "Sofosbuvir: nueva indicación predicha, Infección por el virus de la hepatitis B (hepatitis B virus infection) (nivel de evidencia L2). Indicación original: No consta en los datos locales"
---

# Sofosbuvir
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **8** 
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

## Sofosbuvir: Infección por el virus de la hepatitis B (hepatitis B virus infection)
{: .text-alpha }

## Resumen en Una Frase

Sofosbuvir es un antiviral de acción directa utilizado originalmente para el tratamiento de la infección crónica por el virus de la hepatitis C.
El modelo TxGNN predice que podría ser efectivo para la **infección por el virus de la hepatitis B**, con **10 ensayos clínicos** y **20 publicaciones** asociados. Sin embargo, la evidencia disponible no demuestra un beneficio terapéutico directo: los estudios se centran en la coinfección VHC/VHB y en el riesgo de reactivación del VHB.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Infección por el virus de la hepatitis B (hepatitis B virus infection) |
| Puntaje de Predicción TxGNN | 0.9977 |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold (pregunta de investigación; no avanzar a la fase clínica sin más datos) |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base consultada. Según la información conocida, sofosbuvir es un análogo nucleotídico que inhibe la ARN polimerasa dependiente de ARN NS5B del VHC. Su eficacia en la hepatitis C está bien establecida.

Mecanísticamente, la predicción es débil. El VHB se replica mediante una polimerasa con actividad de transcriptasa inversa dependiente de ADN, por lo que no se espera una acción antiviral directa de sofosbuvir. Los ensayos disponibles incluyen pacientes coinfectados VHC/VHB y monitorizan sobre todo la reactivación del VHB o la cinética del ADN-VHB durante el tratamiento del VHC. No demuestran que sofosbuvir trate el VHB por sí mismo.

La puntuación alta de TxGNN probablemente refleja la proximidad en la red de conocimiento con la hepatitis C (misma familia de hepatitis víricas y frecuente coinfección), más que una base mecanística real.

Un estudio de fase 2 abierto con ledipasvir/sofosbuvir en monoinfección por VHB (NCT03312023, publicado como PMID 36045503) sugiere una reducción modesta del HBsAg, pero es pequeño (n=21), sin grupo control, y el beneficio no está establecido. La combinación incluye ledipasvir, por lo que no puede atribuirse el efecto únicamente a sofosbuvir.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Fase 2 | Completado | 21 | Ledipasvir/sofosbuvir 12 semanas en infección por VHB; el ensayo más directamente relevante, pero de un solo brazo y pequeño |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Fase 2/3 | Completado | 23 | Antivirales de acción directa en coinfección VHC/VHB; se centra en la reactivación del VHB |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Fase 4 | Desconocido | 120 | Sofosbuvir/velpatasvir con TAF profiláctico en coinfección VHC/VHB; el agente activo frente al VHB es TAF |
| [NCT03186313](https://clinicaltrials.gov/study/NCT03186313) | Fase 3 | Completado | 72 | Combinación a dosis fija de sofosbuvir y daclatasvir en VHC genotipo 4; relevancia para VHB incierta |
| [NCT02483156](https://clinicaltrials.gov/study/NCT02483156) | Fase 2/3 | Completado | 80 | Sofosbuvir más ribavirina en VHC genotipo 4; resultados específicos de VHB poco claros |
| [NCT03549312](https://clinicaltrials.gov/study/NCT03549312) | Fase 4 | Desconocido | 25 | Cambio de tratamiento antirretroviral y terapia del VHC en coinfección VIH-VHC; el componente activo frente al VHB es TAF |
| [NCT02363517](https://clinicaltrials.gov/study/NCT02363517) | Fase 3 | Desconocido | 420 | Tratamiento del VHC en personas que se inyectan drogas; sin relevancia para el VHB |
| [NCT02768961](https://clinicaltrials.gov/study/NCT02768961) | Fase 4 | Completado | 64 | Cribado y tratamiento del VHC en prisiones; estudio de implementación |
| [NCT03579576](https://clinicaltrials.gov/study/NCT03579576) | N/A | Completado | 803 | Modelo simplificado de tratamiento del VHC en Myanmar; sin señal de eficacia en VHB |
| [NCT03261349](https://clinicaltrials.gov/study/NCT03261349) | Fase 2 | Desconocido | 21 | Ledipasvir/sofosbuvir en linfoma no Hodgkin de células B asociado a VHC; relevancia para VHB poco clara |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Ensayo fase 2 abierto | J Med Virol | Ledipasvir/sofosbuvir 12 semanas en monoinfección por VHB; evalúa el descenso de HBsAg y ADN-VHB |
| [35268497](https://pubmed.ncbi.nlm.nih.gov/35268497/) | 2022 | Cohorte | J Clin Med | Cinética diferente de ADN-VHB y HBsAg en pacientes coinfectados VHC durante tratamiento con antivirales de acción directa |
| [42558970](https://pubmed.ncbi.nlm.nih.gov/42558970/) | 2026 | Estudio multicéntrico | J Clin Transl Hepatol | Seguridad y eficacia de sofosbuvir/velpatasvir con pretratamiento con TAF en coinfección VHB/VHC, sobre reactivación del VHB |
| [26967675](https://pubmed.ncbi.nlm.nih.gov/26967675/) | 2016 | Revisión | J Clin Virol | Reactivación del VHB durante el tratamiento del VHC con antivirales de acción directa |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Revisión | Minerva Gastroenterol Dietol | Antivirales para hepatitis B y C y su efecto sobre la función renal |
| [42145438](https://pubmed.ncbi.nlm.nih.gov/42145438/) | 2026 | Revisión comparativa | Bioinformation | Comparación de antivirales en hepatitis B y C crónicas |
| [25253190](https://pubmed.ncbi.nlm.nih.gov/25253190/) | 2014 | Revisión | Minerva Pediatr | Tratamiento de hepatitis B y C en niños |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Revisión | World J Gastroenterol | Avances y retos en hepatitis vírica pediátrica |
| [27621502](https://pubmed.ncbi.nlm.nih.gov/27621502/) | 2015 | Reporte de caso | Hosp Pharm | Reactivación de hepatitis B con simeprevir y sofosbuvir para hepatitis C |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Reporte de caso | J Med Case Rep | Reactivación del VHB con mutante de escape inmunitario durante sofosbuvir/velpatasvir |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 113894001 | SOVALDI 400mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (8 interacciones identificadas):
  - **Mayores**: apalutamida, enzalutamida, lorlatinib
  - **Moderadas**: fostamatinib, warfarina, dicumarol, encorafenib
  - **Menores**: ciclosporina
- **Riesgo de reactivación del VHB**: la literatura recoge casos de reactivación del VHB en pacientes coinfectados que reciben antivirales de acción directa para el VHC. Esto representa una cuestión de seguridad y monitorización, no un beneficio terapéutico.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque la puntuación de TxGNN es muy alta y existe un ensayo de fase 2 en VHB, la evidencia es pequeña, de un solo brazo y confundida por ledipasvir. No hay una base mecanística para una acción directa contra el VHB, y los datos de coinfección apuntan más a un riesgo de reactivación que a un beneficio. Entre las indicaciones predichas, la infección por el virus de la hepatitis E tiene un mecanismo más plausible (inhibición in vitro y un ensayo de fase 2), aunque los resultados clínicos son mixtos.

**Para avanzar se necesita:**
- Revisión del prospecto de la AEMPS (advertencias y contraindicaciones), cuya ausencia en los datos compilados impide el cribado de seguridad
- Datos del mecanismo de acción desde DrugBank
- Estudios controlados en monoinfección por VHB que aíslen el efecto de sofosbuvir
- Plan de monitorización del VHB (HBsAg, ADN-VHB, transaminasas) en pacientes coinfectados que reciban sofosbuvir
- Evaluar si conviene priorizar otras indicaciones predichas con mejor respaldo mecanístico
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


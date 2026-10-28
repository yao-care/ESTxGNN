---
layout: default
title: Grazoprevir
parent: Evidencia alta (L1-L2)
nav_order: 386
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-28
description: "Grazoprevir: nueva indicación predicha, Infección por VIH (nivel de evidencia L5). Indicación original: Infección crónica por el virus de la hepatitis C (el texto de indicac…"
monitor_inn: "grazoprevir"
predicted_indications: ["HIV infectious disease", "hepatitis B virus infection", "hepatitis E virus infection", "hepatitis A virus infection", "hepatitis, viral, animal", "Omsk hemorrhagic fever", "Kyasanur forest disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Grazoprevir
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
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

## Grazoprevir: De Infección por Virus de la Hepatitis C a Infección por VIH
{: .text-alpha }

## Resumen en Una Frase

Grazoprevir es un inhibidor de la proteasa NS3/4A del VHC, utilizado originalmente para tratar la infección crónica por el virus de la hepatitis C (en combinación con elbasvir).
El modelo TxGNN predice que podría ser efectivo para **infección por VIH**, pero los **10 ensayos clínicos** y **20 publicaciones** asociados evalúan en realidad la curación de la hepatitis C en pacientes coinfectados con VIH, no actividad anti-VIH.
Se trata, por tanto, de una señal del modelo más que de un reposicionamiento real.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección crónica por el virus de la hepatitis C (el texto de indicación autorizada no está disponible en los datos compilados) |
| Nueva Indicación Predicha | Infección por VIH |
| Puntaje de Predicción TxGNN | 0.9973 |
| Nivel de Evidencia | L1 según el recuento formal de ensayos de Fase 3 (ver nota abajo); en la práctica, evidencia nula para eficacia anti-VIH |
| Estado de Mercado en España | Autorizado pero no comercializado (registros: 1) |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

> **Nota sobre el nivel de evidencia:** existen varios ECA de Fase 3 completados, pero todos tienen como criterio de valoración la respuesta virológica frente al VHC. Por ello, el nivel L1 sobrestima el respaldo real para la indicación de VIH.

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, grazoprevir es un inhibidor de la proteasa serínica NS3/4A del VHC, se utiliza en combinación fija con elbasvir (inhibidor de NS5A), y su eficacia en la hepatitis C crónica está bien establecida.

La relación entre ambas indicaciones es principalmente epidemiológica. El alto puntaje de TxGNN proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni una actividad antiviral demostrada contra el VIH.

Mecanísticamente, la plausibilidad es baja: la proteasa del VIH es una aspartil proteasa, estructural y funcionalmente distinta de la serín proteasa NS3/4A del VHC. No hay datos que muestren que grazoprevir inhiba la proteasa o la replicación del VIH. La evidencia respalda el uso del fármaco en su indicación original (VHC) en población con VIH.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02105662](https://clinicaltrials.gov/study/NCT02105662) | Fase 3 | Completado | 218 | Grazoprevir + elbasvir en pacientes sin tratamiento previo coinfectados VIH/VHC; criterio principal: RVS12 (respuesta VHC) |
| [NCT02897596](https://clinicaltrials.gov/study/NCT02897596) | Fase 3 | Desconocido | 62 | Tratamiento de 8 o 12 semanas en hepatitis C crónica temprana en coinfectados VIH/VHC |
| [NCT02600325](https://clinicaltrials.gov/study/NCT02600325) | Fase 3 | Completado | 80 | Hepatitis C aguda genotipo 1/4 en pacientes con VIH (estudio DAHHS-2) |
| [NCT02785666](https://clinicaltrials.gov/study/NCT02785666) | Fase 3 | Completado | 150 | Estrategia de tratar, asesorar y curar en HSH coinfectados VIH/VHC (Swiss HCVree) |
| [NCT02252016](https://clinicaltrials.gov/study/NCT02252016) | Fase 3 | Completado | 159 | GZR/EBR frente a placebo en VHC con trastornos sanguíneos hereditarios, con y sin coinfección por VIH |
| [NCT03098121](https://clinicaltrials.gov/study/NCT03098121) | Fase 4 | Completado | 40 | Eficacia y tolerabilidad en coinfectados VIH/VHC con experiencia previa a peginterferón/ribavirina |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Fase 4 | Completado | 87 | Riesgo cardiovascular tras erradicar el VHC en pacientes con y sin VIH |
| [NCT04048850](https://clinicaltrials.gov/study/NCT04048850) | N/A | Completado | 25 | Cohorte de tratamiento del VHC con Zepatier en personas con consumo de sustancias, con y sin VIH |
| [NCT03407703](https://clinicaltrials.gov/study/NCT03407703) | N/A | Desconocido | 50 | Efecto de la curación del VHC sobre la función renal, con y sin VIH |
| [NCT02057003](https://clinicaltrials.gov/study/NCT02057003) | N/A | Desconocido | 1000 | Cohorte HEPAVIR: eficacia y tolerabilidad de antivirales de acción directa en coinfectados VIH/VHC |

Ninguno de estos ensayos tiene como objetivo la eficacia contra el VIH.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26423374](https://pubmed.ncbi.nlm.nih.gov/26423374/) | 2015 | Ensayo no aleatorizado, abierto | The Lancet HIV | C-EDGE CO-INFECTION: eficacia y seguridad de grazoprevir + elbasvir en coinfección VHC/VIH (respuesta frente al VHC) |
| [32246857](https://pubmed.ncbi.nlm.nih.gov/32246857/) | 2020 | Revisión sistemática y metaanálisis en red | J Gastroenterol Hepatol | Comparación de eficacia y seguridad de regímenes de antivirales de acción directa en coinfección VHC/VIH |
| [28689442](https://pubmed.ncbi.nlm.nih.gov/28689442/) | 2017 | Revisión | Expert Opin Drug Metab Toxicol | Interacciones entre antivirales de acción directa y antirretrovirales en pacientes con VIH |
| [30745392](https://pubmed.ncbi.nlm.nih.gov/30745392/) | 2019 | Fase 1 (voluntarios sanos) | Antimicrob Agents Chemother | Interacciones farmacocinéticas de elbasvir/grazoprevir con inhibidores de la proteasa del VIH (ritonavir, atazanavir, lopinavir, darunavir) |
| [30541077](https://pubmed.ncbi.nlm.nih.gov/30541077/) | 2019 | Estudio de interacciones | J Antimicrob Chemother | Potencial de interacción con los inhibidores de integrasa raltegravir y dolutegravir |
| [32910788](https://pubmed.ncbi.nlm.nih.gov/32910788/) | 2020 | Estudio de cohorte | Antiviral Therapy | Eficacia de elbasvir/grazoprevir en VHC genotipo 1 con o sin VIH; mejoría de rigidez hepática y esteatosis |
| [28417245](https://pubmed.ncbi.nlm.nih.gov/28417245/) | 2017 | Revisión | Drugs | Revisión de elbasvir/grazoprevir en VHC genotipos 1 y 4 |
| [27603877](https://pubmed.ncbi.nlm.nih.gov/27603877/) | 2016 | Revisión | Expert Rev Clin Pharmacol | Mecanismo, farmacocinética, usos clínicos, seguridad y eficacia de elbasvir/grazoprevir |
| [29427481](https://pubmed.ncbi.nlm.nih.gov/29427481/) | 2018 | Revisión | Liver Int | Resultados en práctica real de antivirales de acción directa de segunda generación, incluidos coinfectados |
| [37731164](https://pubmed.ncbi.nlm.nih.gov/37731164/) | 2023 | Revisión | Clin Pharmacokinet | Mecanismos e importancia clínica de interacciones farmacocinéticas de antivirales de acción directa frente al VHC |

La literatura se centra en el VHC y en las interacciones con antirretrovirales; no aporta datos de actividad anti-VIH.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1161119001 | ZEPATIER 50MG/100MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible en los datos compilados (titular: Merck Sharp & Dohme B.V.) |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 53 interacciones en total. Las de nivel **Mayor** incluyen: claritromicina, dexametasona, eluxadolina, ácido obeticólico, rosuvastatina, simvastatina, cobicistat, eltrombopag y artesunato. Entre las de nivel **Moderado** figuran: aprepitant, cimetidina, clotrimazol, miconazol, troglitazona, deferasirox, ticagrelor, ivacaftor, zafirlukast, cloranfenicol y eritromicina.
- Para pacientes con VIH, la carga de interacciones con antirretrovirales (por ejemplo, regímenes potenciados con cobicistat o ritonavir) es una consideración relevante y debe revisarse caso por caso.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque existen varios ensayos de Fase 3 completados, todos evalúan la curación del VHC en pacientes coinfectados con VIH, no tratamiento del VIH. No hay base mecanística (proteasa serínica del VHC frente a aspartil proteasa del VIH) ni datos que respalden actividad anti-VIH; el alto puntaje de TxGNN parece reflejar la proximidad en la red de conocimiento.

**Para avanzar se necesita:**
- Datos de actividad in vitro de grazoprevir frente a la replicación o la proteasa del VIH
- Datos detallados del mecanismo de acción (MOA)
- Información completa del prospecto de AEMPS (advertencias, contraindicaciones e indicación autorizada)
- Revisión del manejo de interacciones con antirretrovirales en población coinfectada
- Considerar que su valor real en población con VIH es el tratamiento de la hepatitis C (indicación ya existente), no un reposicionamiento
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Velpatasvir
parent: Evidencia moderada (L3-L4)
nav_order: 841
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Velpatasvir: nueva indicación predicha, Infección por el virus de la hepatitis B (nivel de evidencia L3). Indicación original: Infección crónica por el virus de la hepatitis C (según el grafo de c…"
monitor_inn: "velpatasvir"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis A virus infection", "hepatitis, viral, animal", "Omsk hemorrhagic fever", "Kyasanur forest disease", "HIV infectious disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Velpatasvir
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **10** 
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

## Velpatasvir: De Infección por el Virus de la Hepatitis C a Infección por el Virus de la Hepatitis B
{: .text-alpha }

## Resumen en Una Frase

Velpatasvir es un inhibidor de la proteína NS5A del virus de la hepatitis C (VHC), utilizado originalmente para tratar la infección crónica por este virus, habitualmente en combinación con sofosbuvir.
El modelo TxGNN predice que podría ser efectivo para **infección por el virus de la hepatitis B**, pero la evidencia directa es muy limitada: solo **5 ensayos clínicos** asociados (uno con relevancia directa, de fase 4 y estado desconocido) y **20 publicaciones** que tratan casi exclusivamente la hepatitis C o la coinfección VHB/VHC.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección crónica por el virus de la hepatitis C (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Infección por el virus de la hepatitis B |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, velpatasvir es un inhibidor de la NS5A del VHC, su eficacia en hepatitis C está bien comprobada y se comercializa en combinación con sofosbuvir (Epclusa) y con sofosbuvir y voxilaprevir (Vosevi).

Mecanísticamente, el vínculo con la hepatitis B es débil. El VHB es un virus de ADN que se replica mediante transcripción inversa y no tiene un homólogo de NS5A, por lo que velpatasvir no tiene actividad anti-VHB establecida. La puntuación alta del modelo probablemente refleja anotaciones compartidas entre enfermedades hepáticas virales y no una relación mecanística real.

El contexto clínicamente relevante es la coinfección VHB/VHC y la reactivación del VHB durante el tratamiento con antivirales de acción directa. En estos casos se usan fármacos activos frente al VHB (como tenofovir alafenamida, TAF) junto con sofosbuvir/velpatasvir como profilaxis. Se trata de gestión de riesgo, no de eficacia anti-VHB directa de velpatasvir.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Fase 4 | Desconocido | 120 | SOF/VEL 12 semanas con TAF profiláctico en coinfección VHC/VHB en China; cualquier beneficio anti-VHB se atribuiría a TAF, no a velpatasvir |
| [NCT03579576](https://clinicaltrials.gov/study/NCT03579576) | N/A | Completado | 803 | Estrategia simplificada de tratamiento del VHC integrada con el VIH en Myanmar; sin datos de eficacia frente al VHB |
| [NCT03549312](https://clinicaltrials.gov/study/NCT03549312) | Fase 4 | Desconocido | 25 | Cambio de régimen antirretroviral seguido de SOF/VEL en coinfección VIH-VHC; no evalúa velpatasvir para VHB |
| [NCT02836925](https://clinicaltrials.gov/study/NCT02836925) | Fase 2 | Completado | 40 | Actividad antiviral en linfomas B indolentes asociados al VHC; relevancia limitada para VHB |
| [NCT07560046](https://clinicaltrials.gov/study/NCT07560046) | Fase 4 | Aún sin reclutar | 1280 | Ensayo aleatorizado por conglomerados de diagnóstico y tratamiento del VHC en el punto de atención; sin datos sobre VHB |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Reporte de caso | J Med Case Reports | Reactivación del VHB por una variante de escape del HBsAg durante el tratamiento con sofosbuvir/velpatasvir en un paciente anti-HBc positivo |
| [32935438](https://pubmed.ncbi.nlm.nih.gov/32935438/) | 2021 | No clasificado | J Viral Hepat | Estrategia simplificada para VHC en Myanmar; los coinfectados con VHB recibieron tenofovir de forma concurrente |
| [39735164](https://pubmed.ncbi.nlm.nih.gov/39735164/) | 2024 | No clasificado | J Virus Eradication | Estudio en práctica real de SOF/VEL en China, incluyendo pacientes con coinfección VHC/VHB |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Revisión | World J Gastroenterol | Avances y retos en hepatitis viral pediátrica; el tratamiento del VHB sigue lejos de ser curativo |
| [35248213](https://pubmed.ncbi.nlm.nih.gov/35248213/) | 2022 | Cohorte (estudio de un solo brazo) | Lancet Gastroenterol Hepatol | Seguridad y eficacia de SOF/VEL en VHC genotipo 4 en Ruanda |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Revisión | Eur J Gen Pract | Diagnóstico y tratamiento de la hepatitis C crónica en atención primaria |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Revisión | Clin Pharmacokinet | Consideraciones farmacocinéticas y farmacodinámicas de los tratamientos del VHC |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Revisión | Semin Liver Dis | Retratamiento de pacientes con VHC tras fracaso de antivirales de acción directa |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Revisión | AIDS Rev | Informe de la Conferencia Internacional sobre Hepatitis Viral 2017 |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | No clasificado | Klin Mikrobiol Infekc Lek | Evaluación retrospectiva del tratamiento antiviral de hepatitis B y C en niños en Ostrava |

Ninguna publicación demuestra eficacia de velpatasvir frente al VHB.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1161116001 | EPCLUSA 400 mg/100 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 1161116003 | EPCLUSA 150 mg/37,5 mg granulado recubierto en sobre | Granulado recubierto | No disponible en los datos compilados |
| 1161116004 | EPCLUSA 200 mg/50 mg granulado recubierto en sobre | Granulado recubierto | No disponible en los datos compilados |
| 1171223001 | VOSEVI 400 mg/100 mg/100 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 1161116001IP | EPCLUSA 400 mg/100 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |

Hay 6 autorizaciones vigentes en total (la sexta, 1161116001IP1, corresponde también a Epclusa 400 mg/100 mg). Todas pertenecen a Gilead Sciences Ireland Unlimited Company.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 57 interacciones. Entre las principales:
  - **Mayores**: dexametasona y los inhibidores de la bomba de protones (omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol, rabeprazol).
  - **Moderadas**: antiácidos (hidróxido de aluminio, carbonato de calcio, magaldrato, carbonato, hidróxido y óxido de magnesio), antagonistas H2 (cimetidina, famotidina, nizatidina) y naldemedina.
  - **Menores**: fidaxomicina, naloxegol y prucaloprida.
- **Riesgo clínico relevante para esta predicción**: la literatura describe reactivación del VHB durante el tratamiento antiviral del VHC en pacientes con antecedentes de infección por VHB (reporte de caso). Conviene cribar el VHB antes de iniciar el tratamiento.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Velpatasvir carece de mecanismo plausible frente al VHB (virus de ADN sin diana NS5A), y los estudios asociados tratan la hepatitis C o la coinfección, donde el efecto anti-VHB proviene de otros fármacos como TAF. La puntuación alta de TxGNN parece reflejar similitud de anotaciones en el grafo y no una oportunidad real de reposicionamiento.

**Para avanzar se necesita:**
- Datos de actividad antiviral in vitro de velpatasvir frente al VHB (replicación, ADNccc, HBsAg).
- Datos detallados del mecanismo de acción.
- Resultados del estudio NCT04997564, para separar el efecto de velpatasvir del de TAF.
- Los textos de indicación y las advertencias y contraindicaciones del prospecto de la AEMPS.
- Un plan de cribado y monitorización del VHB (HBsAg, anti-HBc, ADN del VHB) en pacientes coinfectados que reciban antivirales de acción directa.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


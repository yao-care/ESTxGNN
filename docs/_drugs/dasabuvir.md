---
layout: default
title: Dasabuvir
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 5
---

# Dasabuvir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Dasabuvir: De Hepatitis C Crónica a Infección por el Virus de la Hepatitis B

## Resumen en Una Frase

Dasabuvir es el inhibidor no nucleósido de la polimerasa NS5B que forma parte del régimen antiviral de acción directa contra el virus de la hepatitis C (VHC) genotipo 1 (junto con ombitasvir/paritaprevir/ritonavir). El modelo TxGNN predice que podría ser efectivo para la **infección por el virus de la hepatitis B (VHB)**, con **14 ensayos clínicos** y **18 publicaciones** identificados, aunque el análisis mecanístico indica que esta asociación es probablemente un enlace espurio del modelo, sin base farmacológica real.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hepatitis C viral crónica, genotipo 1 (como componente del régimen ombitasvir/paritaprevir/ritonavir + dasabuvir) |
| Nueva Indicación Predicha | Infección por el virus de la hepatitis B |
| Puntaje de Predicción TxGNN | 99.37% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción (MOA) de dasabuvir en la fuente consultada (DrugBank). Según la información conocida a partir del contexto clínico disponible, dasabuvir es un inhibidor no nucleósido de la polimerasa NS5B (ARN polimerasa dependiente de ARN) del VHC, y actúa como componente del régimen "3D"/"PrOD" (paritaprevir/ritonavir + ombitasvir + dasabuvir), comercializado como Viekira Pak/Exviera para la hepatitis C crónica genotipo 1.

Sin embargo, el análisis mecanístico de esta predicción específica es desfavorable: el VHC es un virus de ARN que depende de su propia RdRp para replicarse, mientras que el VHB es un virus de ADN cuya replicación depende de una transcriptasa inversa (RT) estructural y funcionalmente distinta. No existe, por tanto, una base molecular directa que justifique la inhibición del VHB por dasabuvir.

La evidencia disponible en pacientes coinfectados VHC/VHB que reciben este régimen para tratar el VHC describe, de hecho, un riesgo de **reactivación** del VHB durante el tratamiento — es decir, una señal de seguridad, no de eficacia terapéutica contra el VHB. Esto sugiere que la predicción de TxGNN probablemente refleja una asociación semántica entre distintos tipos de "hepatitis viral" en el grafo de conocimiento, más que un mecanismo farmacológico real.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Fase 2/3 | Completado | 23 | Único ensayo con relación directa al VHB: evalúa incidencia y factores de reactivación del VHB durante tratamiento anti-VHC en pacientes coinfectados VHC/VHB (no es un ensayo de eficacia contra VHB) |
| [NCT02460133](https://clinicaltrials.gov/study/NCT02460133) | Fase 4 | Activo, no reclutando | 44 | Tasas de reinfección por VHC en población carcelaria tras cura con tratamiento DAA libre de interferón; sin relación directa con VHB |
| [NCT02851069](https://clinicaltrials.gov/study/NCT02851069) | N/A | Completado | 66 | Efectividad real-world de paritaprevir/r-ombitasvir ± dasabuvir en VHC crónico (Colombia); sin relación con VHB |
| [NCT01995071](https://clinicaltrials.gov/study/NCT01995071) | Fase 2 | Completado | 89 | Seguridad y actividad antiviral de ABT-493/ABT-530 en VHC genotipo 1; sin relación con VHB |
| [NCT01939197 (TURQUOISE-I)](https://clinicaltrials.gov/study/NCT01939197) | Fase 2/3 | Completado | 318 | Seguridad del régimen ombitasvir/paritaprevir/ritonavir ± dasabuvir en coinfección VHC/VIH-1; título vinculado por embedding, no aborda VHB |
| [NCT01464827](https://clinicaltrials.gov/study/NCT01464827) | Fase 2 | Completado | 580 | Actividad antiviral, seguridad y farmacocinética de ABT-450/r+ABT-267±ABT-333 en VHC genotipo 1; sin relación con VHB |
| [NCT02493855](https://clinicaltrials.gov/study/NCT02493855) | Fase 2 | Completado | 46 | Cinética de declive viral del VHC con dasabuvir + ribavirina en dosis variables; sin relación con VHB |
| [NCT02219477 (TURQUOISE-CPB)](https://clinicaltrials.gov/study/NCT02219477) | Fase 3 | Completado | 36 | Seguridad y eficacia del régimen en VHC genotipo 1/4 con cirrosis descompensada; sin relación con VHB |
| [NCT01782495 (CORAL-I)](https://clinicaltrials.gov/study/NCT01782495) | Fase 2 | Completado | 129 | Seguridad y eficacia en receptores de trasplante hepático/renal con VHC; sin relación con VHB |
| [NCT02194998 (C_ASCENT)](https://clinicaltrials.gov/study/NCT02194998) | Fase 2 | Terminado | 46 | Terapia libre de interferón en coinfección VIH/VHC; sin relación con VHB |

*Nota: de los 14 ensayos identificados por la búsqueda, prácticamente todos son estudios de VHC; solo NCT02555943 aborda al VHB, y lo hace como señal de seguridad (reactivación), no como indicación terapéutica.*

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29397016](https://pubmed.ncbi.nlm.nih.gov/29397016/) | 2018 | Cohorte | Journal of viral hepatitis | Riesgo de reactivación del VHB en pacientes coinfectados VHB+VHC con cirrosis compensada tratados con ombitasvir/paritaprevir/ritonavir + dasabuvir + ribavirina (cohorte nacional de 2070 pacientes) |
| [25529080](https://pubmed.ncbi.nlm.nih.gov/25529080/) | 2015 | Revisión | Liver International | Revisión general sobre la erradicación del VHC y la búsqueda de una cura para el VHB; no aporta evidencia directa de dasabuvir en VHB |
| [36515288](https://pubmed.ncbi.nlm.nih.gov/36515288/) | 2022 | Cohorte/Epidemiología | Voprosy virusologii | Prevalencia y características moleculares de VHB/VHC/VHD en personas VIH+ (región de Novosibirsk); sin relación con eficacia de dasabuvir |
| [28903508](https://pubmed.ncbi.nlm.nih.gov/28903508/) | 2017 | Cohorte | Clinical Infectious Diseases | Efecto de regímenes PrOD (con/sin dasabuvir) y LDV/SOF sobre la supervivencia en pacientes con VHC (estudio ERCHIVES); sin relación con VHB |
| [28416221](https://pubmed.ncbi.nlm.nih.gov/28416221/) | 2017 | ECA fase 3b (VHC, no VHB) | Lancet Gastroenterology & Hepatology | Ensayo GARNET: eficacia de ombitasvir/paritaprevir/ritonavir + dasabuvir 8 semanas en VHC genotipo 1b sin cirrosis; no aborda VHB |
| [28762541](https://pubmed.ncbi.nlm.nih.gov/28762541/) | 2018 | Pendiente de clasificación | Journal of Gastroenterology and Hepatology | Efectividad y seguridad real-world de PrOD en pacientes con VHC genotipo 1b en Taiwán; sin relación con VHB |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | Pendiente de clasificación | Hepatology | Vías evolutivas de resistencia a inhibidores de proteasa del VHC; sin relación con VHB |
| [26043288](https://pubmed.ncbi.nlm.nih.gov/26043288/) | 2015 | Pendiente de clasificación | Reviews in Medical Virology | Desarrollo acelerado de antivirales de acción directa para el VHC; sin relación con VHB |
| [28992878](https://pubmed.ncbi.nlm.nih.gov/28992878/) | 2017 | Pendiente de clasificación | Hepatobiliary & Pancreatic Diseases International | Uso de peginterferón alfa-2a para VHC en la era de los DAA; sin relación con VHB |
| [26139639](https://pubmed.ncbi.nlm.nih.gov/26139639/) | 2015 | Pendiente de clasificación | The Annals of Pharmacotherapy | Consideraciones de tratamiento del VHC genotipo 1 en poblaciones especiales; sin relación con VHB |

---

## Información de Mercado en España

Dasabuvir **no está comercializado en España** (0 autorizaciones registradas ante AEMPS a la fecha de corte de datos).

---

## Consideraciones de Seguridad

No hay datos estructurados de advertencias, contraindicaciones ni interacciones farmacológicas disponibles en las fuentes consultadas (TFDA/AEMPS, DDI). Consultar el prospecto para información de seguridad.

⚠ La ausencia de datos de advertencias/contraindicaciones del prospecto (TFDA) está señalada como brecha de datos de severidad **bloqueante** para la evaluación de seguridad inicial (S1).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN para infección por VHB carece de fundamento mecanístico plausible (VHC es un virus de ARN dependiente de RdRp; VHB es un virus de ADN dependiente de transcriptasa inversa), y la evidencia clínica real disponible en pacientes coinfectados apunta a un riesgo de reactivación del VHB, no a un efecto terapéutico. De los 5 candidatos generados por el modelo (VHB, VHE, VHA, hepatitis viral animal, fiebre hemorrágica de Omsk), todos reciben recomendación "Hold", y los 4 restantes tienen nivel de evidencia L5 (predicción del modelo sin respaldo real) o se basan en literatura no relacionada con la enfermedad predicha.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica de TFDA con advertencias y contraindicaciones (brecha bloqueante DG001)
- Documentar formalmente el mecanismo de acción (MOA) vía API de DrugBank (brecha alta DG002)
- Evidencia preclínica o in vitro específica de actividad de dasabuvir frente al VHB (no disponible actualmente)
- Reevaluación tras confirmar si la predicción es un artefacto de embedding antes de invertir en estudios adicionales
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


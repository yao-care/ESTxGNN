---
layout: default
title: Bupropion
parent: Solo predicción del modelo (L5)
nav_order: 126
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bupropion: nueva indicación predicha, Trastorno por déficit de atención e hiperactividad (TDAH) (nivel de evidencia L5). Indicación original: Depresión mayor y dependencia de nicotina (según las indi…"
monitor_inn: "bupropion"
predicted_indications: ["attention deficit-hyperactivity disorder", "attention deficit hyperactivity disorder, inattentive type", "faciodigitogenital syndrome", "specific developmental disorder", "chondromyxoid fibroma", "proximal 16p11.2 microdeletion syndrome", "hypervitaminosis", "benign paroxysmal torticollis of infancy", "trigeminal nerve neoplasm", "obsolete hypertelorism (disease)"]
---

# Bupropion
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

# Bupropión: De Trastornos Depresivos y Dependencia de Nicotina a Trastorno por Déficit de Atención e Hiperactividad

## Resumen en Una Frase

Bupropión es un antidepresivo inhibidor de la recaptación de noradrenalina y dopamina, utilizado originalmente para el tratamiento de la depresión mayor y la deshabituación tabáquica (dependencia de nicotina).
El modelo TxGNN predice que podría ser efectivo para el **trastorno por déficit de atención e hiperactividad (TDAH)**,
con **6 ensayos clínicos** (incluido un ensayo de Fase 3 completado) y **20 publicaciones** que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Depresión mayor y dependencia de nicotina (según las indicaciones originales del grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Trastorno por déficit de atención e hiperactividad (TDAH) |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L1 (según la clasificación de los datos compilados; ver nota en la sección de ensayos) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 16 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Bupropión inhibe la recaptación de noradrenalina y dopamina y carece de actividad serotoninérgica. Actualmente no se dispone de datos detallados del mecanismo de acción en los datos compilados para este informe, pero la literatura revisada describe este perfil farmacológico como su mecanismo principal.

El TDAH se asocia a disfunción noradrenérgica y dopaminérgica en varias regiones cerebrales. Los fármacos aprobados para el TDAH (metilfenidato, atomoxetina) actúan sobre las mismas vías catecolaminérgicas, por lo que bupropión ofrece una base mecanística plausible para mejorar la atención y el control de impulsos. Además, el TDAH coexiste con frecuencia con depresión y trastornos por uso de sustancias, poblaciones en las que bupropión ya se emplea.

Debe considerarse una opción de segunda línea o fuera de indicación (off-label), dado que los estimulantes siguen siendo el tratamiento de primera línea. Existe una revisión Cochrane específica sobre bupropión en TDAH adulto (PMID 28965364), aunque en los datos compilados no se dispone de su resumen de conclusiones.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00048360](https://clinicaltrials.gov/study/NCT00048360) | Fase 3 | Completado | 162 | Ensayo aleatorizado, doble ciego, controlado con placebo de bupropión de liberación prolongada (300-450 mg/día) en adultos con TDAH, 8 semanas |
| [NCT00936299](https://clinicaltrials.gov/study/NCT00936299) | Fase 4 | Completado | 105 | Bupropión para TDAH en adolescentes con trastorno por uso de sustancias |
| [NCT00061087](https://clinicaltrials.gov/study/NCT00061087) | Fase 2/3 | Completado | 115 | Tratamiento del TDAH adulto en pacientes en mantenimiento con metadona (el fármaco evaluado debe confirmarse) |
| [NCT01270555](https://clinicaltrials.gov/study/NCT01270555) | No aplica | Completado | 32 | Estudio abierto de bupropión SR en adultos con TDAH y trastornos por uso de sustancias recientes o actuales |
| [NCT00000268](https://clinicaltrials.gov/study/NCT00000268) | No aplica | Completado | 32 | Abuso de cocaína y trastorno por déficit de atención; aporte limitado al TDAH |
| [NCT04553263](https://clinicaltrials.gov/study/NCT04553263) | Fase 1 temprana | Retirado | 0 | Prevención de recaídas en trastorno por uso de estimulantes; sin participantes, no aporta evidencia |

**Nota sobre el nivel de evidencia:** el nivel L1 requiere al menos 2 ECA de Fase 3 completados. En los datos compilados solo figura un ensayo de Fase 3 completado (NCT00048360) más uno de Fase 2/3. Estrictamente, esto correspondería a L2; se mantiene L1 por ser la clasificación de los datos compilados, pero conviene verificarla.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28965364](https://pubmed.ncbi.nlm.nih.gov/28965364/) | 2017 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Bupropión para TDAH en adultos como alternativa a los psicoestimulantes |
| [30097390](https://pubmed.ncbi.nlm.nih.gov/30097390/) | 2018 | Revisión sistemática y metaanálisis en red | Lancet Psychiatry | Eficacia y tolerabilidad comparada de fármacos para el TDAH en niños, adolescentes y adultos |
| [33085721](https://pubmed.ncbi.nlm.nih.gov/33085721/) | 2020 | Revisión sistemática y metaanálisis en red | PLoS One | Comparación de tratamientos farmacológicos para el TDAH en adultos |
| [40203844](https://pubmed.ncbi.nlm.nih.gov/40203844/) | 2025 | Metaanálisis en red (seguridad) | Lancet Psychiatry | Seguridad cardiovascular comparada de los fármacos para el TDAH |
| [37405312](https://pubmed.ncbi.nlm.nih.gov/37405312/) | 2023 | Revisión | Health Psychol Res | Efectos de bupropión en depresión, TDAH y deshabituación tabáquica; farmacocinética, farmacodinamia e interacciones |
| [38915262](https://pubmed.ncbi.nlm.nih.gov/38915262/) | 2024 | Revisión | Expert Rev Neurother | Fármacos no estimulantes para adultos con TDAH, cuando los estimulantes no se toleran o no responden |
| [39172673](https://pubmed.ncbi.nlm.nih.gov/39172673/) | 2024 | Revisión | Am Fam Physician | Abordaje del TDAH en adultos |
| [26601963](https://pubmed.ncbi.nlm.nih.gov/26601963/) | 2016 | Revisión | Curr Pharm Des | Efectos y efectos secundarios de los fármacos para el TDAH, incluido bupropión |
| [27738872](https://pubmed.ncbi.nlm.nih.gov/27738872/) | 2017 | Metaanálisis de tratamientos múltiples | Mol Neurobiol | Eficacia y seguridad de tratamientos del TDAH en niños y adolescentes |
| [24259638](https://pubmed.ncbi.nlm.nih.gov/24259638/) | 2014 | Revisión | Ann Pharmacother | Fisiopatología, etiología y tratamiento del TDAH |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 88040 | Bupropion Accord 150 mg | Comprimido de liberación modificada | No disponible |
| 81596 | Bupropion Cinfa 300 mg | Comprimido de liberación modificada | No disponible |
| 68615 | Elontril 150 mg | Comprimido de liberación modificada | No disponible |
| 63265 | Zyntabac 150 mg | Comprimido de liberación prolongada | No disponible |
| 114988001 | Mysimba 8 mg/90 mg | Comprimido de liberación prolongada | No disponible |

Se muestran 5 de las 16 autorizaciones vigentes (todas de principio activo único). Mysimba es una combinación con naltrexona, aunque figura registrada como producto único en los datos compilados.

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo según el grafo de conocimiento** (no proceden del prospecto): epilepsia, hipertensión, insuficiencia y enfermedad hepática, cirrosis, enfermedad renal, trastorno bipolar maníaco, trastornos psicóticos y esquizoafectivos, anorexia y bulimia nerviosa, dependencia de opiáceos y otras sustancias, infarto de miocardio, enfermedad de la vesícula biliar, hemoglobinopatía y neoplasias del sistema nervioso central.
- **Interacciones farmacológicas:** 665 interacciones registradas. Entre las de nivel mayor figuran fentanilo, lidocaína, codeína, dihidrocodeína, tramadol, metilfenidato, hidrocortisona, aldesleukina, alfentanilo y amantadina. Entre las de nivel moderado: etanol, alprazolam, cetirizina, nifedipino e hidroclorotiazida.
- **Precauciones específicas para TDAH** (según el razonamiento de reposicionamiento): descenso del umbral convulsivo y cautela en pacientes con trastornos por uso de sustancias o de la conducta alimentaria comórbidos.

No se dispone de las advertencias y contraindicaciones del prospecto de la AEMPS; consultar el prospecto para completar la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 3 controlado con placebo, uno de Fase 2/3, una revisión Cochrane y varios metaanálisis que respaldan un uso plausible en TDAH adulto, con base mecanística coherente. Sin embargo, es una opción de segunda línea, con riesgos relevantes (convulsiones, interacciones numerosas) y sin indicación autorizada en España.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones oficiales), una laguna crítica para el cribado de seguridad
- Confirmar los datos del mecanismo de acción en DrugBank
- Verificar el nivel de evidencia (L1 frente a L2) y los resultados del ensayo NCT00048360, así como el fármaco evaluado en NCT00061087
- Revisar las conclusiones de la revisión Cochrane y de los metaanálisis en red sobre eficacia frente a placebo y a estimulantes
- Definir un plan de monitorización para pacientes con epilepsia, trastornos alimentarios, hipertensión o trastornos por uso de sustancias, y para el uso concomitante de opioides y otros fármacos con interacción mayor
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


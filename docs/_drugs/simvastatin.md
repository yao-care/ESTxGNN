---
layout: default
title: Simvastatin
parent: Solo predicción del modelo (L5)
nav_order: 738
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-31
monitor_inn: "simvastatin"
predicted_indications: ["brain stem infarction", "cholesterol-ester transfer protein deficiency", "HIV infectious disease", "ABri amyloidosis", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
description: "Simvastatin: nueva indicación predicha, Brain stem infarction (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Simvastatin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Simvastatin: Brain stem infarction
{: .text-alpha }

## Resumen en Una Frase

Simvastatina es una estatina (inhibidor de la HMG-CoA reductasa) utilizada originalmente para tratar la hipertrigliceridemia, la hiperlipidemia y la prevención de enfermedades cerebrovasculares y arterioscleróticas.
El modelo TxGNN predice que podría ser efectiva para **hipercolesterolemia familiar**,
con **8 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección. Cabe señalar que esta indicación ya está cubierta por los usos originales (hipercolesterolemia familiar homocigota), por lo que se trata más de una confirmación que de un reposicionamiento propiamente dicho.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Brain stem infarction |
| Puntaje de Predicción TxGNN | 0.9941 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 13) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Simvastatina inhibe la HMG-CoA reductasa, lo que reduce la síntesis hepática de colesterol y aumenta la expresión de receptores de LDL, disminuyendo el colesterol LDL (LDL-C). Cabe indicar que los datos compilados para este informe no incluyen una descripción formal del mecanismo de acción; la explicación anterior corresponde al mecanismo farmacológico conocido de la clase.

La hipercolesterolemia familiar se caracteriza por un aclaramiento deficiente de LDL. Las indicaciones originales de simvastatina ya incluyen la hipercolesterolemia familiar homocigota, la hiperlipoproteinemia y la hiperlipidemia combinada familiar, de modo que la predicción es coherente con el uso establecido del fármaco.

En el caso de las formas heterocigotas, la simvastatina aumenta la expresión de receptores LDL a partir de los alelos funcionales restantes. Esto explica la amplia base de ensayos y revisiones disponibles.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Fase 3 | Completado | 720 | Ensayo ENHANCE: ezetimiba + simvastatina a dosis altas frente a simvastatina sola sobre la progresión de la aterosclerosis carotídea en hipercolesterolemia familiar heterocigota |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Fase 3 | Completado | 248 | Ezetimiba coadministrada con simvastatina en adolescentes (10-17 años) con hipercolesterolemia familiar heterocigota |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Fase 3 | Completado | 50 | Ezetimiba añadida a atorvastatina o simvastatina en hipercolesterolemia familiar homocigota (simvastatina como tratamiento de base) |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Fase 3 | Completado | 44 | Extensión abierta a largo plazo de seguridad de ezetimiba con atorvastatina o simvastatina en hipercolesterolemia familiar homocigota |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Fase 3 | Completado | 442 | Efectos renales de rosuvastatina y simvastatina en dislipidemia tipo IIa/IIb, incluida hipercolesterolemia familiar heterocigota (6 semanas, abierto) |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Fase 3 | Completado | 249 | Alirocumab frente a placebo en hipercolesterolemia familiar heterocigota (simvastatina solo como terapia de fondo posible) |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Fase 3 | Completado | 153 | Alirocumab en niños y adolescentes con hipercolesterolemia familiar heterocigota (no es un estudio de simvastatina) |
| [NCT01890967](https://clinicaltrials.gov/study/NCT01890967) | Fase 2 | Completado | 527 | Estudio de rango de dosis de LY3015014 en hipercolesterolemia primaria (no es un estudio de simvastatina) |

Solo dos ensayos (NCT00552097 y NCT00129402) tienen simvastatina como componente central del régimen; el resto la incluye como terapia de fondo o es de otros fármacos.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | ECA | N Engl J Med | Simvastatina con o sin ezetimiba en hipercolesterolemia familiar: efecto sobre la progresión de la aterosclerosis (ENHANCE) |
| [41824590](https://pubmed.ncbi.nlm.nih.gov/41824590/) | 2026 | Guía | J Am Coll Cardiol | Guía ACC/AHA 2026 sobre el manejo de la dislipidemia |
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Guía | Circulation | Guía ACC/AHA 2026 sobre el manejo de la dislipidemia (publicación paralela) |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Estatinas en niños con hipercolesterolemia familiar |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Revisión | Drug Safety | Beneficios y riesgos de simvastatina en hipercolesterolemia familiar |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Revisión | Expert Opin Drug Saf | Evaluación de beneficios y riesgos de simvastatina en hipercolesterolemia familiar |
| [18940534](https://pubmed.ncbi.nlm.nih.gov/18940534/) | 2008 | Estudio clínico | J Am Coll Cardiol | Eficacia y seguridad de ezetimiba más simvastatina en adolescentes con hipercolesterolemia familiar heterocigota |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guía | Endocr Pract | Guías AACE/ACE para el manejo de la dislipidemia y la prevención cardiovascular |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Estudio comparativo | Nutr Metab Cardiovasc Dis | Atorvastatina frente a simvastatina en hipercolesterolemia familiar heterocigota |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Estudio transversal | J Clin Med | Inmunidad celular en niños con hipercolesterolemia familiar tratados con simvastatina |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 65193 | Simvastatina Vir 20 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos compilados |
| 65199 | Simvastatina Normon 40 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos compilados |
| 64276 | Simvastatina Davur 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos compilados |
| 64249 | Simvastatina Tarbis 20 mg comprimidos EFG | Comprimido recubierto | No disponible en los datos compilados |
| 70230 | Simvastatina Cinfamed 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos compilados |

Hay 20 autorizaciones vigentes en total, todas de monofármaco y ninguna cancelada. Se muestran solo las 5 primeras.

---

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de precaución según el grafo de conocimiento (no es texto de prospecto):** enfermedad hepática, pancreatitis, miopatía y enfermedades musculares, rabdomiólisis, diabetes mellitus y cetoacidosis diabética, hiperglucemia, gota, enfermedad de la vesícula biliar, trombocitopenia, úlcera péptica, trastornos de la coagulación, hipotensión, síndrome coronario agudo, infarto de miocardio, enfermedad arterial coronaria, abuso de sustancias, entre otras.
- **Interacciones farmacológicas:** se registran 696 interacciones. Entre las de gravedad **mayor** figuran amiodarona, amlodipino y fenofibrato. Entre las moderadas: paclitaxel, nifedipino, omeprazol, aprepitant, etanol y zidovudina, entre otras.
- **Interacción con antirretrovirales:** los inhibidores de proteasa y los regímenes potenciados con cobicistat inhiben CYP3A4, elevan la exposición a simvastatina y aumentan el riesgo de miopatía y rabdomiólisis. Se prefiere evitar simvastatina en estos casos.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no figuran en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen varios ensayos de Fase 3 completados (incluido el ENHANCE, con 720 pacientes) y una amplia base de revisiones y guías que respaldan el uso de simvastatina en hipercolesterolemia familiar, lo que corresponde a un nivel de evidencia L1. Sin embargo, es una indicación ya cubierta por los usos originales, y las interacciones y el riesgo muscular exigen salvaguardas.

**Para avanzar se necesita:**
- Obtener el prospecto oficial de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas), actualmente ausente.
- Completar los datos del mecanismo de acción desde DrugBank.
- Definir un plan de monitoreo de seguridad (función hepática, CK/síntomas musculares) y reglas para interacciones, especialmente con amiodarona, amlodipino, fenofibrato y antirretrovirales.

---

### Otras predicciones (resumen)

| Indicación predicha | Puntaje TxGNN | Nivel de evidencia | Recomendación |
|------|------|------|------|
| Infarto del tronco encefálico | 0.9941 | L5 | Hold |
| Deficiencia de la proteína de transferencia de ésteres de colesterol | 0.9939 | L5 | Hold |
| Infección por VIH | 0.9922 | L3 | Research Question (el interés es la dislipidemia asociada a antirretrovirales; simvastatina suele evitarse por interacciones) |
| Amiloidosis ABri | 0.9913 | L5 | Hold |
| Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y reducción de sustancia blanca cortical | 0.9910 | L5 | Hold |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


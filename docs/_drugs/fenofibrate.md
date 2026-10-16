---
layout: default
title: Fenofibrate
parent: Evidencia moderada (L3-L4)
nav_order: 330
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-14
description: "Fenofibrate: nueva indicación predicha, Hipercolesterolemia familiar homocigota (nivel de evidencia L4). Indicación original: Hipertrigliceridemia e hiperlipidemia (según el grafo de conocimiento"
---

# Fenofibrate
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **7** 
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

# Fenofibrato: De Hipertrigliceridemia a Hipercolesterolemia Familiar Homocigota

## Resumen en Una Frase

Fenofibrato es un fármaco hipolipemiante, utilizado originalmente para tratar la hipertrigliceridemia y distintas formas de hiperlipidemia.
El modelo TxGNN predice que podría ser efectivo para la **hipercolesterolemia familiar homocigota**, pero los datos compilados para este informe no aportan ningún ensayo clínico con fenofibrato en esta enfermedad (el único ensayo vinculado estudia alirocumab) y la literatura es indirecta.
La predicción de mayor rango (rango 1) tiene por tanto un respaldo muy débil; la indicación con mejor evidencia entre las predichas es **hiperlipoproteinemia** (múltiples ensayos de Fase 3), aunque se solapa con el uso ya autorizado del fármaco.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertrigliceridemia e hiperlipidemia (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Hipercolesterolemia familiar homocigota |
| Puntaje de Predicción TxGNN | 99,91% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 15 |
| Decisión Recomendada | Hold |

**Otras indicaciones predichas (para contexto):**

| Indicación predicha | Puntaje TxGNN | Nivel de evidencia | Decisión |
|------|------|------|------|
| Hiperlipoproteinemia | 99,65% | L1 | Proceed with Guardrails |
| Hipercolesterolemia familiar | 99,62% | L3 | Pregunta de investigación |
| Deficiencia de proteína de transferencia de ésteres de colesterol | 99,61% | L4 | Hold |
| Hipercolesterolemia por deficiencia de colesterol 7α-hidroxilasa | 99,52% | L5 | Hold |
| Hiperlipidemia por deficiencia de lipasa hepática de triglicéridos | 99,42% | L3 | Pregunta de investigación |
| Hipercolesterolemia autosómica dominante | 99,05% | L3 | Pregunta de investigación |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información farmacológica conocida, fenofibrato es un agonista de PPAR-alfa (el receptor PPARα figura como diana). Esto aumenta la actividad de la lipoproteína lipasa y reduce la apoC-III, con lo que disminuyen las lipoproteínas ricas en triglicéridos y aumenta el HDL-C. Su eficacia en hipertrigliceridemia e hiperlipidemia mixta está bien establecida.

En la hipercolesterolemia familiar homocigota, el defecto de base es la disfunción del receptor de LDL, que la activación de PPAR-alfa no corrige. El efecto reductor de LDL-C esperable es, por tanto, pequeño. La única referencia específica con fenofibrato (PMID 6593751, 1984) es un estudio de cohorte pequeño en hiperlipoproteinemia tipo II, que incluyó a un paciente homocigoto con la mayor caída de colesterol. El puntaje alto del modelo parece reflejar más la cercanía en la red del metabolismo lipídico que una justificación terapéutica sólida.

En cambio, la predicción de **hiperlipoproteinemia** sí es coherente con el mecanismo (hiperlipidemia mixta con triglicéridos elevados), aunque no constituye un hallazgo novedoso de reposicionamiento, ya que solapa con el uso ya autorizado.

---

## Evidencia de Ensayos Clínicos

Para la indicación principal (hipercolesterolemia familiar homocigota):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Fase 3 | Completado | 18 | Alirocumab (no fenofibrato) en niños y adolescentes con HFHo; evalúa la reducción de LDL-C a las 12 semanas. No es evidencia directa del fármaco |

**Evidencia directa de fenofibrato en la indicación con mejor respaldo (hiperlipoproteinemia):**

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00349375](https://clinicaltrials.gov/study/NCT00349375) | Fase 3 | Completado | 1040 | Fenofibrato 145 mg + simvastatina vs. simvastatina en dislipidemia mixta |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Fase 3 | Completado | 576 | Coadministración de fenofibrato y ezetimiba en hiperlipidemia mixta |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Fase 3 | Completado | 587 | Fenofibrato y ezetimiba en hiperlipidemia mixta |
| [NCT00362934](https://clinicaltrials.gov/study/NCT00362934) | Fase 3 | Completado | 516 | Fenofibrato + simvastatina vs. atorvastatina en dislipidemia mixta |
| [NCT00459745](https://clinicaltrials.gov/study/NCT00459745) | Fase 3 | Completado | 481 | Pravastatina, fenofibrato o su combinación (Pravafen) en hiperlipidemia combinada |
| [NCT01956201](https://clinicaltrials.gov/study/NCT01956201) | Fase 3 | Desconocido | 476 | Fenofibrato añadido a atorvastatina vs. atorvastatina en hipercolesterolemia mixta |
| [NCT00352183](https://clinicaltrials.gov/study/NCT00352183) | Fase 3 | Completado | 450 | Fenofibrato 145 mg + simvastatina 40 mg vs. simvastatina 40 mg |
| [NCT00362206](https://clinicaltrials.gov/study/NCT00362206) | Fase 3 | Completado | 423 | Fenofibrato + simvastatina vs. pravastatina en dislipidemia mixta |
| [NCT01878227](https://clinicaltrials.gov/study/NCT01878227) | Fase 3 | Completado | 420 | Comparación directa de cápsula de coenzima A con fenofibrato en hiperlipidemia |
| [NCT00006412](https://clinicaltrials.gov/study/NCT00006412) | Fase 3 | Completado | 630 | Fenofibrato vs. pravastatina en pacientes con VIH y alteraciones lipídicas |

---

## Evidencia de Literatura

Para la indicación principal (hipercolesterolemia familiar homocigota), la literatura es mayormente indirecta:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Cohorte | Pharmacol Res Commun | 22 pacientes con hiperlipoproteinemia tipo II tratados con fenofibrato: colesterol total −22% y LDL-C −24%; en FH, −28% y −31%; un paciente con HFHo mostró la mayor caída |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Revisión | Indian Heart J | Fármacos hipolipemiantes no estatínicos; fenofibrato en monoterapia indicado sobre todo con triglicéridos >500 mg/dl |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Revisión | Ann N Y Acad Sci | Tratamiento de dislipidemias pediátricas; fenofibrato entre los fármacos que redujeron lípidos |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guía | Endocr Pract | Guías AACE/ACE sobre dislipidemia |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | Estudio farmacocinético | Pharmacotherapy | Interacciones farmacocinéticas de lomitapida con fármacos hipolipemiantes, incluido fenofibrato |

**Literatura relevante para hiperlipoproteinemia:**

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11942772](https://pubmed.ncbi.nlm.nih.gov/11942772/) | 2002 | ECA | Endocr Pract | Fenofibrato micronizado vs. gemfibrozilo en hiperlipoproteinemia tipos IIa/IIb (cruzado, doble ciego) |
| [2653622](https://pubmed.ncbi.nlm.nih.gov/2653622/) | 1989 | Estudio clínico | Cardiology | Estudio multicéntrico controlado con placebo en hiperlipoproteinemia tipo IV/V (147 pacientes) |
| [2226216](https://pubmed.ncbi.nlm.nih.gov/2226216/) | 1990 | Revisión | Drugs | Propiedades farmacodinámicas y uso terapéutico de fenofibrato en dislipidemia |

---

## Información de Mercado en España

Hay 15 autorizaciones vigentes (todas monofármaco); se muestran las 5 principales. Los textos de indicación aprobada no figuran en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 69367 | Fenofibrato Sun 160 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 63533 | Secalip Supra 160 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 72705 | Fenofibrato Teva 200 mg cápsulas duras EFG | Cápsula dura | No disponible |
| 79122 | Fenofibrato Kern Pharma 145 mg comprimidos EFG | Comprimido | No disponible |
| 56864 | Secalip 250 mg cápsulas duras de liberación prolongada | Cápsula dura de liberación prolongada | No disponible |

---

## Consideraciones de Seguridad

- **Contraindicaciones / enfermedades de riesgo (según el grafo de conocimiento, no el prospecto):** insuficiencia y enfermedad hepática, pancreatitis, enfermedad de la vesícula biliar y colelitiasis, miopatía y rabdomiólisis, insuficiencia renal, y alteraciones hematológicas (trombocitopenia, leucopenia, neutropenia, agranulocitosis, anemia).
- **Interacciones farmacológicas:** la consulta no identificó interacciones medicamentosas clínicas; solo registró dianas farmacológicas (PPARα humano y proteína de unión a ácidos grasos 1 de rata). Los ensayos y la literatura sugieren vigilar el riesgo de miopatía al combinar con estatinas.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold** (para hipercolesterolemia familiar homocigota)

**Justificación:**
No existe ningún ensayo con fenofibrato en HFHo, el mecanismo (activación de PPAR-alfa) no corrige el defecto del receptor de LDL y la única evidencia específica es un estudio de cohorte de 1984. Estatinas, ezetimiba, inhibidores de PCSK9 y lomitapida siguen siendo el estándar. La indicación mejor respaldada, hiperlipoproteinemia (L1, Proceed with Guardrails), se solapa con el uso ya autorizado y no es un reposicionamiento novedoso.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (DrugBank)
- Advertencias y contraindicaciones oficiales del prospecto de la AEMPS (bloqueante para el cribado de seguridad)
- Textos de indicación aprobada de las autorizaciones españolas
- Estudios clínicos de fenofibrato como adyuvante en hipercolesterolemia familiar, si se desea explorar esa línea
- Para hiperlipoproteinemia, plan de monitoreo de enzimas hepáticas, función renal y riesgo de miopatía en combinación con estatinas
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Cyclophosphamide
parent: Evidencia alta (L1-L2)
nav_order: 150
evidence_level: L2
indication_count: 5
---

# Cyclophosphamide
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **5** 
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

# Ciclofosfamida: De Indicación Original No Registrada a Leucemia Mieloide

## Resumen en Una Frase

La ciclofosfamida es un fármaco alquilante antineoplásico e inmunosupresor. El Evidence Pack no registra su indicación original, porque los textos de indicación de las autorizaciones españolas están vacíos.
El modelo TxGNN predice que podría ser efectiva para **leucemia mieloide**, con **50 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección.
Casi toda la evidencia corresponde a su papel en regímenes de acondicionamiento y en la profilaxis de la enfermedad injerto contra huésped (EICH) en el trasplante hematopoyético, no a su uso como agente único.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Leucemia mieloide |
| Puntaje de Predicción TxGNN | 99,47 % |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 9 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, la ciclofosfamida es un profármaco alquilante del ADN. Produce entrecruzamiento del ADN y apoptosis en células en proliferación, y además tiene un fuerte efecto linfodepletor.

Estas dos propiedades encajan con la leucemia mieloide. El efecto citotóxico ataca las células leucémicas en división. El efecto linfodepletor e inmunosupresor sustenta su uso en:

- Regímenes de acondicionamiento mieloablativo y no mieloablativo, como busulfán-ciclofosfamida (BuCy) y fludarabina-ciclofosfamida (Flu/Cy).
- Ciclofosfamida postrasplante (PTCy) para prevenir la EICH en trasplantes por leucemia mieloide aguda (LMA) o crónica (LMC).

Es decir, la predicción del modelo coincide con un uso que ya existe en la práctica clínica. Existen ensayos de Fase 3, pero los títulos disponibles no muestran que la ciclofosfamida sea la variable evaluada. Por eso no se asigna el nivel L1.

---

## Evidencia de Ensayos Clínicos

Se muestran 10 de los 50 ensayos registrados, priorizando los que incluyen ciclofosfamida de forma explícita.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01427881](https://clinicaltrials.gov/study/NCT01427881) | Fase 2 | Completado | 43 | Ciclofosfamida postrasplante para prevenir la EICH crónica tras trasplante alogénico en neoplasias hematológicas. Es la intervención directa. |
| [NCT05884333](https://clinicaltrials.gov/study/NCT05884333) | Fase 2 | Reclutando | 54 | Trasplante optimizado de sangre de cordón en neoplasias hematológicas de alto riesgo. La ciclofosfamida probablemente forma parte del acondicionamiento. |
| [NCT00002549](https://clinicaltrials.gov/study/NCT00002549) | Fase 3 | Desconocido | 1520 | Ensayo aleatorizado de inducción y consolidación seguida de trasplante en LMA (AML 10). No se confirma la ciclofosfamida como componente. |
| [NCT02461121](https://clinicaltrials.gov/study/NCT02461121) | Fase 3 | Completado | 156 | Microtrasplante HLA-incompatible frente a trasplante no mieloablativo HLA-idéntico en LMA de riesgo intermedio. El papel de la ciclofosfamida no está confirmado. |
| [NCT01621477](https://clinicaltrials.gov/study/NCT01621477) | Fase 2 | Terminado | 34 | Trasplante haploidéntico más células NK en neoplasias hematológicas en recaída. La eficacia es limitada por la terminación anticipada. |
| [NCT03467386](https://clinicaltrials.gov/study/NCT03467386) | Fase 1 | Suspendido | 56 | Irradiación total de médula y ganglios más PTCy en LMA en remisión completa. |
| [NCT03314974](https://clinicaltrials.gov/study/NCT03314974) | Fase 2 | Reclutando | 300 | Trasplante mieloablativo con profilaxis de EICH basada en PTCy, tacrolimus y micofenolato. |
| [NCT01177371](https://clinicaltrials.gov/study/NCT01177371) | Fase 2 | Completado | 13 | Busulfán y ciclofosfamida en dosis altas más trasplante de médula ósea alogénico en leucemia, síndromes mielodisplásicos, mieloma y linfoma. |
| [NCT00445744](https://clinicaltrials.gov/study/NCT00445744) | N/A | Completado | 52 | Ciclofosfamida seguida de busulfán intravenoso como acondicionamiento en mielofibrosis, LMA o síndrome mielodisplásico. |
| [NCT00049517](https://clinicaltrials.gov/study/NCT00049517) | Fase 3 | Completado | 657 | Intensificación de daunorrubicina antes del autotrasplante en LMA del adulto. No se confirma la ciclofosfamida como variable evaluada. |

---

## Evidencia de Literatura

Se muestran 10 de las 20 publicaciones. No hay ECA en el conjunto.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | Revisión sistemática y metaanálisis en red | Bone Marrow Transplant | Compara regímenes de acondicionamiento mieloablativo (como Bu/Cy) en adultos con LMA trasplantados en remisión completa. |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | Cohorte | Future Oncol | Busulfán-ciclofosfamida, régimen estándar de acondicionamiento, frente a fludarabina-busulfán, con eficacia similar y posiblemente menos toxicidad. |
| [25345651](https://pubmed.ncbi.nlm.nih.gov/25345651/) | 2015 | Cohorte | Am J Hematol | En 165 pacientes con LMA, el trasplante no mieloablativo Cy/Flu y el mieloablativo no difirieron en supervivencia en el análisis univariante. |
| [33325761](https://pubmed.ncbi.nlm.nih.gov/33325761/) | 2021 | Estudio observacional | Leuk Lymphoma | Ciclofosfamida en dosis altas (60 mg/kg) para citorreducción en LMA con hiperleucocitosis o leucostasis (27 pacientes). |
| [39939431](https://pubmed.ncbi.nlm.nih.gov/39939431/) | 2025 | Estudio observacional | Bone Marrow Transplant | 1823 pacientes con LMA trasplantados con PTCy. Analiza la intensidad del acondicionamiento según el riesgo citogenético y molecular. |
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | Cohorte | Haematologica | 217 pacientes con LMA en remisión completa, con acondicionamiento mieloablativo y PTCy. Supervivencia global a 2 años del 77 % y libre de eventos del 72 %. |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | Cohorte | Int J Mol Sci | PTCy tras trasplante de donante emparentado o no emparentado compatible en LMA pediátrica. |
| [38499049](https://pubmed.ncbi.nlm.nih.gov/38499049/) | 2024 | Cohorte | Transpl Immunol | Cladribina con busulfán y ciclofosfamida como acondicionamiento intensivo en LMA en recaída o refractaria. |
| [31628924](https://pubmed.ncbi.nlm.nih.gov/31628924/) | 2020 | Estudio observacional | Hematol Oncol Stem Cell Ther | Compara busulfán/ciclofosfamida con busulfán/fludarabina en LMA y síndrome mielodisplásico, con enfoque en calidad de vida. |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | Cohorte | Cytotherapy | Factores pronósticos del trasplante haploidéntico con PTCy en LMA. |

---

## Información de Mercado en España

Se muestran 5 de las 9 autorizaciones. Los datos disponibles no incluyen el texto de la indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 89859 | Ciclofosfamida Vivanta 1.000 mg polvo para solución inyectable y para perfusión EFG | Polvo para solución inyectable y para perfusión |
| 33411 | Genoxal 200 mg polvo para solución inyectable y para perfusión | Polvo para solución inyectable y para perfusión |
| 86296 | Ciclofosfamida Accord 1.000 mg polvo para solución inyectable y para perfusión EFG | Polvo para solución inyectable |
| 33214 | Genoxal 50 mg comprimidos recubiertos | Comprimido recubierto |
| 90200 | Ciclofosfamida Seacross 500 mg polvo para solución inyectable y para perfusión EFG | Polvo para solución inyectable y para perfusión |

---

## Citotoxicidad

Esta clasificación se basa en la categoría conocida del fármaco. El Evidence Pack no incluye datos de toxicidad de DrugBank.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (agente alquilante, clase mostaza nitrogenada) |
| Riesgo de Mielosupresión | Alto a dosis de acondicionamiento; moderado a dosis convencionales (leucopenia dependiente de la dosis) |
| Clasificación de Emetogenicidad | Moderada a alta, según la dosis |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, electrolitos, análisis de orina (riesgo de cistitis hemorrágica) |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La ciclofosfamida ya se usa en la práctica en el trasplante por leucemia mieloide, como acondicionamiento (BuCy, Flu/Cy) y como PTCy. Hay ensayos de Fase 2 completados y abundantes estudios observacionales. Sin embargo, la evidencia proviene de regímenes combinados, no hay ECA en la literatura recopilada y faltan los datos de seguridad de la ficha técnica española.

**Para avanzar se necesita:**
- Obtener del prospecto de la AEMPS las advertencias y contraindicaciones (brecha bloqueante en la revisión de seguridad).
- Completar los datos del mecanismo de acción consultando la API de DrugBank.
- Confirmar en los ensayos de Fase 3 si la ciclofosfamida forma parte del régimen evaluado, y así valorar un posible nivel L1.
- Aislar la contribución propia de la ciclofosfamida frente a otros componentes de los regímenes (busulfán, fludarabina, irradiación).
- Definir un plan de monitoreo hematológico, urológico y de manejo de citotóxicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


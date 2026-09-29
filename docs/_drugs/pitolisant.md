---
layout: default
title: Pitolisant
parent: Evidencia moderada (L3-L4)
nav_order: 429
evidence_level: L4
indication_count: 3
---

# Pitolisant
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

# Pitolisant: De Narcolepsia a Insomnio

## Resumen en Una Frase

Pitolisant es un antagonista/agonista inverso del receptor H3 de histamina, comercializado en Europa para la narcolepsia con o sin cataplejía (según la literatura del paquete de evidencia).
El modelo TxGNN predice que podría ser efectivo para **Insomnio**, pero la evidencia directa es nula: **1 ensayo clínico** (retirado, sobre otra indicación) y **8 publicaciones** indirectas.
El mecanismo del fármaco va en sentido opuesto a lo que requiere el tratamiento del insomnio, por lo que la predicción es poco creíble.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de AEMPS (los textos de indicación están vacíos). La literatura la describe como narcolepsia con o sin cataplejía |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99,71% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone del campo de mecanismo de acción en la ficha del fármaco. La literatura incluida lo describe como un agonista inverso selectivo del receptor H3 de histamina. Al bloquear este autorreceptor, aumenta la señalización histaminérgica que promueve la vigilia. Por eso se usa en la somnolencia diurna excesiva de la narcolepsia, y se ha estudiado en la somnolencia residual de la apnea obstructiva del sueño (AOS).

**Esta predicción es débil desde el punto de vista mecanístico.** Un fármaco que promueve la vigilia es lo contrario de lo que necesita el insomnio. Además, el insomnio figura como reacción adversa descrita de pitolisant. El puntaje alto (0,997) probablemente refleja la cercanía en el grafo de conocimiento con los trastornos de sueño-vigilia (narcolepsia, somnolencia diurna), y no una dirección terapéutica real.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02800083](https://clinicaltrials.gov/study/NCT02800083) | Fase 2 | Retirado | 0 | Ensayo multicéntrico, doble ciego y controlado con placebo de pitolisant en trastorno por consumo de alcohol. El insomnio no es su objetivo principal; el sueño aparece solo como parte de la salud mental en los objetivos secundarios. Sin participantes, no aporta datos |

---

## Evidencia de Literatura

Ninguna publicación evalúa pitolisant en insomnio. Los ECA son de narcolepsia y AOS (indirectos).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | ECA (Fase 3) | The Lancet Neurology | Seguridad y eficacia de pitolisant en niños de 6 años o más con narcolepsia, con o sin cataplejía (indirecto) |
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | ECA | Chest | Somnolencia diurna residual en pacientes con AOS adherentes a CPAP (indirecto) |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | ECA | Am J Respir Crit Care Med | Somnolencia diurna en pacientes con AOS moderada-grave que rechazan CPAP (indirecto) |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | Cohorte | Revista de Neurología | Estudio de vida real (WAKE) en narcolepsia tipo 1 no respondedora a tratamientos previos |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Revisión | Current Neuropharmacology | Cambios del sistema histaminérgico en trastornos neuropsiquiátricos; menciona pitolisant (somnolencia en narcolepsia) y doxepina (insomnio) |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Revisión | Drug Des Devel Ther | Perfil de pitolisant en el manejo de la narcolepsia |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Revisión | Handbook of Clinical Neurology | Receptores, agonistas y antagonistas de histamina en salud y enfermedad |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Revisión | Clinical Neuropharmacology | Pitolisant como estimulante alternativo en adolescentes con narcolepsia-cataplejía y somnolencia refractaria |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 1151068001 | WAKIX 4,5 mg comprimidos recubiertos con película | Comprimido recubierto con película | Bioprojet Pharma |
| 1151068002 | WAKIX 18 mg comprimidos recubiertos con película | Comprimido recubierto con película | Bioprojet Pharma |
| 1211546001 | OZAWADE 4,5 mg comprimidos recubiertos con película | Comprimido recubierto con película | Bioprojet Pharma |
| 1211546002 | OZAWADE 18 mg comprimidos recubiertos con película | Comprimido recubierto con película | Bioprojet Pharma |

---

## Consideraciones de Seguridad

- **Reacciones adversas relevantes**: el insomnio es una reacción adversa descrita de pitolisant, lo que contradice su uso como tratamiento del insomnio.
- No se encontraron interacciones farmacológicas registradas en la base consultada.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún estudio sobre insomnio, y el único ensayo registrado se retiró sin participantes y era de otra indicación. El mecanismo pro-vigilia va en contra de la indicación, y el insomnio es una reacción adversa conocida. El puntaje TxGNN alto parece un artefacto de proximidad en el grafo.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de AEMPS (advertencias y contraindicaciones), un vacío que bloquea el cribado de seguridad.
- Completar los datos de mecanismo de acción desde DrugBank.
- Evidencia directa en insomnio (preclínica o clínica) que justifique el sentido terapéutico. Sin ella, no hay base para avanzar.

**Otras predicciones del modelo (para referencia):**
- **TDAH** (99,36%, L4): hay una hipótesis biológica plausible (el bloqueo de H3 libera dopamina, noradrenalina y acetilcolina en la corteza prefrontal), pero solo con revisiones y datos preclínicos. Se clasifica como pregunta de investigación.
- **Síndrome faciodigitogenital** (99,29%, L5): sin vínculo mecanístico ni evidencia. Probable artefacto del grafo; se mantiene en Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


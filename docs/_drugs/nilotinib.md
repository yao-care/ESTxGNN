---
layout: default
title: Nilotinib
parent: Solo predicción del modelo (L5)
nav_order: 566
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-29
description: "Nilotinib: nueva indicación predicha, Dermatofibrosarcoma protuberans (nivel de evidencia L4). Indicación original: Leucemia mieloide crónica, BCR-ABL1 positivo"
monitor_inn: "NILOTINIB"
predicted_indications: ["dermatofibrosarcoma protuberans"]
---

# Nilotinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Nilotinib: De Leucemia Mieloide Crónica a Dermatofibrosarcoma Protuberans
{: .text-alpha }

## Resumen en Una Frase

Nilotinib es un inhibidor de tirosina quinasa originalmente utilizado para el tratamiento de la leucemia mieloide crónica con BCR-ABL1 positivo.
El modelo TxGNN predice que podría ser efectivo para **dermatofibrosarcoma protuberans (DFSP)**,
pero actualmente solo cuenta con **1 publicación** (una revisión) y **ningún ensayo clínico** registrado que respalde esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia mieloide crónica, BCR-ABL1 positivo |
| Nueva Indicación Predicha | Dermatofibrosarcoma protuberans |
| Puntaje de Predicción TxGNN | 0.9931 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 11 de 12) |
| Número de Autorizaciones | 12 (vigentes: 11) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, nilotinib es un inhibidor de tirosina quinasa dirigido a BCR-ABL, que además inhibe PDGFR (alfa/beta) y KIT. Su eficacia en la leucemia mieloide crónica BCR-ABL1 positiva es la base de su uso original.

El DFSP suele estar impulsado por la fusión COL1A1-PDGFB, que genera una activación autocrina constitutiva de PDGFRB. Por ello existe una justificación plausible a nivel de diana para los tumores dependientes de PDGFR. La misma lógica de inhibición de PDGFR sustenta el uso de imatinib, establecido en el DFSP irresecable o metastásico.

Es importante subrayar que este vínculo se apoya en la farmacología general de los inhibidores de quinasas y no en datos específicos aportados para este informe. El puntaje de 0.9931 es una predicción computacional y no constituye evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Revisión | Pharmacological Research | Revisión del papel de los inhibidores de molécula pequeña de PDGFR en el tratamiento de trastornos neoplásicos; describe la familia PDGF y su señalización a través de sus receptores |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 89705 | Nilotinib Stada 150 mg cápsulas duras EFG | Cápsula dura | Leucemia mieloide crónica, BCR-ABL1 positivo (según la indicación original) |
| 1241845004 | Nilotinib Accord 50 mg cápsulas duras EFG | Cápsula dura | Leucemia mieloide crónica, BCR-ABL1 positivo (según la indicación original) |
| 89745 | Nilotinib Teva 150 mg cápsulas duras EFG | Cápsula dura | Leucemia mieloide crónica, BCR-ABL1 positivo (según la indicación original) |
| 90289 | Nilotinib Zentiva 150 mg cápsulas duras EFG | Cápsula dura | Leucemia mieloide crónica, BCR-ABL1 positivo (según la indicación original) |
| 07422006 | Tasigna 150 mg cápsulas duras | Cápsula dura | Leucemia mieloide crónica, BCR-ABL1 positivo (según la indicación original) |

Se muestran 5 de las 12 autorizaciones vigentes (todas de principio activo único). El texto de indicación de las autorizaciones no estaba disponible en los datos; la indicación mostrada procede de la indicación original del fármaco.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto. Los datos de contraindicación relacionados con neutropenia, trombocitopenia y anemia sugieren vigilancia hematológica |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática, electrolitos (potasio), glucemia y ECG (intervalo QT) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de riesgo (según el grafo de conocimiento, no texto del prospecto)**:
  - Cardiovasculares: hipertensión, síndrome de QT largo (incluido el familiar), torsades de pointes.
  - Hepáticas y pancreáticas: enfermedad hepática, enfermedad de la vesícula biliar, hiperbilirrubinemia (incluidos hereditaria y síndrome de Gilbert), pancreatitis.
  - Hematológicas: trombocitopenia, neutropenia, agranulocitosis, anemia (incluida la macrocítica).
  - Metabólicas: hiperglucemia, diabetes mellitus, cetoacidosis diabética, deficiencia de potasio, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, hipofosfatemia.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las de nivel **mayor** figuran:
  - Dexametasona
  - Claritromicina
  - Ácido picosulfúrico
  - Polietilenglicol 3350 con electrolitos

  Entre las de nivel moderado destacan los antiácidos e inhibidores de la bomba de protones o antagonistas H2 (famotidina, ranitidina, rabeprazol, omeprazol, cimetidina), otros corticoides (hidrocortisona, betametasona, budesonida, triamcinolona), pioglitazona, loperamida, bupropión, aprepitant, bisacodilo y saxagliptina.

Las advertencias y contraindicaciones del prospecto no estaban disponibles en los datos compilados; consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene una puntuación alta y un fundamento mecanístico plausible (inhibición de PDGFR en un tumor impulsado por PDGFB), pero la evidencia es solo de nivel L4: una revisión y ningún ensayo clínico. Además, faltan los datos de seguridad del prospecto, y el uso establecido en DFSP corresponde a imatinib.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un vacío bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar estudios preclínicos y series de casos o ensayos de nilotinib en DFSP, incluidos pacientes resistentes o intolerantes a imatinib.
- Evaluar el perfil cardiovascular (prolongación del QT) y las interacciones relevantes frente al beneficio esperado.
- Comparar con imatinib, el estándar establecido en esta indicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Lapatinib
parent: Solo predicción del modelo (L5)
nav_order: 452
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Lapatinib: nueva indicación predicha, Dermatofibrosarcoma protuberans (nivel de evidencia L5). Indicación original: Carcinoma de mama HER2 positivo"
monitor_inn: "LAPATINIB"
predicted_indications: ["dermatofibrosarcoma protuberans"]
---

# Lapatinib
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

## Lapatinib: De Carcinoma de Mama HER2 Positivo a Dermatofibrosarcoma Protuberans
{: .text-alpha }

## Resumen en Una Frase

Lapatinib es un inhibidor de tirosina quinasa utilizado originalmente para el tratamiento del carcinoma de mama HER2 positivo.
El modelo TxGNN predice que podría ser efectivo para **dermatofibrosarcoma protuberans**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma de mama HER2 positivo |
| Nueva Indicación Predicha | Dermatofibrosarcoma protuberans |
| Puntaje de Predicción TxGNN | 0.9930 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 2 de 3) |
| Número de Autorizaciones | 3 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, lapatinib es un inhibidor dual de la tirosina quinasa de EGFR y HER2, y su eficacia en el carcinoma de mama HER2 positivo está establecida.

El dermatofibrosarcoma protuberans (DFSP) está impulsado principalmente por la fusión génica COL1A1-PDGFB, que activa la señalización de PDGFRB. El tratamiento dirigido establecido es imatinib, un inhibidor de PDGFR. Por ello, el vínculo mecanístico entre lapatinib y el DFSP no es evidente: la inhibición de EGFR/HER2 no actúa directamente sobre el eje PDGFB-PDGFRB.

Cualquier relación sería especulativa, por ejemplo a través de la interacción entre vías de señalización descendentes (PI3K/AKT, MAPK) o del solapamiento entre vías de receptores tirosina quinasa, y requeriría validación preclínica. La única base actual de la predicción es el puntaje alto del modelo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 07440005 | TYVERB 250 MG comprimidos recubiertos con película | Comprimido masticable | No disponible en los datos compilados |
| 88047 | LAPATINIB STADA 250 MG comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos compilados |
| 07440002 | TYVERB 250 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa EGFR/HER2) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Función hepática, función cardíaca (fracción de eyección del ventrículo izquierdo e intervalo QT), electrolitos (potasio), síntomas respiratorios; consultar el prospecto para el detalle |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación o precaución (según el grafo de conocimiento, no texto del prospecto)**: síndrome de QT largo (incluido el familiar), torsades de pointes, insuficiencia hepática, deficiencia de potasio, enfermedad pulmonar intersticial, daño hepático inducido por fármacos e insuficiencia cardíaca.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las listadas, las de nivel **mayor** son:
  - Loperamida
  - Claritromicina

  Las de nivel **moderado** incluyen:
  - Antiácidos e inhibidores de la secreción gástrica: famotidina, ranitidina, cimetidina, omeprazol, rabeprazol, dexlansoprazol
  - Corticoides: hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida (incluida la nasal)
  - Antieméticos: aprepitant
  - Antidiabéticos: pioglitazona, saxagliptina
  - Laxantes y preparados de limpieza intestinal: bisacodilo, ácido picosulfúrico, polietilenglicol 3350 con electrolitos

No se dispone de las advertencias ni contraindicaciones del prospecto de la AEMPS; consultar el prospecto para esta información.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura, y el vínculo mecanístico con la vía PDGFB-PDGFRB, que impulsa el DFSP, no es evidente. Además, ya existe una terapia dirigida establecida (imatinib).

**Para avanzar se necesita:**
- Validación preclínica (por ejemplo, modelos celulares de DFSP con fusión COL1A1-PDGFB) que demuestre actividad de lapatinib o un vínculo por vías cruzadas (PI3K/AKT, MAPK)
- Datos del mecanismo de acción del fármaco desde DrugBank
- Advertencias y contraindicaciones del prospecto de la AEMPS para completar la evaluación de seguridad (hoy es un vacío bloqueante)
- Revisión sistemática de literatura y ensayos que no se hayan capturado en los datos compilados
- Evaluación de la compatibilidad de la vía de administración y de la similitud con la indicación original
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


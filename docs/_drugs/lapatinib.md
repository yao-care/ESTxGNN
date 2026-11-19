---
layout: default
title: Lapatinib
parent: Solo predicción del modelo (L5)
nav_order: 452
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-05
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
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 3; autorizadas no comercializadas: 1) |
| Número de Autorizaciones | 3 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Lapatinib (traducción no oficial): «Lapatinib es un inhibidor de cinasas de tipo 4-anilinoquinazolina que actúa sobre los dominios intracelulares de tirosina cinasa tanto del receptor del factor de crecimiento epidérmico (EGFR [ErbB1]) como del receptor epidérmico humano de tipo 2 (HER2 [ErbB2]) (valores estimados de K i app de 3nM y 13nM, respectivamente), con una semivida de disociación mayor o igual a 300 minutos. Lapatinib inhibe el crecimiento de células tumorales impulsado por ErbB in vitro y en diversos modelos animales.» Texto original en inglés: "Lapatinib is a 4-anilinoquinazoline kinase inhibitor of the intracellular tyrosine kinase domains of both Epidermal Growth Factor Receptor (EGFR [ErbB1]) and of Human Epidermal Receptor Type 2 (HER2 [ErbB2]) receptors (estimated K i app values of 3nM and 13nM, respectively) with a dissociation half-life of greater than or equal to 300 minutes. Lapatinib inhibits ErbB-driven tumor cell growth in vitro and in various animal models." ([DailyMed: Tykerb (lapatinib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eee37f88-ec6a-4c30-b8aa-e2c71f93088c), versión del 2026-01-27; consultado el 2026-11-19). Según la información conocida, lapatinib es un inhibidor dual de la tirosina quinasa de EGFR y HER2, y su eficacia en el carcinoma de mama HER2 positivo está establecida.

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

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Tykerb (lapatinib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eee37f88-ec6a-4c30-b8aa-e2c71f93088c) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


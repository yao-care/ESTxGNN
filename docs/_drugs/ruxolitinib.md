---
layout: default
title: Ruxolitinib
parent: Solo predicción del modelo (L5)
nav_order: 718
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "RUXOLITINIB"
predicted_indications: ["uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lymphangiomyoma", "lymphangioleiomyomatosis", "liposarcoma", "familial rhabdoid tumor", "lung PEComa", "ovarian myxoid liposarcoma", "hemophagocytic syndrome associated with an infection", "acquired hemophagocytic lymphohistiocytosis associated with malignant disease"]
description: "Ruxolitinib: nueva indicación predicha, Uterine corpus perivascular epithelioid cell tumor (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 6 (comercializadas: 6)"
---

# Ruxolitinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Ruxolitinib: Uterine corpus perivascular epithelioid cell tumor
{: .text-alpha }

## Resumen en Una Frase

Ruxolitinib es un inhibidor de JAK1/JAK2 utilizado originalmente en neoplasias mieloproliferativas, como la mielofibrosis primaria y la policitemia vera.
El modelo TxGNN predice que podría ser efectivo para el **tumor de células epitelioides perivasculares (PEComa) del cuerpo uterino**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción concreta: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Uterine corpus perivascular epithelioid cell tumor |
| Puntaje de Predicción TxGNN | 0.9973 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 6 de 6) |
| Número de Autorizaciones | 6 (comercializadas: 6) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Ruxolitinib (traducción no oficial): «Ruxolitinib, un inhibidor de cinasas, inhibe las cinasas asociadas a Janus (JAK), JAK1 y JAK2, que median la señalización de varias citocinas y factores de crecimiento importantes para la hematopoyesis y la función inmunitaria. La señalización de JAK implica el reclutamiento de STAT (transductores de señales y activadores de la transcripción) hacia los receptores de citocinas, su activación y la posterior localización de las STAT en el núcleo, lo que conduce a la modulación de la expresión génica.» Texto original en inglés: "Ruxolitinib, a kinase inhibitor, inhibits Janus Associated Kinases (JAKs), JAK1 and JAK2, which mediate the signaling of a number of cytokines and growth factors that are important for hematopoiesis and immune function. JAK signaling involves recruitment of STATs (signal transducers and activators of transcription) to cytokine receptors, activation, and subsequent localization of STATs to the nucleus leading to modulation of gene expression." ([DailyMed: Jakafi (ruxolitinib) prescribing information, Incyte Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f1c82580-87ae-11e0-bc84-0002a5d5c51b), versión del 2026-07-20; consultado el 2026-11-19). Según la información conocida, ruxolitinib es un inhibidor de las quinasas JAK1 y JAK2 de la vía JAK-STAT. Su eficacia en neoplasias mieloproliferativas, caracterizadas por una señalización JAK-STAT hiperactiva, está establecida.

Para el PEComa uterino, el vínculo mecanístico es **especulativo**. El PEComa se asocia principalmente con la vía mTOR, y solo se plantea una posible interacción con la señalización JAK-STAT. Los datos compilados no aportan ensayos ni literatura que confirmen esta relación.

**Otras predicciones del modelo.** Entre las 10 principales, otras dos tienen algo más de respaldo:
- **Síndrome hemofagocítico asociado a infección (HLH)**: nivel L3, con 20 publicaciones. Incluye estudios clínicos pediátricos, series de casos y modelos murinos que apoyan la inhibición de JAK/STAT en la hiperinflamación mediada por IFN-γ. Es la dirección mejor respaldada, pero no es la de mayor puntaje. Sus estudios deberían evaluarse en un informe específico.
- **Liposarcoma**: nivel L4, con 2 estudios preclínicos sobre JAK-STAT en el liposarcoma mixoide.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 112773015 | JAKAVI 10 MG COMPRIMIDOS | COMPRIMIDO | Novartis Europharm Limited | Comercializada |
| 112773017 | JAKAVI 5 MG/ML SOLUCION ORAL | SOLUCIÓN ORAL | Novartis Europharm Limited | Comercializada |
| 112773011 | JAKAVI 20 MG COMPRIMIDOS | COMPRIMIDO | Novartis Europharm Limited | Comercializada |
| 112773008 | JAKAVI 15 MG COMPRIMIDOS | COMPRIMIDO | Novartis Europharm Limited | Comercializada |
| 112773005 | JAKAVI 5 MG COMPRIMIDOS | COMPRIMIDO | Novartis Europharm Limited | Comercializada |
| 1231726001 | OPZELURA 15 MG/G CREMA | CREMA | Incyte Biosciences Distribution B.V. | Comercializada |

Se muestran las 6 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Existe además una sexta autorización, OPZELURA 15 MG/G CREMA (Incyte Biosciences Distribution B.V.; n.º 1231726001), en forma de crema (formulación tópica). Jakavi pertenece a Novartis Europharm Limited.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de JAK1/JAK2), no citotóxico convencional |
| Riesgo de Mielosupresión | Medio a alto: la trombocitopenia, la anemia y la neutropenia son efectos conocidos de la clase. Consultar el prospecto |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Hemograma completo con diferencial, función hepática y renal, perfil lipídico; vigilancia de infecciones |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Las más relevantes de las mostradas son:
  - **Mayores**: claritromicina, cobicistat, deferasirox, deferiprona, ibritumomab tiuxetán, tositumomab (incluido tositumomab I-131) y lexidronam de samario (153Sm).
  - **Moderadas**: dexametasona, rosuvastatina, dexfenfluramina, fenfluramina, sibutramina, troglitazona, palifermina y cloruro de estroncio Sr-89.
  - **Menores**: aprepitant, cimetidina, miconazol y clotrimazol.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para el PEComa uterino se basa únicamente en el modelo (L5), sin ensayos, literatura ni un mecanismo respaldado por los datos. No es posible avanzar con esta indicación en este momento.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de ruxolitinib a partir de DrugBank.
- Advertencias y contraindicaciones del prospecto de la AEMPS, actualmente sin datos.
- Estudios preclínicos que evalúen la señalización JAK-STAT en PEComa.
- Considerar priorizar la evaluación de HLH, la indicación con mayor evidencia (L3) entre las predicciones, mediante un informe específico.
- Un plan de monitoreo hematológico y de interacciones, en especial con inhibidores potentes de CYP3A4 como la claritromicina.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Jakafi (ruxolitinib) prescribing information, Incyte Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f1c82580-87ae-11e0-bc84-0002a5d5c51b) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Fluconazole
parent: Solo predicción del modelo (L5)
nav_order: 339
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Fluconazole: nueva indicación predicha, Queratoconjuntivitis epitelial punteada (nivel de evidencia L5). Indicación original: Candidiasis oral (y otras candidiasis, meningitis criptocócica)"
monitor_inn: "Fluconazole"
predicted_indications: ["punctate epithelial keratoconjunctivitis"]
---

# Fluconazole
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

## Fluconazol: De Candidiasis Oral a Queratoconjuntivitis Epitelial Punteada
{: .text-alpha }

## Resumen en Una Frase

Fluconazol es un antifúngico azólico utilizado originalmente para tratar candidiasis (oral, vulvovaginal, esofágica, diseminada y candidemia) y meningitis criptocócica.
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Candidiasis oral (y otras candidiasis, meningitis criptocócica) |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 0.9924 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 16; autorizadas no comercializadas: 1; revocadas o suspendidas: 3) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Fluconazole (traducción no oficial): «El fluconazol es un inhibidor altamente selectivo de la enzima fúngica dependiente del citocromo P450 lanosterol 14-α-desmetilasa. Esta enzima tiene la función de convertir el lanosterol en ergosterol. La consiguiente pérdida de esteroles normales se correlaciona con la acumulación de 14-α-metilesteroles en los hongos y puede ser responsable de la actividad fungistática del fluconazol.» Texto original en inglés: "Fluconazole is a highly selective inhibitor of fungal cytochrome P450 dependent enzyme lanosterol 14-α-demethylase. This enzyme functions to convert lanosterol to ergosterol. The subsequent loss of normal sterols correlates with the accumulation of 14-α-methyl sterols in fungi and may be responsible for the fungistatic activity of fluconazole." ([DailyMed: Diflucan (fluconazole) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f694c617-3383-416c-91b6-b94fda371204), versión del 2026-04-02; consultado el 2026-11-19). Según la información conocida, fluconazol es un antifúngico azólico que inhibe la enzima fúngica lanosterol 14-alfa-desmetilasa (CYP51), bloqueando la síntesis de ergosterol y comprometiendo la membrana de la célula fúngica. Su eficacia en candidiasis y criptococosis está comprobada.

La relación con la nueva indicación es débil. La queratoconjuntivitis epitelial punteada suele ser de origen viral (adenovirus), tóxico, o estar asociada a ojo seco y uso de lentes de contacto, causas que un antifúngico no aborda. Solo sería mecanísticamente aplicable si existiera un componente fúngico en algunos casos.

La puntuación proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Debe tratarse únicamente como una hipótesis sin verificar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

El medicamento está comercializado en este país, con 16 autorizaciones vigentes.

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 64331 | FLUCONAZOL TARBIS 200 mg CAPSULAS DURAS EFG | CÁPSULA DURA | Tarbis Farma S.L. | Comercializada |
| 69082 | FLUCONAZOL TEVA 50 mg CAPSULAS DURAS EFG | CÁPSULA DURA | Teva Pharma S.L.U. | Comercializada |
| 69848 | CANDIFIX 150 mg CAPSULAS DURAS EFG | CÁPSULA DURA | Arafarma Group S.A. | Comercializada |
| 58766 | DIFLUCAN 150 mg CAPSULAS DURAS | CÁPSULA DURA | Vinci Farma, S.A. | Comercializada |
| 64619 | FLUCONAZOL NORMON 200 mg CAPSULAS DURAS EFG | CÁPSULA DURA | Laboratorios Normon S.A. | Comercializada |
| 65089 | FLUCONAZOL MABO 200 mg CAPSULAS DURAS EFG | CÁPSULA DURA | Mabo Farma S.A. | Comercializada |
| 59054 | LOITIN CAPSULAS DURAS 150 mg | CÁPSULA DURA | Dari Pharma S.L. | Comercializada |
| 68847 | FLUCONAZOL TECNIGEN 150 mg CAPSULAS DURAS EFG | CÁPSULA DURA | Tecnimede España Industria Farmaceutica S.A. | Comercializada |
| 59672 | DIFLUCAN 10 mg/ml POLVO PARA SUSPENSION ORAL | POLVO PARA SUSPENSIÓN ORAL | Vinci Farma, S.A. | Comercializada |
| 59055 | LOITIN CAPSULAS DURAS 200 mg | CÁPSULA DURA | Dari Pharma S.L. | Comercializada |

Se muestran 10 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación o precaución (grafo de conocimiento, no texto del prospecto)**: síndrome de QT largo (incluido el familiar), enfermedad renal, piouréter, enfermedad hepática y enfermedad de la vesícula biliar.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones; entre las muestras revisadas:
  - **Mayor**: clorpropamida.
  - **Moderadas**: famotidina, rabeprazol, omeprazol, dexlansoprazol, hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida, loperamida, aprepitant, bisacodilo, ácido picosulfúrico, polietilenglicol con electrolitos y saxagliptina.
  - **Menores**: anfotericina B, clWarithromicina (claritromicina).

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única base es una puntuación alta del modelo (0.9924), sin ensayos clínicos ni literatura, y con una plausibilidad mecanística limitada, ya que las causas habituales de esta enfermedad no son fúngicas.

**Para avanzar se necesita:**
- Revisión sistemática de literatura sobre fluconazol en patología ocular (queratitis fúngica y uso oftálmico).
- Datos detallados del mecanismo de acción y análisis de su vínculo con la fisiopatología de la queratoconjuntivitis epitelial punteada.
- Textos de indicaciones, advertencias y contraindicaciones del prospecto de la AEMPS.
- Evaluación de la compatibilidad de vías de administración (oral/intravenosa frente a la vía tópica ocular).
- Evaluación de seguridad en población con prolongación del QT, enfermedad hepática o renal, y revisión de interacciones.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Diflucan (fluconazole) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f694c617-3383-416c-91b6-b94fda371204) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Sirolimus
parent: Solo predicción del modelo (L5)
nav_order: 740
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-05
monitor_inn: "SIROLIMUS"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lung PEComa", "vulva sarcoma"]
description: "Sirolimus: nueva indicación predicha, Liposarcoma (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 5 (comercializadas: 4; autorizadas no comercializadas: 1)"
---

# Sirolimus
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Sirolimus: Liposarcoma
{: .text-alpha }

## Resumen en Una Frase

Sirolimus es un inhibidor de mTOR (diana de rapamicina en células de mamífero) que se utiliza en medicina de trasplantes y otras indicaciones.
El modelo TxGNN predice que podría ser efectivo para **Liposarcoma (liposarcoma)**, pero por ahora solo existe **1 ensayo clínico** de fase 2 sin resultados publicados, por lo que el respaldo real es muy limitado (nivel de evidencia L5).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 0.9989 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 4 de 5; autorizadas no comercializadas: 1) |
| Número de Autorizaciones | 5 (comercializadas: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Sirolimus (traducción no oficial): «El sirolimús de FYARRO es un inhibidor de la cinasa diana mecanicista de la rapamicina (mTOR, antes denominada diana de la rapamicina en mamíferos). La mTOR, una serina-treonina cinasa, se encuentra en dirección descendente de la vía PI3K/AKT, controla procesos celulares clave como la supervivencia, el crecimiento y la proliferación celulares, y suele estar desregulada en varios tipos de cáncer humano. En las células, el sirolimús se une a la inmunofilina proteína de unión a FK 12 (FKBP-12) para generar un complejo inmunosupresor.» Texto original en inglés: "Sirolimus in FYARRO is an inhibitor of mechanistic target of rapamycin kinase (mTOR, previously known as mammalian target of rapamycin). mTOR, a serine threonine kinase, is downstream of the PI3K/AKT pathway, controls key cellular processes such as cell survival, growth, and proliferation, and is commonly dysregulated in several human cancers. In cells, sirolimus binds to the immunophilin, FK Binding Protein-12 (FKBP-12), to generate an immunosuppressive complex." ([DailyMed: Fyarro (sirolimus) prescribing information, Aadi Bioscience, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0f9bb784-53e2-46f9-a65d-1c6c2a230eaf), versión del 2026-09-09; consultado el 2026-11-19). Según la información conocida, sirolimus inhibe mTORC1, una quinasa que regula el crecimiento y la proliferación celular.

La activación de la vía mTOR se ha descrito en sarcomas de partes blandas, incluido el liposarcoma, y modelos en ratón sugieren que su inhibición puede frenar el crecimiento tumoral. Esto da una lógica biológica plausible para la predicción.

Sin embargo, el único ensayo vinculado evalúa sirolimus en combinación con ciclofosfamida, lo que impide atribuir un efecto al sirolimus solo. La literatura asociada consiste sobre todo en revisiones y datos indirectos de pacientes trasplantados, por lo que la eficacia como agente único no está establecida.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Fase 2 | Completado | 70 | Ensayo de un solo brazo, multicéntrico, de sirolimus más ciclofosfamida en liposarcoma mixoide y condrosarcoma metastásicos o irresecables. No tiene grupo control aleatorizado y no se dispone de resultados publicados. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | ECA | J Am Soc Nephrol | En trasplante renal, sirolimus tras retirada temprana de ciclosporina redujo el riesgo de cáncer; evidencia indirecta, no en liposarcoma. |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Revisión | Cancers | Revisión de nuevas terapias en sarcomas de partes blandas. |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Revisión | Curr Opin Oncol | Revisión de ensayos con agentes dirigidos en sarcomas avanzados. |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Revisión | Bull Cancer | Tratamientos dirigidos en tumores raros del tejido conectivo y sarcomas. |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Revisión | Transplant Proc | Cribado de cáncer en receptores de trasplante renal con inmunosupresión prolongada. |

Ninguna de estas publicaciones evalúa directamente sirolimus en liposarcoma.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 01171010 | RAPAMUNE 2 mg comprimidos recubiertos | Comprimido recubierto | No disponible |
| 01171008 | RAPAMUNE 1 mg comprimidos recubiertos | Comprimido recubierto | No disponible |
| 01171009 | RAPAMUNE 2 mg comprimidos recubiertos | Comprimido recubierto | No disponible |
| 01171013 | RAPAMUNE 0,5 mg comprimidos recubiertos | Comprimido recubierto | No disponible |
| 01171001 | RAPAMUNE 1 mg/ml solución oral | Solución oral | No disponible |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (se registraron 100 interacciones; ejemplos principales):
  - Gravedad mayor: anfotericina B (incluida la formulación de complejo lipídico), mesalazina, balsalazida, claritromicina.
  - Gravedad moderada: acarbosa, metformina, pioglitazona, alogliptina, albiglutida, canagliflozina, clorpropamida, hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona, aprepitant, cimetidina, dapagliflozina.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ningún estudio publicado que pruebe sirolimus en liposarcoma. El único ensayo de fase 2 es de un solo brazo, en combinación con ciclofosfamida y sin resultados publicados, por lo que el respaldo se limita a la predicción del modelo y a un racional mecanístico (nivel L5).

**Para avanzar se necesita:**
- Publicación o acceso a los resultados del ensayo NCT02821507, con análisis específico de la cohorte de liposarcoma.
- Datos detallados del mecanismo de acción.
- Estudios que evalúen sirolimus como agente único en liposarcoma.
- Revisión de advertencias y contraindicaciones del prospecto, no disponibles en los datos compilados.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Fyarro (sirolimus) prescribing information, Aadi Bioscience, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0f9bb784-53e2-46f9-a65d-1c6c2a230eaf) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


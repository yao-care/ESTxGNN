---
layout: default
title: Prednisolone
parent: Solo predicción del modelo (L5)
nav_order: 436
evidence_level: L5
indication_count: 10
---

# Prednisolone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Prednisolona: De Antiinflamatorio e Inmunosupresor Sistémico a Alopecia Areata

## Resumen en Una Frase

Prednisolona es un glucocorticoide sintético usado como antiinflamatorio e inmunosupresor en enfermedades como asma aguda, colitis ulcerosa, artritis reumatoide y lupus eritematoso sistémico.
El modelo TxGNN predice que podría ser efectivo para **alopecia areata**. La evidencia es limitada: **18 ensayos clínicos registrados** (solo 3 tratan realmente alopecia y ninguno prueba prednisolona como intervención principal) y **20 publicaciones**, entre ellas **1 ECA pequeño con prednisolona** y varias revisiones.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las autorizaciones de AEMPS (texto de indicación vacío). DrugBank describe uso antiinflamatorio/inmunosupresor (asma aguda, colitis ulcerosa, enfermedad de Crohn, artritis reumatoide, lupus, EPOC, entre otros) |
| Nueva Indicación Predicha | Alopecia areata |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L2 (un ECA pequeño con prednisolona; sin ensayos registrados de prednisolona en alopecia areata) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos de mecanismo de acción en el campo original de DrugBank. Los datos de farmacología sí muestran que prednisolona actúa sobre el **receptor de glucocorticoides (NR3C1)** y el **receptor de mineralocorticoides (NR3C2)**. Es un agonista del receptor de glucocorticoides con efectos antiinflamatorios e inmunosupresores amplios.

La alopecia areata es una enfermedad autoinmune en la que los linfocitos T atacan el folículo piloso tras perder este su privilegio inmunitario. Suprimir esa inflamación es biológicamente plausible. Un estudio incluido en la evidencia (PMID 30294905) sugiere que los pulsos orales de esteroides modifican los niveles de TNF-α, un mediador importante en esta enfermedad.

Hay límites claros. El único ECA directo con prednisolona es pequeño. Tras suspender el tratamiento las recaídas son frecuentes, y la toxicidad esteroidea limita el uso prolongado. Las revisiones respaldan los corticosteroides como opción a corto plazo, no como tratamiento de mantenimiento.

---

## Evidencia de Ensayos Clínicos

De los 18 ensayos asociados a esta predicción, **15 no evalúan prednisolona en alopecia areata**. Son estudios de lupus eritematoso sistémico (LES), cáncer de próstata y cefaleas, probablemente recuperados por coincidencia de palabras clave. Abajo se listan los tres ensayos sobre alopecia. Los otros 15 no aportan evidencia sobre prednisolona en esta indicación.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Fase 4 | Completado | 42 | Metilprednisolona oral en megapulsos en alopecia areata grave resistente. Mismo grupo farmacológico y el más cercano al uso propuesto, pero no es prednisolona. No hay resultados en el pack |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | N/A (observacional) | Completado | 296 | Tofacitinib en alopecia, con o sin prednisolona adyuvante y sin grupo comparador. Evalúa tofacitinib, no prednisolona |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | N/A | Desconocido | 20 | Compara inyección intralesional con Dermojet frente a jeringa convencional. Contexto de tratamientos con esteroides, sin prednisolona sistémica |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15692475](https://pubmed.ncbi.nlm.nih.gov/15692475/) | 2005 | ECA | J Am Acad Dermatol | Terapia oral en pulsos de prednisolona controlada con placebo en alopecia areata. Es el único ECA directo, pequeño, y el resumen disponible no incluye resultados |
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Metaanálisis en red | Cochrane Database Syst Rev | Compara tratamientos para alopecia areata (inmunosupresores, estimulantes del crecimiento, inmunoterapia de contacto) |
| [30191561](https://pubmed.ncbi.nlm.nih.gov/30191561/) | 2019 | Revisión sistemática | Australas J Dermatol | Evalúa los tratamientos sistémicos de la alopecia areata. La eficacia varía según el tratamiento |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Revisión | Dermatol Pract Concept | Eficacia, recaídas y efectos adversos de los pulsos de corticosteroides en alopecia areata |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Revisión | Pediatr Dermatol | Dosis y pautas de pulsos de corticosteroides en niños con alopecia areata, con sus efectos secundarios |
| [21572877](https://pubmed.ncbi.nlm.nih.gov/21572877/) | 2009 | No clasificado | Dermato-endocrinology | Pulsos de prednisolona a dosis media en alopecia areata. Parece eficaz en fases tempranas, pero los efectos adversos pueden llevar a suspender el tratamiento |
| [32779249](https://pubmed.ncbi.nlm.nih.gov/32779249/) | 2020 | Retrospectivo (138 pacientes) | J Eur Acad Dermatol Venereol | Azatioprina, metotrexato y ciclosporina como ahorradores de esteroides en alopecia areata crónica |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Cohorte retrospectiva (26 pacientes) | Dermatol Ther | Metilprednisolona sola o con metotrexato en alopecia areata extensa |
| [28140540](https://pubmed.ncbi.nlm.nih.gov/28140540/) | 2017 | No clasificado | J Dtsch Dermatol Ges | Corticoterapia secuencial a dosis alta y baja en alopecia areata infantil grave. Las recaídas tras suspender son inevitables |
| [30294905](https://pubmed.ncbi.nlm.nih.gov/30294905/) | 2019 | No clasificado | J Cosmet Dermatol | Cambios en TNF-α sérico y tisular como posible mecanismo de los pulsos orales de esteroides |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 62038 | PRED FORTE 10 MG/ML COLIRIO EN SUSPENSIÓN | Colirio en suspensión | No especificada en los datos |
| 84003 | PAIDOCORT 3 MG/ML SOLUCIÓN ORAL | Solución oral | No especificada en los datos |
| 47546 | ESTILSONA 7 MG/ML GOTAS ORALES EN SUSPENSIÓN | Gotas orales en suspensión | No especificada en los datos |
| 89283 | MINIMS PREDNISOLONA 5 MG/ML COLIRIO EN SOLUCIÓN EN ENVASE UNIDOSIS | Colirio en solución unidosis | No especificada en los datos |

Las autorizaciones cubren dos vías: oftálmica (dos colirios) y oral (solución y gotas). Solo las formas orales son relevantes para pulsos sistémicos en alopecia areata. La compatibilidad de vía y dosis con el uso propuesto aún no está evaluada.

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas / dianas**: la consulta no devolvió interacciones con otros fármacos. Solo registra las dianas farmacológicas de prednisolona: receptor de glucocorticoides (NR3C1) y receptor de mineralocorticoides (NR3C2).
- **Riesgos señalados en la evidencia**: la toxicidad esteroidea con uso prolongado y la recaída tras la suspensión limitan el uso en alopecia areata. Los estudios y revisiones en población pediátrica también describen efectos secundarios asociados a los pulsos.

Consultar el prospecto para advertencias y contraindicaciones detalladas.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay una base biológica razonable (enfermedad autoinmune mediada por linfocitos T) y un ECA con prednisolona, respaldado por revisiones y estudios retrospectivos de corticosteroides sistémicos. Sin embargo, no hay ensayos registrados de prednisolona en alopecia areata y la evidencia directa es pequeña. Las recaídas y la toxicidad esteroidea exigen límites claros de dosis y duración.

**Para avanzar se necesita:**
- Obtener del prospecto de AEMPS las advertencias y contraindicaciones, y completar el mecanismo de acción vía la API de DrugBank.
- Revisar los resultados del ECA de 2005 (PMID 15692475) y de la revisión de pulsos (PMID 37992355) para definir dosis, frecuencia y duración.
- Confirmar la vía y forma farmacéutica adecuadas entre las autorizaciones españolas (solo las orales son candidatas).
- Definir un plan de mitigación de la toxicidad esteroidea y del riesgo de recaída, con la dosis mínima eficaz.
- Comparar con las alternativas actuales, como los inhibidores de JAK, cuando estén disponibles para el paciente.

**Otras predicciones del modelo:**
- **Síndrome nefrótico idiopático sensible a esteroides** (rank 10, L1, Proceed with Guardrails): ya es tratamiento de primera línea y no es un reposicionamiento real. Hay ensayos activos de Fase 3/4 que optimizan dosis y duración.
- **Mucinosis folicular, efluvio telógeno, foliculitis decalvante y otras cinco predicciones**: evidencia L4-L5 (casos aislados o ninguna), decisión Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


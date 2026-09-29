---
layout: default
title: Methylprednisolone
parent: Evidencia moderada (L3-L4)
nav_order: 348
evidence_level: L3
indication_count: 10
---

# Methylprednisolone
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **10** 
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

# Metilprednisolona: De Enfermedades Inflamatorias y Autoinmunes a Alopecia Areata

## Resumen en Una Frase

La metilprednisolona es un glucocorticoide sistémico y tópico, utilizado desde hace décadas en enfermedades inflamatorias y autoinmunes (artritis, lupus, psoriasis, colitis ulcerosa, trastornos alérgicos).
El modelo TxGNN predice que podría ser efectiva para la **alopecia areata**.
La respaldan **1 ensayo clínico de Fase 4 directamente relevante** y **20 publicaciones**, casi todas estudios observacionales, series de casos y revisiones. No hay ensayos de Fase 3 con este fármaco.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedades inflamatorias y autoinmunes (según el uso clínico registrado en farmacología). Los textos de indicación de las autorizaciones españolas están vacíos |
| Nueva Indicación Predicha | Alopecia areata |
| Puntaje de Predicción TxGNN | 99,99 % |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de un texto de mecanismo de acción en el registro del fármaco. Los datos farmacológicos sí lo identifican como ligando del **receptor de glucocorticoides (NR3C1)**. También aparece asociado al canal TRPC5. La activación del receptor de glucocorticoides reduce la respuesta inflamatoria e inmunitaria, que es la base de su uso en las enfermedades autoinmunes ya conocidas.

La alopecia areata es una enfermedad autoinmune en la que los linfocitos T atacan el folículo piloso. Un glucocorticoide sistémico puede frenar ese ataque. La relación con la indicación original es directa: se trata del mismo tipo de problema, una respuesta inmunitaria excesiva, tratado con el mismo mecanismo antiinflamatorio. Las pautas de pulsos, orales o intravenosos, ya se usan fuera de indicación (off-label) en casos extensos o de progresión rápida. Por eso el puntaje tan alto del modelo coincide con la biología conocida.

Los límites son claros. La alopecia areata suele recaer al reducir la dosis, y los efectos adversos de los corticoides se acumulan con el uso repetido. Los inhibidores de JAK son hoy el comparador mejor respaldado.

---

## Evidencia de Ensayos Clínicos

De los 18 ensayos recuperados, solo tres tratan la alopecia areata con corticoides. El resto son en su mayoría estudios de lupus eritematoso sistémico con otros fármacos (baricitinib, sirolimus, entre otros) y no aportan evidencia para la metilprednisolona.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Fase 4 | Completado | 42 | Metilprednisolona oral en pulsos altos y frecuentes en alopecia areata grave resistente a tratamiento. Es el único ensayo directamente relevante. Es pequeño, y su diseño y grupo control no pudieron verificarse |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | N/A | Desconocido | 20 | Compara la inyección intralesional de corticoide con Dermojet (sin aguja) frente a jeringa convencional en alopecia areata. El corticoide concreto no está identificado |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | N/A | Completado | 296 | Estudio observacional de tofacitinib en alopecia, con prednisolona adyuvante en algunos pacientes. El fármaco evaluado es tofacitinib, no metilprednisolona |

**Nota de calidad de datos:** para NCT03616964 y NCT03843125 el análisis automático indica alopecia areata, pero sus títulos oficiales describen lupus eritematoso sistémico. No se han usado como evidencia.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32270396](https://pubmed.ncbi.nlm.nih.gov/32270396/) | 2020 | Revisión sistemática | Dermatol Ther | Ciclosporina sola o con corticoides sistémicos en alopecia areata, con resultados variables |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Revisión | Dermatol Pract Concept | Eficacia, recaídas y efectos adversos de la terapia con pulsos de corticoides en alopecia areata |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Revisión | Pediatr Dermatol | Dosis y pautas de pulsos de corticoides en niños con alopecia areata; las pautas no están bien establecidas |
| [28378336](https://pubmed.ncbi.nlm.nih.gov/28378336/) | 2017 | Revisión | Int J Dermatol | Opciones de tratamiento para alopecia total y universal; ninguna está aprobada por la FDA |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Cohorte retrospectiva | Dermatol Ther | Metilprednisolona sola frente a combinada con metotrexato en 26 pacientes con alopecia areata extensa |
| [25566921](https://pubmed.ncbi.nlm.nih.gov/25566921/) | 2015 | Serie de casos | Indian J Dermatol Venereol Leprol | Pulsos intravenosos de metilprednisolona en alopecia areata grave |
| [23336179](https://pubmed.ncbi.nlm.nih.gov/23336179/) | 2014 | Serie de casos | J Dermatolog Treat | Pulsos de metilprednisolona en alopecia extensa, planteados como opción con menos efectos adversos que el tratamiento oral prolongado |
| [9777767](https://pubmed.ncbi.nlm.nih.gov/9777767/) | 1998 | Estudio prospectivo abierto | J Am Acad Dermatol | Pulso único intravenoso de metilprednisolona en 45 pacientes con alopecia areata grave de menos de 12 meses de evolución |
| [22426909](https://pubmed.ncbi.nlm.nih.gov/22426909/) | 2012 | Estudio clínico | Saudi Med J | Metilprednisolona oral en pulsos altos en alopecia areata grave resistente; corresponde al ensayo NCT01167946 |
| [12746668](https://pubmed.ncbi.nlm.nih.gov/12746668/) | 2003 | Estudio prospectivo abierto | Ann Dermatol Venereol | Pulsos intravenosos mensuales repetidos en 66 pacientes con alopecia areata grave |

---

## Información de Mercado en España

Los textos de indicación aprobada están vacíos en los datos recibidos, por lo que no se muestran.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 34022 | URBASON 20 mg polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable |
| 53202 | SOLU-MODERIN 500 mg polvo y disolvente para solución inyectable | Liofilizado y disolvente para solución inyectable |
| 63188 | LEXXEMA 1 mg/g ungüento | Pomada |
| 82969 | ISZEMA 1 mg/g emulsión cutánea | Emulsión cutánea |
| 59124 | URBASON 40 mg comprimidos | Comprimido |

---

## Consideraciones de Seguridad

- **Advertencias principales:** la literatura señala la recaída tras reducir la dosis y los efectos adversos acumulados de los corticoides con tratamientos repetidos o prolongados.

No se dispone de advertencias ni contraindicaciones formales del prospecto de la AEMPS. Consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La metilprednisolona en pulsos tiene un mecanismo coherente con la alopecia areata y un uso off-label establecido. Sin embargo, la evidencia se limita a un ensayo de Fase 4 pequeño y a estudios observacionales, sin ECA de Fase 3. Por eso solo se justifica en ciclos cortos y con seguimiento, considerando los inhibidores de JAK como comparador mejor respaldado.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS para completar advertencias y contraindicaciones.
- Verificar el diseño y los resultados de NCT01167946 (grupo control, variable principal, tasa de recaída).
- Un ECA comparativo frente a otras opciones (por ejemplo, inhibidores de JAK) y con seguimiento de recaídas.
- Definir una pauta de pulsos, con dosis y duración máxima, y un plan de monitoreo de efectos adversos.
- Fuera de la alopecia areata, la predicción de **síndrome nefrótico idiopático sensible a esteroides** (L4) queda como pregunta de investigación. Su evidencia es indirecta, de clase terapéutica, y el resto de las predicciones tienen solo puntaje del modelo (L5, Hold).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


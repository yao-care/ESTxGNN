---
layout: default
title: Cabergoline
parent: Solo predicción del modelo (L5)
nav_order: 130
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Cabergoline: nueva indicación predicha, Cáncer de hipófisis (pituitary cancer) (nivel de evidencia L5). Indicación original: Hiperprolactinemia y tumor hipofisario productor de prolactina (según…"
monitor_inn: "Cabergoline"
predicted_indications: ["progeria-short stature-pigmented nevi syndrome", "pituitary cancer", "cerebral palsy, spastic quadriplegic", "glaucoma"]
---

# Cabergoline
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Cabergolina: De Hiperprolactinemia a Cáncer de Hipófisis

## Resumen en Una Frase

Cabergolina es un agonista dopaminérgico utilizado originalmente para tratar la hiperprolactinemia y los tumores hipofisarios productores de prolactina.
El modelo TxGNN predice que podría ser efectivo para **cáncer de hipófisis**, con **12 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección, aunque la evidencia se refiere sobre todo a adenomas hipofisarios benignos y no a carcinoma.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperprolactinemia y tumor hipofisario productor de prolactina (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Cáncer de hipófisis (*pituitary cancer*) |
| Puntaje de Predicción TxGNN | 99.04% |
| Nivel de Evidencia | L1 (aplicable al espectro de adenomas; no demuestra beneficio en carcinoma) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Proceed with Guardrails |

> Nota: la predicción de mayor puntaje es "adenocarcinoma de hipófisis" (99.06%), pero solo dispone de tres casos clínicos no concluyentes (L4, Hold). Este informe se centra en "cáncer de hipófisis" (3.ª predicción), que tiene la evidencia más sólida.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, cabergolina es un agonista de los receptores dopaminérgicos D2. Los datos de farmacología muestran además afinidad por receptores serotoninérgicos (5-HT1A, 1B, 1D, 2A, 2B, 2C), adrenérgicos (α1A, α2A, α2B, α2C) y otros receptores dopaminérgicos (D1, D3, D4, D5).

Las células tumorales lactotropas expresan receptores D2. Al activarlos, cabergolina reduce la secreción de prolactina y reduce el tamaño del tumor. Su eficacia en prolactinomas está comprobada y es el tratamiento de primera elección. Una revisión de 2020 (PMID 31597135) describe además mecanismos antitumorales nuevos, como la inhibición de la proliferación celular y la inducción de muerte celular.

Conviene ser prudentes: la evidencia disponible corresponde a adenomas hipofisarios (prolactinoma, adenoma no funcionante, tumor corticotropo) y no a carcinoma hipofisario, una entidad rara que se trata sobre todo con cirugía, radioterapia y temozolomida. La etiqueta "cáncer de hipófisis" parece agrupar enfermedad de tipo adenoma. El valor novedoso real estaría en los adenomas no funcionantes y corticotropos. El puntaje alto del modelo probablemente refleja proximidad en el grafo con adenoma y prolactinoma, no evidencia directa.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00889525](https://clinicaltrials.gov/study/NCT00889525) | Fase 3 | Completado | No disponible | Cabergolina en tumor hipofisario corticotropo (enfermedad de Cushing); sin resultados aportados |
| [NCT03271918](https://clinicaltrials.gov/study/NCT03271918) | Fase 3 | Completado | 140 | Aleatorizado, abierto: cabergolina en adenoma no funcionante residual tras cirugía transesfenoidal |
| [NCT02288962](https://clinicaltrials.gov/study/NCT02288962) | Fase 3 | Activo, no recluta | 60 | Aleatorizado: agonista dopaminérgico en adenomas hipofisarios no funcionantes |
| [NCT07463235](https://clinicaltrials.gov/study/NCT07463235) | Fase 3 | Reclutando | 70 | Dosis alta vs. estándar en microprolactinomas (indicación ya aprobada) |
| [NCT01620138](https://clinicaltrials.gov/study/NCT01620138) | Fase 2/3 | Completado | 21 | Expresión de receptores de somatostatina y dopamina en adenomas no funcionantes y prolactinomas resistentes |
| [NCT01915303](https://clinicaltrials.gov/study/NCT01915303) | Fase 2 | Terminado | 68 | Pasireotida sola o con cabergolina en enfermedad de Cushing |
| [NCT07034859](https://clinicaltrials.gov/study/NCT07034859) | Fase 4 | Inscripción por invitación | 30 | Cabergolina como terapia primaria en adenoma hipofisario no funcionante, 48 semanas |
| [NCT00376064](https://clinicaltrials.gov/study/NCT00376064) | Fase 4 | Completado | 20 | Octreótido + cabergolina en acromegalia parcialmente respondedora, un solo brazo |
| [NCT07045935](https://clinicaltrials.gov/study/NCT07045935) | Fase 4 | Reclutando | 60 | Resultados metabólicos en prolactinoma con agonistas dopaminérgicos |
| [NCT03457389](https://clinicaltrials.gov/study/NCT03457389) | No aplica | Desconocido | 68 | Niveles objetivo de prolactina y recaída tras retirada en prolactinoma |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37097352](https://pubmed.ncbi.nlm.nih.gov/37097352/) | 2023 | Revisión | JAMA | Diagnóstico y manejo de adenomas hipofisarios funcionantes y no funcionantes |
| [36974474](https://pubmed.ncbi.nlm.nih.gov/36974474/) | 2023 | Revisión | J Clin Endocrinol Metab | Abordaje del paciente con prolactinoma |
| [40876473](https://pubmed.ncbi.nlm.nih.gov/40876473/) | 2025 | Revisión | Lancet Diabetes Endocrinol | Patogenia, diagnóstico y manejo de adenomas secretores de prolactina |
| [36013562](https://pubmed.ncbi.nlm.nih.gov/36013562/) | 2022 | Revisión | Medicina (Kaunas) | Tratamiento del prolactinoma: agonistas dopaminérgicos, cirugía y terapia multimodal en casos agresivos |
| [28025719](https://pubmed.ncbi.nlm.nih.gov/28025719/) | 2017 | Revisión | Pituitary | Uso de cabergolina en acromegalia |
| [31597135](https://pubmed.ncbi.nlm.nih.gov/31597135/) | 2020 | Revisión | Neuroendocrinology | Nuevos mecanismos antitumorales de cabergolina y posibles aplicaciones más amplias |
| [38989697](https://pubmed.ncbi.nlm.nih.gov/38989697/) | 2024 | Preclínico | Neuro-oncology | Dirigir HTR2B frena el crecimiento de adenomas no funcionantes y sensibiliza a cabergolina |
| [25732645](https://pubmed.ncbi.nlm.nih.gov/25732645/) | 2015 | Revisión | Endocrinol Metab Clin North Am | En la mayoría de estudios, cabergolina no se asocia a valvulopatía significativa en tumores hipofisarios |
| [30404098](https://pubmed.ncbi.nlm.nih.gov/30404098/) | 2019 | Revisión | Neuroendocrinology | Prolactinomas gigantes: raros, agresivos e invasivos |
| [18426817](https://pubmed.ncbi.nlm.nih.gov/18426817/) | 2008 | Estudio | Eur J Endocrinol | Ligandos somatostatinérgicos para superar la resistencia a agonistas dopaminérgicos en prolactinomas |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 60867 | DOSTINEX 0,5 mg comprimidos (Pfizer) | Comprimido | No disponible |
| 64408 | SOGILEN 1 mg comprimidos (Pfizer) | Comprimido | No disponible |
| 64409 | SOGILEN 2 mg comprimidos (Pfizer) | Comprimido | No disponible |
| 69669 | Cabergolina Teva 0,5 mg comprimidos EFG | Comprimido | No disponible |
| 69686 | Cabergolina Teva 2 mg comprimidos EFG | Comprimido | No disponible |

Hay una sexta autorización vigente: Cabergolina Teva 1 mg comprimidos EFG (n.º 69687).

---

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación (según el grafo de conocimiento, no del prospecto)**: enfermedad hepática, enfermedad de la vesícula biliar, valvulopatía cardíaca, fibrosis pulmonar (incluida la postinflamatoria), fibrosis retroperitoneal relacionada con IgG4, preeclampsia y preeclampsia grave.
- **Interacciones y perfil farmacológico**: cabergolina actúa sobre múltiples receptores (dopaminérgicos D1–D5, serotoninérgicos 5-HT1A/1B/1D/2A/2B/2C y adrenérgicos α1A/α2A/α2B/α2C). La actividad agonista 5-HT2B se relaciona con el riesgo de valvulopatía y fibrosis. No se dispone de interacciones con otros fármacos clasificadas por nivel.
- **Señal ocular**: se ha descrito un caso de glaucoma bilateral de ángulo cerrado en una paciente tratada con cabergolina (PMID 21347189).

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen varios ensayos de Fase 3 completados o en curso con cabergolina en adenomas hipofisarios, pero no hay datos de resultados ni evidencia directa en carcinoma hipofisario. La decisión debe considerarse una pregunta de investigación en adenomas no funcionantes y corticotropos, no una confirmación de beneficio en carcinoma.

**Para avanzar se necesita:**
- Obtener y revisar los resultados de los ensayos NCT00889525, NCT03271918 y NCT02288962.
- Aclarar si "cáncer de hipófisis" corresponde a carcinoma verdadero o a adenoma agresivo, y definir la población diana.
- Obtener el prospecto de la AEMPS (advertencias, contraindicaciones y textos de indicación aprobada).
- Completar los datos del mecanismo de acción (MOA).
- Plan de monitoreo de seguridad cardíaca (valvulopatía), pulmonar y ocular, dado el perfil agonista 5-HT2B y el uso previsiblemente prolongado o a dosis altas.

---

**Otras predicciones evaluadas (Hold):** adenocarcinoma de hipófisis (L4, solo casos clínicos no concluyentes), glaucoma (L4, con señal de seguridad contraria), síndrome de progeria con talla baja y nevus pigmentados, y parálisis cerebral espástica cuadripléjica (L5, sin evidencia ni vínculo mecanístico plausible).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


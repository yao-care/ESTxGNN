---
layout: default
title: Atomoxetine
parent: Solo predicción del modelo (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
---

# Atomoxetine
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

# Atomoxetina: De TDAH a Trastorno Específico del Desarrollo

## Resumen en Una Frase

Atomoxetina es un inhibidor selectivo de la recaptación de noradrenalina, utilizado originalmente para el tratamiento del trastorno por déficit de atención e hiperactividad (TDAH).
El modelo TxGNN predice que podría ser efectivo para el **trastorno específico del desarrollo**, y en la práctica la evidencia se concentra en los síntomas de TDAH en niños con autismo.
Actualmente lo respaldan **8 ensayos clínicos** y **16 publicaciones**, de los cuales solo 2 ensayos aportan evidencia directa en autismo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | TDAH (según el registro farmacológico; los textos de indicación de las autorizaciones AEMPS vienen vacíos) |
| Nueva Indicación Predicha | Trastorno específico del desarrollo |
| Puntaje de Predicción TxGNN | 99,998 % |
| Nivel de Evidencia | L2 (ver nota) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

> Nota: solo hay un ECA de Fase 3 completado (NCT00498173, n=60). Con la tabla de niveles, eso corresponde a L2. El paquete de evidencia asigna internamente L1, porque cuenta además dos ECA de Fase 4 completados en autismo.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente principal. Según la información conocida, atomoxetina es un inhibidor selectivo de la recaptación de noradrenalina. El registro farmacológico la vincula con los transportadores NET (SLC6A2), DAT (SLC6A3) y SERT (SLC6A4). Un mayor tono noradrenérgico prefrontal podría mejorar la atención y reducir la impulsividad.

El TDAH es en sí un trastorno del neurodesarrollo, y por eso el modelo lo acerca a la categoría amplia de "trastorno específico del desarrollo". El TDAH ya es la indicación aprobada. El valor del reposicionamiento está en la **población con autismo y síntomas de TDAH asociados**, donde hay ensayos aleatorizados y un metaanálisis.

Conviene una cautela: la evidencia respalda la mejoría de los **síntomas de TDAH** en autismo, no de los síntomas nucleares del autismo.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00498173](https://clinicaltrials.gov/study/NCT00498173) | Fase 3 | Completado | 60 | ECA doble ciego frente a placebo de atomoxetina en niños y adolescentes con autismo y síntomas de TDAH. Evidencia directa. |
| [NCT00844753](https://clinicaltrials.gov/study/NCT00844753) | Fase 4 | Completado | 128 | Atomoxetina o placebo, con o sin entrenamiento a padres, en niños con autismo, Asperger o TGD-NE con síntomas de TDAH. Evidencia directa. |
| [NCT00380692](https://clinicaltrials.gov/study/NCT00380692) | Fase 4 | Completado | 97 | ECA doble ciego de atomoxetina frente a placebo para síntomas de TDAH en niños y adolescentes con trastorno del espectro autista. |
| [NCT00510276](https://clinicaltrials.gov/study/NCT00510276) | Fase 4 | Completado | 445 | Atomoxetina frente a placebo en adultos jóvenes con TDAH y resultados funcionales. Apoya el núcleo TDAH, no es específico de autismo. |
| [NCT04085172](https://clinicaltrials.gov/study/NCT04085172) | Fase 4 | Completado | 396 | Estudio de guanfacina de liberación prolongada en TDAH pediátrico, con atomoxetina como comparador activo. La población exacta no está confirmada. |
| [NCT05635318](https://clinicaltrials.gov/study/NCT05635318) | No aplica | Desconocido | 102 | Neurofeedback con EEG cuantitativo como terapia adicional en TDAH. La atomoxetina no es la intervención evaluada. |
| [NCT01470261](https://clinicaltrials.gov/study/NCT01470261) | No aplica | Completado | 1398 | Estudio no aleatorizado (ADDUCE) sobre efectos crónicos de fármacos para TDAH. Útil solo como contexto de seguridad. |
| [NCT00573859](https://clinicaltrials.gov/study/NCT00573859) | Fase 1/2 | Completado | 27 | Mecanismos de refuerzo del tabaquismo en adultos con TDAH. Estudio conductual, no de eficacia. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30653855](https://pubmed.ncbi.nlm.nih.gov/30653855/) | 2019 | Revisión sistemática y metaanálisis | Autism Research | Atomoxetina para síntomas de TDAH en niños y adolescentes con autismo. Incluye tres ECA controlados con placebo (241 niños). |
| [39701638](https://pubmed.ncbi.nlm.nih.gov/39701638/) | 2025 | Revisión sistemática y metaanálisis en red | The Lancet Psychiatry | Eficacia y aceptabilidad comparadas de intervenciones farmacológicas, psicológicas y de neuroestimulación para TDAH en adultos. No es específico de autismo. |
| [27721971](https://pubmed.ncbi.nlm.nih.gov/27721971/) | 2016 | Revisión | Therapeutic Advances in Psychopharmacology | Eficacia de atomoxetina en TDAH con comorbilidades frecuentes, incluidos los trastornos generalizados del desarrollo. |
| [32946507](https://pubmed.ncbi.nlm.nih.gov/32946507/) | 2020 | Revisión sistemática | PLoS One | Diferencias por sexo en la prescripción y eficacia de la farmacoterapia del TDAH en niñas y mujeres. |
| [35485452](https://pubmed.ncbi.nlm.nih.gov/35485452/) | 2022 | Cohorte retrospectiva | Neuropsychopharmacology Reports | Factores asociados a la eficacia de atomoxetina en TDAH adulto. Su eficacia a largo plazo ronda el 40 % a los 6 meses. |
| [42675180](https://pubmed.ncbi.nlm.nih.gov/42675180/) | 2026 | Estudio de neuroimagen | Nature Biomedical Engineering | Desviaciones de la conectividad estructural en jóvenes con TDAH que predicen síntomas y respuesta al tratamiento. |
| [41332541](https://pubmed.ncbi.nlm.nih.gov/41332541/) | 2025 | Preprint | bioRxiv | Versión preliminar del estudio de conectividad estructural anterior. No está revisada por pares. |
| [39514707](https://pubmed.ncbi.nlm.nih.gov/39514707/) | 2024 | Reporte de caso | J Dev Behav Pediatr | Niño de 11 años con TDAH, ansiedad, depresión e ideación suicida tratado con atomoxetina y teleterapia. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 82443 | ATOMOXETINA CINFA 25 MG CAPSULAS DURAS EFG | Cápsula dura | Laboratorios Cinfa S.A. |
| 82445 | ATOMOXETINA CINFA 60 MG CAPSULAS DURAS EFG | Cápsula dura | Laboratorios Cinfa S.A. |
| 84536 | ATOMOXETINA MACLEODS 60 MG CAPSULAS DURAS EFG | Cápsula dura | Macleods Pharma España S.L.U. |
| 84533 | ATOMOXETINA MACLEODS 18 MG CAPSULAS DURAS EFG | Cápsula dura | Macleods Pharma España S.L.U. |
| 84531 | ATOMOXETINA MACLEODS 10 MG CAPSULAS DURAS EFG | Cápsula dura | Macleods Pharma España S.L.U. |

Se muestran 5 de las 20 autorizaciones. Los registros no incluyen el texto de la indicación aprobada.

---

## Consideraciones de Seguridad

Señales a vigilar según el análisis del paquete de evidencia para esta indicación:
- **Irritabilidad** y **efectos cardiovasculares**.

Consultar el prospecto para el resto de la información de seguridad (advertencias, contraindicaciones e interacciones).

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay ensayos aleatorizados completados (Fase 3 y Fase 4) y un metaanálisis que respaldan el beneficio de atomoxetina sobre los síntomas de TDAH en niños con autismo. La evidencia no cubre los síntomas nucleares del autismo, y la indicación de TDAH ya está aprobada, por lo que el avance debe acotarse a esa población.

**Para avanzar se necesita:**
- Obtener y revisar la ficha técnica de AEMPS (advertencias y contraindicaciones), que hoy bloquea el cribado de seguridad.
- Completar el mecanismo de acción desde DrugBank.
- Confirmar las indicaciones aprobadas en los registros de AEMPS, que vienen vacíos.
- Definir un plan de monitoreo de irritabilidad y de parámetros cardiovasculares en niños con autismo.
- Las otras 9 predicciones tienen evidencia débil o nula. Tourette (L3) queda como pregunta de investigación, con un único ensayo de Fase 2 terminado con 5 participantes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Terbutaline
parent: Evidencia alta (L1-L2)
nav_order: 780
evidence_level: L1
indication_count: 3
last_modified_at: 2026-10-14
description: "Terbutaline: nueva indicación predicha, Enfermedad pulmonar obstructiva (nivel de evidencia L1). Indicación original: Asma (también asma intrínseco, asma alérgico…"
---

# Terbutaline
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **3** 
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

# Terbutalina: De Asma a Enfermedad Pulmonar Obstructiva

## Resumen en Una Frase

Terbutalina es un agonista beta-2 adrenérgico, utilizado originalmente para el tratamiento del asma, la bronquitis y el enfisema pulmonar.
El modelo TxGNN predice que podría ser efectiva para **enfermedad pulmonar obstructiva**,
con **14 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección. Cabe señalar que esta indicación se solapa en gran medida con las indicaciones ya conocidas del fármaco, por lo que se trata más de una confirmación que de un reposicionamiento propiamente dicho.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Asma (también asma intrínseco, asma alérgico, bronquitis y enfisema pulmonar, según el grafo de conocimiento) |
| Nueva Indicación Predicha | Enfermedad pulmonar obstructiva |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Terbutalina es un agonista selectivo del receptor beta-2 adrenérgico. Su activación en el músculo liso de las vías respiratorias eleva el AMPc intracelular y provoca broncodilatación. Los datos compilados no incluyen una descripción formal del mecanismo de acción, por lo que esta explicación procede del conocimiento farmacológico general. Los datos de farmacología sí confirman que el fármaco actúa sobre los receptores ADRB1 y ADRB2.

La indicación original (asma, bronquitis, enfisema) y la nueva (enfermedad pulmonar obstructiva) comparten la obstrucción reversible del flujo aéreo como característica central. Por ello, el mecanismo broncodilatador es directamente aplicable, y la alta puntuación del modelo concuerda con la farmacología conocida.

## Evidencia de Ensayos Clínicos

Se muestran los ensayos más relevantes (de 14 registrados).

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02224157](https://clinicaltrials.gov/study/NCT02224157) | Fase 3 | Completado | 4215 | Symbicort a demanda vs. budesonida dos veces al día más terbutalina a demanda en asma |
| [NCT02149199](https://clinicaltrials.gov/study/NCT02149199) | Fase 3 | Completado | 3850 | Symbicort a demanda vs. terbutalina a demanda vs. budesonida más terbutalina en asma |
| [NCT06626620](https://clinicaltrials.gov/study/NCT06626620) | Fase 3 | Completado | 120 | Sulfato de magnesio intravenoso vs. terbutalina en niños con exacerbación aguda de asma |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Fase 3 | Completado | 2091 | Symbicort SMART vs. Symbicort más terbutalina a demanda en asma |
| [NCT00849095](https://clinicaltrials.gov/study/NCT00849095) | Fase 3 | Completado | 860 | Budesonida/formoterol a demanda vs. régimen regular más terbutalina a demanda en asma leve-moderada |
| [NCT00252863](https://clinicaltrials.gov/study/NCT00252863) | Fase 3 | Completado | 1600 | Terapia con inhalador único Symbicort vs. práctica convencional (indirecto para terbutalina) |
| [NCT02322788](https://clinicaltrials.gov/study/NCT02322788) | Fase 3 | Completado | 95 | Bricanyl Turbuhaler M3 vs. M2: protección frente a la broncoconstricción inducida por metacolina |
| [NCT01096017](https://clinicaltrials.gov/study/NCT01096017) | Fase 3 | Completado | 24 | Terbutalina Turbuhaler 0,4 mg vs. salbutamol pMDI en adultos japoneses con asma |
| [NCT00837967](https://clinicaltrials.gov/study/NCT00837967) | Fase 3 | Completado | 25 | Tolerabilidad de 10 inhalaciones de Symbicort vs. terbutalina en adultos japoneses con asma |
| [NCT04973345](https://clinicaltrials.gov/study/NCT04973345) | Fase 2/3 | Retirado | 0 | Relación exposición-respuesta de terbutalina en asma; sin participantes, no aporta evidencia |

## Evidencia de Literatura

Se muestran las publicaciones más relevantes (de 20 recuperadas).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29768149](https://pubmed.ncbi.nlm.nih.gov/29768149/) | 2018 | ECA | N Engl J Med | Budesonida-formoterol a demanda como alternativa al tratamiento convencional en asma leve |
| [3073804](https://pubmed.ncbi.nlm.nih.gov/3073804/) | 1988 | ECA | Br J Dis Chest | Terbutalina oral aumentó la fuerza de contracción diafragmática en pacientes con EPOC |
| [6988343](https://pubmed.ncbi.nlm.nih.gov/6988343/) | 1980 | ECA | Int J Clin Pharmacol Ther Toxicol | Comparación doble ciego de clenbuterol y terbutalina oral en enfermedad pulmonar obstructiva crónica |
| [30156361](https://pubmed.ncbi.nlm.nih.gov/30156361/) | 2019 | ECA | Acad Emerg Med | Terbutalina nebulizada con ipratropio vs. terbutalina sola en exacerbación aguda de EPOC con ventilación no invasiva |
| [23348973](https://pubmed.ncbi.nlm.nih.gov/23348973/) | 2013 | Revisión | Am J Respir Crit Care Med | Los agonistas beta-2 de acción corta, incluida la terbutalina, ofrecen alivio rápido de síntomas |
| [36227333](https://pubmed.ncbi.nlm.nih.gov/36227333/) | 2023 | Revisión sistemática | Naunyn-Schmiedeberg's Arch Pharmacol | Farmacocinética clínica de terbutalina en humanos según vía, edad y estado de enfermedad |
| [10384064](https://pubmed.ncbi.nlm.nih.gov/10384064/) | 1999 | Estudio clínico (cruzado, placebo) | Lung | Efecto de una dosis única de terbutalina Turbuhaler sobre función pulmonar y capacidad de ejercicio en EPOC |
| [1615190](https://pubmed.ncbi.nlm.nih.gov/1615190/) | 1992 | Estudio clínico (cruzado, placebo) | Respir Med | Efecto de terbutalina inhalada sobre FEV1, FVC, disnea y distancia de marcha en EPOC |
| [33065789](https://pubmed.ncbi.nlm.nih.gov/33065789/) | 2020 | Estudio clínico | Ann Palliat Med | N-acetilcisteína combinada con sulfato de terbutalina en ancianos con EPOC |
| [2662130](https://pubmed.ncbi.nlm.nih.gov/2662130/) | 1989 | Estudio clínico (cruzado) | Pediatrics | Terbutalina y teofilina de liberación lenta en el tratamiento prolongado del asma infantil |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 52616 | TERBASMIN 0,3 mg/ml SOLUCIÓN ORAL | Solución oral | No disponible en los datos compilados |
| 58859 | TERBASMIN TURBUHALER 500 microgramos/inhalación POLVO PARA INHALACIÓN | Polvo para inhalación | No disponible en los datos compilados |

## Consideraciones de Seguridad

Consultar el prospecto para obtener información sobre advertencias y contraindicaciones.

- **Contraindicaciones o precauciones señaladas en el grafo de conocimiento** (no proceden del texto del prospecto): hipertensión, epilepsia, hiperglucemia, diabetes mellitus, cetoacidosis diabética, deficiencia de potasio, parada cardíaca súbita, enfermedades de la conducción cardíaca, insuficiencia respiratoria, hipertiroidismo (enfermedad de Graves, tirotoxicosis), edema pulmonar, isquemia miocárdica, enfermedad coronaria y desprendimiento de placenta.
- **Interacciones farmacológicas**: los datos disponibles solo describen la actividad sobre los receptores beta-1 y beta-2 adrenérgicos; no se dispone de interacciones con otros fármacos. Un estudio de la literatura (PMID 6107217) analizó la interacción con betabloqueantes (metoprolol, propranolol) en pacientes con enfermedad pulmonar obstructiva.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Varios ensayos de Fase 3 completados, algunos de gran tamaño, evalúan terbutalina en asma, y existen ECAs en enfermedad pulmonar obstructiva crónica. Sin embargo, en muchos de esos ensayos terbutalina actúa como comparador o medicación de rescate, y la indicación ya está cubierta por el uso conocido del fármaco, por lo que se trata sobre todo de una confirmación.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), ya que actualmente no están disponibles.
- Completar los datos del mecanismo de acción desde DrugBank.
- Definir un plan de monitoreo de seguridad cardiovascular, metabólica (glucosa, potasio) y tiroidea, dadas las condiciones señaladas en el grafo de conocimiento.
- Confirmar qué indicaciones figuran en las autorizaciones españolas para delimitar el alcance real del reposicionamiento.

**Otras predicciones del modelo (decisión: Hold):** *malformación respiratoria* (puntaje 99.52%, nivel L4) y *síndrome de Rienhoff* (puntaje 99.38%, nivel L5). Ninguna cuenta con evidencia directa de eficacia: la única señal para la primera es un programa farmacocinético pediátrico genérico, y para la segunda no hay ensayos ni literatura.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


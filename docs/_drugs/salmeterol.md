---
layout: default
title: Salmeterol
parent: Evidencia alta (L1-L2)
nav_order: 483
evidence_level: L1
indication_count: 7
---

# Salmeterol
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **7** 
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

# Salmeterol: Predicción de Nueva Indicación en Bronquitis

## Resumen en Una Frase

Salmeterol es un agonista beta2-adrenérgico de acción prolongada (LABA), comercializado en España en inhaladores para el tratamiento respiratorio de mantenimiento. El modelo TxGNN predice que podría ser efectivo para **bronquitis**, con **16 ensayos clínicos** y **20 publicaciones** relacionados. Sin embargo, la mayor parte de esa evidencia corresponde a EPOC, y en muchos ensayos salmeterol se usa en combinación con fluticasona.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99,92% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 9 |
| Decisión Recomendada | Proceed with Guardrails |

*Nota: los registros de la AEMPS no incluyen el texto de la indicación aprobada, por lo que no se puede indicar la indicación original.*

---

## ¿Por qué es Razonable esta Predicción?

Salmeterol es un LABA que relaja el músculo liso de las vías respiratorias mediante el receptor beta2 y la vía del AMPc, y produce una broncodilatación sostenida. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank; la descripción anterior procede del análisis de racionalidad incluido en el paquete de evidencia. Además, un estudio clínico (PMID 15970448) sugiere que salmeterol podría mejorar el aclaramiento mucociliar en pacientes con bronquitis crónica.

La bronquitis crónica es un fenotipo de la EPOC, y salmeterol ya forma parte del tratamiento de mantenimiento de la EPOC, solo o combinado con un corticosteroide inhalado. Por ello, la predicción es coherente con el uso clínico establecido.

Conviene una cautela: el análisis del propio paquete indica que esto es un uso **dentro o muy cerca de la indicación autorizada**, más que un reposicionamiento genuino. Como el campo de indicación original está vacío, la puntuación tan alta del modelo probablemente refleja también ese vacío de datos.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02173691](https://clinicaltrials.gov/study/NCT02173691) | Fase 3 | Completado | 584 | Tiotropio vs. salmeterol vs. placebo durante 6 meses en EPOC; salmeterol es un brazo directo |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Fase 3 | Completado | 741 | Arformoterol en EPOC; doble ciego, controlado con placebo y control activo, 12 semanas |
| [NCT01110200](https://clinicaltrials.gov/study/NCT01110200) | Fase 4 | Completado | 639 | Fluticasona/salmeterol vs. salmeterol solo sobre exacerbaciones de EPOC tras hospitalización |
| [NCT00857766](https://clinicaltrials.gov/study/NCT00857766) | Fase 4 | Completado | 249 | Fluticasona/salmeterol vs. placebo sobre rigidez arterial en EPOC (16 semanas) |
| [NCT00403286](https://clinicaltrials.gov/study/NCT00403286) | Fase 2 | Completado | 457 | Búsqueda de dosis de fluticasona/formoterol, con Advair Diskus como referencia, en EPOC |
| [NCT00269126](https://clinicaltrials.gov/study/NCT00269126) | Fase 3 | Completado | 150 | Comparación de dos medicamentos en EPOC (18 semanas); título poco informativo |
| [NCT00268177](https://clinicaltrials.gov/study/NCT00268177) | Fase 3 | Completado | 130 | Salmeterol/fluticasona 50/500 vs. placebo sobre inflamación bronquial en EPOC (13 semanas) |
| [NCT00269087](https://clinicaltrials.gov/study/NCT00269087) | Fase 3 | Completado | 122 | Seguridad a largo plazo (56 semanas) de la combinación en EPOC (bronquitis crónica y enfisema) |
| [NCT00633217](https://clinicaltrials.gov/study/NCT00633217) | Fase 4 | Completado | 247 | Fluticasona/salmeterol en inhalador presurizado vs. Diskus en EPOC asociada a bronquitis crónica |
| [NCT01332409](https://clinicaltrials.gov/study/NCT01332409) | N/A | Completado | 2000 | Estudio poscomercialización en EPOC (bronquitis crónica/enfisema); útil solo para señales de seguridad |

*Se muestran 10 de los 16 ensayos disponibles. Varios evalúan combinaciones, por lo que no se puede aislar el efecto de salmeterol solo.*

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15970448](https://pubmed.ncbi.nlm.nih.gov/15970448/) | 2006 | Estudio clínico | Pulm Pharmacol Ther | Efecto agudo de salmeterol vs. placebo sobre el aclaramiento mucociliar y de tos en 14 pacientes con bronquitis crónica |
| [19124357](https://pubmed.ncbi.nlm.nih.gov/19124357/) | 2008 | ECA | Ther Adv Respir Dis | Seguridad y tolerancia a 12 meses de arformoterol y salmeterol en EPOC |
| [9916607](https://pubmed.ncbi.nlm.nih.gov/9916607/) | 1998 | ECA | Clin Ther | Salmeterol inhalado vs. teofilina oral en EPOC leve-moderada: eficacia, tolerabilidad y calidad de vida |
| [12970006](https://pubmed.ncbi.nlm.nih.gov/12970006/) | 2003 | ECA | Chest | Eficacia y seguridad de fluticasona 250/salmeterol 50 en Diskus frente a placebo y cada componente por separado en EPOC |
| [17196106](https://pubmed.ncbi.nlm.nih.gov/17196106/) | 2006 | Metaanálisis | Respir Res | Salmeterol 50 mcg dos veces al día frente a placebo/tratamiento habitual en EPOC |
| [19210134](https://pubmed.ncbi.nlm.nih.gov/19210134/) | 2009 | Cohorte | Curr Med Res Opin | Hospitalizaciones, visitas a urgencias y costes en bronquitis crónica con fluticasona/salmeterol frente a otros tratamientos inhalados de mantenimiento |
| [15329047](https://pubmed.ncbi.nlm.nih.gov/15329047/) | 2004 | Revisión | Drugs | Revisión de salmeterol/fluticasona en EPOC; en EE. UU. está aprobado para EPOC asociada a bronquitis crónica |
| [16915216](https://pubmed.ncbi.nlm.nih.gov/16915216/) | 2006 | Ensayo de experiencia del paciente | MedGenMed | Manejo de EPOC asociada a bronquitis crónica con fluticasona/salmeterol 250/50 |
| [32321518](https://pubmed.ncbi.nlm.nih.gov/32321518/) | 2020 | Análisis del estudio FLAME | Respir Res | Impacto de los síntomas basales y el estado de salud sobre las exacerbaciones de EPOC |

*Se muestran 9 de las 20 publicaciones disponibles.*

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 59489 | SEREVENT ACCUHALER 50 microgramos/inhalación | Polvo para inhalación |
| 83247 | SOLTEL 25 microgramos/inhalación | Suspensión para inhalación en envase a presión |
| 59675 | BETAMICAN ACCUHALER 50 microgramos/inhalación | Polvo para inhalación |
| 59490 | SEREVENT 25 microgramos/inhalación | Suspensión para inhalación en envase a presión |
| 59527 | INASPIR 25 microgramos/inhalación | Suspensión para inhalación en envase a presión |

*Se muestran 5 de las 9 autorizaciones. Los registros no incluyen texto de indicación aprobada.*

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Varios ensayos de Fase 3 completados en EPOC, incluidos brazos con salmeterol, respaldan un nivel de evidencia L1. Salmeterol ya se usa como tratamiento de mantenimiento en EPOC, del que la bronquitis crónica es un fenotipo. Por eso el valor como reposicionamiento es limitado. Además, gran parte de los ensayos usa combinaciones con fluticasona y evalúa EPOC en general, no bronquitis de forma específica.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), pendiente y bloqueante para el cribado de seguridad
- Obtener datos del mecanismo de acción desde DrugBank
- Confirmar la indicación original autorizada en España, ya que los registros no incluyen ese texto
- Revisar la evidencia específica en bronquitis crónica y separar el efecto de salmeterol del de las combinaciones con corticosteroide
- Definir un plan de seguimiento de seguridad (cardiovascular y uso concomitante con corticosteroide inhalado)

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


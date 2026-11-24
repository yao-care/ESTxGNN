---
layout: default
title: Dexrazoxane
parent: Solo predicción del modelo (L5)
nav_order: 243
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Dexrazoxane: nueva indicación predicha, Colangitis esclerosante (nivel de evidencia L5). Indicación original: No disponible en los datos de autorización compilados"
monitor_inn: "dexrazoxane"
predicted_indications: ["sclerosing cholangitis", "bronchitis", "paratyphoid fever", "conjunctivitis", "epiglottitis", "peritonitis", "laryngitis", "urinary tract infection (disease)", "pyelonephritis", "cystitis"]
---

# Dexrazoxane
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

## Dexrazoxano: De Indicación Original No Especificada a Colangitis Esclerosante
{: .text-alpha }

## Resumen en Una Frase

Dexrazoxano es un fármaco cardioprotector y quimioprotector comercializado en España (Cardioxane y Savene), cuya indicación original no figura en los datos de autorización compilados para este informe.
El modelo TxGNN predice que podría ser efectivo para **colangitis esclerosante**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de autorización compilados |
| Nueva Indicación Predicha | Colangitis esclerosante |
| Puntaje de Predicción TxGNN | 0,9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 2) |
| Número de Autorizaciones | 2 (comercializadas: 2) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Dexrazoxane (traducción no oficial): «No se comprende por completo el mecanismo por el cual el dexrazoxano ejerce su actividad citoprotectora. El dexrazoxano es un derivado cíclico del EDTA que penetra las membranas celulares. Los resultados de estudios de laboratorio sugieren que el dexrazoxano se convierte a nivel intracelular en un agente quelante de anillo abierto que interfiere con la generación de radicales libres mediada por hierro, que se considera responsable, en parte, de la miocardiopatía inducida por antraciclinas.» Texto original en inglés: "The mechanism by which dexrazoxane exerts its cytoprotective activity is not fully understood. Dexrazoxane is a cyclic derivative of EDTA that penetrates cell membranes. Results of laboratory studies suggest that dexrazoxane is converted intracellularly to a ring-opened chelating agent that interferes with iron-mediated free radical generation thought to be responsible, in part, for anthracycline-induced cardiomyopathy." ([DailyMed: dexrazoxane prescribing information, Novadoz Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a7c01089-85f5-40aa-b679-f53a425b4d68), versión del 2025-07-31; consultado el 2026-11-19). Según la información conocida, dexrazoxano es un agente quelante del hierro y modulador de la topoisomerasa II, utilizado como cardioprotector frente a la toxicidad de las antraciclinas y en el manejo de la extravasación de antraciclinas (Savene).

Una hipótesis posible, aunque **especulativa y no verificada**, es que la quelación de hierro podría reducir el daño oxidativo o dependiente del hierro en el epitelio biliar. No se ha encontrado ninguna evidencia clínica ni bibliográfica que lo confirme, y la similitud con la indicación original no ha sido evaluada. El puntaje alto del modelo (0,9999) debe interpretarse como una señal computacional, no como prueba de eficacia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 67673 | CARDIOXANE 500 mg POLVO PARA SOLUCION PARA PERFUSION | POLVO PARA SOLUCIÓN PARA PERFUSIÓN | Cnx Therapeutics Ireland Limited | Comercializada |
| 06350001 | SAVENE 20 mg/ml POLVO PARA CONCENTRADO Y DISOLVENTE PARA SOLUCION PARA PERFUSION | POLVO Y DISOLVENTE PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Cnx Therapeutics Ireland Limited | Comercializada |

Se muestran las 2 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Ambas autorizaciones son de medicamentos de principio activo único, vigentes, y pertenecen a Cnx Therapeutics Ireland Limited.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Agente quimioprotector/cardioprotector (quelante de hierro, modulador de topoisomerasa II); se utiliza junto con antineoplásicos |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Ítems de Monitoreo | Consultar las advertencias y precauciones del prospecto (en general, hemograma y función hepática y renal) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento** (no proceden del prospecto): función renal alterada y meningitis no infecciosa.
- **Interacciones farmacológicas** (19 registradas):
  - **Mayor gravedad**: vacunas de virus vivos o atenuados (sarampión, paperas, rubéola, rotavirus, viruela, fiebre amarilla, fiebre tifoidea oral, varicela zóster), BCG, y talimogén laherparepvec.
  - **Gravedad moderada**: doxorrubicina (incluida la liposomal), fumaratos (dimetilfumarato, diroximelfumarato, monometilfumarato), vacuna de adenovirus, vacuna del cólera y probióticos (*Bifidobacterium longum infantis*, *Lactobacillus acidophilus*).

No se dispone de las advertencias ni contraindicaciones del prospecto; consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para colangitis esclerosante se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y con un vínculo mecanístico meramente especulativo.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), ya que su ausencia impide el cribado de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Realizar estudios preclínicos que evalúen el efecto del dexrazoxano en modelos de daño biliar o colangitis esclerosante.
- Evaluar la seguridad en pacientes con función renal alterada y revisar las interacciones con vacunas vivas.

---

## Otras Predicciones Evaluadas

Las demás predicciones del modelo TxGNN (aprendizaje profundo) también tienen una puntuación ≥ 0,99, pero carecen de respaldo clínico:

| Enfermedad | Puntaje TxGNN | Nivel de Evidencia | Recomendación | Observación |
|------|------|------|------|------|
| Bronquitis | 0,9998 | L5 | Hold | Sin mecanismo identificable; la puntuación proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes aprendidas entre enfermedades relacionadas, no evidencia biológica |
| Fiebre paratifoidea | 0,9998 | L5 | Hold | Sin actividad antibacteriana conocida |
| Conjuntivitis | 0,9996 | L5 | Hold | Sin mecanismo plausible |
| Epiglotitis | 0,9996 | L5 | Hold | Sin mecanismo antimicrobiano |
| Peritonitis | 0,9993 | L5 | Hold | Dos publicaciones recuperadas, ninguna respalda el uso |
| Laringitis | 0,9992 | L5 | Hold | Sin mecanismo plausible |
| Infección urinaria | 0,9987 | L5 | Hold | No es antimicrobiano |
| Pielonefritis | 0,9985 | L5 | Hold | La puntuación proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes aprendidas entre enfermedades relacionadas, no evidencia biológica |
| Cistitis | 0,9982 | L4 | Pregunta de investigación | Apoyo preclínico indirecto (ferroptosis); sin datos clínicos directos; el uroprotector establecido es la mesna |

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: dexrazoxane prescribing information, Novadoz Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a7c01089-85f5-40aa-b679-f53a425b4d68) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


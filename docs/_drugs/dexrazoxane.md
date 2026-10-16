---
layout: default
title: Dexrazoxane
parent: Solo predicción del modelo (L5)
nav_order: 243
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dexrazoxane: nueva indicación predicha, Colangitis esclerosante (nivel de evidencia L5). Indicación original: No disponible en los datos de autorización compilados"
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Dexrazoxano: De Indicación Original No Especificada a Colangitis Esclerosante

## Resumen en Una Frase

Dexrazoxano es un fármaco cardioprotector y quimioprotector comercializado en España (Cardioxane y Savene), cuya indicación original no figura en los datos de autorización compilados para este informe.
El modelo TxGNN predice que podría ser efectivo para **colangitis esclerosante**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de autorización compilados |
| Nueva Indicación Predicha | Colangitis esclerosante |
| Puntaje de Predicción TxGNN | 99,99 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, dexrazoxano es un agente quelante del hierro y modulador de la topoisomerasa II, utilizado como cardioprotector frente a la toxicidad de las antraciclinas y en el manejo de la extravasación de antraciclinas (Savene).

Una hipótesis posible, aunque **especulativa y no verificada**, es que la quelación de hierro podría reducir el daño oxidativo o dependiente del hierro en el epitelio biliar. No se ha encontrado ninguna evidencia clínica ni bibliográfica que lo confirme, y la similitud con la indicación original no ha sido evaluada. El puntaje alto del modelo (99,99 %) debe interpretarse como una señal computacional, no como prueba de eficacia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 67673 | CARDIOXANE 500 mg polvo para solución para perfusión | Polvo para solución para perfusión | No especificada en los datos |
| 06350001 | SAVENE 20 mg/ml polvo para concentrado y disolvente para solución para perfusión | Polvo y disolvente para concentrado para solución para perfusión | No especificada en los datos |

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

Las demás predicciones del modelo también tienen un puntaje superior al 99,8 %, pero carecen de respaldo clínico:

| Enfermedad | Puntaje TxGNN | Nivel de Evidencia | Recomendación | Observación |
|------|------|------|------|------|
| Bronquitis | 99,98 % | L5 | Hold | Sin mecanismo identificable; probable artefacto del grafo |
| Fiebre paratifoidea | 99,98 % | L5 | Hold | Sin actividad antibacteriana conocida |
| Conjuntivitis | 99,96 % | L5 | Hold | Sin mecanismo plausible |
| Epiglotitis | 99,96 % | L5 | Hold | Sin mecanismo antimicrobiano |
| Peritonitis | 99,93 % | L5 | Hold | Dos publicaciones recuperadas, ninguna respalda el uso |
| Laringitis | 99,92 % | L5 | Hold | Sin mecanismo plausible |
| Infección urinaria | 99,87 % | L5 | Hold | No es antimicrobiano |
| Pielonefritis | 99,85 % | L5 | Hold | Probable artefacto del grafo |
| Cistitis | 99,82 % | L4 | Pregunta de investigación | Apoyo preclínico indirecto (ferroptosis); sin datos clínicos directos; el uroprotector establecido es la mesna |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


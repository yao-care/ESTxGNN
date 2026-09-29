---
layout: default
title: Bumetanide
parent: Evidencia moderada (L3-L4)
nav_order: 87
evidence_level: L4
indication_count: 1
---

# Bumetanide
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

# Bumetanida: De Edema (Insuficiencia Cardiaca, Hepática y Renal) a Enfermedad Cardiaca Pulmonar Aguda

## Resumen en Una Frase

La bumetanida es un diurético de asa, utilizado para tratar el edema asociado a insuficiencia cardiaca, enfermedad hepática y enfermedad renal.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad cardiaca pulmonar aguda (cor pulmonale agudo)**,
pero ningún ensayo ni publicación disponible estudia directamente esta indicación: hay **3 ensayos clínicos** y **5 publicaciones**, todos sobre insuficiencia cardiaca en general.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Edema asociado a insuficiencia cardiaca, enfermedad hepática y renal (según datos de farmacología; la ficha de AEMPS disponible no incluye texto de indicación) |
| Nueva Indicación Predicha | Enfermedad cardiaca pulmonar aguda |
| Puntaje de Predicción TxGNN | 99,58 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

La bumetanida inhibe los cotransportadores Na-K-Cl. Según los datos de farmacología, actúa sobre el cotransportador renal SLC12A1 (NKCC2) y sobre el basolateral SLC12A2 (NKCC1), y también figura asociada a GPR35. Al bloquear NKCC2 en la rama ascendente gruesa del asa de Henle, produce una natriuresis rápida y descongestión. No hay un mecanismo de acción curado en la base de datos de origen, por lo que esta explicación se basa en farmacología general.

En el cor pulmonale agudo, la sobrecarga de volumen del ventrículo derecho y la congestión sistémica pueden empeorar la función cardiaca derecha. Un diurético potente que reduzca el volumen circulante podría aliviar esa sobrecarga, y esta es la conexión que respalda la predicción.

El puntaje TxGNN es muy alto (0,996), pero es solo una predicción computacional. La evidencia humana disponible se refiere a insuficiencia cardiaca izquierda o general y a edema, no a cor pulmonale agudo. No hay ningún estudio en embolia pulmonar ni en fallo ventricular derecho asociado a SDRA.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT07375212](https://clinicaltrials.gov/study/NCT07375212) | Fase 4 | Retirado | 0 | Dosis única de 4 mg de bumetanida intranasal para medir su efecto sobre la presión arterial pulmonar y el volumen sanguíneo en pacientes con insuficiencia cardiaca y dispositivo implantado (CardioMEMS/Cordella). Directamente relevante, pero sin participantes ni datos. |
| [NCT05580510](https://clinicaltrials.gov/study/NCT05580510) | Fase 2/3 | Desconocido | 160 | Empagliflozina y sacubitrilo/valsartán en insuficiencia cardiaca con fracción de eyección reducida asociada a cardiopatía congénita del adulto. No evalúa bumetanida. |
| [NCT06885164](https://clinicaltrials.gov/study/NCT06885164) | N/A | Reclutando | 200 | Monitorización sismocardiográfica en insuficiencia cardiaca. Estudio no intervencionista, sin evidencia de eficacia. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3304383](https://pubmed.ncbi.nlm.nih.gov/3304383/) | 1987 | Estudio hemodinámico clínico | Br J Clin Pharmacol | En 24 pacientes con enfermedad coronaria e insuficiencia cardiaca aguda (inducida por esfuerzo) o crónica, la bumetanida i.v. redujo el índice cardiaco y la presión de oclusión de la arteria pulmonar, y aumentó la presión arterial y la resistencia vascular sistémica. |
| [6391889](https://pubmed.ncbi.nlm.nih.gov/6391889/) | 1984 | Revisión | Drugs | Revisión farmacodinámica y farmacocinética. Describe su uso en edema por insuficiencia cardiaca congestiva, enfermedad hepática y renal, y congestión pulmonar aguda, con diuresis rápida (en 30 minutos) que dura de 3 a 6 horas. |
| [19142155](https://pubmed.ncbi.nlm.nih.gov/19142155/) | 2009 | Revisión | Am J Ther | Revisión del manejo de la insuficiencia cardiaca aguda y las opciones diuréticas, con resultados de ensayos recientes. |
| [19843838](https://pubmed.ncbi.nlm.nih.gov/19843838/) | 2009 | Revisión | Ann Pharmacother | Revisión comparativa de diuréticos de asa (farmacocinética, seguridad, eficacia y costes) que cuestiona si la furosemida debe ser de primera línea. |
| [39366035](https://pubmed.ncbi.nlm.nih.gov/39366035/) | 2024 | Cohorte/Epidemiología | Am J Emerg Med | Epidemiología de las consultas por insuficiencia cardiaca en urgencias de EE. UU. (2016-2023). Contexto general, sin relación directa con bumetanida. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 52047 | FORDIURAN 1 mg COMPRIMIDOS | Comprimido | No especificada en los datos disponibles |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es mecanísticamente plausible, pero la evidencia es solo de nivel L4: no hay ningún estudio de bumetanida en cor pulmonale agudo. El único ensayo con el fármaco directamente implicado fue retirado sin participantes, y la literatura se refiere a insuficiencia cardiaca general.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS (advertencias y contraindicaciones), cuya ausencia bloquea el cribado de seguridad.
- Completar los datos curados de mecanismo de acción desde DrugBank.
- Buscar estudios específicos en cor pulmonale agudo, embolia pulmonar o fallo ventricular derecho.
- Evaluar la seguridad de la diuresis intensa en una situación de precarga dependiente del ventrículo derecho.
- Definir la compatibilidad de vía de administración (oral frente a intravenosa en el contexto agudo), aún pendiente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Bumetanide
parent: Evidencia moderada (L3-L4)
nav_order: 123
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Bumetanide: nueva indicación predicha, Enfermedad cardiaca pulmonar aguda (nivel de evidencia L4). Indicación original: Insuficiencia cardiaca congestiva (según el grafo de conocimiento"
monitor_inn: "Bumetanide"
predicted_indications: ["acute pulmonary heart disease"]
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

# Bumetanida: De Insuficiencia Cardiaca Congestiva a Enfermedad Cardiaca Pulmonar Aguda

## Resumen en Una Frase

Bumetanida es un diurético de asa, utilizado originalmente para el tratamiento de la insuficiencia cardiaca congestiva y los edemas asociados.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad cardiaca pulmonar aguda (cor pulmonale agudo)**,
pero actualmente solo cuenta con **0 ensayos clínicos** y **5 publicaciones** de apoyo indirecto (sobre insuficiencia cardiaca y diuréticos en general, no específicas de esta indicación).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Insuficiencia cardiaca congestiva (según el grafo de conocimiento; el texto de indicación de la autorización en España no está disponible) |
| Nueva Indicación Predicha | Enfermedad cardiaca pulmonar aguda |
| Puntaje de Predicción TxGNN | 99,58% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

La bumetanida es un diurético de asa potente que inhibe el cotransportador Na-K-2Cl (NKCC2, codificado por SLC12A1) en la rama ascendente gruesa del asa de Henle, lo que produce una natriuresis y diuresis rápidas. Los datos compilados también muestran interacción farmacológica con el cotransportador basolateral NKCC1 (SLC12A2) y con el receptor GPR35. No se dispone de un campo detallado de mecanismo de acción en DrugBank, por lo que esta descripción se basa en la información farmacológica disponible.

La insuficiencia cardiaca congestiva y el cor pulmonale agudo comparten un elemento fisiopatológico: la sobrecarga de volumen y la congestión venosa sistémica. En el cor pulmonale agudo, la sobrecarga del ventrículo derecho puede aliviarse mediante la descongestión, por lo que el vínculo es plausible y coherente con el uso aprobado en insuficiencia cardiaca y edema.

Es necesario ser prudente: la evidencia es indirecta y se refiere a insuficiencia cardiaca aguda y crónica en general, no al cor pulmonale agudo. Además, una reducción excesiva de la precarga puede empeorar el llenado del ventrículo derecho y el gasto cardiaco, de modo que el beneficio depende del estado volémico. El puntaje elevado de TxGNN (0,996) es una predicción computacional y probablemente refleja la gran similitud con la indicación existente de insuficiencia cardiaca.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3304383](https://pubmed.ncbi.nlm.nih.gov/3304383/) | 1987 | Estudio hemodinámico clínico (pequeño, mecanístico) | Br J Clin Pharmacol | Con bumetanida i.v. en 24 pacientes con enfermedad coronaria e insuficiencia cardiaca aguda o crónica, disminuyeron el índice cardiaco y la presión de oclusión de la arteria pulmonar |
| [6391889](https://pubmed.ncbi.nlm.nih.gov/6391889/) | 1984 | Revisión | Drugs | Propiedades farmacodinámicas y farmacocinéticas de la bumetanida; uso en edema por insuficiencia cardiaca, enfermedad hepática y renal, y congestión pulmonar aguda |
| [19142155](https://pubmed.ncbi.nlm.nih.gov/19142155/) | 2009 | Revisión | Am J Ther | Manejo de la insuficiencia cardiaca aguda; la mayoría de los pacientes se controla con diuréticos |
| [19843838](https://pubmed.ncbi.nlm.nih.gov/19843838/) | 2009 | Revisión | Ann Pharmacother | Comparación de perfiles farmacocinéticos, seguridad, eficacia y costes de los diuréticos de asa |
| [39366035](https://pubmed.ncbi.nlm.nih.gov/39366035/) | 2024 | Epidemiología / Cohorte | Am J Emerg Med | Presentaciones de insuficiencia cardiaca en urgencias de EE. UU. (2016-2023); no es específico del fármaco |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 52047 | FORDIURAN 1 mg COMPRIMIDOS | Comprimido | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no del prospecto)**: enfermedad hepática, coma hepático y encefalopatía hepática, enfermedad de la vesícula biliar, trombocitopenia, deficiencia de potasio, diabetes mellitus, cetoacidosis diabética, hiperuricemia, anuria, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, trastornos de la audición y enfermedades del sistema auditivo.
- **Interacciones farmacológicas**: la consulta se completó y devolvió 3 resultados, todos de farmacología de dianas (no interacciones con otros fármacos): GPR35, cotransportador Na-K-Cl específico del riñón (SLC12A1) y cotransportador Na-K-Cl basolateral (SLC12A2). No se identificaron interacciones con otros medicamentos.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto de la AEMPS.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo y en evidencia indirecta (nivel L4): no hay ensayos clínicos y la literatura trata de insuficiencia cardiaca en general, no de cor pulmonale agudo. Además, la reducción de la precarga podría ser perjudicial en el ventrículo derecho según el estado volémico.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada), ya que su ausencia impide completar el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar estudios específicos de diuréticos de asa en cor pulmonale agudo o en disfunción aguda del ventrículo derecho.
- Definir la población y el estado volémico en que el beneficio superaría el riesgo, y valorar un estudio exploratorio de fase 2 si la revisión es favorable.
- Evaluar la compatibilidad de vías de administración (la presentación comercializada en España es solo en comprimidos, y el contexto agudo suele requerir vía intravenosa).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


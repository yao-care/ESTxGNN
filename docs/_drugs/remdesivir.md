---
layout: default
title: Remdesivir
parent: 僅模型預測 (L5)
nav_order: 240
evidence_level: L5
indication_count: 6
---

# Remdesivir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Remdesivir: De Uso Antiviral (COVID-19/Ébola) a Neoplasia Endocrina Múltiple

## Resumen en Una Frase

Remdesivir es un profármaco nucleotídico antiviral cuyo campo de indicación original no está formalmente registrado en este Evidence Pack (dato pendiente), aunque la evidencia asociada en la base de datos (ensayos ACTT, SIMPLE y PREVAIL IV) confirma su uso clínico establecido en COVID-19 y enfermedad por virus Ébola. El modelo TxGNN predice como candidato principal la **Neoplasia Endocrina Múltiple**, con un score de **99.50%**, pero **sin ningún ensayo clínico ni publicación** que respalde esta dirección. La evidencia disponible es, por tanto, mínima y la propia justificación del modelo la califica como una predicción de baja plausibilidad mecanística.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en licencias españolas (fármaco no comercializado); evidencia contextual indica uso como antiviral en COVID-19/Ébola |
| Nueva Indicación Predicha | Neoplasia Endocrina Múltiple (Multiple Endocrine Neoplasia) |
| Puntaje de Predicción TxGNN | 99.50% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción (MOA) de Remdesivir a nivel de ficha de fármaco (data gap de severidad Alta). No obstante, a partir de la evidencia clínica recogida en este mismo Evidence Pack se puede reconstruir que Remdesivir es un profármaco análogo de nucleótido de adenosina que, tras activación metabólica, inhibe la ARN polimerasa dependiente de ARN (RdRp) viral — el mecanismo por el cual ha demostrado actividad frente al virus Ébola y al SARS-CoV-2 en múltiples ensayos de Fase 3 (ACTT-1, SIMPLE, PREVAIL IV).

La Neoplasia Endocrina Múltiple (MEN), en cambio, es un síndrome tumoral endocrino hereditario causado por mutaciones germinales en genes como *RET* (proto-oncogén) o *MEN1* (supresor tumoral). No existe ningún solapamiento mecanístico conocido entre la inhibición de la RdRp viral y la tumorigénesis endocrina asociada a estas vías genéticas. Según la propia justificación generada para esta predicción, se trata muy probablemente de una asociación producida por proximidad estructural o topológica en el grafo de conocimiento del modelo, no por una relación biológica real.

En consecuencia, aunque el score numérico de TxGNN es elevado (99.50%), la ausencia total de evidencia clínica o preclínica de respaldo, combinada con la falta de plausibilidad mecanística, hace que esta predicción deba tratarse como **especulativa y de baja confianza**.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

> Nota: la ficha técnica/prospecto de TFDA-AEMPS para este fármaco no ha podido incorporarse a este análisis (data gap de severidad **Bloqueante**), lo que impide actualmente completar la evaluación de seguridad inicial (etapa S1) para cualquiera de las indicaciones propuestas.

---

## Otras Indicaciones Evaluadas

Este Evidence Pack analizó un total de 6 indicaciones candidatas para Remdesivir. Ninguna alcanzó un nivel de evidencia suficiente para avanzar; todas quedan en **Hold**:

| Rank | Indicación | Score TxGNN | Nivel de Evidencia | Decisión | Nota clave |
|------|-----------|-------------|---------------------|----------|------------|
| 2 | Infección por VIH | 99.32% | L4 | Hold | 23 ensayos y 20 artículos recuperados, pero la mayoría corresponden en realidad a COVID-19 (ACTT/SIMPLE) o Ébola (PREVAIL IV); solo 1 artículo menciona VIH, y es una revisión de comorbilidad, no de eficacia. Mecanísticamente, Remdesivir inhibe la RdRp, no la transcriptasa inversa que usa el VIH para replicarse. |
| 3 | Síndrome de inmunodeficiencia felina (FIV) | 99.07% | L5 | Hold | Sin ensayos ni literatura; indicación veterinaria, sin ruta de desarrollo humano aplicable. |
| 4 | Infección por virus de inmunodeficiencia de simios (SIV) | 99.07% | L5 | Hold | Score idéntico a FIV, lo que sugiere que el modelo agrupó ambas por cercanía en el grafo (familia Lentivirus) más que por aprendizaje independiente. |
| 5 | Trastorno del neurodesarrollo (marcha atáxica, ausencia de habla, sustancia blanca reducida) | 99.03% | L5 | Hold | Enfermedad monogénica rara sin relación conocida con mecanismos antivirales. |
| 6 | Hipercolesterolemia familiar homocigota | 99.03% | L5 | Hold | Trastorno del metabolismo lipídico (vía LDLR/APOB/PCSK9) sin relación con la inhibición de RdRp viral. |

**Hallazgo relevante:** la indicación con mayor volumen de evidencia bruta (VIH, rank 2) es también la que presenta el riesgo más claro de **error de etiquetado/asociación** entre ensayos de COVID-19 y la etiqueta de enfermedad "HIV infectious disease". Esto sugiere una posible limitación en el pipeline de vinculación ensayo-enfermedad que debería revisarse antes de confiar en el volumen de evidencia como proxy de relevancia.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ninguna de las 6 indicaciones predichas por TxGNN para Remdesivir alcanza un nivel de evidencia igual o superior a L3. La indicación de mayor score (Neoplasia Endocrina Múltiple) carece por completo de respaldo clínico o mecanístico. La indicación con mayor volumen documental (VIH) presenta indicios de error de etiquetado de datos, ya que la evidencia recuperada corresponde mayoritariamente a COVID-19 y Ébola, no a VIH. Además, la ausencia del prospecto TFDA/AEMPS constituye un gap bloqueante que impide iniciar la evaluación de seguridad (S1) para cualquier indicación.

**Para avanzar se necesita:**
- Completar los datos de mecanismo de acción (MOA) a nivel de ficha de fármaco (gap de severidad Alta)
- Obtener el prospecto/ficha técnica de TFDA-AEMPS para desbloquear la evaluación de seguridad S1 (gap de severidad Bloqueante)
- Auditar y corregir la vinculación ensayo-enfermedad para la etiqueta "VIH infectious disease", dado el fuerte indicio de contaminación con ensayos de COVID-19/Ébola
- Buscar evidencia mecanística o preclínica real que conecte Remdesivir con neoplasia endocrina múltiple, VIH, FIV, SIV, el trastorno del neurodesarrollo descrito o la hipercolesterolemia familiar homocigota antes de asignar recursos adicionales a esta candidatura
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


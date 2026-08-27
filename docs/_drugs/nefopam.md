---
layout: default
title: Nefopam
parent: 僅模型預測 (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
---

# Nefopam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Nefopam: De Dolor Postoperatorio a Estenosis del Canal Lumbar

## Resumen en Una Frase

Nefopam es un analgésico no opioide y no-AINE de acción central (inhibidor de la recaptación de monoaminas), utilizado clínicamente como coadyuvante en el manejo del dolor postoperatorio. El modelo TxGNN predice múltiples indicaciones nuevas, pero solo una —**Estenosis del Canal Lumbar**— cuenta con respaldo real: **4 publicaciones**, incluyendo **2 ensayos clínicos aleatorizados (ECA)**, mientras que las 9 predicciones de mayor puntaje (subtipos de cataratas) carecen de todo respaldo clínico o mecanístico y están señaladas en los propios datos como probable artefacto del modelo.

> **Nota metodológica:** Las predicciones rank 1–9 (todas variantes de "catarata": craniostenosis cataract, immature/mature/senile/diabetic cataract, etc.) comparten un puntaje TxGNN casi idéntico (~0.9998) sin ningún ensayo clínico ni literatura de soporte, y el propio *repurposing_rationale* las describe explícitamente como "群聚偽陽性" (falso positivo por agrupamiento de embeddings), sin conexión mecanística conocida con nefopam. Por transparencia, no se descartan de los datos originales, pero este informe se centra en la predicción rank 10 (Estenosis del Canal Lumbar), que es la única con evidencia clínica verificable.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Analgésico no opioide de acción central (manejo del dolor postoperatorio) — sin indicación oficial registrada en la fuente de datos de España |
| Nueva Indicación Predicha | Estenosis del Canal Lumbar (Lumbar Spinal Stenosis) |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) de nefopam en esta fuente. Según la información disponible en la propia evidencia recopilada, nefopam es un analgésico no opioide y no-AINE de acción central que actúa inhibiendo la recaptación de monoaminas (mecanismo similar a orfenadrina), y se utiliza clínicamente como parte de esquemas de analgesia multimodal y ahorro de opioides ("opioid-sparing") tras cirugías de columna.

La relación con la estenosis del canal lumbar no es de tratamiento directo de la patología estructural, sino de **manejo perioperatorio del dolor** en pacientes sometidos a cirugía de descompresión lumbar. Es importante señalar este matiz: la evidencia respalda a nefopam como coadyuvante analgésico en el contexto quirúrgico de esta enfermedad, no como tratamiento causal de la estenosis en sí.

En contraste, las nueve predicciones de mayor puntaje del modelo (todas relacionadas con cataratas) no tienen ninguna base mecanística plausible —no existe relación conocida entre un analgésico central y la patología del cristalino— y ni ensayos clínicos ni literatura las respaldan, lo que refuerza la interpretación de que se trata de un artefacto estadístico del modelo más que de una señal biológica real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados (no se identificaron entradas en ClinicalTrials.gov ni ICTRP para esta combinación fármaco-indicación). La evidencia disponible proviene de ensayos publicados directamente en la literatura (ver tabla siguiente).

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38068520](https://pubmed.ncbi.nlm.nih.gov/38068520/) | 2023 | ECA | Journal of Clinical Medicine | ECA doble ciego (n=73) en cirugía por estenosis del canal lumbar: nefopam 20 mg reduce disestesia postoperatoria, dolor y mejora la satisfacción del paciente frente a control con suero salino |
| [41937571](https://pubmed.ncbi.nlm.nih.gov/41937571/) | 2026 | ECA | Asian Spine Journal | ECA doble ciego controlado con placebo: nefopam intravenoso continuo postoperatorio reduce el consumo de opioides en fusión lumbar degenerativa multinivel |
| [31166320](https://pubmed.ncbi.nlm.nih.gov/31166320/) | 2019 | Estudio de cohorte/comparativo | Zhurnal Voprosy Neirokhirurgii im. N.N. Burdenko | Evalúa distintos esquemas de analgesia multimodal perioperatoria (incluye nefopam) sobre la tasa de síndrome de cirugía de espalda fallida en pacientes con estenosis del canal |
| [25535527](https://pubmed.ncbi.nlm.nih.gov/25535527/) | 2014 | Reporte de caso (señal de seguridad: estado epiléptico) | Journal of Korean Neurosurgical Society | Varón de 71 años tras cirugía por estenosis del canal lumbar que presentó estado epiléptico atribuido a nefopam, administrado junto a otros analgésicos; señal de seguridad neurológica relevante |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad — no se dispone de advertencias, contraindicaciones ni interacciones farmacológicas (DDI) estructuradas para nefopam en esta fuente de datos.

**Señal adicional relevante detectada en la literatura (no proviene de la base de datos de seguridad estructurada):** el reporte de caso PMID [25535527](https://pubmed.ncbi.nlm.nih.gov/25535527/) describe estado epiléptico asociado al uso de nefopam en un paciente postquirúrgico de columna. Dado que nefopam es conocido por reacciones adversas neuropsiquiátricas (confusión, alucinaciones, convulsiones), esta señal debe evaluarse formalmente antes de cualquier avance.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Existe evidencia clínica real (2 ECAs, nivel L2) que respalda un rol de nefopam como coadyuvante analgésico y de ahorro de opioides en cirugía por estenosis del canal lumbar. Sin embargo, hay un vacío de datos **bloqueante** (DG001): no se dispone del prospecto/advertencias oficiales de la TFDA, lo que impide completar la evaluación de seguridad inicial (S1). Nefopam tampoco está comercializado en España (0 autorizaciones), y la literatura reporta una señal de seguridad neurológica grave (estado epiléptico) que requiere caracterización formal antes de proceder.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica oficial (TFDA y/o AEMPS) con advertencias y contraindicaciones — actualmente bloqueante
- Confirmar el mecanismo de acción (MOA) detallado vía DrugBank u otra fuente farmacológica
- Evaluar formalmente la señal de convulsiones/estado epiléptico reportada en la literatura
- Definir la vía regulatoria para introducción en España, dado que el fármaco no está actualmente comercializado
- Reevaluar y, de ser posible, filtrar del pipeline las predicciones de tipo "catarata" (rank 1–9), ya señaladas como probable artefacto de agrupamiento del modelo sin soporte clínico
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


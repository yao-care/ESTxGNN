---
layout: default
title: Etelcalcetide
parent: Evidencia moderada (L3-L4)
nav_order: 216
evidence_level: L4
indication_count: 4
---

# Etelcalcetide
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **4** 
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

# Etelcalcetida: De Hiperparatiroidismo Secundario a Hiperfosfatemia

## Resumen en Una Frase

Etelcalcetida es un calcimimético intravenoso, utilizado originalmente para tratar el hiperparatiroidismo secundario en pacientes con enfermedad renal crónica (ERC) en hemodiálisis.
El modelo TxGNN predice que podría ser efectivo para **hiperfosfatemia**,
pero por ahora solo cuenta con **1 ensayo clínico** (mecanístico, sin evaluar el fosfato como resultado) y **5 publicaciones**, la mayoría indirectas.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperparatiroidismo secundario en ERC en hemodiálisis (según la información farmacológica de referencia; el registro de la AEMPS no incluye el texto de la indicación) |
| Nueva Indicación Predicha | Hiperfosfatemia |
| Puntaje de Predicción TxGNN | 99,42 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Etelcalcetida es un calcimimético que activa el receptor sensor de calcio (CaSR) en las células paratiroideas y reduce la hormona paratiroidea (PTH). Se administra por vía intravenosa al final de la sesión de hemodiálisis. El registro no aporta datos detallados del mecanismo de acción; esta descripción se basa en la información farmacológica y en la literatura disponibles.

La hiperfosfatemia y el hiperparatiroidismo secundario forman parte del mismo cuadro de alteraciones minerales y óseas de la ERC. La retención de fosfato es uno de los motores del hiperparatiroidismo secundario. Al reducir la PTH, etelcalcetida podría disminuir de forma indirecta el calcio y el fosfato séricos. Por eso la hiperfosfatemia es una indicación biológicamente cercana a la aprobada.

Conviene ser cautos: la reducción del fosfato sería un efecto secundario, no una indicación primaria ni validada. La única señal específica es un informe preclínico de 2026 (PMID 42044867), que sugiere un beneficio cardíaco mediado por CaSR en hiperfosfatemia crónica. Esa señal no equivale a evidencia clínica de que el fármaco reduzca el fosfato.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03527511](https://clinicaltrials.gov/study/NCT03527511) | N/A | Completado | 21 | Efecto de la vitamina D activa y etelcalcetida sobre osteoclastos humanos en pacientes con ERC. No evalúa la reducción de fosfato ni la hiperfosfatemia como criterio de valoración; solo aporta contexto indirecto (relevancia: C). |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33305109](https://pubmed.ncbi.nlm.nih.gov/33305109/) | 2020 | ECA | Kidney Int Rep | Ensayo DUET: eficacia de etelcalcetida intravenosa en el control del hiperparatiroidismo secundario en hemodiálisis. Respalda la indicación original, no la hiperfosfatemia. |
| [29440923](https://pubmed.ncbi.nlm.nih.gov/29440923/) | 2018 | Revisión | Int J Nephrol Renovasc Dis | Papel de etelcalcetida en el manejo del hiperparatiroidismo en hemodiálisis; reduce la PTH con dosificación tres veces por semana. |
| [42495460](https://pubmed.ncbi.nlm.nih.gov/42495460/) | 2026 | Revisión | Cureus | Revisión narrativa sobre calcimiméticos, análogos de vitamina D y captores de fosfato en el hiperparatiroidismo secundario de pacientes en diálisis. |
| [42044867](https://pubmed.ncbi.nlm.nih.gov/42044867/) | 2026 | Preclínico/Mecanístico | Kidney Int | Etelcalcetida restaura la función cardíaca en hiperfosfatemia crónica mediante la activación de CaSR-cAMP. Es la señal más directa para la nueva indicación. |
| [33211001](https://pubmed.ncbi.nlm.nih.gov/33211001/) | 2021 | Reporte de caso | Clin Nephrol | Calcificación pulmonar metastásica transitoria en un paciente con hiperparatiroidismo en diálisis peritoneal. Relevancia indirecta. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 1161142002 | PARSABIV 2,5 MG SOLUCIÓN INYECTABLE | Solución inyectable | Amgen Europe B.V. |
| 1161142006 | PARSABIV 5 MG SOLUCIÓN INYECTABLE | Solución inyectable | Amgen Europe B.V. |
| 1161142010 | PARSABIV 10 MG SOLUCIÓN INYECTABLE | Solución inyectable | Amgen Europe B.V. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es biológicamente plausible por su cercanía con el hiperparatiroidismo secundario, pero no existe ningún ensayo que evalúe el fosfato como resultado. La única señal específica es preclínica (nivel L4), y el efecto sobre el fosfato sería secundario. Las otras tres predicciones del modelo (várices esofágicas con y sin sangrado, y enfermedad varicosa) no tienen mecanismo plausible ni evidencia (L5) y deben mantenerse en Hold; las dos primeras tienen puntajes idénticos, lo que sugiere nodos casi duplicados en el grafo.

**Para avanzar se necesita:**
- Analizar datos de los ensayos existentes de etelcalcetida (por ejemplo, el DUET) para ver el efecto sobre el fosfato sérico como resultado secundario.
- Diseñar un estudio clínico que use el fosfato sérico como criterio de valoración principal.
- Obtener el prospecto de la AEMPS (advertencias y contraindicaciones) para poder hacer el cribado de seguridad.
- Completar los datos del mecanismo de acción y del texto de la indicación aprobada en el registro.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


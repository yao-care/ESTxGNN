---
layout: default
title: Etelcalcetide
parent: Evidencia moderada (L3-L4)
nav_order: 312
evidence_level: L3
indication_count: 4
last_modified_at: 2026-10-14
description: "Etelcalcetide: nueva indicación predicha, Hiperfosfatemia (nivel de evidencia L3). Indicación original: Hiperparatiroidismo (secundario…"
monitor_inn: "Etelcalcetide"
predicted_indications: ["hyperphosphatemia (disease)", "esophageal varices with bleeding", "esophageal varices without bleeding", "varicose disease"]
---

# Etelcalcetide
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **4** 
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

## Etelcalcetida: De Hiperparatiroidismo a Hiperfosfatemia
{: .text-alpha }

## Resumen en Una Frase

Etelcalcetida es un calcimimético intravenoso, originalmente utilizado para el tratamiento del hiperparatiroidismo (secundario) en pacientes con enfermedad renal crónica en hemodiálisis.
El modelo TxGNN predice que podría ser efectivo para **hiperfosfatemia**, pero actualmente no hay ensayos clínicos registrados y solo **6 publicaciones** se relacionan con esta dirección, ninguna de ellas con evidencia directa de eficacia sobre el fósforo sérico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperparatiroidismo (secundario, en enfermedad renal crónica en hemodiálisis) |
| Nueva Indicación Predicha | Hiperfosfatemia |
| Puntaje de Predicción TxGNN | 0.9942 |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | Comercializado (registros vigentes: 3 de 3) |
| Número de Autorizaciones | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, etelcalcetida es un calcimimético que activa el receptor sensor de calcio (CaSR, gen *CASR*) de la glándula paratiroides y reduce la hormona paratiroidea (PTH). Su eficacia en el hiperparatiroidismo secundario de pacientes en hemodiálisis está comprobada y fue aprobada por la EMA en 2016 y por la FDA en 2017.

La relación con la hiperfosfatemia es sobre todo indirecta. Al reducir la PTH, puede disminuir el recambio óseo y la liberación de minerales, y podría bajar de forma modesta el fósforo sérico y el producto calcio-fósforo. No es un mecanismo de quelación ni de excreción de fosfato.

La hiperfosfatemia suele ser una comorbilidad de la misma población (pacientes en diálisis), por lo que la señal de TxGNN probablemente refleja la coocurrencia de enfermedades y no una indicación realmente nueva. Un estudio preclínico de 2026 sugiere además un beneficio cardíaco mediado por CaSR en hiperfosfatemia crónica, lo cual es un hallazgo mecanístico y no una prueba de eficacia sobre el fósforo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33305109](https://pubmed.ncbi.nlm.nih.gov/33305109/) | 2020 | ECA | Kidney Int Rep | Ensayo DUET: eficacia de etelcalcetida en pacientes en hemodiálisis con hiperparatiroidismo secundario; no se puede confirmar que evalúe resultados sobre fósforo |
| [29440923](https://pubmed.ncbi.nlm.nih.gov/29440923/) | 2018 | Revisión | Int J Nephrol Renovasc Dis | Papel de etelcalcetida en el manejo del hiperparatiroidismo en hemodiálisis; reduce la PTH con administración intravenosa tres veces por semana |
| [42495460](https://pubmed.ncbi.nlm.nih.gov/42495460/) | 2026 | Revisión narrativa | Cureus | Revisión del manejo farmacológico del hiperparatiroidismo secundario en diálisis (calcimiméticos, análogos de vitamina D y quelantes de fosfato) |
| [42044867](https://pubmed.ncbi.nlm.nih.gov/42044867/) | 2026 | Preclínico/mecanístico | Kidney Int | Etelcalcetida restaura la función cardíaca en hiperfosfatemia crónica mediante activación de CaSR-AMPc |
| [42853437](https://pubmed.ncbi.nlm.nih.gov/42853437/) | 2026 | Reporte de caso | CEN Case Rep | Regresión de calcinosis tumoral urémica tras cambiar de cinacalcet a etelcalcetida en un paciente sin hiperfosfatemia grave |
| [33211001](https://pubmed.ncbi.nlm.nih.gov/33211001/) | 2021 | Reporte de caso | Clin Nephrol | Calcificación pulmonar metastásica temporal en un paciente con hiperparatiroidismo en diálisis peritoneal |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1161142002 | PARSABIV 2,5 MG SOLUCIÓN INYECTABLE | Solución inyectable | No disponible en los datos compilados |
| 1161142006 | PARSABIV 5 MG SOLUCIÓN INYECTABLE | Solución inyectable | No disponible en los datos compilados |
| 1161142010 | PARSABIV 10 MG SOLUCIÓN INYECTABLE | Solución inyectable | No disponible en los datos compilados |

Titular de las tres autorizaciones: Amgen Europe B.V.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó y solo se identificó una relación farmacológica de diana, con el receptor sensor de calcio (CaSR), sin nivel de gravedad asignado ni interacciones con otros fármacos.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La puntuación de TxGNN es alta (0.9942), pero no hay ensayos clínicos y la literatura se centra en el hiperparatiroidismo secundario, no en la hiperfosfatemia como indicación independiente. La señal probablemente refleja la coocurrencia de ambas enfermedades en pacientes en diálisis.

**Para avanzar se necesita:**
- Datos del mecanismo de acción detallados y verificados
- Datos de eficacia sobre el fósforo sérico como variable principal o secundaria (por ejemplo, análisis de los ensayos existentes en hemodiálisis)
- Texto de la indicación aprobada y el prospecto de la AEMPS (advertencias y contraindicaciones)
- Aclarar si la hiperfosfatemia constituiría una indicación distinta o solo un resultado secundario del control del hiperparatiroidismo secundario

*Nota: las demás predicciones (varices esofágicas con y sin sangrado, enfermedad varicosa) tienen puntuaciones altas, pero carecen de ensayos, de literatura y de un vínculo mecanístico plausible (nivel L5), por lo que no se recomiendan para avanzar.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


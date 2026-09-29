---
layout: default
title: Sotalol
parent: Solo predicción del modelo (L5)
nav_order: 499
evidence_level: L5
indication_count: 7
---

# Sotalol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Sotalol: De Antiarrítmico a Síndrome del Seno Enfermo Autosómico Dominante Tipo 2

## Resumen en Una Frase

Sotalol es un antiarrítmico que combina el bloqueo de canales de potasio (IKr) con el bloqueo beta no selectivo. La ficha de la AEMPS incluida en el paquete no aporta el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **síndrome del seno enfermo autosómico dominante tipo 2**, pero esta predicción tiene **0 ensayos clínicos** y **0 publicaciones** que la respalden.
Además, mecanísticamente es más probable una señal de falso positivo o de contraindicación que un efecto terapéutico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en las autorizaciones de la AEMPS del paquete (uso antiarrítmico según el mecanismo descrito) |
| Nueva Indicación Predicha | Síndrome del seno enfermo autosómico dominante tipo 2 |
| Puntaje de Predicción TxGNN | 99.76% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados de mecanismo de acción en DrugBank. Según el análisis del paquete, sotalol bloquea los canales de potasio IKr (efecto de clase III) y bloquea de forma no selectiva los receptores beta-adrenérgicos. Ambos efectos enlentecen la frecuencia sinusal y la conducción auriculoventricular.

Esta enfermedad (disfunción del nodo sinusal ligada a HCN4) se caracteriza por bradicardia. Por eso se espera que sotalol la **empeore**, y en general está contraindicado en el síndrome del seno enfermo sin marcapasos. El puntaje alto del grafo probablemente refleja la cercanía entre canales iónicos y conducción cardíaca en el grafo de conocimiento, no un efecto terapéutico. Esta predicción debe tratarse como un probable falso positivo o como una señal de contraindicación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Otras Predicciones del Modelo (Contexto)

Solo dos de las siete predicciones tienen algún soporte documental, y ninguna demuestra beneficio terapéutico.

| # | Indicación predicha | Puntaje | Nivel | Recomendación |
|---|---|---|---|---|
| 2 | Síndrome de Wildervanck | 99.65% | L5 | Hold (sin mecanismo plausible) |
| 3 | Sarcoglicanopatía | 99.64% | L5 | Hold (la inotropía negativa y el riesgo proarrítmico preocupan en miocardiopatía) |
| 4 | Trastorno de ictus (*stroke disorder*) | 99.44% | L4 | Pregunta de investigación |
| 5 | Trastorno afectivo bipolar maníaco | 99.43% | L4 | Hold (la literatura trata de seguridad cardíaca, no de eficacia) |
| 6 | Macrocefalia, rasgos dismórficos y retraso psicomotor | 99.42% | L5 | Hold (sin mecanismo plausible) |
| 7 | Susceptibilidad a ictus isquémico (obsoleto) | 99.23% | L5 | Hold (término obsoleto, evaluar junto con el ictus) |

**Ictus (la predicción con más soporte):** el vínculo es solo indirecto, a través de la fibrilación auricular (FA), que es un factor de riesgo de ictus cardioembólico. Se recuperaron 22 ensayos y 20 publicaciones. Todos evalúan endpoints de FA (mantenimiento del ritmo, recurrencia, hospitalización, seguridad), no la prevención de ictus. Ningún estudio muestra que sotalol reduzca la incidencia de ictus. Los más relevantes son:

| Referencia | Diseño | Hallazgo principal |
|---|---|---|
| [NCT00007605](https://clinicaltrials.gov/study/NCT00007605) | Fase 3, completado, n=706 | Sotalol vs amiodarona para mantener el ritmo sinusal en FA; el endpoint no es ictus |
| [NCT05279833](https://clinicaltrials.gov/study/NCT05279833) | Revisión sistemática/metanálisis en red, completado | Seguridad de dronedarona vs sotalol en FA |
| [NCT02145546](https://clinicaltrials.gov/study/NCT02145546) | Fase 4, estado desconocido, n=600 | Antiarrítmicos (amiodarona, sotalol, propafenona) para prevenir FA en pacientes con síndrome del seno enfermo con marcapasos |
| [PMID 37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | Cohorte, 2023, *Circ Arrhythm Electrophysiol* | Dronedarona vs sotalol en veteranos con FA sin tratamiento antiarrítmico previo |
| [PMID 9576159](https://pubmed.ncbi.nlm.nih.gov/9576159/) | ECA doble ciego, 1998, *Am J Cardiol* | Amiodarona a dosis bajas vs sotalol para suprimir la FA sintomática recurrente |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 89413 | SOTALOL SANDOZ 80 MG COMPRIMIDOS EFG | Comprimido | Sandoz Farmacéutica S.A. |
| 62001 | SOTAPOR 80 mg COMPRIMIDOS | Comprimido | Cheplapharm Arzneimittel GmbH |

## Consideraciones de Seguridad

- **Contraindicación relevante para esta predicción:** sotalol es en general contraindicado en el síndrome del seno enfermo sin marcapasos, porque puede agravar la bradicardia.
- **Riesgos generales del fármaco (según el análisis del paquete):** prolongación del QT, riesgo de torsades de pointes y necesidad de ajustar la dosis según la función renal.
- **Interacciones farmacológicas:** no se encontraron registros de interacciones en la consulta realizada. La literatura recuperada señala un efecto aditivo sobre el QT con antipsicóticos.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal no tiene ensayos ni literatura (L5), y el mecanismo del fármaco sugiere que empeoraría la enfermedad, por lo que probablemente es un artefacto del grafo o una señal de contraindicación. Ninguna de las demás predicciones demuestra beneficio terapéutico. El ictus queda solo como pregunta de investigación indirecta, a través de la FA.

**Para avanzar se necesita:**
- Descartar formalmente la predicción de síndrome del seno enfermo como falso positivo y registrarla como señal de contraindicación.
- Si se quiere explorar el ictus, formular la pregunta de si el control del ritmo con sotalol modifica los resultados de ictus frente a alternativas, con datos que midan ese desenlace.
- Obtener el prospecto de la AEMPS (indicaciones, advertencias y contraindicaciones) para completar el cribado de seguridad.
- Completar los datos de mecanismo de acción desde DrugBank.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


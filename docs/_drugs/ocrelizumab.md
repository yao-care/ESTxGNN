---
layout: default
title: Ocrelizumab
parent: Solo predicción del modelo (L5)
nav_order: 580
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Ocrelizumab: nueva indicación predicha, Carcinoma de mama HER2 positivo (nivel de evidencia L5). Indicación original: Esclerosis múltiple progresiva (según el grafo de conocimiento"
---

# Ocrelizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Ocrelizumab: De Esclerosis Múltiple Progresiva a Carcinoma de Mama HER2 Positivo

## Resumen en Una Frase

Ocrelizumab es un anticuerpo monoclonal humanizado anti-CD20, utilizado originalmente para el tratamiento de la esclerosis múltiple progresiva.
El modelo TxGNN predice que podría ser efectivo para el **carcinoma de mama HER2 positivo**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta indicación, por lo que se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Esclerosis múltiple progresiva (según el grafo de conocimiento; el texto de indicación autorizado en España no está disponible) |
| Nueva Indicación Predicha | Carcinoma de mama HER2 positivo |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, ocrelizumab es un anticuerpo monoclonal humanizado que se une al antígeno CD20 y depleciona selectivamente los linfocitos B CD20+. Su eficacia en la esclerosis múltiple recurrente y primaria progresiva ha sido demostrada en los ensayos OPERA I/II y ORATORIO.

La relación entre la indicación original y la nueva es débil. La esclerosis múltiple es una enfermedad autoinmune mediada en parte por linfocitos B, mientras que el cáncer de mama HER2 positivo está impulsado por la señalización del receptor HER2 en las células epiteliales tumorales. Los datos compilados no respaldan ningún vínculo mecanístico directo entre la depleción de linfocitos B y este tumor.

El puntaje elevado (0.9989) refleja una inferencia basada en el grafo de conocimiento y no está respaldado por estudios reales. La única conexión teórica sería la biología de los linfocitos B infiltrantes de tumores, que es especulativa. Las demás predicciones del modelo (subtipos de mama similar a normal, receptor de progesterona positivo/negativo y luminal A/B) presentan el mismo nivel de evidencia L5 y recomendación Hold.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Para la indicación principal (carcinoma de mama HER2 positivo) actualmente no hay literatura relacionada disponible.

Para la cuarta predicción (tumor de mama luminal A o B) se recuperaron 18 publicaciones, pero tratan casi exclusivamente de ocrelizumab en esclerosis múltiple (por ejemplo, OPERA I/II, ORATORIO, OCARINA II), terapias anti-CD20 y otras enfermedades autoinmunes. Ninguna aborda el cáncer de mama, por lo que no constituyen evidencia para una indicación oncológica y no se listan como respaldo.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1171231001 | OCREVUS 300 MG CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN (Roche Registration GmbH) | Concentrado para solución para perfusión | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (100 interacciones registradas; se muestran las principales):
  - **Moderadas**: corticosteroides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona), radiofármacos y anticuerpos radiomarcados (iobenguano I-131, ibritumomab tiuxetán, tositumomab, samario-153 lexidronam), albendazol, pentamidina y levamisol.
  - **Leves**: sales de zinc (sulfato, acetato, gluconato, cloruro).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura específica, y no existe un vínculo mecanístico plausible entre la depleción de linfocitos B CD20+ y el cáncer de mama HER2 positivo, el cual ya cuenta con terapias dirigidas establecidas.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y análisis del papel de los linfocitos B en el microambiente tumoral mamario
- Estudios preclínicos que respalden la hipótesis
- Revisión sistemática de la literatura específica sobre anti-CD20 y cáncer de mama
- Advertencias y contraindicaciones del prospecto de AEMPS (pendientes de obtener)
- Evaluación de la seguridad, en particular el riesgo de infecciones e hipogammaglobulinemia, en pacientes oncológicos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


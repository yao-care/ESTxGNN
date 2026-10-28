---
layout: default
title: Phenazopyridine
parent: Solo predicción del modelo (L5)
nav_order: 630
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Phenazopyridine: nueva indicación predicha, Bronquitis (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (las autorizaciones no incluyen…"
monitor_inn: "phenazopyridine"
predicted_indications: ["bronchitis"]
---

# Phenazopyridine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Fenazopiridina: De Indicación Original No Registrada a Bronquitis
{: .text-alpha }

## Resumen en Una Frase

Fenazopiridina es un analgésico del tracto urinario que se comercializa en España como MICTUROL SEDANTE; los datos compilados no recogen el texto de su indicación original aprobada.
El modelo TxGNN predice que podría ser efectivo para **bronquitis**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (las autorizaciones no incluyen texto de indicación) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 0.9923 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado (registros anulados: 2 de 2) |
| Número de Autorizaciones | 2 (vigentes: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la fenazopiridina es un analgésico que actúa localmente sobre la mucosa de las vías urinarias, y no hay una indicación original registrada en los datos de las autorizaciones españolas.

Con la información disponible no es posible establecer un vínculo mecanístico entre un analgésico urinario de acción local y la bronquitis, que es una afección inflamatoria de las vías respiratorias. El puntaje alto del modelo (0.9923) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; no está respaldado por estudios reales.

La predicción podría reflejar artefactos del modelo TxGNN (aprendizaje profundo), como vecinos compartidos o anotaciones genéricas de tipo analgésico o antiinflamatorio. Por ello, debe interpretarse con mucha cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 34653 | MICTUROL SEDANTE | Comprimido | No especificada |
| 938033 | MICTUROL SEDANTE FUERTE | Comprimido | No especificada |

Ambas autorizaciones están vigentes, corresponden a monofármaco y su titular es Laboratorio Farmaceutico S.I.T. S.R.L.

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (no proceden del texto del prospecto, por lo que deben verificarse): hipertensión, insuficiencia hepática y enfermedad hepática, encefalopatía hepática, enfermedad renal, porfiria, EPOC, trastornos de ansiedad, trastornos hematológicos (anemia, neutropenia, agranulocitosis, trombocitopenia), hiperplasia prostática benigna, enfermedad de la vesícula biliar, enfermedad coronaria, apnea del sueño y abuso de sustancias, entre otras.
- **Interacciones farmacológicas**: se identificaron 24 interacciones en total; las principales son:
  - **Mayores**: ácido nitroso y leflunomida.
  - **Moderadas**: naltrexona, anestésicos locales (lidocaína, benzocaína, tetracaína, oxibuprocaína, cinchocaína y cocaína), asparaginasa, pegaspargasa, brentuximab vedotina, clofarabina, idelalisib, interferón beta-1a e interferón beta-1b, y metotrexato.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no se puede sustentar un vínculo mecanístico plausible con la bronquitis. Además, faltan las advertencias y contraindicaciones del prospecto, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicación aprobada).
- Obtener datos del mecanismo de acción desde DrugBank.
- Realizar una revisión de literatura preclínica y clínica sobre fenazopiridina y afecciones respiratorias.
- Evaluar la compatibilidad de vía de administración (comprimido oral frente a una indicación respiratoria).
- Verificar si la predicción es un artefacto del modelo TxGNN (aprendizaje profundo) antes de invertir en estudios adicionales.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


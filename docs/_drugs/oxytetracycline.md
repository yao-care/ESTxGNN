---
layout: default
title: Oxytetracycline
parent: Solo predicción del modelo (L5)
nav_order: 599
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "oxytetracycline"
predicted_indications: ["chronic rhinosinusitis", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "punctate epithelial keratoconjunctivitis", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "otitis externa"]
description: "Oxytetracycline: nueva indicación predicha, Chronic rhinosinusitis (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Oxytetracycline
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Oxytetracycline: Chronic rhinosinusitis
{: .text-alpha }

## Resumen en Una Frase

Oxitetraciclina es un antibiótico de la familia de las tetraciclinas, asociado originalmente al tratamiento de infecciones bacterianas (infección urinaria, bronquitis, neumonía y conjuntivitis, entre otras). En España está autorizada solo en pomadas de uso tópico, oftálmico y ótico.
El modelo TxGNN predice que podría ser efectivo para **rinosinusitis crónica**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta indicación concreta. Se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Chronic rhinosinusitis |
| Puntaje de Predicción TxGNN | 0.9961 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 4 de 4) |
| Número de Autorizaciones | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de este fármaco en los datos compilados. Según la información conocida, la oxitetraciclina es una tetraciclina de amplio espectro. Su eficacia en infecciones bacterianas del aparato respiratorio, urinario y ocular figura entre sus indicaciones originales. Mecanísticamente podría ser aplicable a la rinosinusitis crónica.

La relación entre ambas indicaciones es plausible, aunque débil. Varias indicaciones originales son infecciones de vías respiratorias (bronquitis, faringitis, neumonía), y la rinosinusitis crónica puede tener un componente bacteriano e inflamatorio. Además, las tetraciclinas tienen propiedades antiinflamatorias y de inhibición de metaloproteinasas (MMP) que podrían ser relevantes en la inflamación sinusal.

Este razonamiento es una hipótesis. Tampoco está definida la compatibilidad de vía de administración: las presentaciones disponibles en España son pomadas, no formulaciones nasales ni sistémicas.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para rinosinusitis crónica.

**Nota sobre otra indicación predicha:** entre las predicciones secundarias, la **otitis externa** (puntaje TxGNN 0.9927) es la única con literatura. Incluye varios estudios comparativos con combinaciones tópicas de oxitetraciclina, hidrocortisona y polimixina B. Por ejemplo, un ECA de 1985 con 55 pacientes (PMID [2415098](https://pubmed.ncbi.nlm.nih.gov/2415098/)) no halló diferencias frente a framicetina/gramicidina. Un estudio de 2005 (PMID [15949095](https://pubmed.ncbi.nlm.nih.gov/15949095/)) sugiere que un esteroide solo también es eficaz. Esa indicación quedaría en nivel L3, pero la evidencia es antigua, de diseño mixto y con combinaciones, por lo que no puede atribuirse el beneficio solo al antibiótico.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 41198 | Terramicina Pomada Oftálmica Estéril | Pomada oftálmica | No consta en los datos compilados |
| 19650 | Terramicina Pomada Tópica | Pomada | No consta en los datos compilados |
| 27631 | Terracortril Pomada Tópica | Pomada | No consta en los datos compilados |
| 34053 | Terracortril Pomada Estéril Ótico-Oftálmica | Pomada ótica y oftálmica | No consta en los datos compilados |

Las cuatro autorizaciones son de Farmasierra Laboratorios S.L., están vigentes y corresponden a productos de un solo principio activo, según los datos compilados.

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación (según el grafo de conocimiento, no el texto del prospecto):** enfermedad renal, insuficiencia renal, uremia, glomerulonefritis, enfermedad hepática, enfermedad de la vesícula biliar, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal, deficiencia de G6PD, insuficiencia respiratoria, deficiencia de potasio, fibrilación auricular, bloqueo auriculoventricular, síndrome de Adams-Stokes, síndrome de Wolff-Parkinson-White, piouréter, enfermedad por depósito de glucógeno, cistinuria y galactosemia. Estas asociaciones deben verificarse con el prospecto oficial.
- **Interacciones farmacológicas:** se identificaron 144 interacciones. Entre las principales:
  - **Mayor:** vitamina A.
  - **Moderadas:** cationes polivalentes (calcio, magnesio, zinc y potasio, en distintas sales), insulinas (aspart, degludec, detemir, glargina, glulisina y humana) y amoxicilina.
  - **Menor:** manitol.
  
  Dado que las presentaciones comercializadas son tópicas, la relevancia de estas interacciones sistémicas es limitada. Sí serían importantes si se planteara una vía oral.

Para las advertencias del prospecto, consultar el prospecto de cada producto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para rinosinusitis crónica se basa solo en el modelo (nivel L5), sin ensayos ni literatura, y el mecanismo de acción original no está documentado. El fármaco está comercializado en España únicamente en pomadas, que no son adecuadas para la patología sinusal.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (consultar DrugBank).
- Advertencias y contraindicaciones oficiales de los prospectos de la AEMPS.
- Una revisión de la literatura sobre tetraciclinas (doxiciclina, por ejemplo) en rinosinusitis crónica, para valorar el efecto de clase.
- Definir una vía y formulación viable (nasal, irrigación u oral) y su perfil de seguridad.
- Valorar la otitis externa como candidata más cercana a la evidencia disponible, por su uso tópico ya establecido.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


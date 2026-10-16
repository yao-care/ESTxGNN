---
layout: default
title: Pentosan Polysulfate
parent: Solo predicción del modelo (L5)
nav_order: 623
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Pentosan Polysulfate: nueva indicación predicha, Trastorno de liberación primaria de las plaquetas (nivel de evidencia L5). Indicación original: Cistitis intersticial (según el grafo de conocimiento"
monitor_inn: "pentosan polysulfate"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease"]
---

# Pentosan Polysulfate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Polisulfato de pentosano: De Cistitis Intersticial a Trastorno de Liberación Primaria de las Plaquetas

## Resumen en Una Frase

El polisulfato de pentosano es un polisacárido sulfatado con actividad anticoagulante débil similar a la heparina, utilizado originalmente para tratar la cistitis intersticial.
El modelo TxGNN predice que podría ser efectivo para el **trastorno de liberación primaria de las plaquetas**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cistitis intersticial (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Trastorno de liberación primaria de las plaquetas |
| Puntaje de Predicción TxGNN | 99.71% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, el polisulfato de pentosano es un polisacárido sulfatado con actividad similar a la heparina (potenciación de la antitrombina y del cofactor II de la heparina, además de efectos sobre la función plaquetaria y la fibrinólisis). Su eficacia en la cistitis intersticial es la base de su uso original.

Mecanísticamente, **la predicción resulta poco plausible**. Un defecto de liberación (secreción o gránulos de almacenamiento) plaquetaria cursa con tendencia al sangrado, y un fármaco con efecto anticoagulante tipo heparina tendería a empeorarla, no a tratarla. La relación con la indicación original (una patología urinaria) es prácticamente inexistente.

La puntuación elevada probablemente refleja la proximidad en la red del grafo de conocimiento con nodos de plaquetas y coagulación, y no un mecanismo terapéutico real. Otras predicciones del modelo (trombastenia de Glanzmann y enfermedad de pseudo-von Willebrand) presentan el mismo problema: el fármaco no corrige los defectos subyacentes y podría agravar el sangrado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1171189001 | ELMIRON 100 MG CÁPSULAS DURAS | Cápsula dura | No disponible |
| 83238 | TROMBOBEN FORTE 5 MG/G CREMA | Crema | No disponible |
| 32762 | THROMBOCID 1 mg/g POMADA | Pomada | No disponible |
| 83434 | VANOLIV FORTE 5 MG/G CREMA | Crema | No disponible |
| 83435 | VANOLIV 1 MG/G CREMA | Crema | No disponible |

Nota: existen 8 autorizaciones vigentes en total (todas de principio activo único); se muestran las 5 principales. Varias de ellas son formulaciones tópicas o rectales (cremas y pomadas).

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto del prospecto)**: enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, trastornos de la coagulación sanguínea, hemofilia y trombocitopenia inducida por heparina.
- **Interacciones Farmacológicas**: se identificaron 58 interacciones, de nivel moderado en las principales listadas. Destacan los anticoagulantes y antiagregantes: ácido acetilsalicílico, warfarina, apixabán, edoxabán, betrixabán, dalteparina, clopidogrel, cilostazol, dipiridamol, abciximab, cangrelor, alteplasa, bivalirudina, defibrótido, caplacizumab y antitrombina III humana, además de ibritumomab tiuxetán y tositumomab.

Dado el perfil anticoagulante del fármaco, el riesgo de sangrado es una preocupación importante en poblaciones con trastornos plaquetarios. Para el resto de información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos y de literatura (nivel L5), y el mecanismo conocido del fármaco (efecto tipo heparina) es opuesto a lo que requeriría un defecto de liberación plaquetaria, con riesgo de agravar el sangrado.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones).
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Una revisión mecanística y de seguridad que justifique la plausibilidad biológica antes de cualquier estudio.
- Evidencia preclínica o clínica que respalde la asociación; sin ella, no se recomienda continuar.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


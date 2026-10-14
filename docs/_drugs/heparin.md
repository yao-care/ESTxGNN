---
layout: default
title: Heparin
parent: Solo predicción del modelo (L5)
nav_order: 392
evidence_level: L5
indication_count: 2
---

# Heparin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Heparina: De Embolia Pulmonar a Trombofilia por Deficiencia de Proteína C (Autosómica Recesiva)

## Resumen en Una Frase

La heparina es un anticoagulante utilizado originalmente en indicaciones como la embolia pulmonar, la coagulación intravascular diseminada y la púrpura fulminante.
El modelo TxGNN predice que podría ser efectiva para la **trombofilia por deficiencia de proteína C (autosómica recesiva)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden específicamente esta dirección; se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Embolia pulmonar (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Trombofilia por deficiencia de proteína C, autosómica recesiva |
| Puntaje de Predicción TxGNN | 99.29% |
| Nivel de Evidencia | L5 (solo predicción del modelo, sin estudios reales; el análisis preliminar lo clasificaba como L4) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la heparina potencia la actividad de la antitrombina (SERPINC1, con la que interactúa según los datos farmacológicos) e inhibe la trombina y el factor Xa. Esto reduce la formación de coágulos.

La deficiencia de proteína C genera un estado de hipercoagulabilidad, por lo que la anticoagulación con heparina podría contrarrestarlo de forma biológicamente plausible. Además, existe solapamiento con una de las indicaciones originales, la púrpura fulminante, que a menudo se asocia con deficiencia grave de proteína C.

Conviene matizar que el uso de la heparina como puente o tratamiento adyuvante en esta condición se apoya aquí solo en conocimiento general, no en la evidencia aportada. El tratamiento de reemplazo estándar es el concentrado de proteína C, y el inicio de warfarina conlleva un riesgo conocido de necrosis cutánea en estos pacientes, lo que hace relevante el solapamiento con heparina.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal predicha.

Nota: para la segunda predicción (trastorno primario de liberación plaquetaria, puntaje 99.06%) se recuperaron 20 publicaciones, pero ninguna evalúa la heparina como tratamiento de ese trastorno (tratan cirrosis, trombocitopenia inducida por heparina, tromboembolia asociada al cáncer, COVID-19, entre otros temas). Esa predicción tiene un nivel de evidencia L5, un mecanismo cuestionable (la anticoagulación podría agravar el sangrado) y también se recomienda Hold.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 58691 | Heparina Sódica Rovi 1000 UI/ml | Solución inyectable | No disponible |
| 56465 | Heparina Sódica Sala 1.000 UI/ml | Solución inyectable | No disponible |
| 58678 | Menaven 1000 UI/g Gel | Gel (tópico) | No disponible |
| 58679 | Menaven 1000 UI/g Crema | Pomada | No disponible |
| 58693 | Heparina Sódica Rovi 5000 UI/ml | Solución inyectable | No disponible |
| 56029 | Heparina Sódica Sala 5000 UI/ml | Solución inyectable | No disponible |

Hay presentaciones inyectables y tópicas (gel y crema). Las inyectables son las relevantes para una indicación sistémica como la predicha.

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto del prospecto)**:
  - Hemorrágicas y de coagulación: trombocitopenia, trombocitopenia inducida por heparina, hemofilia, trastornos de la coagulación, déficit de antitrombina III, defectos plaquetarios cualitativos, trombastenia de Glanzmann, hemorragia intracraneal e intracerebral, desprendimiento de placenta.
  - Hepáticas y digestivas: insuficiencia hepática, úlcera péptica activa, colitis ulcerosa y enfermedad inflamatoria intestinal, enfermedad de las vías biliares, ictericia obstructiva.
  - Vasculares y oculares: endocarditis infecciosa y subaguda bacteriana, retinopatía diabética e hipertensiva, enfermedades de la retina, arteriosclerosis obliterante, catarata diabética.
  - Otras: osteoporosis y osteoporosis posmenopáusica.
- **Interacciones farmacológicas**: los datos disponibles describen interacciones farmacológicas con la serpina C1 (antitrombina, SERPINC1) y con la glicoproteína Spike del coronavirus (SARS-CoV-2); no hay interacciones con otros fármacos.

Consultar el prospecto para las advertencias principales, que no están disponibles en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (99.29%) y un vínculo mecanístico plausible, pero no existe ningún ensayo clínico ni publicación que la respalde, por lo que es solo una predicción computacional. Además, el estándar de tratamiento es el concentrado de proteína C, y faltan los datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), un faltante bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisión sistemática de la literatura sobre el uso de heparina como puente o adyuvante en la deficiencia de proteína C y la púrpura fulminante neonatal.
- Evaluar la compatibilidad de vías de administración y la comparación con el concentrado de proteína C.
- Definir un plan de monitoreo de seguridad (plaquetas, riesgo de sangrado) para esta población.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


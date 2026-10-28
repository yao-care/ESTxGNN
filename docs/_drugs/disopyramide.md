---
layout: default
title: Disopyramide
parent: Solo predicción del modelo (L5)
nav_order: 257
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Disopyramide: nueva indicación predicha, Síndrome de Tourette (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (el texto de indicación de la a…"
monitor_inn: "disopyramide"
predicted_indications: ["Tourette syndrome", "attention deficit-hyperactivity disorder", "trichotillomania", "attention deficit hyperactivity disorder, inattentive type", "faciodigitogenital syndrome", "specific developmental disorder", "idiopathic neonatal atrial flutter", "chondromyxoid fibroma", "multifocal atrial tachycardia (disease)", "trigeminal nerve neoplasm"]
---

# Disopyramide
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

## Disopiramida: De Indicación Original No Especificada a Síndrome de Tourette
{: .text-alpha }

## Resumen en Una Frase

Disopiramida es un antiarrítmico de clase Ia comercializado en España (DICORYNAN 100 mg cápsulas duras); en los datos compilados no figura el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de Tourette**, pero **no existe ningún ensayo clínico ni publicación** que respalde esta dirección: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (el texto de indicación de la autorización está vacío) |
| Nueva Indicación Predicha | Síndrome de Tourette |
| Puntaje de Predicción TxGNN | 0,9986 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, disopiramida es un antiarrítmico de clase Ia: bloquea los canales de sodio y posee actividad anticolinérgica.

El síndrome de Tourette implica una disfunción de la dopamina y de los circuitos córtico-estriado-tálamo-corticales. No se ha identificado un vínculo mecanístico establecido entre ambos. El puntaje elevado procede del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; carece de respaldo clínico o bibliográfico, por lo que debe interpretarse con mucha cautela.

Otras predicciones del modelo siguen el mismo patrón. Trastorno por déficit de atención e hiperactividad (TDAH, 99,82 %), tricotilomanía (99,81 %) y otros trastornos del neurodesarrollo carecen de mecanismo plausible. Las únicas con cierta plausibilidad farmacológica indirecta, por el efecto de clase antiarrítmica, son el flutter auricular neonatal idiopático y la taquicardia auricular multifocal (nivel L4). Ninguna cuenta con evidencia directa con disopiramida.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para el síndrome de Tourette.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 52549 | DICORYNAN 100 mg CAPSULAS DURAS (Cheplapharm Arzneimittel GmbH) | Cápsula dura | No especificada en los datos disponibles |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proviene del prospecto)**: síndrome de QT largo (incluido el familiar), bloqueo auriculoventricular, miocardiopatías (incluida la hipertrófica), miocarditis, fibrilación y flutter auricular, trastornos hipotensivos, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, deficiencia de potasio, hipoglucemia, hiperplasia prostática benigna, glaucoma de ángulo cerrado, miastenia gravis y enfermedades de la unión neuromuscular.
- **Interacciones Farmacológicas**: se registraron 258 interacciones. Entre las de gravedad **mayor** figuran claritromicina, citrato de potasio y ácido picosulfúrico. Hay numerosas de gravedad moderada, entre ellas corticoesteroides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), anticolinérgicos (atropina, hioscina, glicopirronio, clidinio), anfotericina B, loperamida, aprepitant, bisacodilo, famotidina y clorpropamida. La cimetidina figura como interacción menor.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para el síndrome de Tourette se basa solo en el modelo (L5), sin ensayos ni publicaciones y sin mecanismo plausible. Además, el perfil de seguridad de la disopiramida (efectos proarrítmicos y anticolinérgicos) y su amplio número de interacciones hacen poco favorable explorar esta indicación sin un fundamento adicional.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (advertencias y contraindicaciones oficiales) y la indicación aprobada.
- Completar los datos del mecanismo de acción.
- Realizar estudios preclínicos o una revisión sistemática que justifique un vínculo con la fisiopatología del síndrome de Tourette.
- Si se desea explorar una vía con mayor plausibilidad, priorizar las arritmias auriculares (flutter auricular neonatal idiopático, taquicardia auricular multifocal), que pueden considerarse preguntas de investigación (L4), valorando antes seguridad y dosificación en la población objetivo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


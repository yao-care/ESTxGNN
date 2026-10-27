---
layout: default
title: Ivosidenib
parent: Solo predicción del modelo (L5)
nav_order: 439
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Ivosidenib: nueva indicación predicha, Poliomielitis bulbar (nivel de evidencia L5). Indicación original: Leucemia mieloide aguda (según los datos compilados"
monitor_inn: "IVOSIDENIB"
predicted_indications: ["bulbar polio"]
---

# Ivosidenib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Ivosidenib: De Leucemia Mieloide Aguda a Bulbar Polio
{: .text-alpha }

## Resumen en Una Frase

Ivosidenib es un inhibidor de la IDH1 mutada, originalmente utilizado para el tratamiento de la leucemia mieloide aguda (LMA) y sus subtipos.
El modelo TxGNN predice que podría ser efectivo para **poliomielitis bulbar**, aunque no hay **ningún ensayo clínico** ni **ninguna publicación** que respalde esta predicción.
Los datos compilados indican que el puntaje alto es probablemente un artefacto del grafo de conocimiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia mieloide aguda (según los datos compilados; el texto de indicación autorizado en AEMPS no está disponible) |
| Nueva Indicación Predicha | Poliomielitis bulbar |
| Puntaje de Predicción TxGNN | 99,31% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Ivosidenib es un inhibidor de la isocitrato deshidrogenasa 1 (IDH1) mutada. Reduce los niveles de 2-hidroxiglutarato (2-HG) y alivia el bloqueo de diferenciación en neoplasias mieloides con mutación de IDH1. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados; la descripción anterior procede del análisis mecanístico asociado a la predicción.

**En este caso, la predicción no resulta razonable desde el punto de vista biológico.** La poliomielitis bulbar es una infección viral de las neuronas motoras causada por el poliovirus, sin dependencia conocida de mutaciones de IDH1 ni de la señalización por 2-HG. No se identificó ningún vínculo mecanístico creíble con la indicación original. El puntaje elevado (0,993) se interpreta como un artefacto del grafo de conocimiento y no está respaldado por una justificación biológica.

### Otras predicciones del modelo con mayor plausibilidad

Los datos compilados incluyen dos predicciones alternativas con un vínculo indirecto plausible. Ambas son neoplasias mieloides relacionadas con tratamientos previos, cercanas a las indicaciones originales de LMA relacionada con terapia:

| Indicación predicha | Puntaje TxGNN | Nivel de Evidencia | Recomendación |
|------|------|------|------|
| LMA y síndromes mielodisplásicos relacionados con radiación | 99,26% | L4 | Pregunta de investigación |
| LMA y síndromes mielodisplásicos relacionados con agentes alquilantes | 99,26% | L4 | Pregunta de investigación |

En ambos casos, la actividad se esperaría únicamente en casos con mutación de IDH1. La evidencia es indirecta (extrapolada de las indicaciones de LMA existentes), no se aportaron ensayos ni literatura específicos, y el componente de síndrome mielodisplásico no está claramente respaldado.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1231728001 | TIBSOVO 250 mg comprimidos recubiertos con película (Les Laboratoires Servier) | Comprimido recubierto con película | No disponible en los datos compilados |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de IDH1 mutada) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

**Interacciones Farmacológicas** (se identificaron 100 interacciones en total; se muestran las de la muestra analizada):

- **Gravedad mayor:** aprepitant, claritromicina, dolasetrón, palonosetrón, cisaprida, granisetrón, levofloxacino.
- **Gravedad moderada:** famotidina, loperamida, bisacodilo, ácido picosulfúrico, polietilenglicol (3350 con electrolitos), saxagliptina, eliglustat, linagliptina, sulfato de sodio, aceite de ricino, glicerina, lactitol, lactulosa.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para poliomielitis bulbar carece de ensayos, literatura y fundamento mecanístico (nivel L5), y el puntaje alto de TxGNN parece un artefacto del grafo de conocimiento. No se recomienda avanzar con esta indicación.

**Para avanzar se necesita:**
- Descartar esta indicación como candidata o, en su caso, replantear la priorización hacia las neoplasias mieloides relacionadas con radiación o agentes alquilantes (nivel L4, sujetas a estado mutacional de IDH1).
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicación autorizada), una brecha de datos bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión de la literatura y de registros de ensayos para las indicaciones alternativas de LMA/SMD relacionadas con terapia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


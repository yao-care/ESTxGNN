---
layout: default
title: Droperidol
parent: Solo predicción del modelo (L5)
nav_order: 269
evidence_level: L5
indication_count: 10
---

# Droperidol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Droperidol: De Neuroléptico Inyectable a Síndrome de Tourette

## Resumen en Una Frase

Droperidol es un neuroléptico del grupo de las butirofenonas, comercializado en España como solución inyectable. Los datos compilados para este informe no incluyen el texto de su indicación autorizada.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de Tourette**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de las autorizaciones de la AEMPS |
| Nueva Indicación Predicha | Síndrome de Tourette |
| Puntaje de Predicción TxGNN | 99,89% |
| Nivel de Evidencia | L5 (solo predicción del modelo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción del fármaco en los datos compilados. Según la información farmacológica conocida, droperidol es una butirofenona con potente antagonismo del receptor de dopamina D2.

Otros antagonistas D2 de la misma familia, como haloperidol y pimozida, se utilizan en el síndrome de Tourette. Por eso el mecanismo es plausible: los tics se asocian a una señalización dopaminérgica alterada en los ganglios basales, y bloquear los receptores D2 puede reducirlos.

Esta plausibilidad es solo teórica. No hay estudios con droperidol en esta indicación, y el alto puntaje de TxGNN es únicamente una predicción. El riesgo de prolongación del intervalo QT (advertencia de caja negra) limita además el uso crónico, que es el que requeriría un trastorno como Tourette.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 90791 | DROPERIDOL AGUETTANT 2,5 MG/ML SOLUCIÓN INYECTABLE EFG | Solución inyectable | Laboratoire Aguettant |
| 69837 | XOMOLIX 2,5 mg/ml SOLUCIÓN INYECTABLE | Solución inyectable | Substipharm |
| 86009 | DROPERIDOL KALCEKS 2,5 MG/ML SOLUCIÓN INYECTABLE EFG | Solución inyectable | Kalceks As |
| 86008 | DROPERIDOL KALCEKS 1,25 MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | Kalceks As |
| 82997 | DROPERIDOL HIKMA 2,5 MG/ML SOLUCIÓN INYECTABLE EFG | Solución inyectable | Hikma Farmacêutica (Portugal) S.A. |

Las cinco autorizaciones están vigentes y son de monofármaco. Todas son formas inyectables, lo que es poco práctico para el tratamiento crónico de un trastorno de tics.

---

## Consideraciones de Seguridad

- **Advertencia principal**: riesgo de prolongación del intervalo QT (advertencia de caja negra), que limita el uso crónico.
- **Contraindicaciones (según el grafo de conocimiento TxGNN, no el prospecto)**:
  - Cardiovasculares: síndrome de QT largo (incluido el familiar), torsades de pointes, hipertensión, hipotensión ortostática, síndrome de taquicardia postural ortostática.
  - Neurológicas: enfermedad de los ganglios basales, distonía focal de la mano, blefaroespasmo, atrofia multisistémica.
  - Respiratorias: EPOC, insuficiencia respiratoria.
  - Otras: enfermedad renal, enfermedad hepática, feocromocitoma, déficit de potasio.
- **Interacciones farmacológicas**: se registraron 100 interacciones, de las que se muestran 20. Las de nivel **mayor** incluyen:
  - hidrocortisona, morfina, naloxona;
  - claritromicina, dolasetrón;
  - anfotericina B (varias formulaciones);
  - ácido picosulfúrico y polietilenglicol con electrolitos.

  Entre las de nivel **moderado** figuran famotidina, epinefrina, loperamida, lorcaserina, bisacodilo, difenoxina, difenoxilato, dronabinol y aceite de ricino.

El texto de advertencias y contraindicaciones del prospecto de la AEMPS no está disponible en los datos compilados. Debe consultarse el prospecto para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación se basa solo en la predicción del modelo (L5), sin ensayos clínicos ni literatura. La formulación solo inyectable y el riesgo de QT hacen poco viable el uso crónico en Tourette. Existen alternativas con antagonistas D2 mejor establecidos.

**Para avanzar se necesita:**
- Datos de evidencia clínica o preclínica de droperidol en síndrome de Tourette.
- Texto de advertencias, contraindicaciones e indicación autorizada del prospecto de la AEMPS.
- Datos detallados del mecanismo de acción (MOA).
- Evaluación de compatibilidad de vía y formulación para tratamiento crónico.

**Nota sobre otras indicaciones predichas para droperidol:**
- **Cefalea / migraña** (puntaje 99,47%): nivel L3 y recomendación *Proceed with Guardrails*. Hay un ensayo clínico terminado anticipadamente (NCT01406860, 19 participantes), varias revisiones y un ensayo aleatorizado controlado con placebo publicado (PMID 12552051). El uso se limitaría a urgencias con monitorización del QT.
- **Trastorno bipolar maníaco** (puntaje 99,82%): nivel L3, como pregunta de investigación. La evidencia procede sobre todo de revisiones Cochrane sobre agitación y psicosis aguda, no de tratamiento específico de la manía.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


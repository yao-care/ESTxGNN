---
layout: default
title: Paromomycin
parent: Solo predicción del modelo (L5)
nav_order: 612
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Paromomycin: nueva indicación predicha, Cirrosis asociada a cobre idiopática (nivel de evidencia L5). Indicación original: Coma hepático / encefalopatía hepática (según el grafo de conocimiento"
monitor_inn: "paromomycin"
predicted_indications: ["idiopathic copper-associated cirrhosis", "primitive portal vein thrombosis", "hepatopulmonary syndrome", "hepatoportal sclerosis", "early-onset familial noncirrhotic portal hypertension", "hepatic porphyria", "acute urate nephropathy", "peritonitis"]
---

# Paromomycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Paromomicina: De Coma Hepático a Cirrosis Asociada a Cobre Idiopática

## Resumen en Una Frase

La paromomicina es un antibiótico aminoglucósido de escasa absorción oral, originalmente utilizado para el tratamiento del coma hepático y la encefalopatía hepática.
El modelo TxGNN predice que podría ser efectivo para **cirrosis asociada a cobre idiopática**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Coma hepático / encefalopatía hepática (según el grafo de conocimiento; el texto de indicación de la autorización no está disponible) |
| Nueva Indicación Predicha | Cirrosis asociada a cobre idiopática |
| Puntaje de Predicción TxGNN | 99,90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la paromomicina es un aminoglucósido poco absorbido por vía oral que actúa en el tubo digestivo, reduce la flora bacteriana intestinal y sus productos, y su utilidad en la encefalopatía hepática está establecida. Mecanísticamente, podría ser aplicable a otras hepatopatías crónicas en las que la carga bacteriana intestinal sea relevante.

La relación entre la indicación original y la nueva es, por tanto, el contexto común de enfermedad hepática crónica. Sin embargo, no se conoce ningún efecto directo de la paromomicina sobre el metabolismo del cobre, que es el eje de la cirrosis asociada a cobre idiopática.

La puntuación alta del modelo (0,999) refleja proximidad en la red de conocimiento y no evidencia real. El vínculo es plausible pero no demostrado, y debe tratarse como una hipótesis.

Otras predicciones del modelo con la misma puntuación (trombosis portal primitiva, síndrome hepatopulmonar, esclerosis hepatoportal, hipertensión portal familiar no cirrótica de inicio temprano, porfiria hepática) tampoco cuentan con evidencia clínica ni bibliográfica. La nefropatía aguda por uratos resulta especialmente desfavorable por el riesgo de nefrotoxicidad de los aminoglucósidos. Para peritonitis se recuperaron 16 publicaciones, pero tratan sobre amebiasis y leishmaniasis (estudios in vitro, combinaciones, resistencias y formulaciones) y ninguna evalúa esa indicación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal predicha.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 36795 | HUMATIN 250 MG CÁPSULAS DURAS (Pfizer S.L.) | Cápsula dura | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): enfermedad renal, piouréter, trastorno de pérdida auditiva y sordera mixta ligada al X con fístula perilinfática (*gusher*).
- **Interacciones farmacológicas**: se identificaron 36 interacciones, de las cuales se muestran 20. Las de gravedad **mayor** son:
  - Vacuna viva de *Vibrio cholerae* (cepa CVD 103-HgR)
  - Bloqueantes neuromusculares: cisatracurio, atracurio, doxacurio, metocurina y mivacurio
- Las de gravedad **moderada** incluyen:
  - Inhibidores de la bomba de protones: rabeprazol, omeprazol, esomeprazol, lansoprazol y dexlansoprazol
  - Estrógenos: etinilestradiol, estradiol y mestranol
  - Otros: metotrexato, micofenolato de mofetilo, ácido picosulfúrico, enflurano e indio In-111 oxiquinolina
- La interacción con digoxina es de gravedad **menor**.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no hay un mecanismo conocido que conecte la paromomicina con el metabolismo del cobre. Además, existen señales de seguridad relevantes (riesgo renal y auditivo propio de los aminoglucósidos).

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y análisis mecanístico específico para la cirrosis asociada a cobre.
- Revisión del prospecto de la AEMPS (advertencias y contraindicaciones) para completar el cribado de seguridad.
- Revisión sistemática de la literatura y estudios preclínicos que respalden la hipótesis.
- Valoración de la prioridad frente a otras indicaciones hepáticas con mayor plausibilidad biológica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Mecasermin
parent: Solo predicción del modelo (L5)
nav_order: 496
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Mecasermin: nueva indicación predicha, Monosomía X (nivel de evidencia L5). Indicación original: Síndrome de insensibilidad a la hormona del crecimiento y síndrome de…"
monitor_inn: "mecasermin"
predicted_indications: ["monosomy X", "Wolman disease with hypolipoproteinemia and acanthocytosis", "esophageal varices with bleeding", "esophageal varices without bleeding"]
---

# Mecasermin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Mecasermina: De Síndrome de Insensibilidad a la Hormona del Crecimiento a Monosomía X

## Resumen en Una Frase

Mecasermina es un factor de crecimiento similar a la insulina tipo 1 (IGF-1) recombinante, utilizado originalmente para el síndrome de insensibilidad a la hormona del crecimiento y el síndrome de Laron.
El modelo TxGNN predice que podría ser efectivo para **monosomía X (síndrome de Turner)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Síndrome de insensibilidad a la hormona del crecimiento y síndrome de Laron (según el grafo de conocimiento; la ficha de autorización en España no incluye texto de indicación) |
| Nueva Indicación Predicha | Monosomía X |
| Puntaje de Predicción TxGNN | 99.59% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, mecasermina es IGF-1 recombinante, que actúa sobre el receptor de IGF-1 y reproduce el efecto de la hormona del crecimiento a nivel posterior (downstream). Su eficacia en la insensibilidad a la hormona del crecimiento se debe a que evita la señalización defectuosa de dicha hormona.

El síndrome de Turner (monosomía X) se caracteriza por talla baja, que habitualmente se trata con hormona del crecimiento. Por ello existe un vínculo plausible a través de los efectos promotores del crecimiento. Sin embargo, las pacientes con síndrome de Turner suelen tener intacta la vía GH–IGF-1, por lo que el beneficio de reponer IGF-1 es especulativo.

El puntaje alto de TxGNN (0.996) es solo una predicción computacional; no hay ensayos ni literatura que la sustenten.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 07402001 | INCRELEX 10 mg/ml solución inyectable (Esteve Pharmaceuticals S.A.) | Solución inyectable | No disponible en la ficha |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 24 interacciones, todas de nivel **moderado**. Las principales corresponden a fármacos hipoglucemiantes, por posible riesgo de hipoglucemia:
  - Sulfonilureas: clorpropamida, acetohexamida, glimepirida, glipizida, glibenclamida (gliburida).
  - Meglitinidas: nateglinida.
  - Insulinas: insulina humana (regular, isófana, zinc y zinc prolongada, inhalada), aspart, degludec, detemir, glargina, glulisina y lispro (incluidas formas con protamina).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para monosomía X se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y el beneficio mecanístico es especulativo dado que la vía GH–IGF-1 suele estar intacta en el síndrome de Turner.

**Para avanzar se necesita:**
- Revisión de la literatura sobre IGF-1 en síndrome de Turner y de estudios preclínicos o de mecanismo.
- Datos del mecanismo de acción (MOA) de mecasermina.
- Advertencias y contraindicaciones del prospecto de la AEMPS, que son necesarias antes de cualquier evaluación de seguridad.
- Análisis de compatibilidad de vía de administración y similitud con la indicación original.
- Considerar que otras predicciones tienen mayor plausibilidad mecanística (p. ej., síndrome de insensibilidad a la GH con disregulación inmune 2, autosómico dominante), aunque probablemente ya queda dentro del alcance de la indicación existente y no sería un reposicionamiento genuino.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


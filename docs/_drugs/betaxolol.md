---
layout: default
title: Betaxolol
parent: Solo predicción del modelo (L5)
nav_order: 100
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Betaxolol: nueva indicación predicha, Glaucoma hereditario primario (nivel de evidencia L5). Indicación original: Hipertensión arterial…"
monitor_inn: "BETAXOLOL"
predicted_indications: ["primary hereditary glaucoma"]
---

# Betaxolol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Betaxolol: De Hipertensión e Hipertensión Ocular a Glaucoma Hereditario Primario

## Resumen en Una Frase

Betaxolol es un betabloqueante adrenérgico beta-1 selectivo, utilizado originalmente para el tratamiento de la hipertensión arterial, el glaucoma de ángulo abierto y la hipertensión ocular.
El modelo TxGNN predice que podría ser efectivo para el **glaucoma hereditario primario**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial, glaucoma de ángulo abierto e hipertensión ocular (según el grafo de conocimiento; el texto de indicación autorizado en España no está disponible) |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 99,74 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, betaxolol es un antagonista adrenérgico beta-1 selectivo. En el ojo reduce la presión intraocular (PIO) al disminuir la producción de humor acuoso en el cuerpo ciliar.

El glaucoma hereditario primario (por ejemplo, las formas asociadas a MYOC o CYP1B1) comparte con el glaucoma de ángulo abierto y la hipertensión ocular la vía final de elevación de la PIO y daño de las células ganglionares de la retina. Por ello, un mecanismo que reduce la PIO es biológicamente plausible. El puntaje tan alto del modelo (0,997) probablemente refleja esta cercanía con las indicaciones oftálmicas ya conocidas en el grafo de conocimiento.

Conviene ser prudente: las formas hereditarias congénitas o juveniles suelen tratarse de forma quirúrgica, y el uso de betabloqueantes tópicos en población pediátrica conlleva preocupaciones de seguridad sistémica (bradicardia, broncoespasmo), aunque la selectividad beta-1 de betaxolol reduce el riesgo respiratorio frente a los betabloqueantes no selectivos. Esta asociación es, por tanto, una predicción del modelo sin respaldo clínico directo.

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
| 61015 | BETOPTIC SUSPENSIÓN 2,5 MG/ML COLIRIO EN SUSPENSIÓN (Immedica Pharma AB) | Colirio en suspensión | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

Los datos de advertencias y contraindicaciones del prospecto no están disponibles en los datos compilados. Se recomienda consultar el prospecto de AEMPS.

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): asma (incluidas las formas intrínseca y alérgica), enfisema pulmonar y enfermedad bronquial; bloqueo auriculoventricular y disociación auriculoventricular; enfermedad renal, hepática y de la vesícula biliar; diabetes mellitus, cetoacidosis diabética e hipoglucemia; miastenia gravis y enfermedades de la unión neuromuscular; feocromocitoma, paraganglioma simpático y cáncer de glándula suprarrenal; psoriasis y parapsoriasis; trastornos de ansiedad, neuróticos y distímicos; y otras neoplasias (duodeno, intestino delgado, corazón).
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total; se muestran las 20 primeras consultadas.
  - Moderadas: epinefrina, hidrocortisona, hioscina (hiosciamina), bupropión, triamcinolona, morfina, atropina, dexametasona, betametasona, acetohexamida, budesonida, y sales de calcio (acetato, carbonato, citrato, glubionato, gluconato, lactato).
  - Leves: ácido acetilsalicílico, hidróxido de aluminio, attapulgita.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es plausible mecanísticamente por la cercanía con las indicaciones oftálmicas ya conocidas, pero no existe ningún ensayo clínico ni publicación que la respalde (nivel L5). Además, falta información de seguridad del prospecto y los datos de mecanismo de acción.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), una carencia que bloquea el cribado de seguridad.
- Obtener datos detallados del mecanismo de acción (por ejemplo, desde DrugBank).
- Revisar la literatura sobre el uso de betabloqueantes tópicos en glaucoma hereditario (formas MYOC/CYP1B1) y en población pediátrica.
- Confirmar la indicación autorizada en España para BETOPTIC y la compatibilidad de la vía de administración.
- Evaluar el perfil de seguridad cardiovascular y respiratoria en las poblaciones objetivo, en particular la pediátrica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


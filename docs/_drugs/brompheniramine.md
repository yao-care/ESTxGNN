---
layout: default
title: Brompheniramine
parent: Solo predicción del modelo (L5)
nav_order: 120
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Brompheniramine: nueva indicación predicha, Urticaria alérgica (nivel de evidencia L5). Indicación original: Rinitis alérgica (según el grafo de conocimiento"
monitor_inn: "brompheniramine"
predicted_indications: ["allergic urticaria", "cold urticaria"]
---

# Brompheniramine
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

# Bromfeniramina: De Rinitis Alérgica a Urticaria Alérgica

## Resumen en Una Frase

La bromfeniramina es un antihistamínico H1 de primera generación (clase alquilamina), utilizado originalmente para el tratamiento de la rinitis alérgica, el resfriado común y otras afecciones alérgicas.
El modelo TxGNN predice que podría ser efectivo para **urticaria alérgica**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Rinitis alérgica (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la bromfeniramina es un antagonista del receptor H1 de primera generación (clase alquilamina). La urticaria alérgica está impulsada en gran parte por la liberación de histamina desde los mastocitos, por lo que el bloqueo H1 es mecanísticamente plausible.

Es importante señalar que las indicaciones originales del fármaco ya incluyen urticaria y angioedema. Por tanto, esta predicción se solapa en gran medida con un uso ya existente y no representa una oportunidad de reposicionamiento verdaderamente nueva. El puntaje alto (0.9987) es coherente con ese solapamiento.

Como predicción secundaria, el modelo también propone **urticaria por frío** (puntaje 99.55%). Es una urticaria inducible en la que el frío desencadena la liberación de histamina, y los antihistamínicos H1 son el tratamiento de primera línea. Sin embargo, las guías actuales prefieren antihistamínicos de segunda generación no sedantes (a veces a dosis aumentadas) frente a los de primera generación, debido a la sedación y los efectos anticolinérgicos. Tampoco hay evidencia clínica para esta indicación (nivel L5, decisión Hold).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 79577 | RESFRIOL CÁPSULAS DURAS | Cápsula dura | No disponible en los datos compilados |
| 60577 | ILVICO GRANULADO PARA SOLUCIÓN ORAL | Granulado para solución oral | No disponible en los datos compilados |
| 33844 | ILVICO COMPRIMIDOS RECUBIERTOS | Comprimido recubierto | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proviene del prospecto)**: se asocian la hipertensión, la insuficiencia o enfermedad hepática, la epilepsia, la EPOC, la úlcera gástrica/péptica, la enfermedad renal, la pancreatitis, enfermedades de la vesícula biliar, el hipotiroidismo, la enfermedad inflamatoria intestinal, la diabetes mellitus y la cetoacidosis diabética, la hiperplasia prostática benigna, la hipotensión, el abuso/dependencia de sustancias, la enfermedad coronaria y el infarto de miocardio, la hemoglobinopatía, la colitis por *Clostridium difficile*, la enterocolitis necrosante perinatal y la hipertensión ocular.
- **Interacciones Farmacológicas**: se identificaron 290 interacciones en total. Las de nivel **mayor** son:
  - Cloruro de potasio
  - Citrato de potasio

  Entre las de nivel moderado figuran fármacos anticolinérgicos (atropina, hiosciamina, escopolamina, diciclomina, glicopirronio, propantelina), opioides (morfina, loperamida, opio, eluxadolina) y otros depresores del sistema nervioso central o moduladores (dronabinol, nabilona, metoclopramida).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y se solapa con indicaciones ya existentes del fármaco (urticaria y angioedema). Además, para la urticaria por frío las guías prefieren antihistamínicos de segunda generación.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas), actualmente no disponible, lo que impide el cribado de seguridad.
- Consultar datos del mecanismo de acción en DrugBank.
- Aclarar si la urticaria alérgica ya está cubierta por las indicaciones autorizadas, para determinar si existe realmente una oportunidad de reposicionamiento.
- Buscar ensayos clínicos y literatura específicos para urticaria alérgica y urticaria por frío.
- Evaluar la relación beneficio-riesgo frente a antihistamínicos de segunda generación, dados los efectos sedantes y anticolinérgicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


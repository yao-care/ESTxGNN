---
layout: default
title: Mogamulizumab
parent: Solo predicción del modelo (L5)
nav_order: 540
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Mogamulizumab: nueva indicación predicha, Carcinoma urotelial de la uretra prostática (nivel de evidencia L5). Indicación original: Micosis fungoide y variantes / linfoma cutáneo primario de células …"
monitor_inn: "MOGAMULIZUMAB"
predicted_indications: ["prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "renal pelvis papillary urothelial carcinoma", "human herpesvirus 8-related tumor", "ectomesenchymoma", "malignant cutaneous granular cell skin tumor"]
---

# Mogamulizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Mogamulizumab: De Linfoma Cutáneo de Células T a Carcinoma Urotelial de la Uretra Prostática

## Resumen en Una Frase

Mogamulizumab es un anticuerpo monoclonal dirigido contra CCR4, utilizado originalmente para el tratamiento de linfomas cutáneos de células T (micosis fungoide y variantes, entre otros).
El modelo TxGNN predice que podría ser efectivo para **carcinoma urotelial de la uretra prostática**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Micosis fungoide y variantes / linfoma cutáneo primario de células T (según el grafo de conocimiento; el texto de indicación autorizada en España no está disponible) |
| Nueva Indicación Predicha | Carcinoma urotelial de la uretra prostática |
| Puntaje de Predicción TxGNN | 99,44% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, mogamulizumab es un anticuerpo monoclonal anti-CCR4 que elimina las células CCR4+ mediante citotoxicidad celular dependiente de anticuerpos, incluidos los linfocitos T reguladores (Treg) CCR4+. Su eficacia en linfomas cutáneos de células T está establecida, y mecanísticamente podría ser aplicable a otros tumores si la depleción de Treg redujera la inmunosupresión en el microambiente tumoral.

La relación con el carcinoma urotelial es solo teórica: la reducción de Treg podría potenciar la inmunidad antitumoral, quizás en combinación con inhibidores de puntos de control inmunitario. Sin embargo, los datos disponibles no respaldan un mecanismo específico de CCR4 en este tipo de tumor, ni hay información sobre la expresión de CCR4 o la infiltración de Treg en él.

Otras predicciones del modelo de la misma familia (carcinoma urotelial de pelvis renal, variantes sarcomatoides de vejiga y pelvis renal) comparten la misma limitación: puntajes altos (≈99,4%) sin ensayos ni publicaciones. El puntaje es una predicción del modelo y no establece por sí solo plausibilidad clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1181335001 | POTELIGEO 4 MG/ML concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo monoclonal anti-CCR4 que actúa por citotoxicidad celular dependiente de anticuerpos) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 83 interacciones potenciales; entre las listadas, las de nivel **Mayor** son:
  - Deferiprona
  - Samario (153Sm) lexidronam
  - Adalimumab
  - Baricitinib

  Entre las de nivel **Moderado** figuran estroncio-89 cloruro, roflumilast, cloranfenicol (incluida la vía oftálmica), zidovudina, toxoide tetánico, alefacept, alemtuzumab, anakinra, vacuna contra el ántrax, azatioprina y canakinumab. Las sales de zinc (sulfato, acetato, gluconato, cloruro) son de nivel **Menor**.
  Varias de estas combinaciones implican inmunosupresión o mielosupresión adicional, por lo que requieren revisión individualizada.
- En el caso de tumores asociados al VHH-8, la activación inmunitaria podría conllevar complicaciones inflamatorias (consideración teórica).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa exclusivamente en el puntaje del modelo (nivel L5), sin ensayos clínicos, literatura ni mecanismo específico respaldado. No hay base suficiente para avanzar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), un vacío que bloquea la evaluación de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Evidencia preclínica sobre la expresión de CCR4 y la infiltración de Treg en el carcinoma urotelial
- Búsqueda de estudios clínicos o publicaciones sobre anti-CCR4 en tumores uroteliales
- Revisión de las interacciones de nivel Mayor antes de cualquier uso combinado
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


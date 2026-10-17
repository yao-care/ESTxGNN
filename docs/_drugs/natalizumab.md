---
layout: default
title: Natalizumab
parent: Solo predicción del modelo (L5)
nav_order: 554
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Natalizumab: nueva indicación predicha, Bronquitis (nivel de evidencia L5). Indicación original: Enfermedad de Crohn, enfermedad inflamatoria intestinal…"
monitor_inn: "NATALIZUMAB"
predicted_indications: ["bronchitis", "parapsoriasis", "psoriasis", "severe nonproliferative diabetic retinopathy", "acute lichenoid pityriasis"]
---

# Natalizumab
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

# Natalizumab: De Enfermedad de Crohn y Esclerosis Múltiple a Bronquitis

## Resumen en Una Frase

Natalizumab es un anticuerpo monoclonal utilizado originalmente para el tratamiento de la enfermedad de Crohn, la enfermedad inflamatoria intestinal y la esclerosis múltiple.
El modelo TxGNN predice que podría ser efectivo para **bronquitis**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción basada en grafos de conocimiento.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Crohn, enfermedad inflamatoria intestinal, esclerosis múltiple (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99,46% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, natalizumab bloquea la integrina alfa-4 (VLA-4) y limita el tránsito de leucocitos hacia los tejidos, lo que explica su uso en enfermedades inflamatorias mediadas por el sistema inmune como la esclerosis múltiple y la enfermedad de Crohn.

Mecanísticamente, esta limitación del reclutamiento leucocitario podría atenuar la inflamación de las vías respiratorias impulsada por leucocitos. Sin embargo, no existe evidencia clínica ni bibliográfica que lo apoye, y la alta puntuación de TxGNN (0,995) es únicamente una predicción basada en grafos.

Además, la bronquitis crónica está dirigida principalmente por neutrófilos y con frecuencia es de origen infeccioso. Natalizumab conlleva riesgo de infecciones (por ejemplo, leucoencefalopatía multifocal progresiva, LMP), por lo que el balance riesgo-beneficio resulta desfavorable.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1231745001 | TYRUKO 300 MG concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |
| 106346002 | TYSABRI 150 MG solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No disponible en los datos compilados |
| 06346001 | TYSABRI 300 mg concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto del prospecto)**: leucoencefalopatía multifocal progresiva (LMP).
- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las principales, de gravedad **mayor**:
  - Corticosteroides: hidrocortisona, triamcinolona (incluida la oftálmica), dexametasona, betametasona, budesonida, prednisolona y prednisona.
  - Radiofármacos y anticuerpos: iobenguano (I-131), ibritumomab tiuxetan, tositumomab y tositumomab (I-131).
  - Otros: levamisol, trimetrexato y mercaptopurina.

  Interacciones de gravedad **moderada**: naltrexona. De gravedad **menor**: sales de zinc (sulfato, acetato, gluconato y cloruro).
- Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones oficiales).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para bronquitis se apoya solo en el modelo (nivel L5), sin ensayos ni publicaciones, y el riesgo de infección y de LMP asociado a natalizumab hace que el balance riesgo-beneficio sea desfavorable en una enfermedad frecuentemente infecciosa.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto oficial (advertencias y contraindicaciones) de la AEMPS.
- Estudios preclínicos o de mecanismo que respalden un papel de la integrina alfa-4 en la bronquitis.
- Evaluación del balance riesgo-beneficio frente a las alternativas terapéuticas existentes.
- Revisión de las demás indicaciones predichas (parapsoriasis, psoriasis, retinopatía diabética no proliferativa grave, pitiriasis liquenoide aguda), ya que la evidencia disponible para varias de ellas (en especial psoriasis) sugiere reacciones paradójicas o inducidas por el fármaco, y no beneficio terapéutico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


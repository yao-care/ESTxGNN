---
layout: default
title: Bendroflumethiazide
parent: Solo predicción del modelo (L5)
nav_order: 94
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Bendroflumethiazide: nueva indicación predicha, Enfermedad renal hipertensiva maligna (nivel de evidencia L5). Indicación original: Hipertensión arterial (trastorno hipertensivo)"
---

# Bendroflumethiazide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Bendroflumetiazida: De Hipertensión a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Bendroflumetiazida es un diurético tiazídico utilizado originalmente para el tratamiento de la hipertensión arterial.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (trastorno hipertensivo); el texto de indicación de la autorización no está disponible |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, bendroflumetiazida es un diurético tiazídico, cuya eficacia en la hipertensión está establecida, y la reducción de la presión arterial por depleción de sodio y volumen podría, en teoría, relacionarse con la enfermedad renal hipertensiva.

Sin embargo, la hipertensión maligna con afectación renal es una emergencia hipertensiva que se trata habitualmente con fármacos parenterales de acción rápida. Las tiazidas no son una terapia estándar en este contexto y su eficacia disminuye cuando el filtrado glomerular está reducido.

El puntaje elevado de TxGNN (99.88%) probablemente refleja la cercanía con la indicación original de hipertensión dentro del grafo de conocimiento, y no una evidencia clínica específica. No se aportaron ensayos ni literatura.

### Otras predicciones del modelo

| Posición | Nueva Indicación Predicha | Puntaje TxGNN | Valoración |
|------|------|------|------|
| 2 | Hipertensión renovascular maligna | 99.88% | Extensión de la indicación existente; la monoterapia con diuréticos puede estimular aún más la renina y no es el abordaje preferido. |
| 3 | Hipertensión pulmonar de mecanismo multifactorial poco claro | 99.87% | Los diuréticos solo alivian la sobrecarga de volumen de forma sintomática; probablemente se debe a similitud de nombre en el grafo. |
| 4 | Hipertensión pulmonar por enfermedad pulmonar y/o hipoxia | 99.87% | El manejo se centra en la enfermedad de base; las tiazidas pueden causar hipopotasemia y alcalosis metabólica, con posible empeoramiento en enfermedad pulmonar crónica. |
| 5 | Síndrome de Braddock | 99.83% | Enfermedad muy rara sin fundamento mecanístico ni clínico; probable artefacto del grafo. |

Todas tienen nivel de evidencia L5 y recomendación Hold.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 56535 | NEATENOL DIU 100mg/5mg COMPRIMIDOS | Comprimido | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no del prospecto)**: el grafo asocia el fármaco con contraindicación en las siguientes condiciones:
  - Renales y urinarias: enfermedad renal, anuria, piouréter, nefrocalcinosis.
  - Hepáticas y digestivas: enfermedad hepática, coma hepático, encefalopatía hepática, enfermedad de la vesícula biliar, pancreatitis, ictericia neonatal.
  - Metabólicas y endocrinas: diabetes mellitus, cetoacidosis diabética, deficiencia de potasio, hiperuricemia, gota, hipercalcemia, hiperparatiroidismo, osteítis fibrosa, trastornos del metabolismo del fósforo.
  - Autoinmunes y neuromusculares: lupus eritematoso sistémico (incluido el pediátrico), miastenia gravis (incluida la del adulto), enfermedad de la unión neuromuscular.
  - Cardiorrespiratorias: bloqueo auriculoventricular, enfisema pulmonar, enfermedad bronquial.
  - Psiquiátricas: trastorno de ansiedad, trastorno neurótico, trastorno distímico.
- **Interacciones Farmacológicas**: se identificaron 168 interacciones en total. Entre las mostradas, la mayoría son de nivel moderado:
  - Antidiabéticos (acarbosa, albiglutida, alogliptina, metformina, pioglitazona).
  - Corticoides (hidrocortisona, triamcinolona, dexametasona, beclometasona, betametasona).
  - Inhibidores de la bomba de protones (omeprazol, rabeprazol).
  - Anfotericina B (incluido el complejo lipídico), colecalciferol, bupropión y morfina.
  - De nivel menor: doxiciclina, hiosciamina y atropina.

Para las advertencias principales y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos y literatura (nivel L5). Además, la hipertensión maligna con afectación renal es una emergencia en la que las tiazidas no son tratamiento estándar, y el amplio listado de contraindicaciones (incluida la enfermedad renal y la anuria) es especialmente relevante.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones oficiales), paso imprescindible antes de cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, mediante consulta a DrugBank).
- Revisar sistemáticamente la literatura y los registros de ensayos para detectar evidencia clínica en enfermedad renal hipertensiva.
- Evaluar la compatibilidad de vía de administración y la similitud con la indicación original, hoy pendientes.
- Considerar candidatas alternativas con mayor plausibilidad mecanística.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


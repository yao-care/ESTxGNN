---
layout: default
title: Ethinylestradiol
parent: Solo predicción del modelo (L5)
nav_order: 314
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Ethinylestradiol: nueva indicación predicha, Zinc plasmático elevado (nivel de evidencia L5). Indicación original: Acné, osteoporosis posmenopáusica…"
---

# Ethinylestradiol
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

# Etinilestradiol: De Acné y Osteoporosis Posmenopáusica a Zinc Plasmático Elevado

## Resumen en Una Frase

Etinilestradiol es un estrógeno sintético utilizado originalmente para el acné, la osteoporosis posmenopáusica y la vaginitis atrófica posmenopáusica.
El modelo TxGNN predice que podría ser efectivo para **zinc plasmático elevado**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Acné, osteoporosis posmenopáusica, vaginitis atrófica posmenopáusica (según el grafo de conocimiento; la autorización española no incluye texto de indicación) |
| Nueva Indicación Predicha | Zinc plasmático elevado |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, el etinilestradiol es un agonista de los receptores de estrógenos alfa (ESR1) y beta (ESR2), y su eficacia en indicaciones hormonales como la osteoporosis posmenopáusica y la atrofia vaginal es conocida.

Un vínculo meramente especulativo sería que los estrógenos modifican la síntesis hepática de proteínas transportadoras de zinc (albúmina, alfa-2-macroglobulina) y, con ello, los niveles circulantes de zinc. Sin embargo, la exposición a estrógenos se asocia por lo general con una **disminución**, no con un aumento, del zinc plasmático, por lo que la dirección del efecto no respalda claramente un beneficio terapéutico.

Además, el zinc plasmático elevado es un hallazgo de laboratorio y no una enfermedad con una diana terapéutica establecida, lo que debilita aún más la justificación. La similitud con las indicaciones originales aún está pendiente de evaluar. El único sustento es el puntaje alto del modelo, sin corroboración clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 68629 | Acetato de ciproterona/Etinilestradiol Sandoz 2 mg/0,035 mg comprimidos recubiertos EFG | Comprimido recubierto | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): hipertensión, epilepsia, trastornos de ansiedad, porfirias, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, diabetes mellitus y cetoacidosis diabética, insuficiencia cardíaca congestiva, hipercalcemia, insuficiencia suprarrenal (enfermedad de Addison), hipotiroidismo, lupus eritematoso sistémico, asma e hiperplasia prostática benigna.
- **Interacciones farmacológicas:** Se identificaron 3 interacciones de tipo farmacológico (dianas): receptor de estrógenos alfa (ESR1), receptor de estrógenos beta (ESR2) y transportador de aminoácidos acoplado a protones 1 (SLC36A1). No se dispone de niveles de gravedad.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos ni literatura, y la dirección del efecto de los estrógenos sobre el zinc plasmático no favorece un beneficio terapéutico. Además, el perfil de contraindicaciones es extenso.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias y contraindicaciones oficiales), requisito bloqueante para el cribado de seguridad
- Datos del mecanismo de acción desde DrugBank
- Justificar que el zinc plasmático elevado sea una indicación clínica con relevancia terapéutica
- Revisión sistemática de la literatura sobre estrógenos y zinc sérico
- Evaluar la compatibilidad de la vía de administración y la similitud con las indicaciones originales
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


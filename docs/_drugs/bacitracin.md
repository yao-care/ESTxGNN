---
layout: default
title: Bacitracin
parent: Solo predicción del modelo (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bacitracin: nueva indicación predicha, Queratoconjuntivitis epitelial punteada (nivel de evidencia L5). Indicación original: Queratitis…"
monitor_inn: "bacitracin"
predicted_indications: ["otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "infective urethral stricture", "post-infectious syndrome", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy"]
---

# Bacitracin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Bacitracina: De Queratitis a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

Bacitracina es un antibiótico polipeptídico de uso tópico, originalmente utilizado para el tratamiento de la queratitis, la queratoconjuntivitis y la blefaroconjuntivitis.
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta indicación: el apoyo se basa únicamente en la predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Queratitis, queratoconjuntivitis y blefaroconjuntivitis (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99.999% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la bacitracina es un antibiótico activo frente a bacterias Gram-positivas (inhibe la síntesis de la pared celular bacteriana), su uso en afecciones oculares superficiales está establecido, y mecanísticamente podría ser aplicable a otras afecciones de la superficie ocular.

La queratoconjuntivitis epitelial punteada está estrechamente relacionada con las indicaciones originales (queratitis y queratoconjuntivitis), lo que explica la cercanía en el grafo de conocimiento. Sin embargo, esta entidad suele ser de origen viral o no infeccioso, de modo que un antibacteriano tendría un efecto limitado. La predicción es por tanto plausible por proximidad de enfermedad, pero débil desde el punto de vista mecanístico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 45656 | POMADA ANTIBIOTICA LIADE | Pomada | No especificada en los datos |
| 25490 | DERMO-HUBBER 10 MG/G + 3,5 MG/G + 600 UI/G POMADA | Pomada | No especificada en los datos |
| 39071 | PHONAL COMPRIMIDOS PARA CHUPAR | Comprimido para chupar | No especificada en los datos |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto)**: se asocian, entre otras, infección ocular, conjuntivitis, queratitis por herpes simple, infección ocular fúngica o vírica, glaucoma de ángulo abierto, hipertensión ocular, enfermedad renal, enfermedad hepática, miastenia gravis, epilepsia, diabetes mellitus y cetoacidosis diabética, insuficiencia suprarrenal/enfermedad de Addison, bloqueo auriculoventricular, enfermedad vascular periférica, atrofia cutánea y telangiectasia. Varias de estas asociaciones parecen reflejar los otros componentes de las combinaciones (p. ej., corticoides) y deben verificarse en el prospecto.
- **Interacciones Farmacológicas**: se identificaron 84 interacciones. Las de nivel **Mayor** incluyen:
  - Aminoglucósidos: kanamicina, neomicina y estreptomicina.
  - Deferasirox.
  - Contrastes yodados: diatrizoato, iodipamida, iodixanol e iohexol.

  También hay interacciones de nivel moderado, entre ellas mesalazina, balsalazida, olsalazina, sulfasalazina, exenatida, vancomicina y ácido picosulfúrico.

Las advertencias principales y contraindicaciones del prospecto de la AEMPS no están disponibles; consultar el prospecto para esa información.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5), sin ensayos ni literatura, y la naturaleza frecuentemente viral o no infecciosa de la queratoconjuntivitis epitelial punteada limita la plausibilidad de un antibacteriano.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y de las advertencias/contraindicaciones del prospecto de la AEMPS.
- Revisión bibliográfica específica de bacitracina en queratoconjuntivitis epitelial punteada.
- Confirmar la etiología (bacteriana frente a viral) en la población objetivo y la compatibilidad de la vía oftálmica con las formulaciones disponibles, que son pomadas dermatológicas y comprimidos para chupar.

**Otras predicciones del modelo (para referencia):** la única con algo de literatura es la otitis externa (nivel L4, "Research Question"). La evidencia incluye un estudio de 2007 con pomada de polimixina B y bacitracina, un estudio de susceptibilidad en aislados caninos y dos artículos de 1963, todos indirectos. El resto son L5 y se mantienen en Hold. Varias son categorías inespecíficas o con riesgo de seguridad; en particular, en el síndrome hemolítico urémico asociado a infección preocupa la nefrotoxicidad de la bacitracina sistémica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


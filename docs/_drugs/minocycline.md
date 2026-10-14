---
layout: default
title: Minocycline
parent: Solo predicción del modelo (L5)
nav_order: 531
evidence_level: L5
indication_count: 2
---

# Minocycline
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

# Minociclina: De Infección del Tracto Urinario a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

La minociclina es un antibiótico del grupo de las tetraciclinas, utilizado originalmente para tratar infecciones como las del tracto urinario, bronquitis, acné, ántrax, gonorrea y periodontitis.
El modelo TxGNN predice que podría ser efectiva para la **queratoconjuntivitis epitelial punteada**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección del tracto urinario (según el grafo de conocimiento; el texto de indicación autorizado en AEMPS no está disponible) |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99,63% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la minociclina es una tetraciclina de uso sistémico, con eficacia comprobada en infecciones bacterianas y en acné, y mecanísticamente podría ser aplicable a patologías inflamatorias de la superficie ocular.

Una justificación plausible es que la minociclina posee propiedades antiinflamatorias y de inhibición de metaloproteinasas de matriz (MMP). Las tetraciclinas se emplean en inflamación de la superficie ocular, como la disfunción de las glándulas de Meibomio y la blefaritis. La queratoconjuntivitis epitelial punteada implica inflamación de la superficie ocular, por lo que existe un solapamiento teórico.

Este vínculo es hipotético y no está respaldado por los datos compilados para este informe. La ausencia de datos del mecanismo de acción original limita además la evaluación mecanística.

Como segunda predicción, el modelo propone la **queratitis por exposición** (puntaje 99,20%), también sin evidencia clínica. Su manejo principal es mecánico (lubricación, protección palpebral, corrección de la exposición), por lo que el posible beneficio de la minociclina es especulativo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 51179 | MINOCIN 100 MG CÁPSULAS DURAS (Teofarma S.R.L.) | Cápsula dura | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones / enfermedades de riesgo según el grafo de conocimiento** (no proceden del texto del prospecto): enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal, pseudotumor cerebral, hipertensión intracraneal y discinesia esofágica.
- **Interacciones Farmacológicas**: se identificaron 272 interacciones en total. Entre las de la muestra revisada, destacan las de nivel **mayor** con **isotretinoína** y **acitretina**. Entre las de nivel moderado figuran etinilestradiol, amoxicilina, ampicilina, ácido aminolevulínico tópico, citrato de sodio, asparaginasas, balsalazida, subcitrato de bismuto y potasio, fosfato y acetato de calcio, brentuximab vedotina y cannabidiol. Entre las de nivel menor: acetazolamida, hidroclorotiazida, amilorida y bumetanida.

Las advertencias y contraindicaciones del prospecto de AEMPS no están disponibles; consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y faltan los datos de seguridad del prospecto y el mecanismo de acción, por lo que no es posible avanzar a un cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones)
- Obtener los datos del mecanismo de acción desde DrugBank
- Revisión sistemática de la literatura sobre tetraciclinas/minociclina en queratoconjuntivitis y patologías de la superficie ocular
- Evaluar la compatibilidad de la vía de administración (la presentación autorizada es una cápsula oral; no hay datos de formulación oftálmica)
- Estudios preclínicos o piloto que respalden eficacia y seguridad ocular
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


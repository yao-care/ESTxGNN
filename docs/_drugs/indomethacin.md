---
layout: default
title: Indomethacin
parent: Solo predicción del modelo (L5)
nav_order: 415
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Indomethacin"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "WHIM syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "brachyolmia", "myosclerosis", "juvenile idiopathic arthritis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid nodulosis"]
description: "Indomethacin: nueva indicación predicha, Síndrome de braquidactilia-sindactilia (brachydactyly-syndactyly syndrome) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Indomethacin
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

## Indomethacin: Síndrome de braquidactilia-sindactilia (brachydactyly-syndactyly syndrome)
{: .text-alpha }

## Resumen en Una Frase

Indometacina es un antiinflamatorio no esteroideo (AINE) utilizado originalmente en artritis reumatoide, espondilitis anquilosante, artrosis, gota, bursitis, tendinitis y ductus arterioso persistente.
El modelo TxGNN predice como primera candidata el **síndrome de braquidactilia-sindactilia**, con un puntaje muy alto (0,9997), pero **sin ensayos clínicos ni publicaciones** que lo respalden: es solo una predicción del modelo.
La candidata con más respaldo bibliográfico entre las 10 predichas es la **artritis idiopática juvenil** (19 publicaciones, sin ensayos registrados), que se comenta en la conclusión.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de braquidactilia-sindactilia (brachydactyly-syndactyly syndrome) |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 8 de 10) |
| Número de Autorizaciones | 10 (vigentes: 8) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la indometacina es un inhibidor no selectivo de la ciclooxigenasa (COX-1 y COX-2), lo que reduce la síntesis de prostaglandinas y, con ello, la inflamación, el dolor y la fiebre. Su eficacia en enfermedades inflamatorias articulares está bien establecida.

Para el síndrome de braquidactilia-sindactilia, una malformación congénita de las extremidades, **no se identifica un vínculo mecanístico plausible** entre la inhibición de COX y la fisiopatología de la enfermedad. El alto puntaje de TxGNN es una predicción del modelo, sin respaldo clínico ni bibliográfico.

Las otras predicciones de mayor puntaje (displasias esqueléticas genéticas, síndrome WHIM, braquiolmia, etc.) tampoco cuentan con datos que sustenten un beneficio de los AINE. Las más coherentes con el perfil del fármaco son las artritis idiopáticas juveniles, aunque son más una extensión de las indicaciones articulares existentes que un reposicionamiento genuino.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 42582 | Artrinovo 25 mg cápsulas duras | Cápsula dura | No disponible en los datos |
| 45894 | Aliviosin 100 mg supositorios | Supositorio | No disponible en los datos |
| 42846 | Artrinovo 100 mg supositorios | Supositorio | No disponible en los datos |
| 56980 | Reusin 8 mg/ml solución para pulverización cutánea | Solución cutánea | No disponible en los datos |
| 41723 | Inacid 100 mg supositorios | Supositorio | No disponible en los datos |

Se muestran 5 de las 10 autorizaciones vigentes (todas de monofármaco). Las demás corresponden a Inacid 25 mg cápsulas, Inacid Retard 75 mg, Flogoter 25 mg cápsulas, Flogoter 100 mg supositorios y Artrinovo 50 mg supositorios.

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto)**: hipertensión, epilepsia, úlcera gástrica y úlcera péptica activa, úlcera duodenal, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, trastornos de la coagulación, asma (intrínseca y alérgica), infarto de miocardio, enfermedad cardiovascular, colitis ulcerosa y enfermedad inflamatoria intestinal, enterocolitis necrosante, hemorragia intracerebral, hemoglobinopatías, trastornos de ansiedad y neuróticos, distimia, discinesia esofágica, piouréter y enfermedades infecciosas.
- **Interacciones farmacológicas**: no se registraron interacciones con otros fármacos. Las entradas disponibles describen dianas farmacológicas: COX-1 (PTGS1), COX-2 (PTGS2), receptor DP2 (PTGDR2), PPAR-gamma (PPARG) y transportador de folato acoplado a protones (SLC46A1).

Consultar el prospecto para las advertencias oficiales, ya que no están disponibles en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación principal predicha solo cuenta con el puntaje del modelo (nivel L5), sin ensayos, literatura ni vínculo mecanístico plausible. Además, las advertencias y contraindicaciones oficiales no están disponibles, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas).
- Completar los datos del mecanismo de acción desde DrugBank.
- Plantear una hipótesis biológica que conecte la inhibición de prostaglandinas con la fisiopatología de la enfermedad predicha, antes de cualquier estudio preclínico.
- Valorar como línea alternativa la **artritis idiopática juvenil** (nivel L3, estado "pregunta de investigación"): hay revisiones antiguas y un ECA cruzado de 1978 en 30 niños que comparó cetoprofeno con indometacina, pero la práctica actual se basa en biológicos y FAME, y existen alertas de toxicidad en población pediátrica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


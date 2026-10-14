---
layout: default
title: Naproxen
parent: Solo predicción del modelo (L5)
nav_order: 552
evidence_level: L5
indication_count: 4
---

# Naproxen
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Naproxeno: De Bursitis y Artritis Reumatoide a Síndrome de Braquidactilia-Sindactilia

## Resumen en Una Frase

Naproxeno es un antiinflamatorio no esteroideo (AINE) utilizado originalmente para tratar la bursitis, la artritis reumatoide, la espondilitis anquilosante, la tendinitis, la gota y otros trastornos musculoesqueléticos y dolorosos.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de braquidactilia-sindactilia**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Bursitis, artritis reumatoide, espondilitis anquilosante, tendinitis, gota, osteoartritis (según el grafo de conocimiento; el texto de indicación de las autorizaciones españolas no está disponible) |
| Nueva Indicación Predicha | Síndrome de braquidactilia-sindactilia |
| Puntaje de Predicción TxGNN | 99.35% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, naproxeno es un inhibidor no selectivo de la ciclooxigenasa (COX-1 y COX-2), que reduce la síntesis de prostaglandinas y produce efectos antiinflamatorios y analgésicos. Su eficacia en trastornos inflamatorios y dolorosos del aparato locomotor está comprobada.

Los síndromes de braquidactilia-sindactilia son malformaciones esqueléticas congénitas causadas por defectos genéticos del desarrollo. La inhibición de COX no corrige estas vías, por lo que **los datos disponibles no respaldan un vínculo mecanístico plausible**. En el mejor de los casos, el beneficio se limitaría al alivio sintomático del dolor, lo cual no constituye una señal de reposicionamiento.

Es probable que el puntaje alto (99.35%) refleje la proximidad en el grafo de conocimiento con las indicaciones musculoesqueléticas de naproxeno (artritis, artropatía) y no una justificación biológica. Las otras tres predicciones de mayor puntaje (síndrome de microftalmia colobomatosa-displasia rizomélica, displasia acromesomélica tipo Hunter-Thompson y síndrome de braquiolmia-amelogénesis imperfecta) son también trastornos genéticos raros del desarrollo, igualmente sin evidencia ni vínculo mecanístico, y todas se mantienen en nivel L5 y decisión Hold.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 68435 | Naproxeno Normon 500 mg comprimidos EFG | Comprimido | No disponible |
| 85570 | Naproxeno Aurovitas 500 mg comprimidos EFG | Comprimido | No disponible |
| 80806 | Naproxeno Aurobindo 500 mg comprimidos EFG | Comprimido | No disponible |
| 77727 | Lidet 500 mg comprimidos gastrorresistentes EFG | Comprimido gastrorresistente | No disponible |
| 56267 | Naprosyn 500 mg comprimidos | Comprimido | No disponible |

Se muestran 5 de las 8 autorizaciones vigentes (todas de monofármaco). Las otras tres corresponden a Lundiran 250 mg cápsulas duras, Naproxeno Teva-Ratiopharm 500 mg comprimidos recubiertos con película y Naproxeno Infectopharm 50 mg/ml suspensión oral.

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento** (no proceden del prospecto): hipertensión, insuficiencia hepática y enfermedad hepática, enfermedad renal, insuficiencia cardíaca congestiva, enfermedad coronaria, infarto de miocardio, ictus y trastornos cerebrovasculares, trastornos de la coagulación, anemia, diabetes mellitus y cetoacidosis diabética, osteoporosis, epilepsia, enfermedad de la vesícula biliar, hiperplasia prostática benigna, obesidad y abuso de sustancias, entre otras.
- **Interacciones farmacológicas**: los datos de interacción solo recogen las dianas farmacológicas de naproxeno (COX-1/PTGS1 y COX-2/PTGS2); no se identificaron interacciones con otros fármacos.

Consultar el prospecto para información completa sobre advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre la inhibición de COX y una malformación congénita del desarrollo esquelético. Además, los datos de seguridad del prospecto no están disponibles.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA)
- Evidencia preclínica o clínica que respalde un vínculo biológico con la nueva indicación
- Advertencias y contraindicaciones del prospecto de la AEMPS para completar la evaluación de seguridad
- Textos de indicación aprobada de las autorizaciones españolas
- Evaluación de compatibilidad de vía de administración y de similitud con las indicaciones originales
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


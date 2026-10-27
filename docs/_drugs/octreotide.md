---
layout: default
title: Octreotide
parent: Solo predicción del modelo (L5)
nav_order: 581
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Octreotide: nueva indicación predicha, Queratosis folicular invertida vulvar (nivel de evidencia L5). Indicación original: Acromegalia…"
monitor_inn: "Octreotide"
predicted_indications: ["vulvar inverted follicular keratosis", "seborrheic keratosis"]
---

# Octreotide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Octreotida: De Acromegalia a Queratosis Folicular Invertida Vulvar
{: .text-alpha }

## Resumen en Una Frase

Octreotida es un análogo de la somatostatina, utilizado originalmente para el tratamiento de la acromegalia, el hiperpituitarismo y el síndrome carcinoide.
El modelo TxGNN predice que podría ser efectivo para **queratosis folicular invertida vulvar**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Acromegalia, hiperpituitarismo y síndrome carcinoide (según el grafo de conocimiento de TxGNN; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Queratosis folicular invertida vulvar |
| Puntaje de Predicción TxGNN | 99.58% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 16 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información farmacológica disponible, octreotida actúa como ligando de los receptores de somatostatina SST2, SST3 y SST5 (genes SSTR2, SSTR3 y SSTR5). Se utiliza en tumores secretores de hormona de crecimiento, tumores hipofisarios secretores de TSH y en la obtención de imágenes de tumores neuroendocrinos que expresan receptores de somatostatina.

**No se identifica un vínculo mecanístico respaldado por los datos** entre la señalización de los receptores de somatostatina y la queratosis folicular invertida vulvar. Esta última es una lesión epitelial benigna poco frecuente, que normalmente se trata mediante escisión. La puntuación alta de TxGNN (0.996) es una predicción computacional, sin respaldo clínico ni biológico demostrado en este análisis. La similitud con la indicación original está pendiente de evaluar.

Cabe señalar que la segunda predicción del modelo, la queratosis seborreica (puntaje 99.55%), también carece de ensayos y literatura, y cuenta con tratamientos procedimentales establecidos (crioterapia, curetaje). Ambas predicciones podrían derivar de la misma señal de vecindad en el grafo (lesiones queratinocíticas relacionadas) y no de evidencia independiente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 16 autorizaciones vigentes (todas de principio activo único). Los textos de indicación aprobada no están disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 59559 | Sandostatin 100 microgramos/ml solución inyectable y para perfusión | Solución inyectable y para perfusión | Novartis Farmacéutica S.A. |
| 59561 | Sandostatin 50 microgramos/ml solución inyectable y para perfusión | Solución inyectable y para perfusión | Novartis Farmacéutica S.A. |
| 62139 | Sandostatin LAR 10 mg | Polvo y disolvente para suspensión inyectable | Novartis Farmacéutica S.A. |
| 62140 | Sandostatin LAR 20 mg | Polvo y disolvente para suspensión inyectable | Novartis Farmacéutica S.A. |
| 74584 | Octreotida Sun 100 microgramos/ml EFG | Solución inyectable | Sun Pharmaceutical Industries (Europe) B.V. |

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de precaución según el grafo de conocimiento** (no proceden del texto del prospecto): hiperglucemia, diabetes mellitus, cetoacidosis diabética, hipoglucemia, hipotiroidismo, mixedema, hipotiroidismo congénito, cirrosis hepática, enfermedad hepática, enfermedad de la vesícula biliar, colelitiasis, colecistolitiasis, coledocolitiasis, íleo, obstrucción intestinal, paro cardíaco súbito, enfermedad de la conducción cardíaca, insuficiencia renal, uremia y deficiencia de vitamina B12.
- **Interacciones farmacológicas**: la consulta se completó y no se identificaron interacciones con otros fármacos; únicamente figuran las dianas farmacológicas SST2, SST3 y SST5.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico plausible; además, existen tratamientos locales establecidos para esta lesión benigna.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados (p. ej., desde DrugBank)
- Revisión del prospecto de la AEMPS (advertencias y contraindicaciones), pendiente para el cribado de seguridad
- Búsqueda sistemática de literatura y ensayos que relacionen la señalización de somatostatina con queratosis folicular invertida
- Evaluación de la compatibilidad de vías de administración (sistémica frente a las opciones locales actuales)
- Análisis de la relevancia clínica y de la necesidad médica no cubierta de esta indicación
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


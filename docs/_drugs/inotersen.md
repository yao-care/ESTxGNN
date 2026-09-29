---
layout: default
title: Inotersen
parent: Evidencia moderada (L3-L4)
nav_order: 280
evidence_level: L4
indication_count: 10
---

# Inotersen
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Inotersen: De Polineuropatía por Amiloidosis Hereditaria por Transtiretina (hATTR) a Porfiria Aguda Intermitente

## Resumen en Una Frase

Inotersen es un oligonucleótido antisentido que reduce la producción hepática de transtiretina (TTR). La literatura recuperada lo sitúa en el tratamiento de la amiloidosis hereditaria por transtiretina (hATTR). El modelo TxGNN predice que podría ser efectivo para **porfiria aguda intermitente**, pero por ahora solo hay **0 ensayos clínicos** y **1 publicación** (una revisión general) que lo mencionan, sin respaldo mecanístico directo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrada en los datos de AEMPS (el texto de indicación está vacío). Según la literatura: hATTR |
| Nueva Indicación Predicha | Porfiria aguda intermitente (PAI) |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, inotersen es un oligonucleótido antisentido dirigido al hígado que disminuye la producción de TTR. Su uso en hATTR se apoya en la literatura recuperada.

La relación con la porfiria aguda intermitente es débil. La PAI se debe a una producción excesiva de ALAS1 en el hígado, secundaria a un defecto en la enzima PBGD (gen *HMBS*). La TTR no forma parte de esa vía. Los únicos vínculos plausibles son de clase: ambas enfermedades se tratan con terapias oligonucleotídicas dirigidas al hígado y ambas cursan con neuropatía periférica.

El puntaje TxGNN es muy alto, pero no está respaldado por una justificación a nivel de vía. El agente mecanísticamente relevante para la PAI es givosirán, un ARNip contra ALAS1. Las otras 9 predicciones del modelo (apendicitis, paquimeningitis y otras entidades relacionadas con IgG4, meningitis, peritonitis) tienen nivel L5 y ninguna evidencia clínica ni de literatura. Todas quedan en Hold.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30847674](https://pubmed.ncbi.nlm.nih.gov/30847674/) | 2019 | Revisión | Neurological Sciences | Revisión general de terapias nuevas y ya aprobadas para neuropatías periféricas genéticas, con énfasis en hATTR. El resumen disponible no evalúa el uso en porfiria aguda intermitente |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1181296002 | TEGSEDI 284 MG SOLUCIÓN INYECTABLE EN JERINGA PRECARGADA (Akcea Therapeutics Ireland Limited) | Solución inyectable en jeringa precargada | No especificada en los datos disponibles |

## Consideraciones de Seguridad

- **Advertencias del análisis de predicciones**: inotersen tiene eventos adversos inmunomediados conocidos (glomerulonefritis, trombocitopenia), lo que aconseja cautela en enfermedades de base inmunitaria.
- **Interacciones farmacológicas**: no se encontraron registros en la consulta realizada.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para porfiria aguda intermitente se basa solo en el modelo, sin ensayos clínicos, con una única revisión general y sin vínculo mecanístico entre la TTR y la vía de la PAI. Existe además una alternativa mecanísticamente adecuada (givosirán).

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS para completar advertencias y contraindicaciones (bloqueante para el cribado de seguridad).
- Confirmar el mecanismo de acción y la indicación original consultando DrugBank.
- Justificar a nivel de vía por qué la reducción de TTR podría influir en la PAI, o descartar la hipótesis.
- Buscar estudios preclínicos o clínicos específicos en PAI antes de reconsiderar la decisión.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


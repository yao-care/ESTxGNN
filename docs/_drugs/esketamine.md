---
layout: default
title: Esketamine
parent: Evidencia moderada (L3-L4)
nav_order: 211
evidence_level: L4
indication_count: 2
---

# Esketamine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **2** 
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

# Esketamina: De Indicación Original No Registrada a Agorafobia

## Resumen en Una Frase

Esketamina se comercializa en España como solución para pulverización nasal (Spravato), pero el registro disponible no indica su indicación original.
El modelo TxGNN predice que podría ser efectiva para **agorafobia**, aunque **no hay ensayos clínicos** y solo **1 publicación** general (una revisión de 2020) que se relaciona de forma indirecta con esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrada en la autorización disponible |
| Nueva Indicación Predicha | Agorafobia |
| Puntaje de Predicción TxGNN | 99.57% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la farmacología general, la esketamina es un antagonista del receptor NMDA que modula la señalización glutamatérgica.

En los trastornos de ansiedad y del miedo se ha propuesto una desregulación glutamatérgica y una plasticidad sináptica alterada. Esto ofrece un vínculo plausible con la agorafobia, pero no está demostrado.

El puntaje alto de TxGNN (0.996) es solo una predicción del modelo basada en el grafo de conocimiento. No constituye evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33424664](https://pubmed.ncbi.nlm.nih.gov/33424664/) | 2020 | Revisión | Frontiers in Psychiatry | Revisión general de los tratamientos farmacológicos, aprobados y fuera de indicación, para trastornos de ansiedad (pánico, TAG, ansiedad social) y de las opciones emergentes. No es específica de agorafobia. Con los datos disponibles no se puede confirmar si trata la esketamina o la ketamina. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191410001 | SPRAVATO 28 MG SOLUCION PARA PULVERIZACION NASAL (Janssen-Cilag International N.V) | Solución para pulverización nasal | No especificada en el registro |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la única publicación es una revisión general que no trata específicamente la agorafobia. El respaldo se limita a una predicción del modelo y a un vínculo mecanístico plausible pero no comprobado. También faltan los datos de seguridad del prospecto de AEMPS.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), un bloqueo para el cribado de seguridad
- Confirmar la indicación original autorizada y el mecanismo de acción (DrugBank)
- Revisar el texto completo de la revisión de 2020 para ver si menciona esketamina o ketamina en trastornos de ansiedad
- Buscar estudios específicos de esketamina o ketamina en agorafobia y ansiedad, y ensayos en registros internacionales
- Sobre la segunda predicción (tortícolis paroxística benigna de la infancia): no hay evidencia y el perfil riesgo-beneficio es desfavorable, por lo que se recomienda descartarla
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


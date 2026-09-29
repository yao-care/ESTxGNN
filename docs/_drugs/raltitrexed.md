---
layout: default
title: Raltitrexed
parent: Solo predicción del modelo (L5)
nav_order: 453
evidence_level: L5
indication_count: 10
---

# Raltitrexed
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Raltitrexed: De Indicación Original No Registrada a Colangitis Esclerosante

## Resumen en Una Frase

Raltitrexed es un antimetabolito (antifolato) inhibidor de la timidilato sintasa, comercializado en España como polvo para solución para perfusión (Tomudex). El Evidence Pack no registra su indicación original aprobada.
El modelo TxGNN predice que podría ser efectivo para **colangitis esclerosante**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es solo una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de autorización disponibles |
| Nueva Indicación Predicha | Colangitis esclerosante |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según el análisis asociado, raltitrexed es un inhibidor de la timidilato sintasa (antifolato), que bloquea la síntesis de ADN en células que se dividen rápidamente.

Para la colangitis esclerosante, **no se identifica un mecanismo plausible**. Esta enfermedad es colestásica y fibroinflamatoria, y la inhibición de la timidilato sintasa no tiene un vínculo evidente con esa patología. Raltitrexed además puede elevar las transaminasas y causar hepatotoxicidad, lo que es una preocupación en una enfermedad hepática colestásica.

El puntaje de 99.97% es solo una salida del modelo, sin respaldo en ensayos ni publicaciones. Por tanto, la predicción debe tratarse como una hipótesis sin corroborar.

### Otras indicaciones predichas (todas L5, Hold)

| # | Indicación predicha | Puntaje TxGNN | Comentario |
|---|------|------|------|
| 2 | Síndrome mielodisplásico | 99.97% | Efecto antiproliferativo concebible, pero especulativo. La mielosupresión es grave en pacientes que ya tienen citopenias |
| 3–7 | Síndromes drepanocíticos (Hb E, beta-talasemia, Hb C, HPFH, Hb D) | 99.96% | Hipótesis no probada de inducción de hemoglobina fetal. El puntaje idéntico sugiere una señal compartida del grafo, no evidencia independiente |
| 8 | Síndrome mielodisplásico no clasificado | 99.96% | Misma lógica y mismo riesgo que el síndrome mielodisplásico |
| 9 | Citopenia refractaria de la infancia | 99.96% | Sin datos pediátricos. La mielosupresión es una preocupación mayor en niños con fallo medular |
| 10 | Deleción parcial del brazo largo del cromosoma 5 | 99.95% | Equivale al SMD con del(5q), que ya cuenta con terapia dirigida establecida |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61452 | TOMUDEX 2 MG POLVO PARA SOLUCION PARA PERFUSION (Hospira Invicta S.A.) | Polvo para solución para perfusión | No consta en los datos disponibles |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, antifolato inhibidor de la timidilato sintasa) |
| Riesgo de Mielosupresión | Alto (la mielosupresión marcada es una toxicidad conocida) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, transaminasas y función hepática, función renal |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

---

## Consideraciones de Seguridad

- **Hepatotoxicidad**: raltitrexed puede elevar las transaminasas, lo que es especialmente relevante en una enfermedad colestásica como la colangitis esclerosante.
- **Mielosupresión**: es un riesgo importante y desfavorable en las indicaciones hematológicas predichas (síndromes mielodisplásicos, síndromes drepanocíticos, citopenia refractaria de la infancia).
- **Interacciones farmacológicas**: no se encontraron registros en la consulta realizada.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5): no hay ensayos ni publicaciones, y no se identifica un mecanismo plausible. El perfil de toxicidad (hepatotoxicidad y mielosupresión) es desfavorable para las indicaciones predichas.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS para completar advertencias y contraindicaciones, y confirmar la indicación aprobada.
- Obtener datos del mecanismo de acción desde DrugBank para analizar el vínculo mecanístico.
- Buscar evidencia preclínica o clínica que conecte la inhibición de la timidilato sintasa con la colangitis esclerosante.
- Evaluar la seguridad hepática y hematológica antes de considerar cualquier estudio.

*Estos resultados son solo para investigación y no constituyen consejo médico. Todo candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


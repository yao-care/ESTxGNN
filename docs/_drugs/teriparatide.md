---
layout: default
title: Teriparatide
parent: Solo predicción del modelo (L5)
nav_order: 522
evidence_level: L5
indication_count: 10
---

# Teriparatide
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

# Teriparatida: De Osteoporosis a Úlcera Duodenal

## Resumen en Una Frase

Teriparatida es un fragmento de la hormona paratiroidea humana (PTH 1-34), utilizado originalmente para tratar la osteoporosis en pacientes con alto riesgo de fractura.
El modelo TxGNN predice que podría ser efectiva para la **úlcera duodenal**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es solo una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Osteoporosis en pacientes con alto riesgo de fractura (según datos farmacológicos; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Úlcera duodenal |
| Puntaje de Predicción TxGNN | 99.86% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 15 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en este paquete de evidencia. Según la información farmacológica conocida, teriparatida es un péptido que actúa sobre los receptores PTH1R y PTH2R. Su eficacia en la osteoporosis está comprobada gracias a su acción anabólica sobre el hueso.

Con la información disponible, **no se identifica un vínculo mecanístico plausible** entre la señalización anabólica ósea de la PTH(1-34) y la fisiopatología de la úlcera duodenal. El puntaje TxGNN es muy alto (99.86%), pero refleja solo asociaciones dentro del grafo de conocimiento. No hay estudios que lo confirmen, y el modelo no aporta una explicación biológica propia.

Por eso esta predicción debe tratarse como una hipótesis sin respaldo. No debe interpretarse como una recomendación terapéutica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Teriparatida cuenta con 15 autorizaciones en España. Estas son las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1161159004 | TERROSA 20 microgramos/80 microlitros solución inyectable en pluma precargada (Gedeon Richter) | Solución inyectable |
| 1161159001 | TERROSA 20 microgramos/80 microlitros solución inyectable (Gedeon Richter) | Solución inyectable |
| 1161161001 | MOVYMIA 20 microgramos/80 microlitros solución inyectable (Stada Arzneimittel) | Solución inyectable |
| 1161161002 | MOVYMIA 20 microgramos/80 microlitros solución inyectable (Stada Arzneimittel) | Solución inyectable |
| 85653 | DURATIL 20 microgramos/80 microlitros solución inyectable en pluma precargada EFG (GP Pharm) | Solución inyectable en pluma precargada |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para úlcera duodenal se basa solo en el modelo (nivel L5), sin ensayos, sin literatura y sin un mecanismo plausible. No hay base para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (DrugBank) y del prospecto de la AEMPS (advertencias y contraindicaciones), que aún faltan.
- Una hipótesis biológica que vincule la señalización PTH1R/PTH2R con la úlcera duodenal.
- Estudios preclínicos que respalden esa hipótesis antes de plantear cualquier estudio clínico.

**Nota sobre otras predicciones del mismo farmaco:** de las 10 indicaciones predichas, la mejor respaldada no es la primera, sino la **osteoporosis asociada al embarazo y la lactancia** (puesto 8, puntaje 99.55%). Tiene nivel L3, con 2 ensayos clínicos indirectos y 20 publicaciones, entre ellas una revisión sistemática con metaanálisis y estudios de cohortes con teriparatida. Su decisión es **Proceed with Guardrails**: uso fuera de indicación, inicio tras suspender la lactancia, atención a la planificación de futuros embarazos, control de calcio y vitamina D, y supervisión especializada. No se identificó ningún ECA dedicado. Conviene evaluarla en un informe aparte.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


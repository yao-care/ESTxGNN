---
layout: default
title: Fluvoxamine
parent: Solo predicción del modelo (L5)
nav_order: 241
evidence_level: L5
indication_count: 10
---

# Fluvoxamine
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

# Fluvoxamina: De Depresión y Trastorno Obsesivo-Compulsivo a Trastorno Esquizoide de la Personalidad

## Resumen en Una Frase

La fluvoxamina es un inhibidor selectivo de la recaptación de serotonina (ISRS), utilizado originalmente en episodios depresivos mayores y trastorno obsesivo-compulsivo (TOC).
El modelo TxGNN predice que podría ser efectiva para el **trastorno esquizoide de la personalidad**, pero **no hay ensayos clínicos** y solo **1 publicación** asociada, que no contiene datos de eficacia de la fluvoxamina.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de AEMPS (el texto de indicación está vacío). Según la fuente farmacológica: episodios depresivos mayores y TOC |
| Nueva Indicación Predicha | Trastorno esquizoide de la personalidad |
| Puntaje de Predicción TxGNN | 99.997% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro de origen. Según la información farmacológica disponible, la fluvoxamina actúa sobre el transportador de serotonina (SERT, gen SLC6A4) y es además agonista del receptor sigma-1 (SIGMAR1). Su eficacia en depresión y TOC está establecida, pero no hay un puente mecanístico documentado hacia el trastorno esquizoide de la personalidad.

La única publicación asociada es un estudio transversal sobre trastornos y rasgos de personalidad en pacientes con trastorno dismórfico corporal. Menciona rasgos esquizoides como hipótesis descriptiva, y 26 de los sujetos participaron en un estudio con fluvoxamina. No aporta datos de eficacia de la fluvoxamina en esta condición.

Además, el mismo puntaje (99.997%) aparece en varios nodos de trastornos de la personalidad (histriónico, esquizotípico, paranoide). Esto sugiere un **artefacto de vecindad en el grafo** y no una señal específica de esta indicación. Por ello, la predicción debe considerarse hipotética.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10929788](https://pubmed.ncbi.nlm.nih.gov/10929788/) | 2000 | Estudio transversal/cohorte | Comprehensive Psychiatry | Evalúa trastornos y rasgos de personalidad en 148 pacientes con trastorno dismórfico corporal (26 participaron en un estudio con fluvoxamina). No aporta datos de eficacia de fluvoxamina en el trastorno esquizoide. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 57233 | DUMIROX 50 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 58212 | DUMIROX 100 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 63277 | FLUVOXAMINA SANDOZ 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 63276 | FLUVOXAMINA SANDOZ 50 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |

Los titulares son Viatris Healthcare Limited (Dumirox) y Sandoz Farmacéutica S.A. (genéricos). El texto de indicación aprobada no está disponible en los datos recibidos.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. La consulta de interacciones devolvió únicamente dianas farmacológicas (SERT y receptor sigma-1), no interacciones medicamentosas propiamente dichas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene respaldo experimental: no hay ensayos clínicos y la única publicación no evalúa la eficacia de la fluvoxamina. El puntaje idéntico en varios trastornos de la personalidad apunta a un artefacto del modelo.

**Para avanzar se necesita:**
- Estudios clínicos o preclínicos que evalúen la fluvoxamina específicamente en el trastorno esquizoide.
- Un puente mecanístico documentado; el campo de mecanismo de acción de la fuente está vacío.
- Texto de indicaciones, advertencias y contraindicaciones del prospecto de AEMPS.

**Nota:** en la misma lista de predicciones, la **ansiedad** (puntaje 99.97%, nivel L2, Proceed with Guardrails) y la **depresión endógena** (99.85%, L2, Proceed with Guardrails) tienen evidencia clínica mucho más sólida. Se recomienda evaluarlas en informes separados y priorizarlas frente a esta indicación. Ambas podrían ser uso cercano a la indicación autorizada más que un reposicionamiento genuino.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


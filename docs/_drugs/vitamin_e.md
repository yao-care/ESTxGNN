---
layout: default
title: Vitamin E
parent: Solo predicción del modelo (L5)
nav_order: 856
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Vitamin E: nueva indicación predicha, Trastorno congénito del metabolismo de la bilirrubina (nivel de evidencia L5). Indicación original: Colestasis y déficit familiar aislado de vitamina E (según el…"
---

# Vitamin E
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

# Vitamina E: De Colestasis a Trastorno Congénito del Metabolismo de la Bilirrubina

## Resumen en Una Frase

La vitamina E es un nutriente liposoluble antioxidante, utilizado originalmente en situaciones de colestasis (incluidas las formas intrahepáticas familiares) y en el déficit familiar aislado de vitamina E.
El modelo TxGNN predice que podría ser efectiva para el **trastorno congénito del metabolismo de la bilirrubina**, pero actualmente hay **0 ensayos clínicos** y solo **1 publicación** con relación indirecta, por lo que la evidencia es esencialmente solo predictiva.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Colestasis y déficit familiar aislado de vitamina E (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Trastorno congénito del metabolismo de la bilirrubina |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la vitamina E (alfa-tocoferol) es un antioxidante liposoluble que protege las membranas celulares de la peroxidación lipídica. Su uso en colestasis está bien establecido como tratamiento de soporte, ya que la reducción del flujo biliar provoca malabsorción de vitaminas liposolubles.

La relación con la nueva indicación es indirecta. El único artículo recuperado para esta predicción (PMID 7915305, 1994) trata de un déficit de síntesis de ácidos biliares (déficit de 3β-hidroxi-C27-esteroide deshidrogenasa/isomerasa) como causa de colestasis intrahepática progresiva. Es un trastorno de síntesis de ácidos biliares, no un trastorno directo de la bilirrubina, y no evalúa la vitamina E.

Un vínculo plausible es que la colestasis asociada puede causar déficit de vitamina E, que la suplementación corrige. Esto sería **tratamiento de soporte, no un reposicionamiento modificador de la enfermedad**. El puntaje TxGNN, aunque muy alto, es solo una predicción computacional.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7915305](https://pubmed.ncbi.nlm.nih.gov/7915305/) | 1994 | Serie de casos | The Journal of Pediatrics | Describe el déficit de 3β-hidroxi-C27-esteroide deshidrogenasa/isomerasa como causa de colestasis intrahepática progresiva en niños (cribado de 30 casos). No evalúa vitamina E. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 62277 | AUXINA E-400 UI cápsulas blandas | Cápsula blanda | No disponible |
| 14261 | AUXINA E-50 UI cápsulas blandas | Cápsula blanda | No disponible |
| 34892 | AUXINA E-200 UI cápsulas blandas | Cápsula blanda | No disponible |
| 32807 | EPHYNAL ampollas | Solución inyectable | No disponible |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; las 20 primeras analizadas incluyen:
  - **Moderadas**: ácido acetilsalicílico, hierro, sevelamer, hierro sacarosa, abciximab, antitrombina III humana, apixabán, dipiridamol, betrixabán, bivalirudina, cangrelor y caplacizumab. Muchas implican fármacos antitrombóticos/anticoagulantes, por lo que conviene vigilar el riesgo hemorrágico.
  - **Leves**: corticoides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisona, prednisolona) y orlistat.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (L5): no hay ensayos clínicos y la única publicación recuperada no evalúa la vitamina E. El beneficio plausible (corregir el déficit de vitamina E en colestasis) es soporte nutricional, no un efecto sobre el trastorno de la bilirrubina.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Advertencias y contraindicaciones del prospecto de la AEMPS (pendientes; bloquean el cribado de seguridad).
- Textos de indicación aprobada de las 4 autorizaciones españolas.
- Revisión de la literatura específica sobre vitamina E en trastornos de la bilirrubina y colestasis hereditaria, preferiblemente estudios controlados.
- Aclarar si el objetivo es soporte nutricional o un efecto modificador de la enfermedad.
- Como contexto, otras predicciones del modelo tienen aún menos respaldo: la de enfermedad hepática inducida por fármacos (rank 4, L4) se apoya solo en estudios preclínicos, y la del nevus de Ito (rank 8) parece un falso positivo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


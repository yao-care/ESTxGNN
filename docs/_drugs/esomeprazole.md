---
layout: default
title: Esomeprazole
parent: Solo predicción del modelo (L5)
nav_order: 308
evidence_level: L5
indication_count: 3
---

# Esomeprazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Esomeprazol: De Enfermedad de Úlcera Péptica a Reflujo Duodenogástrico

## Resumen en Una Frase

Esomeprazol es un inhibidor de la bomba de protones (S-isómero del omeprazol), utilizado originalmente para la enfermedad de úlcera péptica, el reflujo gastroesofágico y el síndrome de Zollinger-Ellison.
El modelo TxGNN predice que podría ser efectivo para **reflujo duodenogástrico**,
pero actualmente hay **0 ensayos clínicos** y **1 publicación** (una revisión general sobre inhibidores de la bomba de protones) relacionados con esta dirección, por lo que la evidencia es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de úlcera péptica (según las indicaciones originales del grafo de conocimiento; los textos de indicación de las autorizaciones españolas no constan en los datos) |
| Nueva Indicación Predicha | Reflujo duodenogástrico |
| Puntaje de Predicción TxGNN | 99.53% |
| Nivel de Evidencia | L4 (solo racionalidad mecanística, sin estudios específicos para esta indicación) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Esomeprazol inhibe la bomba de protones gástrica (H+/K+-ATPasa, cuyo gen diana es ATP4A) y, con ello, reduce la secreción de ácido gástrico. Por eso se usa en la úlcera péptica, el reflujo gastroesofágico y los estados de hipersecreción ácida. Los datos compilados no incluyen una descripción detallada del mecanismo de acción, por lo que esta explicación se basa en el conocimiento farmacológico general de la clase.

El reflujo duodenogástrico consiste en el retorno de contenido duodenal (bilis y secreciones pancreáticas) al estómago. Al ser una enfermedad cercana a los trastornos gastroduodenales ya tratados con esomeprazol, el grafo de conocimiento le asigna un puntaje alto. Una menor acidez podría reducir el daño de la mucosa y los síntomas asociados.

Sin embargo, este reflujo depende sobre todo de la motilidad y de la disfunción pilórica, no del ácido. La supresión ácida tendría, como mucho, un efecto sintomático o indirecto. El puntaje alto refleja probablemente la proximidad en el grafo con las indicaciones aprobadas, y no una evidencia clínica propia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Revisión | European Journal of Clinical Pharmacology | Actualización del uso clínico y la farmacocinética de los inhibidores de la bomba de protones, fármacos de primera elección en úlcera péptica, infección por *H. pylori*, reflujo gastroesofágico, lesiones por AINE y síndrome de Zollinger-Ellison. No aborda directamente el reflujo duodenogástrico. |

---

## Información de Mercado en España

Hay 20 autorizaciones vigentes, todas de medicamentos con esomeprazol como único principio activo. Se muestran las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 63437 | Nexium Mups 40 mg comprimidos gastrorresistentes | Comprimido gastrorresistente |
| 66038 | Nexium 40 mg polvo para solución inyectable y para perfusión | Polvo para solución inyectable y para perfusión |
| 69980 | Nexium 10 mg granulado gastrorresistente para suspensión oral, sobre | Granulado para suspensión oral |
| 63940 | Axiago 20 mg comprimidos gastrorresistentes | Comprimido gastrorresistente |
| 72702 | Esomeprazol Teva 40 mg cápsulas duras gastrorresistentes EFG | Cápsula dura gastrorresistente |

---

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación en el grafo de conocimiento** (no proceden del texto del prospecto): insuficiencia hepática, osteoporosis, osteoporosis posmenopáusica, fractura ósea y gastritis atrófica crónica. Deben verificarse contra el prospecto oficial.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto de la AEMPS.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en la cercanía con las indicaciones ya aprobadas dentro del grafo de conocimiento. No hay ensayos clínicos y la única publicación es una revisión general que no estudia esta enfermedad. Además, la fisiopatología del reflujo duodenogástrico (motilidad y función pilórica) no depende principalmente del ácido, por lo que el beneficio sería, como mucho, sintomático.

**Para avanzar se necesita:**
- Estudios clínicos o series de casos que evalúen esomeprazol en reflujo duodenogástrico, con criterios de valoración definidos (síntomas, gastritis biliar, hallazgos endoscópicos).
- Revisión de la literatura sobre inhibidores de la bomba de protones en reflujo biliar, y comparación con tratamientos orientados a la motilidad.
- Datos detallados del mecanismo de acción y del prospecto oficial (advertencias y contraindicaciones) para completar el análisis de seguridad.
- Nota: otra indicación predicha, la úlcera duodenal, cuenta con abundante evidencia clínica (varios ensayos de Fase 3 completados), pero es esencialmente un uso ya cubierto por la indicación de úlcera péptica y no un reposicionamiento real.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


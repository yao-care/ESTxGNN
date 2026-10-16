---
layout: default
title: Bleomycin
parent: Solo predicción del modelo (L5)
nav_order: 109
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Bleomycin: nueva indicación predicha, Neoplasia de la cauda equina (nivel de evidencia L5). Indicación original: Linfomas (Hodgkin y no Hodgkin) y cáncer de cabeza y cuello (según el…"
monitor_inn: "bleomycin"
predicted_indications: ["cauda equina neoplasm", "adult astrocytic tumour", "reticulum cell sarcoma", "primary pulmonary lymphoma", "pulmonary blastoma", "well-differentiated fetal adenocarcinoma of the lung"]
---

# Bleomycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Bleomicina: De Linfoma de Hodgkin y No Hodgkin a Neoplasia de la Cauda Equina

## Resumen en Una Frase

La bleomicina es un antibiótico glucopeptídico citotóxico, utilizado originalmente en el tratamiento de linfomas (Hodgkin y no Hodgkin) y de cáncer de cabeza y cuello.
El modelo TxGNN predice que podría ser efectiva para la **neoplasia de la cauda equina**, pero actualmente **no hay ensayos clínicos** y solo hay **1 publicación**, de relevancia indirecta, que se relaciona con esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Linfomas (Hodgkin y no Hodgkin) y cáncer de cabeza y cuello (según el grafo de conocimiento TxGNN; los textos de indicación de las autorizaciones españolas no estaban disponibles) |
| Nueva Indicación Predicha | Neoplasia de la cauda equina |
| Puntaje de Predicción TxGNN | 99.30% |
| Nivel de Evidencia | L4 (la única publicación es indirecta; en la práctica, casi solo hay predicción del modelo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según lo conocido, la bleomicina es un glucopéptido citotóxico que provoca roturas en las cadenas de ADN. Su eficacia en linfomas y en cáncer de cabeza y cuello está comprobada, y mecanísticamente podría ser aplicable a otros tumores de crecimiento rápido.

La predicción del modelo parece apoyarse en la cercanía dentro del grafo de conocimiento entre la bleomicina y otras neoplasias. No se ha establecido un vínculo directo con los tumores de la cauda equina. La única publicación recuperada trata sobre radioterapia de rescate en germinoma del sistema nervioso central recaído tras quimioterapia primaria. Esa quimioterapia incluía bleomicina (régimen carboplatino, etopósido y bleomicina), pero el estudio no demuestra un efecto de la bleomicina en tumores de la cauda equina.

A esto se suma una limitación farmacológica importante: la penetración de la bleomicina a través de la barrera hematoencefálica y hematomedular es limitada. Esto pesa en contra de su uso en tumores del eje neural.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9440744](https://pubmed.ncbi.nlm.nih.gov/9440744/) | 1998 | Cohorte (retrospectivo) | Journal of Clinical Oncology | Evalúa la radioterapia como rescate en pacientes con germinoma del SNC que recayeron tras quimioterapia primaria con carboplatino, etopósido y bleomicina. Es evidencia indirecta, no específica de la cauda equina ni del efecto de la bleomicina. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 49313 | Bleomicina Viatris 15.000 UI (Ph Eur) = 15 U (USP) polvo para solución inyectable | Polvo para solución inyectable | Viatris Pharmaceuticals S.L. |
| 81969 | Bleomicina Accord 15.000 UI polvo para solución inyectable y para perfusión EFG | Polvo para solución inyectable | Accord Healthcare S.L.U. |

Ambas autorizaciones son de medicamento de principio activo único y están vigentes.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (glucopéptido antitumoral que induce roturas en el ADN) |
| Riesgo de Mielosupresión | Bajo a moderado (se describe históricamente como un agente relativamente respetuoso con la médula ósea); confirmar en el prospecto |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Función pulmonar (incluida capacidad de difusión) y radiografía/imagen torácica por el riesgo de toxicidad pulmonar, hemograma, función hepática y renal |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

Estos datos proceden del conocimiento general de la clase del fármaco. Consultar las advertencias y precauciones del prospecto.

---

## Consideraciones de Seguridad

- **Toxicidad pulmonar**: es la principal preocupación asociada a la bleomicina, y especialmente relevante en pacientes de edad avanzada y con dosis acumuladas altas.
- **Interacciones Farmacológicas**: se identificaron 205 interacciones potenciales. Entre las listadas figuran levofloxacino (nivel menor), pantoprazol, palonosetrón, lactulosa, aprepitant, morfina, omeprazol, lansoprazol, vancomicina, prednisona, hidrocortisona, manitol, cloruro de potasio, prednisolona, ranitidina, granisetrón, ondansetrón, famotidina, claritromicina y metoclopramida. Para todas ellas, salvo levofloxacino, la gravedad no está clasificada.

Consultar el prospecto para el resto de la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (99.30%), pero no hay ensayos clínicos y la única publicación es indirecta. Además, la penetración limitada en el sistema nervioso y la toxicidad pulmonar de la bleomicina no favorecen esta nueva indicación.

**Para avanzar se necesita:**
- Evidencia directa de eficacia de la bleomicina en tumores de la cauda equina o de la médula espinal (estudios preclínicos o series de casos).
- Datos sobre penetración en el SNC o sobre vías de administración alternativas (por ejemplo, intratecal o intratumoral), cuya compatibilidad está pendiente de evaluar.
- Datos detallados del mecanismo de acción (MOA).
- Advertencias y contraindicaciones del prospecto de la AEMPS.
- Comparación con las alternativas terapéuticas actuales para estos tumores.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


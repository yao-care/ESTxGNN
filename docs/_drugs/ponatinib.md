---
layout: default
title: Ponatinib
parent: Solo predicción del modelo (L5)
nav_order: 650
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Ponatinib: nueva indicación predicha, Fibromatosis gingival (nivel de evidencia L5). Indicación original: Leucemia mieloide crónica, BCR-ABL1 positiva"
monitor_inn: "PONATINIB"
predicted_indications: ["fibromatosis, gingival", "liposarcoma"]
---

# Ponatinib
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

## Ponatinib: De Leucemia Mieloide Crónica BCR-ABL1 Positiva a Fibromatosis Gingival
{: .text-alpha }

## Resumen en Una Frase

Ponatinib es un inhibidor de tirosina quinasa de múltiples dianas, originalmente utilizado para el tratamiento de la leucemia mieloide crónica BCR-ABL1 positiva.
El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**, aunque actualmente **no existen ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia mieloide crónica, BCR-ABL1 positiva |
| Nueva Indicación Predicha | Fibromatosis gingival |
| Puntaje de Predicción TxGNN | 99,04% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, ponatinib es un inhibidor multiquinasa (BCR-ABL, FGFR, PDGFR, VEGFR, SRC, KIT) con eficacia comprobada en la leucemia mieloide crónica, y mecanísticamente podría actuar sobre las vías de proliferación de fibroblastos y de señalización fibrótica.

Este vínculo es especulativo y no está respaldado por ninguna evidencia aportada. La fibromatosis gingival es una enfermedad benigna y rara, a menudo hereditaria o inducida por fármacos. Para un fármaco con toxicidad cardiovascular y trombótica grave, el balance riesgo-beneficio es desfavorable sin evidencia que lo sustente.

Como indicación alternativa, el modelo también predice **liposarcoma** (puntaje 99,00%), con una publicación preclínica de perfilado de quinasas (ver más abajo). Tampoco hay ensayos clínicos para esta indicación y su nivel de evidencia es igualmente L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Para fibromatosis gingival, actualmente no hay literatura relacionada disponible.

Para la indicación alternativa (liposarcoma), se identificó una publicación preclínica:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29132397](https://pubmed.ncbi.nlm.nih.gov/29132397/) | 2017 | Preclínico | Journal of Hematology & Oncology | Perfilado de quinasas en liposarcomas mediante ARNi y cribado de fármacos para identificar dianas terapéuticas. No se puede confirmar a partir de los datos disponibles que ponatinib fuera uno de los agentes activos. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 113839006 | ICLUSIG 30 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |
| 113839005 | ICLUSIG 15 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |
| 113839003 | ICLUSIG 45 mg comprimidos recubiertos con película | Comprimido | No disponible en los datos |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; en general, hemograma y función hepática y renal |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; entre las principales de las 20 revisadas:
  - **Mayores**: ácido acetilsalicílico y claritromicina.
  - **Moderadas**: loperamida, aprepitant, dexametasona, naldemedina, naltrexona, metronidazol y miconazol.
  - **Menores**: antiácidos y antisecretores gástricos (famotidina, ranitidina, cimetidina, nizatidina, omeprazol, lansoprazol, pantoprazol, rabeprazol, dexlansoprazol, óxido de magnesio) y naloxegol.

Para las advertencias y contraindicaciones, consultar el prospecto. Cabe señalar que las evaluaciones de los datos compilados mencionan una advertencia de recuadro por toxicidad cardiovascular y trombótica grave, que debe verificarse en el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en un puntaje alto del modelo TxGNN (nivel L5), sin ensayos clínicos ni literatura que la respalden. Dado el perfil de toxicidad cardiovascular del fármaco y la naturaleza benigna de la fibromatosis gingival, el balance riesgo-beneficio no es favorable en este momento.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Advertencias y contraindicaciones del prospecto de la AEMPS (carencia bloqueante para el cribado de seguridad).
- Evidencia preclínica específica de ponatinib en fibroblastos gingivales o modelos de fibrosis.
- Revisión del texto completo de la publicación PMID 29132397 para confirmar si ponatinib fue evaluado, y búsqueda de datos in vitro/in vivo en liposarcoma como alternativa.
- Análisis de compatibilidad de vías de administración y de similitud con la indicación original.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


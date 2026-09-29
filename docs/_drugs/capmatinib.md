---
layout: default
title: Capmatinib
parent: Solo predicción del modelo (L5)
nav_order: 100
evidence_level: L5
indication_count: 2
---

# Capmatinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Capmatinib: De Indicación Original No Disponible a Artritis Reumatoide

## Resumen en Una Frase

Capmatinib es un inhibidor selectivo de la tirosina quinasa MET (receptor de HGF), comercializado en España como Tabrecta. Los datos recibidos no incluyen su indicación original aprobada.
El modelo TxGNN predice que podría ser efectivo para **artritis reumatoide**, pero **no hay ensayos clínicos** y solo hay **1 publicación** de carácter general (una revisión sobre inhibidores de quinasas, sin datos específicos de artritis reumatoide). La evidencia actual es únicamente la predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de AEMPS recibidos |
| Nueva Indicación Predicha | Artritis reumatoide |
| Puntaje de Predicción TxGNN | 99.45% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Capmatinib es un inhibidor selectivo de la tirosina quinasa MET (receptor del factor de crecimiento de hepatocitos, HGF). No se dispone de datos detallados sobre su mecanismo de acción original en los datos recibidos. Su perfil corresponde al de un fármaco de tipo oncológico.

Existe una justificación biológica plausible, pero es solo una hipótesis. La señalización HGF/MET se ha vinculado con la activación de fibroblastos sinoviales, la angiogénesis y el reclutamiento de células inflamatorias en la sinovial reumatoide. Por eso, inhibir MET podría, en teoría, modular estos procesos.

No se aportaron datos preclínicos ni clínicos de capmatinib en artritis reumatoide. El puntaje alto de TxGNN (0.994) es una predicción computacional, no evidencia clínica. La similitud con la indicación original tampoco pudo evaluarse.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Revisión | Pharmacological Research | Actualización 2021 de las propiedades de los inhibidores de proteína quinasas de molécula pequeña aprobados por la FDA. Es una revisión general sin datos específicos de capmatinib en artritis reumatoide. Su relevancia está pendiente de valoración. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1221650002 | Tabrecta 150 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 1221650004 | Tabrecta 200 mg comprimidos recubiertos con película | Comprimido recubierto con película |

Ambas autorizaciones pertenecen a Novartis Europharm Limited. El texto de la indicación aprobada no estaba disponible en los datos recibidos.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de quinasa MET) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se recuperaron interacciones farmacológicas en la consulta realizada.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única base de la predicción es el puntaje del modelo (nivel L5). No hay ensayos clínicos ni literatura específica, y faltan la indicación original, el mecanismo de acción detallado y los datos de seguridad. Por ello no es posible avanzar.

La segunda predicción del modelo, el síndrome de braquidactilia-sindactilia, no tiene vínculo mecanístico identificable, ni ensayos ni literatura. Probablemente sea un artefacto del grafo de conocimiento.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), requisito bloqueante para el cribado de seguridad
- Obtener el mecanismo de acción detallado desde DrugBank
- Confirmar la indicación original aprobada
- Buscar evidencia preclínica de la inhibición de MET en modelos de artritis reumatoide
- Evaluar la compatibilidad de la vía de administración y la similitud con la indicación original

*Los resultados son solo para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


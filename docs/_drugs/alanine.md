---
layout: default
title: Alanine
parent: Solo predicción del modelo (L5)
nav_order: 28
evidence_level: L5
indication_count: 1
---

# Alanine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Alanina: De Indicación Original No Especificada a Gastroparesia

## Resumen en Una Frase

La alanina es un aminoácido no esencial que participa en el ciclo glucosa-alanina y en la gluconeogénesis. En España está autorizada como parte del producto TEBETANE COMPUESTO CÁPSULAS, aunque los datos compilados no recogen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para **gastroparesia**, pero **no hay ensayos clínicos** y solo **3 publicaciones** de contexto general (ninguna evalúa la alanina como tratamiento), por lo que la evidencia es únicamente predictiva.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de la autorización de AEMPS |
| Nueva Indicación Predicha | Gastroparesia |
| Puntaje de Predicción TxGNN | 99,37% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la alanina es un aminoácido no esencial implicado en el ciclo glucosa-alanina y en la gluconeogénesis. No se ha podido confirmar su indicación original en España, por lo que no es posible establecer una relación directa con la nueva indicación.

No se ha establecido un vínculo mecanístico creíble. Una conexión indirecta plausible (nutrición con aminoácidos o modulación glucémica en la gastroparesia diabética) es meramente especulativa y no está respaldada por los datos disponibles. El puntaje de 99,37% es una predicción del modelo y no constituye evidencia clínica.

Las tres publicaciones recuperadas tratan sobre complicaciones hepáticas y gastrointestinales en enfermedad renal y diabetes. Mencionan la gastroparesia como comorbilidad, pero no estudian la alanina como tratamiento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10926110](https://pubmed.ncbi.nlm.nih.gov/10926110/) | 2000 | Revisión | Advances in Renal Replacement Therapy | Describe trastornos gastrointestinales y hepáticos en la enfermedad renal terminal; la gastroparesia es más frecuente en la insuficiencia renal crónica. No evalúa la alanina. |
| [26315331](https://pubmed.ncbi.nlm.nih.gov/26315331/) | 2016 | Revisión | Diabetic Medicine | Describe la hepatosclerosis diabética como posible complicación microvascular de la diabetes. No evalúa la alanina. |
| [33763324](https://pubmed.ncbi.nlm.nih.gov/33763324/) | 2021 | Reporte de caso | Cureus | Caso de hepatopatía por glucógeno en una paciente con diabetes tipo 1 que también presentaba gastroparesia. No evalúa la alanina. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 52469 | TEBETANE COMPUESTO CÁPSULAS | Cápsula dura | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento (no proceden del prospecto)**: el grafo de conocimiento TxGNN (PrimeKG) asocia la alanina con contraindicaciones en las siguientes enfermedades:
  - Renales: enfermedad renal, enfermedad renal crónica, insuficiencia renal crónica, insuficiencia renal terminal, nefrolitiasis, nefrocalcinosis, nefropatía aguda por uratos y piouréter.
  - Metabolismo del calcio y del fósforo: hipercalcemia, hipercalcemia humoral de la malignidad, sarcoidosis y trastornos del metabolismo del fósforo.
  - Cardiovasculares: enfermedad cardíaca, enfermedad cardiovascular, intoxicación digitálica y fibrilación ventricular.
  - Metabolismo de la fenilalanina: fenilcetonuria y trastornos del metabolismo de la fenilalanina.

  Estas asociaciones deben verificarse con la ficha técnica.
- **Interacciones farmacológicas**: no se encontraron datos de interacciones.

Cabe destacar que varias de estas enfermedades (especialmente la enfermedad renal) coinciden con poblaciones en las que la gastroparesia es frecuente, lo que exige especial cautela.

Consultar el prospecto para el resto de la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5). No hay ensayos clínicos, la literatura recuperada no evalúa la alanina en gastroparesia, y no se ha establecido un mecanismo plausible. Además, las contraindicaciones del grafo de conocimiento (renales y cardiovasculares) afectan a poblaciones en las que la gastroparesia es frecuente.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto y la ficha técnica de AEMPS (advertencias, contraindicaciones e indicación aprobada), que es un requisito bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, mediante consulta a DrugBank).
- Aclarar la composición del producto TEBETANE COMPUESTO, ya que es una autorización monocomponente según el registro pero con nombre de compuesto.
- Realizar una búsqueda dirigida de estudios preclínicos o clínicos sobre alanina o aminoácidos en gastroparesia.
- Evaluar la compatibilidad de la vía de administración y la similitud con la indicación original.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Trametinib
parent: Solo predicción del modelo (L5)
nav_order: 538
evidence_level: L5
indication_count: 10
---

# Trametinib
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

# Trametinib: De Melanoma con Mutación BRAF V600 a Coroideremia

## Resumen en Una Frase

Trametinib es un inhibidor de MEK1/2 comercializado en España. Los registros de autorización no incluyen el texto de la indicación original, pero los ensayos asociados lo sitúan en melanoma con mutación BRAF V600. El modelo TxGNN predice que podría ser efectivo para la **coroideremia** (puntaje de 99,31 %), pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de autorización de la AEMPS (los ensayos del fármaco apuntan a melanoma con mutación BRAF V600) |
| Nueva Indicación Predicha | Coroideremia |
| Puntaje de Predicción TxGNN | 99,31 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente consultada. Según la información conocida, trametinib es un inhibidor alostérico de MEK1/2 que bloquea la señalización de la vía MAPK, y su eficacia está comprobada en tumores con activación de esa vía, como el melanoma BRAF-mutante.

La coroideremia es una degeneración retiniana hereditaria causada por la pérdida de función de CHM/REP1. Esta pérdida provoca defectos en la prenilación de las proteínas Rab y la degeneración del epitelio pigmentario de la retina y de los fotorreceptores. **No se ha encontrado un vínculo establecido entre esta enfermedad y la señalización MAPK/MEK.**

Por tanto, el puntaje alto proviene de una predicción basada en el grafo de conocimiento, sin respaldo mecanístico ni clínico. Además, la inhibición crónica de MEK conlleva un riesgo conocido de toxicidad retiniana (retinopatía asociada a inhibidores de MEK), lo que preocupa especialmente en una enfermedad degenerativa de la retina.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 114931002 | MEKINIST 0,5 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 114931006 | MEKINIST 2 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 1231781001 | SPEXOTRAS 0,05 mg/ml polvo para solución oral | Polvo para solución oral |
| 114931006IP | MEKINIST 2 mg comprimidos recubiertos con película | Comprimido recubierto con película |

Todas las autorizaciones pertenecen a Novartis Europharm Limited. Los registros no incluyen el texto de la indicación aprobada.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de MEK1/2) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Examen oftalmológico (por el riesgo de retinopatía asociada a inhibidores de MEK). Para el resto de parámetros, consultar el prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Toxicidad retiniana**: la inhibición crónica de MEK se asocia con retinopatía. Este riesgo es especialmente relevante en una enfermedad degenerativa de la retina como la coroideremia.

Para el resto de la información de seguridad (advertencias, contraindicaciones e interacciones), consultar el prospecto. No se encontraron interacciones farmacológicas registradas.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos, literatura ni vínculo mecanístico con la vía MEK, es decir, se trata solo de una predicción del modelo (L5). El riesgo de toxicidad retiniana del fármaco va en contra de su uso en una enfermedad degenerativa de la retina.

**Para avanzar se necesita:**
- Datos preclínicos que relacionen la vía MAPK/MEK con la fisiopatología de la coroideremia (CHM/REP1 y prenilación de Rab)
- Evaluación del riesgo de retinopatía por inhibidores de MEK en este contexto
- Datos de seguridad del prospecto de la AEMPS y del mecanismo de acción

**Nota:** las predicciones posteriores del modelo, todas ellas subtipos de melanoma, cuentan con más respaldo. Varias alcanzan el nivel L2 gracias a ensayos de Fase 2 y 3 con dabrafenib más trametinib. Si el objetivo es priorizar candidatos con evidencia, conviene evaluarlas por separado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


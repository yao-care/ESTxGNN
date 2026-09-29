---
layout: default
title: Vitamin A
parent: Solo predicción del modelo (L5)
nav_order: 565
evidence_level: L5
indication_count: 10
---

# Vitamin A
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

# Vitamina A: De Indicación Original No Registrada a Deficiencia Congénita de Protrombina

## Resumen en Una Frase

La vitamina A es un nutriente liposoluble comercializado en España en pomadas nasales y cápsulas. Los datos de autorización disponibles no indican su indicación original.
El modelo TxGNN predice que podría ser efectiva para la **deficiencia congénita de protrombina**, pero **ninguno de los 5 ensayos clínicos** asociados evalúa vitamina A y **no hay publicaciones** que respalden esta dirección. La predicción parece ser un artefacto del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de autorización |
| Nueva Indicación Predicha | Deficiencia congénita de protrombina |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la vitamina A es un nutriente esencial y precursor de los retinoides, y su papel en la visión, la función epitelial y la diferenciación celular está bien establecido. No hay una razón mecanística que la conecte con la deficiencia de protrombina.

La protrombina (factor II) es una proteína de la coagulación **dependiente de la vitamina K**, no de la vitamina A. No existe una relación establecida entre la vitamina A y la síntesis o función de la protrombina.

El puntaje TxGNN es muy alto (0.9997), pero probablemente refleja la proximidad entre nodos del grafo de conocimiento (por ejemplo, nodos de "vitaminas") y no un vínculo terapéutico real. Por eso la predicción debe tratarse con mucha cautela.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03534752](https://clinicaltrials.gov/study/NCT03534752) | N/A | Completado | 220 | Estudio retrospectivo de adultos con errores congénitos del metabolismo en Suiza francófona. No incluye intervención con vitamina A |
| [NCT02392767](https://clinicaltrials.gov/study/NCT02392767) | N/A | Completado | 25 | Suplemento dietético combinado (L-arginina, Pycnogenol, vitamina K2, vitaminas B) sobre la función endotelial en hipertensión. No guarda relación con la indicación |
| [NCT04384341](https://clinicaltrials.gov/study/NCT04384341) | N/A | Completado | 448 | Pérdida ósea en hemofilia (estudio PHILEOS). No es deficiencia de protrombina ni evalúa vitamina A |
| [NCT00168077](https://clinicaltrials.gov/study/NCT00168077) | Fase 3 | Completado | 40 | Beriplex P/N (concentrado de complejo de protrombina) en deficiencia adquirida de factores II, VII, IX y X por anticoagulación oral. No evalúa vitamina A y no es congénita |
| [NCT00562783](https://clinicaltrials.gov/study/NCT00562783) | Fase 2 | Completado | 90 | Ensayo aleatorizado doble ciego de "Vitalliver" en cirrosis descompensada. No se identifica la vitamina en los datos y no se confirma vínculo con la coagulación |

Los 5 ensayos fueron clasificados con relevancia baja (grado C).

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 28811 | RINOCUSI VITAMÍNICO 12.500 UI/g POMADA NASAL | Pomada nasal |
| 24328 | AUXINA A MASIVA 50.000 UI CÁPSULAS BLANDAS | Cápsula dura |
| 66883 | RINOVITEX 12.500 UI/g POMADA NASAL | Pomada nasal |

Los registros no incluyen texto de indicación aprobada.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5). No hay ensayos con vitamina A ni literatura, y la protrombina depende de la vitamina K. El puntaje alto parece un artefacto del grafo de conocimiento.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un vacío de datos bloqueante para cualquier evaluación de seguridad
- Obtener datos del mecanismo de acción desde DrugBank
- Confirmar la indicación aprobada de cada autorización en España
- Revisar la lista completa de predicciones. Entre ellas, la de **enfermedad perinatal** tiene evidencia más sólida (ECA de Fase 3 y revisiones Cochrane), aunque corresponde a un uso ya establecido más que a un reposicionamiento novedoso, y requiere límites de población y dosis por la teratogenicidad de la vitamina A a dosis altas.

*Este informe es solo para fines de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


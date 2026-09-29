---
layout: default
title: Roxadustat
parent: Solo predicción del modelo (L5)
nav_order: 478
evidence_level: L5
indication_count: 4
---

# Roxadustat
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Roxadustat: De Anemia Renal a Síndrome de Ojo Seco

## Resumen en Una Frase

Roxadustat es un inhibidor de la prolil-hidroxilasa del HIF, comercializado en España como EVRENZO y utilizado en la anemia asociada a enfermedad renal. Esta indicación no figura en el texto de las autorizaciones y procede del conocimiento general y del contexto del ensayo identificado.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de ojo seco**, pero solo hay **1 ensayo clínico** observacional e indirecto y **ninguna publicación** que lo respalde.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Anemia asociada a enfermedad renal (por conocimiento general; el texto de indicación de las autorizaciones está vacío) |
| Nueva Indicación Predicha | Síndrome de ojo seco |
| Puntaje de Predicción TxGNN | 99.51% |
| Nivel de Evidencia | L5 (solo predicción del modelo; el único ensayo es indirecto) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente. Según el conocimiento general, roxadustat inhibe la prolil-hidroxilasa del HIF y estabiliza el HIF-alfa. Esto estimula la producción endógena de eritropoyetina, lo que explica su uso en la anemia renal.

La relación con el ojo seco es hipotética. La vía HIF podría modular la inflamación de la superficie ocular y la función de las glándulas de Meibomio. Ningún dato directo respalda esta idea.

El único ensayo identificado estudia las glándulas de Meibomio en pacientes con anemia renal, población que puede recibir roxadustat. Su título no confirma que el fármaco sea la exposición estudiada. Podría reflejar el efecto de la enfermedad de base y no del fármaco. El puntaje TxGNN (0.995) es una predicción computacional y no constituye evidencia clínica.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06287879](https://clinicaltrials.gov/study/NCT06287879) | N/A (observacional) | Desconocido | 50 | Función y morfología de las glándulas de Meibomio en pacientes con anemia renal y síntomas de ojo seco. Sin resultados publicados. Evidencia indirecta (grado C); no evalúa la eficacia de roxadustat en el ojo seco. |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1211574001 | EVRENZO 20 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en los datos |
| 1211574002 | EVRENZO 50 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en los datos |
| 1211574003 | EVRENZO 70 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en los datos |
| 1211574004 | EVRENZO 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en los datos |
| 1211574005 | EVRENZO 150 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en los datos |

Titular: Astellas Pharma Europe B.V. Solo se identificó la vía oral.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en los datos disponibles.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita a una predicción del modelo y a un estudio observacional indirecto, sin literatura ni ensayos que evalúen roxadustat en el ojo seco. Faltan además los datos de seguridad de la ficha técnica de la AEMPS, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de la AEMPS (advertencias y contraindicaciones), un bloqueo actual.
- Obtener el mecanismo de acción detallado desde DrugBank.
- Verificar en el registro de ClinicalTrials.gov si roxadustat es la exposición definida en NCT06287879.
- Buscar respaldo preclínico de la vía HIF en la superficie ocular y las glándulas de Meibomio.
- Definir la vía de administración: la forma comercializada es oral y no hay datos sobre formulación oftálmica.

**Nota sobre otras predicciones del modelo:** las predicciones siguientes (enfermedad ósea de Paget, dentinogénesis imperfecta y carcinoma escamoso) tienen nivel L5 y ninguna evidencia clínica. En el carcinoma escamoso, la estabilización del HIF plantea más bien una preocupación de seguridad oncológica que un beneficio potencial.

*Este informe es solo de referencia para la investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


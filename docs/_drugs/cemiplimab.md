---
layout: default
title: Cemiplimab
parent: Solo predicción del modelo (L5)
nav_order: 114
evidence_level: L5
indication_count: 10
---

# Cemiplimab
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

# Cemiplimab: De Indicación Original No Especificada a Carcinoma Adenoescamoso de Vesícula Biliar

## Resumen en Una Frase

Cemiplimab (comercializado en España como LIBTAYO) es un inhibidor de PD-1. Los datos suministrados no incluyen su indicación original aprobada.
El modelo TxGNN predice que podría ser efectivo para **carcinoma adenoescamoso de vesícula biliar**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, por lo que es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (el texto de indicación aprobada de la autorización está vacío) |
| Nueva Indicación Predicha | Carcinoma adenoescamoso de vesícula biliar |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información del análisis, cemiplimab es un anticuerpo que bloquea PD-1 (un inhibidor del punto de control inmunitario). Este bloqueo puede restaurar la actividad antitumoral de los linfocitos T.

El carcinoma adenoescamoso de vesícula biliar combina un componente glandular y uno escamoso. El bloqueo de PD-1 podría actuar sobre el componente escamoso. Sin embargo, esta histología mixta es muy poco frecuente y no hay ningún ensayo ni publicación en los datos suministrados. Por eso el vínculo mecanístico sigue sin confirmarse.

El puntaje de TxGNN es muy alto (0.9999), pero es una señal del modelo, no una prueba clínica. La similitud con la indicación original está pendiente de evaluar, porque esa indicación no figura en los datos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

**Nota sobre otras predicciones:** entre las 10 indicaciones predichas, solo una tiene literatura. Para el carcinoma basocelular del oído externo (puesto 4, nivel L4) hay un reporte de caso: [34157152](https://pubmed.ncbi.nlm.nih.gov/34157152/) (2021, *Clinical and Experimental Dermatology*). Describe una respuesta duradera tras suspender cemiplimab en un paciente con carcinoma basocelular localmente avanzado. Es una observación aislada que solo genera hipótesis y no es específica del oído externo.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191376001 | LIBTAYO 350 MG CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Concentrado para solución para perfusión | No especificada en los datos |

Titular: Regeneron Ireland Designated Activity Company.

## Citotoxicidad

Cemiplimab es un fármaco antineoplásico (inmunoterapia anti-PD-1). Los datos suministrados no incluyen categorías de DrugBank ni datos de toxicidad, por lo que la clasificación se basa en el tipo de fármaco.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (inhibidor del punto de control PD-1), no citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto (en general, hemograma y funciones hepática, renal y tiroidea) |
| Protección en Manejo | Consultar el prospecto y los procedimientos del centro para el manejo de medicamentos oncológicos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. La búsqueda de interacciones farmacológicas no devolvió resultados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni literatura (nivel L5, etapa S0), y faltan datos bloqueantes de seguridad del prospecto de la AEMPS. Con este respaldo no se puede avanzar más allá de una hipótesis del modelo.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un vacío de datos bloqueante
- Obtener el mecanismo de acción y la indicación original aprobada (consulta a DrugBank y a la ficha técnica)
- Buscar ensayos y literatura específicos del carcinoma adenoescamoso de vesícula biliar, incluidos reportes de caso y series retrospectivas
- Valorar priorizar el carcinoma basocelular del oído externo (L4, "Research Question"), donde ya existe un reporte de caso

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


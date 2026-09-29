---
layout: default
title: Niraparib
parent: Solo predicción del modelo (L5)
nav_order: 382
evidence_level: L5
indication_count: 10
---

# Niraparib
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

# Niraparib: De Cáncer de Ovario a Neoplasia de Epiglotis

## Resumen en Una Frase

Niraparib es un inhibidor de PARP. Según la literatura recuperada, está aprobado como tratamiento de mantenimiento en cáncer de ovario recurrente sensible a platino.
El modelo TxGNN predice que podría ser efectivo para **Neoplasia de Epiglotis**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción concreta: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en el registro de AEMPS (texto de indicación vacío). La literatura recuperada lo describe como mantenimiento en cáncer de ovario recurrente sensible a platino |
| Nueva Indicación Predicha | Neoplasia de epiglotis |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Niraparib es un inhibidor de PARP que actúa por letalidad sintética en tumores con deficiencia de recombinación homóloga (HRD), como los que tienen mutaciones en BRCA. Al bloquear la reparación del ADN dependiente de PARP, las células tumorales incapaces de repararlo por otra vía mueren. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank, así que esta descripción proviene del análisis de racionalidad del propio paquete de evidencia.

La relación con la nueva indicación es **especulativa**. No hay datos de HRD ni de BRCA para tumores de epiglotis, y no se recuperó ningún ensayo ni publicación que vincule niraparib con esta neoplasia. La puntuación alta de TxGNN (99.99%) refleja la cercanía del fármaco con enfermedades oncológicas en el grafo de conocimiento. No es una prueba de eficacia. Además, casi todas las predicciones de este fármaco tienen puntuaciones muy parecidas (entre 99.98% y 99.99%), por lo que el puntaje por sí solo no permite priorizar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1171235001 | ZEJULA 100 MG CAPSULAS DURAS | Cápsula dura |
| 1171235006 | ZEJULA 100 MG COMPRIMIDOS RECUBIERTOS CON PELICULA | Comprimido recubierto con película |

Ambas autorizaciones pertenecen a Glaxosmithkline Trading Services Limited. El registro recuperado no incluye el texto de indicación aprobada.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de PARP) |
| Riesgo de Mielosupresión | Medio a alto. El paquete de evidencia señala su toxicidad hematológica (trombocitopenia, anemia y neutropenia son las más reportadas para esta clase) |
| Clasificación de Emetogenicidad | Baja a moderada (criterio general de la clase, no proviene del paquete) |
| Items de Monitoreo | Hemograma completo, función hepática y renal, presión arterial |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para neoplasia de epiglotis es solo del modelo (L5): no hay ensayos, literatura ni datos de HRD/BRCA que la respalden. Además, faltan los datos de seguridad del prospecto de AEMPS, que bloquean el cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones)
- Completar los datos de mecanismo de acción desde DrugBank
- Buscar literatura y ensayos específicos sobre niraparib o inhibidores de PARP en tumores de cabeza y cuello
- Evaluar el estado de HRD/BRCA en neoplasias de epiglotis

**Nota:** entre las otras predicciones, la de *neoplasia quística* (puesto 2) tiene mejor respaldo (L3, etapa S1, "Research Question"). Incluye el ensayo de fase 2 NCT04716686 (niraparib en carcinoma seroso de endometrio, 83 participantes, en reclutamiento) y literatura sobre carcinomas serosos. Aun así, ese respaldo es indirecto y no tiene resultados publicados, por lo que merece evaluarse por separado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


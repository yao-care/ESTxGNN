---
layout: default
title: Axitinib
parent: Solo predicción del modelo (L5)
nav_order: 58
evidence_level: L5
indication_count: 10
---

# Axitinib
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

# Axitinib: De Carcinoma de Células Renales Avanzado a Carcinoma Renal con Translocaciones Xp11.2/Fusiones del Gen TFE3

## Resumen en Una Frase

Axitinib es un inhibidor de tirosina quinasa dirigido a los receptores VEGFR1-3. Se comercializa en España y, según el Evidence Pack, su indicación establecida es el carcinoma de células renales.
El modelo TxGNN predice que podría ser efectivo para el **carcinoma renal asociado a translocaciones Xp11.2/fusiones del gen TFE3**, un subtipo raro de carcinoma renal.
Esta dirección la respalda **1 ensayo clínico** (Fase 2, aleatorizado, 15 pacientes, sin resultados) y **ninguna publicación** específica.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en las autorizaciones españolas (el campo de indicación está vacío). El Evidence Pack señala el carcinoma de células renales como su indicación comercializada establecida |
| Nueva Indicación Predicha | Carcinoma renal asociado a translocaciones Xp11.2/fusiones del gen TFE3 |
| Puntaje de Prediccion TxGNN | 99.90% |
| Nivel de Evidencia | L5 según las reglas de este informe (el único ensayo no está completado y no hay resultados). El Evidence Pack asigna L2 |
| Estado de Mercado en Espana | ✓ Comercializado |
| Numero de Autorizaciones | 9 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información disponible en el análisis, axitinib inhibe de forma selectiva los receptores VEGFR1, VEGFR2 y VEGFR3, con lo que bloquea la angiogénesis tumoral.

El carcinoma renal con fusiones TFE3 tiene un fenotipo angiogénico ligado a las vías MET y VEGF. Por eso el bloqueo de VEGFR es plausible por extrapolación desde el carcinoma renal de células claras, donde el uso de axitinib ya está establecido. El ensayo registrado añade nivolumab (bloqueo de PD-1) a axitinib.

Esta predicción es más una **extensión a un subtipo histológico** que un reposicionamiento hacia una enfermedad distinta. El propio Evidence Pack indica que el vacío en las indicaciones originales probablemente refleja datos de origen incompletos. Además, no hay resultados publicados en este subtipo, que es muy raro, y la extrapolación desde el adulto con células claras es incierta.

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Fase 2 | Activo, sin reclutar | 15 | Ensayo aleatorizado de axitinib + nivolumab frente a nivolumab en monoterapia en carcinoma renal con translocación TFE (irresecable o metastásico), en todas las edades. Fecha estimada de finalización: 13/11/2026. Sin resultados publicados. Muestra muy pequeña: no permite concluir sobre eficacia |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación específica.

## Informacion de Mercado en Espana

Se muestran 5 de las 9 autorizaciones. El texto de indicación aprobada está vacío en todas las fuentes recibidas, por lo que no se incluye esa columna.

| Numero de Autorizacion | Nombre del Producto | Forma Farmaceutica | Titular |
|---------|------|------|-----------|
| 12777005 | INLYTA 5 mg comprimidos recubiertos con película | Comprimido recubierto con película | Pfizer Europe MA EEIG |
| 1241847009 | Axitinib Accord 3 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Accord Healthcare S.L.U. |
| 1241847014 | Axitinib Accord 5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Accord Healthcare S.L.U. |
| 89675 | Axitinib Teva 5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Teva Pharma S.L.U. |
| 88718 | Axitinib Stada 5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Laboratorio Stada S.L. |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificacion de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa de VEGFR1-3) |
| Riesgo de Mielosupresion | Consultar las advertencias y precauciones del prospecto |
| Clasificacion de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Proteccion en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
Para este subtipo solo existe un ensayo de Fase 2 pequeño (n=15), aún sin resultados ni publicaciones, y no hay datos de seguridad del prospecto español. Con la información actual no se puede pasar a una fase de decisión más avanzada. Por separado, el uso de axitinib en carcinoma renal en general sí cuenta con ensayos de Fase 3 (por ejemplo AXIS y JAVELIN Renal 101), pero eso corresponde a su indicación establecida y no a esta predicción.

**Para avanzar se necesita:**
- Resultados del ensayo NCT03595124 (finalización estimada en noviembre de 2026).
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones) para completar la evaluación de seguridad.
- Obtener el mecanismo de acción detallado desde DrugBank.
- Confirmar la indicación original aprobada en España, ya que el texto de indicación está vacío en las 9 autorizaciones.
- Revisar la literatura sobre axitinib en carcinoma renal de niños y adultos jóvenes (por ejemplo, la revisión narrativa PMID 39326645, identificada en otras predicciones del mismo farmaco), como apoyo indirecto.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


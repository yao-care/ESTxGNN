---
layout: default
title: Obinutuzumab
parent: Solo predicción del modelo (L5)
nav_order: 387
evidence_level: L5
indication_count: 3
---

# Obinutuzumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Obinutuzumab: De Indicación Original No Registrada a Leucemia Linfocítica Crónica/Linfoma Linfocítico de Células Pequeñas (CLL/SLL) de Centro Pregerminal

## Resumen en Una Frase

Obinutuzumab es un anticuerpo monoclonal anti-CD20, comercializado en España como Gazyvaro. El paquete de datos no incluye su indicación original.
El modelo TxGNN predice que podría ser efectivo para la **leucemia linfocítica crónica/linfoma linfocítico de células pequeñas de centro pregerminal**, pero para este subtipo hay **0 ensayos clínicos** y **0 publicaciones** en el paquete. La predicción se apoya solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos recibidos (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Leucemia linfocítica crónica/linfoma linfocítico de células pequeñas de centro pregerminal |
| Puntaje de Predicción TxGNN | 99.21% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Obinutuzumab es un anticuerpo anti-CD20 tipo II glicoingenierizado. Actualmente no se dispone de datos detallados sobre su mecanismo de acción en el paquete de datos. Las células de CLL/SLL expresan CD20, así que la relación con la diana del fármaco es biológicamente plausible.

Esta predicción no equivale a una prueba de eficacia. La falta de ensayos y literatura para este subtipo refleja un vacío de cobertura de datos, no evidencia de ausencia de efecto. Además, obinutuzumab ya se usa como tratamiento de CLL, por lo que la predicción podría ser un "redescubrimiento" de una indicación existente y no un reposicionamiento genuino. Esto debe verificarse contra la ficha técnica y los ensayos pivotales.

El modelo también predijo un subtipo hermano con mutación somática hipermutada de IGHV, con exactamente el mismo puntaje (0.992). Es probable que ambas entradas sean duplicados a nivel de ontología de la misma enfermedad. Una evaluación real requeriría evidencia de CLL mapeada a la enfermedad padre y datos estratificados por IGHV.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación predicha.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación predicha.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 114937001 | GAZYVARO 1000 MG concentrado para solución para perfusión | Concentrado para solución para perfusión | Roche Registration GmbH |
| 114937001IP | GAZYVARO 1000 MG concentrado para solución para perfusión | Concentrado para solución para perfusión | Roche Registration GmbH |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida / inmunoterapia (anticuerpo monoclonal anti-CD20) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto (en la evidencia asociada se recomienda vigilar citopenias) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, reacciones a la perfusión, infecciones, reactivación del VHB |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para este subtipo solo hay predicción del modelo (L5), sin ensayos ni literatura en el paquete. Además, probablemente se trate de un uso ya existente y no de un reposicionamiento nuevo.

En el mismo paquete, la indicación de **linfoma folicular** (puesto 3, puntaje 99.18%) sí cuenta con evidencia de nivel L1 y recomendación "Proceed with Guardrails". Incluye el ensayo de Fase 3 GALLIUM (PMID 28976863 y 29856692), el ensayo aleatorizado de Fase 2 ROSEWOOD y varios estudios de combinación con lenalidomida. Sin embargo, obinutuzumab ya está comercializado para linfoma folicular, por lo que esto valida un uso existente y no un reposicionamiento novedoso. Esa indicación merece un informe propio.

**Para avanzar se necesita:**
- Confirmar la indicación autorizada en la ficha técnica de la AEMPS (el texto de indicación está vacío en los datos)
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones)
- Datos del mecanismo de acción desde DrugBank
- Mapear la evidencia de CLL/SLL a la enfermedad padre y a datos estratificados por IGHV
- Verificar contra ensayos pivotales si esta entrada es un redescubrimiento de una indicación ya autorizada
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


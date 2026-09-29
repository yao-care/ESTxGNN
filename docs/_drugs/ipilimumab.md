---
layout: default
title: Ipilimumab
parent: Solo predicción del modelo (L5)
nav_order: 291
evidence_level: L5
indication_count: 2
---

# Ipilimumab
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

# Ipilimumab: De Inmunoterapia Anti-CTLA-4 a Coroideremia

## Resumen en Una Frase

Ipilimumab es un anticuerpo que bloquea CTLA-4 y activa los linfocitos T. Es un fármaco de inmunoterapia oncológica y está comercializado en España como Yervoy.
El modelo TxGNN predice que podría ser efectivo para **coroideremia**, con un puntaje muy alto, pero **sin ningún ensayo clínico ni publicación** que respalde esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Coroideremia |
| Puntaje de Predicción TxGNN | 99.06% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

**No se identifica un vínculo mecanístico plausible.** Ipilimumab bloquea CTLA-4, un freno del sistema inmunitario, y así potencia la activación de los linfocitos T. Este mecanismo está bien validado en oncología.

La coroideremia es una degeneración retiniana hereditaria ligada al cromosoma X. Se debe a la pérdida de función del gen *CHM* (proteína REP1). No la causa una tolerancia inmunitaria mediada por linfocitos T, así que potenciar la respuesta T no tiene un blanco biológico claro en esta enfermedad.

Además, el bloqueo sistémico de puntos de control inmunitarios puede provocar eventos adversos inmunomediados, incluida la uveítis. Eso podría dañar una retina que ya se está degenerando. El puntaje alto de TxGNN (0.99) probablemente es un artefacto del grafo de conocimiento, porque no lo respalda ningún ensayo ni publicación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 11698001 | YERVOY 5 MG/ML CONCENTRADO PARA SOLUCION PARA PERFUSION | Concentrado para solución para perfusión |
| 11698002 | YERVOY 5 MG/ML CONCENTRADO PARA SOLUCION PARA PERFUSION | Concentrado para solución para perfusión |
| 11698001IP | YERVOY 5 MG/ML CONCENTRADO PARA SOLUCION PARA PERFUSION | Concentrado para solución para perfusión |

Titular de las tres autorizaciones: Bristol-Myers Squibb Pharma EEIG.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (inhibidor de punto de control inmunitario anti-CTLA-4) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Eventos adversos inmunomediados**: el bloqueo sistémico de CTLA-4 conlleva riesgo de eventos adversos inmunomediados, incluida la uveítis. En una enfermedad retiniana degenerativa como la coroideremia, este riesgo es especialmente relevante.

Para el resto de la información de seguridad (advertencias, contraindicaciones e interacciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para coroideremia es solo un resultado del modelo (L5). No hay ensayos ni literatura, y no existe un vínculo mecanístico plausible. Además, existe un riesgo de toxicidad ocular inmunomediada.

**Para avanzar se necesita:**
- Una hipótesis mecanística que justifique el bloqueo de CTLA-4 en una enfermedad no dependiente de la tolerancia inmunitaria de linfocitos T
- Datos preclínicos que respalden la hipótesis
- Datos de mecanismo de acción y de seguridad del prospecto de la AEMPS

**Nota sobre la segunda predicción:** TxGNN también propone **melanoma no cutáneo** (puntaje 99.02%). Esa predicción sí cuenta con respaldo, con nivel de evidencia L3 y recomendación *Proceed with Guardrails*.

- **Ensayos clínicos:** el registro incluye decenas de ensayos en melanoma, entre ellos ensayos de Fase 3. La mayoría enrolan melanoma cutáneo, por lo que son evidencia indirecta.
- **Literatura:** hay 5 publicaciones. La única con datos directos en subtipos no cutáneos es un estudio de cohorte retrospectivo en melanoma cutáneo, uveal y mucoso (PMID 24999899).
- **Salvaguardas:** confirmar el subtipo de melanoma, exigir resultados estratificados por subtipo, vigilar los eventos adversos inmunomediados y preferir combinaciones con un inhibidor de PD-1 cuando los datos las respalden.

Este resultado merece una evaluación separada.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


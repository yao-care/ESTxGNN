---
layout: default
title: Mogamulizumab
parent: Solo predicción del modelo (L5)
nav_order: 363
evidence_level: L5
indication_count: 7
---

# Mogamulizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Mogamulizumab: De Linfoma Cutáneo de Células T a Carcinoma Urotelial de la Uretra Prostática

## Resumen en Una Frase

Mogamulizumab es un anticuerpo monoclonal anti-CCR4 comercializado en España como Poteligeo. La ficha de AEMPS del Evidence Pack no incluye el texto de la indicación, pero el contexto del fármaco apunta al linfoma cutáneo de células T.
El modelo TxGNN predice que podría ser efectivo para **carcinoma urotelial de la uretra prostática**, pero por ahora hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consignada en el registro de AEMPS (el contexto del fármaco apunta a linfoma cutáneo de células T) |
| Nueva Indicación Predicha | Carcinoma urotelial de la uretra prostática |
| Puntaje de Predicción TxGNN | 99,44% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Mogamulizumab se dirige a CCR4, un receptor de quimiocinas presente en ciertas células T. Su actividad conocida en linfoma cutáneo de células T (micosis fungoide y síndrome de Sézary) sugiere una posible aplicabilidad mecanística en otros tumores.

Una hipótesis especulativa es que el fármaco elimine las células T reguladoras (Treg) CCR4+, lo que podría reducir la supresión inmunitaria en el microambiente tumoral del cáncer urotelial. Esta hipótesis **no está respaldada por los datos suministrados** y no hay evidencia clínica. Sería una pregunta preclínica razonable, por ejemplo evaluar la expresión de CCR4 en tejido tumoral urotelial.

La relación de similitud con la indicación original aún está pendiente de análisis. La compatibilidad de vía de administración también está pendiente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1181335001 | POTELIGEO 4 MG/ML CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Concentrado para solución para perfusión | No consignada en el registro |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-CCR4) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5, etapa S0), sin ensayos ni literatura. El mecanismo propuesto es hipotético y los datos de seguridad de AEMPS no están disponibles.

**Para avanzar se necesita:**
- Obtener del prospecto de AEMPS las advertencias y contraindicaciones, un vacío bloqueante para el cribado de seguridad.
- Confirmar el mecanismo de acción (MOA) en DrugBank.
- Confirmar la indicación aprobada en España.
- Buscar ensayos y literatura sobre CCR4 y Treg en carcinoma urotelial.
- Evaluar de forma preclínica la expresión de CCR4 en tejido tumoral urotelial.
- Realizar una revisión de seguridad por el riesgo teórico de inmunosupresión.

Las otras seis predicciones del modelo (todas con puntaje superior a 99% y nivel L5) también carecen de evidencia y quedan en Hold. Entre ellas, el tumor relacionado con el herpesvirus humano 8 requeriría además una revisión específica del riesgo de reactivación viral o infección.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


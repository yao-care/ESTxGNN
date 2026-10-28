---
layout: default
title: Inclisiran
parent: Solo predicción del modelo (L5)
nav_order: 412
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Inclisiran: nueva indicación predicha, Deficiencia de potasio (potassium deficiency disease) (nivel de evidencia L5). Indicación original: No disponible en los datos de las autorizaciones de la AEMPS"
monitor_inn: "inclisiran"
predicted_indications: ["potassium deficiency disease", "esophageal disease", "atypical coarctation of aorta", "migraine disorder", "non-syndromic esophageal malformation", "migraine with brainstem aura", "aortic malformation", "esophageal ulcer", "Raynaud disease"]
---

# Inclisiran
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Inclisirán: De Hipercolesterolemia a Deficiencia de Potasio (predicción del modelo)
{: .text-alpha }

## Resumen en Una Frase

Inclisirán es un ARN de interferencia pequeño (siRNA) dirigido contra PCSK9 y comercializado en España como LEQVIO. Los datos compilados para este report no incluyen el texto de la indicación autorizada, pero el fármaco se utiliza para reducir el colesterol LDL.
El modelo TxGNN predice que podría ser efectivo para **deficiencia de potasio**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de las autorizaciones de la AEMPS |
| Nueva Indicación Predicha | Deficiencia de potasio (potassium deficiency disease) |
| Puntaje de Predicción TxGNN | 0,9993 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 2 de 2) |
| Número de Autorizaciones | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, inclisirán es un siRNA que silencia PCSK9 en el hígado, lo que aumenta la expresión de receptores de LDL hepáticos y reduce el colesterol LDL.

No se ha identificado un vínculo mecanístico plausible entre este mecanismo y la homeostasis del potasio. El puntaje elevado (0.9993) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Por ello, esta predicción debe considerarse una hipótesis sin fundamento mecanístico actual, y no una indicación razonable para reposicionamiento.

Otras predicciones del modelo (todas con nivel L5 y recomendación Hold) incluyen enfermedad esofágica, coartación atípica de aorta, migraña y enfermedad de Raynaud. Ninguna cuenta con evidencia directa. En el caso de la malformación aórtica, aparecen dos ensayos de Fase 3 que, por su diseño, estudian hipercolesterolemia familiar pediátrica y no esa enfermedad.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para deficiencia de potasio.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1201494001 | LEQVIO 284 mg solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No disponible |
| 1201494001IP | LEQVIO 284 mg solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No disponible |

Titular: Novartis Europharm Limited.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para deficiencia de potasio se basa solo en el modelo (L5), sin ensayos, sin literatura y sin vínculo mecanístico plausible con el silenciamiento de PCSK9. No hay base para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y una hipótesis biológica que conecte PCSK9 con la homeostasis del potasio
- Datos de seguridad del prospecto de la AEMPS (advertencias y contraindicaciones), actualmente sin disponer
- Texto de la indicación autorizada para establecer la relación con la indicación original
- Estudios preclínicos o series observacionales que respalden la hipótesis
- Verificar en el registro los dos ensayos de Fase 3 pediátricos asociados a malformación aórtica, que parecen coincidencias de ontología y no evidencia real
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


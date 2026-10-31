---
layout: default
title: Amylmetacresol
parent: Solo predicción del modelo (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
description: "Amylmetacresol: nueva indicación predicha, Síndrome de la cauda equina (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "amylmetacresol"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "ciliary body disease", "panuveitis (disease)", "iris disease", "infectious anterior uveitis", "uveitis", "ciliary body cancer", "benign neoplasm of ciliary body"]
---

# Amylmetacresol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Amilmetacresol: De Indicación Original No Especificada a Síndrome de la Cauda Equina
{: .text-alpha }

## Resumen en Una Frase

Amilmetacresol es un antiséptico de uso local que se comercializa en pastillas para chupar y en solución para pulverización bucal, y se emplea habitualmente en preparados para la garganta.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de la cauda equina**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Síndrome de la cauda equina |
| Puntaje de Predicción TxGNN | 0,9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 14) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, amilmetacresol es un antiséptico de acción local que se utiliza en pastillas para la garganta, a menudo combinado con otros principios activos (como diclorobencil alcohol o lidocaína en algunos productos), con exposición sistémica mínima.

En este caso, **la predicción no resulta razonable desde el punto de vista farmacológico**. El síndrome de la cauda equina es una urgencia neurológica compresiva que se trata mediante cirugía, y no existe una justificación plausible para un antiséptico bucofaríngeo. No se ha establecido ningún vínculo mecanístico.

El puntaje elevado del modelo (0,9999) es únicamente una predicción computacional y probablemente refleja artefactos del modelo TxGNN (aprendizaje profundo). Otras predicciones del mismo modelo (síndrome del intestino irritable, uveítis, enfermedades del cuerpo ciliar, entre otras) presentan puntajes similares y tampoco cuentan con ningún respaldo clínico o bibliográfico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de producto con un único principio activo). Los textos de indicación aprobada no están disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 78850 | Bucomax pastillas para chupar sabor menta | Pastilla para chupar | No disponible |
| 61935 | Strepsils pastillas para chupar sabor fresa | Pastilla para chupar | No disponible |
| 80162 | Geisil 0,6 mg/1,2 mg pastillas para chupar sabor menta | Pastilla para chupar | No disponible |
| 63896 | Strepsils con lidocaína pastillas para chupar | Pastilla para chupar | No disponible |
| 85434 | Farinstop spray solución para pulverización bucal | Solución para pulverización bucal | No disponible |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se identificaron interacciones farmacológicas en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos, literatura ni vínculo mecanístico plausible. Además, la vía y la formulación actuales (uso local bucofaríngeo) no son compatibles con la patología predicha.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), actualmente no disponible
- Obtener datos del mecanismo de acción desde DrugBank
- Disponer de evidencia preclínica o clínica que justifique un vínculo con la indicación predicha
- Evaluar la compatibilidad de vía de administración y formulación con la nueva indicación
- Valorar si alguna de las otras predicciones (p. ej., síndrome del intestino irritable) cuenta con un fundamento mecanístico más defendible antes de invertir recursos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


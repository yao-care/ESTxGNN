---
layout: default
title: Pioglitazone
parent: Solo predicción del modelo (L5)
nav_order: 640
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-31
description: "Pioglitazone: nueva indicación predicha, Opsismodisplasia (nivel de evidencia L5). Indicación original: Diabetes mellitus tipo 2"
monitor_inn: "Pioglitazone"
predicted_indications: ["opsismodysplasia", "classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Pioglitazone
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

## Pioglitazona: De Diabetes Mellitus Tipo 2 a Opsismodisplasia
{: .text-alpha }

## Resumen en Una Frase

Pioglitazona es un agonista de PPAR-gamma (tiazolidindiona) utilizado originalmente para el tratamiento de la diabetes mellitus tipo 2.
El modelo TxGNN predice que podría ser efectivo para **opsismodisplasia**, una displasia esquelética rara,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diabetes mellitus tipo 2 |
| Nueva Indicación Predicha | Opsismodisplasia |
| Puntaje de Predicción TxGNN | 0.9959 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 8) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, pioglitazona es un agonista del receptor activado por proliferadores de peroxisomas gamma (PPARG), lo que se confirma en los datos de farmacología recopilados (que también muestran interacción con TRPM3). Su eficacia en diabetes tipo 2 como sensibilizador de insulina está bien establecida.

Para la opsismodisplasia, **no se identifica un vínculo mecanístico respaldado por los datos**. Esta enfermedad es una displasia esquelética rara asociada a variantes del gen INPPL1, y su relación con la activación de PPAR-gamma no está establecida. El puntaje elevado del modelo (0.9959) es únicamente una predicción computacional, sin ensayos ni literatura que la corroboren.

Cabe señalar que el modelo generó otras predicciones con puntajes similares (síndrome de la persona rígida clásico y focal, síndrome de disfunción sensible a tiamina, varias lipodistrofias localizadas y agenesia pancreática). Entre ellas, las lipodistrofias tienen una justificación biológica teórica por el papel de PPAR-gamma en el tejido adiposo, aunque tampoco cuentan con evidencia clínica. Todas permanecen en nivel L5 y decisión Hold.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la opsismodisplasia.

---

## Información de Mercado en España

Pioglitazona está comercializada en España con 20 autorizaciones vigentes (todas de monofármaco, ninguna cancelada), en forma de comprimidos. Se muestran las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 00150005 | ACTOS 30 mg COMPRIMIDOS (Cheplapharm) | Comprimido | No disponible en los datos |
| 76481 | PIOGLITAZONA CINFA 15 MG COMPRIMIDOS EFG | Comprimido | No disponible en los datos |
| 00150010IP | ACTOS 30 MG COMPRIMIDOS (Takeda) | Comprimido | No disponible en los datos |
| 00151001 | GLUSTIN 15 mg COMPRIMIDOS | Comprimido | No disponible en los datos |
| 76275 | PIOGLITAZONA AUROBINDO 15 MG COMPRIMIDOS EFG | Comprimido | No disponible en los datos |

---

## Consideraciones de Seguridad

No se dispone de advertencias ni contraindicaciones extraídas del prospecto. Consultar el prospecto para información de seguridad completa.

- **Contraindicaciones según el grafo de conocimiento (no proviene del prospecto)**: el grafo de conocimiento asocia pioglitazona con enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, deficiencias hipofisarias (incluido hipopituitarismo y síndrome de Sheehan), hipogonadismo hipogonadotrópico (incluido síndrome de Kallmann), deficiencia de hormona del crecimiento, enfermedad del timo, insuficiencia suprarrenal (enfermedad de Addison) y enfermedades infecciosas. Esta información debe confirmarse con la ficha técnica oficial.
- **Interacciones y dianas farmacológicas**: los datos registran dos dianas de pioglitazona: el receptor PPAR-gamma (PPARG) y el canal TRPM3. No son interacciones medicamentosas clínicas propiamente dichas. Además, la EMA concedió en 2014 la designación de medicamento huérfano a pioglitazona para la adrenoleucodistrofia.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para opsismodisplasia es solo del modelo (nivel L5), sin ensayos clínicos, sin literatura específica y sin un vínculo mecanístico plausible. Además, el perfil de seguridad conocido de pioglitazona (insuficiencia cardíaca, enfermedad hepática y renal) exige cautela en cualquier nueva indicación.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y análisis de un posible vínculo entre PPAR-gamma e INPPL1 o la vía implicada en la opsismodisplasia
- Estudios preclínicos (modelos celulares o animales) que justifiquen la hipótesis
- Obtener y revisar el prospecto de AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), lo que constituye un vacío de datos bloqueante para el cribado de seguridad
- Evaluar si otras predicciones (por ejemplo, lipodistrofias) tienen una justificación biológica más sólida antes de priorizar esta indicación
- Confirmar la compatibilidad de la vía de administración y la similitud con la indicación original (pendientes)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Pioglitazone
parent: Solo predicción del modelo (L5)
nav_order: 640
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-20
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
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 8; autorizadas no comercializadas: 4; revocadas o suspendidas: 8) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Pioglitazone (traducción no oficial): «ACTOS es una tiazolidinediona cuyo mecanismo de acción depende de la presencia de insulina. ACTOS disminuye la resistencia a la insulina en la periferia y en el hígado, lo que da lugar a un aumento de la eliminación de glucosa dependiente de insulina y a una disminución de la producción hepática de glucosa. […] La pioglitazona no es un secretagogo de insulina.» Texto original en inglés: "ACTOS is a thiazolidinedione that depends on the presence of insulin for its mechanism of action. ACTOS decreases insulin resistance in the periphery and in the liver resulting in increased insulin-dependent glucose disposal and decreased hepatic glucose output. […] Pioglitazone is not an insulin secretagogue." ([DailyMed: Actos (pioglitazone) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d2ddc491-88a9-4063-9150-443b4fa4330c), versión del 2025-03-28; consultado el 2026-11-19). Según la información conocida, pioglitazona es un agonista del receptor activado por proliferadores de peroxisomas gamma (PPARG), lo que se confirma en los datos de farmacología recopilados (que también muestran interacción con TRPM3). Su eficacia en diabetes tipo 2 como sensibilizador de insulina está bien establecida.

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

Se muestran las 5 principales:

<!-- review:begin es-lic-20261105-pioglitazone-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Pioglitazona está comercializada en España con 20 autorizaciones vigentes (todas de monofármaco, ninguna cancelada), en forma de comprimidos. Se muestran las 5 principales:" Eliminado: afirmaba que el medicamento no está autorizado o comercializado en España, o que sus autorizaciones están revocadas o suspendidas, lo que no coincide con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-pioglitazone-1 -->

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

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Pioglitazona está comercializada en España con 20 autorizaciones vigentes (todas de monofármaco, ninguna cancelada), en forma de comprimidos" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Actos (pioglitazone) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d2ddc491-88a9-4063-9150-443b4fa4330c) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


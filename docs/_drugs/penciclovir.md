---
layout: default
title: Penciclovir
parent: Solo predicción del modelo (L5)
nav_order: 621
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "PENCICLOVIR"
predicted_indications: ["fascioliasis"]
description: "Penciclovir: nueva indicación predicha, Fascioliasis (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 1)"
---

# Penciclovir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Penciclovir: Fascioliasis
{: .text-alpha }

## Resumen en Una Frase

Penciclovir es un análogo nucleósido de la guanosina, utilizado originalmente en crema para el tratamiento del herpes labial.
El modelo TxGNN predice que podría ser efectivo para **fascioliasis**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Fascioliasis |
| Puntaje de Predicción TxGNN | 0.9906 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Penciclovir (traducción no oficial): «Penciclovir es un agente antiviral activo frente a los alfaherpesvirus. […] Penciclovir tiene actividad inhibitoria frente al virus del herpes simple de tipos 1 (VHS-1) y 2 (VHS-2). En las células infectadas por VHS-1 o VHS-2, la timidina cinasa viral fosforila el penciclovir a una forma monofosfato que, a su vez, es convertida por cinasas celulares en la forma activa, el trifosfato de penciclovir.» Texto original en inglés: "Penciclovir is an antiviral agent active against alpha herpes viruses. […] Penciclovir has inhibitory activity against herpes simplex virus types 1 (HSV-1) and 2 (HSV-2). In cells infected with HSV-1 or HSV-2, the viral thymidine kinase phosphorylates penciclovir to a monophosphate form that, in turn, is converted by cellular kinases to the active form penciclovir triphosphate." ([DailyMed: Denavir (penciclovir) prescribing information, Mylan Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=61229829-55a0-4d6f-a423-4b48a2b4d8e5), versión del 2018-11-26; consultado el 2026-11-19). Según la información conocida, penciclovir es un análogo nucleósido de la guanosina que es fosforilado por la timidina cinasa viral y, después, inhibe la ADN polimerasa viral. Por ello, su actividad es específica frente a herpesvirus, y su eficacia en el herpes labial es la base de su uso clínico.

La relación con la fascioliasis es débil. *Fasciola hepatica* y *Fasciola gigantica* son trematodos y no se conoce en ellos una vía de activación dependiente de timidina cinasa viral. Tampoco se ha descrito un mecanismo antiparasitario plausible para penciclovir.

El puntaje alto de TxGNN (0,9906) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. La predicción debe considerarse una hipótesis computacional sin respaldo mecanístico demostrado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 61462 | FENIVIR 10 mg/g CREMA | CREMA | Perrigo Espana S.A. | Comercializada |

Se muestra la única autorización con este principio activo en los datos de CIMA (AEMPS).

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (nivel L5), sin ensayos clínicos ni literatura, y no existe un mecanismo biológico plausible que vincule un antiviral específico de herpesvirus con un trematodo. Con la información actual no se justifica avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del fármaco para evaluar cualquier vínculo mecanístico.
- Evidencia preclínica *in vitro* o *in vivo* de actividad frente a *Fasciola* spp.
- Revisión del prospecto de la AEMPS (advertencias y contraindicaciones) para completar el cribado de seguridad.
- Evaluación de la compatibilidad de la vía de administración: el producto autorizado es una crema de uso tópico, poco adecuada para una infección hepatobiliar sistémica.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Denavir (penciclovir) prescribing information, Mylan Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=61229829-55a0-4d6f-a423-4b48a2b4d8e5) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


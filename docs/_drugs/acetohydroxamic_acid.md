---
layout: default
title: Acetohydroxamic Acid
parent: Solo predicción del modelo (L5)
nav_order: 19
evidence_level: L5
indication_count: 4
monitor_inn: "acetohydroxamic acid"
predicted_indications: ["Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis"]
last_modified_at: 2026-11-24
description: "Acetohydroxamic Acid: nueva indicación predicha, Uretritis por Ureaplasma (Ureaplasma urethritis) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 2 (comercializadas: 2)"
---

# Acetohydroxamic Acid
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Ácido acetohidroxámico: inhibidor de la ureasa → Uretritis por Ureaplasma (Ureaplasma urethritis)
{: .text-alpha }

## Resumen en Una Frase

El ácido acetohidroxámico es un inhibidor de la ureasa que se comercializa en España en cápsulas.
El modelo TxGNN predice que podría ser efectivo para **Uretritis por Ureaplasma (Ureaplasma urethritis)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Uretritis por Ureaplasma (Ureaplasma urethritis) |
| Puntaje de Predicción TxGNN | 0,9963 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 2) |
| Número de Autorizaciones | 2 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Acetohydroxamic Acid (traducción no oficial): «El AHA inhibe de forma reversible la enzima bacteriana ureasa, con lo que inhibe la hidrólisis de la urea y la producción de amoníaco en la orina infectada por microorganismos que desdoblan la urea. La reducción de las concentraciones de amoníaco y la disminución del pH potencian la eficacia de los agentes antimicrobianos y permiten un aumento de la tasa de curación de estas infecciones.» Texto original en inglés: "AHA reversibly inhibits the bacterial enzyme urease, thereby inhibiting the hydrolysis of urea and production of ammonia in urine infected with urea-splitting organisms. The reduced ammonia levels and decreased pH enhance the effectiveness of antimicrobial agents and allow an increased cure rate of these infections." ([DailyMed: Lithostat (acetohydroxamic acid) prescribing information, Mission Pharmacal Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6660b616-a82d-9109-19ce-2bdf9747acea), versión del 2026-01-08; consultado el 2026-11-19). Según la farmacología conocida, el ácido acetohidroxámico inhibe la ureasa, una enzima que degrada la urea a amoníaco.

*Ureaplasma urealyticum* produce ureasa, de modo que existe un vínculo biológico plausible: inhibir la enzima podría reducir la producción de amoníaco y la alcalinización e irritación local asociadas. Este vínculo se infiere de la farmacología de la ureasa y de la predicción del modelo, no de datos clínicos.

Conviene ser prudente: la uretritis por Ureaplasma se trata habitualmente con antibióticos (por ejemplo, doxiciclina o azitromicina), y la inhibición de la ureasa no es una estrategia establecida para erradicar el microorganismo. En el mejor de los casos, un uso sería complementario.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 56204 | URONEFREX 125 mg CAPSULAS | CÁPSULA DURA | Ferrer Internacional S.A. | Comercializada |
| 56203 | URONEFREX 250 mg CAPSULAS | CÁPSULA DURA | Ferrer Internacional S.A. | Comercializada |

Se muestran las 2 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de riesgo según las relaciones asociadas al fármaco (no proceden del texto del prospecto)**: trombocitopenia, abuso/dependencia de sustancias, anemia, anemia macrocítica, leucopenia, anemia hemolítica y flebitis.
- **Interacciones Farmacológicas** (5 registradas):
  - Mayor: cladribina.
  - Moderada: alemtuzumab, ocrelizumab, omacetaxina mepesuccinato y ustekinumab.
- Otras consideraciones señaladas en el análisis: posible teratogenicidad y riesgo de anemia hemolítica.

Consultar el prospecto para información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (puntaje 0,9963), sin ensayos clínicos ni literatura, y el tratamiento antibiótico actual ya es eficaz. Además, el perfil hematológico del fármaco exige cautela.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco.
- Advertencias y contraindicaciones del prospecto de la AEMPS.
- Estudios preclínicos o clínicos que evalúen directamente la uretritis por Ureaplasma.
- Evaluación de seguridad, en especial hematológica y reproductiva.
- Análisis de compatibilidad de vía de administración y de similitud con la indicación original.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Lithostat (acetohydroxamic acid) prescribing information, Mission Pharmacal Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6660b616-a82d-9109-19ce-2bdf9747acea) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Eculizumab
parent: Solo predicción del modelo (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-05
monitor_inn: "ECULIZUMAB"
predicted_indications: ["cyclic hematopoiesis", "autosomal recessive severe congenital neutropenia due to JAGN1 deficiency", "X-linked severe congenital neutropenia", "congenital neutropenia-myelofibrosis-nephromegaly syndrome", "adult idiopathic neutropenia", "autosomal recessive severe congenital neutropenia due to CXCR2 deficiency", "primary immunodeficiency syndrome due to p14 deficiency", "autosomal recessive severe congenital neutropenia due to CSF3R deficiency", "severe congenital neutropenia", "primary release disorder of platelets"]
description: "Eculizumab: nueva indicación predicha, Hematopoyesis cíclica (cyclic hematopoiesis) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 3 (comercializadas: 3)"
---

# Eculizumab
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

## Eculizumab: Hematopoyesis cíclica (cyclic hematopoiesis)
{: .text-alpha }

## Resumen en Una Frase

Eculizumab es un anticuerpo monoclonal inhibidor del complemento C5, utilizado originalmente para el tratamiento de la hemoglobinuria paroxística nocturna y la neuromielitis óptica.
El modelo TxGNN predice que podría ser efectivo para **hematopoyesis cíclica**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hematopoyesis cíclica (cyclic hematopoiesis) |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 3 de 3) |
| Número de Autorizaciones | 3 (comercializadas: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Eculizumab (traducción no oficial): «Eculizumab, el principio activo de SOLIRIS, es un anticuerpo monoclonal que se une específicamente y con alta afinidad a la proteína del complemento C5, con lo que inhibe su escisión en C5a y C5b e impide la generación del complejo terminal del complemento C5b-9. SOLIRIS inhibe la hemólisis intravascular mediada por el complemento terminal en pacientes con HPN y la microangiopatía trombótica (MAT) mediada por el complemento en pacientes con SHUa.» Texto original en inglés: "Eculizumab, the active ingredient in SOLIRIS, is a monoclonal antibody that specifically binds to the complement protein C5 with high affinity, thereby inhibiting its cleavage to C5a and C5b and preventing the generation of the terminal complement complex C5b-9. SOLIRIS inhibits terminal complement-mediated intravascular hemolysis in PNH patients and complement-mediated thrombotic microangiopathy (TMA) in patients with aHUS." ([DailyMed: Soliris (eculizumab) prescribing information, Alexion Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ebcd67fa-b4d1-4a22-b33d-ee8bf6b9c722), versión del 2026-07-08; consultado el 2026-11-19). Según la información conocida, eculizumab es un inhibidor del componente C5 del complemento, que bloquea la vía terminal del complemento. Su eficacia en enfermedades mediadas por complemento, como la hemoglobinuria paroxística nocturna, está establecida.

Sin embargo, la relación mecanística con la nueva indicación **no está respaldada** por los datos. La hematopoyesis cíclica (neutropenia cíclica) se asocia típicamente a mutaciones en *ELANE* que alteran la regulación de los precursores de neutrófilos, y no a una patología mediada por el complemento. El puntaje elevado de TxGNN (0,9997) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; debe interpretarse con cautela.

Otras predicciones del modelo con puntajes similares (neutropenias congénitas graves por deficiencia de JAGN1, CXCR2 o CSF3R, neutropenia idiopática del adulto, entre otras) tampoco cuentan con evidencia clínica ni mecanismo plausible de inhibición de C5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para hematopoyesis cíclica.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1231727001 | BEKEMV 300 mg concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |
| 07393001 | SOLIRIS 300 mg concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |
| 1231735001 | EPYSQLI 300 mg concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 4 interacciones de nivel menor con distintas formulaciones de inmunoglobulina G humana (intravenosa, subcutánea, intramuscular, e intravenosa y subcutánea).

Para advertencias y contraindicaciones, consultar el prospecto. Como dato general, la inhibición del complemento aumenta el riesgo de infecciones graves, en particular meningocócicas, algo especialmente relevante en pacientes con inmunodeficiencia de base.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya exclusivamente en el puntaje del modelo (nivel L5), sin ensayos clínicos, sin literatura directamente relevante y sin un vínculo mecanístico plausible entre la inhibición de C5 y la hematopoyesis cíclica.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción y un análisis mecanístico que justifique el papel del complemento en esta enfermedad
- Estudios preclínicos o de mecanismo que muestren una implicación del complemento en la hematopoyesis cíclica
- Revisión del prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas)
- Evaluación del perfil de riesgo-beneficio, en especial el riesgo de infecciones por la inhibición del complemento

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Soliris (eculizumab) prescribing information, Alexion Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ebcd67fa-b4d1-4a22-b33d-ee8bf6b9c722) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


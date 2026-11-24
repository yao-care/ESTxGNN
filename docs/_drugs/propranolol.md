---
layout: default
title: Propranolol
parent: Solo predicción del modelo (L5)
nav_order: 670
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "PROPRANOLOL"
predicted_indications: ["distal myopathy, Tateyama type", "congenital myopathy with excess of thin filaments", "chondroma", "cirrhotic cardiomyopathy"]
description: "Propranolol: nueva indicación predicha, Miopatía distal tipo Tateyama (distal myopathy, Tateyama type) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 11 (comercializadas: 11)"
---

# Propranolol
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

## Propranolol: Miopatía distal tipo Tateyama (distal myopathy, Tateyama type)
{: .text-alpha }

## Resumen en Una Frase

Propranolol es un betabloqueante no selectivo, utilizado originalmente para la hipertensión, las arritmias (como la fibrilación auricular), la miocardiopatía hipertrófica y el hemangioma.
El modelo TxGNN predice que podría ser efectivo para la **miopatía distal tipo Tateyama**, pero se trata únicamente de una predicción del modelo: **no hay ensayos clínicos ni publicaciones** que la respalden.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Miopatía distal tipo Tateyama (distal myopathy, Tateyama type) |
| Puntaje de Predicción TxGNN | 0.9940 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 11 de 11) |
| Número de Autorizaciones | 11 (comercializadas: 11) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Propranolol (traducción no oficial): «No se ha establecido el mecanismo del efecto antihipertensivo del propranolol. Entre los factores que contribuyen a la acción antihipertensiva se encuentran: la disminución del gasto cardíaco, la inhibición de la liberación de renina por los riñones y la disminución del flujo simpático tónico desde los centros vasomotores del cerebro.» Texto original en inglés: "The mechanism of the antihypertensive effect of propranolol has not been established. Among factors that contribute to the antihypertensive action are: decreased cardiac output, inhibition of renin release by the kidneys, and diminution of tonic sympathetic nerve outflow from vasomotor centers in the brain." ([DailyMed: Inderal Xl (propranolol hydrochloride) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ac196ff5-9215-402b-bc57-69aa87f8bade), versión del 2026-08-27; consultado el 2026-11-19). Según la información conocida, propranolol es un betabloqueante no selectivo cuya eficacia en enfermedades cardiovasculares (hipertensión, arritmias, miocardiopatía hipertrófica) y en tumores vasculares como el hemangioma está establecida.

Para la miopatía distal tipo Tateyama **no se identificó un vínculo mecanístico** a partir de los datos disponibles. No hay una justificación evidente para el bloqueo beta-adrenérgico en esta miopatía distal, y el alto puntaje (0.994) refleja solo una señal del modelo, sin respaldo clínico ni bibliográfico.

Conviene además tener en cuenta que el grafo de conocimiento registra la miopatía y otras enfermedades musculares entre las contraindicaciones de propranolol, lo que hace aún más necesaria la cautela ante esta predicción.

### Otras predicciones del modelo (contexto)

| Rango | Enfermedad | Puntaje TxGNN | Nivel de Evidencia | Recomendación |
|------|------|------|------|------|
| 2 | Miopatía congénita con exceso de filamentos finos | 0.9930 | L5 | Hold |
| 4 | Condroma | 0.9914 | L5 | Hold |
| 5 | Miocardiopatía cirrótica | 0.9912 | L5 | Pregunta de investigación |
| 6 | Miocardiopatía | 0.9912 | L5 | Pregunta de investigación |

Las predicciones 5 y 6 son las que cuentan con algo de literatura (cirrosis con intervalo QT prolongado y estudios hemodinámicos en miocardiopatía hipertrófica), aunque esta última se solapa con indicaciones ya existentes.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 89689 | PROPRANOLOL TARBIS 10 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Tarbis Farma S.L. | Comercializada |
| 89692 | PROPRANOLOL TARBIS 40 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Tarbis Farma S.L. | Comercializada |
| 84656 | PROPRANOLOL AUROVITAS 10 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Aurovitas Spain, S.A.U. | Comercializada |
| 84649 | PROPRANOLOL AUROVITAS 40 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Aurovitas Spain, S.A.U. | Comercializada |
| 77175 | PROPRANOLOL ACCORD 40 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Accord Healthcare S.L.U. | Comercializada |
| 83608 | PROPRANOLOL KERN PHARMA 10 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Kern Pharma S.L. | Comercializada |
| 83607 | PROPRANOLOL KERN PHARMA 40 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Kern Pharma S.L. | Comercializada |
| 114919001 | HEMANGIOL 3,75 MG/ML SOLUCION ORAL | SOLUCIÓN ORAL | Pierre Fabre Medicament | Comercializada |
| 77174 | PROPRANOLOL ACCORD 10 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Accord Healthcare S.L.U. | Comercializada |
| 42504 | SUMIAL 10 mg COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Atnahs Pharma Netherlands Bv. | Comercializada |

Se muestran 10 de 11 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Todas las autorizaciones son de principio activo único; entre ellas figuran Propranolol Accord (10 y 40 mg), Propranolol Kern Pharma (10 y 40 mg) y Sumial (10 y 40 mg).

<!-- review:begin es-lic-20261124b-propranolol-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Se muestran 5 de las 11 autorizaciones vigentes (todas de principio activo único). Las restantes corresponden a Propranolol Accord (10 y 40 mg), Propranolol Kern Pharma (10 y 40 mg) y Sumial (10 y 40 mg)." Corregido: la frase hablaba de autorizaciones que no figuraban en la tabla anterior (por ejemplo, «la sexta», «las restantes» u «otras»). La tabla de Información de Mercado en España se genera desde el 2026-11-24 por programa a partir de los datos de CIMA (AEMPS) y las incluye; las cifras actuales están en el Resumen rápido. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261124b-propranolol-1 -->

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): bronquitis, trastornos de ansiedad, enfermedad renal, pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, lupus eritematoso sistémico, miopatía y enfermedades musculares, parálisis periódica familiar, diabetes mellitus, cetoacidosis diabética, gota, hiperparatiroidismo, encefalopatía hepática, anuria, miastenia gravis, entre otras.
- **Interacciones farmacológicas** (100 registradas; se muestran las principales):
  - **Mayor:** epinefrina.
  - **Moderadas:** hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona, atropina, bupropión, morfina, cimetidina, canagliflozina, clorpropamida, lorcaserina.
  - **Menores:** ácido ascórbico, ácido acetilsalicílico, óxido de magnesio.
- **Consideración en cirrosis avanzada:** la literatura aportada para la miocardiopatía cirrótica sugiere que los betabloqueantes no selectivos pueden alterar la homeostasis circulatoria y renal en ascitis refractaria.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para la miopatía distal tipo Tateyama se basa solo en el modelo (nivel L5), sin ensayos, sin literatura y sin un mecanismo plausible. Además, las enfermedades musculares figuran entre las contraindicaciones registradas del fármaco.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de propranolol y una hipótesis mecanística concreta para esta miopatía.
- Revisión sistemática de la literatura y de registros de ensayos específicos de la enfermedad.
- Obtención de las advertencias y contraindicaciones del prospecto de AEMPS (actualmente no disponibles) antes de cualquier evaluación de seguridad.
- Evaluación preclínica (modelos celulares o animales) que justifique la hipótesis.
- Como alternativa de mayor viabilidad, priorizar las preguntas de investigación sobre miocardiopatía cirrótica, que cuenta con algo de literatura, sin olvidar sus señales de seguridad.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Inderal Xl (propranolol hydrochloride) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ac196ff5-9215-402b-bc57-69aa87f8bade) |
| 2026-11-24 | Eliminado: descripción de la tabla anterior y número; «Las restantes» → «entre ellas» | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


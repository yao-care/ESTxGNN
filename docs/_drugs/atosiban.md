---
layout: default
title: Atosiban
parent: Solo predicción del modelo (L5)
nav_order: 77
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Atosiban: nueva indicación predicha, Glaucoma hereditario primario (nivel de evidencia L5). Indicación original: No disponible en los textos de autorización de la AEMPS (según otras…"
monitor_inn: "atosiban"
predicted_indications: ["primary hereditary glaucoma", "open-angle glaucoma", "congenital hypotrichosis milia", "alopecia", "hypotrichosis simplex of the scalp", "vascular disease", "diffuse alopecia areata", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "visceral calciphylaxis"]
---

# Atosiban
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

## Atosiban: De Indicación Original No Registrada a Glaucoma Hereditario Primario
{: .text-alpha }

## Resumen en Una Frase

Atosiban es un antagonista peptídico de los receptores de oxitocina y vasopresina, utilizado en Europa como tocolítico para retrasar el parto prematuro en mujeres adultas embarazadas de 24 a 33 semanas.
El modelo TxGNN predice que podría ser efectivo para **glaucoma hereditario primario**, con una puntuación muy alta (0,9992), pero **sin ensayos clínicos ni publicaciones** que respalden esta dirección; se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los textos de autorización de la AEMPS (según otras fuentes de datos, tocolítico en parto prematuro) |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 0,9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 9 de 15; revocadas o suspendidas: 6) |
| Número de Autorizaciones | 15 (comercializadas: 9) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Atosiban es (traducción no oficial): «Antagonista del receptor de oxitocina». Texto original en inglés: "Oxytocin receptor antagonist" ([ChEMBL CHEMBL382301 (atosiban): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL382301), CC BY-SA 3.0; consultado el 2026-11-19). Según la información farmacológica compilada, atosiban actúa como antagonista de los receptores de oxitocina (OXTR) y de los receptores de vasopresina V1A, V1B y V2. Su uso establecido es la inhibición de las contracciones uterinas en el parto prematuro.

La relación entre la indicación original (obstétrica) y el glaucoma hereditario primario es muy débil. Los datos no muestran ningún vínculo establecido con la fisiopatología del glaucoma hereditario (defectos de la malla trabecular o del drenaje del humor acuoso). La puntuación elevada de TxGNN refleja similitud en la red de conocimiento, no biología demostrada.

Cabe señalar que otras indicaciones predichas (por ejemplo, glaucoma de ángulo abierto, alopecia o enfermedad vascular) tampoco cuentan con evidencia clínica. Solo "enfermedad vascular" presenta literatura preclínica indirecta (nivel L4), centrada en oxitocina y no en atosiban como tratamiento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para glaucoma hereditario primario.

---

## Información de Mercado en España

Los textos de indicación aprobada no figuran en los datos compilados. Principales autorizaciones:

<!-- review:begin es-lic-20261105-atosiban-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Se registran 15 autorizaciones vigentes, todas de fármaco único. Los textos de indicación aprobada no figuran en los datos compilados." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-atosiban-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 79315 | ATOSIBAN ALTAN 6.75 MG/0.9 ML SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Altan Pharmaceuticals Sa | Comercializada |
| 81920 | ATOSIBAN EVER PHARMA 75 MG/10 ML CONCENTRADO PARA SOLUCION PARA PERFUSION | SOLUCIÓN INYECTABLE | Ever Valinject Gmbh | Comercializada |
| 113852001 | Atosiban SUN 6,75 mg/0,9 ml solucion inyectable EFG | SOLUCIÓN INYECTABLE | Sun Pharmaceutical Industries (Europe) B.V. | Comercializada |
| 99124001 | TRACTOCILE 7,5 mg/ml, SOLUCION INYECTABLE | SOLUCIÓN INYECTABLE | Ferring Pharmaceuticals A/S | Comercializada |
| 81919 | ATOSIBAN EVER PHARMA 6,75 MG/0,9 ML SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Ever Valinject Gmbh | Comercializada |
| 81918 | ATOSIBAN EVER PHARMA 37,5 MG/5 ML CONCENTRADO PARA SOLUCION PARA PERFUSION EFG | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Ever Valinject Gmbh | Comercializada |
| 113852002 | Atosiban SUN 37,5 mg/5 ml concentrado para solucion para perfusion EFG | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Sun Pharmaceutical Industries (Europe) B.V. | Comercializada |
| 79314 | ATOSIBAN ALTAN 37,5 MG/5 ML CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN EFG | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Altan Pharmaceuticals Sa | Comercializada |
| 99124002 | TRACTOCILE 7,5 mg/ml, CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Ferring Pharmaceuticals A/S | Comercializada |
| 84868 | ATOSIBAN HYBIO 37,5 MG/5 ML CONCENTRADO PARA SOLUCCION PARA PERFUSION EFG | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Hybio Pharmaceutical Germany Gmbh | Revocada |

Se muestran 10 de 15 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas / farmacología de dianas**: la consulta se completó con 4 registros, todos de interacción con dianas farmacológicas (no con otros fármacos): receptores V1A (AVPR1A), V1B (AVPR1B), V2 (AVPR2) y de oxitocina (OXTR). No se dispone de niveles de gravedad.
- **Señal de seguridad indirecta**: un estudio de cohorte neonatal (PMID 30646165, JAMA Network Open, 2018) examinó la asociación entre la exposición a tocolíticos y la hemorragia intraventricular en prematuros. Es una señal a vigilar, no evidencia terapéutica.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para glaucoma hereditario primario se basa solo en la puntuación del modelo (nivel L5), sin ensayos clínicos, literatura ni vínculo mecanístico plausible con el glaucoma.

**Para avanzar se necesita:**
- Revisión del prospecto de la AEMPS (indicaciones, advertencias y contraindicaciones), actualmente sin datos
- Datos detallados del mecanismo de acción (por ejemplo, desde DrugBank)
- Estudios preclínicos que evalúen la modulación de receptores de oxitocina/vasopresina en la presión intraocular o el drenaje del humor acuoso
- Análisis de compatibilidad de vía de administración (atosiban solo está disponible en formas parenterales; una indicación oftalmológica requeriría evaluar formulaciones alternativas)
- Considerar si otras indicaciones predichas, como enfermedad vascular (L4), merecen priorizarse como pregunta de investigación

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Eliminado: "Se registran 15 autorizaciones vigentes, todas de fármaco único" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; la versión anterior se guarda en el registro) | [ChEMBL CHEMBL382301 (atosiban): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL382301) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


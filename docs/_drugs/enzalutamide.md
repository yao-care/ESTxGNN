---
layout: default
title: Enzalutamide
parent: Solo predicción del modelo (L5)
nav_order: 293
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
monitor_inn: "Enzalutamide"
predicted_indications: ["prostate leiomyoma", "Brenner tumor", "fibroma of prostate", "benign reproductive system neoplasm", "benign prostate phyllodes tumor"]
description: "Enzalutamide: nueva indicación predicha, Prostate leiomyoma (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 17 (comercializadas: 1; autorizadas no comercializadas: 16)"
---

# Enzalutamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Enzalutamide: Prostate leiomyoma
{: .text-alpha }

## Resumen en Una Frase

Enzalutamida es un inhibidor del receptor de andrógenos, utilizado originalmente para el tratamiento del cáncer de próstata.
El modelo TxGNN predice que podría ser efectivo para **susceptibilidad al cáncer de próstata/cáncer cerebral**, un fenotipo de susceptibilidad y no una enfermedad tratable en sentido estricto,
con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección actualmente.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Prostate leiomyoma |
| Puntaje de Predicción TxGNN | 0.9957 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 17; autorizadas no comercializadas: 16) |
| Número de Autorizaciones | 17 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Enzalutamida es un inhibidor del receptor de andrógenos (AR), que es su diana farmacológica. Está aprobada para el cáncer de próstata, incluidos el cáncer de próstata resistente a la castración y el sensible a hormonas. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Enzalutamide (traducción no oficial): «La enzalutamida es un inhibidor del receptor de andrógenos que actúa en distintos pasos de la vía de señalización del receptor de andrógenos. Se ha demostrado que la enzalutamida inhibe de forma competitiva la unión de los andrógenos a los receptores de andrógenos y, en consecuencia, inhibe la translocación nuclear de los receptores de andrógenos y su interacción con el ADN.» Texto original en inglés: "Enzalutamide is an androgen receptor inhibitor that acts on different steps in the androgen receptor signaling pathway. Enzalutamide has been shown to competitively inhibit androgen binding to androgen receptors; and consequently, inhibits nuclear translocation of androgen receptors and their interaction with DNA." ([DailyMed: Xtandi (enzalutamide) prescribing information, Astellas Pharma US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b129fdc9-1d8e-425c-a5a9-8a2ed36dfbdf), versión del 2026-07-28; consultado el 2026-11-19).

Por ello, la puntuación alta debe interpretarse con cautela. La puntuación proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 17 autorizaciones vigentes (todas de principio activo único). Los textos de indicación aprobada no estaban disponibles en los datos compilados.

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 113846002 | XTANDI 40 MG COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Astellas Pharma Europe B.V. | Comercializada |
| 89057 | ENZALUTAMIDA SANDOZ 80 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Sandoz Farmaceutica S.A. | Autorizada, no comercializada |
| 89615 | ENZALUTAMIDA ACCORD 40 MG CAPSULAS BLANDAS EFG | CÁPSULA BLANDA | Accord Healthcare S.L.U. | Autorizada, no comercializada |
| 1241842002 | ENZALUTAMIDA VIATRIS 40 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Viatris Limited | Autorizada, no comercializada |
| 113846001 | XTANDI 40 MG CAPSULAS BLANDAS | CÁPSULA BLANDA | Astellas Pharma Europe B.V. | Autorizada, no comercializada |

Se muestran 5 de 17 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia hormonal dirigida (inhibidor del receptor de andrógenos); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura. Además, la indicación predicha es un fenotipo de susceptibilidad y no una enfermedad tratable. Otras predicciones del mismo fármaco, como "cáncer de órgano reproductor masculino", sí cuentan con ensayos de Fase 3, pero estos corresponden en su mayoría a la indicación ya aprobada (cáncer de próstata) y no aportan un reposicionamiento nuevo.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA)
- Textos de indicación, advertencias y contraindicaciones del prospecto de la AEMPS
- Evidencia clínica o preclínica que vincule el bloqueo del AR con la nueva indicación
- Reevaluar las demás predicciones del modelo, priorizando indicaciones que sean enfermedades tratables y distintas del cáncer de próstata

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Xtandi (enzalutamide) prescribing information, Astellas Pharma US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b129fdc9-1d8e-425c-a5a9-8a2ed36dfbdf) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


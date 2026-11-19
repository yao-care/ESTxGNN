---
layout: default
title: Alteplase
parent: Solo predicción del modelo (L5)
nav_order: 45
evidence_level: L5
indication_count: 6
monitor_inn: "alteplase"
predicted_indications: ["heparin cofactor 2 deficiency", "congenital coronary artery anomaly", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "coronary stenosis"]
last_modified_at: 2026-11-05
description: "Alteplase: nueva indicación predicha, Deficiencia de cofactor II de la heparina (heparin cofactor 2 deficiency) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 2 (comercializadas: 1)"
---

# Alteplase
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Alteplasa: activador tisular del plasminógeno recombinante (trombolítico) → Deficiencia de cofactor II de la heparina (heparin cofactor 2 deficiency)
{: .text-alpha }

## Resumen en Una Frase

Alteplasa es un activador tisular del plasminógeno recombinante que se utiliza como trombolítico y está comercializado en España.
El modelo TxGNN predice que podría ser efectivo para la **Deficiencia de cofactor II de la heparina (heparin cofactor 2 deficiency)**.
Actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que es una predicción basada únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Deficiencia de cofactor II de la heparina (heparin cofactor 2 deficiency) |
| Puntaje de Predicción TxGNN | 0,9972 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 2; revocadas o suspendidas: 1) |
| Número de Autorizaciones | 2 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Alteplase (traducción no oficial): «Alteplasa es una enzima (serina proteasa) que tiene la propiedad de convertir el plasminógeno en plasmina de forma potenciada por la fibrina. En ausencia de fibrina, produce una conversión limitada del plasminógeno. Alteplasa se une a la fibrina de un trombo y convierte el plasminógeno atrapado en plasmina, con lo que inicia la fibrinólisis local.» Texto original en inglés: "Alteplase is an enzyme (serine protease) that has the property of fibrin-enhanced conversion of plasminogen to plasmin. It produces limited conversion of plasminogen in the absence of fibrin. Alteplase binds to fibrin in a thrombus and converts the entrapped plasminogen to plasmin, thereby initiating local fibrinolysis." ([DailyMed: Cathflo Activase (alteplase) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=91ecdef2-95ff-42dd-a31c-c8a09cab3ad9), versión del 2026-01-20; consultado el 2026-11-19). Por su clase farmacológica, alteplasa convierte el plasminógeno en plasmina, enzima que disuelve la fibrina de los coágulos. Esto la hace útil ante trombos agudos.

La deficiencia de cofactor II de la heparina es una trombofilia hereditaria, con mayor tendencia a formar trombos. Mecanísticamente, alteplasa podría disolver un trombo agudo que aparezca en este contexto. Sin embargo, eso sería tratar el evento trombótico y no la deficiencia en sí.

El vínculo es solo una predicción del modelo. No hay ensayos ni literatura que lo confirmen, y también hay que considerar el riesgo de sangrado y de nueva trombosis tras la lisis.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Los datos locales no incluyen el texto de indicación aprobada de estas autorizaciones.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 76900 | ACTILYSE CATHFLO 2 MG polvo para solución inyectable y para perfusión | Polvo para solución inyectable y para perfusión |
| 59494 | ACTILYSE polvo y disolvente para solución inyectable y para perfusión | Polvo y disolvente para solución inyectable y para perfusión |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 140 interacciones. Entre las principales:
  - **Gravedad mayor**: abciximab, apixaban, fondaparinux, anisindiona, acalabrutinib, deferasirox, ibritumomab tiuxetán y tositumomab (incluido el marcado con I-131). En general, aumentan el riesgo de sangrado.
  - **Gravedad moderada**: ácido acetilsalicílico, ibuprofeno, ketorolaco, fluvoxamina, fosinopril, ácido aminocaproico, aprotinina, fenfluramina, dexfenfluramina y sibutramina.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (0,9972), pero no hay ensayos clínicos ni publicaciones sobre esta enfermedad, por lo que el nivel de evidencia es L5. Además, el beneficio mecanístico se limitaría a tratar eventos trombóticos agudos, con riesgo de sangrado.

**Para avanzar se necesita:**
- Revisión de literatura específica sobre trombólisis en pacientes con deficiencia de cofactor II de la heparina.
- Datos del mecanismo de acción y de las advertencias y contraindicaciones del prospecto.
- Evaluación de la relación beneficio-riesgo de sangrado y de trombosis de rebote en esta población.
- Definición de la vía de administración y de la población diana.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Cathflo Activase (alteplase) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=91ecdef2-95ff-42dd-a31c-c8a09cab3ad9) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


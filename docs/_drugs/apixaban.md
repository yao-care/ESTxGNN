---
layout: default
title: Apixaban
parent: Solo predicción del modelo (L5)
nav_order: 60
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "apixaban"
predicted_indications: ["migraine disorder"]
description: "Apixaban: nueva indicación predicha, trastorno de migraña (migraine disorder) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Apixaban
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

## Apixaban: trastorno de migraña (migraine disorder)
{: .text-alpha }

## Resumen en Una Frase

Apixabán es un anticoagulante oral que inhibe directamente el factor Xa. El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña (migraine disorder)**, pero la evidencia es de nivel **L5**: hay **1 ensayo clínico** sin relación directa con la migraña y **3 publicaciones** (dos de ellas casos clínicos en los que la migraña no mejoró o empeoró con apixabán).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | trastorno de migraña (migraine disorder) |
| Puntaje de Predicción TxGNN | 0.9902 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 10; autorizadas no comercializadas: 9; revocadas o suspendidas: 1) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Apixabán inhibe de forma directa y selectiva el factor Xa de la coagulación. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Apixaban (traducción no oficial): «El apixabán es un inhibidor selectivo del FXa. No requiere antitrombina III para ejercer su actividad antitrombótica. El apixabán inhibe el FXa libre y el unido al coágulo, así como la actividad de la protrombinasa. El apixabán no tiene ningún efecto directo sobre la agregación plaquetaria, pero inhibe indirectamente la agregación plaquetaria inducida por la trombina.» Texto original en inglés: "Apixaban is a selective inhibitor of FXa. It does not require antithrombin III for antithrombotic activity. Apixaban inhibits free and clot-bound FXa, and prothrombinase activity. Apixaban has no direct effect on platelet aggregation, but indirectly inhibits platelet aggregation induced by thrombin." ([DailyMed: Eliquis (apixaban) prescribing information, Aphena Pharma Solutions - Tennessee, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=41a133ef-e461-48ad-8221-b735bdd0ec25), versión del 2026-09-24; consultado el 2026-11-19).

La hipótesis teórica es que la migraña con aura, sobre todo en pacientes con foramen oval permeable o anticuerpos antifosfolípido, podría implicar embolia paradójica o microtrombosis, de modo que un tratamiento antitrombótico podría reducir el aura o la carga de migraña.

Sin embargo, esta hipótesis no está respaldada para apixabán. El puntaje de TxGNN es alto (0,9902), pero es una predicción computacional sin mecanismo establecido, y los casos publicados son contradictorios o desfavorables: uno describe empeoramiento de la migraña con aura tras iniciar apixabán y otro, resolución con warfarina pero no con apixabán. Cualquier posible beneficio no sería un efecto de clase de los anticoagulantes.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Fase 3 | Completado | 664 | Cierre del foramen oval permeable o anticoagulantes frente a antiagregantes para prevenir la recurrencia de ictus. La migraña no fue la indicación ni el criterio principal, y no se evidencia que el anticoagulante estudiado fuera apixabán; no aporta evidencia directa para migraña. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Estudio retrospectivo (75 pacientes) | Lupus | Tratamiento antitrombótico en migraña refractaria con anticuerpos antifosfolípido; el diseño y los fármacos no se pueden verificar solo con el título, y no se confirma que incluya apixabán. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Caso clínico con revisión | The Neurologist | Migraña con aura que empeoró tras iniciar apixabán; la literatura sobre anticoagulantes orales directos y migraña es escasa y controvertida. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Caso clínico | Headache | Migraña con aura remitida con warfarina durante 12 años; los síntomas reaparecieron al cambiar a apixabán y se resolvieron al reanudar warfarina. |

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 85788 | APIXABAN TEVA 5 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Teva Pharma S.L.U. | Comercializada |
| 89318 | APIXABÁN TECNIMEDE 5 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Tecnimede España Industria Farmaceutica S.A. | Comercializada |
| 90909 | APIXABAN NORMON 5 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorios Normon S.A. | Comercializada |
| 90741 | APIXABAN ALMUS 2,5 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Almus Farmaceutica S.A.U. | Comercializada |
| 111691010 | ELIQUIS 5 MG COMPRIMIDO RECUBIERTO CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Bristol-Myers Squibb/Pfizer Eeig | Comercializada |
| 86418 | APIXABAN TAD 5 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Tad Pharma Gmbh | Comercializada |
| 90740 | APIXABAN ALMUS 5 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Almus Farmaceutica S.A.U. | Comercializada |
| 90238 | APIXABAN ROVI 2,5 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorios Farmaceuticos Rovi S.A. | Comercializada |
| 86636 | APIXABAN STADA 5 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorio Stada S.L. | Comercializada |
| 90371 | APIXABAN VIVANTA 2,5 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Vivanta Generics S.R.O. | Comercializada |

Se muestran 10 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

Los datos locales solo recogen parte de las autorizaciones, por lo que esta lista puede ser parcial; entre ellas hay autorizaciones comercializadas (como Eliquis), otras autorizadas sin comercializar y alguna revocada.

<!-- review:begin es-lic-20261124c-apixaban-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Los datos locales incluyen al menos 20 autorizaciones, por lo que esta lista puede ser parcial; solo una figura como vigente y comercializada (Eliquis) y una está cancelada." Corregido: según CIMA (AEMPS), hay varias autorizaciones de apixabán comercializadas (además de ELIQUIS, genéricos de otros titulares), otras autorizadas sin comercializar y algunas revocadas; la frase anterior decía que solo una estaba comercializada. Los datos de este informe solo recogen parte de las autorizaciones; las cifras recogidas están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261124c-apixaban-1 -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registran 324 interacciones. Entre las de nivel mayor figuran el ácido acetilsalicílico, cobicistat, deferasirox, ibritumomab tiuxetán y tositumomab. Entre las de nivel moderado figuran aprepitant, claritromicina, clotrimazol, dexametasona, miconazol y rolapitant, entre otras.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún estudio respalda el uso de apixabán en la migraña; los dos casos clínicos describen migraña con aura que empeoró o no se resolvió con apixabán. El nivel de evidencia es L5 y el puntaje alto de TxGNN (0,9902) no basta por sí solo para avanzar.

**Para avanzar se necesita:**
- Estudios clínicos que evalúen directamente apixabán en migraña, con criterios de valoración específicos.
- Datos del mecanismo de acción y del vínculo biológico con la migraña.
- Información de seguridad del prospecto (advertencias y contraindicaciones) para valorar el riesgo hemorrágico en esta población.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Eliquis (apixaban) prescribing information, Aphena Pharma Solutions - Tennessee, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=41a133ef-e461-48ad-8221-b735bdd0ec25) |
| 2026-11-24 | «al menos 20 … solo una figura como vigente y comercializada (Eliquis)» → hay varias comercializadas; sin cifras | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


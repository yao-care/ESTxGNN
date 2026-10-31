---
layout: default
title: Apixaban
parent: Evidencia moderada (L3-L4)
nav_order: 60
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-31
description: "Apixaban: nueva indicación predicha, Trastorno de migraña (nivel de evidencia L4). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "apixaban"
predicted_indications: ["migraine disorder"]
---

# Apixaban
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

## Apixabán: De Indicación Original no Especificada a Trastorno de Migraña
{: .text-alpha }

## Resumen en Una Frase

Apixabán es un anticoagulante oral que inhibe directamente el factor Xa. Los datos compilados para este informe no incluyen el texto de su indicación aprobada en España.
El modelo TxGNN predice que podría ser efectivo para **Trastorno de migraña**, pero la evidencia es muy limitada: **1 ensayo clínico** de relevancia baja (no evalúa migraña de forma directa) y **3 publicaciones** (dos informes de caso contradictorios y un estudio retrospectivo con antitrombóticos en general).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Trastorno de migraña |
| Puntaje de Predicción TxGNN | 0,9902 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 1) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, apixabán es un inhibidor directo del factor Xa de la coagulación, y su uso como anticoagulante está ampliamente establecido. Sin embargo, su vínculo mecanístico con la migraña es, en el mejor de los casos, indirecto.

Una hipótesis es que la migraña con aura, especialmente en pacientes con foramen oval permeable (FOP) o con anticuerpos antifosfolípidos, podría implicar embolia paradójica o microtrombosis. En ese escenario, la terapia antitrombótica podría reducir el aura o la carga de migraña.

El puntaje de TxGNN es muy alto (0,9902), pero proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; no hay un mecanismo establecido. Los informes de caso disponibles son contradictorios: uno describe empeoramiento de migraña con aura tras iniciar apixabán, y otro describe resolución del aura con warfarina pero no con apixabán. Esto sugiere que un posible beneficio no sería un efecto de clase de los anticoagulantes y no está respaldado para apixabán.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Fase 3 | Completado | 664 | Cierre del FOP o anticoagulantes frente a antiagregantes para prevenir la recurrencia del ictus. La migraña no era la indicación ni el objetivo principal; no aporta evidencia directa de eficacia de apixabán en migraña (relevancia baja). |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33402037](https://pubmed.ncbi.nlm.nih.gov/33402037/) | 2021 | Estudio retrospectivo (75 pacientes) | Lupus | Respuesta a terapia antitrombótica en migraña refractaria con anticuerpos antifosfolípidos; el diseño y los fármacos concretos no se pueden verificar con la información disponible. |
| [37582651](https://pubmed.ncbi.nlm.nih.gov/37582651/) | 2023 | Informe de caso con revisión | The Neurologist | Migraña con aura que empeoró tras iniciar apixabán; la literatura sobre anticoagulantes orales directos y migraña es escasa y controvertida. |
| [28960288](https://pubmed.ncbi.nlm.nih.gov/28960288/) | 2017 | Informe de caso | Headache | Mujer de 55 años con migraña con aura en remisión durante 12 años con warfarina; los síntomas reaparecieron con apixabán y se resolvieron al reanudar warfarina. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 85788 | Apixaban Teva 5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 89409 | Apixabán Farmalider 2,5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 90861 | Apixaban Grindeks 2,5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 89868 | Apixaban Olpha 2,5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 111691010 | Eliquis 5 mg comprimido recubierto con película | Comprimido recubierto con película | No disponible |

Se muestran 5 de las 20 autorizaciones vigentes (todas de medicamento de un solo principio activo; ninguna cancelada).

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 324 interacciones en total. Entre las de nivel **mayor** figuran: ácido acetilsalicílico, cobicistat, deferasirox, ibritumomab tiuxetán y tositumomab (incluido tositumomab I-131). Entre las de nivel **moderado**: aprepitant, claritromicina, clotrimazol, dexametasona, fenfluramina, dexfenfluramina, eliglustat, miconazol, rolapitant, sibutramina, troglitazona, yoduro I-123, yoduro I-131 y sugammadex.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN es muy alta, pero se apoya solo en el modelo: el único ensayo de Fase 3 no evalúa migraña y la literatura se limita a informes de caso contradictorios, con un posible empeoramiento tras apixabán. El nivel de evidencia es L4.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), pues es un requisito previo para cualquier evaluación de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Estudios que evalúen directamente apixabán en migraña, idealmente en subpoblaciones con FOP o anticuerpos antifosfolípidos
- Una revisión sistemática de la señal de seguridad (posible empeoramiento de la migraña con aura) y del riesgo hemorrágico en esta población
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


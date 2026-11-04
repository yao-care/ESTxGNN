---
layout: default
title: Apixaban
parent: Solo predicción del modelo (L5)
nav_order: 60
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-04
monitor_inn: "apixaban"
predicted_indications: ["migraine disorder"]
description: "Apixaban: nueva indicación predicha, trastorno de migraña (migraine disorder) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
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
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 1) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Apixabán inhibe de forma directa y selectiva el factor Xa de la coagulación. No se dispone de datos detallados sobre su mecanismo de acción en los datos compilados para este informe, por lo que no fue posible un contraste mecanístico más profundo.

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

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 85788 | Apixaban Teva 5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 89409 | Apixabán Farmalider 2,5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 90861 | Apixaban Grindeks 2,5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 89868 | Apixaban Olpha 2,5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 111691010 | Eliquis 5 mg comprimido recubierto con película | Comprimido recubierto con película | No disponible |

Los datos locales incluyen al menos 20 autorizaciones, por lo que esta lista puede ser parcial; solo una figura como vigente y comercializada (Eliquis) y una está cancelada.

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

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


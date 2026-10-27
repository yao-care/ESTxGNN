---
layout: default
title: Icatibant
parent: Evidencia alta (L1-L2)
nav_order: 401
evidence_level: L1
indication_count: 7
last_modified_at: 2026-10-14
description: "Icatibant: nueva indicación predicha, Deficiencia de inhibidor de C1 (nivel de evidencia L1). Indicación original: Angioedema hereditario"
monitor_inn: "icatibant"
predicted_indications: ["C1 inhibitor deficiency", "serpinopathy with toxic serpin polymerization", "pseudo-von Willebrand disease", "primary release disorder of platelets", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "Glanzmann thrombasthenia"]
---

# Icatibant
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **7** 
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

## Icatibant: De Angioedema Hereditario a Deficiencia de Inhibidor de C1
{: .text-alpha }

## Resumen en Una Frase

Icatibant es un antagonista del receptor B2 de bradicinina, utilizado originalmente para el tratamiento del angioedema hereditario (incluido el asociado a deficiencia de C1 inhibidor).
El modelo TxGNN predice que podría ser efectivo para la **deficiencia de inhibidor de C1**, una indicación que coincide con su uso ya aprobado, por lo que funciona más como validación del modelo que como reposicionamiento real.
Esta dirección está respaldada por **11 ensayos clínicos** y **20 publicaciones** en los datos compilados para este informe.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Angioedema hereditario |
| Nueva Indicación Predicha | Deficiencia de inhibidor de C1 |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 13 |
| Decisión Recomendada | Proceed with Guardrails |

> Nota: los datos de las autorizaciones españolas no incluyen el texto de indicación aprobada. La indicación original procede de las relaciones indicación-fármaco del grafo de conocimiento utilizado por el modelo.

## Por qué es Razonable esta Predicción

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información compilada, icatibant es un péptido sintético antagonista selectivo del receptor B2 de bradicinina (BDKRB2), con afinidad también registrada por el receptor B1 (BDKRB1).

En la deficiencia de inhibidor de C1 se produce una activación descontrolada del sistema calicreína-cinina y un exceso de bradicinina, que provoca los ataques de angioedema a través de la señalización del receptor B2. Icatibant bloquea directamente esta vía. La literatura también describe un mecanismo análogo en la deficiencia adquirida de C1 inhibidor, con un estudio observacional en ocho pacientes que respalda su uso.

Conviene subrayar que esta indicación coincide con el uso ya aprobado del fármaco (angioedema hereditario con deficiencia de C1 inhibidor). Por tanto, no es un reposicionamiento propiamente dicho, sino una confirmación de que el modelo recupera una asociación conocida. La extensión realmente nueva sería el angioedema adquirido por deficiencia de C1 inhibidor.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00097695](https://clinicaltrials.gov/study/NCT00097695) | Fase 3 | Completado | 84 | Icatibant subcutáneo vs. placebo (doble ciego) en ataques agudos cutáneos y/o abdominales de angioedema hereditario |
| [NCT00500656](https://clinicaltrials.gov/study/NCT00500656) | Fase 3 | Completado | 85 | Icatibant vs. ácido tranexámico oral; variable principal: tiempo hasta el inicio del alivio |
| [NCT00912093](https://clinicaltrials.gov/study/NCT00912093) | Fase 3 | Completado | 98 | Eficacia y seguridad de icatibant vs. placebo en ataques agudos de angioedema hereditario |
| [NCT00997204](https://clinicaltrials.gov/study/NCT00997204) | Fase 3 | Completado | 151 | Estudio abierto de autoadministración: seguridad, tolerancia local y eficacia |
| [NCT01386658](https://clinicaltrials.gov/study/NCT01386658) | Fase 3 | Completado | 32 | Farmacocinética, tolerabilidad y seguridad de una dosis única en niños y adolescentes |
| [NCT03888755](https://clinicaltrials.gov/study/NCT03888755) | Fase 3 | Completado | 8 | Estudio abierto en pacientes japoneses con ataques agudos de angioedema hereditario tipo I o II |
| [NCT04654351](https://clinicaltrials.gov/study/NCT04654351) | Fase 3 | Completado | 2 | Seguridad, eficacia y farmacocinética en niños y adolescentes japoneses (muestra muy limitada) |
| [NCT01457430](https://clinicaltrials.gov/study/NCT01457430) | Fase 4 | Completado | 19 | Autoadministración de icatibant frente a administración en centro médico |
| [NCT04057131](https://clinicaltrials.gov/study/NCT04057131) | N/A | Completado | 179 | Encuesta poscomercialización en Japón sobre seguridad y eficacia |
| [NCT05509569](https://clinicaltrials.gov/study/NCT05509569) | N/A | Completado | 32 | Vigilancia poscomercialización en población pediátrica japonesa |
| [NCT07290855](https://clinicaltrials.gov/study/NCT07290855) | Fase 4 | Completado | 5 | Seguridad y eficacia en angioedema inducido por bradicinina en Taiwán |

*Se omite un ensayo de Fase 1 en voluntarios sanos japoneses (NCT02045264), por ser solo de apoyo farmacocinético.*

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22686628](https://pubmed.ncbi.nlm.nih.gov/22686628/) | 2012 | Observacional | Allergy | Icatibant en 8 pacientes con deficiencia adquirida de C1 inhibidor: 48 ataques moderados a graves tratados con 30 mg subcutáneos |
| [29757016](https://pubmed.ncbi.nlm.nih.gov/29757016/) | 2018 | Revisión de estudios clínicos | Expert Rev Clin Immunol | Seguridad y eficacia de icatibant en adolescentes y niños mayores de 2 años con angioedema hereditario |
| [23420425](https://pubmed.ncbi.nlm.nih.gov/23420425/) | 2013 | Revisión sistemática | Pneumonol Alergol Pol | Comparación de conestat alfa, C1 inhibidor humano e icatibant en ataques agudos en adultos |
| [20030426](https://pubmed.ncbi.nlm.nih.gov/20030426/) | 2010 | Revisión | Drugs | Icatibant como antagonista del receptor B2; en FAST-1 la diferencia en la variable principal no alcanzó significación, aunque fue eficaz en otras variables |
| [33602658](https://pubmed.ncbi.nlm.nih.gov/33602658/) | 2021 | Revisión | J Investig Allergol Clin Immunol | Tratamiento actual del angioedema hereditario y fármacos en desarrollo |
| [37716525](https://pubmed.ncbi.nlm.nih.gov/37716525/) | 2023 | Estudio retrospectivo | J Allergy Clin Immunol Pract | Diagnóstico, evolución y tratamiento del angioedema adquirido por deficiencia de C1 inhibidor; sin terapia autorizada |
| [32753245](https://pubmed.ncbi.nlm.nih.gov/32753245/) | 2020 | Recomendaciones | Rev Med Interne | Recomendaciones CREAK para el diagnóstico y tratamiento del angioedema adquirido |
| [28687105](https://pubmed.ncbi.nlm.nih.gov/28687105/) | 2017 | Revisión | Immunol Allergy Clin North Am | Deficiencia adquirida de C1 inhibidor y su asociación con autoinmunidad y trastornos linfoproliferativos |
| [24925394](https://pubmed.ncbi.nlm.nih.gov/24925394/) | 2014 | Revisión | Chem Immunol Allergy | Enfermedades mediadas por bradicinina, con angioedema como manifestación común |
| [22197274](https://pubmed.ncbi.nlm.nih.gov/22197274/) | 2012 | Guía de consenso | J Allergy Clin Immunol | Manejo ginecológico y obstétrico de mujeres con angioedema hereditario por deficiencia de C1 inhibidor |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 08461001 | FIRAZYR 30 mg solución inyectable en jeringa precargada (Takeda) | Solución inyectable en jeringa precargada | No disponible en los datos |
| 87158 | Icatibanto Aguettant 30 mg EFG | Solución inyectable en jeringa precargada | No disponible en los datos |
| 86573 | Icatibanto Piramal 30 mg EFG | Solución inyectable en jeringa precargada | No disponible en los datos |
| 86352 | Icatibanto Stada 30 mg EFG | Solución inyectable en jeringa precargada | No disponible en los datos |
| 86865 | Icatibanto Fresenius 30 mg EFG | Solución inyectable en jeringa precargada | No disponible en los datos |

En total hay 13 autorizaciones vigentes, todas de monofármaco y ninguna cancelada.

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: se identificaron 12 registros. Diez corresponden a interacciones de nivel **moderado** con inhibidores de la ECA: benazepril, captopril, enalapril, perindopril, trandolapril, moexipril, lisinopril, quinapril, ramipril y fosinopril. Los otros dos son registros farmacológicos de unión a los receptores de bradicinina B1 y B2 (no son interacciones clínicas).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen varios ensayos de Fase 3 completados (incluidos controlados con placebo y con comparador activo) y un mecanismo bien establecido, lo que justifica el nivel L1. Sin embargo, la indicación predicha coincide con la ya aprobada, por lo que el valor de reposicionamiento reside solo en el angioedema adquirido, donde la evidencia se limita a estudios observacionales pequeños.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), actualmente no disponible
- Confirmar los datos formales del mecanismo de acción
- Evidencia prospectiva de mayor calidad en angioedema adquirido por deficiencia de C1 inhibidor
- Plan de manejo de la interacción con inhibidores de la ECA
- Verificar el texto de indicación aprobada en las autorizaciones españolas

**Nota sobre otras predicciones:** las demás indicaciones predichas (serpinopatía con polimerización tóxica de serpinas, pseudo-enfermedad de von Willebrand, trastorno primario de liberación plaquetaria, miopatía necrosante inmunomediada, síndrome antisintetasa y trombastenia de Glanzmann) no tienen ensayos ni literatura, carecen de vínculo mecanístico plausible y se clasifican como L5 con decisión **Hold**. Probablemente son artefactos de proximidad en el grafo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


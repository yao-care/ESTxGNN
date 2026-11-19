---
layout: default
title: Glucagon
parent: Solo predicción del modelo (L5)
nav_order: 380
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
monitor_inn: "glucagon"
predicted_indications: ["irritable bowel syndrome"]
description: "Glucagon: nueva indicación predicha, Síndrome del intestino irritable (irritable bowel syndrome) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 2 (comercializadas: 2)"
---

# Glucagon
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

## Glucagon: Síndrome del intestino irritable (irritable bowel syndrome)
{: .text-alpha }

## Resumen en Una Frase

El glucagón es una hormona peptídica comercializada en España en inyectable y en polvo nasal.
El modelo TxGNN predice que podría ser efectivo para el **síndrome del intestino irritable (irritable bowel syndrome)**, pero ningún estudio ha probado el glucagón en esta enfermedad: los 2 ensayos clínicos y las publicaciones disponibles se refieren a GLP-1 y a sus agonistas, que son fármacos distintos. El nivel de evidencia es **L5**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome del intestino irritable (irritable bowel syndrome) |
| Puntaje de Predicción TxGNN | 0.9924 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 2) |
| Número de Autorizaciones | 2 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Glucagon (traducción no oficial): «El glucagón aumenta la concentración de glucosa en sangre mediante la activación de los receptores hepáticos de glucagón, lo que estimula la degradación del glucógeno y la liberación de glucosa desde el hígado. Las reservas hepáticas de glucógeno son necesarias para que el glucagón produzca un efecto antihipoglucemiante.» Texto original en inglés: "Glucagon increases blood glucose concentration by activating hepatic glucagon receptors, thereby stimulating glycogen breakdown and release of glucose from the liver. Hepatic stores of glycogen are necessary for glucagon to produce an antihypoglycemic effect." ([DailyMed: glucagon prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e4be1c0e-0fe6-45a0-9229-5cde98434b84), versión del 2020-09-16; consultado el 2026-11-19). Por conocimiento general, el glucagón actúa sobre el receptor GCGR y puede inhibir la motilidad gastrointestinal, por lo que se usa como antiespasmódico en pruebas diagnósticas de imagen.

El GLP-1 y el glucagón derivan del mismo precursor (proglucagón) y ambos pueden reducir la motilidad del tramo antro-duodeno-yeyunal. Esto sugiere un vínculo plausible con el síndrome del intestino irritable, donde intervienen la motilidad intestinal y el eje intestino-cerebro.

Sin embargo, los receptores son distintos (GLP-1R frente a GCGR). La evidencia encontrada no puede atribuirse al glucagón, y el puntaje elevado del modelo es una predicción computacional que probablemente refleja la cercanía entre péptidos de la misma familia.

## Evidencia de Ensayos Clínicos

Ningún ensayo evalúa el glucagón en síndrome del intestino irritable; ambos estudian análogos o formas nativas de GLP-1.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Fase 1/2 | Completado | 52 | ROSE-010 (análogo de GLP-1) sobre la función motora gastrointestinal en mujeres con SII con estreñimiento predominante; evidencia solo indirecta |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Fase 1 | Completado | 12 | GLP-1 nativo frente a ROSE-010 sobre la motilidad antro-duodeno-yeyunal posprandial en humanos; no incluye pacientes con SII |

## Evidencia de Literatura

Las publicaciones tratan de GLP-1 o de agonistas del receptor de GLP-1, no de glucagón.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Revisión sistemática | Frontiers in Endocrinology | Mejoría del SII con agonistas del receptor de GLP-1; GLP-1 y ROSE-010 inhiben la motilidad gastrointestinal |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Cohorte | Annals of Gastroenterology | Patrones de prescripción y suspensión de agonistas de GLP-1 en pacientes con SII |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | Análisis exploratorio | Scandinavian Journal of Gastroenterology | Alivio del dolor con ROSE-010 en SII según características de los pacientes |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Revisión | Experimental Physiology | Papel del GLP-1 en la fisiopatología del SII |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Revisión | Advances in Experimental Medicine and Biology | GLP-1 en aerosol para diabetes y SII |
| [40880735](https://pubmed.ncbi.nlm.nih.gov/40880735/) | 2025 | Estudio en pacientes | Frontiers in Nutrition | Aumento de GLP-1 circulante tras una dieta baja en FODMAP en pacientes con SII |
| [30023410](https://pubmed.ncbi.nlm.nih.gov/30023410/) | 2018 | Revisión | Cellular and Molecular Gastroenterology and Hepatology | Interacciones bidireccionales del eje cerebro-intestino-microbioma |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59327 | GlucaGen HypoKit 1 mg polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | No disponible en los datos |
| 1191406001 | Baqsimi 3 mg polvo nasal en envase unidosis | Polvo nasal | No disponible en los datos |

## Consideraciones de Seguridad

**Interacciones Farmacológicas:** se identificaron 25 interacciones, todas de nivel menor entre las mostradas. Incluyen la warfarina y numerosos betabloqueantes (acebutolol, atenolol, betaxolol, bisoprolol, carvedilol, labetalol, metoprolol, nadolol, pindolol, propranolol, sotalol, timolol, esmolol y carteolol, entre otros, incluidas formulaciones oftálmicas).

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún estudio que evalúe el glucagón en el síndrome del intestino irritable; la evidencia disponible corresponde a GLP-1 y sus agonistas, fármacos y receptores distintos. El puntaje alto del modelo (0,9924) no basta por sí solo para avanzar.

**Para avanzar se necesita:**
- Estudios preclínicos o clínicos que prueben directamente el glucagón en el síndrome del intestino irritable
- Datos detallados del mecanismo de acción y análisis de la diferencia entre los receptores GCGR y GLP-1R
- Advertencias y contraindicaciones del prospecto de las autorizaciones españolas
- Evaluación de la compatibilidad de vía de administración y dosis para esta posible indicación

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: glucagon prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e4be1c0e-0fe6-45a0-9229-5cde98434b84) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


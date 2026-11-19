---
layout: default
title: Desloratadine
parent: Solo predicción del modelo (L5)
nav_order: 234
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-20
monitor_inn: "Desloratadine"
predicted_indications: ["nasal cavity disease", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic", "rosacea conjunctivitis"]
description: "Desloratadine: nueva indicación predicha, Nasal cavity disease (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Desloratadine
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

## Desloratadine: Nasal cavity disease
{: .text-alpha }

## Resumen en Una Frase

Desloratadina es un antihistamínico H1 de segunda generación, utilizado originalmente para el tratamiento de la rinitis alérgica y la urticaria.
con **2 ensayos clínicos** y **6 publicaciones** (de las cuales 3 son ensayos aleatorizados directamente relacionados con la indicación) que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Nasal cavity disease |
| Puntaje de Predicción TxGNN | 0.9987 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 15; autorizadas no comercializadas: 4; revocadas o suspendidas: 1) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Desloratadine (traducción no oficial): «La desloratadina es un antagonista tricíclico de la histamina de acción prolongada con actividad antagonista selectiva de la histamina en los receptores H1. Los datos de unión a receptores indican que, a una concentración de 2-3 ng/mL (7 nanomolar), la desloratadina muestra una interacción significativa con el receptor H1 de la histamina humano.» Texto original en inglés: "Desloratadine is a long-acting tricyclic histamine antagonist with selective H1-receptor histamine antagonist activity. Receptor binding data indicates that at a concentration of 2-3 ng/mL (7 nanomolar), desloratadine shows significant interaction with the human histamine H1-receptor." ([DailyMed: Desloratadine Oral Solution (desloratadine) prescribing information, INA Pharmaceutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=41d5e0d4-6188-847b-e063-6294a90a2e2f), versión del 2025-10-23; consultado el 2026-11-19). Según la información conocida, desloratadina es un antagonista (agonista inverso) selectivo del receptor H1 de histamina de acción periférica. Su eficacia en rinitis alérgica y urticaria idiopática/alérgica ha sido comprobada, y mecanísticamente es aplicable a la urticaria por frío.

La urticaria por frío es un subtipo de urticaria inducible mediado por la desgranulación de mastocitos y la liberación de histamina tras la exposición al frío. El bloqueo del receptor H1 actúa directamente sobre la respuesta de roncha y eritema. Dado que la urticaria crónica ya figura entre las indicaciones originales, la urticaria por frío es una entidad estrechamente relacionada.

Además, el aumento de dosis (hasta 4 veces la dosis estándar) de antihistamínicos H1 es una estrategia respaldada por las guías para la urticaria refractaria a la dosis habitual, lo que se refleja en los ensayos que comparan 5, 10 y 20 mg de desloratadina.

<!-- review:begin es-lic-20261105-desloratadine-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Se registran 20 autorizaciones vigentes en total (todas de monofármaco), con presentaciones en comprimido recubierto, comprimido bucodispersable y solución oral." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-desloratadine-1 -->

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Fase 4 | Completado | 30 | Estudio multicéntrico, doble ciego, con escalada de dosis (5, 10 y 20 mg) en urticaria por frío adquirida, para determinar la dosis suficiente para inhibir los síntomas |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Fase 4 | Completado | 33 | Estudio exploratorio, aleatorizado, doble ciego, cruzado y controlado con placebo: 5 mg vs. 20 mg sobre lesiones de urticaria inducidas experimentalmente |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | ECA | J Allergy Clin Immunol | La dosis alta de desloratadina reduce el volumen de las ronchas y mejora los umbrales de provocación por frío frente a la dosis estándar (cruzado, controlado con placebo) |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | ECA | Br J Dermatol | Medición del umbral crítico de temperatura en urticaria por frío con escalada de dosis de antihistamínicos H1 |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | ECA | J Dermatolog Treat | Desloratadina 5 mg durante 4 días inhibe la urticaria por frío en 12 pacientes (prueba con cubito de hielo) |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Revisión | Drugs | Etiología, manejo y opciones de tratamiento de la urticaria crónica |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Revisión | Allergy | Ebastina en rinitis alérgica y urticaria crónica idiopática (otro antihistamínico; evidencia indirecta) |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Reporte de caso | Qatar Med J | Urticaria por frío tras anafilaxia por picadura de hormiga negra (sin relación directa con el tratamiento) |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 76043 | Deloratadina Combix 5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 75387 | Desloratadina Stada 0,5 mg/ml solución oral EFG | Solución oral | No disponible |
| 75335 | Desloratadina Cinfa 5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 00160055 | Aerius 5 mg comprimidos bucodispersables | Comprimido bucodispersable | No disponible |
| 77984 | Desloratadina Alter 5 mg comprimidos bucodispersables EFG | Comprimido bucodispersable | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proceden del prospecto)**: el grafo de conocimiento asocia desloratadina con precaución en enfermedad hipertensiva/hipertensión, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, diabetes mellitus y cetoacidosis diabética, hiperplasia benigna de próstata, enfermedad coronaria y aterosclerosis, glaucoma de ángulo cerrado, e hipertiroidismo (enfermedad de Graves/tirotoxicosis). Esta información debe confirmarse con el prospecto oficial.
- **Interacciones farmacológicas**: la consulta se completó y solo identificó la interacción farmacodinámica con el receptor H1 (diana principal del fármaco); no se identificaron interacciones con otros fármacos. Un dato farmacológico adicional señala actividad antiviral frente a SARS-CoV-2 en cribados de reposicionamiento, probablemente por fosfolipidosis inducida, sin relevancia clínica establecida.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen ensayos aleatorizados, doble ciego y controlados con placebo (publicaciones y ensayos de Fase 4 completados) que respaldan directamente el uso de desloratadina, incluso a dosis elevadas, en urticaria por frío, y el mecanismo es biológicamente coherente. No obstante, los estudios son pequeños (12–33 pacientes) y de Fase 4, por lo que no hay ensayos de Fase 3 confirmatorios.

**Para avanzar se necesita:**
- Revisar el prospecto oficial de la AEMPS (advertencias y contraindicaciones) y confirmar el texto de indicaciones aprobadas
- Obtener datos detallados del mecanismo de acción (MOA) desde fuentes de referencia
- Evaluar la seguridad de dosis superiores a la autorizada (hasta 4 veces), dado que su uso sería fuera de ficha técnica
- Verificar las precauciones en poblaciones específicas (insuficiencia renal/hepática, enfermedad cardiovascular)
- Valorar un ensayo de mayor tamaño que confirme la eficacia y la dosis óptima

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Se registran 20 autorizaciones vigentes en total (todas de monofármaco), con presentaciones en comprimido recubierto, comprimido bucodispers" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Desloratadine Oral Solution (desloratadine) prescribing information, INA Pharmaceutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=41d5e0d4-6188-847b-e063-6294a90a2e2f) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


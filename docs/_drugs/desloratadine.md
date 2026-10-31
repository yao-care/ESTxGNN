---
layout: default
title: Desloratadine
parent: Solo predicción del modelo (L5)
nav_order: 234
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-31
monitor_inn: "Desloratadine"
predicted_indications: ["nasal cavity disease", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic", "rosacea conjunctivitis"]
description: "Desloratadine: nueva indicación predicha, Nasal cavity disease (nivel de evidencia L5). Indicación original: No consta en los datos locales"
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
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 15) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según la información conocida, desloratadina es un antagonista (agonista inverso) selectivo del receptor H1 de histamina de acción periférica. Su eficacia en rinitis alérgica y urticaria idiopática/alérgica ha sido comprobada, y mecanísticamente es aplicable a la urticaria por frío.

La urticaria por frío es un subtipo de urticaria inducible mediado por la desgranulación de mastocitos y la liberación de histamina tras la exposición al frío. El bloqueo del receptor H1 actúa directamente sobre la respuesta de roncha y eritema. Dado que la urticaria crónica ya figura entre las indicaciones originales, la urticaria por frío es una entidad estrechamente relacionada.

Además, el aumento de dosis (hasta 4 veces la dosis estándar) de antihistamínicos H1 es una estrategia respaldada por las guías para la urticaria refractaria a la dosis habitual, lo que se refleja en los ensayos que comparan 5, 10 y 20 mg de desloratadina.

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

Se registran 20 autorizaciones vigentes en total (todas de monofármaco), con presentaciones en comprimido recubierto, comprimido bucodispersable y solución oral.

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


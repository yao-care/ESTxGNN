---
layout: default
title: Dapsone
parent: Evidencia alta (L1-L2)
nav_order: 222
evidence_level: L1
indication_count: 1
last_modified_at: 2026-10-14
description: "Dapsone: nueva indicación predicha, Neumocistosis (nivel de evidencia L1). Indicación original: Dermatitis herpetiforme, acné y lepra (según el grafo de conocimiento"
monitor_inn: "Dapsone"
predicted_indications: ["pneumocystosis"]
---

# Dapsone
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **1** 
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

## Dapsona: De Dermatitis Herpetiforme a Neumocistosis
{: .text-alpha }

## Resumen en Una Frase

La dapsona es una sulfona utilizada originalmente para tratar la dermatitis herpetiforme, el acné y la lepra.
El modelo TxGNN predice que podría ser efectiva para la **neumocistosis** (neumonía por *Pneumocystis*),
con **10 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección. En la práctica, esta indicación ya es un uso clínico establecido como alternativa en las guías.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dermatitis herpetiforme, acné y lepra (según el grafo de conocimiento; el texto de indicación de la autorización en España no está disponible) |
| Nueva Indicación Predicha | Neumocistosis |
| Puntaje de Predicción TxGNN | 99.73% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Español | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

No se dispone actualmente de datos detallados sobre el mecanismo de acción en la fuente original. Según la información conocida, la dapsona es una sulfona que inhibe la dihidropteroato sintasa en la vía de síntesis del folato, el mismo blanco que el sulfametoxazol. Los datos farmacológicos compilados también describen una inhibición *in vitro* de la actividad dihidrofolato reductasa en *Pneumocystis carinii* (CI50 de 1,5 µM).

*Pneumocystis jirovecii* depende de esta vía, por lo que el mecanismo antifolato explica de forma plausible la actividad frente a la neumonía por *Pneumocystis* (PCP). La dapsona ya tiene actividad antimicrobiana demostrada en lepra y efecto antiinflamatorio en dermatosis neutrofílicas, lo que respalda su perfil antiinfeccioso.

Esta indicación es, de hecho, un uso clínico aceptado: la dapsona es una alternativa recomendada por las guías para la profilaxis de la PCP y, combinada con trimetoprima, para el tratamiento de la PCP leve a moderada en pacientes que no toleran TMP-SMX. Por ello se describe mejor como un uso establecido respaldado por guías que como un reposicionamiento novedoso.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Fase 3 | Completado | 700 | Dapsona diaria vs atovacuona diaria para profilaxis de PCP en pacientes con VIH intolerantes a trimetoprima/sulfonamidas |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Fase 3 | Completado | 600 | Tres regímenes antineumocisto (incluida dapsona) más zidovudina para prevención primaria en VIH avanzado |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Fase 3 | Completado | 400 | Pentamidina en aerosol mensual vs dapsona tres veces por semana para profilaxis de PCP |
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Fase 3 | Completado | 290 | Dapsona/trimetoprima y clindamicina/primaquina vs TMP-SMX en PCP leve a moderada |
| [NCT00000739](https://clinicaltrials.gov/study/NCT00000739) | Fase 1 | Completado | 96 | Comparación de toxicidad y farmacocinética de dapsona diaria vs semanal en niños con VIH |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Fase 1 | Completado | 20 | Trimetrexato con leucovorina más dapsona vs TMP-SMX en PCP moderadamente grave (muestra pequeña) |
| [NCT00002043](https://clinicaltrials.gov/study/NCT00002043) | No indicada | Completado | No indicada | Dapsona 100 mg vs 50 mg para profilaxis primaria de PCP en pacientes con complejo relacionado con el SIDA |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | No indicada | Completado | No indicada | Dapsona (con trimetoprima) vs TMP-SMX en el primer episodio de PCP en pacientes con SIDA |
| [NCT02550080](https://clinicaltrials.gov/study/NCT02550080) | Fase 4 | Desconocido | 3130 | Cribado genético HLA-B*1301 para el síndrome de hipersensibilidad a dapsona; no evalúa eficacia en PCP |
| [NCT00636935](https://clinicaltrials.gov/study/NCT00636935) | Fase 4 | Retirado | 0 | Corticoides orales y fibrosis intersticial en PCP; no evalúa dapsona y no aporta datos |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | Revisión sistemática / metaanálisis en red | Clin Microbiol Infect | Eficacia y seguridad comparadas de regímenes de profilaxis de PCP en personas con VIH (TMP-SMX, regímenes con dapsona, pentamidina en aerosol, atovacuona) |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Revisión sistemática / metaanálisis en red | Clin Microbiol Infect | Comparación de regímenes de tratamiento de PCP en personas con VIH; TMP-SMX sigue siendo el tratamiento principal |
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | Guía | J Antimicrob Chemother | Guías ECIL para la prevención de PCP en neoplasias hematológicas y trasplante de progenitores; TMP-SMX es de elección |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Revisión | Expert Opin Pharmacother | Revisión de *P. jirovecii* con enfoque en prevención y tratamiento |
| [11155588](https://pubmed.ncbi.nlm.nih.gov/11155588/) | 2001 | Revisión | Dermatol Clin | La dapsona es útil en la profilaxis de la neumonía por *Pneumocystis* en VIH; fármaco de elección en dermatitis herpetiforme |
| [18971152](https://pubmed.ncbi.nlm.nih.gov/18971152/) | 2008 | Revisión | J Formos Med Assoc | Revisión de la neumonía por *Pneumocystis*, principal infección oportunista en pacientes con SIDA |
| [9227859](https://pubmed.ncbi.nlm.nih.gov/9227859/) | 1997 | Revisión | Clin Microbiol Rev | Neumocistosis extrapulmonar, complicación muy poco frecuente de la PCP |
| [1727534](https://pubmed.ncbi.nlm.nih.gov/1727534/) | 1992 | Revisión | Med Clin North Am | La neumocistosis es prevenible y tratable en pacientes con VIH |
| [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/) | 1998 | Reporte de caso (seguridad) | Ann Pharmacother | Metahemoglobinemia por dapsona en profilaxis de PCP |
| [33280223](https://pubmed.ncbi.nlm.nih.gov/33280223/) | 2021 | Revisión retrospectiva de casos | Pediatr Transplant | Metahemoglobinemia por dapsona en niños con trasplante renal que la usan como profilaxis de PCP |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 15201 | SULFONA COMPRIMIDOS (Esteve Pharmaceuticals S.A.) | Comprimido | Texto de indicación no disponible |

## Consideraciones de Seguridad

- **Contraindicaciones y enfermedades de riesgo (según el grafo de conocimiento, no según el prospecto)**: enfermedad hepática, enfermedad de la vesícula biliar, anemia, anemia macrocítica, déficit de G6PD, enfermedad por depósito de glucógeno, cistinuria, galactosemia, déficit de piruvato deshidrogenasa E3 y metahemoglobinemia por déficit de metahemoglobina reductasa.
- **Riesgos descritos en la literatura**: metahemoglobinemia e hipoxia, complicaciones hepáticas, pancreatitis aguda y síndrome de hipersensibilidad (asociado a HLA-B*1301).
- **Interacciones farmacológicas**: no se identificaron interacciones fármaco-fármaco clínicas; los dos registros disponibles corresponden a dianas farmacológicas (TAS2R40 y la dihidropteroato sintasa de *Plasmodium falciparum*).
- Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Varios ensayos de Fase 3 completados (n=290 a 700) comparan regímenes con dapsona para la profilaxis y el tratamiento de la PCP, y los metaanálisis en red recientes apoyan su uso como alternativa. El perfil de seguridad exige salvaguardas, en particular por el riesgo hemolítico y de metahemoglobinemia.

**Para avanzar se necesita:**
- Cribado de G6PD antes de iniciar el tratamiento y vigilancia de metahemoglobinemia y hemograma.
- Obtener las advertencias y contraindicaciones del prospecto de la AEMPS, actualmente no disponibles.
- Confirmar el texto de indicación autorizado en España para la autorización 15201 y si la PCP figura en ficha técnica o es uso fuera de indicación.
- Datos detallados del mecanismo de acción desde DrugBank.
- Considerar la atención a la hipersensibilidad y a la reactividad cruzada con sulfonamidas, así como el cribado de HLA-B*1301 en poblaciones relevantes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


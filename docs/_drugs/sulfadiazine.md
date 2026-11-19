---
layout: default
title: Sulfadiazine
parent: Solo predicción del modelo (L5)
nav_order: 750
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-05
monitor_inn: "Sulfadiazine"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis"]
description: "Sulfadiazine: nueva indicación predicha, Neumocistosis (pneumocystosis) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 1)"
---

# Sulfadiazine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Sulfadiazine: Neumocistosis (pneumocystosis)
{: .text-alpha }

## Resumen en Una Frase

Sulfadiazina es una sulfonamida utilizada originalmente para el tratamiento de la toxoplasmosis y otras infecciones e inflamaciones oculares e intestinales.
El modelo TxGNN predice que podría ser efectiva para **neumocistosis**,
pero actualmente **no hay ensayos clínicos** y solo hay **20 publicaciones** de carácter indirecto (mayoritariamente revisiones generales y reportes de casos) que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Neumocistosis (pneumocystosis) |
| Puntaje de Predicción TxGNN | 0.9939 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Sulfadiazine (traducción no oficial): «Las sulfonamidas sistémicas son agentes bacteriostáticos que tienen un espectro de actividad similar. Las sulfonamidas inhiben de forma competitiva la síntesis bacteriana de ácido fólico (ácido pteroilglutámico) a partir del ácido aminobenzoico. Las cepas resistentes son capaces de utilizar precursores del ácido fólico o ácido fólico preformado.» Texto original en inglés: "The systemic sulfonamides are bacteriostatic agents having a similar spectrum of activity. Sulfonamides competitively inhibit bacterial synthesis of folic acid (pteroylglutamic acid) from aminobenzoic acid. Resistant strains are capable of utilizing folic acid precursors or preformed folic acid." ([DailyMed: sulfadiazine prescribing information, Chartwell RX, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6032d6f7-cbce-4e5d-841c-a1e24b616f91), versión del 2024-09-24; consultado el 2026-11-19). Según el conocimiento farmacológico general, la sulfadiazina es una sulfonamida que inhibe la dihidropteroato sintetasa, enzima de la vía de biosíntesis del folato. *Pneumocystis jirovecii* depende de esta vía, por lo que existe un vínculo mecanístico plausible a nivel de clase.

Las sulfonamidas, en particular el sulfametoxazol combinado con trimetoprima (TMP-SMX), son tratamientos establecidos de la neumonía por *Pneumocystis*. La sulfadiazina se usa sobre todo junto con pirimetamina para la toxoplasmosis, y es probable que muchas de las publicaciones halladas reflejen esa coocurrencia de ambas infecciones oportunistas en pacientes con SIDA.

Conviene ser prudente: la sulfadiazina no es el agente estándar contra *Pneumocystis* (lo es el TMP-SMX) y la literatura aportada no ofrece datos directos de eficacia de la sulfadiazina en esta indicación. El puntaje elevado de TxGNN es coherente con el mecanismo compartido de las sulfonamidas, pero es una predicción computacional, no evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Se muestran las publicaciones más relevantes (en su mayoría revisiones y reportes de casos; ninguna ofrece datos directos de eficacia de sulfadiazina en neumocistosis).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2645082](https://pubmed.ncbi.nlm.nih.gov/2645082/) | 1989 | Sin clasificar | Clinical Pharmacy | Pirimetamina-sulfadiazina para neumonía por *P. carinii* y toxoplasmosis en SIDA (sin resumen disponible) |
| [15673759](https://pubmed.ncbi.nlm.nih.gov/15673759/) | 2005 | Estudio de mecanismo | Antimicrob Agents Chemother | Mutaciones en el gen DHPS de *P. jirovecii* confieren resistencia cruzada a sulfamidas |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Revisión | Drugs | Terapia y profilaxis de infecciones sistémicas por protozoos (*Pneumocystis*, *Toxoplasma*, etc.) |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Revisión | American Family Physician | Antiparasitarios de elección; TMP-SMX para neumonía por *Pneumocystis* y quinina-pirimetamina-sulfadiazina para malaria resistente |
| [7909657](https://pubmed.ncbi.nlm.nih.gov/7909657/) | 1994 | Revisión | Annals of Internal Medicine | Avances en el manejo de infecciones oportunistas asociadas al SIDA |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Revisión | Clinical Pharmacy | Tratamiento de complicaciones infecciosas del SIDA, con la neumonía por *P. carinii* como la más frecuente |
| [9097375](https://pubmed.ncbi.nlm.nih.gov/9097375/) | 1997 | Revisión | Seminars in Respiratory Infections | Neumonía por *Toxoplasma* en pacientes inmunodeprimidos |
| [29604970](https://pubmed.ncbi.nlm.nih.gov/29604970/) | 2018 | Revisión | Handbook of Clinical Neurology | Infección del sistema nervioso central por *Toxoplasma gondii* |
| [9562233](https://pubmed.ncbi.nlm.nih.gov/9562233/) | 1998 | Revisión | Int J Clin Pharmacol Ther | Nefrotoxicidad de fármacos antiinfecciosos, incluida la precipitación tubular de sulfonamidas |
| [2060528](https://pubmed.ncbi.nlm.nih.gov/2060528/) | 1991 | Estudio observacional | Eur J Clin Microbiol Infect Dis | Seguimiento de 35 pacientes con SIDA en tratamiento de mantenimiento de toxoplasmosis, con recaídas de toxoplasmosis y neumocistosis |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 06960 | SULFADIAZINA REIG JOFRE 500 MG COMPRIMIDOS | Comprimido | Texto de indicación no disponible |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto)**: porfiria (incluida la hereditaria), enfermedad renal, obstrucción del tracto urinario, enfermedad hepática, enfermedad de la vesícula biliar, enfermedades hematológicas (anemia aplásica, agranulocitosis, neutropenia, leucopenia, trombocitopenia, anemia macrocítica y anemia por deficiencia de ácido fólico), deficiencia de G6PD, acetilación lenta, asma, galactosemia, cistinuria y enfermedades de almacenamiento de glucógeno.
- **Riesgos señalados en el análisis**: nefrotoxicidad y cristaluria, hipersensibilidad.
- **Interacciones farmacológicas**: se identificaron 82 interacciones. Entre las 20 de nivel moderado listadas figuran:
  - antidiabéticos (clorpropamida, glimepirida, glipizida, gliburida, tolazamida, repaglinida, nateglinida), con posible riesgo de hipoglucemia;
  - múltiples insulinas (aspart, degludec, detemir, glargina, glulisina, lispro, humana);
  - balsalazida, ácido picosulfúrico y naltrexona.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo y en un vínculo mecanístico a nivel de clase (nivel de evidencia L4), sin ensayos clínicos y con literatura indirecta. Además, ya existe un tratamiento estándar (TMP-SMX) y el perfil de seguridad es exigente.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones oficiales), pendiente de la revisión de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar datos directos de eficacia de sulfadiazina frente a *Pneumocystis* (estudios preclínicos o clínicos) y compararla con TMP-SMX.
- Evaluar la seguridad renal, hematológica y las interacciones en poblaciones inmunodeprimidas.

---

**Nota sobre la segunda predicción (queratoconjuntivitis epitelial punteada):** puntaje TxGNN de 0.9936, nivel de evidencia L5, sin ensayos clínicos ni literatura. No es plausible que una sulfonamida sistémica sea eficaz, dado que las causas suelen ser virales o relacionadas con sequedad ocular. Decisión: **Hold**, solo como generación de hipótesis.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: sulfadiazine prescribing information, Chartwell RX, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6032d6f7-cbce-4e5d-841c-a1e24b616f91) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


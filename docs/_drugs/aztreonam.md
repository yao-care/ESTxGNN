---
layout: default
title: Aztreonam
parent: Evidencia moderada (L3-L4)
nav_order: 85
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Aztreonam: nueva indicación predicha, Uretritis gonocócica (nivel de evidencia L3). Indicación original: Infección del tracto urinario, infección por Pseudomonas aeruginosa…"
monitor_inn: "AZTREONAM"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "gonococcal urethritis", "Ureaplasma urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
---

# Aztreonam
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Aztreonam: De Infección Urinaria a Uretritis Gonocócica

## Resumen en Una Frase

Aztreonam es un antibiótico monobactámico, originalmente utilizado para tratar infecciones por bacterias gramnegativas como las infecciones del tracto urinario, las infecciones por *Pseudomonas aeruginosa* y la peritonitis.
El modelo TxGNN genera varias predicciones; la más respaldada por la evidencia disponible es **uretritis gonocócica**, con **0 ensayos clínicos** y **6 publicaciones** (incluido un ensayo abierto de un solo brazo de 2020).
La predicción con mayor puntaje del modelo (hiperamilasemia) carece de toda evidencia y de plausibilidad mecanística, por lo que este informe se centra en la candidata con mayor sustento.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección del tracto urinario, infección por *Pseudomonas aeruginosa*, peritonitis (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Uretritis gonocócica (candidata con mayor evidencia; la primera predicha por puntaje es hiperamilasemia) |
| Puntaje de Predicción TxGNN | 99,59 % (uretritis gonocócica); hiperamilasemia: 99,73 % |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold (la evidencia es de baja calidad; ver conclusión) |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, aztreonam es un monobactámico que inhibe la síntesis de la pared celular bacteriana al unirse a la proteína fijadora de penicilina 3 (PBP3), con actividad exclusiva contra bacterias gramnegativas aerobias.

*Neisseria gonorrhoeae* es un diplococo gramnegativo, por lo que cae dentro del espectro de acción de aztreonam. Esto se relaciona con las indicaciones originales (infecciones urinarias y otras infecciones gramnegativas): en todas se trata de una infección bacteriana susceptible al mismo mecanismo. Varios estudios de dosis única de la década de 1980 y un ensayo abierto de 2020 describen eficacia, incluso frente a gonococos resistentes a penicilina.

Hay que matizar: la evidencia es no aleatorizada y mayoritariamente antigua, se han descrito cepas resistentes (PMID 11406757) y aztreonam no es hoy un tratamiento de primera línea de la gonorrea. Su papel sería, en todo caso, como alternativa en cepas resistentes o pacientes alérgicos a betalactámicos.

### Otras predicciones del modelo

| Enfermedad predicha | Puntaje | Nivel | Valoración |
|------|------|------|------|
| Hiperamilasemia | 99,73 % | L5 | Sin vínculo mecanístico; es un hallazgo de laboratorio. Hold |
| Síndrome de hiperviscosidad policlonal | 99,73 % | L5 | Sin mecanismo plausible. Hold |
| Analbuminemia congénita | 99,69 % | L5 | Sin fundamento mecanístico. Hold |
| Ureaplasma urethritis | 99,59 % | L5 | Implausible: *Ureaplasma* carece de pared celular. No recomendado |
| Incompatibilidad de grupo sanguíneo | 99,59 % | L5 | Sin vínculo; el único artículo es un falso positivo por palabra clave. Hold |
| Enfermedad hematológica premaligna | 99,54 % | L5 | Sin fundamento mecanístico. Hold |
| Epiglotitis | 99,53 % | L4 | Plausible (*H. influenzae*), pero evidencia indirecta y alternativas establecidas |
| Gammapatía monoclonal | 99,50 % | L4 | Solo tratamiento de soporte de infecciones; no es reposicionamiento real |
| Pielonefritis xantogranulomatosa | 99,49 % | L5 | Indirectamente plausible; manejo principalmente quirúrgico, sin literatura |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Literatura sobre uretritis gonocócica:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Ensayo clínico abierto de un solo brazo | Antimicrob Agents Chemother | Aztreonam 2 g intramuscular en dosis única en varones con gonorrea; se evalúa la erradicación, incluida la faringe |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Estudio clínico | Antimicrob Agents Chemother | Aztreonam 1 g i.m. vs. espectinomicina 2 g: sin fracasos en ninguno; satisfactorio en gonorrea uretral no complicada |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | Estudio clínico | Genitourin Med | Dosis única de 1 g i.m. eliminó la infección en 61 varones y 26 mujeres (salvo una faringe); bien tolerado |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Estudio clínico | Hinyokika Kiyo | Estudio epidemiológico y terapéutico japonés sobre terapia de dosis única en infecciones gonocócicas |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | Estudio clínico/in vitro | J Infect Dis | Eficacia de aztreonam frente a gonococos productores de penicilinasa, motivada por cepas resistentes a espectinomicina |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Informe de resistencia/microbiología | J Infect Chemother | Aparición de *N. gonorrhoeae* con alta resistencia a cefemas y aztreonam sin producción de betalactamasa |

Literatura de otras predicciones (indirecta):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3766490](https://pubmed.ncbi.nlm.nih.gov/3766490/) | 1986 | Serie clínica | Am J Dis Child | 59 niños con infecciones graves gramnegativas (incluye un caso de epiglotitis); evidencia no específica |
| [4079014](https://pubmed.ncbi.nlm.nih.gov/4079014/) | 1985 | Estudio clínico | Jpn J Antibiot | Infecciones graves en trastornos hematológicos: respuesta del 51,1 % de 90 pacientes evaluables; tratamiento de soporte |
| [34956120](https://pubmed.ncbi.nlm.nih.gov/34956120/) | 2021 | Genómica de resistencia | Front Microbiol | Coexistencia de bla NDM-1 y mcr-9 en *K. pneumoniae*; no relevante para la indicación predicha |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 09543002 | CAYSTON 75 mg polvo y disolvente para solución para inhalación por nebulizador (Gilead Sciences Ireland) | Polvo para solución para inhalación por nebulizador | No disponible en los datos compilados |
| 57781 | AZACTAM 1 g polvo para solución inyectable (Galenicum Derma S.L.U.) | Polvo para solución inyectable | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones / enfermedades asociadas (según el grafo de conocimiento, no el prospecto)**: enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal y enfermedad bronquial.
- **Interacciones farmacológicas**: se identificaron 27 interacciones; se muestran 20 en los datos compilados. Las de nivel **moderado** son ácido picosulfúrico, dicumarol y warfarina (vigilar anticoagulación). Otras de nivel no clasificado incluyen vancomicina, amikacina, anfotericina B, tacrolimus, heparina, morfina, inhibidores de la bomba de protones (pantoprazol, omeprazol, lansoprazol), hidrocortisona, dexametasona, ondansetrón, metronidazol, ácido acetilsalicílico, salbutamol, fluconazol y aciclovir.

Las advertencias y contraindicaciones oficiales del prospecto de la AEMPS no están disponibles; consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La mejor candidata (uretritis gonocócica) cuenta solo con estudios no aleatorizados, mayoritariamente de los años 80, y un ensayo abierto de un solo brazo de 2020, además de informes de resistencia. Las predicciones con mayor puntaje carecen de plausibilidad mecanística, de modo que el puntaje del modelo por sí solo no es indicativo de utilidad clínica. Uretritis gonocócica podría pasar a "Proceed with Guardrails" si se confirma con evidencia adicional, como línea alternativa en cepas resistentes.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), actualmente un vacío de datos bloqueante.
- Obtener datos del mecanismo de acción desde DrugBank.
- Verificar los diseños de estudio de la literatura (los títulos estaban truncados) y evaluar con detalle los resultados del ensayo de 2020, especialmente en faringe.
- Revisar datos de resistencia actuales de *N. gonorrhoeae* y compararlos con las guías vigentes.
- Evaluar la compatibilidad de vías de administración (aztreonam se comercializa en España como inyectable e inhalado) frente a las necesarias para la nueva indicación.
- Descartar formalmente las predicciones sin plausibilidad mecanística (hiperamilasemia, hiperviscosidad, analbuminemia, *Ureaplasma*).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


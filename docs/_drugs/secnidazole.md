---
layout: default
title: Secnidazole
parent: Evidencia alta (L1-L2)
nav_order: 727
evidence_level: L1
indication_count: 7
last_modified_at: 2026-10-14
description: "Secnidazole: nueva indicación predicha, Flujo vaginal (nivel de evidencia L1). Indicación original: Giardiasis, vaginosis bacteriana, vaginitis, vulvitis, vulvovaginitis…"
monitor_inn: "Secnidazole"
predicted_indications: ["postmenopausal atrophic vaginitis", "ulceration of vulva", "vaginal discharge", "vulvar neoplasm", "trichomonal vulvovaginitis", "leukoplakia of vagina", "vulvovaginal candidiasis"]
---

# Secnidazole
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

## Secnidazol: De Giardiasis y Vaginosis Bacteriana a Flujo Vaginal
{: .text-alpha }

## Resumen en Una Frase

Secnidazol es un antimicrobiano 5-nitroimidazol, originalmente utilizado para el tratamiento de la giardiasis, la vaginosis bacteriana y la tricomoniasis, entre otras infecciones.
El modelo TxGNN predice que podría ser efectivo para **flujo vaginal** (la tercera predicción de la lista, la primera con evidencia clínica real),
con **3 ensayos clínicos** y **15 publicaciones** que actualmente respaldan esta dirección. Sin embargo, la evidencia corresponde sobre todo a indicaciones ya existentes (vaginosis bacteriana y tricomoniasis).

> **Nota sobre la selección:** las dos primeras predicciones por puntaje (vaginitis atrófica posmenopáusica y úlcera de vulva) no tienen ninguna evidencia y se consideran biológicamente poco plausibles. Por eso el informe se centra en "flujo vaginal", la predicción con mayor respaldo. Las demás predicciones se resumen al final de la sección de conclusión.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Giardiasis, vaginosis bacteriana, vaginitis, vulvitis, vulvovaginitis, tricomoniasis (según el grafo de conocimiento; el texto de indicación de la autorización española está vacío) |
| Nueva Indicación Predicha | Flujo vaginal |
| Puntaje de Predicción TxGNN | 99.41% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, secnidazol es un 5-nitroimidazol, de la misma clase que metronidazol y tinidazol. Estos fármacos se activan por reducción en organismos anaerobios y protozoos como *Trichomonas vaginalis*, y dañan su ADN.

El flujo vaginal anormal es un síntoma, no una enfermedad en sí misma. Sus causas más frecuentes son la vaginosis bacteriana, la tricomoniasis y la candidiasis. Secnidazol ya está respaldado para las dos primeras, por lo que la predicción se solapa en gran medida con indicaciones existentes. No hay evidencia de que sirva en la candidiasis, porque los nitroimidazoles no actúan sobre hongos.

Por tanto, la predicción es razonable solo si el flujo tiene una causa confirmada de vaginosis bacteriana o tricomoniasis. No lo es para flujo no infeccioso o puramente candidiásico.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03935217](https://clinicaltrials.gov/study/NCT03935217) | Fase 3 | Completado | 147 | Ensayo aleatorizado, doble ciego, controlado con placebo y de tratamiento diferido, con una dosis oral única de 2 g en mujeres con tricomoniasis |
| [NCT02111629](https://clinicaltrials.gov/study/NCT02111629) | Fase 3 | Completado | 118 | Fluconazol más secnidazol en flujo vaginal sintomático (Bogotá, Colombia); el diseño combinado impide atribuir el efecto solo a secnidazol |
| [NCT03937869](https://clinicaltrials.gov/study/NCT03937869) | Fase 4 | Completado | 40 | Estudio abierto de seguridad de una dosis oral única de 2 g en adolescentes con vaginosis bacteriana; pequeño y sin grupo control |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28867602](https://pubmed.ncbi.nlm.nih.gov/28867602/) | 2017 | ECA (Fase 3) | Am J Obstet Gynecol | Eficacia y seguridad de secnidazol 2 g en dosis oral única frente a placebo en vaginosis bacteriana |
| [20885970](https://pubmed.ncbi.nlm.nih.gov/20885970/) | 2010 | ECA (Fase 3) | Infect Dis Obstet Gynecol | Estudio de no inferioridad, doble ciego y doble simulación, de secnidazol frente a metronidazol en vaginosis bacteriana |
| [29132478](https://pubmed.ncbi.nlm.nih.gov/29132478/) | 2017 | ECA | J Coll Physicians Surg Pak | Clindamicina vaginal en dosis múltiples frente a secnidazol oral en dosis única en vaginosis bacteriana sintomática |
| [33768237](https://pubmed.ncbi.nlm.nih.gov/33768237/) | 2021 | Fase 3 (según el título) | Clin Infect Dis | Eficacia y seguridad de secnidazol en dosis oral única frente a placebo en tricomoniasis |
| [31129560](https://pubmed.ncbi.nlm.nih.gov/31129560/) | 2019 | Revisión sistemática y metanálisis | Eur J Obstet Gynecol Reprod Biol | Eficacia y seguridad de secnidazol 2 g en dosis única en vaginosis bacteriana |
| [39463760](https://pubmed.ncbi.nlm.nih.gov/39463760/) | 2024 | Revisión sistemática y metanálisis en red | Front Cell Infect Microbiol | Comparación de eficacia y seguridad de varios fármacos para la vaginosis bacteriana |
| [22529484](https://pubmed.ncbi.nlm.nih.gov/22529484/) | 2012 | Estudio comparativo | Indian J Pharmacol | Tasas de curación de metronidazol, tinidazol, secnidazol y ornidazol en dosis única en vaginosis bacteriana |
| [29323627](https://pubmed.ncbi.nlm.nih.gov/29323627/) | 2018 | Estudio abierto de Fase 3 | J Womens Health | Seguridad de una dosis única de 2 g en mujeres y adolescentes con vaginosis bacteriana |
| [35863010](https://pubmed.ncbi.nlm.nih.gov/35863010/) | 2022 | Estudio in vitro | Microbiol Spectrum | Actividad de varios 5-nitroimidazoles frente a aislados clínicos de *T. vaginalis* en mujeres con flujo vaginal |
| [15733882](https://pubmed.ncbi.nlm.nih.gov/15733882/) | 2005 | Estudio clínico | Int J Gynaecol Obstet | Curación de la vaginosis bacteriana con una dosis oral única de 1 g de secnidazol |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 90874 | DEIRON 2 G GRANULADO EN SOBRE (Faes Farma S.A.) | Granulado en sobre | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 92 interacciones, y se muestran 20 en los datos compilados, todas de nivel moderado. Destacan:
  - **Antiinfecciosos nitroimidazólicos:** metronidazol y tinidazol.
  - **Estatinas:** rosuvastatina, simvastatina y atorvastatina.
  - **Antineoplásicos:** paclitaxel, cabazitaxel, carboplatino, bortezomib, carfilzomib, brentuximab vedotina y trastuzumab emtansina.
  - **Otros:** amiodarona, levodopa, adalimumab, certolizumab pegol, auranofina, yoduro I-123, yoduro I-131 y ácido picosulfúrico.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay dos ensayos de Fase 3 completados y varios ECA publicados con secnidazol en vaginosis bacteriana y tricomoniasis, que son causas principales del flujo vaginal. Sin embargo, es sobre todo respaldo a indicaciones ya existentes, no una indicación realmente nueva.

**Para avanzar se necesita:**
- Restringir el uso a casos con etiología confirmada (vaginosis bacteriana o tricomoniasis), no a flujo no infeccioso ni candidiásico.
- Obtener el texto de indicaciones y las advertencias y contraindicaciones del prospecto de la AEMPS.
- Obtener los datos de mecanismo de acción desde DrugBank.
- Revisar las interacciones, en especial con otros nitroimidazoles, estatinas y antineoplásicos.
- Verificar el diseño del estudio PMID 33768237 (Fase 3 aleatorizado, según su título).

**Otras predicciones (para referencia):**

| Predicción | Puntaje | Nivel | Decisión | Comentario |
|---|---|---|---|---|
| Vaginitis atrófica posmenopáusica | 99.70% | L5 | Hold | Causada por déficit de estrógenos; un mecanismo antimicrobiano es poco plausible |
| Úlcera de vulva | 99.42% | L5 | Hold | Causas heterogéneas; sin evidencia |
| Neoplasia de vulva | 99.37% | L5 | Hold | Sin evidencia ni mecanismo plausible |
| Vulvovaginitis tricomoniásica | 99.37% | L3 | Pregunta de investigación | Ya es una indicación original; una publicación de Fase 3 |
| Leucoplasia de vagina | 99.34% | L5 | Hold | Cambio epitelial queratinizante, no infeccioso |
| Candidiasis vulvovaginal | 99.16% | L4 | Hold | Los nitroimidazoles no actúan sobre hongos; el único ensayo es una combinación con fluconazol |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


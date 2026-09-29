---
layout: default
title: Norethisterone
parent: Solo predicción del modelo (L5)
nav_order: 383
evidence_level: L5
indication_count: 1
---

# Norethisterone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Noretisterona: De Anticoncepción y Trastornos Menstruales a Amenorrea

## Resumen en Una Frase

La noretisterona es un progestágeno sintético que, según la ficha farmacológica, se usa como anticonceptivo y para trastornos menstruales como la endometriosis o el sangrado vaginal anormal por desequilibrio hormonal.
El modelo TxGNN predice que podría ser efectivo para **amenorrea**, pero la evidencia disponible es indirecta: **7 ensayos clínicos** y **20 publicaciones** que, en su mayoría, describen la amenorrea como efecto o resultado y no como enfermedad tratada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las autorizaciones de AEMPS (texto de indicación vacío). Según la ficha farmacológica: anticoncepción y trastornos menstruales |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99,60 % |
| Nivel de Evidencia | L4 (sin evidencia clínica directa; solo evidencia indirecta y plausibilidad farmacológica) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, la noretisterona es un progestágeno sintético cuya diana farmacológica registrada es el receptor de progesterona (PGR). Suprime el eje hipotálamo-hipófisis-gónadas e induce atrofia endometrial.

Por eso, la amenorrea es un efecto farmacológico bien conocido de la exposición a este fármaco. Esto explica por qué un modelo basado en grafos asocia ambos conceptos con una puntuación tan alta.

Hay un punto que impide dar por buena la predicción. En los datos disponibles, la amenorrea aparece como **resultado o efecto secundario**, no como condición tratada. En los ensayos, la noretisterona (como acetato de noretindrona) solo es el componente de "add-back" de la combinación relugolix + estradiol + acetato de noretindrona, usada en sangrado menstrual abundante por miomas uterinos. Con estos registros no se puede resolver si el fármaco **trata** la amenorrea (por ejemplo, como prueba de progestágeno o regulación del ciclo) o si la **provoca**. Tampoco se verificó la indicación en el prospecto.

---

## Evidencia de Ensayos Clínicos

Ningún ensayo evalúa la noretisterona sola en amenorrea. Todos se centran en sangrado menstrual abundante asociado a miomas uterinos.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03049735](https://clinicaltrials.gov/study/NCT03049735) | Fase 3 | Completado | 388 | LIBERTY 1: relugolix con estradiol y acetato de noretindrona vs placebo durante 24 semanas en sangrado abundante por miomas. Indirecto: es una combinación y otra condición |
| [NCT03103087](https://clinicaltrials.gov/study/NCT03103087) | Fase 3 | Completado | 382 | LIBERTY 2: misma pauta combinada vs placebo. La amenorrea aparece probablemente como resultado secundario |
| [NCT03412890](https://clinicaltrials.gov/study/NCT03412890) | Fase 3 | Completado | 477 | Extensión abierta de un solo brazo de LIBERTY 1 y 2 (28 semanas). Aporta datos de durabilidad y seguridad, sin grupo control |
| [NCT03751124](https://clinicaltrials.gov/study/NCT03751124) | Fase 3 | Completado | 229 | Estudio de retirada aleatorizada de la combinación hasta 104 semanas. Informa sobre el mantenimiento de la supresión del sangrado |
| [NCT01817530](https://clinicaltrials.gov/study/NCT01817530) | Fase 2 | Completado | 571 | Elagolix (solo y con add-back) en sangrado abundante por miomas. No evalúa noretisterona |
| [NCT01441635](https://clinicaltrials.gov/study/NCT01441635) | Fase 2 | Completado | 271 | Prueba de concepto de elagolix frente a placebo. No incluye noretisterona |
| [NCT06953076](https://clinicaltrials.gov/study/NCT06953076) | N/A | Reclutando | 111 | Estudio ecográfico de los cambios en miomas durante el tratamiento con relugolix, estradiol y noretisterona. No aporta eficacia en amenorrea |

Un ensayo adicional, [NCT05620355](https://clinicaltrials.gov/study/NCT05620355) (Fase 3, estado desconocido, 312 participantes, BG2109 en sangrado abundante por miomas), no se pudo verificar: el título está truncado y no se confirma que incluya noretisterona ni amenorrea.

---

## Evidencia de Literatura

Solo se listan publicaciones con resumen disponible. Ninguna evalúa la noretisterona como tratamiento de la amenorrea.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6446442](https://pubmed.ncbi.nlm.nih.gov/6446442/) | 1980 | ECA | Contraception | Enantato de noretisterona vs DMPA en Bangladesh. La proporción de mujeres sin sangrado (amenorrea) fue mayor con DMPA que con NET-EN |
| [38530848](https://pubmed.ncbi.nlm.nih.gov/38530848/) | 2024 | Ensayo aleatorizado (WHICH) | PLoS One | DMPA-IM vs NET-EN: efectos sobre estradiol, medidas menstruales, psicológicas y conductuales relevantes para el riesgo de VIH |
| [41489365](https://pubmed.ncbi.nlm.nih.gov/41489365/) | 2026 | Estudio observacional/comparativo | Biology of Reproduction | Análisis secundario del ensayo WHICH (521 mujeres): descensos similares de estradiol con ambos anticonceptivos, pero más amenorrea con DMPA-IM |
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | Revisión sistemática | Cochrane Database Syst Rev | Anticonceptivos inyectables combinados: muy eficaces y reversibles; los cambios en el patrón de sangrado pueden limitar su aceptabilidad |
| [18843662](https://pubmed.ncbi.nlm.nih.gov/18843662/) | 2008 | Revisión sistemática | Cochrane Database Syst Rev | Versión anterior de la misma revisión Cochrane, con conclusiones similares |
| [37103532](https://pubmed.ncbi.nlm.nih.gov/37103532/) | 2023 | Revisión | Obstetrics and Gynecology | Antagonistas orales de GnRH (con esteroides de reemplazo) en leiomiomas uterinos con sangrado menstrual abundante |
| [2660092](https://pubmed.ncbi.nlm.nih.gov/2660092/) | 1989 | Revisión | Pediatric Clinics of North America | Principios de la anticoncepción hormonal en adolescentes |
| [1908716](https://pubmed.ncbi.nlm.nih.gov/1908716/) | 1991 | Revisión | Curr Opin Obstet Gynecol | Implantes subdérmicos de progestágeno: niveles bajos y estables, sin estrógenos |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 39927 | PRIMOLUT-NOR 5 mg COMPRIMIDOS (Bayer Hispania S.L.) | Comprimido |
| 44646 | PRIMOLUT-NOR 10 mg COMPRIMIDOS (Bayer Hispania S.L.) | Comprimido |

El texto de indicación aprobada no está disponible en los datos de ambas autorizaciones.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: no hay interacciones entre fármacos registradas. El único registro es farmacológico: la noretisterona actúa sobre el receptor de progesterona (PGR).

Consultar el prospecto para advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La puntuación TxGNN es muy alta (99,60 %), pero no hay ningún ensayo ni publicación que pruebe la noretisterona como tratamiento de la amenorrea. La amenorrea aparece como efecto o resultado, y los ensayos de Fase 3 evalúan una combinación en otra condición. Es una pregunta de investigación, no una candidata lista para avanzar.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de AEMPS (indicaciones, advertencias y contraindicaciones), lo que hoy bloquea el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Aclarar si la noretisterona **trata** la amenorrea (prueba de progestágeno, regulación del ciclo) o solo la **induce**
- Buscar estudios que evalúen la noretisterona sola en amenorrea, con indicación clínica explícita
- Verificar el ensayo NCT05620355, cuyos datos están truncados
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


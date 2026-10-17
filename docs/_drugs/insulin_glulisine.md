---
layout: default
title: Insulin Glulisine
parent: Solo predicción del modelo (L5)
nav_order: 421
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Insulin Glulisine: nueva indicación predicha, Diabetes mellitus tipo 1 (nivel de evidencia L5). Indicación original: Diabetes mellitus"
monitor_inn: "Insulin glulisine"
predicted_indications: ["thiamine-responsive dysfunction syndrome", "opsismodysplasia", "focal stiff limb syndrome", "classic stiff person syndrome", "autoimmune oophoritis", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
---

# Insulin Glulisine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Insulina glulisina: De Diabetes Mellitus a Diabetes Mellitus Tipo 1

## Resumen en Una Frase

La insulina glulisina es un análogo de insulina humana de acción rápida, originalmente utilizado para el tratamiento de la diabetes mellitus y la cetoacidosis diabética.
El modelo TxGNN predice que podría ser efectiva para la **diabetes mellitus tipo 1**, con **30 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.
Cabe señalar que la diabetes tipo 1 ya está dentro del alcance de la indicación original (diabetes mellitus), por lo que se trata más de una confirmación de una indicación existente que de un reposicionamiento propiamente dicho.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diabetes mellitus; cetoacidosis diabética |
| Nueva Indicación Predicha | Diabetes mellitus tipo 1 |
| Puntaje de Predicción TxGNN | 99,55% |
| Nivel de Evidencia | L2 (provisional; probablemente L1 si se verifican los ensayos pivotales de Fase 3) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la insulina glulisina es un análogo de insulina humana de acción rápida que se une al receptor de insulina, favorece la captación periférica de glucosa y suprime la producción hepática de glucosa. Su perfil farmacocinético se caracteriza por un inicio de acción más rápido y una duración más corta que la insulina humana regular.

La diabetes tipo 1 es una enfermedad de deficiencia absoluta de insulina, por lo que el reemplazo con insulina de acción rápida a la hora de las comidas (bolo) en un régimen basal-bolo es mecanísticamente directo. Por ello, la predicción es coherente con el amplio historial clínico existente y con el alto puntaje del modelo (0,996).

Es importante subrayar que esta predicción no constituye un reposicionamiento genuino: la diabetes tipo 1 queda comprendida dentro de la indicación original de diabetes mellitus. Las demás indicaciones predichas (rangos 2 a 10) tienen únicamente respaldo del modelo (L4-L5), sin ensayos ni literatura, y varias parecen reflejar comorbilidad (síndrome de la persona rígida) o incluso un efecto adverso conocido de la insulina (lipodistrofia localizada), por lo que no se consideran oportunidades terapéuticas.

---

## Evidencia de Ensayos Clínicos

Se han compilado 30 ensayos; se listan los 10 más relevantes, priorizando los de mayor tamaño y diseño más sólido.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00115570](https://clinicaltrials.gov/study/NCT00115570) | Fase 3 | Completado | 572 | Glulisina vs. lispro en niños y adolescentes con DM1 (26 semanas, abierto, paralelo) |
| [NCT00135941](https://clinicaltrials.gov/study/NCT00135941) | Fase 3 | Completado | 582 | Glargina + glulisina (MDI) vs. insulina premezclada en DM1 o DM2; resultados reportados por pacientes |
| [NCT00467376](https://clinicaltrials.gov/study/NCT00467376) | Fase 3 | Completado | 485 | Glulisina vs. lispro con glargina en DM1 o DM2 (12 semanas); eficacia, seguridad e hipoglucemia |
| [NCT00290979](https://clinicaltrials.gov/study/NCT00290979) | Fase 3 | Completado | 250 | No inferioridad de glulisina (HMR1964) frente a lispro en DM1 (28 semanas), según cambio de HbA1c |
| [NCT07070752](https://clinicaltrials.gov/study/NCT07070752) | Fase 3 | Completado | 224 | Inmunogenicidad de GP40321 frente a Apidra SoloStar en DM1 |
| [NCT00397553](https://clinicaltrials.gov/study/NCT00397553) | Fase 3 | Completado | 104 | Eficacia y seguridad de glulisina con glargina en DM1 (datos locales, abierto, no aleatorizado) |
| [NCT00046150](https://clinicaltrials.gov/study/NCT00046150) | Fase 3 | Completado | 59 | Seguridad de glulisina vs. insulina aspart en bombas de infusión (CSII) en DM1 |
| [NCT01194245](https://clinicaltrials.gov/study/NCT01194245) | Fase 2 | Completado | 135 | Lispro-PH20 o aspart-PH20 vs. lispro en DM1; estudio cruzado doble ciego aleatorizado |
| [NCT01848990](https://clinicaltrials.gov/study/NCT01848990) | Fase 4 | Completado | 456 | Hialuronidasa recombinante antes de la infusión (CSII) en DM1; cambio de HbA1c a 6 meses |
| [NCT00384085](https://clinicaltrials.gov/study/NCT00384085) | Fase 4 | Completado | 588 | Glargina con adición escalonada de glulisina vs. insulina premezclada en DM2 (64 semanas) |

Entre los demás ensayos figuran estudios de Fase 4 en CSII (p. ej., NCT00607087, n=289, glulisina vs. aspart y lispro) y estudios pediátricos sobre la glucemia posprandial. Nótese que el ensayo NCT04974528 (Afrezza, Fase 3, n=319) usa glulisina solo como comparador.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [16308840](https://pubmed.ncbi.nlm.nih.gov/16308840/) | 2005 | ECA | Horm Metab Res | Estudio multinacional, abierto, aleatorizado (683 pacientes) que compara glulisina con lispro en adultos con DM1 |
| [19614947](https://pubmed.ncbi.nlm.nih.gov/19614947/) | 2009 | Ensayo clínico | Diabetes Obes Metab | Eficacia y seguridad de glulisina vs. lispro en pacientes japoneses con DM1, con glargina como basal |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | Revisión sistemática | Drugs Today | Análogos de insulina en DM1 pediátrica, incluida glulisina |
| [20150026](https://pubmed.ncbi.nlm.nih.gov/20150026/) | 2010 | Revisión sistemática | Endocr Pract | Análogos de acción rápida vs. insulina regular en regímenes basal-bolo en DM1 (HbA1c, hipoglucemia, dosis) |
| [35933650](https://pubmed.ncbi.nlm.nih.gov/35933650/) | 2022 | Estudio comparativo | Acta Diabetol | Glulisina vs. lispro y aspart en bomba en DM1; efectividad relativa y tasas de hipoglucemia y cetoacidosis |
| [19496630](https://pubmed.ncbi.nlm.nih.gov/19496630/) | 2009 | Revisión | Drugs | Revisión de su uso en diabetes; no inferior a otras insulinas rápidas y de acción corta |
| [16706558](https://pubmed.ncbi.nlm.nih.gov/16706558/) | 2006 | Revisión | Drugs | Inicio más rápido y duración más corta que la insulina regular; control glucémico similar en DM1 |
| [28544684](https://pubmed.ncbi.nlm.nih.gov/28544684/) | 2017 | Estudio clínico | Pediatr Int | Glulisina en CSII en 20 niños con DM1; mejora de la glucemia posprandial tras 1 año |
| [18076215](https://pubmed.ncbi.nlm.nih.gov/18076215/) | 2008 | Farmacología clínica | Clin Pharmacokinet | Farmacocinética y farmacodinamia: absorción más rápida y duración más corta que la insulina regular |
| [25865292](https://pubmed.ncbi.nlm.nih.gov/25865292/) | 2016 | Revisión | Diabetes Metab Res Rev | Infusión subcutánea continua: poblaciones, seguridad, eficacia y farmacoeconomía |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 04285001 | APIDRA 100 unidades/ml solución inyectable en vial | Solución inyectable | No disponible en los datos |
| 04285032 | APIDRA 100 unidades/ml SoloStar solución inyectable en pluma precargada | Solución inyectable en pluma precargada | No disponible en los datos |
| 04285008 | APIDRA 100 unidades/ml solución inyectable en cartucho | Solución inyectable en cartucho | No disponible en los datos |
| 04285032IP | APIDRA SoloStar 100 unidades/ml solución inyectable en una pluma precargada | Solución inyectable en pluma precargada | No disponible en los datos |
| 04285024 | APIDRA 100 unidades/ml OptiClik solución inyectable en cartucho | Solución inyectable en cartucho | No disponible en los datos |

Las cinco autorizaciones están vigentes, son de monofármaco y pertenecen a Sanofi-Aventis Deutschland GmbH.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; las principales, de nivel moderado, incluyen:
  - Agonistas adrenérgicos y simpaticomiméticos: fenilefrina, epinefrina, pseudoefedrina, salbutamol y formoterol.
  - Betabloqueantes: acebutolol.
  - Otros antidiabéticos: metformina, pioglitazona, alogliptina y albiglutida.
  - Corticoides: hidrocortisona sistémica (moderada); hidrocortisona y alclometasona tópicas (leve).
  - Otros: acetazolamida, hidroclorotiazida, doxiciclina, etinilestradiol, estradiol, alpelisib y etanol.

  Estas interacciones pueden alterar el control glucémico, con riesgo de hipoglucemia o hiperglucemia, por lo que requieren seguimiento.
- **Riesgo adicional**: la lipodistrofia localizada en el sitio de inyección es un efecto adverso conocido de la terapia con insulina (rotar los sitios de inyección).

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un amplio cuerpo de ensayos clínicos (incluidos varios de Fase 3 en DM1) y literatura que respalda la eficacia y seguridad de la glulisina en diabetes tipo 1, además de su comercialización vigente en España. Sin embargo, la indicación ya está cubierta por la aprobación original, y falta verificar formalmente el nivel de evidencia y los datos de seguridad de la ficha técnica.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto/ficha técnica de la AEMPS para obtener advertencias, contraindicaciones y el texto de las indicaciones aprobadas (actualmente vacío).
- Confirmar el nivel de evidencia: verificar los ensayos pivotales de Fase 3 (p. ej., NCT00115570, NCT00290979, PMID 16308840) para valorar la elevación a L1.
- Completar los datos de mecanismo de acción desde DrugBank.
- Plan de monitoreo de hipoglucemia y de interacciones farmacológicas.
- No priorizar las indicaciones de rangos 2 a 10, que solo cuentan con predicción del modelo (L4-L5); en las lipodistrofias existe además una señal de seguridad. La agenesia pancreática (L4) podría estudiarse como pregunta de investigación, con evaluación específica de dosis y seguridad neonatal.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Pentamidine
parent: Solo predicción del modelo (L5)
nav_order: 622
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Pentamidine: nueva indicación predicha, Queratoconjuntivitis epitelial punteada (nivel de evidencia L5). Indicación original: Neumocistosis…"
monitor_inn: "Pentamidine"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "neurotrophic keratopathy", "exposure keratitis", "non-human animal disease", "congenital analbuminemia"]
---

# Pentamidine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Pentamidina: De Neumocistosis a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

Pentamidina es un antimicrobiano utilizado originalmente para tratar la neumocistosis y la tripanosomiasis (incluida la tripanosomiasis africana humana).
El modelo TxGNN predice que podría ser efectiva para la **queratoconjuntivitis epitelial punteada**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Neumocistosis, tripanosomiasis africana humana y tripanosomiasis (según el grafo de conocimiento; el texto de indicación de la autorización española está vacío) |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99,73% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de la pentamidina en los datos compilados para este informe. Según la información conocida, pentamidina es un agente antiprotozoario y antifúngico, con eficacia establecida en infecciones como la neumocistosis y la tripanosomiasis.

La relación con la nueva indicación es débil. Los datos no respaldan ningún vínculo mecanístico entre la pentamidina y la queratoconjuntivitis epitelial punteada. El puntaje de 0,997 es una predicción computacional sin ensayos ni literatura detrás. Cualquier justificación antimicrobiana o antiinflamatoria para una enfermedad de la superficie ocular sería especulativa.

Además, la toxicidad sistémica conocida de la pentamidina (nefrotoxicidad, alteraciones de la glucemia, prolongación del QT) y su elevada carga de interacciones farmacológicas pesarían en contra de su uso sin una justificación clara.

Otras predicciones del modelo, todas con evidencia L5 y recomendación Hold: queratopatía neurotrófica (99,67%), queratitis por exposición (99,36%), enfermedad animal no humana (99,13%, categoría no específica y no accionable en humanos, probablemente un artefacto de la ontología) y analbuminemia congénita (99,09%).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59621 | PENTACARINAT 300 MG POLVO PARA SOLUCIÓN INYECTABLE | Polvo para suspensión inyectable | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto del prospecto): hipertensión, torsades de pointes, enfermedad renal, pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, hiperglucemia, hipoglucemia, diabetes mellitus, cetoacidosis diabética, asma, trastornos hipotensivos, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, anemia (incluida la macrocítica), paro cardíaco súbito, enfermedad de la conducción cardíaca y leucopenia.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones. Las principales, de nivel moderado, incluyen:
  - Antidiabéticos: acarbosa, albiglutida, alogliptina, metformina, pioglitazona, canagliflozina, clorpropamida, dapagliflozina.
  - Antifúngicos nefrotóxicos: anfotericina B y anfotericina B (complejo lipídico).
  - Inhibidores de la bomba de protones y antagonistas H2: omeprazol, rabeprazol, famotidina.
  - Macrólidos: claritromicina.
  - Fármacos gastrointestinales: loperamida, mesalazina, balsalazida, bisacodilo, ácido picosulfúrico, polietilenglicol con electrolitos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto de la AEMPS.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos clínicos ni literatura, sin mecanismo de acción disponible y con un perfil de seguridad sistémico preocupante para una enfermedad de la superficie ocular.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la pentamidina (p. ej., consulta a DrugBank).
- Advertencias y contraindicaciones del prospecto oficial de la AEMPS.
- Una hipótesis mecanística plausible para la superficie ocular, respaldada por estudios preclínicos.
- Evaluación de la compatibilidad de vía y formulación (el producto autorizado es inyectable; no hay datos de formulación oftálmica).
- Búsqueda sistemática de literatura y ensayos clínicos que no aparecen en los datos actuales.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Clarithromycin
parent: Solo predicción del modelo (L5)
nav_order: 187
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-31
description: "Clarithromycin: nueva indicación predicha, hiperamilasemia (nivel de evidencia L4). Indicación original: Infecciones bacterianas (otitis media infecciosa…"
monitor_inn: "Clarithromycin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility"]
---

# Clarithromycin
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

## Claritromicina: De Otitis Media Infecciosa a hiperamilasemia
{: .text-alpha }

## Resumen en Una Frase

Claritromicina es un antibiótico macrólido, utilizado originalmente para tratar infecciones bacterianas como la otitis media infecciosa, las infecciones estreptocócicas y estafilocócicas, la neumonía y la sinusitis maxilar.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia**,
pero solo hay **0 ensayos clínicos** y **1 publicación** (un reporte de caso), por lo que la evidencia es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones bacterianas (otitis media infecciosa, infecciones estreptocócicas y estafilocócicas, neumonía, sinusitis maxilar) |
| Nueva Indicación Predicha | Hiperamilasemia |
| Puntaje de Predicción TxGNN | 0.9935 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 7) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

Nota: los textos de indicación aprobada de las autorizaciones de la AEMPS están vacíos en los datos compilados. Por ello, la indicación original procede de las indicaciones registradas en el grafo de conocimiento utilizado por el modelo.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, claritromicina es un antibiótico de la clase de los macrólidos, su eficacia en infecciones respiratorias y otras infecciones bacterianas está establecida, pero los datos compilados no permiten sustentar un mecanismo que la vincule con la hiperamilasemia.

La única publicación disponible (PMID 15228140, 2004) es un reporte de caso de infección pulmonar por *Mycobacterium abscessus* acompañada de macroamilasemia primaria. En ese contexto, la claritromicina probablemente se empleó por su acción antimicrobiana, no como tratamiento de la hiperamilasemia. La coincidencia entre ambas condiciones en un mismo paciente no demuestra un efecto terapéutico.

Por tanto, el alto puntaje del modelo no está respaldado por una justificación biológica en los datos disponibles. Esta predicción debe considerarse una hipótesis sin sustento mecanístico, y es posible que sea un artefacto del modelo TxGNN (aprendizaje profundo).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15228140](https://pubmed.ncbi.nlm.nih.gov/15228140/) | 2004 | Reporte de caso | Nihon Kokyuki Gakkai Zasshi | Paciente de 76 años con infección pulmonar por *M. abscessus* y macroamilasemia primaria concomitante. No demuestra un efecto de la claritromicina sobre la hiperamilasemia. |

---

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de medicamentos de un solo principio activo; ninguna cancelada).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 90077 | Claritromicina Brown & Burk 250 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos |
| 78064 | Claritromicina Teva 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos |
| 60518 | Klacid 500 mg granulado para suspensión oral | Granulado para solución oral | No disponible en los datos |
| 64663 | Claritromicina Aristo 500 mg comprimidos recubiertos EFG | Comprimido recubierto | No disponible en los datos |
| 64670 | Claritromicina Farmalider 250 mg comprimidos recubiertos con película EFG | Comprimido recubierto | No disponible en los datos |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): síndrome de QT largo, torsades de pointes, taquicardia ventricular (incluida la polimórfica catecolaminérgica), insuficiencia hepática, enfermedad hepática, colestasis, porfiria, enfermedad renal, enfermedad de la vesícula biliar, osteoporosis, fractura ósea, colitis por *Clostridium difficile*, enterocolitis necrotizante perinatal, miastenia gravis y mononucleosis infecciosa.
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total; entre las mostradas destacan las de nivel **mayor** con abemaciclib, fentanilo y acalabrutinib. Entre las de nivel moderado figuran paclitaxel, tramadol, nifedipino, ethinylestradiol, hidrocortisona, adenosina, afatinib, famotidina, formoterol, acarbosa, abiraterona, flunisolida, trastuzumab emtansina y abametapir (tópico). Las de nivel menor incluyen dolutegravir, zidovudina y loratadina.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa casi exclusivamente en el puntaje del modelo; la única publicación es un reporte de caso sin evidencia de efecto terapéutico, y no hay ensayos clínicos ni mecanismo plausible. Además, la claritromicina presenta riesgos relevantes (prolongación del QT e interacciones mayores).

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la claritromicina y una hipótesis biológica que la relacione con la hiperamilasemia
- Revisión del prospecto de la AEMPS para advertencias y contraindicaciones oficiales
- Estudios clínicos o series de casos que evalúen directamente el efecto de claritromicina sobre la amilasa
- Evaluación de otras predicciones de mayor plausibilidad, como la queratoconjuntivitis epitelial punteada (nivel L4, vínculo antiinflamatorio indirecto de los macrólidos, a verificar en el estudio PMID 38472959)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


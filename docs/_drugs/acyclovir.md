---
layout: default
title: Acyclovir
parent: Evidencia alta (L1-L2)
nav_order: 22
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Acyclovir: nueva indicación predicha, Verrugas comunes (la predicción de mayor puntaje… (nivel de evidencia L2). Indicación original: Infecciones por herpes simple, herpes zóster, varicela, herpes la…"
monitor_inn: "Acyclovir"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "common wart", "post-infectious neuralgia", "hepatitis C induced liver cirrhosis", "eosinophilic pustular folliculitis", "sequela of COVID-19", "vulvovaginal candidiasis", "papular urticaria", "disease of orbital region", "epidemic keratoconjunctivitis"]
---

# Acyclovir
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **10** 
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

# Aciclovir: De Infecciones por Herpes a Verrugas Comunes

## Resumen en Una Frase

Aciclovir es un antiviral análogo de nucleósidos, utilizado originalmente para tratar infecciones por herpes simple, herpes zóster, varicela, herpes labial, encefalitis herpética y herpes genital.
El modelo TxGNN predice que podría ser efectivo para **verrugas comunes** (la segunda predicción mejor clasificada, y la primera con ensayos clínicos), con **4 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones por herpes simple, herpes zóster, varicela, herpes labial, encefalitis herpética y herpes genital (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Verrugas comunes (la predicción de mayor puntaje, queratoconjuntivitis epitelial punteada, 99.67 %, solo tiene evidencia L5) |
| Puntaje de Predicción TxGNN | 99.46 % |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, aciclovir se fosforila por la timidina quinasa viral y, en su forma activa, inhibe la ADN polimerasa de los herpesvirus. Su eficacia en infecciones por herpes simple y varicela-zóster está comprobada.

Las verrugas comunes están causadas por el virus del papiloma humano (VPH), un virus ADN. Esto crea una afinidad conceptual con la indicación original, pero el mecanismo clásico de aciclovir no aplica directamente, porque el VPH no codifica timidina quinasa. Los mecanismos propuestos incluyen la modulación inmunitaria tras la inyección intralesional o una inhibición inespecífica de la síntesis de ADN viral.

La señal clínica es consistente: varios ensayos pequeños, en su mayoría del mismo entorno regional, comparan aciclovir intralesional con crioterapia, vitamina D3, antígeno de Candida, 5-FU y vacuna contra el VPH con resultados alentadores. Sin embargo, son estudios pequeños, mayormente sin enmascaramiento y de calidad incierta, y ninguno es un ensayo confirmatorio de Fase 3. La justificación mecanística es débil pese a la señal clínica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06261684](https://clinicaltrials.gov/study/NCT06261684) | Fase 2/3 | Desconocido | 92 | ECA de aciclovir intralesional vs. crioterapia en verrugas plantares; diseño comparativo más relevante. Existe un ECA publicado relacionado (PMID 40889709) |
| [NCT05429151](https://clinicaltrials.gov/study/NCT05429151) | Fase 4 | Desconocido | 40 | Aciclovir intralesional vs. antígeno de Candida en verrugas plantares |
| [NCT07448844](https://clinicaltrials.gov/study/NCT07448844) | Fase 4 | Reclutando | 40 | Vitamina D3 vs. aciclovir intralesional en verrugas cutáneas virales; aún sin resultados |
| [NCT05324904](https://clinicaltrials.gov/study/NCT05324904) | No aplica | Desconocido | 44 | Vitamina D3 vs. aciclovir intralesional en verrugas plantares; aciclovir actúa como comparador |

---

## Evidencia de Literatura

Se listan las publicaciones más relevantes para verrugas comunes (prioridad: ECA y estudios comparativos).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40889709](https://pubmed.ncbi.nlm.nih.gov/40889709/) | 2026 | ECA | J Am Acad Dermatol | Aciclovir intralesional vs. crioterapia en verrugas plantares |
| [38822848](https://pubmed.ncbi.nlm.nih.gov/38822848/) | 2024 | ECA | Arch Dermatol Res | Aciclovir intralesional vs. vacuna de hepatitis B en verrugas plantares resistentes (48 pacientes) |
| [40488756](https://pubmed.ncbi.nlm.nih.gov/40488756/) | 2025 | Estudio comparativo/ECA | Arch Dermatol Res | Aciclovir vs. 5-fluorouracilo intralesional en verrugas recalcitrantes |
| [40056255](https://pubmed.ncbi.nlm.nih.gov/40056255/) | 2025 | Estudio comparativo | Arch Dermatol Res | Aciclovir intralesional vs. vacuna tetravalente contra el VPH en verrugas recalcitrantes (60 pacientes) |
| [37303436](https://pubmed.ncbi.nlm.nih.gov/37303436/) | 2023 | Estudio comparativo | Cureus | Aciclovir intralesional vs. inmunoterapia con PPD en verrugas virales |
| [34412535](https://pubmed.ncbi.nlm.nih.gov/34412535/) | 2022 | Estudio clínico | J Cutan Med Surg | Aciclovir intralesional como opción terapéutica potencial en verrugas cutáneas |
| [41686619](https://pubmed.ncbi.nlm.nih.gov/41686619/) | 2026 | Revisión sistemática y metaanálisis en red | Medicine | Comparación de modalidades de tratamiento de verrugas cutáneas, incluido aciclovir intralesional |
| [38793636](https://pubmed.ncbi.nlm.nih.gov/38793636/) | 2024 | Casos clínicos y revisión | Viruses | Remisión de enfermedades relacionadas con VPH (condilomas) con aciclovir o valaciclovir |
| [26885794](https://pubmed.ncbi.nlm.nih.gov/26885794/) | 2016 | Estudio clínico/caso | J Drugs Dermatol | Verrugas plantares persistentes que se resolvieron tras aciclovir oral por herpes zóster |
| [6467981](https://pubmed.ncbi.nlm.nih.gov/6467981/) | 1984 | Publicación clínica | Cutis | Verrugas vulgares y pomada de aciclovir |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 63759 | Aciclovir Viatris 200 mg comprimidos EFG | Comprimido | No disponible en los datos compilados |
| 62686 | Aciclovir Sandoz 800 mg comprimidos EFG | Comprimido | No disponible en los datos compilados |
| 85741 | Hervax 250 mg polvo para solución para perfusión EFG | Polvo para solución para perfusión | No disponible en los datos compilados |
| 56633 | Zovirax 30 mg/g pomada oftálmica | Pomada oftálmica | No disponible en los datos compilados |
| 56780 | Zovirax 50 mg/g crema | Crema | No disponible en los datos compilados |

En total hay 20 autorizaciones vigentes (todas de monofármaco, ninguna cancelada), con formas orales, perfusión intravenosa, crema y pomada oftálmica.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): hipertensión, enfermedad renal, insuficiencia renal, hiperglucemia, diabetes mellitus, cetoacidosis diabética, insuficiencia suprarrenal, obesidad, ictus y trastornos cerebrovasculares, infarto de miocardio, síndrome hemolítico urémico, púrpura trombocitopénica, enfermedad vascular periférica, atrofia cutánea y telangiectasias, entre otras. Deben verificarse con el prospecto oficial.
- **Interacciones farmacológicas** (100 registradas): las de nivel moderado incluyen balsalazida, mesalazina, olsalazina, sulfasalazina y trospio. Otras con nivel no clasificado incluyen anfotericina B, manitol, metformina, morfina, omeprazol, pantoprazol, doxiciclina y epinefrina.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe una señal clínica consistente, con un ECA de Fase 2/3 y varios estudios comparativos de aciclovir intralesional en verrugas, pero son pequeños, de calidad incierta y con mecanismo débil. Además, el uso intralesional no corresponde a las formas actualmente autorizadas, por lo que solo procede avanzar con salvaguardas.

**Para avanzar se necesita:**
- Confirmar los resultados del ensayo NCT06261684 y del ECA publicado (PMID 40889709).
- Un ensayo confirmatorio de Fase 3, multicéntrico, con enmascaramiento y comparadores estándar.
- Datos del mecanismo de acción y de la vía de administración (la formulación intralesional a partir de la perfusión no está contemplada en las autorizaciones).
- Advertencias y contraindicaciones del prospecto de la AEMPS, actualmente sin datos.
- Plan de seguridad para pacientes con enfermedad renal y otras poblaciones de riesgo.
- Evaluar de forma independiente las otras predicciones: queratoconjuntivitis epitelial punteada (L5, Hold), enfermedades de la región orbitaria (L3, vinculada a herpes ocular, extensión de indicaciones existentes) y otras con mecanismo no plausible (hepatitis C, candidiasis vulvovaginal, queratoconjuntivitis epidémica).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


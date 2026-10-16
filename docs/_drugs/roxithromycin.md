---
layout: default
title: Roxithromycin
parent: Solo predicción del modelo (L5)
nav_order: 716
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Roxithromycin: nueva indicación predicha, Lepra (nivel de evidencia L5). Indicación original: No disponible en las autorizaciones de AEMPS"
monitor_inn: "roxithromycin"
predicted_indications: ["leprosy", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "Ambras type hypertrichosis universalis congenita", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "nephrogenic syndrome of inappropriate antidiuresis", "pulmonary hypertension"]
---

# Roxithromycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Roxitromicina: De Infecciones Bacterianas a Lepra

## Resumen en Una Frase

Roxitromicina es un antibiótico macrólido comercializado en España en comprimidos recubiertos de 150 mg y 300 mg, utilizado para infecciones bacterianas (respiratorias, urinarias y de tejidos blandos).
El modelo TxGNN predice que podría ser efectivo para **lepra**, con **5 publicaciones** (estudios preclínicos y revisiones) y **ningún ensayo clínico** que respaldan actualmente esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las autorizaciones de AEMPS; según la farmacología, infecciones respiratorias, urinarias y de tejidos blandos |
| Nueva Indicación Predicha | Lepra |
| Puntaje de Predicción TxGNN | 99.70% |
| Nivel de Evidencia | L3 (con salvedades: la evidencia es mayoritariamente preclínica, en el límite L3/L4) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento general, roxitromicina es un macrólido que inhibe la síntesis proteica bacteriana al unirse a la subunidad ribosomal 50S. Su actividad *in vitro* es similar a la de eritromicina, con acción predominante frente a bacterias grampositivas y algunas gramnegativas, como *Legionella pneumophila*.

La lepra está causada por *Mycobacterium leprae*, una bacteria. Varios estudios preclínicos indican que algunos macrólidos tienen actividad frente a este microorganismo. En un modelo de ratón (almohadilla plantar), roxitromicina y claritromicina resultaron activas y bactericidas, mientras que eritromicina y azitromicina fueron inactivas. Claritromicina mostró mayor actividad que roxitromicina, posiblemente por alcanzar concentraciones más altas en el sitio de infección.

Una revisión japonesa también señala que roxitromicina tiene actividad antimicobacteriana frente a *M. leprae* y efectos antiinflamatorios e inmunomoduladores. Sin embargo, todos los datos proceden de modelos no humanos y no hay ensayos clínicos, por lo que la plausibilidad es mecanística pero la evidencia de eficacia en personas es insuficiente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [1648889](https://pubmed.ncbi.nlm.nih.gov/1648889/) | 1991 | Preclínico (ratón) | Antimicrob Agents Chemother | Roxitromicina y claritromicina fueron activas y bactericidas frente a *M. leprae* en la almohadilla plantar de ratón; claritromicina fue superior. Eritromicina y azitromicina fueron inactivas |
| [3072920](https://pubmed.ncbi.nlm.nih.gov/3072920/) | 1988 | Preclínico (in vitro e in vivo) | Antimicrob Agents Chemother | Comparación de la actividad de nuevos macrólidos frente a *M. leprae*, con determinación de concentraciones séricas en ratones |
| [2665640](https://pubmed.ncbi.nlm.nih.gov/2665640/) | 1989 | Preclínico (in vitro, macrófagos) | Antimicrob Agents Chemother | Evaluación rápida de más de 25 antimicrobianos frente a *M. leprae* en macrófagos murinos mediante síntesis de glucolípido fenólico I |
| [10481449](https://pubmed.ncbi.nlm.nih.gov/10481449/) | 1999 | Revisión | Nihon Hansenbyo Gakkai Zasshi | Claritromicina, roxitromicina, minociclina y fosfomicina combinan actividad antimicobacteriana con efectos antiinflamatorios e inmunomoduladores en la neuropatía periférica lepromatosa |
| [12762831](https://pubmed.ncbi.nlm.nih.gov/12762831/) | 2003 | Revisión | Am J Clin Dermatol | Guía sobre la selección y el uso adecuado de macrólidos en infecciones cutáneas |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 64815 | Roxitromicina Sandoz 300 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos compilados |
| 64803 | Roxitromicina Sandoz 150 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos compilados |

## Consideraciones de Seguridad

**Interacciones Farmacológicas**: la consulta de interacciones se completó y devolvió un registro de tipo farmacológico: roxitromicina actúa sobre el receptor de motilina (MLNR), un efecto conocido en macrólidos que puede asociarse a estimulación de la motilidad gastrointestinal. No se identificaron interacciones con otros fármacos ni niveles de gravedad.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para lepra es mecanísticamente plausible, pero se apoya solo en estudios preclínicos antiguos (1988-1991) y revisiones, sin ensayos clínicos. Además, claritromicina mostró mayor actividad que roxitromicina, por lo que roxitromicina no parece la mejor opción dentro de su clase.

**Para avanzar se necesita:**
- Datos de advertencias y contraindicaciones del prospecto de AEMPS
- Datos detallados del mecanismo de acción (MOA)
- Texto de las indicaciones aprobadas en las autorizaciones españolas
- Comparación directa con claritromicina y con los regímenes estándar de lepra
- Estudios clínicos o datos observacionales en humanos que respalden eficacia y seguridad en lepra

**Otras predicciones del modelo:** las demás indicaciones predichas (hipertricosis, síndromes malformativos, síndrome nefrogénico de antidiuresis inapropiada, hipertensión pulmonar, entre otras) carecen de ensayos y de literatura directa, y no tienen una relación mecanística plausible con roxitromicina. Por ello se recomienda mantenerlas en espera (Hold).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


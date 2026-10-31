---
layout: default
title: Ciprofloxacin
parent: Solo predicción del modelo (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
monitor_inn: "Ciprofloxacin"
predicted_indications: ["diffuse scleroderma", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "punctate epithelial keratoconjunctivitis", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
description: "Ciprofloxacin: nueva indicación predicha, Esclerodermia difusa (diffuse scleroderma) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Ciprofloxacin
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

## Ciprofloxacin: Esclerodermia difusa (diffuse scleroderma)
{: .text-alpha }

## Resumen en Una Frase

Ciprofloxacino es una fluoroquinolona antibacteriana, originalmente utilizada para tratar infecciones como la fiebre tifoidea, la salmonelosis, la neumonía bacteriana y las infecciones por *Pseudomonas aeruginosa*.
El modelo TxGNN predice que podría ser efectivo para **esclerodermia difusa**, aunque actualmente solo hay **0 ensayos clínicos** y **2 publicaciones** de apoyo, de carácter exploratorio.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Esclerodermia difusa (diffuse scleroderma) |
| Puntaje de Predicción TxGNN | 0.9987 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 13) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, ciprofloxacino es una fluoroquinolona cuya eficacia antibacteriana está comprobada, y su acción clásica consiste en inhibir la ADN girasa y la topoisomerasa IV bacterianas. Esto no explica por sí solo un efecto en la esclerodermia.

Para la esclerodermia difusa se plantean dos vínculos posibles. El primero es un posible efecto antifibrótico en la piel (PMID 20507401), aunque su mecanismo no está bien establecido. El segundo es indirecto: tratar el sobrecrecimiento bacteriano del intestino delgado, frecuente en la esclerosis sistémica (PMID 7728404), que causa diarrea y malabsorción.

La evidencia se limita a literatura pequeña y exploratoria, sin datos confirmatorios sobre desenlaces cutáneos o de fibrosis. Por ello la predicción debe considerarse una hipótesis.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Estudio clínico exploratorio (el resumen menciona un ensayo controlado, doble ciego y aleatorizado) | The Journal of Dermatology | Evalúa si ciprofloxacino oral reduce la gravedad de la esclerodermia y su utilidad como antifibrótico en la piel |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Observacional | British Journal of Rheumatology | Sobrecrecimiento bacteriano del intestino delgado en 24 pacientes con esclerosis sistémica con diarrea y pérdida de peso; evalúa métodos diagnósticos y resultado del tratamiento |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 58407 | Ciprofloxacino Tarbis 250 mg | Comprimido recubierto con película | No disponible |
| 62709 | Ciprofloxacino Pensa 500 mg | Comprimido recubierto con película | No disponible |
| 62646 | Ciprofloxacino Normon 2 mg/ml | Solución para perfusión | No disponible |
| 61521 | Septocipro Ótico 1 mg | Gotas óticas en solución | No disponible |
| 60608 | Oftacilox 3 mg/ml | Colirio en solución | No disponible |

Hay 20 autorizaciones vigentes, todas de medicamentos con un solo principio activo. Incluyen comprimidos, solución para perfusión, gotas óticas, colirio y suspensión oral.

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del texto del prospecto): síndrome de QT largo (incluido el familiar), torsades de pointes, epilepsia, enfermedad renal, deficiencia de potasio, tendinitis y otras afecciones tendinosas (bursitis aquílea, espolón calcáneo, periartritis), neuropatía periférica y enfermedades del sistema nervioso periférico, colitis por *Clostridium difficile*, miastenia gravis y enfermedades de la unión neuromuscular.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las de nivel **mayor** figuran los corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona) y bupropión. Entre las de nivel moderado figuran antidiabéticos (metformina, pioglitazona, acarbosa, alogliptina), famotidina, loperamida, ácido acetilsalicílico y aprepitant, entre otros.
- Los corticoides son relevantes en la esclerosis sistémica por su uso frecuente en enfermedades autoinmunes. Se asocian con un mayor riesgo de tendinopatía junto con fluoroquinolonas, lo que exige cautela.
- Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (0.9987), pero el respaldo se limita a dos publicaciones exploratorias, sin ensayos clínicos registrados y con un mecanismo antifibrótico no establecido. Además, los pacientes con esclerodermia podrían usar corticoides, que interactúan de forma importante con ciprofloxacino y aumentan el riesgo de tendinopatía.

**Para avanzar se necesita:**
- Revisar el texto completo del estudio de 2010 (PMID 20507401) para confirmar diseño, tamaño muestral y resultados.
- Datos del mecanismo de acción y de la plausibilidad antifibrótica.
- Un ensayo clínico confirmatorio con desenlaces cutáneos y de fibrosis.
- Obtener del prospecto de la AEMPS las advertencias, contraindicaciones e indicaciones aprobadas.
- Evaluar el perfil de seguridad en esta población (tendones, QT, neuropatía y uso concomitante de corticoides).

**Otras predicciones del modelo:** la única otra con respaldo sustancial es la **peste septicémica** (nivel L3), por el uso consolidado de fluoroquinolonas contra *Yersinia pestis* y ensayos aleatorizados sobre peste bubónica. Es una extensión dentro de la misma clase antiinfecciosa más que un reposicionamiento, y requiere confirmar evidencia directa en peste septicémica. Las demás predicciones carecen de mecanismo y de evidencia clínica, y en algunos casos, como la neuropatía periférica adquirida asociada a enfermedad hematológica, plantean preocupaciones de seguridad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


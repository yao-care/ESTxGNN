---
layout: default
title: Risankizumab
parent: Solo predicción del modelo (L5)
nav_order: 704
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Risankizumab: nueva indicación predicha, Dermatitis (nivel de evidencia L5). Indicación original: Psoriasis (la ficha de autorización no incluye texto de indicación"
monitor_inn: "RISANKIZUMAB"
predicted_indications: ["dermatitis", "neonatal dermatomyositis", "amyopathic dermatomyositis", "acrodermatitis chronica atrophicans", "acne keloid", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "hydroa vacciniforme, familial", "severe nonproliferative diabetic retinopathy", "pityriasis lichenoides", "acute lichenoid pityriasis"]
---

# Risankizumab
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

## Risankizumab: De Psoriasis a Dermatitis
{: .text-alpha }

## Resumen en Una Frase

Risankizumab es un anticuerpo monoclonal humanizado que bloquea la subunidad p19 de la IL-23 y se utiliza originalmente para el tratamiento de la psoriasis.
El modelo TxGNN predice que podría ser efectivo para **dermatitis**, con **2 ensayos clínicos** y **20 publicaciones** relacionados.
Sin embargo, el único ensayo controlado de Fase 2 (en dermatitis atópica) no demostró eficacia, por lo que la predicción debe interpretarse con mucha cautela.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Psoriasis (la ficha de autorización no incluye texto de indicación; se toma de las indicaciones originales del grafo de conocimiento) |
| Nueva Indicación Predicha | Dermatitis |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L2 (un ECA de Fase 2 completado, con resultado no favorable) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Risankizumab bloquea selectivamente la subunidad p19 de la IL-23, situada aguas arriba de la activación de las células Th17/Th22. Este mecanismo está bien validado en la psoriasis. No se dispone de datos formales de mecanismo de acción en la base de datos consultada, por lo que esta descripción se basa en el análisis mecanístico del informe y en la literatura.

La dermatitis atópica está impulsada sobre todo por la vía Th2, y el eje IL-23 contribuye solo de forma menor, por lo que el fundamento mecanístico es más débil que en la psoriasis. El ensayo de Fase 2 (NCT03706040) no mostró una eficacia relevante frente a placebo, lo que concuerda con esa limitación. Es probable que el puntaje tan alto de TxGNN refleje la cercanía con la psoriasis en el grafo de conocimiento y no evidencia independiente en dermatitis atópica.

Queda un posible nicho en fenotipos de solapamiento psoriasis/eccema, donde hay reportes de casos con uso combinado con dupilumab. También hay reportes de eccema paradójico durante el tratamiento con inhibidores de IL-23, lo que sugiere que el fármaco incluso podría provocar lesiones eccematosas en algunos pacientes.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03706040](https://clinicaltrials.gov/study/NCT03706040) | Fase 2 | Completado | 172 | Estudio aleatorizado, doble ciego y controlado con placebo de risankizumab en dermatitis atópica moderada-grave en adultos y adolescentes; la publicación asociada indica que no se demostró eficacia |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Fase 4 | Aún sin reclutar | 10 | Estudio de un microdispositivo cutáneo in situ para probar fármacos en dermatitis atópica y psoriasis; relevancia limitada para la eficacia |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36588137](https://pubmed.ncbi.nlm.nih.gov/36588137/) | 2023 | ECA | Dermatol Ther | Fase 2 aleatorizada, doble ciego y controlada con placebo de risankizumab en dermatitis atópica moderada-grave |
| [40856907](https://pubmed.ncbi.nlm.nih.gov/40856907/) | 2025 | Revisión sistemática | Am J Clin Dermatol | Manejo de la psoriasis eritrodérmica con terapias sistémicas |
| [40794374](https://pubmed.ncbi.nlm.nih.gov/40794374/) | 2025 | Revisión sistemática | Inflammopharmacology | Efectos terapéuticos y paradójicos de los inhibidores de interleucinas en el liquen plano |
| [41822639](https://pubmed.ncbi.nlm.nih.gov/41822639/) | 2026 | Revisión sistemática | Cureus | Resultados cardiovasculares de los biológicos en enfermedades dermatológicas inflamatorias |
| [39201826](https://pubmed.ncbi.nlm.nih.gov/39201826/) | 2024 | Revisión | Children (Basel) | Biológicos y moléculas pequeñas en alopecia areata, psoriasis, dermatitis atópica e hidradenitis pediátricas |
| [31098898](https://pubmed.ncbi.nlm.nih.gov/31098898/) | 2019 | Revisión | Drugs | Primera aprobación global de risankizumab (Japón, 2019) en psoriasis y variantes |
| [33078990](https://pubmed.ncbi.nlm.nih.gov/33078990/) | 2020 | Revisión | Expert Opin Biol Ther | Biológicos actuales y emergentes en dermatitis atópica pediátrica |
| [39668419](https://pubmed.ncbi.nlm.nih.gov/39668419/) | 2025 | Cohorte | Int J Dermatol | Efectividad y seguridad de dupilumab combinado con risankizumab en dermatitis atópica y psoriasis concomitantes |
| [41645692](https://pubmed.ncbi.nlm.nih.gov/41645692/) | 2026 | Reporte de caso | Dermatol Rep | Upadacitinib para el eccema paradójico inducido por inhibidores de IL-23 |
| [33185530](https://pubmed.ncbi.nlm.nih.gov/33185530/) | 2020 | Reporte de caso | Eur J Dermatol | Erupción eccematosa en pacientes con psoriasis durante el tratamiento con risankizumab |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191361005 | SKYRIZI 360 MG solución inyectable en cartucho | Solución inyectable en cartucho | No disponible en los datos |
| 1191361001 | SKYRIZI 75 MG solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No disponible en los datos |
| 1191361004 | SKYRIZI 600 MG concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos |
| 1191361002 | SKYRIZI 150 mg solución inyectable en pluma precargada | Solución inyectable en pluma precargada | No disponible en los datos |
| 1191361007 | SKYRIZI 180 MG solución inyectable en cartucho | Solución inyectable en cartucho | No disponible en los datos |

Se muestran 5 de las 6 autorizaciones vigentes (todas de Abbvie Deutschland GmbH & Co. KG).

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 78 interacciones. Entre las principales:
  - **Mayor**: adalimumab, baricitinib, certolizumab pegol, cladribina.
  - **Moderada**: roflumilast, tacrolimus, azatioprina, ciclosporina, alefacept, alemtuzumab, anakinra, canakinumab, denosumab, y algunas vacunas (toxoide tetánico, ántrax, cólera de cepa viva).
  - **Menor**: sales de zinc (sulfato, acetato, gluconato, cloruro).
  
  En general se trata de riesgo aditivo de inmunosupresión; las vacunas de microorganismos vivos requieren especial atención.
- Reportes de la literatura describen eccema paradójico durante el tratamiento con inhibidores de IL-23, incluido risankizumab (incidencia estimada del 1-3% en pacientes con psoriasis tratados con biológicos).

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El único ensayo controlado de Fase 2 en dermatitis atópica no demostró eficacia frente a placebo y el fundamento mecanístico es débil (enfermedad dominada por Th2). El alto puntaje de TxGNN parece reflejar la vecindad con la psoriasis más que evidencia propia.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción y de las advertencias y contraindicaciones del prospecto de la AEMPS.
- Análisis completo del ensayo NCT03706040 y de sus subgrupos, para evaluar si algún fenotipo se beneficia.
- Estudios específicos en fenotipos de solapamiento psoriasis/eccema, si se quiere explorar ese nicho.
- Evaluación del riesgo de eccema paradójico y de las interacciones con otros inmunosupresores.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


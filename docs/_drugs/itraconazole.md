---
layout: default
title: Itraconazole
parent: Evidencia moderada (L3-L4)
nav_order: 437
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Itraconazole: nueva indicación predicha, Pneumocistosis (nivel de evidencia L4). Indicación original: Candidiasis esofágica, candidemia, histoplasmosis, aspergilosis…"
monitor_inn: "Itraconazole"
predicted_indications: ["pneumocystosis"]
---

# Itraconazole
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

# Itraconazol: De Candidiasis Esofágica y Otras Micosis a Pneumocistosis

## Resumen en Una Frase

Itraconazol es un antifúngico azólico utilizado originalmente para tratar micosis como la candidiasis esofágica, la aspergilosis, la histoplasmosis y la blastomicosis, entre otras.
El modelo TxGNN predice que podría ser efectivo para **pneumocistosis**, pero sin ensayos clínicos registrados y con **20 publicaciones** de apoyo indirecto (sobre todo revisiones y series de casos).
La evidencia actual se basa en la predicción del modelo y no hay estudios que demuestren eficacia directa.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Candidiasis esofágica, candidemia, histoplasmosis, aspergilosis, blastomicosis, entre otras (el texto de indicación de las autorizaciones españolas no está disponible; se tomó de las indicaciones del grafo de conocimiento) |
| Nueva Indicación Predicha | Pneumocistosis |
| Puntaje de Predicción TxGNN | 99.34% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 13 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Itraconazol inhibe la lanosterol 14-alfa-desmetilasa fúngica (CYP51), bloqueando la síntesis de ergosterol, un componente esencial de la membrana de los hongos. Es la base de su eficacia en micosis como la aspergilosis, la histoplasmosis y las candidiasis.

Sin embargo, *Pneumocystis jirovecii* difiere de la mayoría de los hongos patógenos: su membrana contiene colesterol en lugar de ergosterol como esterol dominante, por lo que el mecanismo clásico de los azoles probablemente tenga actividad limitada. El puntaje elevado del modelo (0.993) probablemente refleja la cercanía en la red de conocimiento con otras infecciones fúngicas y contextos de infección oportunista, y no un mecanismo validado frente a *Pneumocystis*.

La buena penetración pulmonar del itraconazol (PMID 21973267) es solo un dato farmacocinético y no demuestra eficacia. El tratamiento de referencia para profilaxis y tratamiento de la pneumocistosis es trimetoprima-sulfametoxazol, con alternativas como atovacuona, pentamidina y dapsona.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Se muestran las publicaciones más relevantes. Ninguna evalúa directamente itraconazol en pneumocistosis; en su mayoría son revisiones o series de casos sobre infecciones oportunistas.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | Ensayo de Fase III aleatorizado, doble ciego, controlado con placebo | HIV Medicine | Itraconazol en cápsulas como profilaxis de infecciones fúngicas profundas en pacientes con VIH inmunodeprimidos (no específico de *Pneumocystis*) |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Revisión | Clinical Pharmacokinetics | Penetración de antiinfecciosos, incluidos antifúngicos, en el líquido de revestimiento epitelial pulmonar |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Revisión | BMJ Clinical Evidence | Profilaxis primaria y secundaria de infecciones oportunistas en VIH |
| [15250025](https://pubmed.ncbi.nlm.nih.gov/15250025/) | 2004 | Revisión | Clinical Infectious Diseases | Profilaxis antimicrobiana en neutropenia febril; trimetoprima-sulfametoxazol es muy eficaz frente a *Pneumocystis* |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Revisión | Drugs | Tratamiento y profilaxis de infecciones sistémicas por protozoos, incluido *Pneumocystis carinii* |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Revisión | Seminars in Respiratory Infections | Infecciones tras el trasplante de pulmón |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Revisión | Current Clinical Topics in Infectious Diseases | Profilaxis y tratamiento de infecciones en receptores de trasplante de médula ósea |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohorte | Transplantation Proceedings | Infecciones fúngicas invasivas tras trasplante renal en un centro |
| [2233233](https://pubmed.ncbi.nlm.nih.gov/2233233/) | 1990 | Serie de casos | Medicine | Histoplasmosis diseminada en el SIDA: hallazgos clínicos, diagnóstico y tratamiento |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Reporte de caso y revisión | Frontiers in Immunology | Coinfección por *Talaromyces marneffei* y *Pneumocystis jirovecii* en un niño con mutación de STAT1 |

## Información de Mercado en España

Indicación aprobada: el texto de indicación no está disponible en los datos compilados para este rereporte.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59343 | SPORANOX 100 mg CÁPSULAS (Janssen Cilag) | Cápsula dura | No disponible |
| 71234 | ITRACONAZOL NORMON 100 mg CÁPSULAS DURAS EFG | Cápsula dura | No disponible |
| 65762 | ITRACONAZOL ALTER 100 mg CÁPSULAS DURAS EFG | Cápsula dura | No disponible |
| 78446 | ITRACONAZOL ALTAN 10 mg/ml concentrado y disolvente para solución para perfusión EFG | Concentrado para solución para perfusión | No disponible |
| 59371 | CANADIOL 100 mg CÁPSULAS (Esteve) | Cápsula dura | No disponible |

En total hay 13 autorizaciones vigentes (todas de medicamentos con un único principio activo); aquí se muestran 5. Existe una presentación intravenosa (perfusión), además de las cápsulas.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): síndrome de QT largo (incluida la forma familiar) y torsades de pointes; insuficiencia cardíaca congestiva, miocardiopatías y cardiopatía isquémica o coronaria; enfermedad hepática y daño hepático inducido por fármacos; enfermedad renal e insuficiencia renal; enfermedad pulmonar obstructiva crónica; neuropatía periférica; hipopotasemia (déficit de potasio); pérdida de audición y trastornos visuales.
- **Interacciones farmacológicas** (100 registradas; se muestran las principales):
  - **Mayor**: loperamida, triamcinolona, budesonida.
  - **Moderada**: famotidina, ranitidina, cimetidina, rabeprazol, omeprazol (los fármacos que reducen la acidez gástrica pueden disminuir la absorción de las cápsulas), hidrocortisona, dexametasona, betametasona, alosetrón, aprepitant.
  - **Menor**: metformina, pioglitazona, clorpropamida, anfotericina B.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L4/L5 en la práctica): no hay ensayos clínicos y la literatura es indirecta. Además, el mecanismo antifúngico clásico es poco plausible porque *Pneumocystis* carece de ergosterol como esterol principal, y ya existen tratamientos de referencia eficaces.

**Para avanzar se necesita:**
- Datos de mecanismo de acción (MOA) de DrugBank y análisis de la plausibilidad frente a *Pneumocystis*.
- Estudios preclínicos in vitro o in vivo de actividad de itraconazol frente a *Pneumocystis*.
- Advertencias y contraindicaciones oficiales del prospecto de la AEMPS.
- Análisis de compatibilidad de vías de administración y comparación con trimetoprima-sulfametoxazol, atovacuona, pentamidina y dapsona.
- Evaluación del riesgo cardíaco (QT) y de las interacciones en la población inmunodeprimida.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


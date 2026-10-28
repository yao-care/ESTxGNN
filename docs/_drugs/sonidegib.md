---
layout: default
title: Sonidegib
parent: Solo predicción del modelo (L5)
nav_order: 743
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Sonidegib: nueva indicación predicha, Meduloblastoma con nodularidad extensa (nivel de evidencia L2). Indicación original: Carcinoma cutáneo / carcinoma basocelular"
monitor_inn: "SONIDEGIB"
predicted_indications: ["medulloblastoma with extensive nodularity", "xeroderma pigmentosum", "annular epidermolytic ichthyosis", "epidermolysis bullosa simplex with mottled pigmentation", "trichothiodystrophy photosensitive", "cutaneous adenocystic carcinoma", "benign neoplasm of sweat gland", "eccrine carcinoma", "obsolete cataract, microcephaly, failure to thrive, kyphoscoliosis syndrome"]
---

# Sonidegib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Sonidegib: De Carcinoma Cutáneo a Meduloblastoma con nodularidad extensa
{: .text-alpha }

## Resumen en Una Frase

Sonidegib es un inhibidor oral de la proteína Smoothened (SMO) de la vía Hedgehog, originalmente utilizado para el tratamiento del carcinoma basocelular y otros carcinomas cutáneos.
El modelo TxGNN predice que podría ser efectivo para **cáncer de piel**, con **6 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.
Cabe señalar que esta predicción se solapa en gran medida con la indicación ya aprobada, por lo que es más una ampliación a una categoría adyacente que un uso verdaderamente nuevo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma cutáneo / carcinoma basocelular (según las indicaciones originales registradas en el grafo de conocimiento; el texto de indicación de la autorización no está disponible) |
| Nueva Indicación Predicha | Cáncer de piel |
| Puntaje de Predicción TxGNN | 0.9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según la información conocida, sonidegib es un antagonista del receptor Smoothened (SMO), una molécula similar a un receptor acoplado a proteína G esencial para la señalización de las proteínas Hedgehog. Su eficacia en carcinoma basocelular avanzado ha sido comprobada, y mecanísticamente es aplicable al cáncer de piel dependiente de Hedgehog.

El carcinoma basocelular (CBC) está impulsado por la activación aberrante de la vía Hedgehog (mutaciones en PTCH1/SMO), que sonidegib inhibe. La indicación predicha, "cáncer de piel", engloba al CBC, por lo que se solapa con el uso ya aprobado (CBC localmente avanzado). Se trata, por tanto, de una categoría más amplia o adyacente y no de un uso completamente nuevo.

Conviene tener presente que otros tumores cutáneos no dependientes de Hedgehog (por ejemplo, carcinoma espinocelular o melanoma) no tendrían el mismo sustento mecanístico. La utilidad real de la predicción se limita, en la práctica, a los tumores cutáneos con activación de la vía Hedgehog.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01327053](https://clinicaltrials.gov/study/NCT01327053) | Fase 2 | Completado | 230 | Ensayo aleatorizado y doble ciego de dos dosis de LDE225 (sonidegib) en CBC localmente avanzado o metastásico; evidencia directa de eficacia y seguridad |
| [NCT03534947](https://clinicaltrials.gov/study/NCT03534947) | Fase 2 | Completado | 16 | Piloto de sonidegib neoadyuvante de corta duración seguido de cirugía o imiquimod en CBC de localizaciones cosméticamente difíciles |
| [NCT05463757](https://clinicaltrials.gov/study/NCT05463757) | N/A | Reclutando | 80 | Registro prospectivo de vismodegib y sonidegib en CBC avanzado o múltiple en los Países Bajos; datos de práctica real |
| [NCT04007744](https://clinicaltrials.gov/study/NCT04007744) | Fase 1 | Activo, sin reclutar | 36 | Sonidegib más pembrolizumab en tumores sólidos avanzados; información de seguridad de la combinación, no específica de piel |
| [NCT02303041](https://clinicaltrials.gov/study/NCT02303041) | Fase 2 | Terminado | 10 | Piloto de sonidegib más buparlisib en CBC avanzado; terminado con solo 10 pacientes, evidencia mínima |
| [NCT01757327](https://clinicaltrials.gov/study/NCT01757327) | Fase 2 | Retirado | 0 | Ensayo controlado con placebo en cáncer de mama; retirado sin inscripción, no aporta datos |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37604067](https://pubmed.ncbi.nlm.nih.gov/37604067/) | 2023 | Guía | Eur J Cancer | Actualización 2023 de la guía europea de consenso para el diagnóstico y tratamiento del CBC, con clasificación en CBC "fácil" y "difícil de tratar" |
| [31288208](https://pubmed.ncbi.nlm.nih.gov/31288208/) | 2019 | Guía | Eur J Cancer | Guía europea interdisciplinaria previa para el diagnóstico y tratamiento del CBC |
| [32759706](https://pubmed.ncbi.nlm.nih.gov/32759706/) | 2020 | Revisión | Int J Mol Sci | Revisión integral del CBC: características histológicas y moleculares, y mecanismos de resistencia a tratamientos sistémicos |
| [26919418](https://pubmed.ncbi.nlm.nih.gov/26919418/) | 2016 | Revisión | Cell | Inhibición de la vía Hedgehog; vismodegib y sonidegib son inhibidores de SMO aprobados en CBC localmente avanzado |
| [39062023](https://pubmed.ncbi.nlm.nih.gov/39062023/) | 2024 | Revisión | Biomedicines | Epidemiología, factores de riesgo y opciones de tratamiento del cáncer de piel no melanoma avanzado y metastásico |
| [36844955](https://pubmed.ncbi.nlm.nih.gov/36844955/) | 2022 | Revisión | Front Med | Estrategias clásicas y nuevas en melanoma avanzado y cáncer de piel no melanoma |
| [26833519](https://pubmed.ncbi.nlm.nih.gov/26833519/) | 2016 | Revisión | Clin Med (Lond) | Panorama del cáncer de piel no melanoma (CBC y carcinoma espinocelular) |
| [33888008](https://pubmed.ncbi.nlm.nih.gov/33888008/) | 2021 | Opinión de expertos | Expert Opin Drug Saf | Opinión de expertos sobre eficacia, seguridad y tolerabilidad de sonidegib |
| [33194718](https://pubmed.ncbi.nlm.nih.gov/33194718/) | 2020 | Revisión | Front Oncol | Sonidegib en el tratamiento del CBC avanzado |
| [26323341](https://pubmed.ncbi.nlm.nih.gov/26323341/) | 2015 | Revisión | Drugs | Primera aprobación global de sonidegib (Odomzo), antagonista oral de SMO |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1151030002 | ODOMZO 200 MG CÁPSULAS DURAS | Cápsula dura | Texto de indicación no disponible en los datos compilados |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de SMO de la vía Hedgehog) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Según la evaluación de los ensayos: creatina quinasa (CK) por toxicidad musculoesquelética; además de funciones hepática y renal según el prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto; considerar además el riesgo de toxicidad embriofetal |

---

## Consideraciones de Seguridad

- **Toxicidad musculoesquelética:** vigilar la elevación de CK.
- **Teratogenicidad:** riesgo de toxicidad embriofetal.
- **Interacciones farmacológicas:** se identificaron 100 interacciones en la base consultada; la lista muestra las principales:
  - **Mayores:** aprepitant, dexametasona, claritromicina, clotrimazol, cobicistat. Es relevante el manejo de inhibidores e inductores de CYP3A.
  - **Moderadas:** cimetidina, metreleptina, miconazol, troglitazona, deferasirox.
  - **Menores:** famotidina, ranitidina, rabeprazol, dexlansoprazol, omeprazol, lansoprazol, nizatidina, pantoprazol, esomeprazol.

Para advertencias y contraindicaciones detalladas, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo aleatorizado de Fase 2 completado (NCT01327053) que respalda la eficacia y seguridad de sonidegib en CBC, y la indicación predicha se solapa ampliamente con el uso ya aprobado. Se recomienda avanzar con salvaguardas, dado que no se trata de un uso verdaderamente nuevo y existen riesgos relevantes de seguridad.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada), actualmente no disponible.
- Datos detallados del mecanismo de acción (MOA).
- Definir con precisión qué subtipos de cáncer de piel (distintos del CBC) dependen de Hedgehog, para delimitar la población objetivo.
- Plan de monitoreo de CK y toxicidad musculoesquelética, anticoncepción y prevención de toxicidad embriofetal.
- Revisión del manejo de interacciones con inhibidores e inductores de CYP3A.

---

### Nota sobre otras indicaciones predichas

Entre las demás predicciones, la **xerodermia pigmentosa** (L4, solo un reporte de caso de 2026 sobre múltiples CBC en un paciente con esta enfermedad, con beneficio indirecto sobre los tumores) merece seguimiento como pregunta de investigación. El **meduloblastoma con nodularidad extensa** es mecanísticamente plausible (vía SHH/SMO) pero carece de ensayos y literatura, y exigiría abordar la toxicidad sobre las placas de crecimiento en pacientes pediátricos; se mantiene en Hold. El resto de las predicciones (L5) carece de evidencia y de fundamento mecanístico claro.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


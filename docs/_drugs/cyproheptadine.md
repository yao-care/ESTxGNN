---
layout: default
title: Cyproheptadine
parent: Evidencia moderada (L3-L4)
nav_order: 213
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-14
description: "Cyproheptadine: nueva indicación predicha, Urticaria alérgica (nivel de evidencia L4). Indicación original: Rinitis alérgica (según las indicaciones originales del grafo de cono…"
monitor_inn: "cyproheptadine"
predicted_indications: ["allergic urticaria", "cold urticaria", "nasal cavity disease", "acute laryngopharyngitis"]
---

# Cyproheptadine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **4** 
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

# Ciproheptadina: De Rinitis Alérgica a Urticaria Alérgica

## Resumen en Una Frase

La ciproheptadina es un antihistamínico de primera generación, utilizado originalmente en cuadros alérgicos como la rinitis alérgica, la urticaria y el angioedema.
El modelo TxGNN predice que podría ser efectiva para **urticaria alérgica**, aunque esta indicación ya figura entre las originales y, por tanto, es más una extensión que un reposicionamiento real.
No hay **ningún ensayo clínico registrado**; la evidencia se limita a **9 publicaciones**, en su mayoría informes clínicos antiguos (1961-1976).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Rinitis alérgica (según las indicaciones originales del grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Espana | ✓ Comercializado |
| Numero de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la ciproheptadina es un antihistamínico H1 de primera generación con actividad antagonista sobre los receptores de serotonina (5-HT2) y efectos anticolinérgicos.

La urticaria y el angioedema ya forman parte de las indicaciones originales del fármaco, por lo que la urticaria alérgica es esencialmente una extensión de un uso establecido y no un reposicionamiento genuino. El bloqueo de histamina y serotonina sobre la respuesta de habón y eritema mediada por mastocitos es mecanísticamente plausible y coherente.

Cabe señalar que la literatura de respaldo es mayoritariamente de las décadas de 1960 y 1970, con baja calidad o evidencia indirecta, y sin ensayos registrados.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7488341](https://pubmed.ncbi.nlm.nih.gov/7488341/) | 1995 | Estudio comparativo doble ciego cruzado | Asian Pac J Allergy Immunol | Ciproheptadina vs. ketotifeno en 6 niños tailandeses con urticaria por frío |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Revisión | Drugs | Revisión de acrivastina (no específica de ciproheptadina) en rinitis alérgica y urticaria |
| [812662](https://pubmed.ncbi.nlm.nih.gov/812662/) | 1976 | Evaluación clínica comparativa | Curr Ther Res | Eficacia relativa de ciproheptadina e hidroxizina en el prurito de dermatosis alérgicas |
| [1305812](https://pubmed.ncbi.nlm.nih.gov/1305812/) | 1992 | Observacional/diagnóstico | Asian Pac J Allergy Immunol | Prueba del cubito de hielo en niños; tras 4 semanas de ciproheptadina solo 17 % seguía positivo a los 3 min |
| [4382319](https://pubmed.ncbi.nlm.nih.gov/4382319/) | 1967 | Informe clínico/revisión | Med Lett Drugs Ther | Ciproheptadina en dermatosis alérgicas y pruriginosas |
| [13685954](https://pubmed.ncbi.nlm.nih.gov/13685954/) | 1961 | Informe clínico | Br Med J | Ciproheptadina en el tratamiento de la urticaria |
| [14347187](https://pubmed.ncbi.nlm.nih.gov/14347187/) | 1965 | Informe clínico | Rev Lyon Med | Combinación de ciproheptadina y dexametasona en dermatosis inflamatorias y alérgicas |
| [14106555](https://pubmed.ncbi.nlm.nih.gov/14106555/) | 1964 | Evaluación clínica | J Assoc Physicians India | Evaluación clínica de ciproheptadina en dermatosis alérgicas |
| [14138414](https://pubmed.ncbi.nlm.nih.gov/14138414/) | 1964 | Informe clínico | Arerugi | Efecto terapéutico de inhibidores de serotonina en enfermedades alérgicas infantiles |

### Otras indicaciones predichas

- **Urticaria por frío** (TxGNN 99.76 %, nivel L3): existen estudios comparativos pequeños y antiguos, incluidos estudios doble ciego (p. ej., [PMID 334082](https://pubmed.ncbi.nlm.nih.gov/334082/), [PMID 6480953](https://pubmed.ncbi.nlm.nih.gov/6480953/), [PMID 2901993](https://pubmed.ncbi.nlm.nih.gov/2901993/)) frente a clorfeniramina, placebo, doxepina, hidroxizina y acrivastina. No hay ensayos registrados. Las guías actuales prefieren antihistamínicos H1 de segunda generación no sedantes, por lo que la cuestión principal es su beneficio relativo frente a la sedación y la carga anticolinérgica. Es la candidata con mejor respaldo de las cuatro predichas.
- **Enfermedad de la cavidad nasal** (TxGNN 99.21 %, nivel L5): término amplio e inespecífico; probablemente refleja los usos ya existentes en rinitis. Sin ensayos ni literatura.
- **Laringofaringitis aguda** (TxGNN 99.13 %, nivel L5): probablemente refleja el solapamiento con las indicaciones de faringitis y resfriado común, con beneficio solo sintomático. Sin ensayos ni literatura.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 35622 | PERIACTIN 4 MG COMPRIMIDOS | Comprimido | No disponible en los datos compilados |
| 49107 | TONICO JUVENTUS 1 MG/ML + 250 MCG/ML SUSPENSIÓN EXTEMPORÁNEA | Polvo para suspensión oral | No disponible en los datos compilados |
| 53715 | DYNAMOGÉN 3 MG/1 G/10ML SOLUCIÓN ORAL | Solución oral | No disponible en los datos compilados |
| 48622 | COVITASA CÁPSULAS | Cápsula dura | No disponible en los datos compilados |
| 47944 | PRANZO 62,5 / 1,25 / 0,5 mg/ml SOLUCIÓN ORAL | Solución oral | No disponible en los datos compilados |

Hay una sexta autorización vigente: DESARROL 50 MG/ML + 25 MG/ML + 0,2 MG/ML SOLUCIÓN ORAL (n.º 50242, solución oral, Faes Farma). Todas son autorizaciones vigentes de producto único (ninguna cancelada).

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto)**: hipertensión arterial, úlcera péptica, hiperplasia prostática benigna, hipertensión ocular, glaucoma de ángulo cerrado, hipertiroidismo (enfermedad de Graves, tirotoxicosis) y obstrucción del cuello vesical. Estas coinciden con el perfil anticolinérgico del fármaco.
- **Interacciones Farmacológicas**: se identificaron 308 interacciones. Las de nivel **mayor** son con **cloruro de potasio** y **citrato de potasio**. Entre las de nivel moderado figuran fármacos anticolinérgicos (atropina, hiosciamina, escopolamina, glicopirronio, diciclomina, trospio, propantelina), opioides (morfina, opio, loperamida), cannabinoides (dronabinol, nabilona), eluxadolina, metoclopramida y fenfluramina.

No se dispone de las advertencias ni contraindicaciones del prospecto; se recomienda consultar el prospecto oficial.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La urticaria alérgica ya está cubierta por las indicaciones originales, la evidencia es de nivel L4 y proviene casi toda de informes clínicos de los años 60-70, sin ensayos registrados. El valor añadido como reposicionamiento es limitado. De las predicciones secundarias, la urticaria por frío es la más sólida (L3), pero queda por justificar su beneficio frente a los antihistamínicos de segunda generación.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), una laguna bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Obtener los textos de indicación aprobados de las autorizaciones españolas.
- Evaluar de forma prioritaria la urticaria por frío mediante revisión sistemática o ensayo comparativo frente a antihistamínicos de segunda generación, ponderando sedación y carga anticolinérgica.
- Definir un plan de seguridad para poblaciones con las condiciones contraindicadas y para la coadministración con sales de potasio y anticolinérgicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


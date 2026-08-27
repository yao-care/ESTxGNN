---
layout: default
title: Cabazitaxel
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
---

# Cabazitaxel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Cabazitaxel: De Cáncer de Próstata Resistente a la Castración a Cáncer de Mama

## Resumen en Una Frase

Cabazitaxel es un taxano de segunda generación cuya evidencia clínica disponible en este paquete lo sitúa históricamente en el tratamiento del **cáncer de próstata metastásico resistente a la castración** (combinado con prednisona, tras progresión a docetaxel). El modelo TxGNN predice que podría ser efectivo para **Cáncer de Mama**, con un puntaje del **99.92%**. Actualmente no hay ensayos clínicos catalogados de forma estructurada para este par fármaco-indicación, pero existen **20 publicaciones**, incluyendo un **ensayo clínico aleatorizado de Fase II completado** (GENEVIEVE) y un estudio de Fase I/II con combinación de capecitabina en cáncer de mama metastásico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de próstata metastásico resistente a la castración (mCRPC), según contexto derivado de la literatura del paquete |
| Nueva Indicación Predicha | Cáncer de Mama (carcinoma de mama femenino) |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos estructurados de mecanismo de acción (MOA) en la base de datos (dato bloqueante pendiente de DrugBank). Sin embargo, según la información contextual disponible, cabazitaxel es un taxano de segunda generación cuyo mecanismo es equivalente al de docetaxel y paclitaxel: se une a la β-tubulina, estabiliza los microtúbulos y bloquea la mitosis, induciendo apoptosis en células de rápida proliferación. A diferencia de los taxanos clásicos, cabazitaxel es menos sensible al eflujo mediado por la glicoproteína P (P-gp), lo que en teoría le confiere actividad frente a células tumorales con resistencia previa a taxanos.

El cáncer de mama es una de las indicaciones estándar de la clase de los taxanos (paclitaxel, docetaxel), por lo que la extensión mecanística a esta neoplasia es razonable. De hecho, esta hipótesis ya cuenta con respaldo clínico real: el estudio GENEVIEVE (Fase II, aleatorizado) comparó cabazitaxel frente a paclitaxel semanal como tratamiento neoadyuvante en cáncer de mama triple negativo o luminal B/HER2-negativo operable, y el estudio de Villanueva et al. evaluó cabazitaxel combinado con capecitabina en cáncer de mama metastásico previamente tratado con antraciclinas y taxanos. Esto sugiere que la predicción de TxGNN no es puramente especulativa, sino que coincide con una línea de investigación clínica ya explorada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en el campo estructurado de ensayos clínicos del paquete de evidencia. La evidencia de ensayos clínicos disponible se encuentra referenciada dentro de la literatura (ver tabla siguiente).

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | ECA (Fase II) | European Journal of Cancer | Estudio GENEVIEVE: comparó tasa de respuesta patológica completa de cabazitaxel vs. paclitaxel semanal como neoadyuvancia en cáncer de mama HER2-negativo (triple negativo o luminal B) operable |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Fase I/II | European Journal of Cancer | Estudio de escalada de dosis de cabazitaxel + capecitabina en cáncer de mama metastásico progresado tras antraciclina y taxano; evaluó dosis máxima tolerada, seguridad y actividad |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | Preclínico | Journal for ImmunoTherapy of Cancer | Cabazitaxel mejora la inmunoterapia dirigida a CD47 en cáncer de mama triple negativo al modular macrófagos asociados al tumor |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Revisión | Molecular Cancer Therapeutics | Mecanismos de resistencia a cabazitaxel usando modelos celulares de cáncer de mama (MCF-7); menor resistencia cruzada que paclitaxel/docetaxel en variantes multirresistentes |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | Preclínico | Journal of Controlled Release | Nanopartículas de cabazitaxel mejoran la eficacia en un modelo de xenoinjerto derivado de paciente (PDX) de cáncer de mama basal, con remisión completa en 6 de 8 tumores |
| [28504249](https://pubmed.ncbi.nlm.nih.gov/28504249/) | 2017 | Preclínico | Acta Pharmacologica Sinica | Micelas poliméricas cargadas con cabazitaxel evaluadas frente a metástasis de cáncer de mama in vitro e in vivo |
| [36918084](https://pubmed.ncbi.nlm.nih.gov/36918084/) | 2023 | Preclínico | Journal of Controlled Release | Nanomedicina redox-sensible con cabazitaxel conjugado y dasatinib para modular la interacción tumor-estroma en cáncer de mama |
| [34309357](https://pubmed.ncbi.nlm.nih.gov/34309357/) | 2021 | Preclínico | Bioconjugate Chemistry | Entrega dirigida de cabazitaxel mediante péptido cíclico penetrante en modelos de cáncer de mama y próstata |
| [33360926](https://pubmed.ncbi.nlm.nih.gov/33360926/) | 2021 | Preclínico | Colloids and Surfaces B: Biointerfaces | Diseño y evaluación de nanopartículas lipídicas (NLC) cargadas con cabazitaxel frente a líneas celulares de cáncer de mama |
| [30521787](https://pubmed.ncbi.nlm.nih.gov/30521787/) | 2019 | Preclínico | Chemistry and Physics of Lipids | Liposferas coencapsuladas de cabazitaxel y timoquinona como combinación sinérgica para cáncer de mama |

---

## Citotoxicidad

Cabazitaxel es un agente antineoplásico citotóxico (taxano de segunda generación).

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (clase taxano, inhibidor de microtúbulos) |
| Riesgo de Mielosupresión | Alto — la literatura del paquete describe la neutropenia como una de las toxicidades más frecuentes de cabazitaxel, de forma consistente con la clase de los taxanos |
| Clasificación de Emetogenicidad | No especificada en los datos disponibles — consultar el prospecto |
| Items de Monitoreo | Hemograma completo con diferencial (por riesgo de neutropenia), función hepática y renal |
| Protección en Manejo | Requiere manejo conforme a normativas de fármacos citotóxicos/peligrosos, al tratarse de un agente antineoplásico parenteral |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No hay datos de advertencias, contraindicaciones ni interacciones farmacológicas disponibles en el paquete de evidencia actual (esta es una brecha de datos de severidad *Blocking*, ver Próximos Pasos).

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo clínico aleatorizado de Fase II completado (GENEVIEVE) y un estudio de Fase I/II con evidencia clínica real de cabazitaxel en cáncer de mama, respaldados por una base mecanística sólida (clase taxano) y múltiples estudios preclínicos convergentes. Sin embargo, la ausencia total de datos de seguridad (ficha técnica/prospecto) impide avanzar sin salvaguardas.

**Para avanzar se necesita:**
- Ficha técnica/prospecto de TFDA con advertencias y contraindicaciones (brecha bloqueante, DG001)
- Datos estructurados de mecanismo de acción vía DrugBank (DG002)
- Datos de interacciones farmacológicas (DDI), actualmente no encontrados
- Confirmación formal del estado regulatorio original y posible vía de autorización en España, dado que el fármaco no está actualmente comercializado
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


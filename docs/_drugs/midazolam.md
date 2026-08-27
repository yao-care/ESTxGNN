---
layout: default
title: Midazolam
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 1
---

# Midazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Midazolam: De Sedación/Anestesia a Insomnio

## Resumen en Una Frase

Midazolam es una benzodiazepina de acción corta ampliamente utilizada para sedación en procedimientos y anestesia. El modelo TxGNN predice que podría ser efectivo para **Insomnio**, con **10 ensayos clínicos** y **7 publicaciones** que actualmente respaldan esta dirección — incluyendo estudios históricos que ya evaluaron midazolam como hipnótico en los años 80-90.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sedación / Anestesia (uso general conocido de la clase benzodiazepina; no hay ficha técnica estructurada disponible en este pack) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) de midazolam en este Evidence Pack. Según la información regulatoria disponible, midazolam es una benzodiazepina cuya eficacia como sedante en procedimientos y en anestesia está ampliamente establecida, y mecanísticamente podría ser aplicable al tratamiento del insomnio.

Esta predicción no es una extrapolación puramente novedosa: la propia revisión de literatura de este pack muestra ensayos clínicos históricos de los años 80-90 (PMID 6138072, 2121802, 6120704) que ya evaluaron midazolam específicamente como hipnótico para el insomnio y trastornos del sueño, reportando eficacia comparable a los hipnóticos de referencia de esa época. Esto sugiere que TxGNN está recuperando un uso clínico previamente documentado pero hoy poco explotado, más que proponiendo una aplicación enteramente inédita.

Pese a esta evidencia histórica, el estado actual de midazolam en España es "No comercializado" (0 autorizaciones), y faltan datos críticos de seguridad (contraindicaciones, advertencias de ficha técnica AEMPS/TFDA) — una brecha de severidad Blocking que debe resolverse antes de iniciar cualquier evaluación de seguridad.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00744380](https://clinicaltrials.gov/study/NCT00744380) | No aplica | Completado | 23 | Comparación doble-ciego de midazolam vs dexmedetomidina para facilitar la extubación en pacientes de UCI médica/quirúrgica bajo sedación benzodiazepínica |
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Fase 4 | Completado | 111 | Compara la calidad del sueño postoperatorio entre dexmedetomidina y midazolam combinados con anestesia espinal en resección transuretral de próstata (RTUP) |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | No aplica | Terminado | 5 | Compara calidad/cantidad de sueño (polisomnografía 24h) entre dexmedetomidina y midazolam en pacientes de UCI con ventilación mecánica, e incidencia de delirium |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Fase 1 | Terminado | 6 | Compara hallazgos polisomnográficos en pacientes ventilados mecánicamente sedados con agonistas α2 (dexmedetomidina) vs agonistas GABA (midazolam), evaluando etapas de sueño y tiempo total de sueño |
| [NCT04082767](https://clinicaltrials.gov/study/NCT04082767) | Fase 3 | Desconocido | 120 | Ensayo pediátrico que compara la eficacia sedante de dexmedetomidina vs midazolam en niños críticamente enfermos con ventilación mecánica |
| [NCT07336095](https://clinicaltrials.gov/study/NCT07336095) | Fase 3 | Aún no reclutando | 195 | Compara melatonina oral vs midazolam oral como premedicación en niños sometidos a amigdalectomía, evaluando efecto inductor del sueño de la melatonina frente a las limitaciones conocidas del midazolam |
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | No aplica | Reclutando | 280 | Ensayo doble-ciego controlado con placebo que evalúa midazolam oral preoperatorio en pacientes con alteraciones del sueño/ansiedad sometidos a cirugía colorrectal laparoscópica |
| [NCT06480500](https://clinicaltrials.gov/study/NCT06480500) | Fase 2 | Reclutando | 110 | Ensayo con midazolam como comparador activo, evaluando terapia cognitivo-conductual por internet combinada con ketamina IV para suicidalidad en depresión resistente al tratamiento |
| [NCT05466279](https://clinicaltrials.gov/study/NCT05466279) | No aplica | Completado | 131 | Ensayo aleatorizado y controlado que compara anestesia general con remazolam vs propofol+midazolam |
| [NCT06498869](https://clinicaltrials.gov/study/NCT06498869) | No aplica | Completado | 178 | Estudio aleatorizado doble-ciego que evalúa el efecto de ketamina sobre la calidad del sueño (índice de Pittsburgh) en pacientes sometidos a colonoscopia bajo sedación con midazolam |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | ECA | British Journal of Clinical Pharmacology | Midazolam 15 mg vs Vesparax en insomnio secundario a enfermedad neuromuscular; ambos eficaces, midazolam mejor tolerado y sin efecto resaca |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | ECA | Journal of Clinical Psychopharmacology | Estudio multicéntrico aleatorizado doble-ciego que compara flurazepam y midazolam durante 14 días en insomnes crónicos, evaluando sueño, rendimiento y niveles plasmáticos |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | ECA (resumen ejecutivo) | Journal of Clinical Psychopharmacology | Resumen ejecutivo del mismo estudio multicéntrico de 14 días con flurazepam y midazolam en insomnio crónico |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | Estudio piloto (dosis-respuesta) | Arzneimittel-Forschung | Estudio piloto multicéntrico en 75 pacientes con insomnio leve-moderado que establece el rango de dosis óptimo de midazolam oral (10-30 mg) |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Revisión | Orvosi Hetilap | Revisión sobre insomnio y su relación con hipoperfusión cerebral; discute clasificación primaria/secundaria del insomnio |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Revisión | Acta Psychiatrica Scandinavica Suppl. | Revisión sobre el uso clínico de hipnóticos y la necesidad de variedad de benzodiazepinas según su perfil farmacocinético |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | Estudio piloto | Journal of Clinical Medicine | Evalúa si lemborexant (frente a benzodiazepinas tradicionales como midazolam) puede prevenir delirium en pacientes de alto riesgo sometidos a sedación profunda endoscópica |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque existe evidencia histórica sólida (ECAs doble-ciego) sobre la eficacia de midazolam como hipnótico para el insomnio y el score de predicción TxGNN es muy alto (99.74%), un data gap de severidad **Blocking** en el prospecto/advertencias de TFDA impide iniciar la evaluación de seguridad (S1). Además, midazolam no está actualmente comercializado en España (0 autorizaciones).

**Para avanzar se necesita:**
- Obtener y analizar el prospecto (ficha técnica) con advertencias, contraindicaciones e interacciones (DG001, Blocking)
- Confirmar el mecanismo de acción detallado vía DrugBank (DG002)
- Evaluar la vía de registro/comercialización en España dado el estado "No comercializado"
- Completar la clasificación de relevancia de los ensayos clínicos y literatura, actualmente marcados como "pending"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


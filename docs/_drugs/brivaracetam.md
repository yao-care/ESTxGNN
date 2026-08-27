---
layout: default
title: Brivaracetam
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
---

# Brivaracetam
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

# Brivaracetam: De Epilepsia Focal a Epilepsia Visual

## Resumen en Una Frase

Brivaracetam es un antiepiléptico ligando de alta afinidad de la proteína SV2A, actualmente utilizado como tratamiento adyuvante y en monoterapia para crisis de inicio focal. El modelo TxGNN predice que podría ser efectivo para **Epilepsia Visual** (crisis inducidas por estímulos visuales/fotosensibilidad), pero **no hay ensayos clínicos específicos** para este subtipo — la evidencia actual proviene de **19 publicaciones** centradas en epilepsia focal general, sin estudios diseñados para la variante visual.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Epilepsia de inicio focal (crisis focales), en terapia adyuvante y monoterapia |
| Nueva Indicación Predicha | Epilepsia visual (crisis inducidas por estímulos visuales) |
| Puntaje de Predicción TxGNN | 99.51% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Research Question (etapa S1) |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha técnica. Según la información conocida en la literatura, brivaracetam es un ligando de alta afinidad de la proteína de vesícula sináptica 2A (SV2A), análogo estructural de levetiracetam con 15-30 veces mayor afinidad y selectividad por esta diana. Está aprobado como tratamiento adyuvante y en monoterapia para crisis de inicio focal.

La epilepsia visual (fotosensible) es una variante refleja dentro del espectro de las epilepsias focales/generalizadas idiopáticas, en la que estímulos visuales desencadenan hiperexcitabilidad cortical. Mecanísticamente, la inhibición amplia de la liberación de neurotransmisores mediada por SV2A podría, en teoría, reducir esta hiperexcitabilidad y suprimir crisis reflejas de este tipo.

Sin embargo, ningún ensayo clínico ha sido diseñado específicamente para esta subpoblación: toda la evidencia disponible proviene de estudios en epilepsia focal general, por lo que la aplicabilidad al subtipo visual es una extrapolación mecanística, no una demostración clínica directa.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38576178](https://pubmed.ncbi.nlm.nih.gov/38576178/) | 2024 | ECA | Epilepsia Open | Ensayo fase III doble ciego, controlado con placebo, en pacientes asiáticos con crisis focales no controladas; evalúa eficacia, seguridad y tolerabilidad del brivaracetam adyuvante |
| [37483441](https://pubmed.ncbi.nlm.nih.gov/37483441/) | 2023 | Revisión Sistemática/Metaanálisis | Frontiers in Neurology | Revisión sistemática y metaanálisis de seguridad y eficacia del brivaracetam en epilepsia infantil |
| [31033711](https://pubmed.ncbi.nlm.nih.gov/31033711/) | 2019 | Revisión (incluye ECA fase 3) | JAAPA | Compara brivaracetam con levetiracetam y ofrece pautas de uso seguro y eficaz |
| [38811492](https://pubmed.ncbi.nlm.nih.gov/38811492/) | 2024 | Revisión narrativa | Advances in Therapy | Revisión del perfil preclínico y beneficios clínicos del brivaracetam como ligando SV2A de alta afinidad |
| [40568060](https://pubmed.ncbi.nlm.nih.gov/40568060/) | 2025 | Revisión | Journal of Epilepsy Research | Síntesis de datos de ensayos clínicos y de vida real sobre eficacia, seguridad y tolerabilidad |
| [31195850](https://pubmed.ncbi.nlm.nih.gov/31195850/) | 2019 | Revisión | Expert Review of Neurotherapeutics | Revisión de eficacia y seguridad en epilepsia focal; análogo de levetiracetam con mayor afinidad SV2A |
| [38117319](https://pubmed.ncbi.nlm.nih.gov/38117319/) | 2024 | No clasificado | Intensive Care Medicine | Revisión clínica del manejo del estado epiléptico en UCI, con mención de antiepilépticos de acción rápida |
| [37684052](https://pubmed.ncbi.nlm.nih.gov/37684052/) | 2023 | No clasificado | BMJ | Revisión sobre manejo de la epilepsia en embarazo y lactancia, con perfiles de seguridad comparados |
| [32120063](https://pubmed.ncbi.nlm.nih.gov/32120063/) | 2020 | No clasificado | Neuropharmacology | Revisión de mecanismos de acción de los antiepilépticos actuales, incluyendo ligandos SV2A |
| [36218253](https://pubmed.ncbi.nlm.nih.gov/36218253/) | 2022 | No clasificado | Revista de Neurología | Revisión sobre estado epiléptico pediátrico y su manejo terapéutico |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Research Question (etapa S1)**

**Justificación:**
La predicción para epilepsia visual alcanza un nivel de evidencia L3: existen publicaciones relevantes sobre brivaracetam en epilepsia, pero ninguna diseñada específicamente para el subtipo visual/fotosensible, y no hay ensayos clínicos dedicados. A esto se suma que el fármaco no está comercializado en España (0 autorizaciones) y que falta el prospecto/ficha técnica de TFDA, un vacío de datos de severidad *Blocking* que impide una evaluación de seguridad inicial (S1).

**Para avanzar se necesita:**
- Ficha técnica/prospecto con advertencias y contraindicaciones (actualmente bloqueante para evaluación de seguridad)
- Datos formales del mecanismo de acción (MOA)
- Un ensayo o estudio de mecanismo diseñado específicamente para epilepsia visual/fotosensible, en lugar de extrapolación desde epilepsia focal general
- Evaluar la vía regulatoria en España dado que el fármaco aún no está comercializado
- Considerar en paralelo la indicación "status epilepticus" (rank 2 en el mismo Evidence Pack), que cuenta con evidencia sustancialmente más sólida (L2, ensayo comparativo completado de brivaracetam IV vs. levetiracetam, n=152) y podría representar una vía de reposicionamiento más avanzada
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


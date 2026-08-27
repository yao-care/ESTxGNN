---
layout: default
title: Risankizumab
parent: 僅模型預測 (L5)
nav_order: 245
evidence_level: L5
indication_count: 10
---

# Risankizumab
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

# Risankizumab: De Psoriasis a Dermatitis Atópica

## Resumen en Una Frase

Risankizumab es un anticuerpo monoclonal IgG humanizado dirigido contra la subunidad p19 de IL-23, aprobado originalmente para el tratamiento de la psoriasis (psoriasis vulgar, artritis psoriásica, psoriasis pustulosa generalizada y psoriasis eritrodérmica). El modelo TxGNN predice que también podría ser efectivo para **Dermatitis (Dermatitis Atópica)**, con **7 ensayos clínicos** y **17 publicaciones** que actualmente respaldan esta dirección, si bien la evidencia disponible es todavía limitada y requiere lectura cuidadosa (ver más abajo).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Psoriasis (psoriasis vulgar, artritis psoriásica, psoriasis pustulosa generalizada, psoriasis eritrodérmica) — según aprobación global reportada en literatura; sin licencias registradas en España |
| Nueva Indicación Predicha | Dermatitis (Dermatitis Atópica) |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Según la literatura disponible en este paquete de evidencia (PMID 31098898), risankizumab es un anticuerpo monoclonal IgG humanizado que bloquea selectivamente la subunidad p19 de IL-23. El dato estructurado de mecanismo de acción (MOA) en la base de origen aún no está disponible (ver brecha DG002, pendiente de consulta directa a DrugBank), pero esta descripción funcional consta en la evidencia bibliográfica recopilada.

La psoriasis (indicación original) y la dermatitis atópica (nueva indicación predicha) son ambas dermatosis inflamatorias inmunomediadas. Según PMID 36588137, la dermatitis atópica es una enfermedad heterogénea con participación de las vías Th2, Th22 y potencialmente Th17, lo que respalda mecanísticamente el bloqueo de IL-23/IL-22 como estrategia terapéutica — esto da sustento biológico directo a la predicción de TxGNN, más allá de la mera cercanía de nodos en el grafo de conocimiento.

Sin embargo, es importante señalar una advertencia relevante: una parte considerable de la literatura recuperada (7 de los 17 artículos) describe casos de **eczema o dermatitis paradójica inducida por el propio risankizumab** en pacientes tratados por psoriasis (p. ej. PMID 37014149, 36939506, 41645692, 33185530). Esta es evidencia en la dirección opuesta — el fármaco como causa, no como tratamiento, de dermatitis — y debe diferenciarse claramente de la evidencia terapéutica real (el ensayo Fase 2 en dermatitis atópica) al evaluar esta oportunidad de reposicionamiento.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT07021495](https://clinicaltrials.gov/study/NCT07021495) | N/A | Reclutando | 840 | Estudio observacional de perfil de biomarcadores en 6 enfermedades cutáneas inflamatorias inmunomediadas, incluyendo dermatitis atópica, dentro de la iniciativa NGID |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A | Completado | 1000 | Estudio retrospectivo sobre supervivencia a 10 años de terapias biológicas en psoriasis cutánea (indicación original, no dermatitis) |
| [NCT05969223](https://clinicaltrials.gov/study/NCT05969223) | Fase 4 | Completado | 214 | Risankizumab en psoriasis genital o del cuero cabelludo moderada-grave (indicación original) |
| [NCT04908475](https://clinicaltrials.gov/study/NCT04908475) | Fase 4 | Completado | 352 | Risankizumab vs. apremilast en psoriasis en placas moderada (indicación original) |
| [NCT04818385](https://clinicaltrials.gov/study/NCT04818385) | N/A | Completado | 240 | Cohorte observacional en Taiwán sobre durabilidad de respuesta (PASI90) en psoriasis (indicación original) |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Fase 4 | Aún no reclutando | 10 | Microdispositivo cutáneo para ensayar fármacos aprobados, incluida dermatitis atópica y psoriasis |
| [NCT03706040](https://clinicaltrials.gov/study/NCT03706040) | Fase 2 | Completado | 172 | **Único ensayo específico en dermatitis atópica**: seguridad y eficacia de risankizumab en adultos y adolescentes con dermatitis atópica moderada-grave |

Nota: la mayoría de estos ensayos evalúan psoriasis (indicación ya establecida); solo NCT03706040 aborda directamente la nueva indicación predicha.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36588137](https://pubmed.ncbi.nlm.nih.gov/36588137/) | 2023 | ECA | Dermatology and Therapy | Ensayo Fase 2 aleatorizado, doble ciego, controlado con placebo, de risankizumab en dermatitis atópica moderada-grave; sustenta bloqueo de IL-23/IL-22 dado el rol de Th2/Th22/Th17 |
| [40856907](https://pubmed.ncbi.nlm.nih.gov/40856907/) | 2025 | Revisión Sistemática | American Journal of Clinical Dermatology | Manejo de psoriasis eritrodérmica con terapias sistémicas |
| [41822639](https://pubmed.ncbi.nlm.nih.gov/41822639/) | 2026 | Revisión Sistemática | Cureus | Resultados cardiovasculares asociados a terapia biológica en dermatosis inflamatorias |
| [39201826](https://pubmed.ncbi.nlm.nih.gov/39201826/) | 2024 | Revisión | Children (Basel) | Revisión narrativa de biológicos y moléculas pequeñas en alopecia areata, psoriasis, dermatitis atópica y hidradenitis supurativa pediátricas |
| [33078990](https://pubmed.ncbi.nlm.nih.gov/33078990/) | 2020 | Revisión | Expert Opinion on Biological Therapy | Biológicos actuales y emergentes para dermatitis atópica pediátrica |
| [31098898](https://pubmed.ncbi.nlm.nih.gov/31098898/) | 2019 | Revisión | Drugs | Perfil de primera aprobación global de risankizumab; describe MOA (anti-IL-23 p19) e indicaciones aprobadas |
| [40071317](https://pubmed.ncbi.nlm.nih.gov/40071317/) | 2025 | Observacional | Experimental Dermatology | Estudio longitudinal retrospectivo de experiencia clínica en psoriasis eritrodérmica |
| [38607726](https://pubmed.ncbi.nlm.nih.gov/38607726/) | 2024 | Revisión | Military Medicine | Reevaluación de inmunomoduladores sistémicos para psoriasis y eczema en contexto militar |
| [40794374](https://pubmed.ncbi.nlm.nih.gov/40794374/) | 2025 | Revisión Sistemática | Inflammopharmacology | Rol de inhibidores de interleucinas en liquen plano: efectos terapéuticos y paradójicos |
| [37381703](https://pubmed.ncbi.nlm.nih.gov/37381703/) | 2023 | Reporte de Caso | Journal of Dermatological Treatment | Acrodermatitis continua de Hallopeau tratada exitosamente con risankizumab |

Advertencia: fuera de este top 10, otros 7 artículos recuperados (PMID 39668419, 37014149, 33368238, 36939506, 41645692, 33185530, 33185535) describen casos de eczema o reacciones paradójicas **inducidas** por risankizumab, no su uso terapéutico en dermatitis — relevante para la sección de seguridad.

---

## Información de Mercado en España

Risankizumab no está comercializado en España (0 autorizaciones registradas; estado: No comercializado).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad — actualmente no hay datos estructurados de advertencias, contraindicaciones ni interacciones farmacológicas disponibles en este paquete (la obtención del prospecto de la agencia reguladora está pendiente, ver brecha DG001, de severidad bloqueante).

Como hallazgo adicional relevante de la literatura: varios reportes de caso documentan eczema o dermatitis paradójica como **efecto adverso** de risankizumab en pacientes tratados por psoriasis (PMID 37014149, 36939506, 41645692, 33185530). Esto debe considerarse explícitamente al evaluar la nueva indicación, ya que introduce una tensión mecanística que la evidencia terapéutica (ensayo Fase 2) no resuelve por sí sola.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La brecha de datos sobre advertencias/contraindicaciones del prospecto (DG001) es de severidad bloqueante y impide una evaluación de seguridad inicial (S1). A esto se suma que el fármaco no está comercializado en España, que la evidencia específica para dermatitis atópica se limita a un único ensayo Fase 2 completado (sin confirmación en Fase 3), y que existe una señal de literatura contradictoria (eczema paradójico inducido por el propio fármaco) que debe aclararse antes de avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica (TFDA o equivalente europeo) para completar la evaluación de seguridad (DG001)
- Confirmar el mecanismo de acción mediante consulta directa a DrugBank (DG002)
- Un ensayo Fase 3 confirmatorio específico en dermatitis atópica
- Diferenciar claramente, mediante revisión clínica dirigida, los casos de eczema terapéutico vs. eczema/dermatitis paradójica inducida por el fármaco
- Evaluar la viabilidad regulatoria y de mercado en España, dado que actualmente no hay autorizaciones registradas
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


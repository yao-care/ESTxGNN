---
layout: default
title: Brodalumab
parent: 僅模型預測 (L5)
nav_order: 46
evidence_level: L5
indication_count: 10
---

# Brodalumab
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

# Brodalumab: De Psoriasis en Placas a Estrongiloidiasis (señal de riesgo, no de eficacia)

## Resumen en Una Frase

Brodalumab es un anticuerpo monoclonal anti-IL-17RA utilizado originalmente para la psoriasis en placas moderada a grave. El modelo TxGNN predice con muy alta puntuación (**99.84%**) una asociación con **estrongiloidiasis**, pero el propio análisis mecanístico indica que esta asociación refleja un riesgo de reactivación de la infección bajo bloqueo de IL-17, no un beneficio terapéutico — es decir, una señal de reposicionamiento invertida. Ninguna de las 10 indicaciones predichas cuenta con evidencia clínica sólida; la mejor alternativa ("enfermedad ocular") solo alcanza nivel L4 con evidencia indirecta y de baja relevancia.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Psoriasis en placas moderada a grave (dato general conocido del fármaco; no está presente en el Evidence Pack) |
| Nueva Indicación Predicha | Estrongiloidiasis (rank 1) — señal mecanísticamente invertida, ver advertencia abajo |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L5 (solo predicción del modelo, sin ensayos ni literatura) |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Brodalumab es un anticuerpo monoclonal completamente humano dirigido contra el receptor A de IL-17 (IL-17RA), que bloquea la señalización de IL-17A, IL-17F e IL-17E (IL-25). Este mecanismo es la base de su eficacia conocida en enfermedades inflamatorias mediadas por la vía Th17, como la psoriasis en placas.

Sin embargo, la predicción de mayor puntuación (estrongiloidiasis) **no representa una oportunidad terapéutica**: el eje IL-17 es una vía central de la inmunidad antihelmíntica del huésped, y clínicamente los inhibidores de IL-17 —incluido brodalumab— se asocian a mayor riesgo de reactivación o empeoramiento de infecciones por *Strongyloides stercoralis*. De hecho, las recomendaciones de uso de esta clase de fármacos incluyen el cribado y tratamiento de estrongiloidiasis latente antes de iniciar tratamiento. El modelo probablemente detectó la fuerte relación biológica entre IL-17 y la inmunidad antiparasitaria, pero interpretó la dirección de forma opuesta a la realidad clínica (asociación de riesgo, no de beneficio). Esta predicción debe tratarse como una **alerta de seguridad**, no como candidato de reposicionamiento.

Entre el resto de las predicciones, la única con algo de evidencia asociada es "enfermedad ocular" (rank 2, L4), respaldada por un ensayo observacional de baja relevancia y una revisión general sobre el bloqueo de IL-17 en enfermedades reumáticas sistémicas — ninguno aporta evidencia directa de eficacia en una indicación oftalmológica concreta. Las demás predicciones (deficiencia vitamínica, anomalía de von Hippel, y el clúster de neuropatías ópticas/epiescleritis) carecen de cualquier ensayo clínico o publicación de respaldo, y sus vínculos mecanísticos son puramente especulativos.

---

## Evidencia de Ensayos Clínicos (rank 1 — Estrongiloidiasis)

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura (rank 1 — Estrongiloidiasis)

Actualmente no hay literatura relacionada disponible.

### Evidencia Adicional — Enfermedad Ocular (rank 2, referencia)

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT07021495](https://clinicaltrials.gov/study/NCT07021495) | N/A | Reclutando | 840 | Estudio observacional multicéntrico de biomarcadores en 6 enfermedades cutáneas inflamatorias inmunomediadas (incluye psoriasis); no evalúa brodalumab en enfermedad ocular — relevancia baja (grado C) |

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32993066](https://pubmed.ncbi.nlm.nih.gov/32993066/) | 2020 | Revisión | Int J Mol Sci | Revisión sobre el bloqueo de IL-17 en enfermedades reumáticas sistémicas; no es específica de ninguna indicación oftalmológica |

---

## Consideraciones de Seguridad

Los campos estructurados de seguridad (advertencias, contraindicaciones, interacciones) están todos marcados como no disponibles en este Evidence Pack. Consultar el prospecto para información de seguridad completa.

**Nota relevante detectada durante el análisis:** aunque no forma parte del bloque de seguridad estructurado, el propio análisis mecanístico de la predicción rank 1 señala que los inhibidores de IL-17 (clase de brodalumab) se asocian a riesgo de reactivación/empeoramiento de estrongiloidiasis. El cribado de esta parasitosis antes de iniciar tratamiento es una consideración de seguridad conocida para esta clase farmacológica.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La predicción de mayor puntuación (estrongiloidiasis) es una falsa señal de dirección mecanística invertida (riesgo, no beneficio) y debe descartarse como candidato de reposicionamiento.
- Ninguna de las 10 indicaciones predichas alcanza un nivel de evidencia superior a L4, y esa única ("enfermedad ocular") se apoya en evidencia indirecta y de baja relevancia.
- Existen brechas de datos bloqueantes (advertencias/contraindicaciones TFDA, severidad *Blocking*) que impiden avanzar a la fase de evaluación de seguridad S1.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica oficial (TFDA/AEMPS) con advertencias y contraindicaciones (brecha bloqueante).
- Confirmar el mecanismo de acción formal y las indicaciones originales aprobadas vía DrugBank.
- Si se desea explorar la vía IL-17 en enfermedad ocular, definir una indicación oftalmológica específica (p. ej. uveítis asociada a espondiloartropatía) en lugar de la etiqueta genérica "eye disease", y buscar evidencia clínica dirigida.
- Implementar protocolo de cribado de estrongiloidiasis como consideración de seguridad de clase, independientemente de cualquier uso de reposicionamiento.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


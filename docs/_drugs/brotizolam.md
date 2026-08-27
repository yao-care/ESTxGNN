---
layout: default
title: Brotizolam
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 6
---

# Brotizolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Brotizolam: Sin Comercialización Registrada en España → Insomnio (Uso Internacional Ya Establecido)

## Resumen en Una Frase

Brotizolam (DrugBank DB09017) es una benzodiazepina (tienotriazolodiazepina) que actualmente **no está comercializada en España** (0 autorizaciones registradas) y de la que no se dispone de datos de indicación original en el paquete de evidencia. El modelo TxGNN predice como indicación de mayor puntuación el **Insomnio**, con un puntaje del **99.94%**, respaldado por **3 ensayos clínicos** (incluyendo un Fase 3 completado) y **3 publicaciones**. Cabe destacar que esta no es una hipótesis de reposicionamiento novedosa: el propio nombre comercial internacional del fármaco (Lendormin) ya se usa como hipnótico para el insomnio en otros países, por lo que el caso de uso real es la **introducción al mercado español**, no el descubrimiento de un nuevo mecanismo terapéutico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el paquete de evidencia (sin autorización en España); uso internacional ya conocido: insomnio (nombre comercial Lendormin) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

No se dispone de datos estructurados de mecanismo de acción (original_moa: Data Gap) en el paquete de evidencia. Sin embargo, la propia justificación mecanística recogida en la evidencia indica que brotizolam es una tienotriazolodiazepina, clase perteneciente a las benzodiazepinas, que actúa como **modulador alostérico positivo del receptor GABA-A**. Este es el mecanismo estándar y ya establecido por el cual las benzodiazepinas producen su efecto hipnótico — no se trata de una hipótesis novedosa de reposicionamiento, sino de la aplicación farmacológica central y ya conocida del fármaco.

En consecuencia, la relación entre "indicación original" y "nueva indicación predicha" en este caso particular es prácticamente circular: brotizolam ya se comercializa internacionalmente (marca Lendormin) como hipnótico de acción corta para el insomnio. Lo que realmente representa esta evaluación no es un descubrimiento mecanístico nuevo, sino la valoración de si existe suficiente evidencia clínica para justificar la **entrada de este fármaco, ya validado en otros mercados, al mercado español**, donde actualmente no cuenta con ninguna autorización.

Por este motivo, la predicción de TxGNN debe interpretarse como una **confirmación de validez del modelo** (recupera correctamente el uso clínico real y conocido del fármaco) más que como un hallazgo de reposicionamiento en sentido estricto. Las demás indicaciones predichas por el modelo (retirada alcohólica, categorías de "abuso de sustancias", ansiedad) presentan niveles de evidencia mucho más bajos (L3-L5) y en varios casos reflejan señales de riesgo de abuso/dependencia del propio fármaco más que oportunidades terapéuticas genuinas.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00347295](https://clinicaltrials.gov/study/NCT00347295) | Fase 3 | Completado | 253 | Ensayo aleatorizado, doble ciego, doble simulación, multicéntrico: eficacia y seguridad de brotizolam (Lendormin) frente a estazolam en pacientes ambulatorios con insomnio |
| [NCT02224014](https://clinicaltrials.gov/study/NCT02224014) | N/A | Completado | 485 | Estudio de resultados de uso de Lendormin D en condiciones de práctica clínica normal, evaluando seguridad y eficacia en pacientes con insomnio |
| [NCT02776228](https://clinicaltrials.gov/study/NCT02776228) | Fase 3 | Desconocido | 200 | Prevalencia de insomnio tras cirugía cardíaca y resultado del tratamiento con benzodiazepinas en este contexto (población específica post-quirúrgica) |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [8992838](https://pubmed.ncbi.nlm.nih.gov/8992838/) | 1996 | Estudio clínico | Zhurnal nevrologii i psikhiatrii imeni S.S. Korsakova | Brotizolam (0.25 mg antes de dormir, 10 días) mejoró significativamente la estructura del sueño en 25 pacientes con insomnio neurótico, facilitando el inicio del sueño |
| [26171909](https://pubmed.ncbi.nlm.nih.gov/26171909/) | 2015 | Revisión sistemática (Cochrane) | Cochrane Database of Systematic Reviews | Revisión sobre efectos de opioides, hipnóticos y sedantes (incluyendo benzodiazepinas) sobre la respiración alterada durante el sueño en adultos con apnea obstructiva |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Revisión | Acta Psychiatrica Scandinavica Supplementum | Revisión sobre el uso clínico de hipnóticos, clasificación del insomnio y necesidad de variedad de agentes hipnóticos según perfil farmacocinético |

---

## Información de Mercado en España

Brotizolam **no dispone actualmente de ninguna autorización de comercialización en España** (0 licencias registradas en el paquete de evidencia). No es posible presentar una tabla de productos autorizados por ausencia de datos.

---

## Consideraciones de Seguridad

No se dispone de información de seguridad estructurada en el paquete de evidencia (advertencias, contraindicaciones e interacciones farmacológicas no encontradas). Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo Fase 3 completado, aleatorizado y doble ciego (N=253) más un estudio observacional post-comercialización de gran tamaño (N=485) que respaldan directamente el uso de brotizolam en insomnio, un uso ya establecido internacionalmente bajo la marca Lendormin. Sin embargo, la ausencia total de datos de seguridad (advertencias, contraindicaciones, MOA formal) y la falta de cualquier presencia regulatoria en España son barreras que deben resolverse (Data Gap DG001, severidad "Blocking") antes de avanzar a evaluación de seguridad (S1).

**Para avanzar se necesita:**
- Obtención del prospecto/ficha técnica (TFDA/AEMPS o equivalente) con advertencias y contraindicaciones
- Datos de mecanismo de acción (MOA) formalizados desde DrugBank u otra fuente regulatoria
- Evaluación de vía regulatoria para introducción al mercado español (nueva solicitud de autorización)
- Dado que se trata de una benzodiazepina, plan de gestión de riesgo de dependencia/abuso, considerando que el propio modelo señaló indicaciones relacionadas con abuso de sustancias (rank 3-5) como posibles señales de seguridad del fármaco mismo
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Regorafenib
parent: 僅模型預測 (L5)
nav_order: 239
evidence_level: L5
indication_count: 8
---

# Regorafenib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

Usando la Evidence Pack proporcionada, genero el informe de evaluación para Regorafenib (DB08896), centrado en la indicación predicha con mayor solidez de evidencia (rank 1: Liposarcoma, único candidato con nivel de evidencia L2 y ensayos clínicos dedicados).

---

# Regorafenib: De Cáncer Colorrectal Metastásico a Liposarcoma

## Resumen en Una Frase

Regorafenib es un inhibidor multiquinasa oral, utilizado originalmente en el tratamiento del cáncer colorrectal metastásico, el tumor del estroma gastrointestinal (GIST) y el carcinoma hepatocelular (indicaciones descritas en la literatura incluida en este informe).
El modelo TxGNN predice que podría ser efectivo para **Liposarcoma**, con **2 ensayos clínicos de Fase 2 completados** y **9 publicaciones** que actualmente respaldan esta dirección — si bien, como se detalla más adelante, los resultados clínicos específicos en liposarcoma han sido mixtos y en parte negativos.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer colorrectal metastásico, GIST y carcinoma hepatocelular (según literatura incluida; sin registro de autorización en España en esta consulta) |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99,76% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción exacto de regorafenib procedentes de DrugBank. Según la información disponible en la evidencia recopilada, regorafenib es un inhibidor multiquinasa oral que actúa sobre receptores angiogénicos (VEGFR1-3, TIE2), receptores del estroma tumoral (PDGFR-β, FGFR) y quinasas oncogénicas (KIT, RET, RAF). Su eficacia en cáncer colorrectal metastásico, GIST y carcinoma hepatocelular ya está establecida clínicamente.

El liposarcoma, especialmente en sus subtipos desdiferenciado y mixoide, es un tumor de partes blandas con alta dependencia de la angiogénesis, lo que ofrece una base mecanística plausible para un fármaco antiangiogénico como regorafenib. De hecho, regorafenib ha sido evaluado sistemáticamente en sarcomas de partes blandas dentro del mismo programa de ensayos (REGOSARC, SARC024), que incluyó específicamente cohortes de liposarcoma junto con otros subtipos ya validados (leiomiosarcoma, sarcoma sinovial).

Sin embargo, es importante señalar una matización relevante: los dos ensayos de Fase 2 disponibles (REGOSARC y SARC024) mostraron actividad clara en sarcomas no adipocíticos, pero **no lograron demostrar beneficio consistente específicamente en la cohorte de liposarcoma**. Esto no invalida la hipótesis mecanística, pero sí indica que la traducción clínica en este subtipo tumoral concreto no está confirmada y requiere guardarraíles (guardrails) antes de avanzar.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01900743](https://clinicaltrials.gov/study/NCT01900743) | Fase 2 | Completado | 219 | REGOSARC: ensayo aleatorizado, doble ciego, controlado con placebo en sarcoma de partes blandas metastásico tras fracaso de antraciclinas; incluyó cohorte específica de liposarcoma (Cohorte A) junto con leiomiosarcoma, sarcoma sinovial y otros subtipos. |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Fase 2 | Completado | 131 | SARC024: protocolo tipo "cesta" que evaluó regorafenib oral en subtipos seleccionados de sarcoma, incluyendo liposarcoma, osteosarcoma y sarcoma de Ewing/Ewing-like. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | ECA | The Lancet. Oncology | Publicación principal de REGOSARC: eficacia y seguridad de regorafenib en sarcoma de partes blandas avanzado tras antraciclina. |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | ECA | European Journal of Cancer | Análisis actualizado de REGOSARC post-cruce: eficacia demostrada en leiomiosarcoma, sarcoma sinovial y otros sarcomas no adipocíticos, **pero no en liposarcoma**. |
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | ECA | The Oncologist | Cohorte de liposarcoma de SARC024 (regorafenib vs. placebo): los resultados **no respaldan el uso rutinario de regorafenib** en esta población. |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Protocolo de ensayo | BMC Cancer | Protocolo del estudio REGOSARC: justificación del bloqueo de la angiogénesis en la biología del sarcoma. |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | Análisis secundario (Q-TWiST) | Cancer | Análisis de calidad de vida ajustada por tiempo (Q-TWiST) de REGOSARC: beneficio clínico integrado favorable a regorafenib en sarcoma no adipocítico. |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Revisión | Targeted Oncology | Papel creciente de regorafenib en el tratamiento del sarcoma, resume evidencia de Fase 2/3 en distintos subtipos incluyendo liposarcoma. |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Revisión | Critical Reviews in Oncology/Hematology | Revisión sobre terapia de mantenimiento tras primera línea en sarcoma de partes blandas avanzado. |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | Estudio retrospectivo (comparador) | Anti-Cancer Drugs | Estudio de anlotinib en liposarcoma WDLS/DDLS; menciona regorafenib como TKI ya aprobado en sarcoma no adipocítico. |
| [26266019](https://pubmed.ncbi.nlm.nih.gov/26266019/) | 2015 | Reporte de caso (fármaco distinto, pazopanib) | Rare Tumors | Caso de respuesta a pazopanib en sarcoma de Ewing extraóseo; citado como justificación para incluir un brazo de sarcoma de Ewing en SARC024. |

---

## Información de Mercado en España

Regorafenib no cuenta actualmente con ninguna autorización de comercialización registrada en la consulta de la AEMPS (0 autorizaciones, estado: no comercializado). No es posible, por tanto, presentar una tabla de presentaciones ni de indicaciones aprobadas localmente.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida — inhibidor multiquinasa oral (VEGFR1-3, TIE2, PDGFR-β, FGFR, KIT, RET, RAF) |
| Riesgo de Mielosupresión | Bajo-moderado; los inhibidores multiquinasa orales suelen causar menor mielosupresión que la quimioterapia citotóxica clásica. No hay datos cuantitativos específicos disponibles — consultar el prospecto |
| Clasificación de Emetogenicidad | Baja, perfil típico de los inhibidores de tirosina quinasa orales |
| Items de Monitoreo | Función hepática (hepatotoxicidad descrita en la literatura de la clase), presión arterial (hipertensión asociada a inhibición de VEGFR), piel (síndrome mano-pie), función renal y proteinuria |
| Protección en Manejo | Al ser un antineoplásico oral, se recomiendan precauciones estándar de manejo de citostáticos (uso de guantes por cuidadores, evitar manipulación directa o fraccionamiento de los comprimidos sin indicación específica) |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen dos ensayos clínicos de Fase 2 completados (REGOSARC y SARC024) que evaluaron específicamente regorafenib en liposarcoma, lo que aporta un nivel de evidencia L2 y descarta que se trate de una predicción puramente especulativa. Sin embargo, ambos estudios coinciden en que, a diferencia de otros subtipos de sarcoma de partes blandas donde regorafenib sí mostró beneficio, **los resultados en la cohorte específica de liposarcoma no respaldan su uso rutinario**. Esta discordancia entre la solidez del cuerpo de evidencia y el resultado clínico obtenido justifica un avance cauteloso con guardarraíles claros, en lugar de una recomendación de "Go" directa.

**Para avanzar se necesita:**
- Datos de mecanismo de acción (MOA) verificados directamente en DrugBank/ficha técnica
- Advertencias, contraindicaciones e interacciones farmacológicas (DDI) desde el prospecto oficial de la AEMPS o TFDA
- Análisis por subtipo histológico de liposarcoma (bien diferenciado/desdiferenciado vs. mixoide/pleomórfico), ya que la respuesta podría diferir entre subtipos
- Evaluación de combinaciones (p. ej., con inmunoterapia) que podrían mejorar los resultados negativos observados en monoterapia
- Confirmación del estado real de registro/comercialización en España, dado que la ausencia de autorización podría reflejar una limitación de la fuente de datos consultada más que una ausencia real de aprobación
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


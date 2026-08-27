---
layout: default
title: Vandetanib
parent: 僅模型預測 (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
---

# Vandetanib
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

# Vandetanib: De Carcinoma Medular de Tiroides a Carcinoma de Células Renales

## Resumen en Una Frase

Vandetanib es un inhibidor oral de triple diana (VEGFR2/3, EGFR y RET), utilizado originalmente para el **carcinoma medular de tiroides** (dependiente de RET). El modelo TxGNN predice que podría ser efectivo para **Carcinoma de Células Renales**, con **4 ensayos clínicos** y **6 publicaciones** que actualmente respaldan esta dirección, aunque la mayoría de los ensayos específicos de este tumor son de tamaño reducido o fueron interrumpidos.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma medular de tiroides (según el mecanismo de acción documentado en el paquete de evidencia; no hay indicación oficial registrada en los datos regulatorios de España) |
| Nueva Indicación Predicha | Carcinoma de Células Renales |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Según la información disponible en el paquete de evidencia, vandetanib es un inhibidor de tirosina-quinasa que actúa simultáneamente sobre VEGFR2/3, EGFR y RET. Su indicación original, el carcinoma medular de tiroides, depende de la activación constitutiva de RET, mientras que su actividad anti-VEGFR le confiere un efecto antiangiogénico adicional.

El carcinoma de células renales —especialmente los subtipos asociados a la enfermedad de Von Hippel-Lindau (VHL), HLRCC o deficiencia de SDH— es un tumor caracterizado por una activación intensa del eje HIF-VEGF, el mismo mecanismo que explotan fármacos ya aprobados para este cáncer (sunitinib, pazopanib, axitinib, cabozantinib). Por eso, el bloqueo de VEGFR por vandetanib tiene una base biológica plausible en este contexto, tal como respalda el artículo farmacológico original de ZD6474 (PMID 15886878), que demostró actividad antiangiogénica en un modelo ortotópico de carcinoma renal.

Es importante señalar que **no se dispone de datos oficiales de mecanismo de acción (MOA) ni de ficha técnica de TFDA/AEMPS** en este paquete (brecha de datos DG001 y DG002); la descripción anterior proviene del razonamiento mecanístico incluido en la evidencia de la indicación predicha, no de una fuente regulatoria confirmada.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Fase 2 | Completado | 37 | Vandetanib en pacientes con enfermedad de Von Hippel-Lindau y tumores renales asociados; evalúa si el fármaco puede prevenir la angiogénesis tumoral. |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Fase 1/2 | Interrumpido | 7 | Combinación de vandetanib con metformina en cáncer renal asociado a HLRCC, SDH o carcinoma papilar renal esporádico; estudio detenido por bajo reclutamiento. |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Fase 2 | Completado | 82 | Ensayo aleatorizado de carboplatino + gemcitabina con o sin vandetanib como primera línea en cáncer urotelial avanzado (no específicamente carcinoma de células renales) en pacientes no aptos para cisplatino; único ensayo con diseño controlado y muestra amplia, pero en una población tumoral distinta (vía urinaria, no parénquima renal). |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Fase 2 | Interrumpido | 3 | Vandetanib en carcinoma renal de células claras avanzado; interrumpido por reclutamiento insuficiente, sin conclusiones robustas. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36302175](https://pubmed.ncbi.nlm.nih.gov/36302175/) | 2023 | ECA (otro fármaco) | Clinical Cancer Research | Ensayo de fase 2 de guadecitabina en tumores deficientes en SDH, incluido HLRCC-RCC; contexto de comparación, no evalúa vandetanib directamente. |
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Revisión | Clinical & Experimental Metastasis | Revisión sobre reprogramación metabólica y epigenética en carcinoma renal deficiente en fumarato hidratasa; menciona terapias dirigidas en evaluación. |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Preclínico (modelo murino) | Molecular Cancer Research | Modelo de ratón de carcinoma renal con translocación TFE3/Xp11.2; identifica nuevas dianas terapéuticas. |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Revisión (nintedanib, comparación de clase) | OncoTargets and Therapy | Revisión de agentes antiangiogénicos en tumores sólidos, menciona vandetanib entre los inhibidores multi-diana comparables. |
| [28477875](https://pubmed.ncbi.nlm.nih.gov/28477875/) | 2017 | Revisión (cabozantinib, comparación de clase) | Bulletin du Cancer | Revisión del mecanismo de cabozantinib (VEGFR2/c-MET/RET), útil como comparador de clase para vandetanib. |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Revisión | ASCO Educational Book | Revisión de terapias sistémicas en cáncer de tiroides avanzado; confirma la indicación original de vandetanib como inhibidor de RET aprobado por la FDA. |

---

## Citotoxicidad

Vandetanib es un antineoplásico (terapia dirigida oncológica), por lo que aplica esta sección.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor multiquinasa oral: VEGFR2/3, EGFR, RET) |
| Riesgo de Mielosupresión | No se dispone de datos específicos en este paquete; la literatura de clase disponible describe principalmente toxicidad hepática ([PMID 23981115](https://pubmed.ncbi.nlm.nih.gov/23981115/)) y proteinuria ([PMID 32105149](https://pubmed.ncbi.nlm.nih.gov/32105149/)) más que mielosupresión clásica |
| Clasificación de Emetogenicidad | No especificada en los datos disponibles; consultar el prospecto |
| Items de Monitoreo | Función hepática, función renal y proteinuria, presión arterial, e intervalo QT/ECG (existe una advertencia de seguridad grave para vandetanib en cáncer medular de tiroides, [PMID 23185843](https://pubmed.ncbi.nlm.nih.gov/23185843/), y datos de mortalidad relacionada con el tratamiento en la clase de inhibidores de VEGFR, [PMID 22651902](https://pubmed.ncbi.nlm.nih.gov/22651902/)) |
| Protección en Manejo | Debe seguir las precauciones estándar de manejo de agentes antineoplásicos orales; no hay ficha técnica de TFDA/AEMPS disponible para confirmar medidas específicas (brecha de datos bloqueante, ver Conclusión) |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- Existe una brecha de datos **bloqueante**: no hay ficha técnica/prospecto de TFDA-AEMPS disponible, por lo que no puede completarse ni siquiera la evaluación de seguridad inicial (S1).
- El fármaco no está comercializado en España (0 autorizaciones), por lo que no hay una vía regulatoria inmediata de acceso.
- La evidencia clínica específica para carcinoma de células renales es limitada: de los 4 ensayos identificados, solo uno (NCT01191892) tiene diseño aleatorizado y muestra amplia, pero corresponde a una población de cáncer urotelial, no renal; los ensayos verdaderamente centrados en carcinoma renal (NCT00566995, NCT01372813, NCT02495103) tienen muestras muy pequeñas o fueron interrumpidos.

**Para avanzar se necesita:**
- Ficha técnica/prospecto de TFDA-AEMPS con advertencias, contraindicaciones e interacciones (brecha bloqueante DG001).
- Confirmación oficial del mecanismo de acción desde DrugBank (brecha DG002).
- Verificación del estatus regulatorio real de vandetanib en España (la indicación original documentada, carcinoma medular de tiroides, no aparece registrada en los datos de licencias de este paquete).
- Ensayos clínicos dedicados y de mayor tamaño en carcinoma de células renales (los actuales son pequeños o fueron interrumpidos), idealmente segmentados por subtipo molecular (VHL, HLRCC, SDH, células claras).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


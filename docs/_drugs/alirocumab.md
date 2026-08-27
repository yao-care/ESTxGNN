---
layout: default
title: Alirocumab
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 10
---

# Alirocumab
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

# ALIROCUMAB: De Hipercolesterolemia a Enfermedad del Proceso Catabólico del Colesterol

> **Nota de selección**: TxGNN generó 10 indicaciones candidatas para alirocumab, todas con puntajes muy próximos (~99%) y clasificadas en el extremo profundo del ranking global (posiciones 8583–10213). De esas 10, solo **"cholesterol catabolic process disease"** (rango 5) alcanzó evidencia clínica y bibliográfica real; las otras 9 —incluida la de mayor puntaje, ictiosis ligada al X— no tienen ningún ensayo ni publicación de respaldo y quedan en Hold. Este informe se centra en el único candidato con base evidencial suficiente para una decisión.

## Resumen en Una Frase

Alirocumab es un anticuerpo monoclonal inhibidor de PCSK9, utilizado originalmente para el tratamiento de la hipercolesterolemia y la dislipidemia con el fin de reducir el LDL-colesterol y el riesgo cardiovascular. El modelo TxGNN predice que también podría ser relevante para trastornos del proceso catabólico del colesterol, con **1 ensayo clínico de Fase 3 completado** y **19 publicaciones** que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipercolesterolemia / dislipidemia (reducción de LDL-C y riesgo cardiovascular) |
| Nueva Indicación Predicha | Enfermedad del proceso catabólico del colesterol (*cholesterol catabolic process disease*) |
| Puntaje de Predicción TxGNN | 99.36% |
| Nivel de Evidencia | L2 (1 ECA de Fase 3 completado) |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## Por qué es Razonable esta Predicción?

No hay datos de mecanismo de acción disponibles en DrugBank en este Evidence Pack (bloqueado como DG002), pero la literatura recopilada describe el mecanismo con detalle: alirocumab es un anticuerpo monoclonal humano que se une a la PCSK9 circulante, impidiendo que esta se una al receptor de LDL (LDLR) en la superficie del hepatocito. Al bloquear la degradación del LDLR mediada por PCSK9, aumenta la densidad de receptores disponibles para captar LDL-C circulante, acelerando su aclaramiento.

La indicación original (hipercolesterolemia/dislipidemia) y la nueva indicación predicha (trastornos del catabolismo del colesterol) comparten el mismo eje fisiopatológico: ambas giran en torno a la incapacidad del organismo para depurar o metabolizar adecuadamente el colesterol circulante. De hecho, uno de los estudios recuperados (PMID 38191052) muestra que la inhibición de PCSK9 activa la vía PPARα-CYP7A1 —la enzima clave que convierte el colesterol en ácidos biliares para su eliminación—, lo que conecta mecanísticamente el fármaco con el catabolismo del colesterol, más allá de su efecto ya conocido sobre el LDLR.

Esto contrasta con las otras 9 indicaciones predichas por TxGNN (ictiosis ligada al X, defectos de esteroidogénesis, displasia diafisaria, enfermedades neurodegenerativas, etc.), para las cuales el propio modelo no encuentra ningún respaldo clínico o bibliográfico y el vínculo mecanístico es, en el mejor de los casos, especulativo.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03207945](https://clinicaltrials.gov/study/NCT03207945) | Fase 3 | Completado | 118 | Evalúa el efecto de la inhibición de PCSK9 sobre el riesgo cardiovascular en pacientes con VIH tratado; la aterosclerosis en este contexto cursa con mayor inflamación vascular, disfunción endotelial y predominio de placa no calcificada, marcadores relacionados con el metabolismo/depuración del colesterol. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39913634](https://pubmed.ncbi.nlm.nih.gov/39913634/) | 2025 | ECA (post-hoc) | Diabetes Care | Análisis post-hoc de ODYSSEY OUTCOMES: la reducción de Lp(a) y LDL-C con alirocumab no se asocia a mayor riesgo de diabetes de nuevo diagnóstico. |
| [38658193](https://pubmed.ncbi.nlm.nih.gov/38658193/) | 2024 | Revisión/Observacional | Eur Heart J Cardiovasc Pharmacother | Más de 47.000 paciente-años de ODYSSEY OUTCOMES: alirocumab reduce eventos isquémicos recurrentes y mortalidad por todas las causas, con reducción sostenida de LDL-C. |
| [29526502](https://pubmed.ncbi.nlm.nih.gov/29526502/) | 2018 | Estudio clínico | Kidney International | Eficacia y seguridad de alirocumab para reducir LDL-C en pacientes con hipercolesterolemia e insuficiencia renal (eGFR 30-59), comparado con función renal normal. |
| [38191052](https://pubmed.ncbi.nlm.nih.gov/38191052/) | 2024 | Estudio mecanístico | Metabolism | La inhibición de PCSK9 previene y alivia los cálculos biliares de colesterol activando CYP7A1 vía PPARα, enzima clave del catabolismo del colesterol a ácidos biliares. |
| [39947256](https://pubmed.ncbi.nlm.nih.gov/39947256/) | 2025 | Revisión | Pharmacol Ther | Compara el direccionamiento de PCSK9 dentro vs. fuera del hepatocito; alirocumab y evolocumab actúan extracelularmente uniendo la PCSK9 circulante. |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Revisión | Curr Atheroscler Rep | Nuevos desarrollos en el tratamiento de la hipercolesterolemia familiar homocigota, incluyendo terapias anti-PCSK9. |
| [36422206](https://pubmed.ncbi.nlm.nih.gov/36422206/) | 2022 | Revisión | Medicina (Kaunas) | Diagnóstico y opciones de tratamiento de la hipercolesterolemia familiar, con mutaciones en APOB, LDLR y PCSK9. |
| [38277255](https://pubmed.ncbi.nlm.nih.gov/38277255/) | 2024 | Revisión | Curr Opin Lipidol | Actualización sobre terapias dirigidas a PCSK9 y su impacto en la reducción de LDL-C y riesgo cardiovascular. |
| [38185721](https://pubmed.ncbi.nlm.nih.gov/38185721/) | 2024 | Revisión | Signal Transduct Target Ther | Revisión exhaustiva del papel de PCSK9 en el metabolismo lipídico y su relevancia en enfermedad hepática, infecciosa y autoinmune, más allá de la cardiovascular. |
| [36739653](https://pubmed.ncbi.nlm.nih.gov/36739653/) | 2023 | Revisión | Kardiol Pol | Evidencia actual y perspectivas futuras sobre los inhibidores de PCSK9 y la reducción de eventos cardiovasculares. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad (no hay advertencias, contraindicaciones ni interacciones farmacológicas registradas en las fuentes consultadas; la ficha técnica de la TFDA está pendiente de obtener — ver DG001).

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 3 completado y un cuerpo bibliográfico consistente que conecta mecanísticamente la inhibición de PCSK9 con el catabolismo del colesterol (incluyendo activación de la vía CYP7A1), pero la evidencia clínica directa en población específica con "trastorno del proceso catabólico del colesterol" sigue siendo indirecta (el ensayo disponible es en pacientes VIH+, no en la población diana exacta).

**Para avanzar se necesita:**
- Obtener el prospecto de la TFDA con advertencias/contraindicaciones (DG001, bloqueante para evaluación de seguridad S1)
- Datos detallados de MOA vía API de DrugBank (DG002)
- Ensayos clínicos dirigidos específicamente a poblaciones con trastornos definidos del catabolismo del colesterol (más allá de estudios generales de PCSK9i)
- Confirmar la ausencia de comercialización en España y evaluar vía regulatoria si se decide avanzar
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


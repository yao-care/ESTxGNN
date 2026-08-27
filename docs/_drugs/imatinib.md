---
layout: default
title: Imatinib
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 10
---

# Imatinib
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

# Imatinib: De Leucemia Mieloide Crónica/GIST a Neoplasias Fibroblásticas (Candidato Multi-Indicación)

## Resumen en Una Frase

Imatinib es un inhibidor de tirosina quinasa (BCR-ABL, KIT, PDGFR) originalmente comercializado para el tratamiento de la **leucemia mieloide crónica** y **tumores del estroma gastrointestinal (GIST)** [fuente: PMID 18623899, PMID 18230575]. El modelo TxGNN genera **10 indicaciones candidatas**, todas dentro del espectro de neoplasias de estirpe fibroblástica/sarcomatosa, con la más sólida siendo **Neoplasia Fibroblástica** (representada clínicamente por el dermatofibrosarcoma protuberans, DFSP), respaldada por **20 publicaciones**, aunque sin ensayos clínicos vinculados en este paquete de evidencia.

---

## Resumen Rapido (Indicacion Ancla: Neoplasia Fibroblastica)

| Item | Contenido |
|------|------|
| Indicacion Original | Leucemia mieloide crónica y GIST (según literatura citada en el paquete) |
| Nueva Indicacion Predicha (ancla) | Neoplasia Fibroblástica (rank 2) |
| Puntaje de Prediccion TxGNN | 99.94% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Proceed with Guardrails |

---

## Ranking Comparativo de las 10 Indicaciones Predichas

| Rank | Indicacion | Score TxGNN | Nivel Evidencia | Etapa | Recomendacion |
|------|-----------|-------------|-----------------|-------|---------------|
| 1 | Heart fibrosarcoma | 99.94% | L4 | S1 | Hold |
| 2 | Fibroblastic neoplasm (DFSP) | 99.94% | L2 | S3 | Proceed with Guardrails |
| 3 | Conventional fibrosarcoma | 99.93% | L3 | S1 | Research Question |
| 4 | Kidney fibrosarcoma | 99.93% | L3 | S1 | Hold |
| 5 | Low grade fibromyxoid sarcoma | 99.93% | L5 | S0 | Hold |
| 6 | Liposarcoma | 99.88% | L2 | S2 | Research Question |
| 7 | Liver fibrosarcoma | 99.86% | L4 | S0 | Hold |
| 8 | Autosomal recessive familial Mediterranean fever | 99.86% | L5 | S0 | Hold |
| 9 | Ovarian myxoid liposarcoma | 99.85% | L5 | S0 | Hold |
| 10 | Familial rhabdoid tumor | 99.83% | L5 | S0 | Hold |

---

## Por que es Razonable esta Prediccion?

Según la literatura recopilada, imatinib es un inhibidor de tirosina quinasa que bloquea BCR-ABL, c-KIT y el receptor del factor de crecimiento derivado de plaquetas (PDGFR), mecanismo que sustentó su aprobación original en leucemia mieloide crónica y GIST (PMID 18230575, PMID 18623899). Este dato no está registrado en el campo estructurado de MOA de DrugBank (marcado como pendiente de captura), pero es consistente en múltiples abstracts del propio paquete de evidencia.

El grupo de indicaciones predichas por TxGNN converge casi en su totalidad en sarcomas de estirpe fibroblástica. La conexión mecanicista más fuerte corresponde al **dermatofibrosarcoma protuberans (DFSP)**, representado en el nodo "fibroblastic neoplasm": esta neoplasia presenta la fusión característica **COL1A1-PDGFB**, que mantiene activado el receptor PDGFRB de forma constitutiva, el blanco directo de imatinib. Esta relación ya está validada clínicamente (imatinib es tratamiento estándar en DFSP irresecable/metastásico según guías europeas, PMID 39904126), lo que hace que esta predicción sea la más razonable del grupo.

En contraste, indicaciones como "conventional fibrosarcoma" o "kidney fibrosarcoma" no tienen mutaciones controladoras conocidas en PDGFR/KIT/BCR-ABL, y el fibrosarcoma de bajo grado fibromixoide está impulsado por la fusión FUS-CREB3L2, ajena al mecanismo de imatinib. El liposarcoma es heterogéneo: los subtipos bien diferenciado/desdiferenciado dependen de amplificación MDM2/CDK4 y el subtipo mixoide de la fusión FUS-DDIT3, ninguno target de imatinib, aunque sí existen varios ensayos históricos de fase I/II que probaron imatinib en sarcoma de tejido blando de forma no selectiva por subtipo. Indicaciones como fiebre mediterránea familiar o tumor rabdoide familiar carecen de cualquier vínculo mecanístico conocido y probablemente representan ruido del embedding del modelo.

---

## Evidencia de Ensayos Clinicos

| Indicacion | Numero de Ensayo | Farmaco Probado | Fase | Estado | Inscripcion | Hallazgos Principales |
|-----------|---------|------|------|------|------|---------|
| Liposarcoma | [NCT00031915](https://clinicaltrials.gov/study/NCT00031915) | Imatinib | Fase 2 | Completado | N/A | Gleevec (imatinib) en sarcomas de tejido blando y hueso; incluye subgrupo de liposarcoma |
| Liposarcoma | [NCT00006357](https://clinicaltrials.gov/study/NCT00006357) | Imatinib (STI571) | Fase 1/2 | Completado | 91 | Búsqueda de dosis de STI571 en sarcoma de tejido blando avanzado |
| Kidney fibrosarcoma / Liposarcoma | [NCT00154388](https://clinicaltrials.gov/study/NCT00154388) | Imatinib | Fase 2 | Completado | 185 | Estudio exploratorio de imatinib en enfermedades raras malignas con quinasas sensibles a imatinib; basket trial, no específico de estas indicaciones |
| Liposarcoma | [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Sunitinib (no imatinib) | Fase 2 | Completado | 48 | Sarcoma de tejido blando metastásico/irresecable; fármaco distinto a imatinib |
| Liposarcoma | [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Regorafenib (no imatinib) | Fase 2 | Completado | 131 | Protocolo SARC024 en subtipos de sarcoma seleccionados; fármaco distinto a imatinib |

**Nota:** Solo NCT00031915, NCT00006357 y (parcialmente) NCT00154388 probaron imatinib directamente. Para "Fibroblastic neoplasm" (DFSP) —la indicación con el vínculo mecanístico más sólido— este paquete no capturó ningún ensayo clínico vinculado, pese a que imatinib tiene ensayos históricos conocidos en DFSP (p. ej. B2225); se recomienda revisión manual del mapeo de nodo-ensayo. Para heart fibrosarcoma, conventional fibrosarcoma, low grade fibromyxoid sarcoma, liver fibrosarcoma, fiebre mediterránea familiar, liposarcoma mixoide ovárico y tumor rabdoide familiar no hay ensayos clínicos registrados.

---

## Evidencia de Literatura

| PMID | Indicacion Asociada | Ano | Tipo | Revista | Hallazgos Principales |
|------|---------------------|-----|------|------|---------|
| [39904126](https://pubmed.ncbi.nlm.nih.gov/39904126/) | Fibroblastic neoplasm | 2025 | Guía clínica (Tier 1) | Eur J Cancer | Guía interdisciplinaria europea (EADO/EDF/UEMS/EADV) actualizada sobre diagnóstico y tratamiento del DFSP |
| [25852058](https://pubmed.ncbi.nlm.nih.gov/25852058/) | Fibroblastic neoplasm | 2015 | Revisión (Tier 2) | Mol Cancer Ther | Pérdida de CDKN2A/p16 como blanco terapéutico (CDK4) en DFSP resistente a imatinib |
| [19635106](https://pubmed.ncbi.nlm.nih.gov/19635106/) | Fibroblastic neoplasm | 2009 | Cohorte (Tier 2) | Histopathology | Confirma fusión COL1A1-PDGFB en 20 casos de DFSP, con implicancias terapéuticas directas |
| [27806849](https://pubmed.ncbi.nlm.nih.gov/27806849/) | Conventional fibrosarcoma | 2016 | Revisión (Tier 2) | Ann Diagn Pathol | Patología, genética y estrategias terapéuticas del DFSP, incluida transformación fibrosarcomatosa |
| [41236573](https://pubmed.ncbi.nlm.nih.gov/41236573/) | Fibroblastic neoplasm | 2025 | Preclínico | Human Cell | Establece línea celular de DFSP resistente a imatinib para investigación de mecanismos de resistencia |
| [17708241](https://pubmed.ncbi.nlm.nih.gov/17708241/) | Liposarcoma | 2007 | Reporte de caso | Hepatogastroenterology | Falta de actividad de imatinib en 2 casos de liposarcoma retroperitoneal KIT+ (hallazgo negativo relevante) |
| [12702540](https://pubmed.ncbi.nlm.nih.gov/12702540/) | Liposarcoma | 2003 | Serie de casos (Tier 3) | Ann Oncol | Uso potencial de imatinib en melanoma ocular y liposarcoma con expresión de c-KIT (CD117) |
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | Liposarcoma | 2011 | Fase 2 (Tier 2) | Int J Cancer | Sunitinib (no imatinib) en leiomiosarcoma, liposarcoma y histiocitoma fibroso maligno recidivante |
| [31173362](https://pubmed.ncbi.nlm.nih.gov/31173362/) | Liposarcoma | 2019 | Fase 3 | Cancer | Trabectedina (no imatinib) vs. dacarbazina en liposarcoma/leiomiosarcoma avanzado |
| [17687201](https://pubmed.ncbi.nlm.nih.gov/17687201/) | Kidney fibrosarcoma | 2007 | Revisión (Tier 2) | Gan To Kagaku Ryoho | Revisión de imatinib y sunitinib; sin datos específicos de fibrosarcoma renal |

**Notas de calidad:** Varios PMID recuperados no prueban imatinib (sunitinib, trabectedina, regorafenib) y solo comparten la indicación oncológica — se mantienen por contexto competitivo, no como evidencia directa del fármaco. Para heart fibrosarcoma solo hay 1 publicación (revisión general, sin datos robustos según su propio título). Para autosomal recessive familial Mediterranean fever, ovarian myxoid liposarcoma y familial rhabdoid tumor no existe literatura vinculada.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. El paquete de evidencia no contiene datos estructurados de advertencias, contraindicaciones ni interacciones farmacológicas (consulta TFDA/AEMPS sin resultados e interacciones no encontradas en la base consultada).

---

## Citotoxicidad

**Imatinib es un agente antineoplásico** (indicación original oncológica: leucemia mieloide crónica y GIST, según literatura del paquete).

| Item | Contenido |
|------|------|
| Clasificacion de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa BCR-ABL/KIT/PDGFR), no quimioterapia citotóxica convencional |
| Riesgo de Mielosupresion | Consultar las advertencias y precauciones del prospecto |
| Clasificacion de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Proteccion en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Conclusion y Proximos Pasos

**Decision: Proceed with Guardrails** (para Neoplasia Fibroblástica/DFSP) — **Research Question** (para Liposarcoma y Conventional Fibrosarcoma) — **Hold** (para las 7 indicaciones restantes)

**Justificacion:**
- La indicación "Fibroblastic neoplasm" tiene el respaldo mecanístico y clínico más sólido (fusión COL1A1-PDGFB, práctica clínica ya establecida en DFSP), pero este paquete no vinculó ningún ensayo clínico, lo que exige verificación manual antes de avanzar.
- Liposarcoma y conventional fibrosarcoma requieren estratificación por subtipo molecular antes de emitir una recomendación, ya que la evidencia agregada mezcla subtipos sensibles y no sensibles a imatinib.
- Las 7 indicaciones restantes carecen de mecanismo plausible, evidencia clínica suficiente, o ambas cosas, y se recomienda no continuar sin nueva evidencia.

**Para avanzar se necesita:**
- Confirmar el vínculo entre el nodo TxGNN "fibroblastic neoplasm" y ensayos clínicos conocidos de imatinib en DFSP (posible gap de mapeo de datos)
- Datos formales de MOA desde DrugBank (actualmente pendiente pese a consulta exitosa) y ficha técnica/prospecto de TFDA-AEMPS (bloqueado, DG001)
- Reestratificación de liposarcoma y fibrosarcoma convencional por subtipo molecular (MDM2/CDK4, FUS-DDIT3, COL1A1-PDGFB) antes de evaluación S2+
- Confirmación de estado de comercialización real en España (el registro actual muestra 0 autorizaciones, lo cual debe validarse dado que imatinib es un fármaco ampliamente utilizado)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


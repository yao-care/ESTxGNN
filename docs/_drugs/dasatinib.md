---
layout: default
title: Dasatinib
parent: 僅模型預測 (L5)
nav_order: 84
evidence_level: L5
indication_count: 10
---

# Dasatinib
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

# Dasatinib: De Leucemia Mieloide Crónica a Sarcoma de Ewing

## Resumen en Una Frase

Dasatinib es un inhibidor de tirosina-cinasas (BCR-ABL, SRC, c-KIT, PDGFR-β) cuyo uso oncológico mejor establecido —según la evidencia de ensayos de Fase 3 incluida en este paquete (p. ej. DASISION)— es la leucemia mieloide crónica Ph+, aunque actualmente no consta comercializado en España. El modelo TxGNN predice que también podría ser efectivo en **Sarcoma de Ewing**, con **3 ensayos clínicos** y **9 publicaciones** que respaldan parcialmente esta dirección, si bien con evidencia clínica aún débil.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Leucemia mieloide crónica (LMC) Ph+ — inferida de la evidencia de ensayos de Fase 3 del propio paquete; sin ficha de licencia española que lo confirme |
| Nueva Indicación Predicha | Sarcoma de Ewing (Ewing sarcoma) |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

DrugBank no aporta un campo de mecanismo de acción estructurado para este fármaco (brecha de datos pendiente, DG002), pero la literatura incluida en el paquete lo describe consistentemente como un inhibidor de múltiples tirosina-cinasas —BCR-ABL, la familia SRC, c-KIT, el receptor de efrina A y PDGFR-β (PMID 18215092)—, siendo aproximadamente 325 veces más potente que imatinib frente a BCR-ABL. Toda la evidencia clínica de Fase 3 recopilada en este paquete (DASISION, comparaciones frente a imatinib/Gleevec, estudios en LMC resistente) confirma que este es el terreno oncológico donde dasatinib está mejor consolidado.

La conexión con el sarcoma de Ewing pasa por SRC, no por BCR-ABL: múltiples estudios preclínicos muestran que la activación de SRC impulsa la formación de invadopodios, la migración y la invasión de células de sarcoma de Ewing (PMID 31521948, PMID 27566104), y que la inhibición de SRC con dasatinib reduce la migración/invasión e induce apoptosis en líneas celulares de sarcoma óseo dependientes de esta cinasa (PMID 17363602, PMID 18202781). Es una hipótesis mecanísticamente coherente, pero limitada: cuando se probó en clínica como agente único dentro de un ensayo amplio de sarcomas avanzados, la propia literatura del paquete señala que dasatinib **fracasó como monoterapia** en los subtipos sarcoma de Ewing y rabdomiosarcoma (PMID 35655525), lo que sugiere que cualquier desarrollo futuro debería explorar combinaciones en lugar de monoterapia.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Fase 1/2 | Terminado | 7 | Dasatinib + ifosfamida/carboplatino/etopósido en pediatría; ensayo terminado anticipadamente con muestra muy pequeña |
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Fase 2 | Completado | 366 | Estudio de tasa de respuesta y supervivencia libre de progresión a 6 meses con dasatinib en sarcomas avanzados (incluye sarcoma de Ewing); es la principal fuente de evidencia clínica, pero la literatura asociada indica que dasatinib en monoterapia no fue eficaz en este subtipo |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Fase 1 | Reclutando | 41 | Ensayo de terapia CAR-T anti-B7-H3, **no evalúa dasatinib**; aparece por coincidencia de la etiqueta de enfermedad, relevancia baja |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Revisión | Sarcoma | Revisa el complejo FAK-SRC en DSRCT, sarcoma de Ewing y rabdomiosarcoma; confirma que dasatinib en monoterapia fracasó en el ensayo Fase 2 para estos subtipos |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Revisión | Oncology Letters | Revisión sobre la señalización SRC como diana terapéutica potencial en sarcoma |
| [35190971](https://pubmed.ncbi.nlm.nih.gov/35190971/) | 2022 | Revisión | Curr Treat Options Oncol | Revisión de terapia sistémica para condrosarcoma; no es específica de sarcoma de Ewing |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Preclínico | Neoplasia | Tenascina C y SRC cooperan para promover la formación de invadopodios y la invasión en sarcoma de Ewing |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Preclínico | Neoplasia | El estrés del microambiente tumoral activa SRC e induce migración celular en sarcoma de Ewing |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Preclínico | Oncology Reports | Dasatinib muestra actividad antiproliferativa y antimigratoria in vitro en líneas de neuroblastoma y sarcoma de Ewing |
| [29776413](https://pubmed.ncbi.nlm.nih.gov/29776413/) | 2018 | Preclínico | Cell Commun Signal | El antagonista de CXCR4 plerixafor promueve proliferación y activa señalización de RTK en sarcoma de Ewing; relevancia indirecta, no evalúa dasatinib |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Preclínico | Cancer Research | Dasatinib inhibe migración/invasión en líneas de sarcoma humano e induce apoptosis en sarcoma óseo dependiente de SRC |
| [32999666](https://pubmed.ncbi.nlm.nih.gov/32999666/) | 2020 | Reporte de caso | Case Rep Oncol | Anomalía cromosómica rara en crisis blástica de LMC; no relacionado con sarcoma de Ewing, probable coincidencia de palabra clave |

---

## Información de Mercado en España

Dasatinib **no consta comercializado en España** según este paquete de evidencia (0 autorizaciones registradas, sin fichas de producto disponibles).

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida — inhibidor de tirosina-cinasas (BCR-ABL, SRC, c-KIT, PDGFR-β), según literatura del paquete (PMID 18215092) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto (sin datos estructurados de DrugBank/TFDA) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal; la literatura del paquete describe casos de derrame pleural/pericárdico, quilotórax y neumonitis intersticial asociados a dasatinib (PMID 36448074, PMID 36346055), por lo que la función pulmonar también debería vigilarse |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto — pendiente de confirmar (brecha bloqueante DG001) |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad: no hay advertencias, contraindicaciones ni interacciones farmacológicas documentadas en este paquete de evidencia (búsqueda de DDI sin resultados). La brecha DG001 (ficha técnica/prospecto TFDA no disponible) es de severidad **bloqueante** y actualmente impide completar la evaluación de seguridad inicial (S1).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La brecha de datos DG001 (advertencias y contraindicaciones TFDA) es bloqueante y no permite completar la evaluación de seguridad S1. Además, la evidencia clínica más sólida disponible (NCT00464620, Fase 2 completado) muestra, según la literatura asociada, que dasatinib fracasó como monoterapia en sarcoma de Ewing, y el fármaco no está actualmente comercializado en España.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica TFDA con advertencias y contraindicaciones (DG001, bloqueante)
- Obtener el mecanismo de acción estructurado vía API de DrugBank (DG002)
- Confirmar el estado real de autorización/comercialización en España (AEMPS)
- Evaluar estrategias de combinación (no monoterapia) para sarcoma de Ewing, dado el fracaso documentado del agente único
- Nota: este paquete evaluó 9 candidatas adicionales; la leucemia mieloide crónica presenta evidencia mucho más robusta (múltiples ensayos Fase 3 completados) y merecería un informe de evaluación independiente
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


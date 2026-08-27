---
layout: default
title: Trandolapril
parent: 僅模型預測 (L5)
nav_order: 282
evidence_level: L5
indication_count: 6
---

# Trandolapril
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

Usando el skill **data-report** implícitamente no aplica aquí (no es CLI output crudo), sino que sigo el prompt-plantilla ya definido en la conversación. Genero el informe directamente:

---

# Trandolapril: De Hipertensión Arterial (IECA) a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Trandolapril es un inhibidor de la enzima convertidora de angiotensina (IECA); no hay datos de indicación original ni de MOA detallado en las fuentes consultadas, pero por clase farmacológica se usa para hipertensión arterial e insuficiencia cardiaca. El modelo TxGNN predice que podría ser efectivo para **Hipertensión Renovascular Maligna**, pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde específicamente esta dirección.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No disponible — Trandolapril no está comercializado en España (0 autorizaciones); sin texto de indicación aprobada en la fuente regulatoria consultada |
| Nueva Indicacion Predicha | Hipertensión Renovascular Maligna |
| Puntaje de Prediccion TxGNN | 99.92% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Espana | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción específico de trandolapril en esta fuente. Según la información conocida, trandolapril pertenece a la clase de los inhibidores de la ECA (IECA), que bloquean la conversión de angiotensina I a angiotensina II, reduciendo la presión arterial y la resistencia vascular periférica; su eficacia como antihipertensivo de clase está bien establecida.

La hipertensión renovascular maligna suele asociarse a estenosis de la arteria renal (con frecuencia bilateral) y activación intensa del sistema renina-angiotensina-aldosterona, lo que en teoría hace atractivo el uso de un IECA para controlar la presión. Sin embargo, este mismo mecanismo es un arma de doble filo: en presencia de estenosis bilateral de arteria renal, los IECA dilatan la arteriola eferente y pueden provocar una caída abrupta de la presión de filtración glomerular, con riesgo de insuficiencia renal aguda.

No existe evidencia clínica específica de trandolapril en esta indicación — la predicción se basa únicamente en similitud mecanística de clase farmacológica, sin estudios que confirmen beneficio ni descarten el riesgo renal mencionado.

---

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La predicción se apoya únicamente en el score de TxGNN (99.92%) y en un razonamiento mecanístico de clase (IECA), sin ningún ensayo clínico ni publicación que la respalde, y con un riesgo mecánico conocido (insuficiencia renal aguda en estenosis bilateral de arteria renal) que no ha sido evaluado. La evidencia actual (L4) es insuficiente para avanzar a evaluación de seguridad.

**Para avanzar se necesita:**
- Datos del prospecto/ficha técnica (TFDA/AEMPS) sobre advertencias y contraindicaciones — actualmente es un vacío de datos bloqueante (Blocking)
- Mecanismo de acción (MOA) detallado y específico de trandolapril, verificado en DrugBank
- Estudios preclínicos o clínicos específicos en hipertensión renovascular maligna, dado el riesgo teórico de deterioro de función renal en estenosis bilateral
- Evaluación de la interacción fármaco-enfermedad en pacientes con enfermedad renovascular antes de cualquier consideración clínica

---

**Nota:** El conjunto de predicciones de TxGNN para trandolapril incluye otro candidato con evidencia mecanística más concreta — enfermedad cardiopulmonar crónica (cor pulmonale), respaldada por un estudio animal específico de trandolapril (PMID 8989645, nivel L3, etapa S1, recomendación "Research Question") — que podría merecer un informe independiente si se desea explorar esa vía en lugar de, o además de, la indicación de rango 1 aquí evaluada.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Delamanid
parent: 僅模型預測 (L5)
nav_order: 87
evidence_level: L5
indication_count: 7
---

# Delamanid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Delamanid: De Tuberculosis Multirresistente a Tuberculosis Bovina

## Resumen en Una Frase

Delamanid es un derivado nitro-dihidro-imidazooxazólico utilizado originalmente en el tratamiento de la tuberculosis pulmonar multirresistente (MDR-TB), como componente de regímenes combinados de segunda línea. El modelo TxGNN predice que podría ser efectivo para **Tuberculosis Bovina** (infección zoonótica por *Mycobacterium bovis*), aunque actualmente esta dirección cuenta con **0 ensayos clínicos** y solo **1 publicación** (de naturaleza genómica, no terapéutica) que la respalden.

> **Nota**: el paquete de evidencia contiene 7 indicaciones predichas para delamanid, todas dentro del espectro micobacteriano/tuberculoso salvo un falso positivo descartado (urticaria alérgica). La aquí destacada (rank 1) es la de mayor puntuación TxGNN, pero no la de mayor evidencia real — ver nota al final.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tuberculosis pulmonar multirresistente (MDR-TB), en terapia combinada de segunda línea *(no incluida en los datos de licencias del Evidence Pack; se trata de la indicación regulatoria global conocida de delamanid, ya que en España el fármaco no está comercializado)* |
| Nueva Indicación Predicha | Tuberculosis bovina (infección zoonótica por *M. bovis*) |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en este paquete de evidencia. Según la información conocida, delamanid es un antimicobacteriano que actúa inhibiendo la síntesis de ácido micólico de la pared celular, un mecanismo dirigido al género *Mycobacterium* en general y no exclusivo de *Mycobacterium tuberculosis*. Su eficacia en tuberculosis pulmonar multirresistente ha sido comprobada clínicamente.

*Mycobacterium bovis* (agente de la tuberculosis bovina, que puede transmitirse de forma zoonótica al ser humano) es filogenéticamente muy próximo a *M. tuberculosis* y comparte la misma vía de síntesis de pared celular. Mecanísticamente, por tanto, es plausible que delamanid conserve actividad frente a *M. bovis*, lo que da coherencia biológica a la predicción del modelo TxGNN.

Sin embargo, esta plausibilidad mecanística no está todavía respaldada por evidencia experimental directa: no existen ensayos clínicos registrados con delamanid en tuberculosis bovina/zoonótica, y la única publicación asociada es un estudio genómico sobre diversidad de resistencia en aislados de *M. bovis*, que no evalúa el fármaco. La predicción debe considerarse, por ahora, una hipótesis mecanística razonable pendiente de validación experimental.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39487429](https://pubmed.ncbi.nlm.nih.gov/39487429/) | 2024 | Estudio genómico observacional (WGS) | BMC Genomics | Caracterización mediante secuenciación de genoma completo de la diversidad genética y resistencia a fármacos en aislados de *M. bovis* causantes de tuberculosis zoonótica humana; no evalúa el uso de delamanid. |

---

## Información de Mercado en España

Delamanid no está actualmente comercializado en España (0 autorizaciones registradas en el Evidence Pack).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en la plausibilidad mecanística (proximidad filogenética entre *M. bovis* y *M. tuberculosis*) y en la puntuación del modelo TxGNN; no existe ningún ensayo clínico ni literatura que evalúe directamente delamanid en tuberculosis bovina/zoonótica, y el único artículo asociado es de naturaleza genómica, no terapéutica.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica de TFDA-EMA de delamanid (advertencias y contraindicaciones), bloqueante para cualquier evaluación de seguridad (DG001)
- Datos detallados del mecanismo de acción (MOA) desde DrugBank (DG002)
- Estudios preclínicos o in vitro de actividad de delamanid frente a *M. bovis*
- Confirmación de si la indicación se dirige a población humana con tuberculosis zoonótica o a uso veterinario, dado que delamanid es un fármaco de uso humano

**Nota adicional:** dentro del mismo paquete de evidencia, la indicación "inactive tuberculosis" (rank 2, puntuación TxGNN prácticamente idéntica, 99.91%) cuenta con 2 ensayos de Fase 2/3 activos (incluyendo NCT03568383, Fase 3, 5.832 participantes) y 20 publicaciones — representa una vía de evidencia considerablemente más sólida y podría priorizarse para una evaluación paralela.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


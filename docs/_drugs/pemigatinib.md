---
layout: default
title: Pemigatinib
parent: 僅模型預測 (L5)
nav_order: 217
evidence_level: L5
indication_count: 10
---

# Pemigatinib
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

# Pemigatinib: De Colangiocarcinoma con Fusión FGFR2 a Neoplasia Endocrina Múltiple

## Resumen en Una Frase

Pemigatinib es un inhibidor selectivo de FGFR1/2/3 cuyo uso conocido es el colangiocarcinoma con fusión de FGFR2 (dato tomado del razonamiento mecanístico interno, no de una ficha técnica confirmada). El modelo TxGNN predice que podría ser efectivo para **Neoplasia Endocrina Múltiple (MEN)**, pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección, y el propio análisis mecanístico señala que probablemente se trata de un falso positivo del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Colangiocarcinoma con fusión de FGFR2* (*fuente: razonamiento mecanístico interno; no confirmado por ficha técnica AEMPS/TFDA — dato de licencia no disponible) |
| Nueva Indicación Predicha | Neoplasia Endocrina Múltiple (MEN) |
| Puntaje de Predicción TxGNN | 99.71% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos oficiales sobre el mecanismo de acción en ficha técnica (Data Gap de severidad Alta). Según la información disponible en el razonamiento mecanístico generado internamente, pemigatinib es un inhibidor selectivo de FGFR1/2/3, cuya eficacia en el colangiocarcinoma con fusión de FGFR2 ha sido comprobada en el desarrollo clínico del fármaco.

Sin embargo, para la indicación predicha en primer lugar (Neoplasia Endocrina Múltiple), el propio análisis del candidato indica que **no existe un vínculo mecanístico plausible**: el síndrome MEN está asociado principalmente a mutaciones en los genes MEN1 y RET, sin relación conocida con la vía de señalización FGFR1/2/3. No hay respaldo mecanístico ni evidencia clínica, por lo que esta predicción podría corresponder a una asociación espuria dentro del espacio de embeddings de TxGNN, más que a una hipótesis biológica sólida.

Cabe destacar que, entre las 10 indicaciones predichas de mayor puntaje para este fármaco, varias corresponden a enfermedades veterinarias (fiebre catarral maligna, rinotraqueítis infecciosa bovina) o a direcciones mecanísticas opuestas a la farmacología del inhibidor de FGFR (amenorrea, esclerosis lateral amiotrófica), lo que sugiere ruido generalizado en esta región del espacio de predicción para este fármaco. La única excepción parcial es el carcinoma de mama HER2 positivo (rank 3), que alcanzó nivel de evidencia L4 gracias a una publicación de revisión sobre inhibidores de cinasas, apoyada en el crosstalk conocido entre las vías FGFR y HER2 como mecanismo de resistencia a terapias anti-HER2.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Citotoxicidad

*(Sección incluida por tratarse de un antineoplásico — inhibidor dirigido de FGFR1/2/3, con uso conocido en colangiocarcinoma.)*

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor selectivo de FGFR1/2/3) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación de mayor puntaje (MEN) carece de respaldo mecanístico y no cuenta con ningún ensayo clínico ni publicación; el propio análisis interno la señala como probable falso positivo. Además, la ficha técnica/prospecto oficial no está disponible (Data Gap bloqueante), lo que impide iniciar la evaluación de seguridad S1 para cualquier dirección de reposicionamiento de este fármaco.

**Para avanzar se necesita:**
- Obtener la ficha técnica oficial (AEMPS/TFDA) del producto — actualmente bloqueante para la evaluación de seguridad
- Confirmar mecanismo de acción y categorías DrugBank mediante consulta directa a la API de DrugBank
- Si se prioriza investigación adicional, dirigir el esfuerzo al candidato rank 3 (carcinoma de mama HER2 positivo), único que alcanzó nivel de evidencia L4, aunque aún requiere estudios primarios (actualmente solo respaldado por una revisión bibliográfica general)
- Descartar o reevaluar la hipótesis MEN salvo que surja nueva evidencia mecanística o clínica
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


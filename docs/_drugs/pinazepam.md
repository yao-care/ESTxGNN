---
layout: default
title: Pinazepam
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 7
---

# Pinazepam
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

# Pinazepam: De Ansiedad (uso histórico) a Insomnio

## Resumen en Una Frase

Pinazepam es un derivado benzodiazepínico (7-cloro-1-propargil-5-fenil-3H-1,4-benzodiazepin-2-ona) cuyo uso ha sido documentado históricamente en la literatura como ansiolítico/sedante (comercializado en Italia bajo el nombre "Domar"); actualmente no está comercializado en España ni Taiwán. El modelo TxGNN predice que podría ser efectivo para **Insomnio**, con un puntaje de **99.95%**, pero de momento solo existe **1 ensayo clínico** registrado —de relevancia limitada (Grado C, sin relación con insomnio ni con el fármaco)— y **ninguna publicación específica** que respalde esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en registros regulatorios (fármaco no comercializado en España). La literatura histórica lo describe como ansiolítico/sedante de clase benzodiazepina |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción específico de pinazepam. Según la información disponible en la literatura, pinazepam es un derivado 1,4-benzodiazepínico que se metaboliza principalmente a N-desmetildiazepam (nordiazepam), el mismo metabolito activo compartido con diazepam. Este grupo de fármacos actúa como modulador positivo del receptor GABA-A, mecanismo que constituye la base farmacológica estándar tanto del efecto ansiolítico como del efecto sedante-hipnótico.

Pinazepam ha sido descrito en estudios preclínicos y clínicos tempranos como un ansiolítico con menor actividad hipnótica y menor deterioro de la coordinación motora en comparación con diazepam, y fue comercializado históricamente en Italia para el tratamiento de la ansiedad. La relación entre ansiedad e insomnio es estrecha dentro de la clase de las benzodiazepinas: el efecto sedante-hipnótico es un "efecto de clase" compartido por prácticamente todos los agonistas GABA-A, lo que hace mecanísticamente plausible que un ansiolítico como pinazepam también reduzca la latencia de sueño.

No obstante, esta plausibilidad es puramente de clase farmacológica (class-effect) y no está respaldada por ningún ensayo clínico o estudio específico de pinazepam en insomnio. La predicción de TxGNN debe interpretarse, por tanto, como una hipótesis mecanística razonable pero no verificada con evidencia directa del fármaco.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04151485](https://clinicaltrials.gov/study/NCT04151485) | NA | Desconocido | 177 | Programa psicológico mente/cuerpo para fertilidad en Hungría; es un ensayo conductual no farmacológico sin relación directa con insomnio ni con pinazepam (relevancia Grado C) |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible que respalde específicamente el uso de pinazepam en insomnio.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se dispone actualmente de las advertencias, contraindicaciones ni interacciones farmacológicas del fármaco (los datos del prospecto de la TFDA aún no han sido incorporados), por lo que la evaluación de seguridad inicial no puede completarse con la información disponible.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para insomnio se apoya únicamente en un razonamiento de clase farmacológica (efecto sedante-hipnótico compartido por las benzodiazepinas), sin ningún ensayo clínico ni publicación específica de pinazepam en esta indicación; el único ensayo recuperado es irrelevante (estudio conductual no farmacológico, relevancia Grado C). Además, el fármaco no está comercializado en España ni Taiwán y falta información básica de seguridad (prospecto de la TFDA), lo que impide iniciar siquiera la evaluación inicial de seguridad (S1).

**Para avanzar se necesita:**
- Obtener el prospecto/advertencias de la TFDA (brecha bloqueante DG001), requisito previo para cualquier evaluación de seguridad
- Datos detallados del mecanismo de acción (MOA) desde DrugBank (brecha DG002)
- Evidencia clínica o de literatura específica de pinazepam en insomnio, actualmente inexistente
- Como nota adicional: la indicación secundaria "ansiedad" (rank 6 en el listado de predicciones) presenta un nivel de evidencia superior (L3, etapa S1, "Research Question"), con literatura específica de pinazepam y antecedente de comercialización histórica ("Domar", Italia) para esa indicación; podría valer la pena evaluarla como candidata alternativa o complementaria
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


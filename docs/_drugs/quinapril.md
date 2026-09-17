---
layout: default
title: Quinapril
parent: Solo predicción del modelo (L5)
nav_order: 232
evidence_level: L5
indication_count: 5
---

# Quinapril
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Quinapril: Indicación Original No Disponible → Hipertensión Renovascular Maligna

## Resumen en Una Frase

Quinapril (DrugBank DB00881) no cuenta actualmente con datos de indicación original ni de mecanismo de acción en este Evidence Pack. El modelo TxGNN predice que podría ser efectivo para **Hipertensión Renovascular Maligna**, con un puntaje de **99,86%**, pero por ahora no existe ningún ensayo clínico ni publicación que respalde directamente esta indicación específica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el Evidence Pack |
| Nueva Indicación Predicha | Hipertensión Renovascular Maligna |
| Puntaje de Predicción TxGNN | 99,86% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de quinapril en esta fuente. Tampoco hay registro de su(s) indicación(es) original(es) en los datos regulatorios consultados.

Como referencia, el propio candidato genera cuatro predicciones adicionales de alta puntuación con perfil clínico relacionado (hipertensión renal maligna, hipertensión pulmonar por enfermedad pulmonar/hipoxia, hipertensión pulmonar de mecanismo multifactorial y síndrome de Braddock), lo que sugiere que el modelo está agrupando el candidato dentro de un espacio fenotípico cardiovascular/renal. Sin embargo, sin el MOA original ni la indicación aprobada, no es posible en este momento construir una justificación mecanística verificable para la indicación de rango 1.

**Se recomienda completar primero los data gaps DG001 (advertencias/contraindicaciones) y DG002 (MOA vía DrugBank) antes de profundizar en el razonamiento mecanístico.**

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación predicha de mayor rango (hipertensión renovascular maligna) no cuenta con ningún ensayo clínico ni literatura de respaldo (Nivel de Evidencia L5, solo predicción del modelo). Además, faltan datos críticos de MOA, indicación original y seguridad, y el fármaco no está comercializado en España (0 autorizaciones). No hay base suficiente para avanzar a evaluación de seguridad (S1).

**Para avanzar se necesita:**
- Resolver DG001: obtener advertencias/contraindicaciones desde la fuente regulatoria correspondiente
- Resolver DG002: obtener el mecanismo de acción (MOA) vía DrugBank API
- Confirmar la(s) indicación(es) original(es) aprobada(s) del fármaco
- Evidencia clínica o de literatura específica para hipertensión renovascular maligna (rank 1)
- Dado que rank 3 (hipertensión pulmonar por enfermedad pulmonar/hipoxia) sí arrojó 20 resultados en PubMed, revisar manualmente esa literatura para confirmar relevancia real antes de descartar esa vía alternativa
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


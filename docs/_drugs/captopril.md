---
layout: default
title: Captopril
parent: Evidencia moderada (L3-L4)
nav_order: 101
evidence_level: L4
indication_count: 4
---

# Captopril
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **4** 
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

# Captopril: De Inhibidor de la ECA a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Captopril es un inhibidor de la enzima convertidora de angiotensina (ECA), comercializado en España en comprimidos. El modelo TxGNN predice que podría ser efectivo para la **enfermedad renal hipertensiva maligna**, pero la evidencia es mínima: **0 ensayos clínicos** y **1 publicación**, un reporte de caso diagnóstico sin valor terapéutico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de autorización de la AEMPS disponibles (todas las fichas tienen el campo de indicación vacío) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.28% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados en la base de datos. Según la información conocida, captopril es un inhibidor de la ECA, es decir, actúa sobre el sistema renina-angiotensina-aldosterona (SRAA), y mecanísticamente podría ser aplicable a la hipertensión maligna con daño renal.

En la hipertensión maligna con afectación renal se plantea que la activación del SRAA participa en el daño. Bloquear la ECA reduce la formación de angiotensina II, lo que da un fundamento fisiopatológico plausible para la predicción del modelo.

Este fundamento es solo teórico. La única publicación recuperada es un reporte de caso diagnóstico (renografía con captopril con resultado positivo en un paciente con carcinoma renal, sin estenosis de la arteria renal). No aporta datos de eficacia terapéutica. Además, la indicación original del fármaco no está verificada en los datos disponibles, por lo que no se puede evaluar la similitud con ella.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Reporte de caso (diagnóstico) | Clinical Nuclear Medicine | Renografía con captopril positiva sin estenosis de arteria renal, debida a un gran carcinoma renal cromófobo. La hipertensión dependiente de renina se resolvió tras la nefrectomía. Uso diagnóstico, no terapéutico. |

---

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones. El texto de indicación aprobada no está registrado en ninguna de ellas.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 61620 | Captopril Mylan 50 mg comprimidos EFG | Comprimido | Mylan Pharmaceuticals S.L. |
| 64762 | Captopril Mabo 50 mg comprimidos EFG | Comprimido | Mabo Farma S.A. |
| 55939 | Captopril Qualigen 50 mg comprimidos | Comprimido | Neuraxpharm Spain S.L. |
| 64764 | Captopril Tarbis 25 mg comprimidos EFG | Comprimido | Tarbis Farma S.L. |
| 62424 | Captopril Sandoz 25 mg comprimidos EFG | Comprimido | Sandoz Farmacéutica S.A. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya en una puntuación alta del modelo (99.28%) y en un fundamento mecanístico plausible. Sin embargo, no hay ensayos clínicos y la única publicación es un reporte de caso diagnóstico sin evidencia de eficacia. Tampoco están verificadas la indicación original ni la información de seguridad de la ficha técnica.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de la AEMPS (advertencias y contraindicaciones), un requisito previo al cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar la indicación original aprobada en las autorizaciones españolas.
- Buscar estudios clínicos de captopril en hipertensión maligna con afectación renal.
- Evaluar el riesgo de lesión renal aguda con inhibidores de la ECA en pacientes con estenosis bilateral de arteria renal o riñón único funcionante.
- Como contexto, la predicción relacionada de **hipertensión renovascular maligna** (puntuación idéntica, nivel L4) cuenta con más literatura, aunque compuesta sobre todo de revisiones y reportes de caso. Puede servir como línea de investigación complementaria.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


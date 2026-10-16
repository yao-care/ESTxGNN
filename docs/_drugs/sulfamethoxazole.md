---
layout: default
title: Sulfamethoxazole
parent: Evidencia moderada (L3-L4)
nav_order: 751
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Sulfamethoxazole: nueva indicación predicha, Conjuntivitis contagiosa aguda (nivel de evidencia L4). Indicación original: Otitis media infecciosa (según el grafo de conocimiento"
---

# Sulfamethoxazole
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

# Sulfametoxazol: De Otitis Media Infecciosa a Conjuntivitis Contagiosa Aguda

## Resumen en Una Frase

Sulfametoxazol es una sulfonamida antibacteriana, originalmente utilizada para infecciones como la otitis media infecciosa, la nocardiosis, la toxoplasmosis y la neumocistosis.
El modelo TxGNN predice que podría ser efectivo para **conjuntivitis contagiosa aguda**, aunque esta enfermedad ya figura entre sus indicaciones originales en el grafo de conocimiento, por lo que no es un reposicionamiento genuino.
La evidencia se limita a **0 ensayos clínicos** y **1 publicación** (un estudio de cohorte sobre bacteriología de la conjuntivitis infantil).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Otitis media infecciosa (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Conjuntivitis contagiosa aguda |
| Puntaje de Predicción TxGNN | 99,63% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 7 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento general, el sulfametoxazol inhibe la enzima bacteriana dihidropteroato sintetasa, bloqueando la síntesis de folato, y se combina habitualmente con trimetoprima para lograr un efecto sinérgico. Esta explicación procede de conocimiento general y no de los datos aportados.

Mecanísticamente, un antibacteriano de este tipo es plausible frente a la conjuntivitis bacteriana. Sin embargo, la conjuntivitis ya figura entre las indicaciones originales del fármaco en el grafo de conocimiento, por lo que **no se trata de un verdadero candidato a reposicionamiento**. El puntaje elevado (0,996) probablemente refleja esa asociación ya existente y no una señal nueva.

Además, la compatibilidad de vías de administración no está evaluada: las formas disponibles en España son orales (comprimidos, suspensión) e inyectables, y no hay formulación oftálmica en los datos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31788487](https://pubmed.ncbi.nlm.nih.gov/31788487/) | 2019 | Cohorte (retrospectivo) | Medical Hypothesis, Discovery & Innovation Ophthalmology Journal | Análisis retrospectivo de la bacteriología y los patrones de sensibilidad antibiótica en la conjuntivitis bacteriana aguda infantil en el oeste de Grecia; el estudio no evalúa específicamente el sulfametoxazol según los datos disponibles |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 48670 | SEPTRIN 80 mg/400 mg COMPRIMIDOS | Comprimido | No disponible |
| 54920 | SOLTRIM 160MG/ 800MG POLVO Y SOLUCIÓN PARA SOLUCIÓN INYECTABLE | Polvo y solución para solución inyectable | No disponible |
| 58501 | SEPTRIN FORTE 160 mg/800 mg COMPRIMIDOS | Comprimido | No disponible |
| 48669 | SEPTRIN PEDIATRICO 20 mg/100 mg COMPRIMIDOS | Comprimido | No disponible |
| 48671 | SEPTRIN PEDIATRICO 8 mg/40 mg/ml SUSPENSIÓN ORAL | Suspensión oral | No disponible |

Hay 7 autorizaciones vigentes en total; se muestran las 5 principales.

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto de prospecto)**: porfiria (hereditaria y trastornos del metabolismo de porfirinas), enfermedad renal, insuficiencia renal, uremia, glomerulonefritis, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, anemia por deficiencia de ácido fólico, deficiencia de G6PD, colitis por *Clostridium difficile*, enterocolitis necrotizante perinatal, enfermedad por depósito de glucógeno, cistinuria, galactosemia y piouréter.
- **Interacciones Farmacológicas**: se identificaron 151 interacciones en total. Entre las mostradas, destacan las de nivel **moderado** con antidiabéticos (clorpropamida, glimepirida, acetohexamida, glipizida, gliburida) y con distintas insulinas (humana, aspart, degludec, detemir, glargina, glulisina), con riesgo de hipoglucemia; también balsalazida y ácido picosulfúrico (moderadas). Las de nivel **leve** incluyen famotidina, claritromicina, dolasetrón, palonosetrón, cisaprida y granisetrón.

No se dispone de las advertencias y contraindicaciones del prospecto de la AEMPS; consultar el prospecto para completar la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La conjuntivitis ya es una indicación original del fármaco según el grafo de conocimiento, por lo que el puntaje alto de TxGNN no representa una señal nueva. Además, no hay ensayos clínicos, solo un estudio de cohorte indirecto, y falta información clave de seguridad del prospecto.

**Para avanzar se necesita:**
- Confirmar con el prospecto de la AEMPS las indicaciones aprobadas, advertencias y contraindicaciones.
- Obtener datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Definir si existe interés real en una vía oftálmica, ya que las formulaciones disponibles son orales e inyectables.
- Seleccionar una indicación realmente nueva (no incluida entre las originales) para evaluar un reposicionamiento genuino.
- Buscar evidencia específica del sulfametoxazol (o cotrimoxazol) en conjuntivitis, incluidos ensayos clínicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Sulfamethoxazole
parent: Solo predicción del modelo (L5)
nav_order: 751
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "sulfamethoxazole"
predicted_indications: ["acute contagious conjunctivitis"]
description: "Sulfamethoxazole: nueva indicación predicha, Conjuntivitis contagiosa aguda (acute contagious conjunctivitis) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 7 (comercializadas: 7)"
---

# Sulfamethoxazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Sulfamethoxazole: Conjuntivitis contagiosa aguda (acute contagious conjunctivitis)
{: .text-alpha }

## Resumen en Una Frase

Sulfametoxazol es una sulfonamida antibacteriana, originalmente utilizada para infecciones como la otitis media infecciosa, la nocardiosis, la toxoplasmosis y la neumocistosis.
El modelo TxGNN (aprendizaje profundo) predice que podría ser efectivo para **conjuntivitis contagiosa aguda**.
La evidencia se limita a **0 ensayos clínicos** y **1 publicación** (un estudio de cohorte sobre bacteriología de la conjuntivitis infantil).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Conjuntivitis contagiosa aguda (acute contagious conjunctivitis) |
| Puntaje de Predicción TxGNN | 0.9963 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 7 de 7) |
| Número de Autorizaciones | 7 (comercializadas: 7) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Sulfamethoxazole es (traducción no oficial): «Inhibidor de la dihidropteroato sintasa bacteriana». Texto original en inglés: "Bacterial dihydropteroate synthase inhibitor" ([ChEMBL CHEMBL443 (sulfamethoxazole): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL443), CC BY-SA 3.0; consultado el 2026-11-19). Según el conocimiento general, el sulfametoxazol inhibe la enzima bacteriana dihidropteroato sintetasa, bloqueando la síntesis de folato, y se combina habitualmente con trimetoprima para lograr un efecto sinérgico. Esta explicación procede de conocimiento general y no de los datos aportados.

Mecanísticamente, un antibacteriano de este tipo es plausible frente a la conjuntivitis bacteriana. El puntaje elevado (0,9963) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Además, la compatibilidad de vías de administración no está evaluada: las formas disponibles en España son orales (comprimidos, suspensión) e inyectables, y no hay formulación oftálmica en los datos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

<!-- review:begin es-lic-20261124b-sulfamethoxazole-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Hay 7 autorizaciones vigentes en total; se muestran las 5 principales." Eliminado: la frase describía cuántas filas mostraba la tabla anterior y repetía el número de autorizaciones. La tabla de Información de Mercado en España se genera desde el 2026-11-24 por programa a partir de los datos de CIMA (AEMPS); las cifras actuales están en el Resumen rápido y bajo la tabla. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261124b-sulfamethoxazole-1 -->

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31788487](https://pubmed.ncbi.nlm.nih.gov/31788487/) | 2019 | Cohorte (retrospectivo) | Medical Hypothesis, Discovery & Innovation Ophthalmology Journal | Análisis retrospectivo de la bacteriología y los patrones de sensibilidad antibiótica en la conjuntivitis bacteriana aguda infantil en el oeste de Grecia; el estudio no evalúa específicamente el sulfametoxazol según los datos disponibles |

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 48670 | SEPTRIN 80 mg/400 mg COMPRIMIDOS | COMPRIMIDO | Teofarma S.R.L. | Comercializada |
| 54920 | SOLTRIM 160MG/ 800MG POLVO Y SOLUCION PARA SOLUCION INYECTABLE | POLVO Y SOLUCIÓN PARA SOLUCIÓN INYECTABLE | Almirall S.A. | Comercializada |
| 58501 | SEPTRIN FORTE 160 mg/800 mg COMPRIMIDOS | COMPRIMIDO | Teofarma S.R.L. | Comercializada |
| 48669 | SEPTRIN PEDIATRICO 20 mg/100 mg COMPRIMIDOS | COMPRIMIDO | Teofarma S.R.L. | Comercializada |
| 48671 | SEPTRIN PEDIATRICO 8 mg/40 mg/ml SUSPENSION ORAL | SUSPENSIÓN ORAL | Teofarma S.R.L. | Comercializada |
| 45611 | BRONCOVIR SUSPENSION ORAL | SUSPENSIÓN ORAL | Industria Quimica Y Farmaceutica Vir S.A. | Comercializada |
| 49391 | BALSOPRIM 26,6MG/ML+5,4MG/ML+0,5MG/ML SUSPENSIÓN ORAL | SUSPENSIÓN ORAL | Desma Laboratorio Farmaceutico S.L. | Comercializada |

Se muestran las 7 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto de prospecto)**: porfiria (hereditaria y trastornos del metabolismo de porfirinas), enfermedad renal, insuficiencia renal, uremia, glomerulonefritis, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, anemia por deficiencia de ácido fólico, deficiencia de G6PD, colitis por *Clostridium difficile*, enterocolitis necrotizante perinatal, enfermedad por depósito de glucógeno, cistinuria, galactosemia y piouréter.
- **Interacciones Farmacológicas**: se identificaron 151 interacciones en total. Entre las mostradas, destacan las de nivel **moderado** con antidiabéticos (clorpropamida, glimepirida, acetohexamida, glipizida, gliburida) y con distintas insulinas (humana, aspart, degludec, detemir, glargina, glulisina), con riesgo de hipoglucemia; también balsalazida y ácido picosulfúrico (moderadas). Las de nivel **leve** incluyen famotidina, claritromicina, dolasetrón, palonosetrón, cisaprida y granisetrón.

No se dispone de las advertencias y contraindicaciones del prospecto de la AEMPS; consultar el prospecto para completar la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje alto de TxGNN (modelo de aprendizaje profundo) puede reflejar similitudes aprendidas entre enfermedades relacionadas, no evidencia biológica. Además, no hay ensayos clínicos, solo un estudio de cohorte indirecto, y falta información clave de seguridad del prospecto.

**Para avanzar se necesita:**
- Confirmar con el prospecto de la AEMPS las indicaciones aprobadas, advertencias y contraindicaciones.
- Obtener datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Definir si existe interés real en una vía oftálmica, ya que las formulaciones disponibles son orales e inyectables.
- Seleccionar una indicación realmente nueva (no incluida entre las originales) para evaluar un reposicionamiento genuino.
- Buscar evidencia específica del sulfametoxazol (o cotrimoxazol) en conjuntivitis, incluidos ensayos clínicos.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; la versión anterior se guarda en el registro) | [ChEMBL CHEMBL443 (sulfamethoxazole): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL443) |
| 2026-11-24 | Eliminado: descripción de la tabla anterior y número de autorizaciones | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


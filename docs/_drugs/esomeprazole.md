---
layout: default
title: Esomeprazole
parent: Solo predicción del modelo (L5)
nav_order: 308
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "Esomeprazole"
predicted_indications: ["duodenal obstruction"]
description: "Esomeprazole: nueva indicación predicha, Duodenal obstruction (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Esomeprazole
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

## Esomeprazole: Duodenal obstruction
{: .text-alpha }

## Resumen en Una Frase

Esomeprazol es un inhibidor de la bomba de protones (S-isómero del omeprazol), utilizado originalmente para la enfermedad de úlcera péptica, el reflujo gastroesofágico y el síndrome de Zollinger-Ellison.
El modelo TxGNN predice que podría ser efectivo para **reflujo duodenogástrico**,
pero actualmente hay **0 ensayos clínicos** y **1 publicación** (una revisión general sobre inhibidores de la bomba de protones) relacionados con esta dirección, por lo que la evidencia es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Duodenal obstruction |
| Puntaje de Predicción TxGNN | 0.9945 |
| Nivel de Evidencia | L5 (solo racionalidad mecanística, sin estudios específicos para esta indicación) |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 13; autorizadas no comercializadas: 1; revocadas o suspendidas: 6) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Esomeprazol inhibe la bomba de protones gástrica (H+/K+-ATPasa, cuyo gen diana es ATP4A) y, con ello, reduce la secreción de ácido gástrico. Por eso se usa en la úlcera péptica, el reflujo gastroesofágico y los estados de hipersecreción ácida. Los datos compilados no incluyen una descripción detallada del mecanismo de acción, por lo que esta explicación se basa en el conocimiento farmacológico general de la clase.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Revisión | European Journal of Clinical Pharmacology | Actualización del uso clínico y la farmacocinética de los inhibidores de la bomba de protones, fármacos de primera elección en úlcera péptica, infección por *H. pylori*, reflujo gastroesofágico, lesiones por AINE y síndrome de Zollinger-Ellison. No aborda directamente el reflujo duodenogástrico. |

---

## Información de Mercado en España

Se muestran las 5 principales:

<!-- review:begin es-lic-20261105-esomeprazole-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Hay 20 autorizaciones vigentes, todas de medicamentos con esomeprazol como único principio activo. Se muestran las 5 principales:" Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-esomeprazole-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 72702 | ESOMEPRAZOL TEVA 40 mg CAPSULAS DURAS GASTRORRESISTENTES EFG | CÁPSULA DURA GASTRORRESISTENTE | Teva Pharma S.L.U. | Comercializada |
| 66038 | NEXIUM 40 mg POLVO PARA SOLUCION INYECTABLE Y PARA PERFUSION | POLVO PARA SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN | Grünenthal Pharma S.A. | Comercializada |
| 63940 | AXIAGO 20 mg COMPRIMIDOS GASTRORRESISTENTES | COMPRIMIDO GASTRORRESISTENTE | Grünenthal Pharma S.A. | Comercializada |
| 81799 | ESOMEPRAZOL MABO 20 MG CAPSULAS DURAS GASTRORRESISTENTES EFG | CÁPSULA DURA GASTRORRESISTENTE | Mabo Farma S.A. | Comercializada |
| 63437 | NEXIUM MUPS 40 mg COMPRIMIDOS GASTRORRESISTENTES | COMPRIMIDO GASTRORRESISTENTE | Grünenthal Pharma S.A. | Comercializada |

Se muestran 5 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación en el grafo de conocimiento** (no proceden del texto del prospecto): insuficiencia hepática, osteoporosis, osteoporosis posmenopáusica, fractura ósea y gastritis atrófica crónica. Deben verificarse contra el prospecto oficial.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto de la AEMPS.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**

**Para avanzar se necesita:**
- Estudios clínicos o series de casos que evalúen esomeprazol en reflujo duodenogástrico, con criterios de valoración definidos (síntomas, gastritis biliar, hallazgos endoscópicos).
- Revisión de la literatura sobre inhibidores de la bomba de protones en reflujo biliar, y comparación con tratamientos orientados a la motilidad.
- Datos detallados del mecanismo de acción y del prospecto oficial (advertencias y contraindicaciones) para completar el análisis de seguridad.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Hay 20 autorizaciones vigentes, todas de medicamentos con esomeprazol como único principio activo" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


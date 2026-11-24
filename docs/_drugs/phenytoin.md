---
layout: default
title: Phenytoin
parent: Solo predicción del modelo (L5)
nav_order: 634
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "Phenytoin"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
description: "Phenytoin: nueva indicación predicha, Neoplasia del nervio trigémino (trigeminal nerve neoplasm) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 6 (comercializadas: 4)"
---

# Phenytoin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Phenytoin: Neoplasia del nervio trigémino (trigeminal nerve neoplasm)
{: .text-alpha }

## Resumen en Una Frase

Fenitoína es un antiepiléptico bloqueador de canales de sodio dependientes de voltaje, utilizado originalmente para tratar la epilepsia (crisis tónico-clónicas generalizadas, crisis parciales, síndrome de Lennox-Gastaut y estatus epiléptico).
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino**, aunque **no hay ensayos clínicos** y solo **2 publicaciones** relacionadas, ninguna de las cuales aborda directamente esa enfermedad.
Se trata de una predicción sin respaldo real (nivel L5); la puntuación procede del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, como la neuralgia del trigémino, una indicación distinta y mejor sustentada, no evidencia biológica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino (trigeminal nerve neoplasm) |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 4 de 6; revocadas o suspendidas: 2) |
| Número de Autorizaciones | 6 (comercializadas: 4) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Phenytoin (traducción no oficial): «No se ha establecido el mecanismo preciso por el cual la fenitoína ejerce su efecto terapéutico, pero se cree que implica el bloqueo dependiente del voltaje de los canales de sodio de la membrana, lo que produce una reducción de las descargas neuronales sostenidas de alta frecuencia.» Texto original en inglés: "The precise mechanism by which phenytoin exerts its therapeutic effect has not been established but is thought to involve the voltage-dependent blockade of membrane sodium channels resulting in a reduction in sustained high-frequency neuronal discharges." ([DailyMed: Extended Phenytoin Sodium (phenytoin sodium) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=363cd347-d25e-42b9-9ce7-30642f3cb353), versión del 2026-06-25; consultado el 2026-11-19). Según la información conocida, la fenitoína bloquea de forma dependiente del uso los canales de sodio dependientes de voltaje (entre ellos Nav1.2, codificado por SCN2A), lo que estabiliza las membranas neuronales y limita la descarga repetitiva de alta frecuencia. Su eficacia en la epilepsia está bien establecida.

Para la neoplasia del nervio trigémino, **no existe una justificación mecanística directa de actividad antitumoral**. El bloqueo de canales de sodio podría aliviar el dolor neuropático causado por la afectación nerviosa, pero sería un efecto sintomático y no modificador de la enfermedad. Los dos artículos recuperados tratan sobre la neuralgia del trigémino y el síndrome de Sturge-Weber, no sobre neoplasias del trigémino.

La puntuación elevada procede del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, como la **neuralgia del trigémino** (puesto 9 de las predicciones), donde la fenitoína sí tiene una base mecanística sólida, aunque como opción de segunda línea o histórica; no es evidencia biológica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Revisión | Expert Review of Neurotherapeutics | Revisión de los múltiples tratamientos médicos y quirúrgicos de la neuralgia del trigémino; no trata neoplasias del nervio |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Serie de casos | Anales Españoles de Pediatría | Experiencia con 14 casos de síndrome de Sturge-Weber, con su evolución y respuesta terapéutica; no aborda la indicación predicha |

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 56245 | FENITOINA RUBIO 50 MG/ML SOLUCIÓN INYECTABLE | SOLUCIÓN INYECTABLE | Laboratorios Rubio S.A. | Comercializada |
| 65372 | FENITOINA ALTAN 50 MG/ ML SOLUCION INYECTABLE | SOLUCIÓN INYECTABLE | Altan Pharmaceuticals Sa | Comercializada |
| 45695 | EPANUTIN 100 mg CAPSULAS DURAS | CÁPSULA DURA | Viatris Healthcare Limited | Comercializada |
| 5970 | SINERGINA 100 mg COMPRIMIDOS | COMPRIMIDO | Faes Farma S.A. | Comercializada |
| 65340 | FENITOINA KERN PHARMA 50 mg/ml SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Kern Pharma S.L. | Revocada |
| 65303 | FENITOINA ACCORD 50 MG/ML SOLUCION INYECTABLE | SOLUCIÓN INYECTABLE | Accord Healthcare S.L.U. | Revocada |

Se muestran las 6 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Hay una sexta autorización (65303, Fenitoína Accord 50 mg/ml solución inyectable), revocada. Todas son de principio activo único; 65340 y 65303 están revocadas.

<!-- review:begin es-lic-20261112-phenytoin-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Hay una sexta autorización vigente (65303, Fenitoína Accord 50 mg/ml solución inyectable) que no se lista por el límite de cinco. Las seis son de principio activo único y están vigentes." Según CIMA (AEMPS), datos del 2026-11-09, están revocadas 65340 (Fenitoína Kern Pharma 50 mg/ml solución inyectable EFG) y 65303 (Fenitoína Accord 50 mg/ml solución inyectable). La tabla de Información de Mercado en España se genera desde el 2026-11-24 por programa a partir de los datos de CIMA (AEMPS) e incluye la autorización 65303. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261112-phenytoin-1 -->

---

## Consideraciones de Seguridad

- **Contraindicaciones / enfermedades de precaución (según el grafo de conocimiento, no el prospecto)**:
  - Cardiovasculares: síndrome de QT largo (incluido el familiar), torsades de pointes, trastornos hipotensivos.
  - Hepáticas: insuficiencia hepática, hepatopatía, enfermedad de la vesícula biliar, coma hepático y encefalopatía hepática.
  - Hematológicas: trombocitopenia, neutropenia, agranulocitosis.
  - Metabólicas: hiperglucemia, diabetes mellitus, cetoacidosis diabética, porfiria (incluida la hereditaria).
  - Otras: enfermedad renal, piouréter, lupus eritematoso sistémico (incluido el pediátrico), trastornos de ansiedad, trastorno neurótico, trastorno distímico, abuso/dependencia de sustancias, apnea del sueño (obstructiva), síndrome de hipoventilación central congénita y síndrome de Haddad.
- **Interacciones farmacológicas**: la consulta se completó y solo registró una relación farmacológica, con el canal Nav1.2 (SCN2A) como diana. No se identificaron interacciones con otros fármacos.
- La literatura recuperada para otras indicaciones describe reacciones adversas como trombocitopenia, hiperglucemia, cetoacidosis diabética y empeoramiento de porfiria aguda intermitente, coherentes con la lista anterior.

Las advertencias y contraindicaciones del prospecto de la AEMPS no estaban disponibles en los datos compilados; consulte el prospecto para la información de seguridad oficial.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para neoplasia del nervio trigémino carece de ensayos clínicos, de literatura directa y de un mecanismo antitumoral plausible (nivel L5). La puntuación alta procede del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, como la neuralgia del trigémino, no evidencia biológica.

**Para avanzar se necesita:**
- Descartar esta indicación como candidata antitumoral, salvo que aparezca evidencia preclínica o clínica específica.
- Considerar reorientar el análisis hacia la **neuralgia del trigémino**, donde existen guías (EAN 2019), revisiones y estudios observacionales con fenitoína intravenosa (nivel L3, aunque no supera a carbamazepina/oxcarbazepina de primera línea); requeriría una comparación directa con los tratamientos actuales.
- Obtener los datos del mecanismo de acción detallados (DrugBank).
- Descargar y analizar el prospecto de la AEMPS para completar las advertencias y contraindicaciones oficiales (bloqueante para el cribado de seguridad).
- Verificar los textos de indicación aprobada en las autorizaciones españolas, que aparecen vacíos.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Autorizaciones vigentes: 6 → 4 (65340 y 65303 revocadas) | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Extended Phenytoin Sodium (phenytoin sodium) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=363cd347-d25e-42b9-9ce7-30642f3cb353) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


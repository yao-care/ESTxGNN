---
layout: default
title: Phenytoin
parent: Solo predicción del modelo (L5)
nav_order: 634
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
monitor_inn: "Phenytoin"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
description: "Phenytoin: nueva indicación predicha, Neoplasia del nervio trigémino (trigeminal nerve neoplasm) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
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
| Estado de Mercado en España | Comercializado (registros vigentes: 4 de 6) |
| Número de Autorizaciones | 6 (vigentes: 4) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la fenitoína bloquea de forma dependiente del uso los canales de sodio dependientes de voltaje (entre ellos Nav1.2, codificado por SCN2A), lo que estabiliza las membranas neuronales y limita la descarga repetitiva de alta frecuencia. Su eficacia en la epilepsia está bien establecida.

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

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 56245 | Fenitoína Rubio 50 mg/ml solución inyectable | Solución inyectable | No disponible |
| 65372 | Fenitoína Altan 50 mg/ml solución inyectable | Solución inyectable | No disponible |
| 65340 | Fenitoína Kern Pharma 50 mg/ml solución inyectable EFG | Solución inyectable | No disponible |
| 45695 | Epanutin 100 mg cápsulas duras | Cápsula dura | No disponible |
| 5970 | Sinergina 100 mg comprimidos | Comprimido | No disponible |

Hay una sexta autorización vigente (65303, Fenitoína Accord 50 mg/ml solución inyectable) que no se lista por el límite de cinco. Las seis son de principio activo único y están vigentes.

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


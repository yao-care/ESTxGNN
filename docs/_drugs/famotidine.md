---
layout: default
title: Famotidine
parent: Solo predicción del modelo (L5)
nav_order: 325
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
monitor_inn: "Famotidine"
predicted_indications: ["duodenal obstruction", "abnormality of glucagon secretion", "multiple endocrine neoplasia", "acne (disease)"]
description: "Famotidine: nueva indicación predicha, Duodenal obstruction (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Famotidine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Famotidine: Duodenal obstruction
{: .text-alpha }

## Resumen en Una Frase

Famotidina es un antagonista de los receptores H2 de histamina, utilizado originalmente para tratar la úlcera gástrica y duodenal, el reflujo gastroesofágico y otros trastornos de hipersecreción ácida.
El modelo TxGNN predice que podría ser efectiva para el **reflujo duodenogástrico**, pero la evidencia es limitada: **ningún ensayo clínico registrado** y **2 publicaciones** relacionadas.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Duodenal obstruction |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 9 de 9) |
| Número de Autorizaciones | 9 (vigentes: 9) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, famotidina es un antagonista del receptor H2 que reduce la secreción de ácido gástrico. Su eficacia en úlcera gástrica y duodenal, reflujo gastroesofágico y esofagitis está comprobada, y mecanísticamente podría ser aplicable al reflujo duodenogástrico.

La relación entre la indicación original y la nueva es de vecindad mecanística. Al disminuir la acidez gástrica, famotidina podría reducir el daño de la mucosa causado por el contenido duodenal refluido. Es probable que el alto puntaje de TxGNN refleje en gran parte este solapamiento con las indicaciones ya aprobadas (reflujo gastroesofágico y esofagitis).

Hay que tener presente una limitación importante: famotidina **no actúa directamente sobre el reflujo biliar**, que es el componente central del reflujo duodenogástrico. Su beneficio sería, por tanto, sintomático y de protección de la mucosa, no un tratamiento de la causa.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12532466](https://pubmed.ncbi.nlm.nih.gov/12532466/) | 2003 | Estudio clínico (pacientes críticos) | World Journal of Gastroenterology | Investiga el efecto de famotidina sobre el reflujo gastroesofágico y duodeno-gastro-esofágico en pacientes críticos, así como sus posibles mecanismos y los factores asociados al reflujo |
| [16259441](https://pubmed.ncbi.nlm.nih.gov/16259441/) | 2004 | Estudio clínico / revisión | Eksperimental'naia i klinicheskaia gastroenterologiia | Evalúa famotidina 20 mg dos veces al día en etapas tempranas de la enfermedad por reflujo gastroduodenal (grados 0 y 1 de la escala de Savary-Miller modificada), con valoración clínica y endoscópica |

Los resúmenes disponibles describen los objetivos de los estudios, pero no sus resultados cuantitativos.

---

## Información de Mercado en España

Famotidina está comercializada en España con 9 autorizaciones vigentes, todas de monofármaco. A continuación se listan las 5 principales. Los textos de indicación aprobada no están disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 63319 | Famotidina Cinfa 20 mg comprimidos recubiertos con película EFG | Comprimido recubierto |
| 66094 | Famotidina Normon 40 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 63713 | Famotidina Aristo 40 mg comprimidos EFG | Comprimido |
| 63317 | Famotidina Cinfa 40 mg comprimidos recubiertos con película EFG | Comprimido recubierto |
| 62090 | Pepcid 10 mg comprimidos recubiertos | Comprimido recubierto |

---

## Consideraciones de Seguridad

- **Contraindicaciones / enfermedades de precaución (según el grafo de conocimiento, no según el prospecto):** enfermedad renal y función renal alterada, enfermedad hepática, enfermedad de la vesícula biliar, sarcoidosis, hiperparatiroidismo, hipercalcemia, nefrolitiasis y nefrocalcinosis, trastornos del metabolismo del fósforo, diarrea, estreñimiento, lesiones óseas metastásicas líticas y cáncer o neoplasia gástrica (incluidos adenocarcinoma difuso, linitis plástica y carcinoma gástrico).
- **Interacciones farmacológicas:** la consulta no identificó interacciones medicamentosas. Solo se registraron las dianas farmacológicas de famotidina (receptor H2 y TAS2R31).

Consultar el prospecto para la información de seguridad oficial.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos registrados y la literatura es escasa, con solo dos estudios clínicos, sin resultados cuantitativos disponibles.

**Para avanzar se necesita:**
- Revisar los textos completos de los dos estudios (PMID 12532466 y 16259441) para conocer sus resultados y su calidad metodológica.
- Obtener datos detallados del mecanismo de acción.
- Diseñar o localizar ensayos controlados en reflujo duodenogástrico, con comparadores como inhibidores de la bomba de protones.
- Obtener las advertencias, contraindicaciones e indicaciones aprobadas del prospecto de la AEMPS.
- Aclarar el valor adicional frente al uso ya aprobado en reflujo gastroesofágico y esofagitis.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


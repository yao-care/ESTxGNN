---
layout: default
title: Nitrendipine
parent: Solo predicción del modelo (L5)
nav_order: 571
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Nitrendipine: nueva indicación predicha, Migraña (trastorno migrañoso) (nivel de evidencia L5). Indicación original: Hipertensión arterial de leve a moderada (según la información farmac…"
monitor_inn: "nitrendipine"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "pulmonary hypertension"]
---

# Nitrendipine
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

# Nitrendipino: De Hipertensión Arterial a Migraña

## Resumen en Una Frase

Nitrendipino es un antagonista del calcio de tipo dihidropiridina, utilizado en el tratamiento de la hipertensión de leve a moderada.
El modelo TxGNN predice que podría ser efectivo para **migraña (trastorno migrañoso)**,
pero **no hay ensayos clínicos** y solo **3 publicaciones** de carácter general, por lo que la predicción carece de respaldo directo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial de leve a moderada (según la información farmacológica compilada; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Migraña (trastorno migrañoso) |
| Puntaje de Predicción TxGNN | 99,42 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Nitrendipino bloquea los canales de calcio de tipo L (dihidropiridina), lo que relaja el músculo liso vascular y reduce la presión arterial. Los datos compilados lo relacionan además con otros canales de calcio dependientes de voltaje (Cav1.1 a Cav1.4) y con el canal KCa3.1. No se dispone de un texto detallado sobre el mecanismo de acción, por lo que esta descripción se basa en la clase farmacológica.

La relación con la migraña es de tipo clase: otros bloqueadores de canales de calcio, como la flunarizina, se usan en profilaxis migrañosa, y la excitabilidad neuronal y los mecanismos vasomotores podrían intervenir. Sin embargo, no hay datos de nitrendipino específicos para migraña y el razonamiento no es propio del fármaco.

Las dos publicaciones más afines con el fármaco son revisiones generales (interacciones con pomelo, dihidropiridinas de segunda generación), y la tercera es un caso de migraña abdominal en adultos que no evalúa nitrendipino. Ninguna aporta evidencia directa.

### Otras predicciones del modelo (contexto)

| Indicación predicha | Puntaje TxGNN | Nivel | Observación |
|------|------|------|------|
| Migraña con aura del tronco encefálico | 99,29 % | L5 | Sin ensayos ni literatura; subtipo raro, no verificable |
| Hipertensión pulmonar | 99,14 % | L3 | Estudios hemodinámicos pequeños y antiguos (1986-1992) y datos preclínicos |
| Angina de Prinzmetal | 99,10 % | L3 | Estudio pequeño no controlado (1991); uso coherente con la clase |

Las dos últimas cuentan con más respaldo que la migraña, aunque ambas siguen siendo preguntas de investigación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para migraña.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15449971](https://pubmed.ncbi.nlm.nih.gov/15449971/) | 2004 | Revisión | Am J Cardiovasc Drugs | Interacciones del zumo de pomelo con fármacos cardiovasculares (inhibición de CYP3A4 y aumento de biodisponibilidad); no aborda migraña |
| [3319491](https://pubmed.ncbi.nlm.nih.gov/3319491/) | 1987 | Revisión | Drugs | Dihidropiridinas de segunda generación (incluido nitrendipino): selectividad vascular e indicaciones clínicas |
| [9760558](https://pubmed.ncbi.nlm.nih.gov/9760558/) | 1998 | Reporte de caso | Neurol Neurochir Pol | Migraña abdominal en una mujer adulta de 35 años; no evalúa nitrendipino |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 58172 | Nitrendipino Stada 20 mg comprimidos EFG | Comprimido | No disponible en los datos compilados |
| 64506 | Enit 10 mg/20 mg comprimidos | Comprimido | No disponible en los datos compilados |
| 64505 | Eneas 10 mg/20 mg comprimidos | Comprimido | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: no se identificaron interacciones fármaco-fármaco clínicas. Los 5 registros compilados describen interacciones con dianas farmacológicas (canales KCa3.1, Cav1.1, Cav1.2, Cav1.3 y Cav1.4), coherentes con su acción como bloqueador de canales de calcio.
- La literatura revisada señala que el zumo de pomelo puede aumentar la biodisponibilidad oral de dihidropiridinas por inhibición de CYP3A4.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para migraña se apoya solo en el modelo (L5), sin ensayos clínicos ni literatura específica de nitrendipino, y el razonamiento mecanístico es de clase. Entre las predicciones, hipertensión pulmonar y angina de Prinzmetal tienen más respaldo (L3), pero también son preguntas de investigación.

**Para avanzar se necesita:**
- Revisión del prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas), que no estaba disponible.
- Datos detallados del mecanismo de acción del fármaco.
- Estudios preclínicos o clínicos de nitrendipino en migraña, o una comparación con bloqueadores de calcio usados en profilaxis (p. ej., flunarizina).
- Si se desea priorizar, evaluar primero hipertensión pulmonar y angina de Prinzmetal, donde existen datos específicos de nitrendipino.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


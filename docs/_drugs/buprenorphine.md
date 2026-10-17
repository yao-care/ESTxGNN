---
layout: default
title: Buprenorphine
parent: Evidencia moderada (L3-L4)
nav_order: 125
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-14
description: "Buprenorphine: nueva indicación predicha, Porfiria aguda intermitente (nivel de evidencia L4). Indicación original: Dependencia de opioides (según el grafo de conocimiento"
monitor_inn: "Buprenorphine"
predicted_indications: ["acute intermittent porphyria", "lingual-facial-buccal dyskinesia", "chronic tic disorder", "continuous spikes and waves during sleep", "extrapyramidal and movement disease", "benign shuddering attacks"]
---

# Buprenorphine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **6** 
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

# Buprenorfina: De Dependencia de Opioides a Porfiria Aguda Intermitente

## Resumen en Una Frase

La buprenorfina es un opioide agonista parcial utilizado originalmente para el tratamiento de la dependencia de opioides (y de otras sustancias, incluida la dependencia de morfina).
El modelo TxGNN predice que podría ser efectiva para **porfiria aguda intermitente**, pero **no hay ensayos clínicos** y solo **1 publicación** (un informe de caso de 1993 sobre manejo anestésico), que no demuestra eficacia terapéutica.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dependencia de opioides (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Porfiria aguda intermitente |
| Puntaje de Predicción TxGNN | 99,41% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información farmacológica conocida, la buprenorfina actúa sobre los receptores opioides μ (OPRM1) y κ (OPRK1), y su eficacia en la dependencia de opioides está comprobada.

Sin embargo, **no se ha establecido un vínculo mecanístico directo** con la porfiria aguda intermitente. La única publicación recuperada describe el manejo anestésico de una paciente con esta enfermedad; trata de la seguridad de los fármacos durante la cirugía, no del tratamiento de la enfermedad. El puntaje tan alto del modelo (0,994) es solo una predicción computacional y no constituye evidencia clínica.

Antes de cualquier consideración, sería necesario verificar de forma independiente el perfil de seguridad de la buprenorfina en porfiria, es decir, si es porfirinogénica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Reporte de caso | Masui (Japanese Journal of Anesthesiology) | Manejo anestésico de una mujer de 40 años con sospecha de porfiria aguda intermitente sometida a histerectomía radical por tumor ovario maligno; trata de seguridad perioperatoria, no de eficacia terapéutica |

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de principio activo único). Los textos de indicación aprobada no están disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 80670 | Gexana 52,5 microgramos/hora parche transdérmico EFG | Parche transdérmico | No disponible |
| 82322 | Buprenorfina Sandoz Farmacéutica 70 microgramos/hora parches transdérmicos EFG | Parche transdérmico | No disponible |
| 1191369001 | Sixmo 74,2 mg implante | Implante | No disponible |
| 1181336002 | Buvidal 16 mg solución inyectable de liberación prolongada | Solución inyectable de liberación prolongada | No disponible |
| 70804 | Feliben 35 microgramos/hora parches transdérmicos | Parche transdérmico | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones asociadas en el grafo de conocimiento** (no proceden del texto del prospecto): síndrome de QT largo (incluido el familiar) y torsades de pointes, hipotensión ortostática, enfermedad pulmonar obstructiva crónica, insuficiencia respiratoria, enfermedad hepática (incluidas las infecciones crónicas por virus de la hepatitis B y C), enfermedad de la vesícula biliar, insuficiencia suprarrenal/enfermedad de Addison, hipotiroidismo/mixedema, hiperplasia benigna de próstata, íleo paralítico y obstrucción intestinal, hipertensión intracraneal/pseudotumor cerebral, estenosis uretral, y trastornos por uso de sustancias.
- **Farmacología**: la buprenorfina interactúa con los receptores opioides μ y κ humanos.
- Para las advertencias principales, contraindicaciones oficiales e interacciones medicamentosas, consultar el prospecto.

Además, en las otras indicaciones predichas se señalan preocupaciones específicas: los opioides pueden reducir el umbral convulsivo (relevante en la encefalopatía epiléptica con espigas-onda continuas durante el sueño) y la relación beneficio-riesgo sería desfavorable en condiciones benignas y autolimitadas como los episodios de estremecimiento benigno.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo computacional y en un informe de caso sobre anestesia que no aborda el tratamiento de la enfermedad. No hay ensayos clínicos ni vínculo mecanístico establecido, y la seguridad en porfiria no está verificada.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la buprenorfina y análisis de su vínculo con la fisiopatología de la porfiria aguda intermitente
- Verificación de si la buprenorfina es porfirinogénica (bases de datos de seguridad en porfiria)
- Obtención y análisis del prospecto de la AEMPS (advertencias y contraindicaciones oficiales)
- Estudios preclínicos o series de casos que sugieran un posible beneficio terapéutico
- Revisión de los demás candidatos predichos (discinesia lingual-facial-bucal, trastorno de tics crónico, entre otros), todos con evidencia igualmente débil (L4–L5) y también en estado Hold
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


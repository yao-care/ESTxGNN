---
layout: default
title: Tipranavir
parent: Solo predicción del modelo (L5)
nav_order: 798
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tipranavir: nueva indicación predicha, Infección por el virus de la inmunodeficiencia de los simios (nivel de evidencia L5). Indicación original: Infección por VIH / SIDA (según el grafo de conocimie…"
monitor_inn: "TIPRANAVIR"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "benign prostate phyllodes tumor"]
---

# Tipranavir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Tipranavir: De Infección por VIH/SIDA a Infección por el Virus de la Inmunodeficiencia de los Simios

## Resumen en Una Frase

Tipranavir es un inhibidor de la proteasa del VIH-1 no peptídico, utilizado originalmente para el tratamiento de la infección por VIH y el SIDA.
El modelo TxGNN predice que podría ser efectivo para la **infección por el virus de la inmunodeficiencia de los simios (SIV)**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata de una predicción puramente computacional sobre un modelo animal, sin relevancia clínica humana directa.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH / SIDA (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Infección por el virus de la inmunodeficiencia de los simios |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, tipranavir es un inhibidor no peptídico de la proteasa del VIH-1, enzima necesaria para la maduración de las partículas virales. Su eficacia en la infección por VIH resistente a otros tratamientos es conocida.

El SIV es un lentivirus muy cercano al VIH y posee una proteasa homóloga, por lo que existe un fundamento mecanístico plausible. Sin embargo, es un virus de modelos animales y no una indicación clínica humana. El puntaje elevado probablemente refleja la proximidad en la red de conocimiento con la indicación de VIH ya aprobada, más que una oportunidad real de reposicionamiento.

Otras predicciones del modelo (p. ej., síndrome de inmunodeficiencia adquirida felina, el complejo relacionado con el SIDA o el VIH congénito) son variantes de la misma indicación o condiciones veterinarias. Las predicciones en neoplasias benignas y trastornos del neurodesarrollo no tienen vínculo mecanístico identificable y parecen artefactos del grafo de conocimiento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 05315002 | APTIVUS 100 MG/ML SOLUCIÓN ORAL | Solución oral | No disponible en los datos compilados |
| 05315001 | APTIVUS 250 MG CÁPSULAS BLANDAS | Cápsula blanda | No disponible en los datos compilados |

Ambas autorizaciones están vigentes y corresponden a Boehringer Ingelheim International GmbH.

## Consideraciones de Seguridad

- **Contraindicaciones y enfermedades de riesgo (según el grafo de conocimiento, no del prospecto)**: enfermedad y fallo hepático, enfermedad de la vesícula biliar, hiperglucemia, diabetes mellitus, cetoacidosis diabética, infección crónica por virus de la hepatitis B y C, trastornos de la coagulación, hemofilia, hipertrigliceridemia, hiperbilirrubinemia (incluido el síndrome de Gilbert), lesiones/traumatismos, neoplasias cerebrales y hemorragia intracraneal.
- **Interacciones farmacológicas**: se identificaron 100 interacciones; las principales mostradas son:
  - **Mayores**: ácido acetilsalicílico y eluxadolina.
  - **Moderadas**: antidiabéticos (acarbosa, albiglutida, alogliptina, metformina, pioglitazona, canagliflozina, clorpropamida, dapagliflozina, dulaglutida, empagliflozina, linagliptina), loperamida, dexametasona, ácido cólico, claritromicina, óxido de magnesio, eliglustat y metronidazol tópico.
- **Nota contextual**: las predicciones del modelo señalan que tipranavir conlleva advertencias de hepatotoxicidad y hemorragia intracraneal, y que los inhibidores de la proteasa elevan triglicéridos y colesterol. Esto debe confirmarse con el prospecto, ya que las advertencias oficiales no estaban disponibles en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (nivel L5), sin ensayos ni literatura, y el SIV es un virus de modelos animales sin aplicación clínica humana. Además, el perfil de seguridad de tipranavir es exigente (hepatotoxicidad, hemorragia intracraneal, múltiples interacciones), por lo que no hay base para avanzar.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS para obtener advertencias y contraindicaciones oficiales (brecha bloqueante).
- Obtener datos del mecanismo de acción desde DrugBank.
- Definir si existe un interés real en una indicación humana distinta de las ya cubiertas por la indicación de VIH; de lo contrario, descartar las predicciones veterinarias y de modelos animales.
- Reunir estudios preclínicos (actividad frente a la proteasa de SIV) antes de reconsiderar la evaluación.
- Reevaluar las demás predicciones (neoplasias benignas, trastorno del neurodesarrollo) solo si aparece evidencia mecanística independiente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


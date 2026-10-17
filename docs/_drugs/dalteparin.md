---
layout: default
title: Dalteparin
parent: Solo predicción del modelo (L5)
nav_order: 217
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Dalteparin: nueva indicación predicha, Trombofilia por deficiencia de proteína C, autosómica recesiva (nivel de evidencia L5). Indicación original: Embolia pulmonar, coagulación intravascular disemin…"
monitor_inn: "dalteparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive", "primary release disorder of platelets", "pseudo-von Willebrand disease", "atypical hemolytic-uremic syndrome with thrombomodulin anomaly", "neuropathy, painful"]
---

# Dalteparin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Dalteparina: De Embolia Pulmonar a Trombofilia por Deficiencia de Proteína C (Autosómica Recesiva)

## Resumen en Una Frase

Dalteparina es una heparina de bajo peso molecular, utilizada originalmente en indicaciones relacionadas con la embolia pulmonar, la coagulación intravascular diseminada y la púrpura fulminante.
El modelo TxGNN predice que podría ser efectiva para **trombofilia por deficiencia de proteína C, autosómica recesiva**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Embolia pulmonar, coagulación intravascular diseminada, púrpura fulminante (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Trombofilia por deficiencia de proteína C, autosómica recesiva |
| Puntaje de Predicción TxGNN | 99,88 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 9 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone actualmente de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, la dalteparina es una heparina de bajo peso molecular que potencia la acción de la antitrombina e inhibe el factor Xa, reduciendo así la formación de trombos.

La deficiencia de proteína C es un estado de hipercoagulabilidad, y la púrpura fulminante (incluida su forma adquirida), una de las indicaciones originales, se asocia clásicamente con deficiencia grave de proteína C. Esta relación hace biológicamente plausible la predicción. En la práctica clínica ya se utiliza anticoagulación en esta condición, aunque los datos compilados no contienen evidencia específica de dalteparina.

Conviene subrayar que el puntaje de 99,88 % es una predicción computacional sin validación clínica ni bibliográfica en los datos compilados.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se listan 5 de las 9 autorizaciones vigentes (todas de Pfizer S.L.; los textos de indicación aprobada no están disponibles en los datos compilados):

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 58537 | FRAGMIN 5.000 UI/0,2 ml solución inyectable en jeringas precargadas | Solución inyectable en jeringa precargada | No disponible |
| 62155 | FRAGMIN 10.000 UI/0,4 ml solución inyectable en jeringas precargadas | Solución inyectable en jeringa precargada | No disponible |
| 61523 | FRAGMIN 10.000 UI/ml solución inyectable en ampollas | Solución inyectable | No disponible |
| 89772 | FRAGMIN 2.500 UI/ml solución inyectable en viales | Solución inyectable | No disponible |
| 62567 | FRAGMIN 7.500 UI/0,3 ml solución inyectable en jeringas precargadas | Solución inyectable en jeringa precargada | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto del prospecto)**: enfermedades hemorrágicas y de la coagulación (hemofilia, trombocitopenia, trombocitopenia inducida por heparina, trombastenia de Glanzmann, defectos plaquetarios cualitativos, enfermedad hematológica, trastorno de la coagulación sanguínea, déficit de antitrombina III); hemorragia intracraneal e intracerebral; desprendimiento prematuro de placenta; úlcera péptica activa; colitis ulcerosa y enfermedad inflamatoria intestinal; insuficiencia hepática; enfermedad de las vías biliares e ictericia obstructiva; endocarditis infecciosa (incluida la subaguda bacteriana); enfermedades retinianas (retinopatía diabética y retinopatía hipertensiva, retinitis, catarata diabética); osteoporosis (incluida la posmenopáusica); arteriosclerosis obliterante.
- **Interacciones Farmacológicas**: se identificaron 174 interacciones en total. Entre las principales de nivel **Mayor** se encuentran: ácido acetilsalicílico, ibuprofeno, ketorolaco, fondaparinux, abciximab, acalabrutinib, deferasirox, trastuzumab emtansina, ibritumomab tiuxetán y tositumomab (incluido el marcado con I-131). Entre las de nivel **Moderado**: fluvoxamina, fosinopril, sugammadex, fenfluramina, dexfenfluramina, sibutramina y yoduro I-123/I-131. En general, el riesgo principal es el aumento de sangrado al combinar con antiagregantes, AINE y otros anticoagulantes.

Para las advertencias y contraindicaciones del prospecto, consultar la ficha técnica oficial.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene plausibilidad biológica (anticoagulación en un estado de hipercoagulabilidad, relacionado con la púrpura fulminante), pero se apoya solo en el modelo (L5), sin ensayos ni literatura. Además, la información de seguridad del prospecto no está disponible.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), ya que la ausencia de estos datos impide el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisión sistemática de la literatura sobre heparinas de bajo peso molecular en la deficiencia de proteína C y la púrpura fulminante.
- Evaluar la vía de administración y la compatibilidad de formas farmacéuticas con el uso propuesto.
- Valorar el perfil de riesgo hemorrágico en la población diana, dadas las contraindicaciones identificadas.

**Nota sobre otras predicciones evaluadas:** las otras cuatro predicciones de mayor rango (trastorno primario de liberación plaquetaria, pseudoenfermedad de von Willebrand, síndrome hemolítico urémico atípico con anomalía de trombomodulina y neuropatía dolorosa) también tienen nivel L5 y decisión Hold. Las dos primeras de ellas son trastornos hemorrágicos en los que un anticoagulante podría empeorar el sangrado, por lo que probablemente son falsos positivos. El único ensayo asociado a la neuropatía dolorosa (NCT00445328, fase 4, terminado, 84 participantes) es un estudio de profilaxis de tromboembolismo venoso sin relación aparente con la indicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


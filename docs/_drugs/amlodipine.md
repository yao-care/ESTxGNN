---
layout: default
title: Amlodipine
parent: Solo predicción del modelo (L5)
nav_order: 52
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Amlodipine: nueva indicación predicha, Infarto del tronco encefálico (nivel de evidencia L5). Indicación original: Hipertensión arterial (según el grafo de conocimiento"
monitor_inn: "Amlodipine"
predicted_indications: ["brain stem infarction", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "MRI defined brain infarct", "ABri amyloidosis", "intracerebral hemorrhage"]
---

# Amlodipine
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

# Amlodipino: De Hipertensión a Infarto del Tronco Encefálico

## Resumen en Una Frase

Amlodipino es un antagonista del calcio utilizado originalmente para tratar la hipertensión arterial, la angina de Prinzmetal y la prevención de trastornos cerebrovasculares.
El modelo TxGNN predice que podría ser efectivo para el **infarto del tronco encefálico**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta indicación específica; se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles en los datos compilados) |
| Nueva Indicación Predicha | Infarto del tronco encefálico |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada. Según la información farmacológica disponible, amlodipino es un antagonista del calcio de tipo dihidropiridina. Se ha descrito como modulador de la apertura (*gating*) de los canales de calcio dependientes de voltaje (Ca<sub>v</sub>1.2 y Ca<sub>v</sub>1.3), lo que produce vasodilatación y reducción de la presión arterial. Los datos indican además que no existe un objetivo primario claramente definido, por la complejidad de su mecanismo y la escasez de datos de afinidad en humanos.

Amlodipino ya figura, según el grafo de conocimiento, con indicaciones relacionadas con el ictus, la enfermedad cerebrovascular y el infarto cerebral, principalmente a través del control de la presión arterial. El infarto del tronco encefálico es un subtipo anatómico de infarto cerebral, por lo que la predicción es plausible como extensión de una indicación existente más que como un reposicionamiento mecanísticamente novedoso.

Esta lectura es una interpretación de los datos disponibles, no una conclusión respaldada por estudios. Para esta entidad concreta no se recuperó ningún ensayo ni publicación, y la relación de similitud con la indicación original está pendiente de análisis.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para el infarto del tronco encefálico.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para el infarto del tronco encefálico.

## Información de Mercado en España

Amlodipino se comercializa en España como medicamento de un solo principio activo (20 autorizaciones vigentes, ninguna cancelada, ninguna combinación). Todas son comprimidos de administración oral. Se muestran las 5 primeras seleccionadas; los textos de indicación aprobada no figuran en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 59160 | NORVAS 10 mg comprimidos | Comprimido | Viatris Healthcare Limited |
| 90902 | Amlodipino Teva-Ratiopharm 5 mg comprimidos EFG | Comprimido | Teva B.V. |
| 84861 | Amlodipino Bluepharma 5 mg comprimidos EFG | Comprimido | Bluepharma Industria Farmacêutica S.A. |
| 85522 | Amlodipino Mabo 5 mg comprimidos EFG | Comprimido | Mabo Farma S.A. |
| 72814 | Amlodipino Combix 10 mg comprimidos EFG | Comprimido | Laboratorios Combix S.L.U. |

## Consideraciones de Seguridad

No se dispone de advertencias principales ni de contraindicaciones extraídas del prospecto. Consultar el prospecto para esa información.

**Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto de etiqueta; deben verificarse con la ficha técnica):
- Hepáticas y biliares: insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar, pancreatitis.
- Renales: enfermedad renal, piouréter.
- Endocrinas y metabólicas: hipotiroidismo (incluido mixedema e hipotiroidismo congénito), hiperparatiroidismo, osteítis fibrosa, diabetes mellitus, cetoacidosis diabética, hiperuricemia, déficit de potasio.
- Angioedema: adquirido, hereditario (con déficit de C1 inhibidor), no histaminérgico e inducido por bloqueadores del sistema renina-angiotensina-aldosterona.
- Musculares: miopatía, enfermedad muscular esquelética, parálisis periódica familiar.
- Hematológicas e inmunológicas: neutropenia, agranulocitosis, lupus eritematoso sistémico (incluido el pediátrico).
- Cardiovasculares: trastornos hipotensivos.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El puntaje del modelo es muy alto (99.94%), pero no hay ningún ensayo clínico ni publicación específica para el infarto del tronco encefálico (nivel L5). Aunque amlodipino ya se usa en prevención de ictus mediante control de la presión arterial, no hay evidencia propia de beneficio en esta entidad.

**Para avanzar se necesita:**
- Una revisión de la literatura y de registros de ensayos específica para infarto del tronco encefálico e infarto cerebral isquémico, para confirmar si existe evidencia en estos subtipos.
- Datos del mecanismo de acción desde DrugBank, y análisis de similitud entre la indicación original y la predicha.
- Obtención y análisis del prospecto de la AEMPS (advertencias y contraindicaciones), requisito previo para cualquier evaluación de seguridad.
- Confirmación de si el uso previsto (prevención secundaria mediante control de la presión arterial) aporta algo más allá de la indicación ya existente.

**Nota sobre otras predicciones:** entre las demás indicaciones predichas, la **hemorragia intracerebral** tiene la evidencia más sólida (nivel L1). Incluye el ensayo de fase 3 TRIDENT (NCT02699645, completado, 1671 participantes) y su publicación de 2026 en *The New England Journal of Medicine*. Esa evidencia respalda una estrategia de combinación de tres antihipertensivos a dosis bajas en una sola píldora, no amlodipino en monoterapia, y no es extrapolable directamente al infarto del tronco encefálico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


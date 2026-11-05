---
layout: default
title: Terbutaline
parent: Solo predicción del modelo (L5)
nav_order: 780
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-05
monitor_inn: "Terbutaline"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome"]
description: "Terbutaline: nueva indicación predicha, malformación respiratoria (respiratory malformation) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Terbutaline
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Terbutaline: malformación respiratoria (respiratory malformation)
{: .text-alpha }

## Resumen en Una Frase

Terbutalina es un agonista de los receptores beta-adrenérgicos (principalmente beta-2), utilizado como broncodilatador en enfermedades obstructivas reversibles de las vías respiratorias.
El modelo TxGNN predice que podría ser útil para **malformación respiratoria (respiratory malformation)**, pero **no hay estudios que lo evalúen directamente**: solo hay **1 ensayo clínico** genérico y publicaciones sobre asma, bronquitis y otros temas relacionados de forma indirecta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | malformación respiratoria (respiratory malformation) |
| Puntaje de Predicción TxGNN | 0.9952 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 2) |
| Número de Autorizaciones | 2 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información farmacológica conocida, la terbutalina actúa sobre los receptores beta-1 y beta-2 adrenérgicos (genes ADRB1 y ADRB2), y se emplea para prevenir y revertir el broncoespasmo en enfermedad obstructiva reversible de las vías respiratorias.

El agonismo beta-2 podría aliviar la broncoconstricción reversible que acompaña a algunas anomalías estructurales de las vías aéreas, pero no corregiría la malformación en sí. El puntaje elevado del modelo (0,9952) probablemente refleja la cercanía de la red con términos de enfermedad respiratoria y no un mecanismo específico de esta enfermedad.

Por tanto, la predicción debe entenderse como una hipótesis del modelo, sin respaldo directo en estudios reales.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Reclutando | 5000 | Programa general de farmacocinética, farmacodinamia y seguridad de fármacos poco estudiados en niños; no es específico de malformación respiratoria y no tiene criterio de eficacia para esta enfermedad |

## Evidencia de Literatura

Ninguna publicación estudia directamente la malformación respiratoria. Las siguientes son las más cercanas temáticamente:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3281307](https://pubmed.ncbi.nlm.nih.gov/3281307/) | 1988 | ECA | Thorax | Adrenalina subcutánea frente a terbutalina en asma aguda grave (20 pacientes) |
| [1629507](https://pubmed.ncbi.nlm.nih.gov/1629507/) | 1992 | ECA | J Allergy Clin Immunol | Budesonida inhalada frente a terbutalina sobre la inflamación de las vías aéreas en asma de reciente diagnóstico |
| [42303000](https://pubmed.ncbi.nlm.nih.gov/42303000/) | 2026 | Cohorte | Respiratory Medicine | Evaluación de síntomas, función pulmonar e imagen en lactantes con bronquiolitis obliterante postinfecciosa |
| [1620986](https://pubmed.ncbi.nlm.nih.gov/1620986/) | 1992 | Observacional | Respiration | Reversibilidad aguda de la impedancia respiratoria anormal con terbutalina inhalada en bronquitis crónica |
| [12061354](https://pubmed.ncbi.nlm.nih.gov/12061354/) | 2002 | Observacional | Acta Paediatrica | Estenosis de vías aéreas centrales en escolares y diagnóstico diferencial con asma |
| [19793774](https://pubmed.ncbi.nlm.nih.gov/19793774/) | 2009 | Revisión/Hipótesis | Toxicol Ind Health | Hipótesis sobre terbutalina, moho y autismo; se refiere a señales de seguridad, no a beneficio |
| [11813927](https://pubmed.ncbi.nlm.nih.gov/11813927/) | 2001 | Reporte de caso | Cardiology in the Young | Terbutalina en bloqueo cardíaco completo fetal; no relacionado con la indicación predicha |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 52616 | TERBASMIN 0,3 mg/ml SOLUCIÓN ORAL | Solución oral | No disponible en los datos compilados |
| 58859 | TERBASMIN TURBUHALER 500 microgramos/inhalación POLVO PARA INHALACIÓN | Polvo para inhalación | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones o condiciones de precaución (relaciones registradas en bases de datos farmacológicas, no texto de prospecto)**: hipertensión, epilepsia, hiperglucemia, deficiencia de potasio, diabetes mellitus, cetoacidosis diabética, paro cardíaco súbito, enfermedad de la conducción cardíaca, insuficiencia respiratoria, hipertiroidismo, enfermedad de Graves, tirotoxicosis, edema pulmonar, isquemia miocárdica, enfermedad coronaria y desprendimiento de placenta.
- **Interacciones farmacológicas**: no se registraron interacciones con otros fármacos; solo la unión farmacológica a los receptores beta-1 y beta-2 adrenérgicos.

Consultar el prospecto para el resto de la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo: no hay ensayos ni publicaciones que estudien la malformación respiratoria directamente, y el único ensayo registrado es un programa farmacocinético general. El mecanismo beta-2 no corregiría la malformación estructural.

**Para avanzar se necesita:**
- Estudios clínicos o preclínicos que evalúen directamente la terbutalina en malformación respiratoria
- Datos detallados del mecanismo de acción y su vínculo con la fisiopatología de esta enfermedad
- Revisión de advertencias y contraindicaciones del prospecto oficial
- Evaluación de la compatibilidad de las vías de administración disponibles con la población afectada

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


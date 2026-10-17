---
layout: default
title: Asenapine
parent: Solo predicción del modelo (L5)
nav_order: 69
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Asenapine: nueva indicación predicha, Distrofia retiniana con o sin anomalías extraoculares (nivel de evidencia L5). Indicación original: Trastorno bipolar maníaco, trastorno bipolar y esquizofrenia"
monitor_inn: "Asenapine"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "congenital disorder of glycosylation with defective fucosylation", "hydranencephaly (disease)", "syndromic myopia", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "myopia 26, X-linked, female-limited", "atypical glycine encephalopathy"]
---

# Asenapine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Asenapina: De Trastorno Bipolar y Esquizofrenia a Distrofia Retiniana con o sin Anomalías Extraoculares

## Resumen en Una Frase

Asenapina es un antipsicótico atípico, utilizado originalmente para el tratamiento del trastorno bipolar (episodios maníacos) y la esquizofrenia.
El modelo TxGNN predice que podría ser efectivo para **distrofia retiniana con o sin anomalías extraoculares**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno bipolar maníaco, trastorno bipolar y esquizofrenia (según el grafo de conocimiento; los registros de AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Distrofia retiniana con o sin anomalías extraoculares |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información farmacológica compilada, asenapina actúa como antagonista de múltiples receptores: serotoninérgicos (5-HT1A, 1B, 1D, 1E y 2A), dopaminérgico D2 e histaminérgico H1. Este perfil es coherente con su eficacia antimaníaca y antipsicótica.

Sin embargo, los datos disponibles **no respaldan un vínculo mecanístico** con la distrofia retiniana hereditaria. Esta enfermedad es una degeneración de origen genético de las células de la retina, y no hay evidencia de que el antagonismo dopaminérgico o serotoninérgico intervenga en sus vías patológicas. La relación con las indicaciones originales (trastornos psiquiátricos) tampoco se ha podido establecer.

El puntaje alto (99.77%) refleja únicamente una asociación calculada en el grafo de conocimiento, sin ensayos, estudios preclínicos ni literatura que la sustenten. Debe interpretarse como una hipótesis sin validar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 8 autorizaciones vigentes (todas de medicamento con un único principio activo, titular Organon N.V.). Los registros no incluyen texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 10640005IP2 | SYCREST 10 MG comprimidos sublinguales | Comprimido sublingual |
| 10640002IP2 | SYCREST 5 MG comprimidos sublinguales | Comprimido sublingual |
| 10640002 | SYCREST 5 MG comprimidos sublinguales | Comprimido sublingual |
| 10640005IP3 | SYCREST 10 MG comprimidos sublinguales | Comprimido sublingual |
| 10640005IP | SYCREST 10 MG comprimidos sublinguales | Comprimido sublingual |

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (según el grafo de conocimiento, no del prospecto):** asenapina figura asociada a contraindicación o precaución en las siguientes condiciones:
  - **Cardiovasculares:** síndrome de QT largo (incluida la forma familiar), torsades de pointes, hipotensión ortostática, síndrome de taquicardia postural ortostática, infarto de miocardio, trombosis coronaria, isquemia miocárdica, enfermedad arterial coronaria.
  - **Cerebrovasculares y neurológicas:** ictus, enfermedad cerebrovascular, infarto cerebral, epilepsia, atrofia multisistémica, síndrome neuroléptico maligno.
  - **Hematológicas:** neutropenia (incluida la neutropenia congénita grave), agranulocitosis, leucopenia, hematopoyesis cíclica, hemoglobinopatía.
  - **Metabólicas y hepáticas:** hiperglucemia, diabetes mellitus, cetoacidosis diabética, obesidad (incluida la monogénica), deficiencia de potasio, insuficiencia hepática.
- **Interacciones farmacológicas:** los 7 registros disponibles describen las dianas receptoras de asenapina (5-HT1A, 5-HT1B, 5-HT1D, 5-HT1E, 5-HT2A, D2 y H1), no interacciones con otros fármacos. No hay datos de interacciones clínicas específicas con otros medicamentos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para distrofia retiniana se basa solo en el puntaje del modelo (nivel L5): no hay ensayos, literatura ni vínculo mecanístico plausible. Además, el perfil de riesgo cardiovascular, hematológico y metabólico de asenapina haría difícil justificar su uso en una enfermedad genética sin respaldo.

**Para avanzar se necesita:**
- Datos oficiales del mecanismo de acción (MOA) y una hipótesis biológica que conecte los receptores de asenapina con las vías de la degeneración retiniana
- Estudios preclínicos (modelos celulares o animales de distrofia retiniana) que respalden la hipótesis
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones oficiales), actualmente pendiente
- Evaluación de viabilidad de la vía de administración, ya que la forma disponible es sublingual y no ocular
- Nota adicional: entre las demás predicciones del modelo, "trastorno afectivo mayor" coincide con la indicación bipolar ya aprobada. Tiene respaldo de literatura (incluido un metaanálisis de ECA en manía aguda, PMID 23719049), pero es prácticamente una indicación existente y no un reposicionamiento real.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


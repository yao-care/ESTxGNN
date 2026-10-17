---
layout: default
title: Ambrisentan
parent: Evidencia moderada (L3-L4)
nav_order: 47
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Ambrisentan: nueva indicación predicha, Malformación arteriovenosa pulmonar (nivel de evidencia L4). Indicación original: Hipertensión arterial pulmonar (según el grafo de conocimiento"
monitor_inn: "ambrisentan"
predicted_indications: ["pulmonary arteriovenous malformation (disease)", "malformation syndrome with odontal and/or periodontal component", "hypotrichosis simplex of the scalp", "hypertrichosis (disease)", "syndrome with a Dandy-Walker malformation as major feature"]
---

# Ambrisentan
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Ambrisentan: De Hipertensión Arterial Pulmonar a Malformación Arteriovenosa Pulmonar

## Resumen en Una Frase

Ambrisentan es un antagonista selectivo del receptor de endotelina tipo A, utilizado originalmente para el tratamiento de la hipertensión arterial pulmonar (HAP).
El modelo TxGNN predice que podría ser efectivo para **Malformación Arteriovenosa Pulmonar**, pero la evidencia es muy limitada: **0 ensayos clínicos** y solo **1 publicación** (un reporte de caso de HAP en un paciente con telangiectasia hemorrágica hereditaria, que no demuestra beneficio en la malformación arteriovenosa en sí).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial pulmonar (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Malformación arteriovenosa pulmonar |
| Puntaje de Predicción TxGNN | 99.41% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Ambrisentan es un antagonista del receptor de endotelina tipo A. La endotelina-1 media la vasoconstricción y el remodelado vascular, y por eso el fármaco se utiliza en la HAP. Los datos compilados no incluyen una descripción detallada del mecanismo de acción en la ficha del fármaco, por lo que este análisis se basa en la clase farmacológica conocida.

La relación con la nueva indicación es débil. La única publicación disponible describe un caso de HAP coexistente con telangiectasia hemorrágica hereditaria (HHT): es una observación a nivel de caso, no evidencia de beneficio en la malformación arteriovenosa pulmonar. Mecanísticamente, la señalización de endotelina podría ser relevante en la enfermedad vascular pulmonar asociada a HHT.

Además, hay un motivo de cautela: las malformaciones arteriovenosas pulmonares son cortocircuitos estructurales que se tratan habitualmente mediante embolización, y en teoría los vasodilatadores podrían empeorar el cortocircuito o la hipoxemia. El puntaje alto del modelo debe interpretarse con prudencia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Reporte de caso | World Journal of Clinical Cases | Caso de HAP en un paciente con telangiectasia hemorrágica hereditaria, con análisis genético familiar; busca crear conciencia sobre esta multimorbilidad. No evalúa ambrisentan en la malformación arteriovenosa pulmonar. |

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de principio activo único). El texto de indicación aprobada no figura en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 08451002 | Volibris 5 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 08451004 | Volibris 10 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 84715 | Ambrisentan Sandoz 5 mg EFG | Comprimido recubierto con película | No disponible |
| 84716 | Ambrisentan Sandoz 10 mg EFG | Comprimido recubierto con película | No disponible |
| 84582 | Ambrisentan Accord 10 mg EFG | Comprimido recubierto con película | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): insuficiencia cardíaca congestiva, anemia, anemia macrocítica y enfermedad venooclusiva pulmonar.
- **Interacciones farmacológicas**: se identificaron 112 interacciones en total. Entre las de nivel moderado figuran canagliflozina, dapagliflozina, empagliflozina, ertugliflozina, eliglustat y naltrexona. Entre las de nivel menor, claritromicina, miconazol y omeprazol.
- **Consideraciones adicionales**: según el análisis de los candidatos, ambrisentan es teratogénico, por lo que debe evitarse en contextos de desarrollo o embarazo. Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no están disponibles en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya en un único reporte de caso sin evidencia de eficacia en la malformación arteriovenosa pulmonar, y existe un riesgo teórico de que la vasodilatación empeore el cortocircuito o la hipoxemia. No hay ensayos clínicos que respalden la dirección propuesta.

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones del prospecto de la AEMPS (brecha de datos bloqueante para el cribado de seguridad).
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisión sistemática de literatura preclínica y clínica sobre antagonistas de endotelina en HHT y malformaciones arteriovenosas pulmonares.
- Evaluación de riesgo fisiológico (cortocircuito, hipoxemia) antes de plantear cualquier estudio exploratorio.

**Nota sobre otras predicciones:** la candidata con mayor soporte es la HAP asociada a enfermedad del tejido conectivo (nivel L2, con un ensayo de Fase 2 de 38 pacientes, un estudio de Fase 4 de 25 pacientes, un metaanálisis y revisiones sistemáticas). Sin embargo, este subtipo ya está dentro de la indicación existente de HAP, por lo que no constituye un reposicionamiento propiamente dicho. Las predicciones sobre hipotricosis, hipertricosis, síndromes de malformación dental y síndrome de Dandy-Walker carecen de respaldo mecanístico y probablemente son artefactos del grafo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


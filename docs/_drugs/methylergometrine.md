---
layout: default
title: Methylergometrine
parent: Solo predicción del modelo (L5)
nav_order: 514
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Methylergometrine: nueva indicación predicha, Hipertricosis (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (las autorizaciones no incluyen…"
monitor_inn: "methylergometrine"
predicted_indications: ["hypertrichosis (disease)", "pulmonary hypertension", "migraine disorder", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "kyphoscoliotic heart disease", "migraine with brainstem aura", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Methylergometrine
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

# Metilergometrina: De Indicación Original No Especificada a Hipertricosis

## Resumen en Una Frase

Metilergometrina es un alcaloide semisintético del cornezuelo del centeno con actividad uterotónica, comercializado en España como Methergin (comprimidos e inyectable). No se dispone del texto de la indicación aprobada en las autorizaciones.
El modelo TxGNN predice que podría ser efectiva para **hipertricosis**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (las autorizaciones no incluyen texto de indicación) |
| Nueva Indicación Predicha | Hipertricosis |
| Puntaje de Predicción TxGNN | 99,87% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la metilergometrina es un alcaloide semisintético del cornezuelo que actúa como agonista de receptores serotoninérgicos 5-HT2 y alfa-adrenérgicos, con actividad uterotónica.

**La predicción no resulta razonable desde el punto de vista biológico.** No se ha establecido ningún vínculo mecanístico entre estas acciones y la regulación del crecimiento del folículo piloso. El puntaje elevado procede únicamente de la proximidad en el grafo de conocimiento. Además, la hipertricosis es un efecto adverso conocido de otros fármacos (por ejemplo, minoxidil y ciclosporina), por lo que un papel terapéutico es poco plausible y la dirección del efecto es incierta.

### Otras predicciones del modelo (para contexto)

| Posición | Indicación predicha | Puntaje TxGNN | Nivel | Valoración |
|------|------|------|------|------|
| 2 | Hipertensión pulmonar | 99,86% | L5 | Sin respaldo; los agonistas 5-HT2B derivados del cornezuelo se asocian a hipertensión arterial pulmonar y valvulopatía, por lo que existe una señal de seguridad |
| 3 | Migraña | 99,84% | L4 | Biológicamente plausible (la metilergometrina es el metabolito activo de la metisergida), pero con barreras de seguridad cardiovascular y fibrótica |
| 4 | Hipertricosis universal congénita tipo Ambras | 99,82% | L5 | Sin fundamento mecanístico |
| 9 | Migraña con aura del tronco encefálico | 99,77% | L5 | Perfil de seguridad desfavorable por riesgo isquémico teórico |

La migraña (posición 3) es la única predicción con alguna plausibilidad biológica y literatura indirecta, aunque los fármacos disponibles actualmente (triptanes, gepantes, anticuerpos anti-CGRP) son más seguros.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para hipertricosis.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 78949 | METHERGIN 0,125 MG COMPRIMIDOS RECUBIERTOS | Comprimido recubierto | No disponible |
| 25658 | METHERGIN 0,2 mg/ml SOLUCIÓN INYECTABLE | Solución inyectable | No disponible |

---

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación según el grafo de conocimiento** (no proceden del prospecto): hipertensión, epilepsia, enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, ictus y trastornos cerebrovasculares, infarto cerebral, arteriosclerosis obliterante y síndrome HELLP.
- **Interacciones farmacológicas**: se identificaron 92 interacciones. Entre las de nivel **mayor** figuran isometepteno, epinefrina (incluidas las formas oftálmica y tópica), lorcaserina, claritromicina y efedrina (incluida la nasal). Entre las de nivel **moderado** figuran doxiciclina, tetraciclina, minociclina, aprepitant, dexametasona, cimetidina, eluxadolina, clotrimazol, miconazol, fenilbutirato de glicerol, metreleptina y troglitazona.
- **Señales de seguridad ligadas a las indicaciones predichas**: riesgo de vasoconstricción coronaria, vasoespasmo, fibrosis retroperitoneal y pulmonar (observada con metisergida), y valvulopatía o hipertensión pulmonar por agonismo 5-HT2B.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no están disponibles en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipertricosis carece de ensayos, literatura y mecanismo plausible (nivel L5), y el perfil farmacológico sugiere que el efecto podría ser contrario o generar riesgos de seguridad. No se recomienda avanzar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), actualmente una laguna bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Si se desea explorar alguna dirección, priorizar la migraña con una revisión sistemática del riesgo cardiovascular y fibrótico, frente a alternativas más seguras.
- Evaluar la compatibilidad de vías de administración y la similitud con la indicación original, hoy pendientes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


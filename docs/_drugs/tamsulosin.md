---
layout: default
title: Tamsulosin
parent: Solo predicción del modelo (L5)
nav_order: 763
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
monitor_inn: "tamsulosin"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "migraine with brainstem aura"]
description: "Tamsulosin: nueva indicación predicha, Ambras type hypertrichosis universalis congenita (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Tamsulosin
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

## Tamsulosin: Ambras type hypertrichosis universalis congenita
{: .text-alpha }

## Resumen en Una Frase

Tamsulosina es un antagonista de los receptores adrenérgicos alfa-1 (subtipos 1A/1D), utilizado originalmente para el tratamiento de la hiperplasia prostática benigna.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis universal congénita de tipo Ambras**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.
La predicción carece de plausibilidad mecanística y debe considerarse un artefacto computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Ambras type hypertrichosis universalis congenita |
| Puntaje de Predicción TxGNN | 1.0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 14) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, tamsulosina es un antagonista alfa-1A/1D adrenérgico que relaja el músculo liso de la próstata y del cuello vesical, lo que mejora los síntomas urinarios de la hiperplasia prostática benigna.

**La predicción no parece razonable desde el punto de vista farmacológico.** El síndrome de Ambras es un trastorno genético raro, vinculado a reordenamientos cromosómicos que afectan la regulación de TRPS1. No hay evidencia de que el bloqueo alfa-1 adrenérgico influya en el desarrollo del folículo piloso ni en el mecanismo genético subyacente. La relación entre la indicación original (urológica, de aparición en la edad adulta) y la nueva (malformación congénita del pelo) es inexistente.

Las demás predicciones del ranking (hipertricosis, hipotricosis, alopecia areata difusa, anomalías del tallo piloso, síndromes malformativos y migraña con aura del tronco encefálico) presentan el mismo problema: ninguna cuenta con vínculo mecanístico creíble.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal predicha.

Como referencia, en la predicción de rango 9 (alopecia) se recuperaron dos publicaciones, pero ninguna demuestra un efecto terapéutico de tamsulosina: una trata sobre finasterida y sus eventos adversos psicológicos (PMID 33175100) y otra sobre cambios en las glándulas de Meibomio en hombres con HBP (PMID 32826647). Son coincidencias incidentales de palabras clave o de población.

---

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de principio activo único; ninguna cancelada). El texto de indicación aprobada no figura en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 6775201401IP1 | OMNIC OCAS 0,4 mg comprimidos de liberación prolongada recubiertos con película | Comprimido de liberación prolongada | No disponible |
| 74994 | Tamsulosina Normon 0,4 mg comprimidos de liberación prolongada EFG | Comprimido de liberación prolongada | No disponible |
| 67217 | Tamsulosina Teva-Ratiopharm 0,4 mg cápsulas duras de liberación modificada EFG | Cápsula dura de liberación modificada | No disponible |
| 68385 | Tamsulosina Normon 0,4 mg cápsulas duras de liberación modificada EFG | Cápsula dura de liberación modificada | No disponible |
| 89664 | Tamsulosina Stadafarma 0,4 mg cápsulas duras de liberación modificada EFG | Cápsula dura de liberación modificada | No disponible |

---

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de precaución** (según relaciones del grafo de conocimiento, no según el texto del prospecto): atrofia multisistémica, síndrome de taquicardia ortostática postural, hipotensión ortostática, enfermedad hepática, enfermedad de la vesícula biliar, priapismo y síndrome del iris flácido intraoperatorio.
- **Interacciones farmacológicas**: se identificaron 202 interacciones. Entre las principales:
  - **Mayor**: claritromicina.
  - **Moderadas**: bupropión, aprepitant, morfina (incluida la liposomal), lorcaserina, cimetidina, clotrimazol, miconazol, eliglustat, dronabinol, nabilona, opio, fenfluramina y dexfenfluramina, y los inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina).

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni literatura que respalden el uso de tamsulosina en la hipertricosis de tipo Ambras, y no hay un mecanismo creíble que lo explique. El puntaje elevado de TxGNN parece un artefacto del modelo TxGNN (aprendizaje profundo) (nivel de evidencia L5).

**Para avanzar se necesita:**
- Datos del mecanismo de acción de tamsulosina que sustenten algún vínculo con la biología del folículo piloso o con TRPS1.
- Evidencia preclínica (modelos celulares o animales) que justifique cualquier estudio posterior.
- Revisión de las demás predicciones del ranking, por si alguna cuenta con una base biológica más sólida.
- Obtención y análisis del prospecto oficial de la AEMPS para completar el perfil de seguridad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


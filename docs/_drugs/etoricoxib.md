---
layout: default
title: Etoricoxib
parent: Solo predicción del modelo (L5)
nav_order: 319
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-31
description: "Etoricoxib: nueva indicación predicha, Migraña (trastorno migrañoso) (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "ETORICOXIB"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "ulerythema ophryogenesis", "pulmonary hypertension", "benign prostatic hyperplasia (disease)", "kyphoscoliotic heart disease", "headache disorder", "trigeminal autonomic cephalalgia"]
---

# Etoricoxib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Etoricoxib: De Indicación Original No Especificada a Migraña
{: .text-alpha }

## Resumen en Una Frase

Etoricoxib es un inhibidor selectivo de la COX-2 que se comercializa en España como antiinflamatorio y analgésico. Los datos compilados para este informe no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **migraña (trastorno migrañoso)**, pero **no hay ensayos clínicos** y solo **1 publicación** vinculada, una revisión exploratoria sin datos de eficacia específicos de etoricoxib.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Migraña (trastorno migrañoso) |
| Puntaje de Predicción TxGNN | 0,9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 8) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone actualmente de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, etoricoxib es un inhibidor selectivo de la ciclooxigenasa-2 (COX-2; gen PTGS2), utilizado en artritis reumatoide, artrosis, lumbalgia crónica, espondilitis anquilosante, dolor agudo y gota. Mecanísticamente podría ser aplicable a la migraña.

La inflamación neurogénica mediada por prostaglandinas y la sensibilización trigeminovascular contribuyen a la migraña, por lo que inhibir la COX-2 es biológicamente plausible. Un estudio preclínico en ganglios trigéminos de rata (PMID 29209105) examinó el efecto de AINE, incluido etoricoxib, sobre la liberación de CGRP y PGE2, lo que apoya de forma indirecta este mecanismo, aunque está vinculado a otra entidad (migraña con o sin aura, susceptibilidad).

Para la migraña como tal, la única publicación vinculada es una revisión exploratoria sobre cefalea por ayuno en Ramadán, que no aporta datos de eficacia de etoricoxib. El puntaje tan alto del modelo es solo una predicción computacional.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [42841395](https://pubmed.ncbi.nlm.nih.gov/42841395/) | 2026 | Revisión exploratoria | Pain management | Revisa la cefalea atribuida al ayuno (p. ej., Ramadán); no ofrece datos de eficacia específicos de etoricoxib en migraña |

---

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de principio activo único, comprimidos recubiertos con película). Los textos de indicación aprobada no están disponibles.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 64933 | EXXIV 120 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 72076 | EXXIV 30 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 80373 | Etoricoxib Viatris 60 mg EFG | Comprimido recubierto con película | No disponible |
| 80262 | Etoricoxib Sandoz 60 mg EFG | Comprimido recubierto con película | No disponible |
| 80673 | Torixib 30 mg EFG | Comprimido recubierto con película | No disponible |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta de interacciones se completó y solo devolvió la relación farmacológica con su diana, COX-2 (PTGS2), sin interacciones medicamentosas clínicas con nivel de gravedad asignado.
- **Señales de seguridad en la literatura vinculada**:
  - Hiperqueratemia: caso de hiperpotasemia potencialmente mortal y disfunción renal aguda con etoricoxib en un paciente tratado con telmisartán y dieta baja en sodio (rica en potasio) (PMID 21373319).
  - Síndrome de vasoconstricción cerebral reversible posiblemente inducido por etoricoxib (PMID 25229174), relevante para cualquier uso en cefaleas.
  - Los inhibidores de COX-2 se asocian a riesgo cardiovascular y de retención de líquidos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para migraña solo existe una predicción del modelo (nivel L5), sin ensayos clínicos y con una única revisión sin datos específicos del fármaco. Como contexto, la predicción de «trastorno de cefalea» (nivel L4) cuenta con series y casos clínicos con etoricoxib (cefalea punzante primaria, cefaleas sensibles a indometacina, cefalea tusígena secundaria), pero sin estudios controlados.

**Para avanzar se necesita:**
- Obtener del prospecto de la AEMPS las indicaciones aprobadas, advertencias y contraindicaciones.
- Completar los datos del mecanismo de acción desde DrugBank.
- Búsqueda de estudios clínicos específicos de etoricoxib en migraña (ensayos aleatorizados o revisiones sistemáticas).
- Evaluar el riesgo cardiovascular, renal y cerebrovascular en la población con migraña antes de plantear un estudio.
- Valorar con mayor prioridad las entidades de cefalea con evidencia de casos (cefalea primaria punzante, cefaleas sensibles a indometacina).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


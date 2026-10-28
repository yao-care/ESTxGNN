---
layout: default
title: Dimenhydrinate
parent: Solo predicción del modelo (L5)
nav_order: 253
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
monitor_inn: "dimenhydrinate"
predicted_indications: ["allergic urticaria", "cold urticaria"]
description: "Dimenhydrinate: nueva indicación predicha, Urticaria alérgica (allergic urticaria) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Dimenhydrinate
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

## Dimenhydrinate: Urticaria alérgica (allergic urticaria)
{: .text-alpha }

## Resumen en Una Frase

Dimenhidrinato es una sal de difenhidramina y 8-cloroteofilina, utilizada originalmente para el vértigo de origen en el sistema nervioso central y la cinetosis (mareo por movimiento).
El modelo TxGNN predice que podría ser efectivo para **urticaria alérgica**, pero no hay **ningún ensayo clínico** y solo **1 publicación** (un estudio farmacocinético preliminar en perros) que respalde esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Urticaria alérgica (allergic urticaria) |
| Puntaje de Predicción TxGNN | 0.9974 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 12 de 19) |
| Número de Autorizaciones | 19 (vigentes: 12) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, el dimenhidrinato es la sal de difenhidramina con 8-cloroteofilina. La difenhidramina es un antagonista del receptor H1 de primera generación, con efectos sedantes y anticolinérgicos, lo que explica su uso en vértigo y cinetosis.

La urticaria alérgica es una enfermedad mediada por histamina (ronchas y prurito), y el bloqueo H1 es un mecanismo establecido para aliviar estos síntomas. El vínculo es, por tanto, biológicamente plausible a través del componente activo difenhidramina, aunque no existe evidencia directa con dimenhidrinato en esta indicación.

Hay que tener en cuenta que las guías prefieren los antihistamínicos de segunda generación por su menor carga sedante y anticolinérgica, lo que reduce el atractivo de reposicionar un agente de primera generación.

**Otra predicción (rango 2):** urticaria por frío (puntaje TxGNN 0,9924, nivel L5). Se basa solo en la predicción del modelo, sin ensayos ni literatura, y también se recomienda Hold. Se trata de una enfermedad impulsada por mastocitos e histamina, por lo que el bloqueo H1 es plausible, pero los antihistamínicos de segunda generación son el tratamiento de primera línea.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Estudio farmacocinético preliminar (en perros sanos) | Veterinary Dermatology | Compara la farmacocinética de la difenhidramina tras administración oral e intravenosa y tras dimenhidrinato oral, y su efecto farmacodinámico sobre la formación de ronchas inducidas por histamina. El dimenhidrinato podría ofrecer mejor absorción oral de difenhidramina. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 60839 | CINFAMAR 50 mg comprimidos recubiertos | Comprimido recubierto | No disponible |
| 57681 | BIODRAMINA 20 mg chicles medicamentosos | Chicle medicamentoso | No disponible |
| 66174 | BIODRAMINA INFANTIL 4 mg/ml solución oral | Solución oral | No disponible |
| 85911 | BIODRAMINA INFANTIL 12,5 mg solución oral | Solución oral en sobre | No disponible |
| 76942 | BIODRAMINA INFANTIL 24 mg solución oral | Solución oral | No disponible |

Se muestran 5 de las 19 autorizaciones vigentes (todas de medicamento con un solo principio activo; ninguna cancelada). Entre las demás hay comprimidos, supositorios y cápsulas duras, así como asociaciones con cafeína.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proceden del prospecto):** hipertensión, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, hiperglucemia, diabetes mellitus y cetoacidosis diabética, úlcera péptica, hiperplasia benigna de próstata, hipotensión, gota, abuso/dependencia de sustancias, trastornos de la coagulación, síndrome coronario agudo, enfermedad coronaria e infarto de miocardio, hemoglobinopatía, hipertensión ocular, glaucoma de ángulo cerrado, estenosis pilórica, hipertiroidismo (enfermedad de Graves, tirotoxicosis), obstrucción del cuello vesical e hipofosfatemia.
- **Interacciones farmacológicas:** se identificaron 67 interacciones. Entre las principales:
  - **Mayores:** cloruro de potasio y citrato de potasio.
  - **Moderadas:** anticolinérgicos (atropina, escopolamina, hiosciamina, glicopirronio, diciclomina, clidinio, propantelina, trospio, metescopolamina, mepenzolato), opioides y similares (morfina, opio, loperamida, eluxadolina), y otros (metoclopramida, prucaloprida, nabilona).
  - El patrón sugiere un efecto aditivo anticolinérgico y sedante.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es biológicamente plausible por el bloqueo H1 de la difenhidramina, pero la evidencia es de nivel L4: ningún ensayo clínico y una sola publicación preclínica/farmacocinética en perros. Además, los antihistamínicos de segunda generación son el tratamiento estándar, con mejor perfil de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), actualmente no disponible.
- Completar los datos del mecanismo de acción.
- Disponer de estudios clínicos en humanos con dimenhidrinato en urticaria y su comparación con antihistamínicos de segunda generación.
- Evaluar la carga sedante y anticolinérgica frente a las contraindicaciones y las interacciones identificadas.
- Confirmar la compatibilidad de vías de administración y formas farmacéuticas para la nueva indicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


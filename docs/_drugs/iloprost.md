---
layout: default
title: Iloprost
parent: Solo predicción del modelo (L5)
nav_order: 405
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
description: "Iloprost: nueva indicación predicha, Hipotricosis simple del cuero cabelludo (nivel de evidencia L5). Indicación original: Hipertensión arterial pulmonar"
monitor_inn: "ILOPROST"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "pulmonary arteriovenous malformation (disease)", "diffuse alopecia areata"]
---

# Iloprost
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Iloprost: De Hipertensión Arterial Pulmonar a Hipotricosis Simple del Cuero Cabelludo
{: .text-alpha }

## Resumen en Una Frase

Iloprost es un análogo estable de la prostaciclina, utilizado originalmente para el tratamiento de la hipertensión arterial pulmonar.
El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial pulmonar |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 0,9945 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 4 de 5) |
| Número de Autorizaciones | 5 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, iloprost es un análogo de la prostaciclina que actúa a través del receptor IP y la señalización del AMPc. Produce vasodilatación pulmonar e inhibe la agregación plaquetaria y la proliferación del músculo liso. Su eficacia en la hipertensión arterial pulmonar está establecida.

La relación entre la indicación original y la nueva es débil. La hipotricosis simple es un trastorno genético del folículo piloso (por ejemplo, variantes en *CDSN* o *APCDD1*) y no tiene una vía de prostaciclina establecida. Solo existe una conexión especulativa: otros análogos de prostaglandinas, como bimatoprost, influyen en el crecimiento del cabello.

En conclusión, el puntaje alto de TxGNN (0,9945) no está respaldado por ningún vínculo mecanístico demostrado ni por datos clínicos. Debe interpretarse como una hipótesis que requiere validación, no como una indicación plausible.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 86227 | Iloprost Zentiva 20 microgramos/ml solución para inhalación por nebulizador | Solución para inhalación por nebulizador | No consta en los datos compilados |
| 61596 | Ilomedin 50 microgramos/0,5 ml, concentrado para solución para perfusión | Concentrado para solución para perfusión | No consta en los datos compilados |
| 03255004 | Ventavis 10 microgramos/ml solución para inhalación por nebulizador | Solución para inhalación por nebulizador | No consta en los datos compilados |
| 86242 | Iloprost Rafarm 10 microgramos/ml solución para inhalación por nebulizador | Solución para inhalación por nebulizador | No consta en los datos compilados |
| 86226 | Iloprost Zentiva 10 microgramos/ml solución para inhalación por nebulizador | Solución para inhalación por nebulizador | No consta en los datos compilados |

Las cinco autorizaciones son de monofármaco y están vigentes. Ninguna incluye una formulación tópica o dermatológica; solo hay formas inhaladas y de perfusión.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proceden del prospecto)**: insuficiencia hepática, enfermedad pulmonar obstructiva crónica (incluida la de inicio precoz grave), trastornos hipotensivos, edema pulmonar y enfermedad bronquial.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las de nivel moderado destacan:
  - Adrenalina
  - Ácido acetilsalicílico
  - Inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina)
  - Insulina humana inhalada
  - Manitol
  - Efedrina
  - Fenfluramina y dexfenfluramina
  - Glicerina
  - Papaverina
  - Sibutramina

  También hay interacciones de nivel no clasificado, como calcitriol, pantoprazol, morfina, metformina y omeprazol.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos, literatura y vínculo mecanístico plausible; es solo un resultado del modelo (nivel L5). Una enfermedad genética del folículo piloso sin relación conocida con la vía de la prostaciclina no justifica avanzar sin evidencia adicional.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de iloprost y una hipótesis biológica concreta sobre el folículo piloso
- Estudios preclínicos en modelos de folículo piloso o de hipotricosis
- Evaluación de la viabilidad de una vía de administración adecuada (las formas autorizadas son inhaladas y de perfusión, no tópicas)
- Revisión del prospecto de la AEMPS para advertencias y contraindicaciones

**Nota complementaria:** entre las demás predicciones del modelo, la hipertensión arterial pulmonar asociada a enfermedad del tejido conectivo muestra el respaldo más sólido (nivel L3, con estudios observacionales y un estudio preclínico). Sin embargo, es un subgrupo dentro de la clase ya aprobada y no un reposicionamiento propiamente dicho. Si el objetivo es priorizar líneas de investigación, esa sería más prometedora que la hipotricosis.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


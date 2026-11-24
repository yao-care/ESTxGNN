---
layout: default
title: Iloprost
parent: Solo predicción del modelo (L5)
nav_order: 405
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
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
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 4 de 5; autorizadas no comercializadas: 1) |
| Número de Autorizaciones | 5 (comercializadas: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Iloprost (traducción no oficial): «El iloprost es un análogo sintético de la prostaciclina PGI 2. El iloprost es un vasodilatador e inhibe la agregación plaquetaria.» Texto original en inglés: "Iloprost is a synthetic analog of prostacyclin PGI 2. Iloprost is a vasodilator and inhibits platelet aggregation." ([DailyMed: Aurlumyn (iloprost) prescribing information, BTG International Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=34036fc0-6832-d066-e063-6394a90a18a4), versión del 2026-08-13; consultado el 2026-11-19). Según la información conocida, iloprost es un análogo de la prostaciclina que actúa a través del receptor IP y la señalización del AMPc. Produce vasodilatación pulmonar e inhibe la agregación plaquetaria y la proliferación del músculo liso. Su eficacia en la hipertensión arterial pulmonar está establecida.

La relación entre la indicación original y la nueva es débil. La hipotricosis simple es un trastorno genético del folículo piloso (por ejemplo, variantes en *CDSN* o *APCDD1*) y no tiene una vía de prostaciclina establecida. Solo existe una conexión especulativa: otros análogos de prostaglandinas, como bimatoprost, influyen en el crecimiento del cabello.

En conclusión, el puntaje alto de TxGNN (0,9945) no está respaldado por ningún vínculo mecanístico demostrado ni por datos clínicos. Debe interpretarse como una hipótesis que requiere validación, no como una indicación plausible.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 86227 | ILOPROST ZENTIVA 20 MICROGRAMOS/ML SOLUCION PARA INHALACION POR NEBULIZADOR | SOLUCIÓN PARA INHALACIÓN POR NEBULIZADOR | Zentiva K.S. | Comercializada |
| 61596 | ILOMEDIN 50 MICROGRAMOS/0,5 ML, CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Bayer Hispania S.L. | Comercializada |
| 86242 | ILOPROST RAFARM 10 MICROGRAMOS/ML SOLUCION PARA INHALACION POR NEBULIZADOR | SOLUCIÓN PARA INHALACIÓN POR NEBULIZADOR | Rafarm S.A. | Comercializada |
| 86226 | ILOPROST ZENTIVA 10 MICROGRAMOS/ML SOLUCION PARA INHALACION POR NEBULIZADOR | SOLUCIÓN PARA INHALACIÓN POR NEBULIZADOR | Zentiva K.S. | Comercializada |
| 03255004 | VENTAVIS 10 microgramos/ml SOLUCION PARA INHALACION POR NEBULIZADOR | SOLUCIÓN PARA INHALACIÓN POR NEBULIZADOR | Bayer Ag | Autorizada, no comercializada |

Se muestran las 5 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Aurlumyn (iloprost) prescribing information, BTG International Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=34036fc0-6832-d066-e063-6394a90a18a4) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


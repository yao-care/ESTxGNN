---
layout: default
title: Hesperidin
parent: Solo predicción del modelo (L5)
nav_order: 393
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
description: "Hesperidin: nueva indicación predicha, Neoplasia mieloproliferativa (nivel de evidencia L5). Indicación original: No disponible en los datos de las autorizaciones"
monitor_inn: "hesperidin"
predicted_indications: ["myeloproliferative neoplasm", "monocytic leukemia", "spermatocytic seminoma", "tubular variant testicular seminoma", "gestational trophoblastic neoplasm"]
---

# Hesperidin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Hesperidina: De Indicación Original No Especificada a Neoplasia Mieloproliferativa
{: .text-alpha }

## Resumen en Una Frase

Hesperidina es un flavonoide comercializado en España (por ejemplo, como Daflon 500 mg), cuya indicación aprobada no figura en los datos compilados para este informe.
El modelo TxGNN predice que podría ser efectivo para **neoplasia mieloproliferativa**,
pero actualmente solo existe **1 publicación** (un estudio computacional in silico) y **ningún ensayo clínico** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de las autorizaciones |
| Nueva Indicación Predicha | Neoplasia mieloproliferativa |
| Puntaje de Predicción TxGNN | 0,9947 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 5 de 10) |
| Número de Autorizaciones | 10 (vigentes: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de la hesperidina. Según la información conocida, es un flavonoide glucósido (la forma aglicona circulante es la hesperetina) que se comercializa en España, entre otros, en preparados como Daflon 500 mg, y mecanísticamente podría ser aplicable a la nueva indicación solo de forma hipotética.

La única publicación de apoyo es un estudio in silico de 2019 que cribó compuestos frente al dominio quinasa de BCR-ABL en leucemia mieloide crónica (LMC). La LMC es una neoplasia mieloproliferativa, por lo que el vínculo es plausible, pero se trata únicamente de acoplamiento molecular computacional, sin validación in vitro, in vivo ni clínica en los datos disponibles.

Además, la baja biodisponibilidad oral de la hesperidina debilita el argumento de una inhibición de quinasas a concentraciones alcanzables. El puntaje alto de TxGNN (0,9947) es una predicción del modelo, no evidencia clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31759365](https://pubmed.ncbi.nlm.nih.gov/31759365/) | 2019 | Estudio in silico / computacional | Asian Pacific Journal of Cancer Prevention | Reposicionamiento de fármacos por métodos in silico dirigidos al dominio quinasa de BCR-ABL en leucemia mieloide crónica, con el objetivo de combatir la resistencia a los inhibidores de tirosina quinasa mediante la proteína Grb-2 |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 4691-2004IP3 | Daflon 500mg comprimidos recubiertos | Comprimido recubierto | No especificada |
| 4691-2004IP | DAFLON 500mg comprimidos recubiertos | Comprimido recubierto | No especificada |
| 59080 | DAFLON 500 mg comprimidos recubiertos con película | Comprimido recubierto | No especificada |
| 8539291C | DAFLON 500 mg comprimidos recubiertos con película | Comprimido recubierto | No especificada |
| 4691-2004IP2 | Daflon 500mg comprimidos recubiertos | Comprimido recubierto | No especificada |

Se muestran 5 de las 10 autorizaciones vigentes; todas son de preparados con un único principio activo. Entre las restantes figuran otras presentaciones de Daflon y Fabroven (cápsulas duras).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo TxGNN y en un estudio computacional sin validación experimental, sin ensayos clínicos. Además, la baja biodisponibilidad de la hesperidina limita la plausibilidad farmacológica.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la hesperidina
- Obtención del prospecto de AEMPS (indicaciones, advertencias y contraindicaciones) para el cribado de seguridad
- Validación preclínica (in vitro e in vivo) de la actividad frente a células de neoplasias mieloproliferativas, con hesperidina y su aglicona hesperetina
- Estudios de farmacocinética para determinar si se alcanzan concentraciones eficaces
- Valorar otras indicaciones predichas con mayor respaldo preclínico solo si aparece evidencia adicional (la leucemia monocítica cuenta con un estudio in vitro de 2003 que sugiere, si acaso, una menor actividad proapoptótica de las formas con rutinósido)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


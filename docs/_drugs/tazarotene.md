---
layout: default
title: Tazarotene
parent: Solo predicción del modelo (L5)
nav_order: 766
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-20
monitor_inn: "Tazarotene"
predicted_indications: ["seborrheic dermatitis", "seborrheic keratosis", "vulvar inverted follicular keratosis"]
description: "Tazarotene: nueva indicación predicha, Dermatitis seborreica (seborrheic dermatitis) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 2 (comercializadas: 0)"
---

# Tazarotene
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Tazarotene: Dermatitis seborreica (seborrheic dermatitis)
{: .text-alpha }

## Resumen en Una Frase

Tazaroteno es un retinoide tópico, utilizado originalmente para el tratamiento de la psoriasis, la parapsoriasis y el acné.
El modelo TxGNN predice que podría ser efectivo para **Dermatitis Seborreica**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; la predicción se basa únicamente en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Dermatitis seborreica (seborrheic dermatitis) |
| Puntaje de Predicción TxGNN | 0.9979 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado (registros anulados: 2 de 2) |
| Número de Autorizaciones | 2 (comercializadas: 0) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Tazarotene (traducción no oficial): «El tazaroteno es un profármaco retinoide que se convierte en su forma activa, el ácido carboxílico del tazaroteno, mediante desesterificación. El ácido tazaroténico se une a los tres miembros de la familia de receptores del ácido retinoico (RAR): RARα, RARβ y RARγ, pero muestra una selectividad relativa por RARβ y RARγ, y puede modificar la expresión génica.» Texto original en inglés: "Tazarotene is a retinoid prodrug which is converted to its active form, the carboxylic acid of tazarotene, by deesterification. Tazarotenic acid binds to all three members of the retinoic acid receptor (RAR) family: RARα, RARβ, and RARγ, but shows relative selectivity for RARβ, and RARγ and may modify gene expression." ([DailyMed: Tazorac (tazarotene) prescribing information, Almirall, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4e4e4b81-420e-4492-8a74-80b692a80057), versión del 2026-11-04; consultado el 2026-11-19). Según la información conocida, el tazaroteno es un profármaco retinoide de uso tópico que se convierte en ácido tazaroténico. Este se une a los receptores del ácido retinoico (RAR), con mayor afinidad por RAR-beta y RAR-gamma, y normaliza la diferenciación de los queratinocitos, reduciendo la hiperproliferación y la inflamación.

La psoriasis y la dermatitis seborreica son dermatosis inflamatorias con descamación y alteración de la renovación epidérmica. Por ello, mecanísticamente, un efecto sobre la diferenciación de queratinocitos podría ser relevante para la descamación y la inflamación de la dermatitis seborreica.

Existen, sin embargo, limitaciones importantes. La dermatitis seborreica depende también de la colonización por *Malassezia* y de la respuesta inmunitaria, aspectos que los retinoides no abordan directamente. Además, la irritación propia de los retinoides tópicos podría empeorar las lesiones faciales y del cuero cabelludo. El vínculo descansa solo en la predicción del modelo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para dermatitis seborreica.

Como información complementaria, para la segunda indicación predicha (queratosis seborreica, puntaje 0,9951, nivel L4) se recuperaron dos publicaciones indirectas. Sus resúmenes no confirman que informen resultados con tazaroteno:

<!-- review:begin es-lic-20261105-tazarotene-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Ambas autorizaciones corresponden a monofármaco, están vigentes y pertenecen a Allergan Pharmaceuticals International Limited." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 autorizaciones (comercializadas: 0); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-tazarotene-1 -->

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36215682](https://pubmed.ncbi.nlm.nih.gov/36215682/) | 2023 | Revisión sistemática | J Dermatol Treat | Eficacia y seguridad de tratamientos tópicos para queratosis seborreicas (26 informes incluidos) |
| [15090020](https://pubmed.ncbi.nlm.nih.gov/15090020/) | 2004 | Cohorte | Int J Dermatol | Comparación de crioterapia estándar con calcipotrieno, tazaroteno e imiquimod tópicos en queratosis seborreicas |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61862 | ZORAC 0,05%, GEL | Gel (tópico) | No especificada en los datos disponibles |
| 61861 | ZORAC 0,1%, GEL | Gel (tópico) | No especificada en los datos disponibles |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): respuesta fotoparoxística, enfermedad de fotosensibilidad y quemadura solar.
- **Interacciones farmacológicas**: la consulta no halló interacciones fármaco-fármaco clínicas. Los 3 registros son de farmacología de dianas: el tazaroteno se une a los receptores del ácido retinoico alfa, beta y gamma (RARA, RARB, RARG), con mayor afinidad por RAR-beta.
- Dado que se trata de un retinoide tópico, conviene vigilar la irritación local, sobre todo en zonas sensibles como cara, cuero cabelludo o mucosas.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para dermatitis seborreica tiene un puntaje alto (0,9979), pero no cuenta con ensayos clínicos ni literatura (nivel L5). Además, la dermatitis seborreica tiene un componente fúngico e inmunitario que el tazaroteno no aborda, y su potencial irritante podría ser un problema.

**Para avanzar se necesita:**
- Datos del mecanismo de acción original verificados en DrugBank
- Advertencias y contraindicaciones del prospecto de la AEMPS (actualmente sin datos)
- Revisión sistemática de literatura preclínica y clínica sobre retinoides tópicos en dermatitis seborreica
- Evaluación de tolerabilidad en cara y cuero cabelludo
- Si se desea explorar la alternativa de queratosis seborreica, revisar el texto completo de las dos publicaciones para comprobar si evaluaron el tazaroteno y con qué resultados

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Ambas autorizaciones corresponden a monofármaco, están vigentes y pertenecen a Allergan Pharmaceuticals International Limited" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Tazorac (tazarotene) prescribing information, Almirall, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4e4e4b81-420e-4492-8a74-80b692a80057) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


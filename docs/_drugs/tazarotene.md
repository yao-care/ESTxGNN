---
layout: default
title: Tazarotene
parent: Solo predicción del modelo (L5)
nav_order: 766
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Tazarotene: nueva indicación predicha, Dermatitis seborreica (nivel de evidencia L5). Indicación original: Psoriasis, parapsoriasis y acné (según el grafo de conocimiento"
monitor_inn: "Tazarotene"
predicted_indications: ["seborrheic dermatitis", "seborrheic keratosis", "vulvar inverted follicular keratosis"]
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Tazaroteno: De Psoriasis a Dermatitis Seborreica

## Resumen en Una Frase

Tazaroteno es un retinoide tópico, utilizado originalmente para el tratamiento de la psoriasis, la parapsoriasis y el acné.
El modelo TxGNN predice que podría ser efectivo para **Dermatitis Seborreica**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; la predicción se basa únicamente en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Psoriasis, parapsoriasis y acné (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Dermatitis seborreica |
| Puntaje de Predicción TxGNN | 99,79% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información original del fármaco. Según la información conocida, el tazaroteno es un profármaco retinoide de uso tópico que se convierte en ácido tazaroténico. Este se une a los receptores del ácido retinoico (RAR), con mayor afinidad por RAR-beta y RAR-gamma, y normaliza la diferenciación de los queratinocitos, reduciendo la hiperproliferación y la inflamación.

La psoriasis y la dermatitis seborreica son dermatosis inflamatorias con descamación y alteración de la renovación epidérmica. Por ello, mecanísticamente, un efecto sobre la diferenciación de queratinocitos podría ser relevante para la descamación y la inflamación de la dermatitis seborreica.

Existen, sin embargo, limitaciones importantes. La dermatitis seborreica depende también de la colonización por *Malassezia* y de la respuesta inmunitaria, aspectos que los retinoides no abordan directamente. Además, la irritación propia de los retinoides tópicos podría empeorar las lesiones faciales y del cuero cabelludo. El vínculo descansa solo en la predicción del modelo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para dermatitis seborreica.

Como información complementaria, para la segunda indicación predicha (queratosis seborreica, puntaje 99,51%, nivel L4) se recuperaron dos publicaciones indirectas. Sus resúmenes no confirman que informen resultados con tazaroteno:

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

Ambas autorizaciones corresponden a monofármaco, están vigentes y pertenecen a Allergan Pharmaceuticals International Limited.

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
La predicción para dermatitis seborreica tiene un puntaje alto (99,79%), pero no cuenta con ensayos clínicos ni literatura (nivel L5). Además, la dermatitis seborreica tiene un componente fúngico e inmunitario que el tazaroteno no aborda, y su potencial irritante podría ser un problema.

**Para avanzar se necesita:**
- Datos del mecanismo de acción original verificados en DrugBank
- Advertencias y contraindicaciones del prospecto de la AEMPS (actualmente sin datos)
- Revisión sistemática de literatura preclínica y clínica sobre retinoides tópicos en dermatitis seborreica
- Evaluación de tolerabilidad en cara y cuero cabelludo
- Si se desea explorar la alternativa de queratosis seborreica, revisar el texto completo de las dos publicaciones para comprobar si evaluaron el tazaroteno y con qué resultados
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


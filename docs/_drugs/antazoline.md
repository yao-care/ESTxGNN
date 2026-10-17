---
layout: default
title: Antazoline
parent: Evidencia moderada (L3-L4)
nav_order: 59
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-14
description: "Antazoline: nueva indicación predicha, Urticaria alérgica (nivel de evidencia L4). Indicación original: Rinitis alérgica (según el grafo de conocimiento"
monitor_inn: "antazoline"
predicted_indications: ["recalcitrant atopic dermatitis", "IgE responsiveness, atopic", "nasal cavity disease", "acute laryngopharyngitis"]
---

# Antazoline
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **6** 
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

# Antazolina: De Rinitis Alérgica a Urticaria Alérgica

## Resumen en Una Frase

Antazolina es un antihistamínico H1 de primera generación, utilizado originalmente en afecciones alérgicas como la rinitis alérgica, la conjuntivitis atópica y la urticaria.
El modelo TxGNN predice que podría ser efectivo para **urticaria alérgica**, aunque esta indicación ya figura entre sus usos originales.
Actualmente no hay **ensayos clínicos** registrados y solo hay **2 publicaciones** con apoyo indirecto.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Rinitis alérgica (según el grafo de conocimiento; las autorizaciones españolas no incluyen texto de indicación) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99,99% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, antazolina es un antagonista del receptor H1 de histamina de primera generación. Bloquea los efectos de la histamina liberada por los mastocitos, responsable de picor, enrojecimiento y habones en las reacciones alérgicas.

La urticaria alérgica es una enfermedad mediada por histamina, por lo que el encaje mecanístico es sólido. Sin embargo, la urticaria y el angioedema ya figuran entre las indicaciones originales de antazolina. Por tanto, esta predicción es en gran medida una reformulación de un uso existente y no un reposicionamiento genuino. El puntaje elevado probablemente refleja la similitud a nivel de clase farmacológica.

La literatura recuperada ofrece solo un apoyo indirecto: un artículo sobre complicaciones relacionadas con la anafilaxia y otro sobre afinidades de receptores de agentes oftálmicos y sistémicos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31929239](https://pubmed.ncbi.nlm.nih.gov/31929239/) | 2020 | Revisión | Annals of Cardiac Anaesthesia | Fibrilación auricular inducida por anafilaxia y consideraciones fisiopatológicas, terapéuticas y anestésicas. Apoyo solo indirecto. |
| [34387278](https://pubmed.ncbi.nlm.nih.gov/34387278/) | 2021 | Otro (evaluación de afinidad de receptores) | Current Opinion in Allergy and Clinical Immunology | Evaluación de los perfiles de receptores de fármacos oftálmicos y sistémicos usados en el ojo seco. Apoyo indirecto. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 81752 | OPTIALERG 5 MG/ML + 0,25 MG/ML COLIRIO EN SOLUCIÓN | Colirio en solución | No disponible en los datos compilados |
| 19763 | ALERGOFTAL 0,25 mg/ml + 5 mg/ml COLIRIO EN SOLUCIÓN | Colirio en solución | No disponible en los datos compilados |

Ambos productos son colirios de uso oftálmico, lo que difiere de la vía necesaria para una indicación cutánea como la urticaria.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): hipertensión, enfermedad cardiovascular, diabetes mellitus y cetoacidosis diabética, hiperglucemia, hipertiroidismo (enfermedad de Graves, tirotoxicosis), úlcera péptica, hiperplasia prostática benigna, obstrucción del cuello vesical, hipertensión ocular, glaucoma de ángulo cerrado, infección ocular y conjuntivitis.
- **Interacciones farmacológicas**: no se encontraron interacciones registradas en la consulta realizada.

Consultar el prospecto para la información de advertencias y contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es mecanísticamente plausible, pero coincide con indicaciones ya existentes y no cuenta con ensayos clínicos. La literatura es solo indirecta. Además, las únicas presentaciones comercializadas son colirios, y en la práctica se prefieren antihistamínicos de segunda generación no sedantes.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones oficiales), requisito previo para cualquier evaluación de seguridad.
- Datos detallados del mecanismo de acción desde DrugBank.
- Evaluar la compatibilidad de vía de administración (colirio frente a formulaciones sistémicas o tópicas cutáneas).
- Literatura o ensayos específicos de antazolina en urticaria.
- Comparación con antihistamínicos de segunda generación en cuanto a eficacia y perfil de seguridad.

**Otras predicciones del modelo (todas con nivel L5 y decisión Hold):** urticaria por frío (99,96%), dermatitis atópica recalcitrante (99,71%), respuesta atópica de IgE (99,68%), enfermedad de la cavidad nasal (99,46%) y laringofaringitis aguda (99,45%). Ninguna cuenta con ensayos ni literatura, y varias se solapan con indicaciones originales o tienen un vínculo mecanístico débil.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


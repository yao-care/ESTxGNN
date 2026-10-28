---
layout: default
title: Levocabastine
parent: Solo predicción del modelo (L5)
nav_order: 464
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
monitor_inn: "Levocabastine"
predicted_indications: ["allergic urticaria", "rosacea conjunctivitis"]
description: "Levocabastine: nueva indicación predicha, Urticaria alérgica (allergic urticaria) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Levocabastine
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

## Levocabastine: Urticaria alérgica (allergic urticaria)
{: .text-alpha }

## Resumen en Una Frase

Levocabastina es un antihistamínico antagonista selectivo de los receptores H1, utilizado originalmente en el tratamiento de la conjuntivitis alérgica (atópica, papilar y primaveral).
El modelo TxGNN predice que podría ser efectivo para **urticaria alérgica**,
pero actualmente no hay **ningún ensayo clínico** registrado y solo se dispone de **3 publicaciones** de apoyo indirecto (una revisión, un estudio clínico en rinitis alérgica y un análisis de farmacovigilancia).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Urticaria alérgica (allergic urticaria) |
| Puntaje de Predicción TxGNN | 0.9918 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 2 de 3) |
| Número de Autorizaciones | 3 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según la farmacología establecida, la levocabastina es un antagonista selectivo del receptor H1 de la histamina. En la urticaria alérgica, la liberación de histamina por los mastocitos provoca el habón y el eritema, y los antihistamínicos H1 son el tratamiento de primera línea. Por ello, el mecanismo es biológicamente plausible.

La relación con la indicación original es de tipo fisiopatológico: tanto la conjuntivitis alérgica como la urticaria alérgica son procesos mediados por histamina.

Sin embargo, existe una limitación importante: la levocabastina solo se comercializa en forma de colirio y spray nasal, con exposición sistémica mínima. No hay evidencia de que estas vías controlen la urticaria cutánea. Además, ya existen antihistamínicos H1 sistémicos (p. ej., de segunda generación) que cubren esta necesidad, por lo que un producto tópico reposicionado encaja mal.

También se observa una segunda predicción (conjuntivitis rosácea, 0.9917), sin ninguna evidencia clínica ni bibliográfica. La rosácea ocular se debe principalmente a disfunción de las glándulas de Meibomio, inestabilidad de la película lagrimal, inflamación y factores microbianos o de Demodex, y no principalmente a la histamina. La predicción probablemente refleja la cercanía nosológica con otras conjuntivitis. Su nivel de evidencia es L5 y se recomienda Hold.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [8938880](https://pubmed.ncbi.nlm.nih.gov/8938880/) | 1996 | Estudio clínico (ECA cruzado, doble ciego, controlado con placebo) | Rhinology | En 22 pacientes con rinitis alérgica, la levocabastina nasal (0,5 mg/ml) redujo significativamente los estornudos y la rinorrea tras provocación nasal con alérgeno; evidencia en rinitis, no en urticaria |
| [1685361](https://pubmed.ncbi.nlm.nih.gov/1685361/) | 1991 | Revisión | Clinical Pharmacokinetics | Revisa la farmacocinética y farmacodinamia de los antihistamínicos H1 de segunda generación, usados en rinoconjuntivitis alérgica y urticaria crónica; no es específica de levocabastina |
| [42585211](https://pubmed.ncbi.nlm.nih.gov/42585211/) | 2026 | Análisis descriptivo de farmacovigilancia | PloS one | Caracteriza las reacciones adversas de azelastina y levocabastina a partir de la base WHO-VigiAccess; aporta información de seguridad, no de eficacia en urticaria |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 60920 | REACTINE LEVOCABASTINA 0,5 mg/ml colirio en suspensión | Colirio en suspensión | Texto de indicación no disponible |
| 60918 | BILINA 0,5 mg/ml suspensión para pulverización nasal | Solución para pulverización nasal | Texto de indicación no disponible |
| 60917 | BILINA 0,5 mg/ml colirio en suspensión | Colirio en suspensión | Texto de indicación no disponible |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: los datos farmacológicos compilados registran una interacción con el receptor NTS2 (NTSR2), sin afinidad documentada que sustente este mecanismo ni nivel de gravedad clínica asignado. Se señala además que la FDA registra este fármaco como «descontinuado» en EE. UU.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje TxGNN es alto y el mecanismo H1 es plausible, no hay ensayos clínicos y la evidencia es solo indirecta (L4). Las formulaciones comercializadas (oftálmica y nasal) con exposición sistémica mínima no son adecuadas para una enfermedad cutánea, y ya existen alternativas sistémicas.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias y contraindicaciones) para completar la evaluación de seguridad
- Confirmar los datos del mecanismo de acción en DrugBank
- Evidencia de que alguna vía o formulación pueda lograr exposición suficiente para controlar la urticaria cutánea
- Estudios clínicos o preclínicos específicos de levocabastina en urticaria que demuestren ventajas frente a los antihistamínicos sistémicos actuales
- Completar el análisis de compatibilidad de vías de administración, actualmente pendiente
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


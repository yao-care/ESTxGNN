---
layout: default
title: Upadacitinib
parent: Solo predicción del modelo (L5)
nav_order: 551
evidence_level: L5
indication_count: 2
---

# Upadacitinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Upadacitinib: De Enfermedades Inflamatorias Inmunomediadas a Síndrome de Microftalmía Colobomatosa-Displasia Rizomélica

## Resumen en Una Frase

Upadacitinib es un inhibidor selectivo de JAK1 que se comercializa en España como Rinvoq y se usa en enfermedades inflamatorias inmunomediadas. Los datos de autorización recibidos no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de microftalmía colobomatosa-displasia rizomélica**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las autorizaciones (el texto de indicación está vacío); se asume uso inmunomediado por conocimiento general |
| Nueva Indicación Predicha | Síndrome de microftalmía colobomatosa-displasia rizomélica |
| Puntaje de Predicción TxGNN | 99.61% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Por conocimiento general, upadacitinib es un inhibidor selectivo de JAK1 que reduce la señalización de citocinas por la vía JAK-STAT en enfermedades inmunomediadas.

Con los datos proporcionados, **no se sustenta un vínculo mecanístico** con la nueva indicación. Este síndrome es un trastorno congénito raro del desarrollo, con coloboma/microftalmía y displasia esquelética rizomélica. Presumiblemente es de origen genético y no está causado por inflamación dependiente de JAK. Además, un inmunomodulador administrado después del nacimiento difícilmente revertiría malformaciones estructurales que se originan en la embriogénesis.

El puntaje alto de TxGNN (0.996) es solo una predicción del grafo de conocimiento. Puede reflejar la topología del grafo o la escasa anotación de una enfermedad rara, más que una justificación biológica. La similitud con la indicación original está pendiente de análisis.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191404001 | RINVOQ 15 MG COMPRIMIDOS DE LIBERACIÓN PROLONGADA | Comprimido de liberación prolongada | No especificada en los datos |
| 1191404006 | RINVOQ 30 MG COMPRIMIDOS DE LIBERACIÓN PROLONGADA | Comprimido de liberación prolongada | No especificada en los datos |
| 1191404010 | RINVOQ 45 MG COMPRIMIDOS DE LIBERACIÓN PROLONGADA | Comprimido de liberación prolongada | No especificada en los datos |

Las tres autorizaciones pertenecen al titular Abbvie Deutschland GmbH & Co. KG.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como referencia general, upadacitinib tiene advertencias conocidas de infecciones, trombosis y neoplasias malignas. Esto pesa en contra de su uso sin una justificación clara.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ningún respaldo clínico ni bibliográfico (L5). El mecanismo de JAK1 no explica de forma plausible una malformación congénita del desarrollo. El perfil de seguridad de upadacitinib exige una justificación clara que hoy no existe.

La segunda predicción del modelo, el síndrome de braquidactilia-sindactilia (puntaje 99.58%, L5), tiene la misma limitación. Se trata de una malformación congénita de extremidades sin conexión evidente con la señalización JAK-STAT, y también queda en Hold.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank
- Prospecto de AEMPS con advertencias y contraindicaciones, y el texto de las indicaciones aprobadas
- Evidencia de que la vía JAK-STAT participa en la fisiopatología de este síndrome
- Estudios preclínicos o de mecanismo que respalden la hipótesis
- Revisión de la anotación del grafo para descartar que el puntaje sea un artefacto de una enfermedad rara con pocos datos

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


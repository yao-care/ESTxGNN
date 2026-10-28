---
layout: default
title: Tenoxicam
parent: Solo predicción del modelo (L5)
nav_order: 777
evidence_level: L5
indication_count: 8
monitor_inn: "TENOXICAM"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "headache disorder", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "trigeminal autonomic cephalalgia", "alopecia"]
last_modified_at: 2026-10-23
description: "Tenoxicam: nueva indicación predicha, Brachydactyly-syndactyly syndrome (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Tenoxicam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Tenoxicam: Brachydactyly-syndactyly syndrome
{: .text-alpha }

## Resumen en Una Frase

El modelo TxGNN predice que podría ser efectivo para el **trastorno de cefalea**, con **1 ensayo clínico** (en curso, sin resultados) y **2 publicaciones** de apoyo indirecto.
Ningún estudio citado evalúa tenoxicam de forma directa en esta indicación con resultados concluyentes.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Brachydactyly-syndactyly syndrome |
| Puntaje de Predicción TxGNN | 0.9980 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 2) |
| Número de Autorizaciones | 2 (vigentes: 1) |
| Decisión Recomendada | Hold (línea de investigación) |

> Nota: se presenta la predicción de mayor interés clínico. Los puestos 1 y 2 del modelo (síndrome de braquidactilia-sindactilia y síndrome de microftalmia colobomatosa-displasia rizomélica) tienen puntajes algo superiores, pero carecen de cualquier evidencia y de vínculo mecanístico, por lo que se descartan como líneas de trabajo.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento general, tenoxicam es un AINE que inhibe la ciclooxigenasa (COX-1 y COX-2) y reduce la síntesis de prostaglandinas, lo que explica su efecto antiinflamatorio y analgésico en patología articular.

Las prostaglandinas participan en la inflamación neurogénica y la sensibilización al dolor de la migraña y otras cefaleas primarias. Los AINE son una clase establecida para el tratamiento de la migraña aguda, de modo que la predicción es mecanísticamente coherente a nivel de clase.

Sin embargo, el respaldo específico de tenoxicam es limitado: hay un ensayo de fase 4 en curso y literatura observacional o comparativa sobre AINE y triptanes, no ensayos controlados con tenoxicam que hayan finalizado.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06786650](https://clinicaltrials.gov/study/NCT06786650) | Fase 4 | Activo, sin reclutamiento | 100 | Compara tenoxicam intravenoso con ibuprofeno intravenoso para aliviar la cefalea en el ataque agudo de migraña. Inicio en mayo de 2024; sin resultados disponibles. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27813032](https://pubmed.ncbi.nlm.nih.gov/27813032/) | 2016 | Cohorte | Agri | Compara triptanes, AINE y su combinación en el tratamiento del ataque de migraña (estudio de clase, no específico de tenoxicam). |
| [18345416](https://pubmed.ncbi.nlm.nih.gov/18345416/) | 2007 | Cohorte | Arquivos de Neuro-Psiquiatria | Revisión de historias de 109 pacientes con cefaleas primarias agudas en un centro de urgencias; la migraña probable fue el diagnóstico más frecuente. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 58665 | REUTENOX 20 mg comprimidos recubiertos (vigente) | Comprimido recubierto | Sin texto de indicación disponible |
| 60557 | REUTENOX 20 mg granulado para suspensión oral (cancelada) | Granulado para suspensión oral | Sin texto de indicación disponible |

## Consideraciones de Seguridad

- **Señal de seguridad relacionada:** una publicación de 1997 (PMID 9303679) describe un caso de alopecia secundaria a tenoxicam, como posible reacción adversa no descrita previamente. Esto va en contra de la predicción de beneficio para alopecia.
- No se encontraron interacciones farmacológicas registradas en los datos compilados.

Consultar el prospecto para información completa de advertencias y contraindicaciones.

## Otras Predicciones del Modelo (Resumen)

| Enfermedad predicha | Puntaje TxGNN | Nivel | Valoración |
|------|------|------|------|
| Síndrome de braquidactilia-sindactilia | 0,9980 | L5 | Sin vínculo mecanístico ni evidencia; trastorno congénito genético |
| Síndrome de microftalmia colobomatosa-displasia rizomélica | 0,9980 | L5 | Sin vínculo mecanístico ni evidencia |
| Hipotricosis simple del cuero cabelludo | 0,9966 | L5 | Sin vínculo mecanístico ni evidencia |
| Hipotricosis congénita con milia | 0,9966 | L5 | Sin vínculo mecanístico ni evidencia |
| Alopecia areata difusa | 0,9961 | L5 | Especulativa; sin evidencia |
| Cefalea autonómica trigeminal | 0,9961 | L5 | Solo extrapolación indirecta desde otro AINE (indometacina); ningún estudio citado aborda esta enfermedad |
| Alopecia | 0,9960 | L5 | La única publicación sugiere un efecto adverso, no un beneficio |

## Conclusión y Próximos Pasos

**Decisión: Hold (línea de investigación)**

**Justificación:**
La predicción de trastorno de cefalea es plausible a nivel de clase de AINE y cuenta con un ensayo de fase 4 directamente relacionado, pero aún sin resultados, y con literatura solo observacional. No hay un ensayo controlado completado que permita concluir eficacia de tenoxicam.

**Para avanzar se necesita:**
- Resultados del ensayo NCT06786650 (tenoxicam IV frente a ibuprofeno IV en migraña aguda).
- Datos del mecanismo de acción y de las advertencias y contraindicaciones del prospecto de la AEMPS (actualmente faltan y bloquean el cribado de seguridad).
- Texto de indicación de las autorizaciones españolas para confirmar los usos aprobados.
- Si se prosigue, revisar la señal de alopecia como posible reacción adversa.
- Descartar las predicciones de enfermedades congénitas raras y de alopecia por falta de respaldo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


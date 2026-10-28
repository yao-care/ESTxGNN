---
layout: default
title: Galcanezumab
parent: Solo predicción del modelo (L5)
nav_order: 369
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
monitor_inn: "GALCANEZUMAB"
predicted_indications: ["heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis"]
description: "Galcanezumab: nueva indicación predicha, Deficiencia de cofactor II de la heparina (heparin cofactor 2 deficiency) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Galcanezumab
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

## Galcanezumab: Deficiencia de cofactor II de la heparina (heparin cofactor 2 deficiency)
{: .text-alpha }

## Resumen en Una Frase

Galcanezumab es un anticuerpo monoclonal que neutraliza el péptido relacionado con el gen de la calcitonina (CGRP), originalmente utilizado para el tratamiento de la migraña.
El modelo TxGNN predice que podría ser efectivo para la **deficiencia de cofactor II de la heparina**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Deficiencia de cofactor II de la heparina (heparin cofactor 2 deficiency) |
| Puntaje de Predicción TxGNN | 0.9950 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 2) |
| Número de Autorizaciones | 2 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

En los datos compilados para este informe, el mecanismo de acción original del fármaco no figura de forma detallada. Según la información conocida, galcanezumab es un anticuerpo monoclonal que neutraliza el CGRP y actúa sobre la vía trigeminovascular, lo que explica su eficacia en la migraña.

**La predicción no resulta biológicamente razonable.** La deficiencia de cofactor II de la heparina es una trombofilia causada por una menor inhibición de la trombina (vía SERPIND1) y no involucra la señalización del CGRP. No se ha identificado ningún vínculo mecanístico creíble entre ambas condiciones.

El puntaje alto (0,995) parece ser un artefacto del modelo TxGNN (aprendizaje profundo), probablemente por proximidad en la red a procesos vasculares o de coagulación. Además, las otras dos predicciones principales (deficiencia de antitrombina tipo 2, con 0,9941, y exceso de factor 5 con trombosis espontánea, con 0,9941) son también trombofilias con puntajes casi idénticos. Esto sugiere un artefacto común del modelo y no señales independientes.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1181330001 | EMGALITY 120 MG solución inyectable en pluma precargada | Solución inyectable | No disponible en los datos |
| 1181330003 | EMGALITY 120 MG solución inyectable en jeringa precargada | Solución inyectable | No disponible en los datos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico creíble entre el bloqueo del CGRP y las trombofilias hereditarias. Los tres candidatos predichos presentan el mismo patrón, lo que apunta a un artefacto del modelo TxGNN (aprendizaje profundo).

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) del fármaco
- Advertencias y contraindicaciones del prospecto de AEMPS, necesarias para cualquier evaluación de seguridad
- Un fundamento biológico plausible que relacione la vía del CGRP con la inhibición de la trombina
- Estudios preclínicos o de mecanismo que justifiquen reconsiderar la hipótesis
- Valorar la posible consideración de la seguridad vascular y trombótica de los inhibidores del CGRP en estos pacientes antes de cualquier uso
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


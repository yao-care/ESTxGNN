---
layout: default
title: Selinexor
parent: Solo predicción del modelo (L5)
nav_order: 729
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Selinexor: nueva indicación predicha, Osteoporosis inducida por fármacos (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (el texto de indicación de la a…"
monitor_inn: "SELINEXOR"
predicted_indications: ["drug-induced osteoporosis"]
---

# Selinexor
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Selinexor: De Indicación Original No Disponible a Osteoporosis Inducida por Fármacos
{: .text-alpha }

## Resumen en Una Frase

Selinexor es un inhibidor selectivo de la exportación nuclear (XPO1/CRM1) comercializado en España como NEXPOVIO. En los datos compilados para este informe no consta el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **osteoporosis inducida por fármacos**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; la predicción se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (el texto de indicación de la autorización está vacío) |
| Nueva Indicación Predicha | Osteoporosis inducida por fármacos |
| Puntaje de Predicción TxGNN | 0,9922 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, selinexor es un inhibidor selectivo de la exportación nuclear que actúa sobre XPO1/CRM1 y es un fármaco oncológico.

Una hipótesis plausible, pero no verificada, es que la inhibición de XPO1 modifique vías de señalización relevantes para la remodelación ósea (por ejemplo, NF-κB, Wnt/β-catenina o la regulación de osteoclastos y osteoblastos). Este vínculo es especulativo y no está respaldado por evidencia aportada.

Además, selinexor es un fármaco oncológico con toxicidad significativa (citopenias, náuseas, anorexia, pérdida de peso, fatiga), por lo que no encaja de forma evidente en una enfermedad crónica y no mortal como la osteoporosis inducida por fármacos. Su perfil de seguridad y las 81 interacciones farmacológicas registradas pesan en contra de su uso en este contexto sin datos que lo respalden. La similitud con la indicación original aún está pendiente de evaluar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1211537001 | NEXPOVIO 20 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor selectivo de la exportación nuclear XPO1) |
| Riesgo de Mielosupresión | Medio a alto (se describen citopenias como toxicidad relevante; confirmar en el prospecto) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto (se describen náuseas como toxicidad frecuente) |
| Items de Monitoreo | Hemograma completo, función hepática y renal, electrolitos, peso y estado nutricional |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registran 81 interacciones en total. Entre las principales mostradas:
  - **Mayores**: deferiprona, samario (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribina y clozapina.
  - **Moderadas**: cloruro de estroncio Sr-89, roflumilast, cloranfenicol (incluida la forma oftálmica), zidovudina, alefacept, alemtuzumab, anakinra, azatioprina, canakinumab, además de vacunas (toxoide tetánico, ántrax, cólera vivo).
  - Muchas de ellas afectan a la médula ósea o al sistema inmunitario, lo que sugiere riesgo aditivo de mielosupresión e inmunosupresión.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única base es una puntuación alta del modelo TxGNN (nivel de evidencia L5), sin ensayos clínicos ni literatura, con un vínculo mecanístico especulativo y un perfil de toxicidad desfavorable para una enfermedad crónica no mortal.

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones del prospecto de AEMPS (brecha bloqueante para el cribado de seguridad).
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar la indicación aprobada de la autorización española.
- Estudios preclínicos que respalden el efecto de la inhibición de XPO1 sobre el metabolismo óseo.
- Revisión sistemática de literatura sobre selinexor y salud ósea.
- Evaluación de la relación beneficio-riesgo frente a las alternativas existentes para la osteoporosis inducida por fármacos.
- Evaluación de compatibilidad de vía de administración y similitud con la indicación original (actualmente pendientes).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


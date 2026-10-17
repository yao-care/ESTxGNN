---
layout: default
title: Nadifloxacin
parent: Solo predicción del modelo (L5)
nav_order: 548
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Nadifloxacin: nueva indicación predicha, Malaria (nivel de evidencia L5). Indicación original: Acné (según la base de conocimiento del modelo"
monitor_inn: "nadifloxacin"
predicted_indications: ["malaria"]
---

# Nadifloxacin
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

# Nadifloxacino: De Acné a Malaria

## Resumen en Una Frase

Nadifloxacino es una fluoroquinolona de uso tópico, comercializada en España en crema al 1% y utilizada originalmente para el tratamiento del acné.
El modelo TxGNN predice que podría ser efectivo para **malaria**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: la predicción se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Acné (según la base de conocimiento del modelo; el texto de indicación de la autorización de AEMPS no está disponible) |
| Nueva Indicación Predicha | Malaria |
| Puntaje de Predicción TxGNN | 99.16% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, nadifloxacino es una fluoroquinolona tópica que inhibe la ADN girasa y la topoisomerasa IV bacterianas, y su uso en acné está relacionado con su actividad antibacteriana sobre la piel.

Un vínculo mecanístico plausible, pero no verificado, es que los parásitos *Plasmodium* poseen una ADN girasa localizada en el apicoplasto, que es una diana conocida de fluoroquinolonas como el ciprofloxacino en estudios preclínicos antipalúdicos. Esto sugeriría una posible actividad teórica frente al parásito.

Sin embargo, nadifloxacino está formulado y comercializado para uso tópico en acné, por lo que la exposición sistémica probablemente sea demasiado baja para alcanzar concentraciones antipalúdicas. Ningún dato compilado para este informe respalda esta hipótesis, que sigue siendo especulativa. La relación entre la indicación original (infección/inflamación cutánea) y la malaria (infección parasitaria sistémica) es, además, distante.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 64291 | NADIXA 1% CREMA (Ferrer Internacional S.A.) | Crema | No disponible en los datos compilados |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en un puntaje alto del modelo (nivel L5), sin ensayos clínicos ni literatura. Además, la vía tópica del producto autorizado probablemente no permita alcanzar concentraciones sistémicas antipalúdicas.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de AEMPS (advertencias y contraindicaciones), actualmente sin datos y que bloquea el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Estudios preclínicos in vitro de actividad de nadifloxacino frente a *Plasmodium* (p. ej., inhibición de la girasa del apicoplasto)
- Evaluar la viabilidad de exposición sistémica y la compatibilidad de vías de administración (hoy pendiente)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


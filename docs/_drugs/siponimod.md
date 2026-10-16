---
layout: default
title: Siponimod
parent: Solo predicción del modelo (L5)
nav_order: 739
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Siponimod: nueva indicación predicha, Hipertensión pulmonar (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (el texto de indicación de las…"
---

# Siponimod
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Siponimod: De Indicación Original No Especificada a Hipertensión Pulmonar

## Resumen en Una Frase

Siponimod es un modulador selectivo de los receptores S1P1/S1P5 que se comercializa en España con el nombre Mayzent. Los datos compilados para este informe no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (el texto de indicación de las autorizaciones está vacío) |
| Nueva Indicación Predicha | Hipertensión pulmonar |
| Puntaje de Predicción TxGNN | 99,68 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos. Según la información conocida, siponimod es un modulador selectivo de los receptores de esfingosina-1-fosfato (S1P1 y S1P5). Estos receptores intervienen en la migración de los linfocitos y en la función de barrera endotelial.

La señalización de S1P se ha relacionado con la remodelación vascular pulmonar y con la función de barrera del endotelio, lo que ofrece un posible vínculo teórico con la hipertensión pulmonar. Sin embargo, la modulación de S1P1 provoca bradicardia transitoria y podría tener efectos impredecibles sobre la vasculatura pulmonar.

Este vínculo es puramente computacional (puntaje alto de TxGNN) y no cuenta con ensayos ni literatura de apoyo. No se pudo establecer la relación con la indicación original, ya que esta no figura en los datos.

### Otras predicciones del modelo (para contexto)

| Posición | Indicación predicha | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|------|
| 2 | Trastorno de migraña | 99,66 % | L4 | Solo un reporte de caso/comentario (2022) y una entrada genérica de «Neurología» |
| 3 | Cardiopatía cifoscoliótica | 99,56 % | L5 | Sin vínculo mecanístico plausible; probable artefacto del grafo |
| 4 | Migraña con aura de tronco encefálico | 99,56 % | L4 | Misma publicación de 2022, no específica |
| 5 | Susceptibilidad a migraña con o sin aura | 99,49 % | L4 | Evidencia indirecta, redundante con otras migrañas |
| 6 | Angina de Prinzmetal | 99,34 % | L5 | Sin evidencia; preocupación de seguridad cardíaca |
| 7 | Artritis reumatoide | 99,16 % | L4 | La más plausible biológicamente (secuestro linfocitario), aún en fase de hipótesis |
| 8 | Atrofodermia vermiculada | 99,10 % | L5 | Sin vínculo mecanístico; probable artefacto computacional |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para hipertensión pulmonar.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191414003 | MAYZENT 2 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 1191414001 | MAYZENT 0,25 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 1191414007 | MAYZENT 1 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |

Titular de las tres autorizaciones: Novartis Europharm Limited.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las que se muestran, muchas son de nivel **Mayor**:
  - Antiácidos/antagonistas H2: famotidina, ranitidina, cimetidina.
  - Corticosteroides: hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida.
  - Antieméticos: aprepitant, dolasetrón, palonosetrón.
  - Antibióticos: claritromicina, levofloxacino.
  - Otros: oxandrolona.
  - De nivel **Moderado**: loperamida, bisacodilo, ácido picosulfúrico, polietilenglicol 3350 con electrolitos, sulfato de sodio, naltrexona.
- **Consideración cardíaca (según el análisis de la predicción)**: la modulación de S1P1 puede causar bradicardia y retraso de la conducción auriculoventricular. Esto es especialmente relevante en hipertensión pulmonar, cardiopatía cifoscoliótica y angina de Prinzmetal.

Para advertencias y contraindicaciones, consultar el prospecto, ya que no se dispone de esos datos.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipertensión pulmonar se basa únicamente en el modelo (L5), sin ensayos ni literatura, con un vínculo mecanístico débil y posibles riesgos cardiovasculares. Entre las demás predicciones, solo la artritis reumatoide muestra un fundamento de clase razonable, aunque sigue en fase de hipótesis.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicación aprobada), un vacío crítico que impide el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Estudios preclínicos de siponimod en modelos de hipertensión pulmonar.
- Evaluación específica del riesgo cardiovascular (bradicardia, conducción AV) en pacientes con enfermedad cardiopulmonar.
- Priorizar, de forma exploratoria, la revisión de la hipótesis de artritis reumatoide como alternativa más plausible.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


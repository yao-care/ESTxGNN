---
layout: default
title: Midecamycin
parent: Solo predicción del modelo (L5)
nav_order: 526
evidence_level: L5
indication_count: 1
---

# Midecamycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Midecamicina: De Indicación Original No Registrada a Candidiasis

## Resumen en Una Frase

Midecamicina es un antibiótico macrólido de 16 miembros, comercializado en España como MYOXAM; los datos disponibles no recogen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **candidiasis**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (el texto de indicación de las autorizaciones está vacío) |
| Nueva Indicación Predicha | Candidiasis |
| Puntaje de Predicción TxGNN | 99.02% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, midecamicina es un antibiótico macrólido de 16 miembros que inhibe la síntesis proteica bacteriana al unirse a la subunidad ribosomal 50S, y su uso establecido es antibacteriano.

Los macrólidos no se consideran, en general, agentes antifúngicos, y los datos compilados no respaldan un mecanismo directo de actividad frente a *Candida*. El puntaje elevado de TxGNN (0,990) proviene de la estructura del grafo de conocimiento y puede reflejar cercanía de red con otros antiinfecciosos, más que un vínculo terapéutico real.

Cualquier mecanismo plausible (inhibición ribosomal débil en hongos, efectos inmunomoduladores de los macrólidos o sinergia con azoles) es especulativo y no tiene evidencia aquí. Además, la exposición a antibióticos es un factor de riesgo conocido de candidiasis, por lo que la asociación predicha podría estar confundida en sentido contrario.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 64153 | MYOXAM 600 mg, granulado para suspensión oral | Granulado para suspensión oral | No disponible |
| 61271 | MYOXAM 900 mg, granulado para suspensión oral | Granulado para suspensión oral | No disponible |
| 57810 | MYOXAM 600 mg comprimidos recubiertos | Comprimido recubierto | No disponible |

Las tres autorizaciones corresponden a monofármacos vigentes del Laboratorio Menarini S.A.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos ni literatura, y no hay un fundamento mecanístico plausible para un macrólido frente a *Candida*; además, el uso de antibióticos es un factor de riesgo de candidiasis.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), requisito bloqueante para el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Estudios preclínicos in vitro de actividad frente a *Candida* (solo o combinado con azoles)
- Revisión de literatura sobre efectos antifúngicos o inmunomoduladores de los macrólidos
- Evaluar la compatibilidad de vías de administración con las formas de candidiasis de interés
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Ataluren
parent: Solo predicción del modelo (L5)
nav_order: 71
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Ataluren: nueva indicación predicha, Colestasis intrahepática recurrente benigna (nivel de evidencia L5). Indicación original: Distrofia muscular de Duchenne (según el grafo de conocimiento"
monitor_inn: "ataluren"
predicted_indications: ["benign recurrent intrahepatic cholestasis", "inborn disorder of bilirubin metabolism", "hereditary North American Indian childhood cirrhosis", "familial intrahepatic cholestasis", "severe nonproliferative diabetic retinopathy", "bilirubin metabolism disease"]
---

# Ataluren
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Ataluren: De Distrofia Muscular de Duchenne a Colestasis Intrahepática Recurrente Benigna

## Resumen en Una Frase

Ataluren es un fármaco que promueve la lectura completa de codones de parada prematuros (mutaciones sin sentido), utilizado originalmente en la distrofia muscular de Duchenne.
El modelo TxGNN predice que podría ser efectivo para **colestasis intrahepática recurrente benigna**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Distrofia muscular de Duchenne (según el grafo de conocimiento; el texto de indicación autorizado en AEMPS no está disponible) |
| Nueva Indicación Predicha | Colestasis intrahepática recurrente benigna |
| Puntaje de Predicción TxGNN | 99.42% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, ataluren promueve la lectura completa (*readthrough*) ribosómica de codones de parada prematuros, lo que permite producir proteínas funcionales completas en enfermedades causadas por mutaciones sin sentido. Su uso original se centra en la distrofia muscular de Duchenne.

La colestasis intrahepática recurrente benigna está causada por variantes en *ATP8B1* (y en ocasiones *ABCB11*). Un subconjunto de estas variantes son mutaciones sin sentido, por lo que un mecanismo de lectura completa es teóricamente plausible para esos pacientes.

No obstante, la eficacia dependería del genotipo sin sentido específico de cada paciente, y no se dispone de datos de seguridad hepática ni de exposición en este contexto. El puntaje elevado del modelo es solo una predicción computacional.

### Otras indicaciones predichas (para contexto)

| Rango | Indicación | Puntaje TxGNN | Plausibilidad mecanística |
|------|------|------|------|
| 2 | Trastorno congénito del metabolismo de la bilirrubina | 99.40% | Posible solo en subconjuntos con variantes sin sentido (p. ej., UGT1A1); categoría heterogénea |
| 3 | Cirrosis infantil hereditaria de indios norteamericanos | 99.33% | Débil: variante de cambio de sentido (missense), no sin sentido |
| 4 | Colestasis intrahepática familiar | 99.26% | Teórica para subconjuntos con variantes sin sentido; requiere validación preclínica |
| 5 | Retinopatía diabética no proliferativa grave | 99.24% | Sin vínculo claro; probable artefacto del grafo de conocimiento |
| 6 | Enfermedad del metabolismo de la bilirrubina | 99.11% | Categoría general, demasiado inespecífica |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 113902001 | Translarna 125 mg granulado para suspensión oral | Granulado para suspensión oral | No disponible en los datos compilados |
| 113902002 | Translarna 250 mg granulado para suspensión oral | Granulado para suspensión oral | No disponible en los datos compilados |
| 113902003 | Translarna 1000 mg granulado para suspensión oral | Granulado para suspensión oral | No disponible en los datos compilados |

Titular: PTC Therapeutics International Limited. Las tres autorizaciones están vigentes y son de principio activo único.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura. Aunque el mecanismo de lectura completa es plausible para un subconjunto de pacientes con variantes sin sentido, no hay evidencia que lo respalde en esta indicación.

**Para avanzar se necesita:**
- Obtener y analizar las advertencias y contraindicaciones del prospecto de AEMPS (bloqueante para el cribado de seguridad).
- Completar los datos del mecanismo de acción del fármaco.
- Identificar pacientes con variantes sin sentido en *ATP8B1* o *ABCB11* y validar la eficiencia de la lectura completa en modelos preclínicos con genotipo definido.
- Obtener datos de seguridad y exposición hepática.
- Estrechar las indicaciones más amplias (bilirrubina, colestasis familiar) a un gen y genotipo específicos antes de evaluarlas.
- Descartar la retinopatía diabética y la cirrosis infantil de indios norteamericanos como candidatas, salvo que surja respaldo independiente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


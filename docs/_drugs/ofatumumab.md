---
layout: default
title: Ofatumumab
parent: Solo predicción del modelo (L5)
nav_order: 390
evidence_level: L5
indication_count: 8
---

# Ofatumumab
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

# Ofatumumab: De Indicación Original No Registrada a Leucemia Linfocítica Crónica/Linfoma Linfocítico Pequeño con Hipermutación Somática del Gen IGHV

## Resumen en Una Frase

Ofatumumab es un anticuerpo monoclonal anti-CD20 comercializado en España como Kesimpta, pero los datos recibidos no incluyen su indicación original.
El modelo TxGNN predice que podría ser efectivo para **leucemia linfocítica crónica/linfoma linfocítico pequeño (LLC/LLP) con hipermutación somática del gen IGHV**.
Para este subtipo concreto hay **0 ensayos clínicos** y **0 publicaciones**, por lo que la predicción se apoya solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (el texto de indicación aprobada está vacío en el registro) |
| Nueva Indicación Predicha | LLC/LLP con hipermutación somática del gen de la región variable de la cadena pesada de inmunoglobulina (IGHV) |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información conocida, ofatumumab es un anticuerpo monoclonal dirigido contra CD20, una proteína presente en la superficie de los linfocitos B. Su actividad se atribuye a la citotoxicidad dependiente del complemento y a la citotoxicidad celular dependiente de anticuerpos (ADCC).

Las células de la LLC/LLP expresan CD20, así que un anticuerpo anti-CD20 es plausible en esta enfermedad. El subtipo predicho es una variante molecular de la LLC/LLP, definida por la hipermutación somática del gen IGHV.

Esta plausibilidad viene de la entidad general LLC/LLP, no de estudios en este subtipo. Los datos recibidos no contienen ensayos ni literatura específicos del subtipo, y el puntaje es solo una predicción basada en grafos. El subtipo "LLC/LLP pregerminal" recibió exactamente el mismo puntaje (99.77%), lo que sugiere que ambos comparten el mismo entorno en el grafo y no que haya evidencia independiente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para este subtipo.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para este subtipo.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 121532003 | KESIMPTA 20 mg SOLUCIÓN INYECTABLE EN PLUMA PRECARGADA | Solución inyectable en pluma precargada | No especificada en el registro |

El titular es Novartis Europharm Limited. La presentación registrada es una pluma precargada, mientras que los ensayos de otras indicaciones de ofatumumab incluidos en el paquete de evidencia usan infusión intravenosa. La compatibilidad de vía de administración aún está pendiente de evaluar.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida / inmunoterapia (anticuerpo monoclonal anti-CD20) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para este subtipo no hay ensayos clínicos ni publicaciones (nivel L5), y el puntaje alto de TxGNN no basta por sí solo para avanzar. Además, faltan las advertencias y contraindicaciones del prospecto de la AEMPS, que bloquean el cribado de seguridad.

Este resultado no significa que ofatumumab carezca de evidencia en la LLC/LLP en general. Otras predicciones del mismo paquete tienen más respaldo:
- **LLC/LLP (entidad general)**: nivel L1, con varios ensayos de Fase 3 completados, en los que ofatumumab es a menudo el comparador. Probablemente sea una indicación ya aprobada, no un reposicionamiento.
- **Linfoma folicular**: nivel L2, con ensayos de Fase 2 completados y un ensayo de Fase 3 terminado anticipadamente.

**Para avanzar se necesita:**
- Descargar el prospecto de la AEMPS para obtener advertencias y contraindicaciones (brecha bloqueante).
- Confirmar el mecanismo de acción en DrugBank.
- Completar la indicación original y aprobada, y contrastar la LLC/LLP con la ficha técnica antes de presentarla como reposicionamiento.
- Buscar datos específicos por subtipo de IGHV, por ejemplo análisis de subgrupos de los ensayos de LLC/LLP.
- Evaluar la compatibilidad entre la pluma subcutánea registrada y la vía intravenosa de los ensayos.
- Aclarar el posicionamiento frente a rituximab y obinutuzumab.

*Este informe es solo para referencia de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


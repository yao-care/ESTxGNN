---
layout: default
title: Methionine
parent: Solo predicción del modelo (L5)
nav_order: 511
evidence_level: L5
indication_count: 10
---

# Methionine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Metionina: De Pomada Oftálmica Epitelizante a Acné (predicción principal)

## Resumen en Una Frase

La metionina es un aminoácido esencial que en España está autorizado como componente de una pomada oftálmica epitelizante (combinación de tres principios activos), sin que los datos compilados detallen su indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para **acné**, con **0 ensayos clínicos** y **2 publicaciones** de apoyo indirecto.
La evidencia es muy débil: la predicción es esencialmente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (pomada oftálmica epitelizante) |
| Nueva Indicación Predicha | Acné |
| Puntaje de Predicción TxGNN | 99,9996% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

> **Nota importante:** las 10 predicciones principales incluyen 8 relacionadas con la catarata o la retina. Dado que el producto autorizado es oftálmico, la indicación más coherente para explorar es la **catarata diabética** (único caso con calificación "Pregunta de investigación"). Se detalla en la sección final.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la metionina es un aminoácido azufrado que participa en el ciclo de la metionina y la homocisteína, y en este caso forma parte de una pomada oftálmica combinada con efecto epitelizante.

Para el **acné**, el vínculo es débil. Un estudio (PMID 11277950) halló homocisteína plasmática elevada en pacientes tratados con isotretinoína por acné quístico. La homocisteína pertenece al ciclo de la metionina, pero esto es una asociación metabólica, no evidencia de que la metionina trate el acné. El segundo artículo (caso clínico de mutación de MTHFR) no tiene relevancia evidente para el acné.

Con el puntaje de TxGNN muy alto (0,99999) pero sin ensayos clínicos, conviene tratarlo como una señal del grafo de conocimiento que requiere validación independiente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Observacional | Int J Dermatol | Homocisteína plasmática elevada en pacientes con acné quístico tratados con isotretinoína; asociación metabólica indirecta |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Reporte de caso | BMJ Case Reports | Mutación de MTHFR con encefalopatía neonatal, alopecia y rasgos marfanoides; el acné neonatal es un hallazgo incidental |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 25908 | Pomada Ojos Epitelizante 3 mg/g + 5,5 mg/g + 5 mg/g (Laboratoires Thea) | Pomada oftálmica | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proceden del prospecto):** hipertensión, enfermedad renal (incluida la insuficiencia renal crónica y terminal), diabetes mellitus y cetoacidosis diabética, hipercalcemia, nefrocalcinosis, nefrolitiasis, cardiopatía y enfermedad cardiovascular, hiperlipidemia (incluida la familiar), sarcoidosis, trastornos del metabolismo del fósforo, nefropatía aguda por uratos, intoxicación digitálica, fibrilación ventricular, fenilcetonuria y trastornos del metabolismo de la fenilalanina. Deben verificarse con el prospecto, ya que estas relaciones proceden de asociaciones del grafo y no de la ficha técnica.
- **Interacciones farmacológicas (5 registradas):**
  - Carbón activado: **moderada**.
  - Efedrina, pseudoefedrina, mexiletina y flecainida: **menores**.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones oficiales).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para acné se basa solo en el modelo y en literatura indirecta, sin ensayos clínicos (nivel L5). Entre las demás predicciones, la **catarata diabética** (nivel L4) es la más plausible mecanísticamente: la metionina sulfóxido reductasa B1 protege a las células epiteliales del cristalino frente al daño oxidativo inducido por glucosa alta y peroxinitrito (PMID 23270945 y 22713178). Aun así, estos estudios abordan la enzima de reparación, no la suplementación con metionina, y esta podría elevar la homocisteína. Se mantiene como pregunta de investigación, no como candidata a avance clínico.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada), que es un bloqueo para el cribado de seguridad.
- Datos del mecanismo de acción desde DrugBank.
- Estudios preclínicos que evalúen la metionina tópica u oftálmica en modelos de catarata diabética.
- Evaluar el riesgo de hiperhomocisteinemia con exposición sistémica o local.
- Definir la compatibilidad de la vía de administración (oftálmica) con cada indicación predicha; para acné, la vía dérmica no está evaluada.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


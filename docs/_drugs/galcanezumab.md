---
layout: default
title: Galcanezumab
parent: Solo predicción del modelo (L5)
nav_order: 253
evidence_level: L5
indication_count: 3
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Galcanezumab: De Migraña a Deficiencia de Cofactor II de la Heparina

## Resumen en Una Frase

Galcanezumab es un anticuerpo monoclonal que neutraliza el péptido CGRP y está comercializado en España con el nombre Emgality. Los registros de autorización recibidos no indican su indicación original.
El modelo TxGNN predice que podría ser efectivo para la **deficiencia de cofactor II de la heparina**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en los registros de autorización recibidos |
| Nueva Indicación Predicha | Deficiencia de cofactor II de la heparina |
| Puntaje de Predicción TxGNN | 99.50% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, galcanezumab es un anticuerpo monoclonal que neutraliza el CGRP (péptido relacionado con el gen de la calcitonina). La deficiencia de cofactor II de la heparina es un defecto en un inhibidor de serina proteasas de la trombina.

**No se identificó ningún vínculo mecanístico plausible.** La señalización del CGRP no participa en la vía de inhibición de la trombina. El puntaje alto de TxGNN (0.995) proviene de una predicción basada en grafos de conocimiento, sin ensayos ni literatura que la respalden, y no debe interpretarse como apoyo biológico.

El CGRP tiene funciones vasodilatadoras. Por eso, cualquier efecto en una condición trombofílica requeriría una revisión de seguridad antes de considerarse un posible beneficio.

Las otras dos predicciones principales (deficiencia de antitrombina tipo 2, con 99.41%, y exceso de factor V con trombosis espontánea, con 99.41%) tampoco tienen ensayos, publicaciones ni vínculo mecanístico. Todas son trastornos de la coagulación, lo que sugiere un artefacto del grafo de conocimiento compartido entre estas enfermedades y no una señal específica del fármaco.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1181330001 | EMGALITY 120 MG SOLUCIÓN INYECTABLE EN PLUMA PRECARGADA | Solución inyectable | No especificada en el registro |
| 1181330003 | EMGALITY 120 MG SOLUCIÓN INYECTABLE EN JERINGA PRECARGADA | Solución inyectable | No especificada en el registro |

Ambas autorizaciones corresponden a Eli Lilly Nederland B.V.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos ni literatura y sin vínculo mecanístico plausible con el CGRP. Además, el contexto trombofílico exige cautela por el papel vasodilatador del CGRP.

**Para avanzar se necesita:**
- Ficha técnica de la AEMPS (advertencias y contraindicaciones), un bloqueo para el cribado de seguridad
- Datos del mecanismo de acción (MOA) desde DrugBank
- Indicación aprobada de las autorizaciones españolas, ausente en los registros recibidos
- Una hipótesis biológica que justifique la predicción, con revisión de seguridad sobre riesgo trombótico, antes de considerar cualquier estudio

*Este informe es solo para referencia de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Ataluren
parent: Solo predicción del modelo (L5)
nav_order: 71
evidence_level: L5
indication_count: 6
monitor_inn: "ataluren"
predicted_indications: ["benign recurrent intrahepatic cholestasis", "inborn disorder of bilirubin metabolism", "hereditary North American Indian childhood cirrhosis", "familial intrahepatic cholestasis", "severe nonproliferative diabetic retinopathy", "bilirubin metabolism disease"]
last_modified_at: 2026-11-20
description: "Ataluren: nueva indicación predicha, colestasis intrahepática recurrente benigna (benign recurrent intrahepatic cholestasis) (nivel de evidencia L5). Indicación original: No consta en los datos local…"
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

## Ataluren: promotor de la lectura continua de codones de parada prematuros → colestasis intrahepática recurrente benigna (benign recurrent intrahepatic cholestasis)
{: .text-alpha }

## Resumen en Una Frase

Ataluren es un fármaco oral que favorece la lectura continua ribosómica de los codones de parada prematuros (mutaciones sin sentido).
El modelo TxGNN predice que podría ser efectivo para **colestasis intrahepática recurrente benigna (benign recurrent intrahepatic cholestasis)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | colestasis intrahepática recurrente benigna (benign recurrent intrahepatic cholestasis) |
| Puntaje de Predicción TxGNN | 0,9942 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Autorizado pero no comercializado (registros: 3) |
| Número de Autorizaciones | 3 (comercializadas: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Ataluren es (traducción no oficial): «Modulador del ribosoma 80S» Texto original en inglés: "80S Ribosome modulator" ([ChEMBL CHEMBL256997 (ataluren): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL256997), CC BY-SA 3.0; consultado el 2026-11-19). Según la información conocida, ataluren promueve la lectura continua ribosómica de codones de parada prematuros, es decir, de mutaciones sin sentido, de modo que la célula pueda producir una proteína de longitud completa.

La colestasis intrahepática recurrente benigna se debe a variantes del gen ATP8B1 (y en ocasiones ABCB11). Un subconjunto de estas variantes son mutaciones sin sentido, por lo que, en teoría, la lectura continua podría ser aplicable a esos pacientes.

Esta plausibilidad es solo teórica. No se aportaron ensayos ni literatura, la eficacia dependería del genotipo sin sentido de cada paciente, y no se dispone de datos de seguridad hepática ni de exposición en este contexto. La puntuación alta del modelo es una predicción computacional, no una prueba de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 113902002 | TRANSLARNA 250 MG GRANULADO PARA SUSPENSION ORAL | Granulado para suspensión oral | No registrada en los datos locales |
| 113902003 | TRANSLARNA 1000 MG GRANULADO PARA SUSPENSION ORAL | Granulado para suspensión oral | No registrada en los datos locales |
| 113902001 | TRANSLARNA 125 MG GRANULADO PARA SUSPENSION ORAL | Granulado para suspensión oral | No registrada en los datos locales |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni publicación que estudie directamente esta enfermedad con ataluren, por lo que el nivel de evidencia es L5. La puntuación del modelo no basta por sí sola para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados en fuentes oficiales
- Información de seguridad del prospecto de la AEMPS (advertencias y contraindicaciones)
- Validación preclínica en modelos definidos por genotipo (variantes sin sentido de ATP8B1/ABCB11)
- Evaluación de la eficacia de la lectura continua en estos genes y de la seguridad hepática
- Definición de la población diana según genotipo antes de cualquier estudio clínico

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [ChEMBL CHEMBL256997 (ataluren): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL256997) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


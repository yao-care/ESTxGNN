---
layout: default
title: Lumacaftor
parent: Solo predicción del modelo (L5)
nav_order: 490
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-05
description: "Lumacaftor: nueva indicación predicha, Lepra (nivel de evidencia L5). Indicación original: Fibrosis quística"
monitor_inn: "lumacaftor"
predicted_indications: ["leprosy"]
---

# Lumacaftor
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

## Lumacaftor: De Fibrosis Quística a Lepra
{: .text-alpha }

## Resumen en Una Frase

Lumacaftor es un fármaco utilizado originalmente para el tratamiento de la fibrosis quística, comercializado en España como parte de la combinación Orkambi.
El modelo TxGNN predice que podría ser efectivo para **lepra**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; la predicción se basa únicamente en el modelo computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Fibrosis quística |
| Nueva Indicación Predicha | Lepra |
| Puntaje de Predicción TxGNN | 0.9944 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 5 de 5) |
| Número de Autorizaciones | 5 (comercializadas: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para lumacaftor and ivacaftor (combinación que contiene Lumacaftor) (traducción no oficial): «El lumacaftor mejora la estabilidad conformacional de la F508del-CFTR, lo que da lugar a un aumento del procesamiento y del tráfico de la proteína madura hacia la superficie celular. Los estudios in vitro han demostrado que tanto el lumacaftor como el ivacaftor actúan directamente sobre la proteína CFTR en cultivos primarios de epitelio bronquial humano y en otras líneas celulares portadoras de la mutación F508del-CFTR, para aumentar la cantidad, la estabilidad y la función de la F508del-CFTR en la superficie celular, lo que da lugar a un aumento del transporte de iones cloruro.» Texto original en inglés: "Lumacaftor improves the conformational stability of F508del-CFTR, resulting in increased processing and trafficking of mature protein to the cell surface. In vitro studies have demonstrated that both lumacaftor and ivacaftor act directly on the CFTR protein in primary human bronchial epithelial cultures and other cell lines harboring the F508del-CFTR mutation to increase the quantity, stability, and function of F508del-CFTR at the cell surface, resulting in increased chloride ion transport." ([DailyMed: Orkambi (lumacaftor and ivacaftor) prescribing information, Vertex Pharmaceuticals Incorporated](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3fc1c40e-cfac-47a1-9e1a-61ead3570600), versión del 2026-03-24; consultado el 2026-11-19). Según la información conocida, lumacaftor es un corrector de la proteína CFTR: mejora su plegamiento y su transporte a la membrana celular. Su eficacia en la fibrosis quística está establecida, y se utiliza en combinación con otro modulador de CFTR (Orkambi).

Los datos compilados no respaldan un vínculo biológico plausible entre este mecanismo y la lepra, una infección causada por *Mycobacterium leprae* cuya patogenia implica la respuesta inmunitaria del huésped y la invasión de las células de Schwann. Cualquier conexión sería especulativa y requeriría validación mecanística independiente.

El puntaje TxGNN es muy alto (0.9944), pero procede del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Debe interpretarse con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1151059007 | ORKAMBI 150 MG/188 MG granulado en sobre | Granulado | No disponible en los datos compilados |
| 1151059006 | ORKAMBI 100 MG/125 MG granulado en sobre | Granulado | No disponible en los datos compilados |
| 1151059005 | ORKAMBI 100 MG/125 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 1151059001 | ORKAMBI 200 MG/125 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 1151059008 | ORKAMBI 75 MG/94 MG granulado en sobre | Granulado | No disponible en los datos compilados |

Las cinco autorizaciones están vigentes, corresponden a Vertex Pharmaceuticals (Ireland) Limited y ninguna está cancelada.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 226 interacciones registradas. Entre las incluidas en los datos compilados:
  - **Gravedad mayor**: eliglustat, naldemedina, naloxegol, rolapitant.
  - **Gravedad moderada**: inhibidores de la bomba de protones y antiácidos (omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol, rabeprazol, ranitidina), antidiabéticos (acetohexamida, glimepirida, linagliptina, pioglitazona, repaglinida), corticoides (betametasona, prednisona), bupropión y nitisinona.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para lepra se apoya solo en un puntaje computacional (nivel L5), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico plausible. No hay base suficiente para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y análisis de su posible relación con la patogenia de la lepra.
- Estudios preclínicos in vitro o in vivo que apoyen un efecto en la infección por *M. leprae*.
- Advertencias y contraindicaciones del prospecto de la AEMPS para completar el cribado de seguridad.
- Evaluación de compatibilidad de vías de administración y similitud con la indicación original.
- Revisión de las interacciones farmacológicas relevantes para la población con lepra (por ejemplo, con los tratamientos habituales).

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Orkambi (lumacaftor and ivacaftor) prescribing information, Vertex Pharmaceuticals Incorporated](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3fc1c40e-cfac-47a1-9e1a-61ead3570600) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


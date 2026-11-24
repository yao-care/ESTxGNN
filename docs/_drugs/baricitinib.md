---
layout: default
title: Baricitinib
parent: Solo predicción del modelo (L5)
nav_order: 87
evidence_level: L5
indication_count: 2
monitor_inn: "BARICITINIB"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
last_modified_at: 2026-11-24
description: "Baricitinib: nueva indicación predicha, Síndrome de microftalmía colobomatosa con displasia rizomélica (colobomatous microphthalmia-rhizomelic dysplasia syndro… (nivel de evidencia L5). Indicación or…"
---

# Baricitinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Baricitinib: inhibidor de JAK1/JAK2 → síndrome de microftalmía colobomatosa con displasia rizomélica (colobomatous microphthalmia-rhizomelic dysplasia syndrome)
{: .text-alpha }

## Resumen en Una Frase

Baricitinib es un inhibidor de JAK1/JAK2 comercializado en España. El modelo TxGNN predice que podría ser efectivo para el **síndrome de microftalmía colobomatosa con displasia rizomélica (colobomatous microphthalmia-rhizomelic dysplasia syndrome)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de microftalmía colobomatosa con displasia rizomélica (colobomatous microphthalmia-rhizomelic dysplasia syndrome) |
| Puntaje de Predicción TxGNN | 0,9994 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 2) |
| Número de Autorizaciones | 2 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Baricitinib (traducción no oficial): «El baricitinib es un inhibidor de las cinasas Janus (JAK). Las JAK son enzimas intracelulares que transmiten señales derivadas de las interacciones de citocinas o factores de crecimiento con sus receptores en la membrana celular para influir en los procesos celulares de la hematopoyesis y la función de las células inmunitarias.» Texto original en inglés: "Baricitinib is a Janus kinase (JAK) inhibitor. JAKs are intracellular enzymes which transmit signals arising from cytokine or growth factor-receptor interactions on the cellular membrane to influence cellular processes of hematopoiesis and immune cell function." ([DailyMed: Olumiant (baricitinib) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=866e9f35-9035-4581-a4b1-75a621ab55cf), versión del 2026-10-09; consultado el 2026-11-19). Según la información conocida, baricitinib es un inhibidor de JAK1/JAK2 que actúa sobre la señalización de citocinas en enfermedades autoinmunes e inflamatorias.

El síndrome predicho es un trastorno congénito raro del desarrollo que afecta al ojo y al esqueleto. A partir de los datos disponibles no se puede establecer un vínculo biológicamente plausible entre la inhibición de la vía JAK-STAT y este síndrome. La predicción parece estar impulsada por la topología de la red del modelo más que por una vía validada.

Cualquier hipótesis requeriría antes evidencia genética y de vías de señalización independiente. El puntaje elevado por sí solo no es suficiente para justificar un desarrollo posterior.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 1161170002 | OLUMIANT 2 MG COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Eli Lilly Nederland B.V. | Comercializada |
| 1161170010 | OLUMIANT 4 MG COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Eli Lilly Nederland B.V. | Comercializada |

Se muestran las 2 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (100 interacciones registradas; se listan las principales):
  - **Gravedad mayor**: hidrocortisona, triamcinolona (incluida la oftálmica), betametasona, budesonida, dexametasona, prednisolona, prednisona, deferiprona, ibritumomab tiuxetán, iobenguano (I-131), tositumomab (I-131).
  - **Gravedad moderada**: morfina (incluida la liposomal), ácido acetilsalicílico, nitisinona, opio.
  - **Gravedad menor**: acetato, gluconato y sulfato de zinc.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única base de la predicción es el puntaje del modelo (0,9994), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico plausible. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de baricitinib.
- Evidencia genética y de vías de señalización que conecte JAK-STAT con este síndrome.
- Revisión sistemática de la literatura sobre la enfermedad.
- Datos de advertencias y contraindicaciones del prospecto de la AEMPS para el cribado de seguridad.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Olumiant (baricitinib) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=866e9f35-9035-4581-a4b1-75a621ab55cf) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


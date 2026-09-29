---
layout: default
title: Tacrolimus
parent: Solo predicción del modelo (L5)
nav_order: 508
evidence_level: L5
indication_count: 3
---

# Tacrolimus
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

# Tacrolimus: De Inmunosupresión en Trasplante y Dermatitis Atópica a Dermatitis Seborreica

## Resumen en Una Frase

Tacrolimus es un inhibidor de la calcineurina que en España se comercializa en formas orales de liberación prolongada (Advagraf, Envarsus y genéricos) y en pomada (Protopic). Los datos de autorización recibidos no incluyen el texto de las indicaciones.
El modelo TxGNN predice que podría ser efectivo para la **dermatitis seborreica**, con **2 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de autorización de la AEMPS. Por los productos autorizados, corresponde a inmunosupresión en trasplante (formas orales) y dermatitis atópica (pomada Protopic). Es una inferencia, no un dato del registro |
| Nueva Indicación Predicha | Dermatitis seborreica |
| Puntaje de Predicción TxGNN | 99,26 % |
| Nivel de Evidencia | L2 (un ECA de Fase 3 completado; ver nota en la conclusión) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la farmacología conocida de la clase, tacrolimus inhibe la calcineurina. Con ello bloquea la activación de los linfocitos T y reduce la liberación de citocinas inflamatorias. Su eficacia en dermatitis atópica con pomada está bien establecida. Mecanísticamente podría aplicarse a otras dermatosis inflamatorias.

La dermatitis seborreica es una enfermedad inflamatoria crónica de la piel, con recaídas frecuentes, que afecta sobre todo a la cara y al cuero cabelludo. Se cree que interviene una respuesta inmunitaria inflamatoria frente a la levadura *Malassezia*. Un inhibidor tópico de la calcineurina puede actuar sobre ese componente inflamatorio sin la atrofia cutánea asociada al uso prolongado de corticoides tópicos. Esto lo hace atractivo como tratamiento de mantenimiento.

La relación entre ambas indicaciones es que las dos son dermatosis eccematosas mediadas por inflamación. Además, la pomada de tacrolimus ya está autorizada en España (Protopic 0,1 %), por lo que la vía de administración necesaria ya existe.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Fase 3 | Completado | 120 | Pomada de tacrolimus (Protopic) como tratamiento de mantenimiento de la dermatitis seborreica grave del rostro en adultos. Busca reducir recaídas y el uso de corticoides. No se proporcionaron resultados |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Fase 4 | Completado | 104 | Uso proactivo de tacrolimus 0,1 % una o dos veces por semana para mantener la remisión de la dermatitis seborreica facial del adulto. No se proporcionaron resultados |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33010323](https://pubmed.ncbi.nlm.nih.gov/33010323/) | 2021 | ECA | J Am Acad Dermatol | Tacrolimus 0,1 % frente a ciclopiroxolamina 1 % como tratamiento de mantenimiento en dermatitis seborreica facial grave. Estudio multicéntrico, doble ciego |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | ECA | Ann Dermatol | Tratamiento de mantenimiento de la dermatitis seborreica facial con tacrolimus 0,1 %, siguiendo el régimen intermitente ya usado en dermatitis atópica |
| [22101215](https://pubmed.ncbi.nlm.nih.gov/22101215/) | 2012 | ECA | J Am Acad Dermatol | Hidrocortisona 1 % frente a tacrolimus 0,1 % en dermatitis seborreica facial del adulto. Ensayo simple ciego |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | Ensayo clínico | Ann Parasitol | Sertaconazol 2 % frente a tacrolimus 0,03 % en 60 pacientes con dermatitis seborreica |
| [37067129](https://pubmed.ncbi.nlm.nih.gov/37067129/) | 2023 | Ensayo comparativo | Indian J Dermatol Venereol Leprol | Itraconazol oral durante dos días más tacrolimus tópico frente a tacrolimus tópico solo, en mantenimiento (Vietnam) |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Revisión sistemática | Am J Clin Dermatol | Revisión de los tratamientos tópicos de la dermatitis seborreica facial (antifúngicos, queratolíticos y corticoides) |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Revisión | Am J Clin Dermatol | Los inhibidores tópicos de la calcineurina son una alternativa segura a los corticoides, que tienen uso limitado por sus efectos adversos a largo plazo |
| [12833030](https://pubmed.ncbi.nlm.nih.gov/12833030/) | 2003 | Estudio piloto abierto | J Am Acad Dermatol | 18 pacientes tratados con tacrolimus 0,1 % durante 28 días. El 61 % (11 pacientes) logró el aclaramiento completo |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Revisión | J Drugs Dermatol | Estado actual y perspectivas terapéuticas de la dermatitis seborreica facial |
| [11770914](https://pubmed.ncbi.nlm.nih.gov/11770914/) | 2001 | Revisión | Semin Cutan Med Surg | Usos de tacrolimus y pimecrolimus tópicos en otras dermatosis, entre ellas la dermatitis seborreica |

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones. Los datos recibidos no incluyen el texto de la indicación aprobada de ningún producto.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 88081 | Tacrolimus Stada 5 mg cápsulas duras de liberación prolongada EFG | Cápsula dura de liberación prolongada |
| 02201004 | Protopic 0,1 % pomada | Pomada |
| 114935005 | Envarsus 1 mg comprimidos de liberación prolongada | Comprimido de liberación modificada |
| 07387014 | Advagraf 0,5 mg cápsulas duras de liberación prolongada | Cápsula dura de liberación prolongada |
| 84631 | Conferoport 3 mg cápsulas duras de liberación prolongada EFG | Cápsula dura de liberación prolongada |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un ensayo de Fase 3 completado y un ensayo de Fase 4 completado, ambos sobre la dermatitis seborreica. También hay al menos tres ECA publicados con tacrolimus tópico en esta enfermedad. La pomada ya está comercializada en España, pero la evidencia disponible no incluye resultados publicados de los ensayos registrados ni datos de seguridad de la AEMPS.

**Nota sobre el nivel de evidencia:** El paquete de evidencia asigna L1. Con la regla estricta (≥2 ECA de Fase 3 completados) solo se cumple L2, porque solo hay un ensayo de Fase 3 sobre esta indicación. L1 solo se sostendría si se contaran los ECA publicados cuya fase no consta.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de la AEMPS para obtener advertencias y contraindicaciones, que hoy están ausentes y bloquean el cribado de seguridad.
- Obtener el texto de las indicaciones aprobadas de cada autorización, incluido Protopic, para confirmar si la dermatitis seborreica sería un uso fuera de indicación.
- Conseguir los resultados de NCT02004860 y NCT01591070 (eficacia, tasa de recaídas y tolerabilidad).
- Confirmar los datos del mecanismo de acción en DrugBank.
- Definir un plan de seguimiento de seguridad para el uso tópico prolongado, es decir, mantenimiento intermitente en la cara.

*Los resultados de este informe son solo de referencia para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


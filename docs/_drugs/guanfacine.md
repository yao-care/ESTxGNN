---
layout: default
title: Guanfacine
parent: Solo predicción del modelo (L5)
nav_order: 262
evidence_level: L5
indication_count: 7
---

# Guanfacine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Guanfacina: De TDAH a Síndrome Faciodigitogenital

## Resumen en Una Frase

La guanfacina es un agonista de los receptores adrenérgicos alfa-2, utilizado para el trastorno por déficit de atención e hiperactividad (TDAH), y también para hipertensión y ansiedad según los datos farmacológicos.
El modelo TxGNN predice que podría ser efectiva para el **síndrome faciodigitogenital**, pero hoy hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción. Es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | TDAH (además de hipertensión y ansiedad según datos farmacológicos; el texto de indicación de las autorizaciones AEMPS viene vacío) |
| Nueva Indicación Predicha | Síndrome faciodigitogenital |
| Puntaje de Predicción TxGNN | 99,97 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 11 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información farmacológica disponible, la guanfacina actúa sobre los receptores adrenérgicos alfa-2A, alfa-2B y alfa-2C. Su eficacia en TDAH está establecida, y es un fármaco comercializado en España.

Con los datos suministrados no se puede establecer un vínculo mecanístico entre la agonía alfa-2 y el síndrome faciodigitogenital. El puntaje alto de TxGNN (99,97 %) es solo una predicción. No hay ensayos, literatura ni datos de similitud con la indicación original que la respalden.

Por eso esta candidata no debe avanzar por ahora. Otras indicaciones predichas para este fármaco sí tienen evidencia (ver tabla siguiente).

## Otras Indicaciones Predichas con Evidencia

| Indicación Predicha | Puntaje TxGNN | Nivel | Evidencia Disponible | Decisión |
|------|------|------|------|------|
| Síndrome de Tourette | 99,27 % | L1 | 1 ensayo Fase 3 completado (NCT00004376, n=35), 1 estudio Fase 4 completado (NCT01547000, n=34), guías europeas y revisiones sistemáticas | Proceed with Guardrails |
| Trastorno específico del desarrollo | 99,97 % | L2 | Ensayo Fase 4 completado (NCT04085172, n=396) y otro en reclutamiento (NCT05916339, n=500); la evidencia parece ser sobre TDAH, que podría ser un uso ya autorizado | Proceed with Guardrails |
| Trastorno bipolar maníaco | 99,72 % | L4 | Sin ensayos; literatura general, con señal de seguridad de manía secundaria | Hold |
| Síndrome de piernas inquietas | 99,64 % | L4 | Solo una revisión indirecta sobre sueño en TDAH | Hold |
| Tricotilomanía | 99,79 % | L5 | Sin evidencia específica de guanfacina | Hold |
| Fibroma condromixoide | 99,94 % | L5 | Sin evidencia | Hold |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para el síndrome faciodigitogenital.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para el síndrome faciodigitogenital.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1151040002 | Intuniv 1 mg comprimidos de liberación prolongada (Takeda) | Comprimido de liberación prolongada |
| 1241908006 | Paxneury 6 mg comprimidos de liberación prolongada (Neuraxpharm) | Comprimido de liberación prolongada |
| 1241908003 | Paxneury 3 mg comprimidos de liberación prolongada EFG (Neuraxpharm) | Comprimido de liberación prolongada |
| 1241908001 | Paxneury 1 mg comprimidos de liberación prolongada EFG (Neuraxpharm) | Comprimido de liberación prolongada |
| 1241908004 | Paxneury 4 mg comprimidos de liberación prolongada EFG (Neuraxpharm) | Comprimido de liberación prolongada |

Se muestran 5 de las 11 autorizaciones. El texto de indicación aprobada viene vacío en estos registros.

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

Señales descritas en la literatura asociada a otras indicaciones predichas, que conviene tener presentes:
- **Síncope**: se ha descrito en niños con síndrome de Tourette tratados con guanfacina, probablemente por hipotensión o bradicardia (PMID 16229000).
- **Manía secundaria**: hay reportes pediátricos de reacciones maníacas asociadas a guanfacina (PMID 10467976, 9730081, 27228067).
- **Sobredosis**: se ha reportado una pausa sinusal en una sobredosis combinada con olanzapina (PMID 31447925).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para el síndrome faciodigitogenital no hay ensayos, literatura ni vínculo mecanístico plausible; el alto puntaje de TxGNN es solo una predicción (L5). Dentro de este mismo paquete, el síndrome de Tourette es la candidata más sólida (L1, Proceed with Guardrails).

**Para avanzar se necesita:**
- Para el síndrome faciodigitogenital: una base mecanística y evidencia preclínica o clínica antes de reconsiderar la candidata.
- Para Tourette: verificar los resultados de NCT00004376 y NCT01547000 (no se suministraron), y considerar que ambos estudios son pequeños (n=34-35).
- Para "trastorno específico del desarrollo": confirmar el mapeo de la enfermedad y si se trata de un uso ya autorizado (TDAH).
- Obtener el mecanismo de acción desde DrugBank.
- Descargar y analizar el prospecto de la AEMPS para completar advertencias y contraindicaciones.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Alfentanil
parent: Solo predicción del modelo (L5)
nav_order: 33
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Alfentanil: nueva indicación predicha, Síndrome nefrogénico de antidiuresis inapropiada (nivel de evidencia L5). Indicación original: No especificada en la autorización (uso conocido: anestesia y ana…"
---

# Alfentanil
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

# Alfentanilo: De Indicación No Especificada a Síndrome Nefrogénico de Antidiuresis Inapropiada

## Resumen en Una Frase

Alfentanilo es un opioide agonista del receptor mu de acción corta, utilizado en anestesia y analgesia; la ficha de autorización española disponible no detalla el texto de la indicación.
El modelo TxGNN predice que podría ser efectivo para el **síndrome nefrogénico de antidiuresis inapropiada (NSIAD)**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en la autorización (uso conocido: anestesia y analgesia) |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada |
| Puntaje de Predicción TxGNN | 99,51% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados en los datos compilados para este informe. Según la información conocida, alfentanilo es un agonista del receptor opioide mu de acción corta, empleado en anestesia y analgesia.

El NSIAD está causado por mutaciones de ganancia de función en el receptor V2 de la vasopresina (AVPR2, por ejemplo R137C/R137L). Estas mutaciones generan actividad constitutiva del receptor y retención de agua a pesar de niveles indetectables de vasopresina.

**No se identifica un vínculo mecanístico creíble.** Los opioides se asocian en general con mayor liberación de vasopresina y efectos tipo SIADH, lo que empeoraría la antidiuresis en lugar de mejorarla. Además, no actuarían sobre un receptor V2 constitutivamente activo, que funciona independientemente de la vasopresina. El puntaje alto de TxGNN (0,995) es solo una predicción del modelo y probablemente refleja asociaciones a nivel de red, no un mecanismo biológicamente plausible.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 57471 | LIMIFEN 0,5 mg/ml SOLUCIÓN INYECTABLE (Piramal Critical Care B.V.) | Solución inyectable | No especificada en los datos disponibles |

## Consideraciones de Seguridad

- **Contraindicaciones según grafo de conocimiento (no del prospecto)**: enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, trastornos hipotensivos, pseudotumor cerebral e hipertensión intracraneal.
- **Interacciones Farmacológicas**: se registraron 167 interacciones. Entre las de nivel **mayor** figuran: aprepitant, bupropión, claritromicina, clotrimazol, dexfenfluramina, dolasetrón, fenfluramina, granisetrón y lorcaserina. Entre las de nivel **moderado**: atropina, cimetidina, clidinio, dexametasona, diciclomina, dronabinol, eluxadolina, fenilbutirato de glicerol, glicopirronio, hiosciamina y mazindol.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin estudios reales, y no existe un vínculo mecanístico creíble: los opioides tienden a favorecer la liberación de vasopresina y no actúan sobre un receptor V2 constitutivamente activo. Además, el perfil de seguridad oficial no está disponible.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco
- Advertencias y contraindicaciones del prospecto de AEMPS
- Evidencia preclínica o clínica que justifique un vínculo mecanístico con el receptor V2/AVPR2
- Evaluación de la compatibilidad de la vía de administración con la nueva indicación
- Revisión de las contraindicaciones del grafo de conocimiento (especialmente renales) dado el contexto nefrológico de la indicación predicha
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


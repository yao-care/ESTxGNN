---
layout: default
title: Empagliflozin
parent: Solo predicción del modelo (L5)
nav_order: 199
evidence_level: L5
indication_count: 3
---

# Empagliflozin
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

# Empagliflozina: De Diabetes Mellitus Tipo 2 a Síndrome de la Extremidad Rígida Focal

## Resumen en Una Frase

Empagliflozina es un fármaco comercializado en España, utilizado originalmente para el tratamiento de la diabetes mellitus tipo 2 (según los datos farmacológicos incluidos).
El modelo TxGNN predice que podría ser efectivo para el **síndrome de la extremidad rígida focal**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diabetes mellitus tipo 2 (según datos farmacológicos; los textos de indicación de las autorizaciones de la AEMPS están vacíos) |
| Nueva Indicación Predicha | Síndrome de la extremidad rígida focal |
| Puntaje de Predicción TxGNN | 99.06% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según los datos farmacológicos incluidos, empagliflozina actúa sobre los cotransportadores de sodio-glucosa **SGLT2** (gen SLC5A2) y **SGLT1** (gen SLC5A1). Su eficacia en la diabetes tipo 2 está comprobada, y también se ha descrito una reducción del riesgo de muerte cardiovascular en pacientes con diabetes tipo 2 y enfermedad cardiovascular.

**Con los datos disponibles, no se identifica un vínculo mecanístico plausible** entre la inhibición de SGLT2 y el síndrome de la extremidad rígida focal. Esta enfermedad rara pertenece al espectro del síndrome de la persona rígida, que suele asociarse a alteraciones de la vía GABAérgica o a mecanismos autoinmunes. No hay una relación evidente con el metabolismo de la glucosa ni con el transporte renal de sodio-glucosa.

Además, el puntaje de 0.9906 es idéntico al del síndrome de la persona rígida clásico (segunda predicción). Esto sugiere un artefacto de proximidad en el grafo del modelo y no evidencia independiente. La tercera predicción, la opsismodisplasia (puntaje 0.9903), tampoco tiene ensayos, literatura ni vínculo mecanístico identificado. Ninguno de estos puntajes debe interpretarse como señal clínica sin validación independiente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 8 autorizaciones. Los textos de indicación aprobada no están disponibles en los datos recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 89672 | GLUSOD 10 MG comprimidos recubiertos con película EFG | Comprimido recubierto con película | Medochemie Limited |
| 89671 | GLUSOD 25 MG comprimidos recubiertos con película EFG | Comprimido recubierto con película | Medochemie Limited |
| 91043 | EMPAGLIFLOZINA KERN PHARMA 25 MG comprimidos recubiertos con película EFG | Comprimido recubierto con película | Kern Pharma S.L. |
| 91044 | EMPAGLIFLOZINA KERN PHARMA 10 MG comprimidos recubiertos con película EFG | Comprimido recubierto con película | Kern Pharma S.L. |
| 114930014 | JARDIANCE 10 MG comprimidos recubiertos con película | Comprimido recubierto con película | Boehringer Ingelheim International GmbH |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5): no hay ensayos, no hay literatura y no se identifica un vínculo mecanístico plausible entre la inhibición de SGLT2 y el síndrome de la extremidad rígida focal. El puntaje idéntico al de otra enfermedad vecina apunta a un artefacto del grafo.

**Para avanzar se necesita:**
- Prospecto de la AEMPS con advertencias y contraindicaciones (bloqueante para el cribado de seguridad).
- Datos del mecanismo de acción desde DrugBank.
- Búsqueda de literatura y de estudios preclínicos que relacionen SGLT1/SGLT2 con el síndrome de la persona rígida y sus variantes.
- Revisión de la estructura del grafo de TxGNN para descartar un artefacto de proximidad entre la extremidad rígida focal y el síndrome de la persona rígida clásico.
- Evaluación de la compatibilidad de la vía de administración (pendiente).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


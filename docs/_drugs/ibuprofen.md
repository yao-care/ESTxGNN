---
layout: default
title: Ibuprofen
parent: Solo predicción del modelo (L5)
nav_order: 269
evidence_level: L5
indication_count: 7
---

# Ibuprofen
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

# Ibuprofeno: De Dolor y Fiebre a Displasia Acromesomélica tipo Hunter-Thompson

## Resumen en Una Frase

Ibuprofeno es un antiinflamatorio no esteroideo (AINE) de uso muy extendido, utilizado originalmente como analgésico y antipirético.
El modelo TxGNN predice que podría ser efectivo para la **displasia acromesomélica tipo Hunter-Thompson**, una enfermedad esquelética rara.
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, por lo que se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dolor y fiebre (uso clínico general; las autorizaciones de la AEMPS del registro no incluyen texto de indicación) |
| Nueva Indicación Predicha | Displasia acromesomélica, tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información farmacológica conocida, ibuprofeno es un inhibidor no selectivo de las ciclooxigenasas (COX-1 y COX-2). Su eficacia en dolor, inflamación y fiebre está bien establecida.

La displasia acromesomélica tipo Hunter-Thompson es un trastorno esquelético relacionado con GDF5. Hasta donde alcanzan los datos proporcionados, no existe una vía establecida que conecte la inhibición de COX con la modificación de esta enfermedad. Un posible beneficio, en el mejor de los casos, sería sintomático (dolor o inflamación), y no se aportó evidencia de ello.

Por tanto, esta predicción **no tiene un vínculo mecanístico respaldado**. El puntaje alto (0.997) proviene únicamente del grafo de conocimiento del modelo y no debe interpretarse como evidencia de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Ibuprofeno tiene 20 autorizaciones en España. Se muestran las 5 principales. El registro no incluye el texto de la indicación aprobada de estas autorizaciones. También existen otras formas, como cápsula blanda, granulado efervescente, solución para perfusión y polvo para suspensión oral.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 90114 | Ibuprofeno Combix 400 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Laboratorios Combix S.L.U. |
| 68200 | Ibufarmalid 400 mg suspensión oral | Suspensión oral | Farmalider S.A. |
| 80719 | Espidifen 600 mg granulado para solución oral sabor cola-limón | Granulado para solución oral | Zambon S.A.U. |
| 64030 | Ibuprofeno Mabo 50 mg/g gel | Gel (tópico) | Mabo Farma S.A. |
| 69343 | Ibuprofeno (arginina) Stada 600 mg granulado para solución oral EFG | Granulado para solución oral | Laboratorio Stada S.L. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

La consulta de interacciones devolvió solo dianas farmacológicas de ibuprofeno (COX-1, COX-2, ASIC1, SMCT1, PAT1 y PPARγ), no interacciones con otros fármacos.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico plausible. Las otras seis indicaciones predichas están en la misma situación: braquiolmia con amelogénesis imperfecta, miosclerosis, braquiolmia, síndrome de braquidactilia-sindactilia, pseudoacondroplasia y síndrome de microftalmia colobomatosa con displasia rizomélica. Todas son L5 y Hold.

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank y un análisis del posible vínculo entre COX y la vía GDF5.
- Estudios preclínicos en modelos de la enfermedad que respalden un efecto sobre el hueso o el cartílago.
- Búsqueda sistemática de literatura y ensayos, incluidos reportes de caso.
- Advertencias y contraindicaciones del prospecto de la AEMPS, hoy no disponibles, antes de cualquier revisión de seguridad.
- Evaluación de la compatibilidad de vías de administración (pendiente).
- Valorar, con mayor plausibilidad, si el beneficio sintomático en pseudoacondroplasia (dolor articular) merece una evaluación separada.

Los resultados de este informe son solo para referencia de investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


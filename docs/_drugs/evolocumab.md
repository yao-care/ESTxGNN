---
layout: default
title: Evolocumab
parent: Solo predicción del modelo (L5)
nav_order: 223
evidence_level: L5
indication_count: 6
---

# Evolocumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Evolocumab: De Hipercolesterolemia a Forma Sintomática de Hemofilia en Portadoras

## Resumen en Una Frase

Evolocumab es un anticuerpo monoclonal comercializado en España como Repatha, que se usa para reducir el colesterol LDL.
El modelo TxGNN predice que podría ser efectivo para **la forma sintomática de hemofilia en mujeres portadoras**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrada en el texto de las autorizaciones. Por su uso conocido, reducción del colesterol LDL (conocimiento general, no del Evidence Pack) |
| Nueva Indicación Predicha | Forma sintomática de hemofilia en mujeres portadoras |
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la farmacología general, evolocumab es un anticuerpo monoclonal que neutraliza PCSK9. Esto aumenta el reciclaje del receptor de LDL y reduce el colesterol LDL.

Con este mecanismo, **no se identifica un vínculo plausible** con la hemofilia. La enfermedad se debe a una deficiencia de factor VIII o IX, y evolocumab no tiene un papel conocido en la producción de estos factores ni en la coagulación. El alto puntaje (0.998) refleja únicamente una asociación dentro del grafo de conocimiento, sin datos clínicos ni bibliográficos que la sostengan.

Por tanto, esta predicción debe tratarse como una hipótesis sin respaldo mecanístico. Se recomienda no priorizarla sin evidencia nueva.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1151016003 | REPATHA 140 MG solución inyectable en pluma precargada | Solución inyectable en pluma precargada | No especificada en los datos |
| 1151016003IP | REPATHA 140 MG solución inyectable en pluma precargada | Solución inyectable en pluma precargada | No especificada en los datos |
| 1151016002 | REPATHA 140 MG solución inyectable en pluma precargada | Solución inyectable en pluma precargada | No especificada en los datos |

El titular de las tres autorizaciones es Amgen Europe B.V.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es de nivel L5: no hay ensayos, no hay literatura y no existe un mecanismo plausible que vincule la inhibición de PCSK9 con la hemofilia. Con esta información no se justifica avanzar.

Las otras cinco predicciones del modelo también quedan en Hold con nivel L5:
- **Deficiencia familiar de apolipoproteína C-II:** es la más cercana biológicamente, por ser una enfermedad del metabolismo lipídico. Aun así, la inhibición de PCSK9 no corrige el defecto de activación de la lipoproteína lipasa.
- **Púrpura trombocitopénica, deficiencia de factor XI y hemofilia A con anomalía vascular:** no tienen mecanismo plausible.
- **Enfermedad de actividad catalítica:** es un término genérico de ontología, no una entidad clínica, y debería excluirse o sustituirse por enfermedades específicas.

**Para avanzar se necesita:**
- Buscar ensayos clínicos y literatura específicos para la indicación predicha.
- Contar con datos del mecanismo de acción y del prospecto de la AEMPS (advertencias y contraindicaciones), que hoy no están disponibles.
- Obtener el texto de las indicaciones aprobadas en las autorizaciones españolas.
- Aportar una hipótesis mecanística que justifique el vínculo entre PCSK9 y la coagulación antes de reconsiderar la decisión.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


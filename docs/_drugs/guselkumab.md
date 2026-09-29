---
layout: default
title: Guselkumab
parent: Solo predicción del modelo (L5)
nav_order: 263
evidence_level: L5
indication_count: 10
---

# Guselkumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Guselkumab: Hacia Osteoporosis Inducida por Fármacos

## Resumen en Una Frase

Guselkumab es un anticuerpo monoclonal que bloquea la subunidad p19 de la IL-23 y se comercializa en España como Tremfya. Los datos de licencia recibidos no incluyen el texto de sus indicaciones aprobadas.
El modelo TxGNN predice que podría ser efectivo para **osteoporosis inducida por fármacos**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Osteoporosis inducida por fármacos |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L5 (solo predicción del modelo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro del fármaco. Según la literatura asociada, guselkumab es un inhibidor selectivo de la subunidad p19 de la IL-23. Esta citocina impulsa la diferenciación de linfocitos Th17 y la señalización de IL-17/IL-22, y su bloqueo está validado en enfermedades inflamatorias inmunomediadas como la psoriasis.

El vínculo con la osteoporosis inducida por fármacos es **especulativo**. La señalización IL-23/IL-17 puede favorecer la osteoclastogénesis, por lo que bloquear la IL-23 podría influir en la pérdida ósea. Sin embargo, esta relación no está establecida para la osteoporosis causada por medicamentos (por ejemplo, glucocorticoides). No hay estudios preclínicos ni clínicos aportados que la respalden.

El puntaje alto de TxGNN (99.84%, posición 3491 del ranking global del modelo) indica una asociación en el grafo de conocimiento, pero no constituye evidencia de eficacia. No se ha evaluado la similitud con la indicación original ni la compatibilidad de vías de administración.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 1171234001 | TREMFYA 100 MG solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | Janssen-Cilag International N.V |
| 1171234008 | TREMFYA 200 MG solución inyectable en pluma precargada | Solución inyectable | Janssen-Cilag International N.V |
| 1171234002 | TREMFYA 100 MG OnePress solución inyectable en pluma precargada | Solución inyectable en pluma precargada | Janssen-Cilag International N.V |
| 1171234012 | TREMFYA 45 MG/0,45 ML solución inyectable en pluma precargada | Solución inyectable | Janssen-Cilag International N.V |
| 1171234005 | TREMFYA 200 MG concentrado para solución para perfusión | Concentrado para solución para perfusión | Janssen-Cilag International N.V |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para osteoporosis inducida por fármacos no tiene ensayos, literatura ni estudios preclínicos que la respalden (L5). El vínculo mecanístico es especulativo, y el cribado de seguridad no puede avanzar sin el prospecto de la AEMPS.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas).
- Obtener el mecanismo de acción desde DrugBank.
- Realizar estudios preclínicos que evalúen el efecto del bloqueo de IL-23 sobre el hueso, y una revisión sistemática de la literatura sobre IL-23 y metabolismo óseo.

**Nota sobre otras predicciones del mismo análisis:** dos predicciones de menor rango sí tienen evidencia sólida. La **psoriasis** (puntaje 99.75%) tiene ensayos de Fase 3 completados (por ejemplo, NCT02325219 y los estudios VOYAGE 1 y 2), y la **colitis ulcerosa** (99.70%) tiene el programa QUASAR de Fase 3. Ambas alcanzan nivel L1 y una recomendación de *Proceed with Guardrails*. Probablemente son indicaciones ya aprobadas o en fase avanzada, no reposicionamientos nuevos. Conviene confirmarlo con la ficha técnica antes de tratarlas como candidatas. Las demás predicciones (retinopatía diabética, osteodistrofia renal, entre otras) están en nivel L5 y sin evidencia.

*Este informe es solo para fines de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


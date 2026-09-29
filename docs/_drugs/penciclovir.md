---
layout: default
title: Penciclovir
parent: Solo predicción del modelo (L5)
nav_order: 415
evidence_level: L5
indication_count: 1
---

# Penciclovir
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

# Penciclovir: De Antiviral (indicación original no registrada) a Fascioliasis

## Resumen en Una Frase

Penciclovir es un antiviral análogo de nucleósidos de guanosina, comercializado en España en forma de crema. El registro no incluye su indicación original.
El modelo TxGNN predice que podría ser efectivo para **fascioliasis**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, así que la predicción se apoya solo en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el registro (el texto de indicación de la autorización está vacío) |
| Nueva Indicación Predicha | Fascioliasis |
| Puntaje de Predicción TxGNN | 99.06% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, penciclovir es un análogo nucleósido de guanosina. Es fosforilado por la timidina quinasa viral (VHS/VVZ) y después inhibe la ADN polimerasa viral.

Con esta información, **no se identifica un vínculo mecanístico respaldado por evidencia**. Las especies de *Fasciola* son trematodos parásitos y no se conoce en ellas una vía de activación por timidina quinasa de tipo viral. Por eso el mecanismo antiviral no parece transferible de forma plausible. Cualquier vía inferida por el grafo de conocimiento (por ejemplo, metabolismo de nucleósidos compartido) no puede verificarse con los datos disponibles.

El puntaje de 0.99 es una salida del modelo, no evidencia clínica ni experimental. Además, el tratamiento establecido para la fascioliasis es el triclabendazol, y aquí no se muestra ninguna ventaja frente a él. La única presentación autorizada es una crema de uso tópico, y no hay datos que indiquen que esta vía sea compatible con una infección hepatobiliar.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61462 | FENIVIR 10 mg/g CREMA (Perrigo España S.A.) | Crema | No especificada en el registro |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el puntaje del modelo (nivel L5), sin ensayos, literatura ni mecanismo plausible. Además, no se demuestra ninguna ventaja frente al triclabendazol.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS para completar advertencias y contraindicaciones (bloquea el cribado de seguridad)
- Datos detallados del mecanismo de acción (por ejemplo, consulta a la API de DrugBank)
- Evidencia preclínica (in vitro o in vivo) de actividad frente a *Fasciola*
- Análisis de compatibilidad de vía de administración (crema tópica frente a la necesidad de exposición sistémica)
- Justificación de la ventaja frente al triclabendazol

*Los resultados son solo de referencia para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Tasonermin
parent: Solo predicción del modelo (L5)
nav_order: 765
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tasonermin: nueva indicación predicha, Carcinoma urotelial de la uretra prostática (nivel de evidencia L5). Indicación original: Sarcoma de tejidos blandos (según las indicaciones del grafo de conoc…"
---

# Tasonermin
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

# Tasonermin: De Sarcoma de Tejidos Blandos a Carcinoma Urotelial de la Uretra Prostática

## Resumen en Una Frase

Tasonermin es el factor de necrosis tumoral alfa (TNF-alfa) humano recombinante, utilizado originalmente en perfusión aislada de extremidades para el tratamiento del sarcoma de tejidos blandos.
El modelo TxGNN predice que podría ser efectivo para **carcinoma urotelial de la uretra prostática**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Sarcoma de tejidos blandos (según las indicaciones del grafo de conocimiento; el texto de indicación autorizado no está disponible en los datos compilados) |
| Nueva Indicación Predicha | Carcinoma urotelial de la uretra prostática |
| Puntaje de Predicción TxGNN | 99,81% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Tasonermin es TNF-alfa humano recombinante. Se utiliza junto con melfalán en perfusión aislada de extremidades para el sarcoma de tejidos blandos. Su actividad propuesta consiste en la destrucción selectiva de la vasculatura tumoral y en un aumento de la penetración del quimioterápico en el tumor. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados; esta descripción procede del razonamiento general sobre el fármaco.

La relación entre la indicación original y la nueva es débil. Ambas son neoplasias, pero el sarcoma es de origen mesenquimal y el carcinoma urotelial es epitelial. El puntaje alto del modelo (0,998) parece reflejar una asociación genérica con la categoría "cáncer" en el grafo de conocimiento, no un vínculo mecanístico específico.

Además, existen obstáculos importantes de aplicabilidad. La uretra prostática no permite una perfusión aislada como la de una extremidad, y el TNF-alfa sistémico tiene toxicidad limitante de dosis (hipotensión, síndrome similar al shock séptico). No se identifica una vía de administración plausible.

Otras predicciones del modelo (todas con evidencia L5 y recomendación Hold) incluyen carcinoma sarcomatoide de células transicionales de la pelvis renal (99,80%), carcinoma urotelial de vejiga infiltrante variante sarcomatoide (99,79%), carcinoma urotelial papilar de la pelvis renal (99,79%) y carcinoma de mama HER2 positivo (99,70%), entre otras. Ninguna cuenta con ensayos ni literatura.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 99097001 | BEROMUN 1 mg polvo para solución para perfusión (Belpharma S.A.) | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia / modificador de la respuesta biológica (citocina TNF-alfa recombinante), usada junto con quimioterapia citotóxica (melfalán) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Constantes hemodinámicas (presión arterial), hemograma, función hepática y renal; vigilancia de fuga sistémica durante la perfusión |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto; seguir las regulaciones de manejo de fármacos antineoplásicos del centro |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

No se han encontrado interacciones farmacológicas registradas en las consultas realizadas. Como referencia general no verificada con el prospecto, el TNF-alfa sistémico se asocia a hipotensión y a un síndrome similar al shock séptico.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura, y existen barreras anatómicas y de toxicidad sistémica que impiden una vía de administración viable en la uretra prostática.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un vacío de datos bloqueante para el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Definir una vía de administración viable (por ejemplo, intravesical o regional) con respaldo preclínico
- Realizar una búsqueda sistemática de literatura y ensayos sobre TNF-alfa en carcinoma urotelial
- Evaluar si alguna de las otras predicciones (p. ej., variantes sarcomatoides) tiene un vínculo biológico más sólido
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


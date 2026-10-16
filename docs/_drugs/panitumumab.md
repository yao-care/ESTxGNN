---
layout: default
title: Panitumumab
parent: Solo predicción del modelo (L5)
nav_order: 608
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Panitumumab: nueva indicación predicha, Osteoporosis inducida por fármacos (nivel de evidencia L5). Indicación original: Neoplasia maligna metastásica de colon (según la base de conocimiento…"
---

# Panitumumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Panitumumab: De Neoplasia Maligna Metastásica de Colon a Osteoporosis Inducida por Fármacos

## Resumen en Una Frase

Panitumumab es un anticuerpo monoclonal dirigido contra el receptor del factor de crecimiento epidérmico (EGFR), utilizado originalmente para el tratamiento de la neoplasia maligna metastásica de colon.
El modelo TxGNN predice que podría ser efectivo para **osteoporosis inducida por fármacos**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; la predicción se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Neoplasia maligna metastásica de colon (según la base de conocimiento TxGNN; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Osteoporosis inducida por fármacos |
| Puntaje de Predicción TxGNN | 99.13% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, panitumumab es un anticuerpo monoclonal anti-EGFR, su uso en cáncer colorrectal metastásico está establecido y, mecanísticamente, el bloqueo de EGFR podría influir en el metabolismo óseo.

La señalización de EGFR participa de forma plausible en la diferenciación de los osteoblastos y en la remodelación ósea, por lo que su bloqueo podría afectar teóricamente al hueso. Sin embargo, este vínculo es especulativo y podría apuntar hacia un perjuicio en lugar de un beneficio: la hipomagnesemia y la hipocalcemia son efectos adversos conocidos de panitumumab y podrían afectar negativamente al hueso.

No existe evidencia clínica directa ni indirecta que respalde este reposicionamiento. Además, un puntaje alto puede reflejar una asociación basada en el grafo de conocimiento y no un verdadero efecto terapéutico.

**Otra predicción de TxGNN (rango 2):** retinopatía diabética no proliferativa grave (puntaje 99.05%, nivel L5, Hold). El vínculo mecanístico es débil: la diana validada en esta enfermedad es VEGF, el perfil de toxicidad sistémica del anti-EGFR es conocido y no hay datos que respalden su uso intravítreo. Tampoco hay ensayos ni literatura.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 07423001 | VECTIBIX 20 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |
| 07423003 | VECTIBIX 20 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |
| 07423002 | VECTIBIX 20 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |

Titular: Amgen Europe B.V. Las tres autorizaciones son vigentes y de principio activo único.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-EGFR) |
| Riesgo de Mielosupresión | Bajo como agente único (no es un citotóxico convencional); puede aumentar al combinarse con quimioterapia |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Electrolitos (magnesio, calcio, potasio), piel y mucosas, reacciones a la perfusión; hemograma y función hepática y renal cuando se use con quimioterapia |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (27 interacciones registradas; se muestran las principales):
  - **Mayores:** amiodarona, trióxido de arsénico, bevacizumab, dofetilida, dronedarona, droperidol, ácido aminolevulínico, irinotecán (incluido el liposomal), levacetilmetadol.
  - **Moderadas:** inhibidores de la bomba de protones (rabeprazol, omeprazol, dexlansoprazol, esomeprazol, lansoprazol, pantoprazol), metoxaleno, ácido aminolevulínico tópico, disopiramida, idelalisib.
- Efectos adversos conocidos relevantes para esta predicción: hipomagnesemia e hipocalcemia.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos ni literatura. El vínculo mecanístico es especulativo y podría implicar daño óseo por alteraciones electrolíticas.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA)
- Obtención y análisis del prospecto de la AEMPS (advertencias y contraindicaciones), requisito previo para cualquier evaluación de seguridad
- Estudios preclínicos que evalúen el efecto del bloqueo de EGFR sobre el metabolismo óseo
- Revisión de literatura sobre la relación entre anti-EGFR, hipomagnesemia/hipocalcemia y salud ósea
- Evaluación de la compatibilidad de vías de administración y de la similitud con la indicación original
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


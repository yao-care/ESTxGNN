---
layout: default
title: Panitumumab
parent: Solo predicción del modelo (L5)
nav_order: 405
evidence_level: L5
indication_count: 2
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

# Panitumumab: De Cáncer Colorrectal Metastásico a Osteoporosis Inducida por Fármacos

## Resumen en Una Frase

Panitumumab es un anticuerpo monoclonal humano anti-EGFR, utilizado originalmente en cáncer colorrectal metastásico (dato de conocimiento general; el registro de la AEMPS del pack no incluye el texto de indicación).
El modelo TxGNN predice que podría ser efectivo para **osteoporosis inducida por fármacos**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer colorrectal metastásico (conocimiento general; no consta en los datos de la AEMPS) |
| Nueva Indicación Predicha | Osteoporosis inducida por fármacos |
| Puntaje de Predicción TxGNN | 99.13% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el pack. Según el conocimiento general, panitumumab es un anticuerpo monoclonal totalmente humano que bloquea el receptor del factor de crecimiento epidérmico (EGFR). Su eficacia en la indicación oncológica original está establecida. La señalización de EGFR participa en la diferenciación de los osteoblastos y en la regulación de los osteoclastos a través de RANKL, y de ahí surge la conexión con el hueso.

Sin embargo, el sentido del efecto es incierto. Bloquear EGFR podría perjudicar la formación ósea en lugar de protegerla. Además, panitumumab causa con frecuencia hipomagnesemia, un factor potencialmente negativo para la salud ósea. El puntaje alto de TxGNN (0.991) proviene solo del grafo de conocimiento, sin respaldo clínico ni bibliográfico en los datos. El mecanismo es especulativo y podría apuntar a daño más que a beneficio.

TxGNN también predice **retinopatía diabética no proliferativa grave** (puntaje 99.05%, evidencia L5, decisión Hold). Existe un vínculo preclínico indirecto entre EGFR y la angiogénesis retiniana. Sin embargo, el tratamiento establecido se dirige a VEGF, no hay evidencia de que bloquear EGFR ayude, y un anticuerpo grande de administración sistémica con toxicidad dermatológica y electrolítica encaja mal con una indicación ocular crónica no oncológica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 07423001 | VECTIBIX 20 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No especificada en los datos |
| 07423003 | VECTIBIX 20 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No especificada en los datos |
| 07423002 | VECTIBIX 20 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No especificada en los datos |

Titular de las tres autorizaciones: Amgen Europe B.V.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-EGFR) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; en general se vigilan electrolitos (especialmente magnesio) y la piel |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en los datos disponibles.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5), sin ningún ensayo ni publicación que la respalde. El mecanismo es especulativo y podría indicar un efecto perjudicial sobre el hueso, además de la hipomagnesemia asociada al fármaco.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS con advertencias y contraindicaciones, un dato bloqueante para el cribado de seguridad
- Completar los datos de mecanismo de acción desde DrugBank
- Revisión sistemática de la literatura preclínica sobre EGFR y metabolismo óseo, con atención al sentido del efecto
- Evaluar el impacto de la hipomagnesemia sobre la salud ósea
- Repetir la evaluación solo si aparece evidencia preclínica o clínica independiente del modelo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


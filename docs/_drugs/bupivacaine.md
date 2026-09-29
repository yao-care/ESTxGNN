---
layout: default
title: Bupivacaine
parent: Solo predicción del modelo (L5)
nav_order: 88
evidence_level: L5
indication_count: 4
---

# Bupivacaine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Bupivacaína: De Anestesia Local a Acrodermatitis Crónica Atrófica

## Resumen en Una Frase

Bupivacaína es un anestésico local de tipo amida, utilizado originalmente para bloqueos nerviosos y el control del dolor postoperatorio.
El modelo TxGNN predice que podría ser efectivo para **acrodermatitis crónica atrófica**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Anestesia local (bloqueo del plexo braquial o del nervio femoral, dolor postoperatorio). Procede de los datos farmacológicos, porque los textos de indicación autorizados están vacíos |
| Nueva Indicación Predicha | Acrodermatitis crónica atrófica |
| Puntaje de Predicción TxGNN | 99.23% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 10 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, bupivacaína es un anestésico local de tipo amida que bloquea los canales de sodio dependientes de voltaje. Su eficacia como anestésico local está comprobada. Sin embargo, mecanísticamente **no se identifica un vínculo creíble** con la nueva indicación.

La acrodermatitis crónica atrófica es una manifestación cutánea tardía de la infección por *Borrelia* (borreliosis de Lyme) y se trata con antibióticos. Un bloqueador de canales de sodio no tiene efecto antimicrobiano ni antiinflamatorio conocido sobre esta enfermedad. A lo sumo podría dar alivio sintomático del dolor neuropático, lo que no modifica el curso de la enfermedad.

El puntaje alto (99.23%) proviene de una predicción basada en grafos, sin datos clínicos que la respalden. Las otras tres predicciones del modelo (dermatomiositis neonatal, dermatomiositis amiopática y enfermedad pulmonar intersticial infantil asociada a enfermedad del tejido conectivo) tienen puntajes similares y tampoco tienen evidencia. Es probable que compartan un mismo artefacto de vecindad en el grafo y no constituyan señales independientes.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 10 autorizaciones. Los textos de indicación aprobada no están disponibles en los datos recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 57109 | BUPIVACAINA PHYSAN 2,5 MG/ML SOLUCION INYECTABLE | Solución inyectable | No disponible |
| 58023 | BUPIVACAINA PHYSAN 7,5 MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | No disponible |
| 81695 | BUPIVACAINA ACCORD 2,5 MG/ML SOLUCION INYECTABLE EFG | Solución inyectable | No disponible |
| 81696 | BUPIVACAINA ACCORD 5 MG/ML SOLUCION INYECTABLE EFG | Solución inyectable | No disponible |
| 62412 | BUPIVACAINA B.BRAUN 2,5 mg/ml SOLUCION INYECTABLE | Solución inyectable | No disponible |

## Consideraciones de Seguridad

- **Dianas farmacológicas registradas** (son datos de farmacología, no interacciones con otros fármacos): Nav1.5 (SCN5A, humano), Kv1.5 (KCNA5, humano), Kv4.3 (Kcnd3, ratón) y Kir3.2. Nav1.5 es el canal de sodio cardíaco, lo que concuerda con la cardiotoxicidad conocida de bupivacaína.
- **Preocupaciones señaladas en la evaluación de las predicciones**:
  - Bupivacaína es miotóxica a concentraciones altas, lo que es una preocupación teórica en enfermedades inflamatorias del músculo como la dermatomiositis.
  - En población neonatal, su cardiotoxicidad y sus límites de dosis añaden un riesgo de seguridad.

Para advertencias y contraindicaciones detalladas, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos clínicos ni publicaciones (nivel L5), y no se identifica un vínculo mecanístico creíble entre el bloqueo de canales de sodio y una infección por *Borrelia* tratada con antibióticos. El puntaje alto del modelo por sí solo no basta para avanzar.

**Para avanzar se necesita:**
- Advertencias y contraindicaciones del prospecto de la AEMPS (actualmente no disponibles y bloqueantes para el cribado de seguridad)
- Datos del mecanismo de acción desde DrugBank
- Evidencia preclínica o clínica que vincule bupivacaína con la acrodermatitis crónica atrófica, o revisar las otras tres predicciones por si alguna tiene un fundamento biológico
- Textos de indicación aprobada de las autorizaciones españolas, para confirmar la indicación original
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


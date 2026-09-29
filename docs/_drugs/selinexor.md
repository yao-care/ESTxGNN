---
layout: default
title: Selinexor
parent: Solo predicción del modelo (L5)
nav_order: 487
evidence_level: L5
indication_count: 1
---

# Selinexor
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

# Selinexor: De Indicación Original No Registrada a Osteoporosis Inducida por Fármacos

## Resumen en Una Frase

Selinexor es un inhibidor de XPO1 (exportina-1) comercializado en España como NEXPOVIO. El Evidence Pack no registra su indicación aprobada. El modelo TxGNN predice que podría ser efectivo para **osteoporosis inducida por fármacos**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, así que se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (el texto de indicación aprobada de la AEMPS está vacío) |
| Nueva Indicación Predicha | Osteoporosis inducida por fármacos |
| Puntaje de Predicción TxGNN | 99.22% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Selinexor inhibe XPO1, lo que afecta a la señalización de NF-κB y a la retención nuclear de supresores tumorales. Existen trabajos preclínicos sobre enfermedad ósea en mieloma que exploran efectos en las células de remodelado óseo. Este análisis no incluye citas que los respalden, por lo que el vínculo es hipotético y no está verificado.

El puntaje alto (0.992) refleja únicamente una asociación en el grafo de conocimiento. Hay dos motivos para interpretarlo con mucha cautela:

- **Confusión con dexametasona:** selinexor suele administrarse junto con dexametasona, una causa conocida de osteoporosis inducida por glucocorticoides. Cualquier efecto óseo observado en esos regímenes estaría confundido y no debe leerse como señal terapéutica.
- **Dirección del efecto:** el puntaje podría reflejar una asociación con la pérdida ósea como efecto adverso y no como beneficio terapéutico. Con los datos disponibles no se puede determinar la dirección del efecto.

La similitud con la indicación original y la compatibilidad de vías de administración están pendientes de evaluar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1211537001 | NEXPOVIO 20 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No especificada en los datos disponibles |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de XPO1), antineoplásico |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos ni literatura. Además, la dirección del efecto es incierta y hay un factor de confusión importante con dexametasona.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), dato que bloquea el cribado de seguridad
- Confirmar la indicación aprobada y el mecanismo de acción desde DrugBank
- Buscar evidencia preclínica y clínica de los efectos de selinexor sobre el hueso, separando el efecto de la dexametasona
- Determinar si la asociación del grafo indica beneficio terapéutico o riesgo de pérdida ósea
- Evaluar la similitud con la indicación original y la compatibilidad de vías de administración

*Este informe es solo para referencia de investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


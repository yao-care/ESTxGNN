---
layout: default
title: Safinamide
parent: Solo predicción del modelo (L5)
nav_order: 721
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-31
monitor_inn: "Safinamide"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration"]
description: "Safinamide: nueva indicación predicha, Encefalitis subaguda de Rasmussen (Rasmussen subacute encephalitis) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Safinamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Safinamide: Encefalitis subaguda de Rasmussen (Rasmussen subacute encephalitis)
{: .text-alpha }

## Resumen en Una Frase

Safinamida es un inhibidor de la monoaminooxidasa B (MAO-B), utilizado originalmente para el tratamiento de la enfermedad de Parkinson.
El modelo TxGNN predice que podría ser efectivo para la **encefalitis subaguda de Rasmussen**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Encefalitis subaguda de Rasmussen (Rasmussen subacute encephalitis) |
| Puntaje de Predicción TxGNN | 0.9963 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 11) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción original del fármaco. Según la información farmacológica conocida, safinamida es un inhibidor reversible y selectivo de la MAO-B (más de 800 veces más selectivo para MAO-B que para MAO-A). Se utiliza como tratamiento adyuvante en pacientes con Parkinson que presentan episodios "off". Además, se le atribuyen el bloqueo de canales de sodio dependientes de voltaje y la reducción de la liberación de glutamato.

Estas propiedades podrían relacionarse de forma plausible con las crisis epilépticas y los rasgos neuroinflamatorios de la encefalitis de Rasmussen. Sin embargo, esta enfermedad está impulsada principalmente por una inflamación autoinmune mediada por linfocitos T, y no se ha demostrado ningún vínculo directo entre ese mecanismo y safinamida.

Por tanto, la puntuación procede del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; el razonamiento mecanístico es especulativo. No se dispone de evidencia clínica ni bibliográfica que lo sustente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de principio activo único, ninguna cancelada). El texto de indicación aprobada no figura en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 91074 | Safinamida Teva 100 mg EFG | Comprimido recubierto con película | Teva Pharma S.L.U. |
| 114984008IP1 | Xadago 100 mg | Comprimido recubierto con película | Zambon S.P.A. |
| 90309 | Safinamida Stada 50 mg EFG | Comprimido recubierto con película | Laboratorio Stada S.L. |
| 114984003 | Xadago 50 mg | Comprimido recubierto con película | Zambon S.P.A. |
| 90156 | Safinamida Aurovitas 100 mg EFG | Comprimido recubierto con película | Aurovitas Spain, S.A.U. |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó y registró una única entrada, que corresponde a la diana farmacológica del fármaco (MAO-B, gen *MAOB*), no a una interacción con otro medicamento. No se identificaron interacciones con otros fármacos con nivel de gravedad asignado.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje TxGNN alto, pero no cuenta con ningún ensayo clínico ni publicación (nivel L5). Además, la base fisiopatológica de la encefalitis de Rasmussen (autoinmunidad mediada por linfocitos T) no guarda una relación mecanística demostrada con safinamida.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), imprescindible antes de cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción del fármaco.
- Revisión sistemática de literatura y de registros de ensayos sobre safinamida en encefalitis de Rasmussen.
- Estudios preclínicos que respalden una hipótesis mecanística concreta.
- Valorar, como alternativas, las otras dos predicciones del modelo: la **mielitis** (puntaje 0.9946, L5, hipótesis muy especulativa por la heterogeneidad de la enfermedad) y la **neurodegeneración asociada a PLA2G6** (puntaje 0.9922, L5), que es la biológicamente más plausible por su solapamiento con el parkinsonismo, aunque sigue sin respaldo clínico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


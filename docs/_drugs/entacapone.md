---
layout: default
title: Entacapone
parent: Solo predicción del modelo (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Entacapone
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

# Entacapona: De Enfermedad de Parkinson a Neurodegeneración Asociada a PLA2G6

## Resumen en Una Frase

Entacapona es un inhibidor de la COMT que se usa como complemento del tratamiento con levodopa/carbidopa en la enfermedad de Parkinson.
El modelo TxGNN predice que podría ser efectivo para la **neurodegeneración asociada a PLA2G6**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, por lo que es solo una hipótesis del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Parkinson (complemento de levodopa/carbidopa; según la fuente farmacológica, ya que las fichas de AEMPS no traen texto de indicación) |
| Nueva Indicación Predicha | Neurodegeneración asociada a PLA2G6 |
| Puntaje de Predicción TxGNN | 99.76% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Entacapona es un inhibidor periférico de la catecol-O-metiltransferasa (COMT). Al bloquear esta enzima, prolonga la disponibilidad de levodopa y dopamina y mejora la eficacia del tratamiento en la enfermedad de Parkinson. Los datos farmacológicos también la asocian con el transportador mitocondrial de piruvato (MPC2 y MPC1L). El campo de mecanismo de acción de DrugBank no está disponible, por lo que esta descripción proviene de los datos de farmacología y del razonamiento del propio paquete de evidencia.

Algunos fenotipos de la neurodegeneración asociada a PLA2G6 incluyen distonía-parkinsonismo. Por eso existe un vínculo dopaminérgico plausible con la indicación original. Aun así, el vínculo es solo teórico: el puntaje del modelo no constituye evidencia clínica, y la similitud formal con la indicación original está pendiente de evaluar.

Un tratamiento sintomático que actúa sobre la vía dopaminérgica podría aliviar el componente parkinsoniano. No hay datos que indiquen que modifique la neurodegeneración de fondo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 77488 | Entacapona Aurovitas 200 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Aurovitas Spain, S.A.U. |
| 76383 | Entacapona Viatris 200 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Viatris Limited |
| 82845 | Medapia 200 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Medochemie Iberia S.A. |
| 10655003 | Entacapona Teva 200 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Teva B.V. |
| 98081003 | Comtan 200 mg comprimidos recubiertos con película | Comprimido recubierto con película | Orion Corporation |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Los datos de farmacología registran tres dianas de la entacapona: COMT, MPC2 y MPC1L. No se dispone de interacciones con otros fármacos con nivel de gravedad asignado.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos clínicos ni literatura para esta indicación. Además, faltan los datos de seguridad de la ficha técnica de AEMPS.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de AEMPS (advertencias y contraindicaciones), que es un vacío bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda dirigida de literatura y ensayos sobre entacapona en distonía-parkinsonismo por PLA2G6.
- Como alternativa dentro de las predicciones, priorizar la revisión de "parkinsonismo juvenil de Hunt" y "demencia con cuerpos de Lewy". Ambas tienen un vínculo dopaminérgico más coherente y están clasificadas como preguntas de investigación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


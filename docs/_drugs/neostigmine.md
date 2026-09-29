---
layout: default
title: Neostigmine
parent: Solo predicción del modelo (L5)
nav_order: 376
evidence_level: L5
indication_count: 10
---

# Neostigmine
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

# Neostigmina: De Reversión del Bloqueo Neuromuscular a Miastenia Gravis con Hiperplasia Tímica

## Resumen en Una Frase

Neostigmina es un inhibidor de la acetilcolinesterasa. Según la base farmacológica consultada, se usa en la miastenia gravis, en la reversión de relajantes musculares, en el íleo paralítico y en la retención urinaria posoperatoria. El modelo TxGNN predice que podría ser efectiva para **miastenia gravis con hiperplasia tímica**, pero **actualmente no hay ensayos clínicos ni publicaciones** específicos que respalden esta indicación, por lo que es solo una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en las autorizaciones de AEMPS (texto de indicación vacío). Según farmacología (GtoPdb): miastenia gravis, reversión de relajantes musculares, íleo paralítico, retención urinaria posoperatoria |
| Nueva Indicación Predicha | Miastenia gravis con hiperplasia tímica |
| Puntaje de Predicción TxGNN | 99,97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información farmacológica conocida, neostigmina inhibe la acetilcolinesterasa (gen *ACHE*), la enzima que degrada la acetilcolina en la unión neuromuscular. Al inhibirla, la acetilcolina permanece más tiempo disponible y se potencia la transmisión colinérgica.

En la miastenia gravis autoinmune, los anticuerpos reducen o bloquean los receptores de acetilcolina en la placa motora. Prolongar la acción de la acetilcolina sobre los receptores restantes es la base del tratamiento sintomático estándar. Por eso la predicción es biológicamente plausible, y la miastenia gravis ya figura entre los usos clínicos conocidos de neostigmina.

La hiperplasia tímica es un subtipo frecuente de miastenia gravis. Sin embargo, no se recuperó ningún ensayo ni publicación específica de este subtipo. El efecto es sintomático y no modifica la enfermedad autoinmune de fondo. Mientras una fuente curada no lo confirme, debe tratarse solo como predicción.

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
| 4237 | PROSTIGMINE AMPOLLAS (Meda Pharma S.L.) | Solución inyectable | No especificada en los datos disponibles |
| 36384 | NEOSTIGMINA BRAUN 0,5 MG/ML (B Braun Medical S.A.) | Solución inyectable | No especificada en los datos disponibles |

Ambas presentaciones son inyectables.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó y no devolvió interacciones fármaco-fármaco. Solo registró la diana farmacológica, la acetilcolinesterasa (*ACHE*, humana).

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es mecanísticamente coherente, pero no hay ningún ensayo ni publicación específica de miastenia gravis con hiperplasia tímica (nivel L5, solo predicción del modelo). Además, faltan los datos de seguridad del prospecto de AEMPS, que impiden avanzar al cribado de seguridad.

Dentro de este mismo paquete, la variante *miastenia autoinmune de cinturas* (nivel L4) y la miastenia gravis en general tienen algo más de respaldo indirecto. Aun así, la evidencia disponible es indirecta: una revisión y un estudio genético que no evalúan neostigmina en ese fenotipo.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), un vacío de datos bloqueante.
- Obtener datos del mecanismo de acción desde DrugBank.
- Confirmar el texto de indicación aprobada de las dos autorizaciones.
- Buscar en una fuente curada (guías clínicas, revisiones sistemáticas) evidencia sobre inhibidores de la colinesterasa en miastenia gravis con hiperplasia tímica.
- Definir si la vía inyectable es compatible con el uso previsto, ya que la compatibilidad de vías sigue pendiente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Brinzolamide
parent: Solo predicción del modelo (L5)
nav_order: 113
evidence_level: L5
indication_count: 1
---

# Brinzolamide
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

# Brinzolamida: De Glaucoma de Ángulo Abierto a Glaucoma Hereditario Primario

## Resumen en Una Frase

Brinzolamida es un inhibidor de la anhidrasa carbónica de uso tópico ocular, utilizado originalmente para el tratamiento del glaucoma de ángulo abierto y la hipertensión ocular.
El modelo TxGNN predice que podría ser efectivo para el **glaucoma hereditario primario**, pero actualmente **no hay ensayos clínicos ni publicaciones** registrados que respalden esta dirección; se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Glaucoma de ángulo abierto e hipertensión ocular (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 99,48 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Brinzolamida inhibe la anhidrasa carbónica, en particular la isoforma II. Al hacerlo reduce la secreción de humor acuoso y, con ello, la presión intraocular (PIO). Los datos compilados para este report no incluyen una descripción detallada del mecanismo de acción, por lo que este razonamiento se apoya en conocimiento farmacológico general. Los datos de farmacología sí confirman que el fármaco actúa sobre varias isoformas de anhidrasa carbónica humana (CA1, CA7, CA12 y CA14) y que su uso clínico es reducir la PIO elevada en hipertensión ocular y glaucoma de ángulo abierto.

El glaucoma hereditario primario (por ejemplo, el glaucoma congénito primario o el glaucoma juvenil de ángulo abierto) comparte con la indicación original un factor modificable central: la PIO elevada, principal causa del daño del nervio óptico. Por ello, es plausible que reducir la producción de humor acuoso aporte beneficio.

Conviene interpretar el puntaje tan alto con cautela: probablemente refleja la estrecha similitud con las indicaciones ya aprobadas y la vía compartida de reducción de la PIO, más que evidencia independiente. Además, en el glaucoma congénito primario la patología de fondo es la disgenesia del trabéculo y del ángulo, y el tratamiento médico suele ser solo un puente hacia la cirugía. También preocupa la seguridad pediátrica, ya que la absorción sistémica de inhibidores de la anhidrasa carbónica puede causar alteraciones del equilibrio ácido-base en lactantes. Estos puntos requieren una evaluación específica.

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
| 80098 | Brinzolamida Cinfa 10 mg/ml colirio en suspensión | Colirio en suspensión | No disponible en los datos compilados |
| 79856 | Brinzolamida Stada 10 mg/ml colirio en suspensión | Colirio en suspensión | No disponible en los datos compilados |
| 80014 | Brinzolamida Vir 10 mg/ml colirio en suspensión | Colirio en suspensión | No disponible en los datos compilados |
| 00129001 | Azopt 10 mg/ml colirio en suspensión | Colirio en suspensión | No disponible en los datos compilados |
| 90850 | Aicisi 10 mg/ml colirio en suspensión | Colirio en suspensión | No disponible en los datos compilados |

Existe una sexta autorización vigente (Bolesin 10 mg/ml, n.º 90069, Thalassa Pharma S.L.). En total hay 6 autorizaciones vigentes de monofármaco y ninguna cancelada.

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: la consulta se completó y devolvió 4 registros, todos de tipo farmacológico (dianas). No son interacciones con otros medicamentos, sino la unión de brinzolamida a las isoformas humanas de anhidrasa carbónica CA1, CA7, CA12 y CA14. No se han identificado interacciones con otros fármacos con nivel de gravedad asignado.

Para advertencias y contraindicaciones, consultar el prospecto, ya que no se dispone de esa información en los datos compilados. Dado que este vacío es bloqueante para el cribado de seguridad, debe resolverse antes de avanzar.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura que la respalden. Además, faltan los datos de advertencias y contraindicaciones del prospecto, lo que impide el cribado de seguridad, y existen dudas específicas sobre la población pediátrica.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS para obtener advertencias, contraindicaciones e indicaciones aprobadas.
- Obtener datos detallados del mecanismo de acción (por ejemplo, mediante la API de DrugBank).
- Revisar la literatura y los registros de ensayos sobre el uso de brinzolamida en glaucoma congénito y juvenil.
- Evaluar la seguridad pediátrica (absorción sistémica, alteraciones ácido-base) y el papel real del tratamiento médico frente a la cirugía.
- Confirmar la compatibilidad de vía de administración y la similitud con la indicación original, que están pendientes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


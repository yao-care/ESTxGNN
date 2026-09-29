---
layout: default
title: Amlodipine
parent: Solo predicción del modelo (L5)
nav_order: 38
evidence_level: L5
indication_count: 10
---

# Amlodipine
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

# Amlodipino: De Hipertensión a Infarto del Tronco Encefálico

## Resumen en Una Frase

Amlodipino es un antagonista de los canales de calcio dihidropiridínico, utilizado originalmente para la hipertensión y la angina de pecho estable crónica.
El modelo TxGNN predice que podría ser efectivo para **infarto del tronco encefálico**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, por lo que se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Las 5 autorizaciones de AEMPS revisadas no incluyen texto de indicación. Según la base farmacológica (IUPHAR): hipertensión y angina estable crónica |
| Nueva Indicación Predicha | Infarto del tronco encefálico (brain stem infarction) |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Amlodipino actúa como modulador de la apertura (*gating*) de los canales de calcio dependientes de voltaje. La base farmacológica lo asocia con Ca<sub>v</sub>1.2 y Ca<sub>v</sub>1.3, y también con P2X4. No se dispone de datos detallados de mecanismo de acción en DrugBank, y la fuente indica que no hay un blanco principal claramente definido. Su efecto conocido es la vasodilatación sistémica y el descenso de la presión arterial.

La relación con el infarto del tronco encefálico sería indirecta. Controlar la presión arterial reduce el riesgo cerebrovascular, y esa sería la única vía plausible. Este vínculo no está verificado, porque no hay ensayos ni literatura que evalúen amlodipino en esta enfermedad.

Además, buena parte de este posible beneficio sería una extensión del uso antihipertensivo ya existente, más que un reposicionamiento con un mecanismo nuevo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 90902 | AMLODIPINO TEVA-RATIOPHARM 5 MG COMPRIMIDOS EFG | Comprimido | No especificada en los datos |
| 84861 | AMLODIPINO BLUEPHARMA 5 MG COMPRIMIDOS EFG | Comprimido | No especificada en los datos |
| 85522 | AMLODIPINO MABO 5 MG COMPRIMIDOS EFG | Comprimido | No especificada en los datos |
| 59160 | NORVAS 10 mg COMPRIMIDOS | Comprimido | No especificada en los datos |
| 72814 | AMLODIPINO COMBIX 10 mg COMPRIMIDOS EFG | Comprimido | No especificada en los datos |

---

## Consideraciones de Seguridad

- **Farmacología / blancos moleculares**: la consulta no devolvió interacciones con otros medicamentos. Solo registró interacciones farmacológicas con blancos moleculares: P2X4 (humano), Ca<sub>v</sub>1.2 (conejo) y Ca<sub>v</sub>1.3 (humano).

Consultar el prospecto para información de advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (99.94%), pero no cuenta con ningún ensayo clínico ni publicación. Solo existe una hipótesis indirecta basada en el control de la presión arterial, por lo que el nivel de evidencia es L5.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto (ficha técnica) de AEMPS para completar la revisión de seguridad
- Completar los datos del mecanismo de acción (DrugBank)
- Buscar evidencia específica de amlodipino en infarto del tronco encefálico, ya que actualmente no hay ninguna
- Priorizar otras indicaciones predichas con más respaldo: **hemorragia intracerebral** (L2, ensayo de Fase 3 TRIDENT completado con 1671 pacientes, aunque evalúa una combinación de tres fármacos) y **oclusión de arteria cerebral** (L4, estudios preclínicos de neuroprotección en roedores)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Diclofenac
parent: Solo predicción del modelo (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Diclofenac
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

# Diclofenaco: De Dolor e Inflamación (Artrosis y Artritis Reumatoide) a Hipotricosis Simple del Cuero Cabelludo

## Resumen en Una Frase

Diclofenaco es un antiinflamatorio no esteroideo (AINE) utilizado para tratar el dolor y la inflamación de la artrosis y la artritis reumatoide.
El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es solo una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el texto de las autorizaciones. Según la base farmacológica: dolor e inflamación en artrosis y artritis reumatoide |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 99.69% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de la ficha del fármaco. Los datos farmacológicos complementarios indican que diclofenaco actúa sobre COX-1 y COX-2 (inhibición de la síntesis de prostaglandinas). También aparece asociado a TRPM3, PPARγ, ASIC3 y al transportador de aminoácidos PAT1 (SLC36A1). Su eficacia como analgésico y antiinflamatorio en enfermedades articulares está bien establecida.

Para esta predicción concreta, **los datos no respaldan un vínculo mecanístico**. La hipotricosis simple es un trastorno genético del folículo piloso, y no se identifica una vía plausible que conecte la inhibición de la COX con su fisiopatología. La relación con la indicación original está pendiente de evaluar.

El puntaje alto (99.69%) debe interpretarse con cautela. Refleja la posición del fármaco en el grafo de conocimiento del modelo, no una prueba de eficacia. Las otras predicciones de mayor rango (displasias esqueléticas, alopecia areata difusa, síndrome WHIM) tampoco tienen evidencia clínica ni vínculo mecanístico documentado.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones. El texto de indicación aprobada no está disponible en los datos recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 74119 | Diclofenaco Kern Pharma 11,6 mg/g gel | Gel | Kern Pharma S.L. |
| 62000 | Diclofenaco Pensa 50 mg comprimidos gastrorresistentes EFG | Comprimido | Towa Pharmaceutical S.A. |
| 62024 | Voltaren Retard 75 mg comprimidos de liberación modificada | Comprimido de liberación modificada | Novartis Farmacéutica S.A. |
| 57589 | Diclofenaco Llorens 75 mg solución inyectable EFG | Solución inyectable | Laboratorios Llorens S.L. |
| 61866 | Diclofenaco Alter 50 mg comprimidos gastrorresistentes EFG | Comprimido gastrorresistente | Laboratorios Alter S.A. |

El conjunto de autorizaciones incluye también otras formas: jeringa precargada, colirio, supositorio y solución para pulverización cutánea.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es de nivel L5: no hay ensayos, no hay literatura y no hay un vínculo mecanístico plausible entre la inhibición de la COX y un trastorno genético del folículo piloso. Con estos datos no se justifica avanzar.

**Para avanzar se necesita:**
- Datos preclínicos o de mecanismo que conecten la vía de las prostaglandinas con la hipotricosis simple.
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), actualmente sin datos y con impacto bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisar las demás predicciones. La de **artritis idiopática juvenil** (rango 9, puntaje 99.25%) tiene evidencia nivel L3, con estudios clínicos antiguos de diclofenaco en artritis juvenil, y recomendación "Proceed with Guardrails". Es más cercana a un uso ya establecido de la clase AINE que a un reposicionamiento nuevo, y es la candidata con más respaldo de este paquete.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


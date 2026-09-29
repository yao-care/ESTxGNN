---
layout: default
title: Lomitapide
parent: Solo predicción del modelo (L5)
nav_order: 325
evidence_level: L5
indication_count: 10
---

# Lomitapide
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

# Lomitapida: De Hipercolesterolemia Familiar Homocigota (uso probable, por verificar) a Macrotrombocitopenia con Insuficiencia Mitral

## Resumen en Una Frase

Lomitapida es un inhibidor de la proteína microsomal de transferencia de triglicéridos (MTP), comercializado en España como Lojuxta. El registro de autorizaciones no incluye el texto de la indicación aprobada. Según la evidencia recopilada, su uso probable es la hipercolesterolemia familiar homocigota.
El modelo TxGNN predice que podría ser efectivo para **macrotrombocitopenia con insuficiencia mitral**, pero hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipercolesterolemia familiar homocigota (probable; el texto de indicación no consta en el registro y debe verificarse con la ficha técnica) |
| Nueva Indicación Predicha | Macrotrombocitopenia con insuficiencia mitral |
| Puntaje de Predicción TxGNN | 99.92% (posición 1925 en el ranking del modelo) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Lomitapida inhibe la proteína MTP en hepatocitos y enterocitos. Esta proteína es necesaria para ensamblar y secretar lipoproteínas que contienen apoB (VLDL en el hígado, quilomicrones en el intestino). Al bloquearla, se reduce el colesterol LDL. No hay datos detallados adicionales sobre el mecanismo de acción en el registro.

**Con los datos actuales, esta predicción no resulta razonable.** No se identificó ningún vínculo mecanístico plausible entre la inhibición de MTP y un trastorno plaquetario con valvulopatía mitral. El puntaje alto de TxGNN refleja probablemente la cercanía en el grafo de conocimiento entre enfermedades plaquetarias, no una base farmacológica.

Las otras ocho predicciones de mayor puntaje, todas trastornos plaquetarios (trombocitopenia hereditaria, enfermedad de gránulos densos, trombastenia de Glanzmann, entre otras), tampoco tienen ensayos ni literatura y presentan el mismo problema.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 113851003 | LOJUXTA 20 MG CAPSULAS DURAS | Cápsula dura | Chiesi Farmaceutici S.P.A. |
| 113851002 | LOJUXTA 10 MG CAPSULAS DURAS | Cápsula dura | Chiesi Farmaceutici S.P.A. |
| 113851001 | LOJUXTA 5 MG CAPSULAS DURAS | Cápsula dura | Chiesi Farmaceutici S.P.A. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Además, la evaluación de la predicción sobre trombocitopenia neonatal transitoria señala que lomitapida tiene advertencias de toxicidad embrio-fetal y no se ha estudiado en neonatos.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal es solo del modelo (L5), sin ensayos ni publicaciones, y no tiene un vínculo mecanístico plausible con el mecanismo de lomitapida. No hay base para avanzar.

**Para avanzar se necesita:**
- Verificar la indicación aprobada en la ficha técnica de la AEMPS. El registro no la incluye, y sin ella no se puede confirmar cuál es el uso original.
- Un mecanismo hipotético que conecte la inhibición de MTP con la fisiopatología plaquetaria, más estudios preclínicos que lo respalden.
- Obtener las advertencias y contraindicaciones del prospecto de la AEMPS para el cribado de seguridad.

**Nota sobre otra predicción del mismo análisis:** la única predicción con evidencia real es *hiperlipoproteinemia* (rank 9, puntaje 99.74%, nivel L2, Proceed with Guardrails). Cuenta con 12 ensayos, incluidos Fase 3 completados en hipercolesterolemia familiar homocigota (NCT00730236, NCT04681170, NCT02173158, NCT00943306), y 21 publicaciones. Es probablemente un uso ya aprobado (on-label) y no un reposicionamiento genuino. No se asigna L1 porque los estudios pivotales de Fase 3 son de un solo brazo y la evidencia aleatorizada es de Fase 2 (NCT00690443, NCT00559962). Las salvaguardas necesarias serían monitorizar hepatotoxicidad (esteatosis y transaminasas), vigilar efectos gastrointestinales, tener en cuenta el riesgo embrio-fetal y controlar las interacciones con CYP3A4.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


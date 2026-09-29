---
layout: default
title: Tazarotene
parent: Solo predicción del modelo (L5)
nav_order: 512
evidence_level: L5
indication_count: 3
---

# Tazarotene
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Tazaroteno: De Psoriasis en Placas y Acné a Dermatitis Seborreica

## Resumen en Una Frase

El tazaroteno es un retinoide tópico que se usa en trastornos de la piel como el acné y la psoriasis en placas. Según la información farmacológica disponible, no consta el texto de indicación aprobado en las autorizaciones españolas.
El modelo TxGNN predice que podría ser efectivo para **dermatitis seborreica**. Hasta ahora solo hay **1 ensayo clínico de relevancia indirecta** (en acné, no en dermatitis seborreica) y **ninguna publicación** que respalde esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Acné y psoriasis en placas (según la ficha farmacológica; las autorizaciones de AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Dermatitis seborreica |
| Puntaje de Predicción TxGNN | 99.79% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

El tazaroteno actúa sobre los receptores del ácido retinoico (RARα, RARβ y RARγ). Los datos farmacológicos indican que tiene la mayor afinidad por RARβ. No se dispone de datos curados del mecanismo de acción en DrugBank. Por eso la descripción que sigue se basa en el conocimiento general de la clase de los retinoides tópicos, no en datos verificados de este candidato.

Como retinoide tópico, se considera que normaliza la diferenciación de los queratinocitos, reduce su hiperproliferación y disminuye la inflamación. Estos procesos son la base de su uso en acné y psoriasis. La dermatitis seborreica es una dermatosis inflamatoria de zonas ricas en sebo, con descamación y recambio celular alterado. Por eso es plausible que un fármaco con ese perfil pudiera ayudar.

Esta relación es solo una hipótesis mecanística. El puntaje de 99.79% es una predicción computacional y no tiene validación clínica en los datos disponibles.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06281782](https://clinicaltrials.gov/study/NCT06281782) | No aplica | Desconocido | 40 | Compara plasma rico en plaquetas más retinoides tópicos frente a retinoides tópicos solos en acné vulgar. No estudia dermatitis seborreica ni aísla el tazaroteno. Solo aporta contexto indirecto y no es evidencia para esta indicación. |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 61862 | ZORAC 0,05%, GEL | Gel (tópico) | Allergan Pharmaceuticals International Limited |
| 61861 | ZORAC 0,1%, GEL | Gel (tópico) | Allergan Pharmaceuticals International Limited |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

La consulta de interacciones solo devolvió las dianas farmacológicas del tazaroteno (RARα, RARβ y RARγ). No hay interacciones fármaco-fármaco documentadas.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN es muy alta, pero no hay ensayos ni publicaciones que evalúen el tazaroteno en dermatitis seborreica. El único ensayo asociado trata acné y no es evidencia directa. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Revisar el prospecto de AEMPS para completar advertencias y contraindicaciones, y confirmar la indicación aprobada.
- Obtener datos curados del mecanismo de acción (por ejemplo, desde DrugBank) para sustentar el vínculo mecanístico.
- Realizar una búsqueda dirigida de literatura sobre retinoides tópicos en dermatitis seborreica.
- Valorar la irritación cutánea de un retinoide tópico en zonas de piel sensible, típicas de esta enfermedad.
- Como referencia, la segunda predicción, **queratosis seborreica**, tiene evidencia L3 (una revisión sistemática de 2023 y un estudio comparativo de 2004 frente a crioterapia). Podría ser una línea más avanzada que la dermatitis seborreica, aunque su eficacia frente al estándar de cuidado no está establecida.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


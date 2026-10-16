---
layout: default
title: Bempedoic Acid
parent: Solo predicción del modelo (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bempedoic Acid: nueva indicación predicha, Hipertiroidismo (nivel de evidencia L5). Indicación original: Hipercolesterolemia (conocimiento general"
---

# Bempedoic Acid
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

# Ácido bempedoico: De Hipercolesterolemia a Hipertiroidismo

## Resumen en Una Frase

El ácido bempedoico es un hipolipemiante que inhibe la enzima ATP-citrato liasa (ACLY) y se comercializa en España para reducir el colesterol LDL (esta indicación original es conocimiento general del fármaco; los datos compilados no incluyen el texto de indicación de las autorizaciones).
El modelo TxGNN predice que podría ser efectivo para **hipertiroidismo**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipercolesterolemia (conocimiento general; el texto de indicación de las autorizaciones españolas no está disponible en los datos compilados) |
| Nueva Indicación Predicha | Hipertiroidismo |
| Puntaje de Predicción TxGNN | 99.61% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

El ácido bempedoico inhibe la ATP-citrato liasa (ACLY), una enzima situada por encima de la HMG-CoA reductasa en la síntesis hepática de colesterol. Una vez activado, reduce el colesterol LDL al aumentar la expresión de los receptores de LDL.

**No se ha identificado un vínculo mecanístico establecido con el hipertiroidismo.** El fármaco no tiene acción conocida sobre la síntesis ni la secreción de hormonas tiroideas. El puntaje elevado de TxGNN proviene de relaciones en la red de conocimiento (grafo biomédico), no de datos clínicos ni de literatura. Por ello debe interpretarse con mucha cautela: un puntaje alto no equivale a plausibilidad biológica.

Un posible nexo indirecto sería el metabolismo lipídico, ya que las hormonas tiroideas influyen en el manejo hepático del colesterol. Sin embargo, no hay datos que demuestren que la inhibición de ACLY modifique la función tiroidea.

**Nota sobre otras predicciones del modelo:** entre las diez primeras, la única con respaldo bibliográfico es la **hipercolesterolemia familiar homocigota** (puntaje 99.48%, nivel L3). Cuenta con revisiones, un documento de consenso y un estudio de cohorte en práctica real (PMID 41274797), y su mecanismo es biológicamente plausible. Esa indicación parece una línea de investigación más prometedora que el hipertiroidismo.

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
| 1201425002 | NILEMDO 180 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 1201424002 | NUSTENDI 180 mg/10 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |

Ambas autorizaciones están vigentes y pertenecen a Daiichi Sankyo Europe GmbH.

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas:** se consultaron las bases de datos de interacciones y se registraron 23 interacciones en total; en los datos compilados se detallan 20.
  - **Gravedad mayor (12):** corticosteroides (hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona, metilprednisolona, deflazacort, fludrocortisona), levofloxacino y simvastatina.
  - **Gravedad moderada (8):** empagliflozina, gliburida, repaglinida, rifaximina, rosuvastatina, selexipag, fexofenadina y revefenacina.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipertiroidismo se basa solo en el modelo (L5), sin ensayos, sin literatura y sin un mecanismo plausible. Por ahora no justifica una inversión de investigación.

**Para avanzar se necesita:**
- Una hipótesis mecanística que justifique la relación entre la inhibición de ACLY y la función tiroidea, con estudios preclínicos que la apoyen.
- Revisión del prospecto de la AEMPS para completar advertencias, contraindicaciones e indicaciones autorizadas.
- Evaluar como alternativa prioritaria la hipercolesterolemia familiar homocigota, que cuenta con evidencia L3 y un mecanismo coherente. Requeriría estudios prospectivos frente a evinacumab, lomitapida y terapias dirigidas a PCSK9.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


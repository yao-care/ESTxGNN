---
layout: default
title: Ambroxol
parent: Solo predicción del modelo (L5)
nav_order: 48
evidence_level: L5
indication_count: 4
monitor_inn: "AMBROXOL"
predicted_indications: ["nasal cavity disease", "vulvovaginal candidiasis", "faucial diphtheria", "cervical disc degenerative disorder"]
last_modified_at: 2026-11-24
description: "Ambroxol: nueva indicación predicha, enfermedad de la cavidad nasal (nasal cavity disease) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Ambroxol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Ambroxol: mucolítico y secretolítico → enfermedad de la cavidad nasal (nasal cavity disease)
{: .text-alpha }

## Resumen en Una Frase

Ambroxol es un agente mucolítico y secretolítico que se comercializa en España en múltiples presentaciones orales y bucales.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de la cavidad nasal (nasal cavity disease)**,
pero actualmente no hay ensayos clínicos registrados y solo **1 publicación** de relevancia indirecta (sobre tos aguda) acompaña esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | enfermedad de la cavidad nasal (nasal cavity disease) |
| Puntaje de Predicción TxGNN | 0.9991 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 14; autorizadas no comercializadas: 1; revocadas o suspendidas: 5) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Ambroxol estimula la secreción de surfactante y de moco seroso y mejora el aclaramiento mucociliar. Además, se le atribuye una actividad de bloqueo de canales de sodio de tipo anestésico local y efectos antiinflamatorios. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción original, por lo que esta descripción procede del razonamiento general sobre el fármaco.

Estas propiedades podrían guardar relación con afecciones de la mucosa de las vías respiratorias superiores, entre ellas la cavidad nasal: mejorar el manejo de las secreciones y reducir la inflamación local sería, en teoría, útil. Se trata, sin embargo, de un vínculo plausible y no demostrado.

La única publicación disponible es una revisión de 2015 sobre tos aguda asociada a infecciones respiratorias virales, que solo se relaciona de forma indirecta con la enfermedad de la cavidad nasal. Ninguna fuente estudia directamente esta enfermedad, por lo que el nivel de evidencia se limita a L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26525480](https://pubmed.ncbi.nlm.nih.gov/26525480/) | 2015 | Revisión | Vestnik otorinolaringologii | Revisión sobre el tratamiento de la tos aguda asociada a gripe e infecciones respiratorias virales agudas; relevancia solo indirecta para la enfermedad de la cavidad nasal |

## Información de Mercado en España

Se registran al menos 20 autorizaciones, todas de producto de un solo principio activo; la lista puede ser parcial. Principales autorizaciones:

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 68110 | MUCOSAN 6 MG/ML JARABE | JARABE | Opella Healthcare Spain S.L. | Comercializada |
| 63790 | AMBROXOL NORMON 3 mg/ml SOLUCION ORAL EFG | JARABE | Laboratorios Normon S.A. | Comercializada |
| 86435 | BROXIVAN 6 MG/ML SOLUCION ORAL EFG | SOLUCIÓN ORAL | Medochemie Iberia S.A. | Comercializada |
| 56156 | MUCOSAN PEDIATRICO 3 mg/ml JARABE | JARABE | Opella Healthcare Spain S.L. | Comercializada |
| 63590 | MUXIMED JARABE EFG | JARABE | Amneal Pharma Spain S.L. | Comercializada |
| 86434 | BROXIVAN 3 MG/ML SOLUCION ORAL EFG | SOLUCIÓN ORAL | Medochemie Iberia S.A. | Comercializada |
| 80439 | BUCOXON 20 MG PASTILLAS PARA CHUPAR SABOR REGALIZ | PASTILLA PARA CHUPAR | Laboratorios Cinfa S.A. | Comercializada |
| 80208 | BUCOXON 20 MG PASTILLAS PARA CHUPAR SABOR MENTA | PASTILLA PARA CHUPAR | Laboratorios Cinfa S.A. | Comercializada |
| 86392 | AMBROXOL CINFA 6 MG/ML JARABE | JARABE | Laboratorios Cinfa S.A. | Comercializada |
| 56538 | MUCIBRÓN 3 mg/ ml SOLUCIÓN ORAL. | SOLUCIÓN ORAL | Laboratorios Normon S.A. | Comercializada |

Se muestran 10 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registra una interacción de tipo farmacológico con la glucosilceramidasa beta (GBA1). Ambroxol actúa como chaperona de esta enzima: a pH neutro inhibe su actividad en medio acelular, mientras que dentro de las células aumenta la actividad intralisosomal de la enzima.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La puntuación del modelo es muy alta (0.9991), pero no hay ensayos clínicos y la única publicación disponible aborda la tos aguda, no la enfermedad de la cavidad nasal. La predicción carece por ahora de respaldo clínico directo.

**Para avanzar se necesita:**
- Estudios clínicos o publicaciones que evalúen directamente ambroxol en enfermedades de la cavidad nasal
- Datos detallados del mecanismo de acción y su relación con la mucosa nasal
- Revisión de advertencias y contraindicaciones del prospecto autorizado por la AEMPS
- Evaluación de la compatibilidad de las vías de administración disponibles (oral, bucal, inyectable) con el uso nasal propuesto
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


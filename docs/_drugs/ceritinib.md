---
layout: default
title: Ceritinib
parent: Solo predicción del modelo (L5)
nav_order: 164
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
monitor_inn: "CERITINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "pulmonary sulcus neoplasm", "lung germ cell tumor", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "junctional epidermolysis bullosa"]
description: "Ceritinib: nueva indicación predicha, Fibromatosis gingival (fibromatosis, gingival) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Ceritinib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Ceritinib: Fibromatosis gingival (fibromatosis, gingival)
{: .text-alpha }

## Resumen en Una Frase

Ceritinib es un inhibidor de la quinasa del linfoma anaplásico (ALK), utilizado originalmente para el tratamiento del carcinoma de pulmón no microcítico (CPNM).
El modelo TxGNN predice que podría ser efectivo para **fibromatosis gingival**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Fibromatosis gingival (fibromatosis, gingival) |
| Puntaje de Predicción TxGNN | 0.9986 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, ceritinib es un inhibidor de la tirosina quinasa ALK, y su eficacia en el CPNM con reordenamiento de ALK ha sido comprobada, incluido el ensayo de fase 3 ASCEND-4 en primera línea frente a quimioterapia basada en platino.

Para la fibromatosis gingival no se ha identificado ningún vínculo mecanístico. El puntaje de TxGNN es muy alto (0.9986), pero proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. No se conoce una dependencia de ALK en esta enfermedad, que es un sobrecrecimiento del tejido gingival de naturaleza benigna.

Por ello, la predicción debe interpretarse con cautela: no hay una razón biológica demostrada que justifique que un inhibidor de ALK sea útil en este trastorno.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la fibromatosis gingival.

*Nota: para otras indicaciones predichas de menor rango (por ejemplo, neoplasia benigna de pulmón), la literatura recuperada trata sobre ceritinib en CPNM con ALK reordenado (como el ensayo ASCEND-4, PMID 28126333). Esa evidencia respalda la indicación ya aprobada y no se traslada a la fibromatosis gingival.*

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 115999001 | ZYKADIA 150 MG CÁPSULAS DURAS (Novartis Europharm Limited) | Cápsula dura | No disponible en los datos compilados |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa ALK) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; la literatura señala la vigilancia de la prolongación del intervalo QT, la función hepática y la función renal |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total (se muestran 20 de ellas, la mayoría de nivel moderado). Entre las principales:
  - **Gravedad mayor**: triamcinolona y budesonida.
  - **Gravedad moderada**: antiácidos y supresores de la acidez gástrica (famotidina, ranitidina, rabeprazol, omeprazol), corticoides (hidrocortisona, dexametasona, betametasona), antidiabéticos (metformina, pioglitazona, alogliptina, acarbosa, canagliflozina, albiglutida), loperamida, aprepitant y bisacodilo.
- **Otros riesgos descritos en la literatura**: prolongación del intervalo QT, toxicidad cardíaca, efectos renales e hipersensibilidad (reportes de casos y revisiones). Es información general sobre el perfil de ceritinib, no específica de la nueva indicación.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo, sin ensayos clínicos, sin literatura y sin un vínculo mecanístico plausible entre ALK y la fibromatosis gingival (nivel de evidencia L5). Además, otras predicciones del mismo listado se solapan con la indicación ya aprobada en CPNM o carecen igualmente de respaldo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de ceritinib y análisis de una posible relación con la fisiopatología de la fibromatosis gingival.
- Estudios preclínicos que muestren participación de ALK (o de otras dianas de ceritinib) en la enfermedad.
- Obtención y revisión del prospecto de AEMPS (advertencias, contraindicaciones e indicación autorizada), pendiente antes de cualquier evaluación de seguridad.
- Evaluación de la relación riesgo-beneficio, dado el perfil de toxicidad de un fármaco antineoplásico para una enfermedad benigna.
- Revisión de las demás indicaciones predichas, priorizando aquellas con algún respaldo indirecto.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


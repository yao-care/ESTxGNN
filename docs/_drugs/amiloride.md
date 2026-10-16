---
layout: default
title: Amiloride
parent: Evidencia moderada (L3-L4)
nav_order: 50
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-14
description: "Amiloride: nueva indicación predicha, Hipertensión renovascular maligna (nivel de evidencia L4). Indicación original: Hipertensión arterial e insuficiencia cardíaca congestiva (según la b…"
---

# Amiloride
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **6** 
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

# Amilorida: De Hipertensión Arterial a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Amilorida es un diurético ahorrador de potasio, utilizado originalmente para el tratamiento de la hipertensión y la insuficiencia cardíaca congestiva.
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**,
pero actualmente no hay ensayos clínicos y solo se dispone de **1 publicación** (una revisión sobre hipertensión mineralocorticoide) que no aborda directamente esta indicación.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial e insuficiencia cardíaca congestiva (según la base de conocimiento del modelo; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Hipertensión renovascular maligna |
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la amilorida bloquea el canal epitelial de sodio (ENaC), lo que reduce la reabsorción de sodio en el túbulo distal con efecto diurético y antihipertensivo suave, conservando potasio. Su eficacia en la hipertensión y la insuficiencia cardíaca congestiva está establecida, y mecanísticamente podría ser aplicable a otras formas de hipertensión.

La relación con la nueva indicación es solo indirecta. La hipertensión renovascular maligna está impulsada principalmente por la activación del sistema renina-angiotensina, de modo que el bloqueo del ENaC tiene una relevancia limitada. El puntaje elevado del modelo refleja sobre todo la similitud con la indicación antihipertensiva ya aprobada.

Además, la única publicación recuperada (PMID 12929904) trata de la investigación de la hipertensión mineralocorticoide y no de la hipertensión renovascular maligna. Por ello, la predicción debe considerarse una hipótesis y no una evidencia de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12929904](https://pubmed.ncbi.nlm.nih.gov/12929904/) | 2003 | Revisión | Journal of Hypertension. Supplement | Revisa la investigación de la hipertensión por mineralocorticoides (aldosteronismo primario, hipopotasemia, renina plasmática baja). No aborda la hipertensión renovascular maligna |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 86330 | Amilorida/Hidroclorotiazida Aurovitas 5 mg/50 mg comprimidos EFG | Comprimido | No disponible |
| 55423 | Diuzine 5 mg/50 mg comprimidos | Comprimido | No disponible |
| 53265 | Ameride 5 mg/50 mg comprimidos | Comprimido | No disponible |
| 57632 | Kalten | Cápsula dura | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad del modelo, no texto del prospecto): enfermedad renal, anuria, nefropatía diabética, diabetes mellitus, cetoacidosis diabética, déficit de potasio, acidosis (incluida la acidosis láctica adquirida), enfermedad hepática, encefalopatía y coma hepáticos, pancreatitis, enfermedad de la vesícula biliar, lupus eritematoso sistémico (incluido el pediátrico), gota, hiperuricemia, hiperparatiroidismo, osteítis fibrosa, piouréter e ictericia neonatal.
- **Interacciones farmacológicas**: se identificaron 136 interacciones. Las más relevantes de nivel moderado incluyen:
  - Corticosteroides: hidrocortisona, betametasona, budesonida, dexametasona.
  - Antidiabéticos: metformina, exenatida e inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina).
  - Laxantes: bisacodilo, aceite de ricino, glicerina, lactitol, lactulosa.
  - Otros: bupropión, dronabinol.
  
  Entre las de nivel menor figuran doxiciclina, amoxicilina y cimetidina.
- **Riesgo de hiperpotasemia**: es un riesgo clave en insuficiencia renal, especialmente relevante en la hipertensión maligna con afectación renal. Un caso clínico recuperado en otra indicación (PMID 8615380) describe hiperpotasemia grave en un paciente geriátrico.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya en una puntuación alta del modelo, pero no existen ensayos clínicos y la única publicación no aborda la indicación. El fundamento mecanístico es indirecto, y la hipertensión renovascular maligna es una condición aguda de alto riesgo, con riesgo de hiperpotasemia en la afectación renal.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA), por ejemplo desde DrugBank
- Advertencias y contraindicaciones del prospecto de AEMPS, necesarias para el cribado de seguridad
- Estudios preclínicos o clínicos específicos en hipertensión renovascular maligna
- Evaluación del riesgo de hiperpotasemia y de la función renal en esta población
- Considerar otras indicaciones predichas con mayor respaldo indirecto, como la cardiopatía pulmonar crónica (nivel L3, con estudios en insuficiencia cardíaca), que podría evaluarse como alternativa de investigación
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


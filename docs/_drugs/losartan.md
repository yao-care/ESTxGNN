---
layout: default
title: Losartan
parent: Evidencia moderada (L3-L4)
nav_order: 487
evidence_level: L4
indication_count: 8
last_modified_at: 2026-10-14
description: "Losartan: nueva indicación predicha, Hipertensión renovascular maligna (nivel de evidencia L4). Indicación original: Hipertensión / trastorno hipertensivo / nefropatía diabética (según e…"
monitor_inn: "losartan"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "Prinzmetal angina", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies"]
---

# Losartan
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **8** 
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

# Losartán: De Hipertensión a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Losartán es un antagonista del receptor de angiotensina II (AT1), utilizado originalmente para el tratamiento de la hipertensión y la nefropatía diabética.
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**,
pero actualmente no hay ensayos clínicos registrados y solo se dispone de **2 publicaciones** (un reporte de caso y un capítulo de métodos preclínicos).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión / trastorno hipertensivo / nefropatía diabética (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Hipertensión renovascular maligna |
| Puntaje de Predicción TxGNN | 99,73% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Losartán bloquea el receptor AT1 de la angiotensina II. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados, pero es conocido que este fármaco actúa sobre el sistema renina-angiotensina, y su eficacia en hipertensión y nefropatía diabética está establecida.

El sistema renina-angiotensina es central en la hipertensión renovascular, por lo que el bloqueo del AT1 es mecanísticamente plausible. Sin embargo, esta nueva indicación se solapa en gran medida con la indicación original de hipertensión, por lo que aporta poca novedad terapéutica.

La evidencia se limita a un reporte de caso (arteritis de Takayasu, con enalapril y losartán, con mejora de la presión arterial sin deterioro renal) y a un capítulo de métodos en modelos de rata. Debe actuarse con cautela en la estenosis bilateral de la arteria renal, donde los ARA-II pueden precipitar insuficiencia renal aguda.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10667645](https://pubmed.ncbi.nlm.nih.gov/10667645/) | 2000 | Reporte de caso | Angiology | Paciente con arteritis de Takayasu, nefrectomizada unilateralmente y con hipertensión maligna por estenosis de la arteria renal, refractaria al tratamiento convencional; enalapril y losartán mejoraron la presión arterial sin deterioro de la función renal |
| [22294399](https://pubmed.ncbi.nlm.nih.gov/22294399/) | 2009 | Métodos preclínicos | Current Protocols in Pharmacology | Protocolos para evaluar la actividad antihipertensiva en ratas conscientes (modelos SHR, DOCA-sal y Goldblatt) |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 79865 | Losartan Aurobindo 100 mg EFG | Comprimido recubierto con película | — |
| 79922 | Losartan Teva-Ratio 100 mg EFG | Comprimido recubierto con película | — |
| 81630 | Losartan Aurovitas 100 mg EFG | Comprimido recubierto con película | — |
| 70611 | Losartan Krka 25 mg | Comprimido recubierto con película | — |
| 78476 | Losartan Teva-Ratiopharm 50 mg EFG | Comprimido recubierto con película | — |

Se muestran 5 de las 20 autorizaciones vigentes (todas de fármaco único).

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, lupus eritematoso sistémico, deficiencia de potasio, diabetes mellitus, cetoacidosis diabética, hiperuricemia, trastornos hipotensivos, hiperparatiroidismo, coma y encefalopatía hepática, anuria, gota, hipercalcemia, nefrocalcinosis, alteraciones del metabolismo del fósforo, obstrucción de la arteria renal y deterioro de la función renal.
- **Interacciones farmacológicas**: se identificaron 253 interacciones. Las de nivel **mayor** incluyen citrato de potasio y bicarbonato de potasio (riesgo de hiperpotasemia). Entre las de nivel moderado figuran corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina), insulinas, ácido acetilsalicílico, morfina, bupropión y aprepitant.
- **Precaución específica**: estenosis bilateral de la arteria renal (riesgo de insuficiencia renal aguda con ARA-II).

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje del modelo es muy alto, la evidencia se reduce a un reporte de caso y a un capítulo de métodos preclínicos, sin ensayos clínicos. Además, la indicación se solapa con la hipertensión ya cubierta, por lo que el valor añadido es limitado.

**Para avanzar se necesita:**
- Estudios clínicos (idealmente ensayos controlados) en hipertensión renovascular maligna
- Datos detallados del mecanismo de acción
- Revisión del prospecto de la AEMPS (advertencias y contraindicaciones) y de los textos de indicación autorizados
- Plan de seguridad para pacientes con estenosis de la arteria renal, función renal alterada e hiperpotasemia
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


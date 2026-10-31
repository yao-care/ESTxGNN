---
layout: default
title: Pregabalin
parent: Solo predicción del modelo (L5)
nav_order: 660
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-31
monitor_inn: "Pregabalin"
predicted_indications: ["tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis", "inclusion body myositis", "migraine disorder", "migraine with brainstem aura"]
description: "Pregabalin: nueva indicación predicha, Tendinitis (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Pregabalin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Pregabalin: Tendinitis
{: .text-alpha }

## Resumen en Una Frase

Pregabalina es un fármaco que modula los canales de calcio dependientes de voltaje y que originalmente se utiliza en el trastorno de ansiedad, la fibromialgia, el síndrome de dolor miofascial y la neuralgia posherpética.
El modelo TxGNN predice que podría ser efectivo para **tendinitis**, pero actualmente **no hay ensayos clínicos** y solo **6 publicaciones** de relevancia indirecta (sin estudios que evalúen directamente su uso en tendinitis).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Tendinitis |
| Puntaje de Predicción TxGNN | 0.9971 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 14) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Pregabalina se une a la subunidad alfa2-delta de los canales de calcio dependientes de voltaje y reduce la liberación de neurotransmisores excitadores. Este mecanismo es la base de su utilidad en el dolor neuropático y en los componentes de sensibilización central del dolor.

La relación con la indicación original es parcial: fibromialgia y síndrome de dolor miofascial son cuadros de dolor musculoesquelético, y es probable que la similitud con estas afecciones explique en parte el puntaje del modelo. Sin embargo, la tendinitis es principalmente una afección mecánica e inflamatoria, por lo que el vínculo mecanístico es **indirecto**. La pregabalina podría, como mucho, aliviar el dolor, pero no modificar el proceso patológico del tendón.

Conviene ser prudente: la literatura recuperada trata sobre analgesia perioperatoria tras cirugía del hombro (reparación del manguito rotador), casos clínicos de atrapamiento nervioso y discapacidad asociada a fluoroquinolonas, no sobre el tratamiento de la tendinitis en sí. El puntaje tan alto de TxGNN es solo una predicción y no está respaldado por datos clínicos directos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | ECA | Arthroscopy | La pregabalina oral perioperatoria logró puntuaciones de dolor posoperatorio equivalentes al bloqueo interescalénico tras reparación artroscópica del manguito rotador (analgesia posquirúrgica, no tratamiento de tendinitis) |
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | Estudio de cohorte retrospectivo | J Orthop Sci | Evaluación de la eficacia analgésica y del efecto ahorrador de opioides de la pregabalina tras reparación del manguito rotador |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Revisión/Comentario | Praxis | Discapacidad asociada a fluoroquinolonas (ciprofloxacino), con tendinopatías entre los efectos adversos; relación solo tangencial |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Comentario editorial | Arthroscopy | Diagnóstico y tratamiento quirúrgico del síndrome piriforme (compresión del nervio ciático) |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Reporte de caso | Pain Pract | Atrapamiento del nervio cutáneo femoral posterior tras un maratón, asociado a tendinitis de isquiotibiales |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Preclínico (animal) | Adv Pharmacol Pharm Sci | Extracto de *Cissus quadrangularis* atenúa la neuropatía periférica inducida por vincristina en ratas (sin relación directa con pregabalina) |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 90014 | Pregabalina Normon 300 mg comprimidos EFG | Comprimido | No disponible en los datos compilados |
| 04279012IP | Lyrica 75 mg cápsulas duras | Cápsula dura | No disponible en los datos compilados |
| 104279015 | Lyrica 100 mg cápsulas duras | Cápsula dura | No disponible en los datos compilados |
| 80287 | Pregabalina Aurovitas 150 mg cápsulas duras EFG | Cápsula dura | No disponible en los datos compilados |
| 104279021 | Lyrica 200 mg cápsulas duras | Cápsula dura | No disponible en los datos compilados |

Se muestran 5 de las 20 autorizaciones vigentes (todas de monofármaco). Existen también presentaciones en solución oral (Pregabalina Wockhardt 20 mg/ml).

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): trastorno de ansiedad, trastorno neurótico, trastorno distímico, trombocitopenia, angioedema (incluidas las formas adquirida, hereditaria, no histaminérgica e inducida por bloqueadores del sistema renina-angiotensina-aldosterona), miopatía y enfermedades musculares, parálisis periódica familiar, rabdomiólisis, fascitis nodular, insuficiencia renal y bloqueo auriculoventricular. Cabe señalar que la aparición de "trastorno de ansiedad" en esta lista contrasta con su uso como indicación original, por lo que debe verificarse con el prospecto.
- **Interacciones farmacológicas** (se identificaron 100 interacciones; se destacan las principales):
  - **Mayores:** morfina y morfina liposomal (riesgo de depresión del sistema nervioso central y respiratoria).
  - **Moderadas:** pioglitazona, rosiglitazona, troglitazona, difenoxina, difenoxilato, dronabinol, nabilona, metoclopramida, opio y sibutramina.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje de TxGNN es muy alto (0.9971), no existen ensayos clínicos ni estudios que evalúen la pregabalina en tendinitis; la literatura disponible es indirecta (analgesia posquirúrgica y reportes de casos) y el vínculo mecanístico es débil. La evidencia se sitúa en L4.

**Para avanzar se necesita:**
- Estudios clínicos o series de casos que evalúen directamente la pregabalina en tendinitis (dolor, función y recuperación).
- Datos detallados del mecanismo de acción y su relevancia para el dolor tendinoso.
- Advertencias y contraindicaciones oficiales del prospecto de la AEMPS.
- Plan de monitoreo de seguridad, en especial para las interacciones con opioides y para pacientes con insuficiencia renal o enfermedad muscular.

---

### Otras indicaciones predichas (referencia)

| Indicación | Puntaje TxGNN | Nivel de Evidencia | Recomendación |
|------|------|------|------|
| Trastorno de migraña | 0.9947 | L2 | Pregunta de investigación (evidencia limitada, sobre todo pediátrica; el ensayo de fase 3 NCT00447369 fue retirado) |
| Migraña con aura de tronco encefálico | 0.9943 | L5 | Hold (evidencia preclínica) |
| Miositis de cuerpos de inclusión | 0.9952 | L5 | Hold |
| Miositis fibrosa | 0.9971 | L5 | Hold |
| Miositis granulomatosa idiopática | 0.9971 | L5 | Hold |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


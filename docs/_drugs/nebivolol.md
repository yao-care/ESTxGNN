---
layout: default
title: Nebivolol
parent: Solo predicción del modelo (L5)
nav_order: 555
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-31
monitor_inn: "NEBIVOLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
description: "Nebivolol: nueva indicación predicha, Malignant hypertensive renal disease (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Nebivolol
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

## Nebivolol: Malignant hypertensive renal disease
{: .text-alpha }

## Resumen en Una Frase

Nebivolol es un betabloqueante cardioselectivo (beta-1) con efecto vasodilatador mediado por óxido nítrico, utilizado originalmente para el tratamiento de la hipertensión arterial.
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta indicación específica; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Malignant hypertensive renal disease |
| Puntaje de Predicción TxGNN | 0.9942 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 17) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, nebivolol es un betabloqueante altamente selectivo para el receptor beta-1, con un componente adicional de vasodilatación dependiente de óxido nítrico endotelial (asociado a la activación de beta-3). Su eficacia en hipertensión está establecida y el fármaco está ampliamente comercializado en España.

La hipertensión renovascular está impulsada por la activación del sistema renina-angiotensina. El bloqueo beta-1 reduce la liberación de renina, lo que ofrece un vínculo mecanístico plausible con la nueva indicación. Además, existen señales preclínicas de protección renal con nebivolol en modelos animales.

Conviene ser prudentes: se trata de una forma grave y maligna, en la que el tratamiento definitivo (revascularización, bloqueo del sistema renina-angiotensina) tiene prioridad, por lo que nebivolol sería, como mucho, un tratamiento complementario. La segunda predicción (enfermedad renal hipertensiva maligna) se solapa en gran medida con la indicación ya existente y no representa una oportunidad de reposicionamiento claramente distinta.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal.

A modo de contexto, para otra predicción del mismo fármaco (hipertensión pulmonar por enfermedad pulmonar o hipoxia, puntaje 0,9939) se recuperaron publicaciones, pero casi todas son preclínicas o ajenas al tema, y ninguna demuestra eficacia en hipertensión pulmonar. Las más relevantes de forma indirecta:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19789971](https://pubmed.ncbi.nlm.nih.gov/19789971/) | 2009 | Revisión | Cardiovasc Drugs Ther | Efectos respiratorios de los betabloqueantes en insuficiencia cardíaca; se cuestiona la idea de que estén contraindicados con función pulmonar alterada |
| [23506636](https://pubmed.ncbi.nlm.nih.gov/23506636/) | 2013 | Estudio clínico comparativo | Int J Cardiol | Comparación multiparamétrica de carvedilol, nebivolol y bisoprolol en insuficiencia cardíaca moderada (evidencia indirecta) |
| [21045724](https://pubmed.ncbi.nlm.nih.gov/21045724/) | 2011 | Estudio clínico | J Hypertens | Efecto de betabloqueantes selectivos y no selectivos sobre la presión arterial ambulatoria en hipoxia hipobárica de altitud |
| [21883997](https://pubmed.ncbi.nlm.nih.gov/21883997/) | 2012 | ECA | Cardiovasc Ther | Nebivolol frente a carvedilol sobre el rendimiento físico en altitud en sujetos sanos |
| [32128711](https://pubmed.ncbi.nlm.nih.gov/32128711/) | 2020 | Preclínico (animal) | Pharmacol Rep | Efecto protector renal de nebivolol en lesión renal aguda en ratas, vía SGLT2 y ERK-HIF1α |
| [36947849](https://pubmed.ncbi.nlm.nih.gov/36947849/) | 2023 | Preclínico (animal) | Can J Physiol Pharmacol | Nebivolol protege frente a la nefrotoxicidad por metotrexato en ratas (vía AKT1/Hif-1α/eNOS) |
| [34693844](https://pubmed.ncbi.nlm.nih.gov/34693844/) | 2022 | Preclínico (animal) | Drug Chem Toxicol | Nebivolol atenúa el daño hepático por metotrexato |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 73926 | Nebivolol Cinfa 5 mg comprimidos EFG | Comprimido | No disponible en los datos compilados |
| 71271 | Nebivolol Pensa 5 mg comprimidos EFG | Comprimido | No disponible en los datos compilados |
| 4040 | Lobivon 5 mg comprimidos | Comprimido | No disponible en los datos compilados |
| 83604 | Insucor 10 mg comprimidos | Comprimido | No disponible en los datos compilados |
| 70928 | Nebivolol Normon 5 mg comprimidos EFG | Comprimido | No disponible en los datos compilados |

Se registran 20 autorizaciones vigentes (todas de principio activo único, ninguna cancelada).

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del texto del prospecto): insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar, diabetes mellitus, cetoacidosis diabética, enfermedad vascular periférica, claudicación intermitente, enfermedad arterial periférica, hipoglucemia, bloqueo auriculoventricular, enfermedad bronquial, síndrome del seno enfermo (incluida la forma familiar).
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las listadas, la mayoría son de gravedad moderada: epinefrina, hidrocortisona, hiosciamina, bupropión, triamcinolona, morfina, atropina, dexametasona, lorcaserina, betametasona, budesonida, glicopirronio, canagliflozina, clorpropamida, dapagliflozina y diciclomina, entre otras. Son de gravedad leve el ácido acetilsalicílico y el óxido de magnesio.
- Consideración específica: en hipertensión pulmonar, los betabloqueantes se usan con cautela por el riesgo para la función ventricular derecha y la seguridad respiratoria.

Consultar el prospecto para las advertencias oficiales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción (nivel L5) se basa solo en el modelo, sin ensayos clínicos ni literatura para hipertensión renovascular maligna. Al ser una forma grave en la que priman la revascularización y el bloqueo del sistema renina-angiotensina, nebivolol tendría un papel como mucho complementario.

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre betabloqueantes en hipertensión renovascular
- Datos detallados del mecanismo de acción (MOA)
- Obtención y análisis del prospecto de la AEMPS (advertencias y contraindicaciones oficiales), ya que actualmente impide avanzar en el cribado de seguridad
- Evaluación del riesgo en poblaciones con las contraindicaciones señaladas (enfermedad vascular periférica, bloqueo AV, enfermedad bronquial, diabetes)
- Estudios preclínicos o piloto específicos en hipertensión renovascular
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


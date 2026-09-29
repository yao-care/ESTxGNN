---
layout: default
title: Ezetimibe
parent: Evidencia alta (L1-L2)
nav_order: 224
evidence_level: L1
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **4** 
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

# Ezetimiba: De Reductor del Colesterol a Hiperlipoproteinemia

## Resumen en Una Frase

Ezetimiba es un inhibidor de la absorción intestinal de colesterol que se utiliza para reducir los niveles de colesterol.
El modelo TxGNN predice que podría ser efectivo para **hiperlipoproteinemia**,
con **50 ensayos clínicos** y **19 publicaciones** que respaldan esta dirección.
Esta predicción coincide con el uso ya establecido del fármaco, por lo que es una confirmación más que un reposicionamiento en sentido estricto.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Hiperlipoproteinemia |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

El registro no incluye una descripción detallada del mecanismo de acción, pero los datos de farmacología identifican como diana a NPC1L1 (*NPC1 like intracellular cholesterol transporter 1*). Ezetimiba bloquea esta proteína, que media la absorción intestinal del colesterol de la dieta y de la bilis. Al reducir la entrada de colesterol, disminuye el colesterol LDL (LDL-C).

Este mecanismo es coherente con la hiperlipoproteinemia, definida por niveles elevados de lípidos y lipoproteínas en sangre. El puntaje muy alto de TxGNN (0.996) concuerda con los ensayos de Fase 3 disponibles, en los que ezetimiba se usa sola o combinada con estatinas, fenofibrato u otros hipolipemiantes.

Los ensayos incluyen combinaciones con simvastatina, atorvastatina y fenofibrato, además de ensayos posteriores a la comercialización. Como esta indicación ya corresponde al uso habitual del fármaco, la predicción sirve sobre todo como validación del modelo. No aporta una nueva vía terapéutica.

---

## Evidencia de Ensayos Clínicos

Se identificaron 50 ensayos; se muestran los 10 más relevantes (los de mayor evaluación de relevancia y los de intervención directa con ezetimiba).

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Fase 3 | Completado | 720 | Ezetimiba + simvastatina en dosis alta vs simvastatina sola sobre la progresión de la aterosclerosis carotídea (ENHANCE), en hipercolesterolemia familiar heterocigota |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Fase 3 | Completado | 1220 | Ezetimiba/simvastatina y niacina de liberación prolongada coadministradas en hiperlipidemia tipo IIa/IIb, doble ciego |
| [NCT01763827](https://clinicaltrials.gov/study/NCT01763827) | Fase 3 | Completado | 615 | Evolocumab vs placebo y ezetimiba (comparador activo) en pacientes con riesgo de Framingham ≤10% |
| [NCT00704535](https://clinicaltrials.gov/study/NCT00704535) | N/A | Completado | 4105 | Vigilancia posterior a la comercialización de seguridad y eficacia de ezetimiba en pacientes filipinos |
| [NCT07255820](https://clinicaltrials.gov/study/NCT07255820) | Fase 4 | Completado | 126 | Terapia dual vs triple (rosuvastatina/ezetimiba/ácido bempedoico) en diabetes tipo 2 con LDL-C elevado, abierto |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Fase 3 | Completado | 576 | Coadministración de fenofibrato y ezetimiba en hiperlipidemia mixta |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Fase 3 | Completado | 587 | Coadministración de fenofibrato y ezetimiba en hiperlipidemia mixta (segundo estudio) |
| [NCT02451098](https://clinicaltrials.gov/study/NCT02451098) | Fase 3 | Completado | 385 | Atorvastatina + ezetimiba vs atorvastatina sola en hipercolesterolemia primaria, diseño factorial |
| [NCT00349284](https://clinicaltrials.gov/study/NCT00349284) | Fase 3 | Completado | 181 | Fenofibrato 145 mg, ezetimiba 10 mg y su combinación en dislipidemia tipo IIb con rasgos de síndrome metabólico |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Fase 3 | Completado | 50 | Ezetimiba 10 mg añadida a atorvastatina o simvastatina en hipercolesterolemia familiar homocigota |

En NCT01763827 ezetimiba actúa como comparador activo y no como intervención principal. Por eso solo respalda de forma indirecta su efecto establecido.

---

## Evidencia de Literatura

Se identificaron 19 publicaciones; se muestran las 10 más relevantes.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | ECA | Lancet | TANDEM: ensayo de Fase 3 con combinación fija de obicetrapib y ezetimiba para reducir el LDL-C, controlado con placebo |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | ECA | JAMA | Enlicitide (inhibidor oral de PCSK9) en hipercolesterolemia familiar heterocigota; ezetimiba no es la intervención principal |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Revisión | Molecular Medicine Reports | Avances en los fármacos actuales dirigidos a la hiperlipidemia, cuyo objetivo es prevenir la enfermedad cardiovascular aterosclerótica |
| [30702994](https://pubmed.ncbi.nlm.nih.gov/30702994/) | 2019 | Revisión | Circulation Research | Agentes reductores del colesterol y su eficacia y seguridad, con base genética en PCSK9 |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Revisión | J Am Coll Cardiol | Terapias nuevas y emergentes para reducir LDL-C y apoB, sobre la base de estatinas, ezetimiba e inhibidores de PCSK9 |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | Revisión | Drug and Therapeutics Bulletin | Actualización sobre ezetimiba, que reduce LDL-C y colesterol total sola o con estatina |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Revisión | J Cardiovasc Pharmacol Ther | Revisión de inhibidores de PCSK9 en pacientes intolerantes a estatinas o que no alcanzan objetivos |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Revisión | Cardiology Clinics | Hipercolesterolemia familiar: tratamientos que reducen el LDL-C, entre ellos estatinas y ezetimiba |
| [35101175](https://pubmed.ncbi.nlm.nih.gov/35101175/) | 2022 | Cohorte retrospectiva | Lancet | Experiencia mundial en hipercolesterolemia familiar homocigota y resultados de la práctica actual |
| [18376001](https://pubmed.ncbi.nlm.nih.gov/18376001/) | 2008 | Sin clasificar | N Engl J Med | Texto sobre reducción del colesterol y ezetimiba (sin resumen disponible) |

---

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones. El registro no incluye el texto de indicación aprobada de estas autorizaciones.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 79108 | EZETIMIBA VIATRIS 10 MG COMPRIMIDOS EFG | Comprimido |
| 31-267-03-C | EZETROL 10 mg COMPRIMIDOS | Comprimido |
| 82226 | EZETIMIBA TEVA-RATIOPHARM 10 MG COMPRIMIDOS EFG | Comprimido |
| 82832 | EZETIMIBA ALMUS 10 MG COMPRIMIDOS EFG | Comprimido |
| 81631 | EZETIMIBA ALTER 10 MG COMPRIMIDOS EFG | Comprimido |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ensayos de Fase 3 completados y aleatorizados con ezetimiba (ENHANCE, ezetimiba/simvastatina + niacina, combinaciones con fenofibrato y atorvastatina), lo que da un nivel de evidencia L1. La cautela se debe a dos razones. La indicación ya está cubierta por el uso comercializado, y faltan datos de seguridad de la ficha técnica de la AEMPS.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de la AEMPS para completar advertencias y contraindicaciones (pendiente bloqueante para el cribado de seguridad).
- Corregir en el registro fuente la indicación original y el mecanismo de acción de ezetimiba, que están vacíos.
- Confirmar el texto de indicación aprobada en las autorizaciones españolas.
- Para las otras predicciones del modelo:
  - Hipercolesterolemia familiar (rango 2) tiene evidencia L1, más sólida en la forma heterocigota. En la forma homocigota, la respuesta a ezetimiba es limitada porque no depende del receptor de LDL.
  - Deficiencia de colesterol 7α-hidroxilasa (L4) y deficiencia de la proteína de transferencia de ésteres de colesterilo (L5) quedan en *Hold*. No hay ensayos clínicos ni un vínculo mecanístico claro.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


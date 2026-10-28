---
layout: default
title: Misoprostol
parent: Solo predicción del modelo (L5)
nav_order: 534
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Misoprostol: nueva indicación predicha, Amenorrea (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "MISOPROSTOL"
predicted_indications: ["amenorrhea (disease)", "atypical coarctation of aorta"]
---

# Misoprostol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Misoprostol: De Indicación Original No Especificada a Amenorrea
{: .text-alpha }

## Resumen en Una Frase

Misoprostol es un análogo de la prostaglandina E1 comercializado en España con cinco autorizaciones vigentes. Los datos compilados para este informe no incluyen el texto de su indicación original.
El modelo TxGNN predice que podría ser efectivo para **amenorrea**, pero no hay ensayos clínicos registrados y solo **7 publicaciones** de relación indirecta (aborto médico, aborto retenido, sangrado uterino anormal). La evidencia es esencialmente solo predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 0,9964 |
| Nivel de Evidencia | L5 (según la clasificación de los datos compilados; estrictamente, la evidencia directa corresponde a L5) |
| Estado de Mercado en España | Comercializado (registros vigentes: 5 de 5) |
| Número de Autorizaciones | 5 (vigentes: 5) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, misoprostol es un análogo de la prostaglandina E1 que induce contracciones uterinas y maduración cervical, y se utiliza para inducir la menstruación o evacuar el útero.

El vínculo con la amenorrea es plausible solo en contextos en los que se busca inducir sangrado, como el fallo precoz del embarazo o la amenorrea relacionada con el embarazo. Misoprostol **no** trata las causas subyacentes de la amenorrea (hipotalámicas, hipofisarias, ováricas o anatómicas).

El puntaje tan alto de TxGNN (0,9964) es una predicción computacional sin respaldo clínico directo. La literatura recuperada trata del aborto médico, el aborto retenido y el sangrado uterino anormal. Por ello la asociación es indirecta y probablemente refleja la amenorrea del embarazo más que una verdadera indicación terapéutica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | ECA | Reprod Sci | 744 mujeres con embarazo ultra temprano (amenorrea ≤35 días): mifepristona a dosis baja más misoprostol autoadministrado para aborto médico; evalúa eficacia, seguridad y aceptabilidad |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | ECA (dosis-respuesta) | Reprod Sci | 2500 mujeres con embarazo ultra temprano; dosis decrecientes de mifepristona (150 a 50 mg) seguidas de 200 µg de misoprostol oral; variable principal: aborto completo sin cirugía |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Cohorte | J Obstet Gynaecol Res | Seguridad y eficacia de mifepristona a dosis baja con misoprostol autoadministrado para la interrupción del embarazo temprano |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Cohorte | Hum Reprod | Prevención de embarazo no deseado con mifepristona a dosis baja y misoprostol antes de la menstruación esperada |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Revisión | J Obstet Gynaecol Can | Ablación endometrial en el manejo del sangrado uterino anormal |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Revisión | BMJ | Manejo médico del aborto retenido y del embarazo anembrionario |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Reporte de caso/revisión | Cureus | Hígado graso agudo del embarazo con amenorrea como síntoma; relación solo tangencial con misoprostol |

*Nota: la clasificación del tipo de estudio proviene de los datos compilados; los estudios de mifepristona más misoprostol se describen como ECA según sus títulos. Todos los trabajos se refieren a amenorrea gestacional, no a tratamiento de la amenorrea patológica.*

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 69683 | MISOFAR 200 microgramos comprimidos vaginales | Comprimido vaginal | No disponible en los datos compilados |
| 85394 | ANGUSTA 25 microgramos comprimidos | Comprimido | No disponible en los datos compilados |
| 58403 | CYTOTEC 200 microgramos comprimidos | Comprimido | No disponible en los datos compilados |
| 77146 | MISOONE 400 microgramos comprimidos | Comprimido | No disponible en los datos compilados |
| 69682 | MISOFAR 25 microgramos comprimidos vaginales | Comprimido vaginal | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no texto del prospecto)**: el grafo de conocimiento TxGNN (PrimeKG) asocia misoprostol con contraindicación en: hipertensión, enfermedad hepática e insuficiencia hepática, lesión hepática inducida por fármacos, enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, enfermedad cardiovascular y cardíaca, infarto de miocardio y trombosis coronaria, ictus y enfermedad cerebrovascular, infarto cerebral, enfermedad inflamatoria intestinal, asma (incluidas formas intrínseca y alérgica), úlcera péptica activa, trastornos de la coagulación, hemoglobinopatías, anemia (incluida la macrocítica), abuso o dependencia de sustancias y meningitis no infecciosa. Deben verificarse con el prospecto oficial.
- **Interacciones farmacológicas** (100 interacciones detectadas; principales):
  - **Mayor**: dinoprostona (tópica).
  - **Moderada**: óxido de magnesio, hidróxido de magnesio, carbonato de magnesio, magaldrato y quinapril.
  - **Leve**: citrato de sodio, hidróxido de aluminio, carbonato de calcio, bicarbonato de sodio y naproxeno.
  - Otras (goserelina, ciclosporina, valsartán, ramipril, lorazepam, entre otras) tienen nivel no clasificado.

No se dispone del texto de advertencias y contraindicaciones del prospecto de la AEMPS; debe consultarse para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje computacional; no hay ensayos clínicos y la literatura trata de la amenorrea del embarazo, no de una indicación terapéutica real. El mecanismo no respalda el tratamiento de las causas de la amenorrea y el perfil de contraindicaciones del grafo es amplio.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), que es un requisito bloqueante.
- Completar los datos del mecanismo de acción.
- Definir qué tipo de amenorrea se pretende tratar y aclarar si la predicción refleja solo la amenorrea gestacional.
- Realizar una revisión de la literatura dirigida y, si procede, estudios clínicos específicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


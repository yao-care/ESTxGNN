---
layout: default
title: Misoprostol
parent: Solo predicción del modelo (L5)
nav_order: 359
evidence_level: L5
indication_count: 2
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Misoprostol: De Indicación Original no Registrada a Amenorrea

## Resumen en Una Frase

Los datos recibidos no incluyen la indicación original de misoprostol ni su mecanismo de acción, y en España hay 5 autorizaciones comercializadas.
El modelo TxGNN predice que podría ser efectivo para **amenorrea** (puntaje 99.64%), pero no hay **ningún ensayo clínico** registrado y las **7 publicaciones** recuperadas no evalúan misoprostol como tratamiento de la amenorrea.
Se trata de una predicción sin respaldo experimental directo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99.64% |
| Nivel de Evidencia | L5 (el paquete de evidencia asigna L4, pero ningún estudio evalúa esta indicación) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Misoprostol es un análogo sintético de la prostaglandina E1 (agonista de receptores EP) que provoca contracción uterina y maduración cervical. Ese perfil explica por qué la mayoría de la literatura recuperada lo estudia en el aborto médico, el aborto diferido y el sangrado uterino anormal.

**No se identifica un vínculo mecanístico directo con el tratamiento de la amenorrea.** Los artículos usan misoprostol junto con mifepristona para interrumpir embarazos. En ellos la amenorrea aparece solo como criterio de inclusión, es decir, como signo de embarazo temprano ("amenorrea ≤35 días"), no como enfermedad a tratar.

La hipótesis más probable es que el puntaje alto (0.996) refleje la cercanía en el grafo de conocimiento entre la amenorrea y los nodos de embarazo y aborto. Sería, por tanto, un artefacto del grafo y no una señal terapéutica real. Al no haber indicación original ni mecanismo registrados, la predicción no puede contrastarse con la farmacología conocida.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Ninguna de estas publicaciones evalúa misoprostol para tratar la amenorrea.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | ECA | Reproductive Sciences | 744 mujeres con embarazo ultra temprano (amenorrea ≤35 días). Mifepristona en dosis baja con misoprostol autoadministrado para aborto médico: eficacia, seguridad y aceptabilidad. |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | ECA (dosis-respuesta) | Reproductive Sciences | 2500 mujeres con embarazo ultra temprano. Cinco dosis decrecientes de mifepristona (150 a 50 mg) seguidas de 200 µg de misoprostol oral; variable principal: aborto completo sin cirugía. |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Estudio clínico | Human Reproduction | Prevención de embarazo no deseado con mifepristona en dosis baja más misoprostol antes de la menstruación esperada. |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Estudio clínico | J Obstet Gynaecol Res | Seguridad y eficacia de mifepristona en dosis baja con misoprostol autoadministrado para terminar embarazos tempranos. |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Revisión | J Obstet Gynaecol Can | Ablación endometrial en el manejo del sangrado uterino anormal. No evalúa misoprostol como tratamiento. |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Revisión / reporte de caso | Cureus | Hígado graso agudo del embarazo. La amenorrea aparece solo como síntoma de presentación en una gestante. |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Revisión | BMJ | Manejo médico del aborto diferido y del embarazo anembrionario. No hay resumen disponible. |

## Información de Mercado en España

Los textos de indicación aprobada figuran vacíos en los datos, por lo que no se incluye esa columna.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 69683 | MISOFAR 200 microgramos comprimidos vaginales | Comprimido vaginal | Laboratorios Bial S.A. |
| 69682 | MISOFAR 25 microgramos comprimidos vaginales | Comprimido vaginal | Laboratorios Bial S.A. |
| 85394 | ANGUSTA 25 microgramos comprimidos | Comprimido | Norgine B.V. |
| 58403 | CYTOTEC 200 microgramos comprimidos | Comprimido | Pfizer S.L. |
| 77146 | MISOONE 400 microgramos comprimidos | Comprimido | Exelgyn |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se obtuvieron advertencias, contraindicaciones ni interacciones farmacológicas desde AEMPS y DrugBank.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la literatura recuperada trata del aborto médico, no de la amenorrea. El puntaje alto de TxGNN probablemente refleja la cercanía entre "amenorrea" y "embarazo/aborto" en el grafo. Además, faltan la indicación original, el mecanismo y los datos de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), un vacío bloqueante para el cribado de seguridad.
- Obtener el mecanismo de acción desde DrugBank para analizar el vínculo mecanístico.
- Completar las indicaciones aprobadas de cada autorización.
- Hacer una búsqueda bibliográfica dirigida que evalúe misoprostol específicamente en amenorrea, distinguiendo el uso de la amenorrea como síntoma de embarazo del uso como enfermedad a tratar.
- Valorar el riesgo teratogénico asociado a la exposición prenatal a misoprostol al considerar cualquier población de mujeres en edad fértil.

**Nota sobre la segunda predicción (coartación atípica de la aorta, puntaje 99.30%):** no tiene ensayos ni literatura, por lo que su nivel de evidencia es L5 y su decisión es Hold. Su único vínculo concebible es que misoprostol sea análogo de PGE1, como el alprostadilo, que se usa para mantener abierto el conducto arterioso. Misoprostol no está validado para ese uso, y la exposición prenatal se ha asociado con malformaciones congénitas, lo que desaconseja este reposicionamiento.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


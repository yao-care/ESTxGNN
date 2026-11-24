---
layout: default
title: Zolpidem
parent: Solo predicción del modelo (L5)
nav_order: 868
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "ZOLPIDEM"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia"]
description: "Zolpidem: nueva indicación predicha, Benign paroxysmal torticollis of infancy (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Zolpidem
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

## Zolpidem: Benign paroxysmal torticollis of infancy
{: .text-alpha }

## Resumen en Una Frase

Zolpidem es un hipnótico no benzodiazepínico, originalmente utilizado para el tratamiento del insomnio.
El modelo TxGNN predice que podría ser efectivo para **trastorno del sueño con dificultad para iniciar y mantener el sueño**,
con **0 ensayos clínicos** y **19 publicaciones** que actualmente respaldan esta dirección. Cabe señalar que esta indicación es prácticamente equivalente a la ya autorizada, por lo que no constituye un reposicionamiento real, sino una confirmación del uso aprobado.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Benign paroxysmal torticollis of infancy |
| Puntaje de Predicción TxGNN | 0.9926 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 12; autorizadas no comercializadas: 1; revocadas o suspendidas: 7) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Zolpidem (traducción no oficial): «El zolpidem es un modulador positivo del receptor GABA A que, según se presume, ejerce sus efectos terapéuticos en el tratamiento a corto plazo del insomnio mediante su unión al sitio de las benzodiazepinas de los receptores GABA A que contienen la subunidad α1, lo que aumenta la frecuencia de apertura del canal de cloruro y da lugar a la inhibición de la excitación neuronal.» Texto original en inglés: "Zolpidem is a GABA A receptor positive modulator presumed to exert its therapeutic effects in the short-term treatment of insomnia through binding to the benzodiazepine site of α1 subunit containing GABA A receptors, increasing the frequency of chloride channel opening resulting in the inhibition of neuronal excitation." ([DailyMed: Ambien (zolpidem tartrate) prescribing information, Cosette Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=747949c5-2c91-4909-8a07-71b6826f8e97), versión del 2025-02-07; consultado el 2026-11-19). Según la información conocida, zolpidem es un modulador alostérico positivo del receptor GABA-A con unión preferente a la subunidad alfa-1, lo que produce efectos sedantes e hipnóticos.

La nueva indicación predicha (dificultad para iniciar y mantener el sueño) describe esencialmente el mismo cuadro clínico que el insomnio, la indicación original. Por ello, el mecanismo es directamente aplicable y la puntuación alta del modelo es coherente con ello. No se trata de un reposicionamiento en sentido estricto.

Las guías y revisiones recopiladas (por ejemplo, la guía de la Academia Americana de Medicina del Sueño y un metaanálisis en red publicado en *Lancet*) incluyen a zolpidem entre las opciones farmacológicas para el insomnio, aunque recomiendan la terapia cognitivo-conductual como primera línea y prudencia en personas mayores.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Se muestran las 10 publicaciones más relevantes, priorizando ECA, metaanálisis y guías sobre revisiones narrativas (de un total de 19 disponibles).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | ECA (Fase 3) | JAMA Network Open | Lemborexant frente a placebo y zolpidem de liberación prolongada en adultos mayores con insomnio |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Metaanálisis en red | Lancet | Eficacia comparada de intervenciones farmacológicas para el insomnio agudo y a largo plazo |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Metaanálisis en red | J Manag Care Spec Pharm | Comparación de lemborexant con otros tratamientos del insomnio, incluido zolpidem |
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Guía clínica | J Clin Sleep Med | Recomendaciones de la AASM para el tratamiento farmacológico del insomnio crónico en adultos |
| [39923608](https://pubmed.ncbi.nlm.nih.gov/39923608/) | 2025 | Guía de consenso | Sleep Medicine | Guía europea para cambiar o retirar hipnóticos en el insomnio crónico |
| [37549414](https://pubmed.ncbi.nlm.nih.gov/37549414/) | 2023 | Revisión | J Fam Pract | Actualización sobre el manejo del insomnio en atención primaria |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Revisión | Drugs & Aging | Recomendaciones de manejo farmacológico del insomnio en ancianos |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Revisión | Clin Ther | Seguridad y eficacia de los hipnóticos en adultos mayores |
| [29487083](https://pubmed.ncbi.nlm.nih.gov/29487083/) | 2018 | Revisión | Pharmacol Rev | Fármacos para el insomnio más allá de las benzodiazepinas; efectos adversos de los fármacos Z (tolerancia, dependencia, caídas) |
| [22424586](https://pubmed.ncbi.nlm.nih.gov/22424586/) | 2012 | Revisión | Expert Opin Pharmacother | Zolpidem como agonista del receptor de benzodiazepinas, hipnótico más prescrito en EE. UU. |

## Información de Mercado en España

El texto de indicación aprobada no está disponible en los datos compilados.

<!-- review:begin es-lic-20261105-zolpidem-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Se muestran 5 de las 20 autorizaciones vigentes. El texto de indicación aprobada no está disponible en los datos compilados." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-zolpidem-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 64523 | ZOLPIDEM SANDOZ 10 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Sandoz Farmaceutica S.A. | Comercializada |
| 63794 | ZOLPIDEM STADA 10 mg COMPRIMIDOS RECUBIERTOS EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorio Stada S.L. | Comercializada |
| 83190 | DAGAN 5 MG COMPRIMIDOS BUCODISPERSABLES EFG | COMPRIMIDO BUCODISPERSABLE | Meiji Pharma Spain S.A. | Comercializada |
| 65204 | ZOLPIDEM DESGEN 5 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorio Generfarma S.L. | Comercializada |
| 64811 | ZOLPIDEM VIATRIS 10 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO | Viatris Pharmaceuticals S.L. | Comercializada |
| 83381 | ZOLPIDEM AUROVITAS 10 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Aurovitas Spain, S.A.U. | Comercializada |
| 75798 | ZOLPIDEM TEVA-RATIOPHARM 10 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Teva Pharma S.L.U. | Comercializada |
| 58470 | STILNOX 10 mg COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Sanofi Aventis S.A. | Comercializada |
| 59264 | DALPARAN 10 mg COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Sanofi Aventis S.A. | Comercializada |
| 64551 | ZOLPIDEM NORMON 10 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorios Normon S.A. | Comercializada |

Se muestran 10 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (no proceden del prospecto): trastorno de ansiedad, trastorno neurótico, trastorno distímico, enfermedad hepática, enfermedad de la vesícula biliar, síndrome de apnea obstructiva del sueño, síndrome de apnea del sueño, síndrome de hipoventilación central congénita, síndrome de Haddad, trastorno amnésico, amnesia retrógrada, trastorno por uso de sustancias, abuso/dependencia de sustancias, trastorno por déficit de atención con hiperactividad (incluido el tipo inatento).
- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total (se muestran las 20 principales de la consulta).
  - **Mayores**: morfina y morfina liposomal (riesgo de depresión respiratoria y del sistema nervioso central).
  - **Moderadas**: bupropión, aprepitant, dexametasona, cimetidina, claritromicina, dronabinol, nabilona, metoclopramida, miconazol, clotrimazol, fenilbutirato de glicerol, opio, sibutramina y troglitazona.
  - **Nivel desconocido**: calcitriol, vitamina A, fentermina y pantoprazol.
- Las medidas de control recomendadas incluyen vigilar conductas complejas durante el sueño (advertencia destacada), deterioro al día siguiente, riesgo de dependencia y mayor precaución en personas mayores.

Las advertencias y contraindicaciones del prospecto de la AEMPS no estaban disponibles en los datos compilados; consultar el prospecto para información de seguridad completa.

## Otras Indicaciones Predichas (Referencia)

| Indicación | Puntaje TxGNN | Nivel de Evidencia | Decisión | Comentario |
|------|------|------|------|------|
| Agorafobia | 0.9925 | L5 | Hold | Fundamento débil e indirecto; zolpidem (subunidad alfa-1) se asocia a sedación y no a ansiólisis; existen terapias de primera línea bien establecidas; riesgo de dependencia |

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La indicación predicha coincide con el uso ya aprobado (insomnio) y está respaldada por guías, metaanálisis en red y un ECA de Fase 3 que incluye a zolpidem como comparador. La evidencia es suficiente para confirmar el uso, siempre con medidas de control por los riesgos conocidos de los hipnóticos.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), ya que es un dato bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Definir medidas de control: conductas complejas del sueño, deterioro al día siguiente, riesgo de dependencia y precaución en personas mayores.
- Revisar las interacciones mayores (especialmente con opioides como la morfina) y las contraindicaciones sugeridas por el grafo (apnea del sueño, enfermedad hepática, antecedentes de abuso de sustancias).
- Mantener las indicaciones de rango 2 y 3 (tortícolis paroxística benigna y agorafobia) en espera (Hold), sin evidencia que las respalde.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Se muestran 5 de las 20 autorizaciones vigentes" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Ambien (zolpidem tartrate) prescribing information, Cosette Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=747949c5-2c91-4909-8a07-71b6826f8e97) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


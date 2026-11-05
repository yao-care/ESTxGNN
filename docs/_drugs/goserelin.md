---
layout: default
title: Goserelin
parent: Solo predicción del modelo (L5)
nav_order: 384
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-05
monitor_inn: "goserelin"
predicted_indications: ["amenorrhea (disease)", "renal hypoplasia (disease)", "renal hypoplasia, bilateral"]
description: "Goserelin: nueva indicación predicha, Amenorrea (amenorrhea (disease)) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Goserelin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Goserelin: Amenorrea (amenorrhea (disease))
{: .text-alpha }

## Resumen en Una Frase

Goserelina es un agonista de la hormona liberadora de gonadotropinas (GnRH) que se comercializa en España como implante en jeringa precargada.
El modelo TxGNN predice **Amenorrea (amenorrhea (disease))** como nueva indicación, aunque la amenorrea es aquí un efecto de la supresión ovárica que produce el propio fármaco y no una enfermedad que este trate.
Hay **1 ensayo clínico** y **16 publicaciones** relacionadas, pero ninguno estudia goserelina como tratamiento de la amenorrea, por lo que el nivel de evidencia es **L5**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Amenorrea (amenorrhea (disease)) |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 3; revocadas o suspendidas: 1) |
| Número de Autorizaciones | 3 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen el mecanismo de acción registrado en DrugBank. Goserelina es, sin embargo, un agonista de GnRH bien caracterizado. La administración continua desensibiliza los receptores de GnRH de la hipófisis, reduce la secreción de LH y FSH y disminuye la producción ovárica de estradiol. El resultado es una amenorrea reversible, conocida como supresión ovárica médica.

Este vínculo explica la señal del modelo, pero tiene una limitación importante. La amenorrea es un efecto terapéutico o una medida de resultado, no una enfermedad que goserelina corrija. Usarla como tratamiento de la amenorrea sería contradictorio mecanísticamente, porque el fármaco la provoca.

La mayor parte de la evidencia procede de oncología. Allí la amenorrea aparece como subproducto de la ablación ovárica en cáncer de mama premenopáusico, o como indicador de la función ovárica tras la quimioterapia. Si se quisiera explorar este camino, habría que replantearlo como inducción deliberada de amenorrea (supresión menstrual) o como protección de la función ovárica durante la quimioterapia.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02132390](https://clinicaltrials.gov/study/NCT02132390) | Fase 3 | Desconocido | 300 | Toremifeno adyuvante con o sin goserelina en mujeres premenopáusicas con cáncer de mama con receptores hormonales positivos, con o sin amenorrea inducida por quimioterapia. La amenorrea no es el objetivo principal, por lo que la relevancia es indirecta. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [17159194](https://pubmed.ncbi.nlm.nih.gov/17159194/) | 2007 | ECA (análisis secundario) | J Clin Oncol | Compara el impacto en amenorrea, sofocos y calidad de vida de quimioterapia, goserelina o ambas en cáncer de mama premenopáusico (IBCSG VIII). |
| [12488406](https://pubmed.ncbi.nlm.nih.gov/12488406/) | 2002 | ECA | J Clin Oncol | Goserelina frente a CMF adyuvante en cáncer de mama premenopáusico con ganglios positivos. |
| [14679153](https://pubmed.ncbi.nlm.nih.gov/14679153/) | 2003 | ECA | J Natl Cancer Inst | Quimioterapia seguida de goserelina frente a cada modalidad por separado en cáncer de mama sin afectación ganglionar. |
| [28472240](https://pubmed.ncbi.nlm.nih.gov/28472240/) | 2017 | Revisión/Metaanálisis | Ann Oncol | Ensayo OPTION: un agonista de GnRH durante la quimioterapia para reducir el riesgo de insuficiencia ovárica prematura. |
| [12353820](https://pubmed.ncbi.nlm.nih.gov/12353820/) | 2002 | Revisión/Metaanálisis | Breast Cancer Res Treat | Revisión de los agonistas de LHRH en cáncer de mama precoz y de la ablación ovárica reversible con goserelina. |
| [12734855](https://pubmed.ncbi.nlm.nih.gov/12734855/) | 2003 | Revisión | Br J Surg | Métodos de ablación ovárica en cáncer de mama premenopáusico y relevancia de la supresión ovárica. |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Revisión | J R Army Med Corps | Analiza la inducción terapéutica de amenorrea y cita a goserelina entre los métodos. |
| [25187267](https://pubmed.ncbi.nlm.nih.gov/25187267/) | 2015 | Cohorte | Cancer Res Treat | La ablación ovárica con goserelina mejora la supervivencia en cáncer de mama estadio II/III sin amenorrea inducida por quimioterapia. |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Observacional | J Clin Oncol | Discute si es necesario monitorizar el estradiol en mujeres con supresión ovárica por cáncer de mama. |
| [2522795](https://pubmed.ncbi.nlm.nih.gov/2522795/) | 1989 | Estudio clínico | Br J Obstet Gynaecol | En 12 mujeres con fallo ovárico prematuro, la supresión de gonadotropinas con goserelina no revirtió el fallo ovárico. |

## Información de Mercado en España

Hay 2 autorizaciones vigentes y 1 cancelada. El texto de indicación aprobada no figura en los datos locales.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| R-7832 | ZOLADEX JERINGA PRECARGADA | Implante | No disponible en los datos compilados |
| 61367 | ZOLADEX TRIMESTRAL 10,8 mg IMPLANTE EN JERINGA PRECARGADA | Implante | No disponible en los datos compilados |
| 58603 | ZOLADEX 3,6 mg IMPLANTE EN JERINGA PRECARGADA | Implante | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 371 interacciones. Una es de nivel mayor, con dolasetrón. El resto de las listadas son de nivel moderado:
  - antidiabéticos: acarbosa, metformina, glimepirida, clorpropamida, canagliflozina, dapagliflozina, empagliflozina, alogliptina, linagliptina, saxagliptina, albiglutida y dulaglutida;
  - laxantes: bisacodilo, ácido picosulfúrico y polietilenglicol con electrolitos;
  - otros: famotidina, loperamida, claritromicina y palonosetrón.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún estudio evalúa goserelina como tratamiento de la amenorrea. Los datos disponibles describen la amenorrea como efecto de la supresión ovárica en cáncer de mama, y el mecanismo es contradictorio con usarla como tratamiento. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Replantear la hipótesis, por ejemplo como supresión menstrual deliberada o protección de la función ovárica durante la quimioterapia, con su propia indicación y variables de resultado.
- Ensayos clínicos que estudien directamente esa indicación replanteada.
- Revisar el prospecto de AEMPS para completar advertencias y contraindicaciones.
- Datos de mecanismo de acción en DrugBank.
- Evaluar la seguridad de la supresión estrogénica prolongada, como el efecto sobre la densidad ósea y los síntomas menopáusicos.

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


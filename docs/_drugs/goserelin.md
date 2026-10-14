---
layout: default
title: Goserelin
parent: Solo predicción del modelo (L5)
nav_order: 384
evidence_level: L5
indication_count: 3
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Goserelina: De Endometriosis a Amenorrea

## Resumen en Una Frase

Goserelina es un agonista de la GnRH (hormona liberadora de gonadotropinas), utilizado originalmente para el tratamiento de la endometriosis.
El modelo TxGNN predice que podría ser efectivo para **Amenorrea**, con **1 ensayo clínico** y **16 publicaciones** relacionadas con esta dirección. Sin embargo, la amenorrea es en realidad un efecto terapéutico de la goserelina y no una enfermedad a tratar, por lo que la indicación debe replantearse.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Endometriosis (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99,99 % |
| Nivel de Evidencia | L1 (según la evaluación del conjunto de datos; con la salvedad de que la evidencia es indirecta, ver más abajo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Goserelina es un agonista de la GnRH. La administración continuada desensibiliza los receptores de GnRH de la hipófisis, lo que reduce la secreción de LH y FSH y la producción ovárica de estradiol. El resultado es una amenorrea reversible (supresión ovárica médica). Los datos compilados no incluyen una descripción detallada del mecanismo de acción, pero este efecto farmacodinámico está bien caracterizado y se utiliza terapéuticamente en el cáncer de mama premenopáusico y en la endometriosis.

La relación con la indicación original es directa: en la endometriosis, la supresión del estradiol reduce el crecimiento del tejido endometrial ectópico, y la amenorrea es parte del mecanismo terapéutico.

**Salvedad importante:** la amenorrea aquí es un efecto terapéutico o una medida de resultado, no una enfermedad objetivo independiente. Usar goserelina para "tratar" la amenorrea sería contradictorio mecanísticamente, porque el fármaco la provoca. La propuesta debería reformularse, por ejemplo como **inducción deliberada de amenorrea (supresión menstrual)** o **protección de la función ovárica durante la quimioterapia**. Gran parte de la evidencia procede de oncología, donde la amenorrea es un subproducto de la ablación ovárica o un indicador de la función ovárica tras la quimioterapia.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02132390](https://clinicaltrials.gov/study/NCT02132390) | Fase 3 | Desconocido | 300 | Toremifeno adyuvante con o sin goserelina en mujeres premenopáusicas con cáncer de mama con receptores hormonales positivos, con o sin amenorrea inducida por quimioterapia. Relevancia indirecta: la amenorrea no es el criterio principal de valoración. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12488406](https://pubmed.ncbi.nlm.nih.gov/12488406/) | 2002 | ECA | J Clin Oncol | Goserelina frente a CMF como tratamiento adyuvante en cáncer de mama premenopáusico con ganglios positivos (estudio ZEBRA) |
| [14679153](https://pubmed.ncbi.nlm.nih.gov/14679153/) | 2003 | ECA | J Natl Cancer Inst | Quimioterapia seguida de goserelina frente a cada modalidad por separado en cáncer de mama premenopáusico sin afectación ganglionar (IBCSG VIII) |
| [17159194](https://pubmed.ncbi.nlm.nih.gov/17159194/) | 2007 | ECA (análisis secundario) | J Clin Oncol | Impacto en amenorrea, sofocos y calidad de vida de la quimioterapia, la goserelina o su combinación secuencial |
| [8513962](https://pubmed.ncbi.nlm.nih.gov/8513962/) | 1993 | ECA | Fertil Steril | Goserelina frente a anticonceptivo oral de baja dosis para el dolor pélvico asociado a endometriosis |
| [28472240](https://pubmed.ncbi.nlm.nih.gov/28472240/) | 2017 | Revisión/Metaanálisis | Ann Oncol | Ensayo OPTION: agonista de GnRH para proteger frente a la toxicidad ovárica durante la quimioterapia en cáncer de mama precoz |
| [12353820](https://pubmed.ncbi.nlm.nih.gov/12353820/) | 2002 | Revisión/Metaanálisis | Breast Cancer Res Treat | Agonistas de LHRH en cáncer de mama precoz y beneficios de la ablación ovárica reversible |
| [25187267](https://pubmed.ncbi.nlm.nih.gov/25187267/) | 2015 | Cohortes | Cancer Res Treat | La ablación ovárica con goserelina mejora la supervivencia en cáncer de mama estadio II/III sin amenorrea inducida por quimioterapia |
| [26951320](https://pubmed.ncbi.nlm.nih.gov/26951320/) | 2016 | Observacional | J Clin Oncol | Utilidad de la monitorización de estradiol en mujeres con supresión ovárica por cáncer de mama |
| [12734855](https://pubmed.ncbi.nlm.nih.gov/12734855/) | 2003 | Revisión | Br J Surg | Métodos de ablación ovárica en cáncer de mama pre y perimenopáusico |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Revisión | J R Army Med Corps | Inducción terapéutica de amenorrea; la goserelina es muy eficaz, con la anticoncepción oral continua como alternativa |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| R-7832 | ZOLADEX JERINGA PRECARGADA | Implante | No disponible en los datos compilados |
| 61367 | ZOLADEX TRIMESTRAL 10,8 mg IMPLANTE EN JERINGA PRECARGADA | Implante | No disponible en los datos compilados |
| 58603 | ZOLADEX 3,6 mg IMPLANTE EN JERINGA PRECARGADA | Implante | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): trastorno hipertensivo e hipertensión, hiperglucemia, diabetes mellitus, cetoacidosis diabética, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, obesidad (incluida la monogénica) y obstrucción de las vías urinarias.
- **Interacciones farmacológicas:** se identificaron 371 interacciones. Entre las principales:
  - **Mayor:** dolasetrón.
  - **Moderadas:** antidiabéticos (acarbosa, metformina, glimepirida, clorpropamida, canagliflozina, dapagliflozina, empagliflozina, alogliptina, linagliptina, saxagliptina, albiglutida, dulaglutida), claritromicina, famotidina, loperamida, bisacodilo, ácido picosulfúrico, polietilenglicol con electrolitos y palonosetrón.
  - Las interacciones con antidiabéticos son coherentes con las contraindicaciones del grafo relativas a la glucemia.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El efecto de la goserelina sobre la supresión ovárica y la amenorrea está bien documentado, con varios ECA, aunque casi todos en cáncer de mama y no en la amenorrea como enfermedad. La prueba es indirecta y la indicación, tal como se formula, es mecanísticamente contradictoria, por lo que solo puede avanzar si se replantea.

**Para avanzar se necesita:**
- Reformular la indicación (supresión menstrual deliberada o protección de la función ovárica durante la quimioterapia) y definir criterios de valoración específicos.
- Obtener el prospecto oficial de la AEMPS con advertencias y contraindicaciones, pues faltan en los datos compilados y bloquean el cribado de seguridad.
- Datos detallados del mecanismo de acción.
- Plan de monitorización de seguridad (glucemia, presión arterial, calcio) y revisión de las interacciones con antidiabéticos.

**Otras predicciones del modelo:** la hipoplasia renal (y su forma bilateral) tiene puntuaciones altas (≈99,06 %), pero no cuenta con ensayos, literatura ni vínculo mecanístico identificable. Probablemente son artefactos del modelo y se recomienda **Hold** (nivel de evidencia L5).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


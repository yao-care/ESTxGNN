---
layout: default
title: Palbociclib
parent: Solo predicción del modelo (L5)
nav_order: 603
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-20
description: "Palbociclib: nueva indicación predicha, Hipertiroidismo (nivel de evidencia L5). Indicación original: No disponible en los datos de autorización (el texto de indicación es…"
monitor_inn: "PALBOCICLIB"
predicted_indications: ["hyperthyroidism", "rheumatoid arthritis", "thrombotic disease", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta"]
---

# Palbociclib
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

## Palbociclib: De Indicación No Especificada a Hipertiroidismo
{: .text-alpha }

## Resumen en Una Frase

Palbociclib es un inhibidor de las quinasas dependientes de ciclinas 4 y 6 (CDK4/6) que se comercializa en España con el nombre IBRANCE; los datos compilados para este informe no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **artritis reumatoide** (puntaje de 0,9936, segunda predicción del ranking).
Esta predicción se respalda con **0 ensayos clínicos** y **4 publicaciones** (un reporte de caso, un estudio observacional y dos estudios preclínicos).

> **Nota sobre la selección:** la predicción de mayor puntaje del modelo es hipertiroidismo (0,9944), pero no tiene ensayos ni literatura. Se evalúa aquí la artritis reumatoide por ser la primera con evidencia indirecta disponible. Las demás predicciones (hipertiroidismo, enfermedad trombótica y resistencia a la hormona tiroidea por mutación del receptor beta) se comentan en la conclusión.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de autorización (el texto de indicación está vacío) |
| Nueva Indicación Predicha | Artritis reumatoide (predicción n.º 2; la n.º 1, hipertiroidismo, no tiene evidencia) |
| Puntaje de Predicción TxGNN | 0,9936 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 3 de 6; autorizadas no comercializadas: 3) |
| Número de Autorizaciones | 6 (comercializadas: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Palbociclib es un inhibidor de CDK4/6 que bloquea la progresión del ciclo celular en la fase G1. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Palbociclib (traducción no oficial): «El palbociclib es un inhibidor de las cinasas dependientes de ciclinas (CDK) 4 y 6. La ciclina D1 y las CDK4/6 se encuentran corriente abajo de vías de señalización que conducen a la proliferación celular. In vitro, el palbociclib redujo la proliferación celular de líneas celulares de cáncer de mama positivas para el receptor de estrógeno (RE) al bloquear la progresión de la célula de la fase G1 a la fase S del ciclo celular.» Texto original en inglés: "Palbociclib is an inhibitor of cyclin-dependent kinases (CDK) 4 and 6. Cyclin D1 and CDK4/6 are downstream of signaling pathways which lead to cellular proliferation. In vitro, palbociclib reduced cellular proliferation of estrogen receptor (ER)-positive breast cancer cell lines by blocking progression of the cell from G1 into S phase of the cell cycle." ([DailyMed: Ibrance (palbociclib) prescribing information, U.S. Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=89a142d5-7e61-48bf-9e77-e2cd124c4792), versión del 2026-07-06; consultado el 2026-11-19).

En artritis reumatoide, la hiperplasia sinovial depende de la proliferación de fibroblastos sinoviales. Estudios preclínicos indican que la inhibición del ciclo celular mejora la enfermedad en modelos animales sin suprimir la inmunidad adquirida (PMID 25165034). Otro trabajo señala una hiperplasia sinovial dependiente de CDK6 (PMID 39940918). Además, un reporte de caso describe la mejoría de una artritis reumatoide en una paciente con cáncer de mama tratada con palbociclib (PMID 33587021).

Aun así, la evidencia es indirecta: modelos animales, un caso aislado y un estudio observacional. No hay evidencia clínica controlada, y la similitud con la indicación original no se ha podido evaluar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33587021](https://pubmed.ncbi.nlm.nih.gov/33587021/) | 2021 | Reporte de caso | Modern Rheumatology Case Reports | Mejoría de la artritis reumatoide en una mujer de 56 años con cáncer de mama tratada con palbociclib |
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Observacional (cohorte) | The Oncologist | Enfermedades inmunomediadas preexistentes y emergentes en pacientes con cáncer de mama tratadas con inhibidores de CDK4/6 y terapia endocrina |
| [25165034](https://pubmed.ncbi.nlm.nih.gov/25165034/) | 2016 | Preclínico (modelo animal) | Annals of the Rheumatic Diseases | La inhibición del ciclo celular combinada con bloqueo de citocinas potencia el efecto antiartrítico sin aumentar la inmunosupresión |
| [39940918](https://pubmed.ncbi.nlm.nih.gov/39940918/) | 2025 | Preclínico (modelo animal) | Int J Mol Sci | Hiperplasia sinovial dependiente de CDK6 e independiente de CDK4 en ratones artríticos |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1161147005 | IBRANCE 125 MG CÁPSULAS DURAS | Cápsula dura | No disponible |
| 1161147003 | IBRANCE 100 MG CÁPSULAS DURAS | Cápsula dura | No disponible |
| 1161147001 | IBRANCE 75 MG CÁPSULAS DURAS | Cápsula dura | No disponible |
| 1161147012 | IBRANCE 100 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible |
| 1161147010 | IBRANCE 75 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible |

Hay una sexta autorización (1161147014, IBRANCE 125 MG comprimidos recubiertos con película), no listada por el límite de cinco.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de CDK4/6), usada en cáncer de mama |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto. La literatura preclínica reporta mielosupresión inducida por palbociclib (PMID 39940918) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; en general, hemograma con diferencial |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 100 interacciones (fuente: DDInter). Entre las de nivel **mayor** figuran claritromicina, cobicistat, deferiprona y lexidronam de samario (153Sm). Hay además numerosas interacciones moderadas (por ejemplo aprepitant, dexametasona, cimetidina, simvastatina, cilostazol, miconazol y cisaprida) y una menor (prucaloprida). La lista completa debe revisarse antes de cualquier uso.
- **Señal de seguridad relacionada:** la literatura de farmacovigilancia (FAERS) describe eventos tromboembólicos con inhibidores de CDK4/6 (PMID 36794339, 39123221), además de toxicidad pulmonar, como la enfermedad pulmonar intersticial (PMID 37994878).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia para artritis reumatoide es solo preclínica y de un caso aislado (nivel L4), sin ensayos clínicos. Las otras predicciones carecen de respaldo (hipertiroidismo y resistencia a la hormona tiroidea, nivel L5) o la literatura apunta a un riesgo y no a un beneficio (enfermedad trombótica, donde la tromboembolia es un evento adverso). Los antecedentes de mielosupresión y las interacciones de nivel mayor añaden cautela.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (indicaciones, advertencias y contraindicaciones), actualmente ausente.
- Completar los datos del mecanismo de acción desde DrugBank.
- Estudios preclínicos adicionales y, de ser favorables, un ensayo exploratorio de fase 2 en artritis reumatoide.
- Evaluar la relación beneficio-riesgo, en particular mielosupresión, eventos tromboembólicos e interacciones, en una población no oncológica.
- Valorar la compatibilidad de vías de administración y la similitud con la indicación original, hoy pendientes.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Ibrance (palbociclib) prescribing information, U.S. Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=89a142d5-7e61-48bf-9e77-e2cd124c4792) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


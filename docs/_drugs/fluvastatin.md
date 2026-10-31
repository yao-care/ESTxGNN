---
layout: default
title: Fluvastatin
parent: Solo predicción del modelo (L5)
nav_order: 352
evidence_level: L5
indication_count: 6
monitor_inn: "Fluvastatin"
predicted_indications: ["HIV infectious disease", "cholesterol-ester transfer protein deficiency", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "fibroma of prostate"]
last_modified_at: 2026-10-31
description: "Fluvastatin: nueva indicación predicha, Infección por VIH (nivel de evidencia L5). Indicación original: Arteriosclerosis, aterosclerosis e hiperlipidemia combinada familiar"
---

# Fluvastatin
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

## Fluvastatina: De Arteriosclerosis/Aterosclerosis a Infección por VIH
{: .text-alpha }

## Resumen en Una Frase

Fluvastatina es una estatina (inhibidor de la HMG-CoA reductasa) que, según la relación registrada en el grafo de conocimiento, se asocia con arteriosclerosis, aterosclerosis e hiperlipidemia combinada familiar. El modelo TxGNN predice que podría ser útil en **infección por VIH**, aunque la señal clínica se refiere sobre todo a la dislipidemia asociada al VIH y no al tratamiento de la infección. Los datos compilados incluyen **0 ensayos clínicos registrados** y **13 publicaciones**, varias de ellas estudios clínicos pequeños en pacientes con VIH.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Arteriosclerosis, aterosclerosis e hiperlipidemia combinada familiar (relación registrada en el grafo de conocimiento; las fichas de autorización locales no incluyen texto de indicación) |
| Nueva Indicación Predicha | Infección por VIH |
| Puntaje de Predicción TxGNN | 0,9988 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 16) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

**Nota sobre el nivel de evidencia:** las publicaciones recopiladas estudian fluvastatina en pacientes con VIH, pero abordan la dislipidemia, las interacciones con antirretrovirales, la coinfección por VHC y un modelo murino de nefropatía asociada al VIH. Ninguna estudia el tratamiento de la infección por VIH en sí. Por ello, conforme a las reglas de evaluación, el nivel se fija en L5, aunque el análisis interno de los datos sugería L3.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Por conocimiento general, fluvastatina inhibe la HMG-CoA reductasa (gen *HMGCR*), reduce el colesterol LDL y se utiliza en hipercolesterolemia y en la reducción del riesgo cardiovascular.

Fluvastatina no es un antiviral. Su interés en el VIH es indirecto: la terapia antirretroviral puede causar dislipidemia y aumentar el riesgo cardiovascular, y fluvastatina se metaboliza principalmente por CYP2C9, por lo que tiene menor riesgo de interacción con los inhibidores de proteasa (que inhiben CYP3A4) que otras estatinas como simvastatina o lovastatina. Además, las estatinas podrían tener efectos inmunomoduladores y antiinflamatorios sobre los biomarcadores de activación inmune en personas con VIH, aunque el estudio que lo evalúa no es específico de fluvastatina.

Existen señales preclínicas (protección de los podocitos en un modelo murino de nefropatía asociada al VIH) y datos mixtos y limitados en coinfección VIH/VHC. En conjunto, la predicción del modelo refleja más bien un posible manejo de comorbilidades que un efecto sobre el propio virus.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20118492](https://pubmed.ncbi.nlm.nih.gov/20118492/) | 2010 | ECA abierto | J Antimicrob Chemother | Fluvastatina como adyuvante de interferón pegilado y ribavirina en coinfectados VIH/VHC genotipo 1 |
| [12351967](https://pubmed.ncbi.nlm.nih.gov/12351967/) | 2002 | Estudio clínico | AIDS | Eficacia y seguridad de fluvastatina en pacientes con VIH hiperlipidémicos tratados con inhibidores de proteasa |
| [15293079](https://pubmed.ncbi.nlm.nih.gov/15293079/) | 2004 | Estudio clínico | Infection | Comparación de fluvastatina y pravastatina para reducir lípidos en VIH con terapia antirretroviral, e interacción con indinavir |
| [16868453](https://pubmed.ncbi.nlm.nih.gov/16868453/) | 2006 | Estudio aleatorizado | AIDS | Ezetimiba redujo el LDL un 20 % frente a 24 % con fluvastatina 80 mg/día en pacientes con VIH |
| [33238713](https://pubmed.ncbi.nlm.nih.gov/33238713/) | 2021 | Cohorte/Análisis | AIDS Res Hum Retroviruses | Uso de estatinas y biomarcadores de inflamación e inmunoactivación en VIH con TAR eficaz (no específico de fluvastatina) |
| [19838098](https://pubmed.ncbi.nlm.nih.gov/19838098/) | 2010 | ECA | AIDS | Rosuvastatina frente a pravastatina en dislipidemia por VIH con inhibidores de proteasa (no evalúa fluvastatina) |
| [23703578](https://pubmed.ncbi.nlm.nih.gov/23703578/) | 2013 | Revisión | Clin Pharmacokinet | Interacciones entre estatinas e inhibidores de proteasa antivirales |
| [12660532](https://pubmed.ncbi.nlm.nih.gov/12660532/) | 2003 | Revisión | AIDS | Estatinas y fibratos en la hiperlipidemia de pacientes con VIH con TARGA |
| [19215577](https://pubmed.ncbi.nlm.nih.gov/19215577/) | 2009 | Estudio piloto | J Viral Hepat | Efecto de fluvastatina sobre la replicación del VHC en coinfectados VIH-VHC |
| [19188342](https://pubmed.ncbi.nlm.nih.gov/19188342/) | 2009 | Preclínico | Nephrol Dial Transplant | Fluvastatina previno la lesión de podocitos en un modelo murino de nefropatía asociada al VIH |

## Información de Mercado en España

La lista siguiente es parcial: hay al menos 20 autorizaciones y se muestran 5 de ellas. Los registros no incluyen texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Estado |
|---------|------|------|-----------|
| 64648 | Lescol Prolib 80 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | Vigente |
| 64782 | Vaditon Prolib 80 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | Vigente |
| 69981 | Fluvastatina Teva 20 mg cápsulas duras EFG | Cápsula dura | Vigente |
| 71631 | Fluvastatina Viatris 40 mg cápsulas duras EFG | Cápsula dura | Vigente |
| 72243 | Fluvastatina Farmalider 40 mg cápsulas duras EFG | Cápsula dura | Cancelada |

## Consideraciones de Seguridad

- **Contraindicaciones o enfermedades de precaución registradas en el grafo de conocimiento** (no proceden del texto del prospecto): enfermedad hepática, enfermedad de la vesícula biliar, miopatía, enfermedad muscular, enfermedad del músculo esquelético, parálisis periódica familiar, trastornos hipotensivos, abuso o dependencia de sustancias, rabdomiólisis, fascitis nodular y lesiones.
- **Interacciones farmacológicas**: los datos compilados solo recogen la diana farmacológica (HMG-CoA reductasa), sin interacciones con otros fármacos. La literatura revisada señala que las estatinas pueden interaccionar con los inhibidores de proteasa y causar alteraciones musculares, desde mialgia hasta rabdomiólisis grave; fluvastatina, por su metabolismo vía CYP2C9, presenta menor riesgo.

Consultar el prospecto para el resto de la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún estudio recopilado evalúa fluvastatina como tratamiento de la infección por VIH; la evidencia se limita a dislipidemia, interacciones y comorbilidades en pacientes con VIH, por lo que el nivel es L5 pese al puntaje alto del modelo. Como pregunta de investigación sobre manejo de comorbilidades en VIH puede explorarse, pero no como indicación antiviral.

**Para avanzar se necesita:**
- Definir con claridad el objetivo: tratamiento de la dislipidemia o la inflamación en VIH, no el control de la infección.
- Estudios o ensayos que evalúen directamente fluvastatina frente a desenlaces del VIH (carga viral, activación inmune, eventos cardiovasculares).
- Datos del mecanismo de acción y del prospecto de la AEMPS (advertencias y contraindicaciones).
- Análisis de seguridad e interacciones con los regímenes antirretrovirales actuales.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


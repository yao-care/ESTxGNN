---
layout: default
title: Sirolimus
parent: Solo predicción del modelo (L5)
nav_order: 495
evidence_level: L5
indication_count: 10
---

# Sirolimus
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Sirolimus: De Inmunosupresión en Trasplante Renal a Liposarcoma

## Resumen en Una Frase

Sirolimus (comercializado en España como Rapamune) es un inhibidor de mTOR que se usa como inmunosupresor en trasplante renal. Este uso procede del conocimiento general del fármaco, porque los datos de AEMPS recibidos no incluyen el texto de la indicación.
El modelo TxGNN predice que podría ser efectivo para **liposarcoma**. Hay **5 ensayos clínicos** (solo 1 con sirolimus; los demás usan otros inhibidores de mTOR) y **12 publicaciones**, con evidencia clínica aún limitada y sin resultados publicados para el único ensayo con sirolimus.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Inmunosupresión en trasplante renal (conocimiento general; el texto de indicación de AEMPS no viene en los datos) |
| Nueva Indicación Predicha | Liposarcoma |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L2 (con reservas: el único ensayo con sirolimus es de Fase 2, de brazo único, sin resultados en los datos) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados de DrugBank sobre el mecanismo de acción. Según la información conocida, sirolimus inhibe el complejo mTORC1, una quinasa que regula el crecimiento, la proliferación y el metabolismo celular. Este efecto antiproliferativo es la base tanto de su uso como inmunosupresor como del interés oncológico.

La relación entre la indicación original y la nueva no es clínica sino de vía de señalización. El trasplante renal y el liposarcoma son enfermedades muy distintas, pero en el liposarcoma desdiferenciado se ha descrito activación de las vías Akt-mTOR y MAPK (PMID 26518767). Esto ofrece una diana plausible para un inhibidor de mTORC1.

Además, hay datos preclínicos en un modelo de xenoinjerto ortotópico derivado de paciente (PDOX). La combinación de rapamicina (sirolimus) con cloroquina, que bloquea la autofagia, frenó el crecimiento del liposarcoma desdiferenciado (PMID 36309387) y también fue eficaz en el bien diferenciado (PMID 37400145). Estos datos son de ratón y no equivalen a eficacia en pacientes. Además, el término "liposarcoma" agrupa subtipos con biología distinta, por lo que la aplicabilidad del mecanismo puede variar entre ellos.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Fase 2 | Completado | 70 | Sirolimus + ciclofosfamida en liposarcoma mixoide y condrosarcoma metastásico o irresecable (brazo único). Es el único ensayo con sirolimus; los datos no incluyen resultados. |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Fase 2 | Completado | 216 | Ridaforolimus (inhibidor de mTOR, no sirolimus) en sarcoma avanzado. Apoya el efecto de clase. |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Fase 2 | Activo, sin reclutamiento | 48 | Ribociclib + everolimus en liposarcoma desdiferenciado y leiomiosarcoma avanzados. Enfermedad muy relevante, pero el inhibidor de mTOR es everolimus. |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Fase 1/2 | Completado | 24 | Temsirolimus + doxorrubicina liposomal en sarcomas de tejidos blandos y óseo recurrentes. Población mixta. |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Fase 2 | Completado | 46 | Cixutumumab + temsirolimus en tumores sólidos pediátricos recurrentes o refractarios. Población y tumores distintos del liposarcoma adulto. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | ECA (trasplante renal) | J Am Soc Nephrol | Tras retirar la ciclosporina, el tratamiento con sirolimus redujo el riesgo de cáncer en trasplantados renales. Evidencia indirecta. |
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Ensayo Fase 2 | Clin Cancer Res | Ribociclib + everolimus en liposarcoma desdiferenciado y leiomiosarcoma. Se basa en la sinergia CDK4/6 + mTOR; el resumen disponible no muestra resultados. |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Estudio traslacional | Tumour Biol | En 99 muestras de liposarcoma desdiferenciado se observó activación de las vías Akt-mTOR y MAPK, y se evaluó un inhibidor de mTOR in vitro. |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | Preclínico | Cancer Genomics Proteomics | Cloroquina + rapamicina, con efecto sinérgico sobre la autofagia, como tratamiento del liposarcoma bien diferenciado. |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | Preclínico (PDOX) | In Vivo | Cloroquina + rapamicina detuvo el crecimiento tumoral en un modelo PDOX de liposarcoma desdiferenciado. |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | Preclínico | Mol Cancer Ther | MLN0128, inhibidor de mTOR competitivo con ATP, con actividad en sarcoma óseo y de tejidos blandos. Los rapálogos de primera generación tuvieron utilidad clínica limitada. |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Revisión | Cancers | Avances terapéuticos recientes en sarcomas de tejidos blandos. |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Revisión | Curr Opin Oncol | Tratamientos dirigidos en sarcomas avanzados y resultados de ensayos recientes. |
| [20534289](https://pubmed.ncbi.nlm.nih.gov/20534289/) | 2010 | No clasificado | Transplant Proc | Conversión a rapamicina como inmunosupresor tras una neoplasia en trasplante renal. |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | No clasificado | Bull Cancer | Tratamientos dirigidos en tumores conectivos raros y sarcomas. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 01171010 | RAPAMUNE 2 mg comprimidos recubiertos | Comprimido recubierto | No indicada en los datos de origen |
| 01171008 | RAPAMUNE 1 mg comprimidos recubiertos | Comprimido recubierto | No indicada en los datos de origen |
| 01171009 | RAPAMUNE 2 mg comprimidos recubiertos | Comprimido recubierto | No indicada en los datos de origen |
| 01171013 | RAPAMUNE 0,5 mg comprimidos recubiertos | Comprimido recubierto | No indicada en los datos de origen |
| 01171001 | RAPAMUNE 1 mg/ml solución oral | Solución oral | No indicada en los datos de origen |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Solo un ensayo de Fase 2 de brazo único usa sirolimus en sarcoma, y los datos no muestran sus resultados. El resto de la evidencia es de otros inhibidores de mTOR o preclínica. Además, no se dispone de la información de seguridad del prospecto de AEMPS, lo que impide avanzar a la evaluación de seguridad.

Otras predicciones del mismo fármaco tienen respaldo más sólido y merecen priorizarse. Son el PEComa benigno, la linfangioleiomiomatosis y el PEComa pulmonar, todos con nivel L2 y decisión "Proceed with Guardrails" en el análisis previo.

**Para avanzar se necesita:**
- Resultados publicados o registrados del ensayo NCT02821507 (respuesta y supervivencia), con datos separados para el subgrupo de liposarcoma.
- Definir el subtipo objetivo (mixoide, desdiferenciado o bien diferenciado), porque la evidencia actual no es uniforme.
- Obtener la ficha técnica de AEMPS (advertencias, contraindicaciones e interacciones) para hacer la evaluación de seguridad.
- Datos del mecanismo de acción desde DrugBank para completar el análisis mecanístico.
- Comprobar si hay datos propios de sirolimus, distintos de los de everolimus o temsirolimus, antes de extrapolar el efecto de clase.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


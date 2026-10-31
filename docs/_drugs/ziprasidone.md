---
layout: default
title: Ziprasidone
parent: Solo predicción del modelo (L5)
nav_order: 866
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
description: "Ziprasidone: nueva indicación predicha, Tricotilomanía (nivel de evidencia L5). Indicación original: Trastorno afectivo bipolar maníaco, trastorno bipolar y esquizofrenia"
monitor_inn: "Ziprasidone"
predicted_indications: ["trichotillomania", "hydranencephaly (disease)", "major affective disorder", "congenital disorder of glycosylation with defective fucosylation", "myopia X-linked", "retinal dystrophy with or without extraocular anomalies", "Tourette syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "myopia 26, X-linked, female-limited", "syndromic myopia"]
---

# Ziprasidone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Ziprasidona: De Trastorno Bipolar Maníaco a Tricotilomanía
{: .text-alpha }

## Resumen en Una Frase

Ziprasidona es un antipsicótico atípico utilizado originalmente para el tratamiento de la esquizofrenia y del trastorno bipolar (episodios maníacos).
El modelo TxGNN predice que podría ser efectivo para la **tricotilomanía**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción exclusivamente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno afectivo bipolar maníaco, trastorno bipolar y esquizofrenia |
| Nueva Indicación Predicha | Tricotilomanía |
| Puntaje de Predicción TxGNN | 0.9983 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 19) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Sí se conoce el perfil de unión a receptores de ziprasidona: actúa sobre el receptor de dopamina D2, múltiples receptores de serotonina (5-HT1A, 1B, 1D, 1E, 2A, 2C y 7), el receptor de histamina H1 y los transportadores de serotonina (SERT) y noradrenalina (NET).

Una posible conexión con la tricotilomanía sería el antagonismo dopaminérgico D2 y serotoninérgico 5-HT2A, mecanismos relevantes en trastornos de conductas repetitivas. Sin embargo, esta hipótesis es **especulativa** y no está respaldada por los datos compilados: no se recuperó ningún ensayo ni publicación que la sustente.

La relación con la indicación original es débil. La esquizofrenia y el trastorno bipolar son trastornos psicóticos y afectivos, mientras que la tricotilomanía se clasifica como un trastorno de conductas repetitivas centradas en el cuerpo. El puntaje alto proviene del modelo TxGNN (deep learning) y debe interpretarse con cautela, ya que puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica o clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de principio activo único, en cápsula dura salvo una presentación inyectable).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 64851 | ZELDOX 20 mg cápsulas duras | Cápsula dura |
| 64852 | ZELDOX 40 mg cápsulas duras | Cápsula dura |
| 64853 | ZELDOX 60 mg cápsulas duras | Cápsula dura |
| 64854 | ZELDOX 80 mg cápsulas duras | Cápsula dura |
| 64855 | ZELDOX 20 mg/ml polvo para solución inyectable | Polvo para solución inyectable |

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (según la base de conocimiento del modelo, no el texto del prospecto)**:
  - Cardiovasculares y del ritmo: síndrome de QT largo (incluido el familiar), torsades de pointes, enfermedad de la conducción cardíaca, paro cardíaco súbito, infarto de miocardio, trombosis coronaria.
  - Hipotensión: hipotensión ortostática, síndrome de taquicardia postural ortostática, atrofia multisistémica.
  - Hematológicas: neutropenia, agranulocitosis, hemoglobinopatía.
  - Metabólicas: diabetes mellitus, hiperglucemia, cetoacidosis diabética, hiperlipidemia (incluida la familiar), obesidad (incluida la monogénica), deficiencia de potasio.
  - Neurológicas: epilepsia, enfermedades de los ganglios basales, distonía focal de la mano, blefarospasmo.
  - Otras: insuficiencia hepática, enfermedad renal, piouréter, carcinoma de mama femenino.
- **Perfil farmacológico**: los datos de interacciones disponibles describen únicamente la unión a receptores y transportadores, no interacciones con otros fármacos específicos. Por su riesgo de prolongación del QT, conviene evitar combinaciones con otros fármacos que prolonguen el QT.

Para advertencias principales y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para tricotilomanía se basa solo en el puntaje del modelo (0.9983), sin ensayos clínicos ni literatura (nivel L5), y el vínculo mecanístico es especulativo. El perfil de seguridad, en especial el riesgo cardíaco (QT), exige una justificación clínica sólida antes de avanzar.

**Para avanzar se necesita:**
- Revisión sistemática de literatura específica sobre ziprasidona (o antipsicóticos atípicos) en tricotilomanía y trastornos de conductas repetitivas.
- Datos detallados del mecanismo de acción (MOA) y análisis de su vínculo con la fisiopatología de la tricotilomanía.
- Obtención y análisis del prospecto de la AEMPS (advertencias y contraindicaciones oficiales).
- Estudios preclínicos o un piloto clínico pequeño con monitorización de QTc, si el interés persiste.

**Nota adicional:** en los mismos datos, otras indicaciones predichas para ziprasidona tienen más respaldo que la tricotilomanía: el **trastorno afectivo mayor** (nivel L2, con ensayos de Fase 2 completados, recomendación *Proceed with Guardrails*) y el **síndrome de Tourette** (nivel L3, con un estudio piloto pediátrico). Podrían priorizarse en una evaluación posterior.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


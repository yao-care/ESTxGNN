---
layout: default
title: Modafinil
parent: Solo predicción del modelo (L5)
nav_order: 539
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
monitor_inn: "modafinil"
predicted_indications: ["insomnia (disease)"]
description: "Modafinil: nueva indicación predicha, insomnio (insomnia (disease)) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 7 (comercializadas: 6)"
---

# Modafinil
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Modafinil: insomnio (insomnia (disease))
{: .text-alpha }

## Resumen en Una Frase

Modafinilo es un fármaco promotor de la vigilia, comercializado en España en comprimidos de 100 mg.
El modelo TxGNN predice que podría ser efectivo para **insomnio (insomnia)**, pero la evidencia es muy limitada: **2 ensayos clínicos** registrados (uno terminado con solo 2 participantes y otro completado sin resultados publicados) y ninguna publicación que estudie directamente el insomnio. El nivel de evidencia es **L5**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | insomnio (insomnia (disease)) |
| Puntaje de Predicción TxGNN | 0.9985 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 6 de 7; revocadas o suspendidas: 1) |
| Número de Autorizaciones | 7 (comercializadas: 6) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Modafinil (traducción no oficial): «Se desconoce el mecanismo o los mecanismos mediante los cuales el modafinilo promueve la vigilia. El modafinilo tiene acciones promotoras de la vigilia similares a las de los agentes simpaticomiméticos, incluidos la anfetamina y el metilfenidato, aunque el perfil farmacológico no es idéntico al de las aminas simpaticomiméticas.» Texto original en inglés: "The mechanism(s) through which modafinil promotes wakefulness is unknown. Modafinil has wake-promoting actions similar to sympathomimetic agents including amphetamine and methylphenidate, although the pharmacologic profile is not identical to that of the sympathomimetic amines." ([DailyMed: Provigil (modafinil) prescribing information, Apotex Corp](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0391f182-1958-9fef-a944-53b229ce99e7), versión del 2026-09-16; consultado el 2026-11-19). Por lo general, modafinilo se entiende como un agente promotor de la vigilia que actúa sobre circuitos de vigilia y sobre el transportador de dopamina, con el objetivo de reducir la somnolencia excesiva.

Aquí está la dificultad: el insomnio se caracteriza por dificultad para iniciar o mantener el sueño, justo lo contrario del problema que trata un fármaco que promueve la vigilia. El puntaje alto (0,9985) probablemente refleja la cercanía en la red del modelo con otros trastornos del sueño y la vigilia, y no un vínculo terapéutico real.

Por ello, la plausibilidad mecanística es baja. La literatura disponible trata sobre somnolencia diurna y alteraciones del sueño en enfermedades concomitantes (adultos mayores, enfermedad de Parkinson, trastornos neurológicos, trabajo por turnos), no sobre insomnio en sí.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00124384](https://clinicaltrials.gov/study/NCT00124384) | Fase 4 | Completado | 40 | Efecto de modafinilo, solo o con terapia cognitivo-conductual para el insomnio, sobre el funcionamiento diurno y la gravedad del insomnio; sin resultados publicados |
| [NCT00626210](https://clinicaltrials.gov/study/NCT00626210) | Fase 4 | Terminado | 2 | Alteraciones del sueño y la vigilia en adultos mayores; terminado con solo 2 participantes, sin datos interpretables |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Revisión sistemática/Metaanálisis | PloS one | Eficacia de modafinilo sobre la fatiga y la somnolencia diurna en trastornos neurológicos; no aborda el insomnio |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Revisión sistemática/Metaanálisis | Parkinsonism & related disorders | Intervenciones farmacológicas para somnolencia y trastornos del sueño en Parkinson |
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Revisión | Drugs | Revisión de usos aprobados y en investigación de modafinilo basada en ensayos aleatorizados |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | Revisión | Movement disorders | Revisión basada en la evidencia de tratamientos de síntomas no motores del Parkinson |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Revisión | Drugs | Carga y manejo del trastorno del sueño por trabajo en turnos |

Ninguna de estas publicaciones estudia directamente el insomnio como enfermedad tratada con modafinilo.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 80929 | MODAFINILO TARBIS 100 mg COMPRIMIDOS EFG | Comprimido | No disponible en los datos compilados |
| 75919 | MODAFINILO AUROVITAS 100 MG COMPRIMIDOS EFG | Comprimido | No disponible en los datos compilados |
| 72187 | MODAFINILO MYLAN 100 mg COMPRIMIDOS EFG | Comprimido | No disponible en los datos compilados |
| 61540 | MODIODAL 100 mg COMPRIMIDOS | Comprimido | No disponible en los datos compilados |
| 84141 | MODAFINILO ARISTO 100 MG COMPRIMIDOS EFG | Comprimido | No disponible en los datos compilados |

Hay 7 autorizaciones registradas, de las cuales 6 están vigentes y 1 cancelada.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 249 interacciones potenciales. Entre las de nivel moderado figuran omeprazol, esomeprazol, rabeprazol, dexametasona, eliglustat, linagliptina y cisaprida. Entre las de nivel leve figuran hidrocortisona, pioglitazona, aprepitant, triamcinolona, betametasona, cimetidina, claritromicina, saxagliptina y dronabinol.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo: el único ensayo en insomnio primario (NCT00124384) no tiene resultados publicados y ninguna publicación estudia directamente esta indicación, por lo que el nivel de evidencia es L5. Además, el mecanismo promotor de la vigilia de modafinilo es contrario al objetivo terapéutico en insomnio.

**Para avanzar se necesita:**
- Resultados publicados o registrados del ensayo NCT00124384
- Datos detallados del mecanismo de acción y una justificación mecanística de su uso en insomnio
- Ensayos controlados específicos en insomnio, con datos de eficacia y seguridad
- Revisión del prospecto para advertencias y contraindicaciones

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Provigil (modafinil) prescribing information, Apotex Corp](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0391f182-1958-9fef-a944-53b229ce99e7) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


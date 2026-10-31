---
layout: default
title: Paliperidone
parent: Solo predicción del modelo (L5)
nav_order: 604
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-31
monitor_inn: "Paliperidone"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "myopia X-linked", "syndromic myopia", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation", "myopia 26, X-linked, female-limited", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "atypical glycine encephalopathy"]
description: "Paliperidone: nueva indicación predicha, Distrofia retiniana con o sin anomalías extraoculares (retinal dystrophy with or without extraocular anomalies) (nivel de evidencia L5). Indicación original: …"
---

# Paliperidone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Paliperidone: Distrofia retiniana con o sin anomalías extraoculares (retinal dystrophy with or without extraocular anomalies)
{: .text-alpha }

## Resumen en Una Frase

Paliperidona es un antipsicótico utilizado originalmente para el tratamiento de la esquizofrenia y otros trastornos psicóticos.
El modelo TxGNN predice que podría ser efectivo para **distrofia retiniana con o sin anomalías extraoculares**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Distrofia retiniana con o sin anomalías extraoculares (retinal dystrophy with or without extraocular anomalies) |
| Puntaje de Predicción TxGNN | 0.9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 12) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento general, paliperidona (metabolito activo de la risperidona) actúa como antagonista de los receptores dopaminérgicos D2 y serotoninérgicos 5-HT2A, y su eficacia en esquizofrenia y trastorno esquizoafectivo está establecida.

Con la información disponible, **no se identifica un vínculo mecanístico plausible** entre este perfil farmacológico y la fisiopatología de las distrofias retinianas hereditarias, que son enfermedades de origen genético. El puntaje del modelo es muy alto (0.9992), pero proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; carece de respaldo clínico ni bibliográfico. Las otras predicciones de mayor puntaje (miopía ligada al X, hidranencefalia, enfermedad de Charcot-Marie-Tooth, entre otras) presentan la misma limitación.

La similitud entre la indicación original (trastornos psiquiátricos) y la nueva (enfermedad retiniana hereditaria) no ha sido evaluada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Paliperidona está comercializada en España con 20 autorizaciones vigentes (todas de principio activo único). Los textos de indicación aprobada no figuran en los datos compilados. Se muestran las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 11672002 | XEPLION 50 mg suspensión inyectable de liberación prolongada | Suspensión inyectable en jeringa precargada | No disponible |
| 11672004 | XEPLION 100 mg suspensión inyectable de liberación prolongada | Suspensión inyectable en jeringa precargada | No disponible |
| 114971010 | TREVICTA 525 mg suspensión inyectable de liberación prolongada | Suspensión inyectable de liberación prolongada | No disponible |
| 07395004 | INVEGA 3 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | No disponible |
| 07395006 | INVEGA 6 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de precaución según el grafo de conocimiento** (no proceden del texto del prospecto): síndrome de QT largo (incluida la forma familiar) y torsades de pointes; hipotensión ortostática, trastornos hipotensivos y síndrome de taquicardia postural ortostática; atrofia multisistémica; epilepsia; enfermedades de los ganglios basales y distonías focales; diabetes mellitus, hiperglucemia y cetoacidosis diabética; neutropenia y agranulocitosis; infarto de miocardio y trombosis coronaria; hiperlipidemia, obesidad; enfermedad de Crohn y enfermedad inflamatoria intestinal; carcinoma de mama femenino; insuficiencia renal; deficiencia de potasio; hemoglobinopatías.
- **Interacciones farmacológicas**: se registraron 100 interacciones. Entre las de nivel **mayor** figuran **bupropión** y **morfina**. Entre las de nivel **moderado** destacan los antidiabéticos (acarbosa, metformina, pioglitazona, alogliptina, albiglutida, canagliflozina, clorpropamida), anticolinérgicos (atropina, hiosciamina, glicopirronio), anfotericina B, epinefrina, hidrocortisona, famotidina, loperamida, lorcaserina y bisacodilo.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para distrofia retiniana carece de ensayos clínicos, literatura y vínculo mecanístico plausible; es una salida del modelo (nivel L5). Además, el perfil de seguridad es complejo, con numerosas condiciones de precaución e interacciones relevantes, lo que no justifica avanzar sin una base biológica.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y un análisis mecanístico que relacione paliperidona con la fisiopatología retiniana
- Estudios preclínicos (modelos de distrofia retiniana) que respalden la hipótesis
- Obtención y análisis de las advertencias y contraindicaciones del prospecto de la AEMPS
- Evaluación de la compatibilidad de vías de administración para uso oftalmológico
- Reconsiderar candidatos con más respaldo: la única predicción con estudios asociados es la esquizofrenia resistente al tratamiento (L4), pero es una subpoblación de la indicación ya aprobada, no un reposicionamiento real
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Givosiran
parent: Solo predicción del modelo (L5)
nav_order: 376
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Givosiran: nueva indicación predicha, Síndrome hepatopulmonar (nivel de evidencia L5). Indicación original: Porfiria hepática"
monitor_inn: "GIVOSIRAN"
predicted_indications: ["hepatopulmonary syndrome", "early-onset familial noncirrhotic portal hypertension", "hepatoportal sclerosis", "primitive portal vein thrombosis", "idiopathic copper-associated cirrhosis", "chronic hepatitis C virus infection", "glycogen storage disease due to hepatic glycogen synthase deficiency", "chronic hepatitis B virus infection", "porphyria due to ALA dehydratase deficiency", "disorder of phenylalanine metabolism"]
---

# Givosiran
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

# Givosiran: De Porfiria Hepática a Síndrome Hepatopulmonar

## Resumen en Una Frase

Givosiran es un ARN interferente pequeño (siRNA) conjugado con GalNAc, originalmente utilizado para el tratamiento de la porfiria hepática.
El modelo TxGNN predice que podría ser efectivo para **síndrome hepatopulmonar**, pero **no existe ningún ensayo clínico ni publicación** que respalde esta dirección; se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Porfiria hepática |
| Nueva Indicación Predicha | Síndrome hepatopulmonar |
| Puntaje de Predicción TxGNN | 99,999% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos compilada. Según la información conocida, givosiran es un siRNA conjugado con GalNAc que se dirige al hígado y silencia el ARNm de la ALAS1 hepática, reduciendo los precursores neurotóxicos ALA y PBG. Su eficacia en la porfiria hepática aguda ha sido comprobada en el ensayo de Fase 3 ENVISION.

El síndrome hepatopulmonar se debe a una dilatación vascular intrapulmonar asociada a enfermedad hepática. No se identifica un vínculo mecanístico entre la supresión de ALAS1 y esta patología. Lo más probable es que el puntaje elevado refleje únicamente la cercanía en el grafo de conocimiento con otras enfermedades hepáticas.

Por tanto, esta predicción debe considerarse con mucha cautela: carece de sustento mecanístico y de evidencia clínica o bibliográfica. Las otras predicciones de mayor puntaje (hipertensión portal familiar no cirrótica, esclerosis hepatoportal, trombosis portal primitiva, cirrosis asociada al cobre) presentan la misma limitación.

> Nota: entre las predicciones del modelo, la única con literatura relevante es la **porfiria por deficiencia de ALA deshidratasa (ADP)**, con puntaje de 99,91%. Es mecanísticamente plausible (acumulación de ALA) y cuenta con 9 publicaciones, aunque la evidencia específica se limita a casos clínicos con resultados discordantes (nivel L4). Podría ser una línea de investigación más razonable que la indicación principal.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para el síndrome hepatopulmonar.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1201428001 | GIVLAARI 189 MG/ML SOLUCIÓN INYECTABLE | Solución inyectable | Texto de indicación no disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 87 interacciones registradas. Entre las mostradas, la de nivel **Mayor** es con **eliglustat**; el resto son de nivel **Moderado**, por ejemplo: anfotericina B (y sus formulaciones lipídicas), aminoglucósidos (kanamicina, neomicina, estreptomicina), vancomicina, mesalazina, sulfasalazina, balsalazida, olsalazina, alosetrón, naltrexona, metoclopramida, exenatida, fenfluramina, dexfenfluramina y cafeína.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para síndrome hepatopulmonar es solo computacional (nivel L5), sin ensayos, sin literatura y sin vínculo mecanístico plausible con la supresión de ALAS1.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y del prospecto de la AEMPS (advertencias y contraindicaciones), que siguen pendientes
- Una hipótesis fisiopatológica que conecte el metabolismo del hemo con la dilatación vascular intrapulmonar, apoyada en estudios preclínicos
- Valorar priorizar la indicación de porfiria por deficiencia de ALA deshidratasa, que tiene mayor respaldo mecanístico y bibliográfico, y aclarar la discordancia entre los casos publicados (genotipo y contribución eritroide a la producción de ALA)
- Revisión del perfil de interacciones, en especial con eliglustat
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


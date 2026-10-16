---
layout: default
title: Doravirine
parent: Solo predicción del modelo (L5)
nav_order: 261
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Doravirine: nueva indicación predicha, Síndrome de inmunodeficiencia adquirida felina (nivel de evidencia L5). Indicación original: Infección por VIH / SIDA (según las indicaciones del grafo de conoc…"
---

# Doravirine
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

# Doravirina: De Infección por VIH a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Doravirina es un inhibidor no nucleosídico de la transcriptasa inversa (ITINN), utilizado originalmente para el tratamiento de la infección por VIH y el SIDA.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH / SIDA (según las indicaciones del grafo de conocimiento; el texto de indicación autorizado no está disponible) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, doravirina pertenece a la clase de los inhibidores no nucleosídicos de la transcriptasa inversa (ITINN), con actividad comprobada frente al VIH-1. Su eficacia en la infección por VIH está establecida, y es un fármaco comercializado en España.

El virus de la inmunodeficiencia felina (VIF) es un lentivirus emparentado con el VIH, lo que explica que el modelo asigne un puntaje alto por proximidad en la red de conocimiento a las indicaciones de VIH/SIDA. Sin embargo, esta cercanía refleja más una similitud entre enfermedades que una actividad demostrada del fármaco.

Existen razones para ser cautos: los ITINN suelen tener poca o ninguna actividad frente al VIF por diferencias en el bolsillo de unión de la transcriptasa inversa. Además, se trata de una indicación veterinaria, con escasa relevancia para el reposicionamiento en humanos. El puntaje elevado debe interpretarse como una señal del modelo y no como evidencia de eficacia.

### Otras predicciones del modelo

- **Infección por el virus de inmunodeficiencia simia (VIS)** (puntaje 99.93%): lentivirus de primates estrechamente relacionado con el VIH, pero los ITINN suelen ser inactivos frente al VIS y al VIH-2. Es una indicación de modelo animal/preclínica con escaso valor de reposicionamiento clínico.
- **Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y disminución de la sustancia blanca cortical** (puntaje 99.91%): no se identificó ningún vínculo mecanístico plausible; parece un artefacto de la predicción basada en grafos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Para la indicación principal (síndrome de inmunodeficiencia adquirida felina) actualmente no hay literatura relacionada disponible.

Para la segunda predicción (VIS), el modelo vinculó una publicación, que no aporta evidencia directa sobre doravirina:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Revisión | Current Opinion in HIV and AIDS | Analiza el papel potencial de islatravir, un inhibidor de la translocación de la transcriptasa inversa (fármaco distinto), en el tratamiento y la prevención del VIH-1 |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1181332001 | PIFELTRO 100 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 59 interacciones conocidas. Entre las de la muestra compilada destacan:
  - **Mayores**: dexametasona y lumacaftor.
  - **Moderadas**: fenilbutirato de glicerol, metreleptina, troglitazona, deferasirox, praziquantel y griseofulvina.
  - **Menores**: aprepitant, cimetidina, claritromicina, clotrimazol, miconazol, cobicistat, ticagrelor, ivacaftor, zafirlukast, cloranfenicol, eritromicina y fluconazol.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura directa. Además, los ITINN suelen carecer de actividad frente a lentivirus no humanos, y la indicación principal es veterinaria, con escasa relevancia para el reposicionamiento en humanos.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del fármaco.
- Advertencias y contraindicaciones del prospecto de la AEMPS, así como el texto de la indicación autorizada.
- Estudios in vitro de actividad de doravirina frente a VIF/VIS para validar la señal del modelo.
- Evaluar si existe interés real en una indicación veterinaria, o priorizar otras predicciones con mayor plausibilidad clínica.
- Revisión de las interacciones farmacológicas (especialmente las mayores) si se avanzara hacia cualquier uso adicional.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


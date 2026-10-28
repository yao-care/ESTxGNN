---
layout: default
title: Cefditoren
parent: Solo predicción del modelo (L5)
nav_order: 155
evidence_level: L5
indication_count: 1
monitor_inn: "cefditoren"
predicted_indications: ["rheumatoid arthritis"]
last_modified_at: 2026-10-28
description: "Cefditoren: nueva indicación predicha, Artritis reumatoide (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (el texto de indicación de las…"
---

# Cefditoren
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

## Cefditoreno: De Indicación Original No Registrada a Artritis Reumatoide
{: .text-alpha }

## Resumen en Una Frase

Cefditoreno es una cefalosporina oral de tercera generación, comercializada en España con cuatro autorizaciones, aunque los datos compilados para este informe no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **artritis reumatoide**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (el texto de indicación de las autorizaciones está vacío) |
| Nueva Indicación Predicha | Artritis reumatoide |
| Puntaje de Predicción TxGNN | 0,9902 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 4 de 4) |
| Número de Autorizaciones | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, cefditoreno es una cefalosporina oral de tercera generación que inhibe la síntesis de la pared celular bacteriana al unirse a las proteínas de unión a penicilina (PBP). No tiene actividad antiinflamatoria o inmunomoduladora establecida que sea relevante para la artritis reumatoide.

La relación entre la indicación original (una infección bacteriana, aunque su texto no figura en los datos) y la artritis reumatoide no es evidente desde el punto de vista mecanístico. Cualquier vínculo sería especulativo, por ejemplo, efectos indirectos mediante la modulación del microbioma o brotes desencadenados por infecciones, y ninguno está respaldado por los datos disponibles.

El puntaje alto (0,9902) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 65975 | MEIACT 400 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 65943 | MEIACT 200 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 65942 | SPECTRACEF 200 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 65973 | SPECTRACEF 400 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 27 interacciones, todas de nivel moderado (los datos compilados detallan 20). Las principales son:
  - Antiácidos y sales de magnesio, aluminio o calcio: hidróxido de aluminio, carbonato de calcio, magaldrato, carbonato de magnesio, hidróxido de magnesio, óxido de magnesio, citrato de sodio y bicarbonato de sodio.
  - Antagonistas H2: famotidina, ranitidina (incluida la de citrato de bismuto), cimetidina y nizatidina.
  - Inhibidores de la bomba de protones: omeprazol, esomeprazol, lansoprazol, dexlansoprazol, rabeprazol y pantoprazol.
  - Anticoagulante: dicumarol.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos clínicos ni publicaciones, y sin una plausibilidad mecanística documentada para la artritis reumatoide. Además, faltan los datos de advertencias y contraindicaciones del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (indicaciones, advertencias y contraindicaciones).
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión de la literatura y de registros de ensayos sobre cefditoreno (o cefalosporinas) en artritis reumatoide.
- Evaluar estudios preclínicos que justifiquen una hipótesis inmunomoduladora o de microbioma antes de considerar estudios clínicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


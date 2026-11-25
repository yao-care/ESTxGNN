---
layout: default
title: Lomitapide
parent: Solo predicción del modelo (L5)
nav_order: 477
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-25
description: "Lomitapide: nueva indicación predicha, Macrotrombocitopenia con insuficiencia de la válvula mitral (nivel de evidencia L5). Indicación original: Hipercolesterolemia familiar homocigota (el texto de i…"
monitor_inn: "Lomitapide"
predicted_indications: ["marcothrombocytopenia with mitral valve insufficiency", "hereditary thrombocytopenia with normal platelets", "dense granule disease", "transient neonatal thrombocytopenia", "thrombocytopenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "platelet storage pool deficiency"]
---

# Lomitapide
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

## Lomitapida: De Hipercolesterolemia Familiar Homocigota a Macrotrombocitopenia con Insuficiencia de la Válvula Mitral
{: .text-alpha }

## Resumen en Una Frase

Lomitapida es un inhibidor de la proteína microsomal de transferencia de triglicéridos (MTP), utilizado originalmente para tratar la hipercolesterolemia familiar homocigota.
El modelo TxGNN predice que podría ser efectivo para **macrotrombocitopenia con insuficiencia de la válvula mitral**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipercolesterolemia familiar homocigota (el texto de indicación de las autorizaciones españolas no está disponible; se toma de la base de conocimiento del modelo) |
| Nueva Indicación Predicha | Macrotrombocitopenia con insuficiencia de la válvula mitral |
| Puntaje de Predicción TxGNN | 0.9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 3 de 4; autorizadas no comercializadas: 1) |
| Número de Autorizaciones | 4 (comercializadas: 3) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Lomitapida inhibe la proteína microsomal de transferencia de triglicéridos (MTP). Esta proteína es necesaria para ensamblar las lipoproteínas que contienen apoB (VLDL en el hígado y quilomicrones en el intestino). Al bloquearla, disminuyen el colesterol LDL y otras lipoproteínas aterogénicas. Este es el mecanismo que respalda su uso en la hipercolesterolemia familiar homocigota.

Con la información disponible, **la predicción no resulta mecanísticamente convincente**. No se ha identificado ningún vínculo biológico conocido entre la inhibición de la MTP y la producción de plaquetas o la patología de la válvula mitral. El puntaje alto (0.9992) proviene del modelo TxGNN (aprendizaje profundo) y probablemente refleja similitudes que el modelo aprendió entre enfermedades relacionadas, como otros trastornos plaquetarios raros, y no evidencia biológica ni un mecanismo real.

Hay además una consideración de seguridad: lomitapida tiene una advertencia de hepatotoxicidad y datos limitados en población pediátrica. Esto no favorece su uso en una enfermedad hematológica sin justificación biológica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 113851003 | LOJUXTA 20 MG CAPSULAS DURAS | CÁPSULA DURA | Chiesi Farmaceutici S.P.A. | Comercializada |
| 113851002 | LOJUXTA 10 MG CAPSULAS DURAS | CÁPSULA DURA | Chiesi Farmaceutici S.P.A. | Comercializada |
| 113851001 | LOJUXTA 5 MG CAPSULAS DURAS | CÁPSULA DURA | Chiesi Farmaceutici S.P.A. | Comercializada |
| 113851007 | LOJUXTA 2 MG CAPSULAS DURAS | CÁPSULA DURA | Chiesi Farmaceutici S.P.A. | Autorizada, no comercializada |

Se muestran las 4 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Todas las autorizaciones están vigentes y son de principio activo único. Los datos compilados no incluyen el texto de la indicación aprobada.

<!-- review:begin es-lic-20261125-lomitapide-1 -->

> **Corrección de revisión (2026-11-25)**: Texto original: "Las tres autorizaciones están vigentes y son de principio activo único." Corregido: desde el 2026-11-25 se incorporan a los datos las autorizaciones de CIMA (AEMPS) posteriores a marzo de 2026 (incluidas importaciones paralelas) con el mismo criterio de recogida; la frase ya no coincidía con ellas. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261125-lomitapide-1 -->

---

## Consideraciones de Seguridad

- **Advertencias Principales**: lomitapida tiene una advertencia de hepatotoxicidad (acumulación de grasa hepática y elevación de transaminasas). También se ha señalado un riesgo teratogénico y la escasez de datos pediátricos.
- **Interacciones Farmacológicas**: se registraron 100 interacciones. Entre las 20 principales analizadas:
  - **Gravedad mayor**: acarbosa, doxiciclina, pioglitazona, bupropión, aprepitant, tetraciclina, ácido quenodesoxicólico, claritromicina, minociclina, naltrexona, oxandrolona y oximetolona.
  - **Gravedad moderada**: ranitidina, loperamida, budesonida (incluida la nasal), cimetidina, saxagliptina, eliglustat y linagliptina.
  - Hay que prestar especial atención a los inhibidores de CYP3A4, como la claritromicina.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos clínicos ni literatura. Además, no existe un vínculo mecanístico plausible entre la inhibición de la MTP y la macrotrombocitopenia con insuficiencia mitral. Otras predicciones de la misma lista (trombocitopenia hereditaria, enfermedad de gránulos densos, trombastenia de Glanzmann, etc.) presentan el mismo problema.

La única predicción de la lista con evidencia real es la **hiperlipoproteinemia** (nivel L1, con varios ensayos de Fase 3 completados). Sin embargo, coincide en gran medida con la indicación original, por lo que confirma el uso existente y no constituye un reposicionamiento genuino.

**Para avanzar se necesita:**
- Una hipótesis biológica que conecte la inhibición de la MTP con la fisiología plaquetaria o valvular.
- Estudios preclínicos que respalden la hipótesis antes de plantear cualquier ensayo clínico.
- Obtener del prospecto de la AEMPS las advertencias y contraindicaciones oficiales, así como el texto de la indicación aprobada.
- Una evaluación del balance beneficio-riesgo, dado el perfil de hepatotoxicidad del fármaco.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-25 | «Las tres» → todas | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


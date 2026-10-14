---
layout: default
title: Lomitapide
parent: Solo predicción del modelo (L5)
nav_order: 477
evidence_level: L5
indication_count: 10
---

# Lomitapide
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

# Lomitapida: De Hipercolesterolemia Familiar Homocigota a Macrotrombocitopenia con Insuficiencia de la Válvula Mitral

## Resumen en Una Frase

Lomitapida es un inhibidor de la proteína microsomal de transferencia de triglicéridos (MTP), utilizado originalmente para tratar la hipercolesterolemia familiar homocigota.
El modelo TxGNN predice que podría ser efectivo para **macrotrombocitopenia con insuficiencia de la válvula mitral**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipercolesterolemia familiar homocigota (el texto de indicación de las autorizaciones españolas no está disponible; se toma de la base de conocimiento del modelo) |
| Nueva Indicación Predicha | Macrotrombocitopenia con insuficiencia de la válvula mitral |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Lomitapida inhibe la proteína microsomal de transferencia de triglicéridos (MTP). Esta proteína es necesaria para ensamblar las lipoproteínas que contienen apoB (VLDL en el hígado y quilomicrones en el intestino). Al bloquearla, disminuyen el colesterol LDL y otras lipoproteínas aterogénicas. Este es el mecanismo que respalda su uso en la hipercolesterolemia familiar homocigota.

Con la información disponible, **la predicción no resulta mecanísticamente convincente**. No se ha identificado ningún vínculo biológico conocido entre la inhibición de la MTP y la producción de plaquetas o la patología de la válvula mitral. El puntaje alto (0.999) probablemente refleja la similitud en el grafo de conocimiento con otros trastornos plaquetarios raros, y no un mecanismo real.

Hay además una consideración de seguridad: lomitapida tiene una advertencia de hepatotoxicidad y datos limitados en población pediátrica. Esto no favorece su uso en una enfermedad hematológica sin justificación biológica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 113851003 | LOJUXTA 20 MG CÁPSULAS DURAS | Cápsula dura | Chiesi Farmaceutici S.P.A. |
| 113851002 | LOJUXTA 10 MG CÁPSULAS DURAS | Cápsula dura | Chiesi Farmaceutici S.P.A. |
| 113851001 | LOJUXTA 5 MG CÁPSULAS DURAS | Cápsula dura | Chiesi Farmaceutici S.P.A. |

Las tres autorizaciones están vigentes y son de principio activo único. Los datos compilados no incluyen el texto de la indicación aprobada.

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Anakinra
parent: Solo predicción del modelo (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Anakinra: nueva indicación predicha, Mastocitoma extracutáneo (nivel de evidencia L5). Indicación original: Artritis reumatoide…"
monitor_inn: "ANAKINRA"
predicted_indications: ["extracutaneous mastocytoma", "hepatic infarction", "autosomal recessive familial Mediterranean fever", "aggressive systemic mastocytosis", "hepatic veno-occlusive disease", "peliosis hepatis", "oligoarticular juvenile idiopathic arthritis without anti-nuclear antibodies", "oligoarticular juvenile idiopathic arthritis with anti-nuclear antibodies", "pyogenic autoinflammatory syndrome", "unclassified autoinflammatory syndrome"]
---

# Anakinra
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

# Anakinra: De Artritis Reumatoide a Mastocitoma Extracutáneo

## Resumen en Una Frase

Anakinra es un antagonista recombinante del receptor de interleucina-1 (IL-1), utilizado originalmente para tratar la artritis reumatoide y síndromes autoinflamatorios como el síndrome periódico asociado a criopirina (CAPS) y el síndrome CINCA.
El modelo TxGNN predice que podría ser efectivo para **mastocitoma extracutáneo**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción concreta.
Entre las demás predicciones, la mejor respaldada por la literatura es el **síndrome autoinflamatorio piógeno (PAPA/PAPASH)**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis reumatoide, síndrome periódico asociado a criopirina (CAPS) y síndrome CINCA (según el grafo de conocimiento; el texto de indicación autorizado en AEMPS no está disponible) |
| Nueva Indicación Predicha | Mastocitoma extracutáneo |
| Puntaje de Predicción TxGNN | 99,93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

> **Nota:** La primera predicción (mastocitoma extracutáneo) solo cuenta con el respaldo del modelo. Las predicciones con evidencia más sólida se resumen más abajo, en la sección de conclusión.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, anakinra es un antagonista del receptor de IL-1 que bloquea la señalización de IL-1α e IL-1β, y su eficacia en enfermedades inflamatorias como la artritis reumatoide y los síndromes autoinflamatorios ha sido comprobada.

Para el mastocitoma extracutáneo, la IL-1 podría tener un papel teórico en la inflamación mediada por mastocitos. Sin embargo, no hay un vínculo directo documentado entre anakinra y esta enfermedad en los datos aportados. El puntaje alto del modelo (99,93%) refleja probablemente la cercanía en el grafo de conocimiento y no una señal terapéutica demostrada.

Cabe destacar que otras predicciones tienen una base mecanística mucho más sólida:
- **Fiebre mediterránea familiar (FMF) autosómica recesiva** (puntaje 99,89%): la hiperactivación del inflamasoma pirina genera exceso de IL-1β, que anakinra bloquea directamente. La literatura, sin embargo, se compone sobre todo de revisiones y series con canakinumab (otro bloqueador de IL-1), por lo que apoya un efecto de clase de forma indirecta.
- **Síndrome autoinflamatorio piógeno (PAPA/PAPASH)** (puntaje 99,83%): las mutaciones de PSTPIP1 provocan desregulación del inflamasoma y exceso de IL-1β. Existe una revisión exploratoria de 2023 y un caso con anakinra de 2024.
- **Síndrome autoinflamatorio no clasificado** (puntaje 99,81%): evidencia retrospectiva y de casos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para mastocitoma extracutáneo ni para las demás indicaciones predichas.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para mastocitoma extracutáneo.

Como referencia, estas son las publicaciones más relevantes de la indicación con mayor respaldo (síndrome autoinflamatorio piógeno, PAPA/PAPASH):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38259483](https://pubmed.ncbi.nlm.nih.gov/38259483/) | 2023 | Revisión sistemática (exploratoria) | Frontiers in Immunology | Revisión integral de la eficacia y seguridad de anakinra y canakinumab en enfermedades inflamatorias asociadas a PSTPIP1 |
| [39006661](https://pubmed.ncbi.nlm.nih.gov/39006661/) | 2024 | Reporte de caso y revisión | Cureus | Uso de anakinra en el espectro PAPASH (artritis piógena, acné, pioderma gangrenoso, hidradenitis supurativa) |
| [38006373](https://pubmed.ncbi.nlm.nih.gov/38006373/) | 2023 | Reporte de caso/Revisión | Acta Dermatovenerologica Croatica | Dificultades para lograr remisión a largo plazo en el síndrome PAPA |
| [24275598](https://pubmed.ncbi.nlm.nih.gov/24275598/) | 2013 | Revisión | Seminars in Immunology | El bloqueo de IL-1 en humanos para tratar diversas enfermedades inflamatorias |
| [21532836](https://pubmed.ncbi.nlm.nih.gov/21532836/) | 2010 | Revisión | Current Genomics | Características clínicas, moleculares y genéticas del síndrome PAPA; la sobreproducción de IL-1β es un rasgo molecular claro |
| [27448064](https://pubmed.ncbi.nlm.nih.gov/27448064/) | 2016 | Revisión | Der Hautarzt | Acné grave en enfermedades autoinflamatorias; anakinra usado en ciertos casos por la posible implicación de IL-1β |
| [34778321](https://pubmed.ncbi.nlm.nih.gov/34778321/) | 2021 | Reporte de caso y revisión | Frontiers in Medicine | Afectación renal en enfermedades asociadas a PSTPIP1 (PAID) |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 102203006 | KINERET 100 mg/0,67 ml solución inyectable en jeringa precargada (Swedish Orphan Biovitrum AB) | Solución inyectable | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 100 interacciones en total; en la muestra revisada destacan:
  - **Mayor:** deferiprona.
  - **Moderadas:** corticosteroides (hidrocortisona, betametasona, budesonida, dexametasona, prednisolona, prednisona, triamcinolona), simvastatina, anticoagulantes (apixabán, dicumarol, rivaroxabán) y radiofármacos/anticuerpos radiomarcados (ibritumomab tiuxetán, iobenguano I-131, tositumomab).
  - **Menores:** sales de zinc (acetato, gluconato, sulfato).

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold** (para mastocitoma extracutáneo)

**Justificación:**
La predicción de mastocitoma extracutáneo se basa únicamente en el modelo (nivel L5), sin ensayos ni literatura, y sin un mecanismo plausible documentado. Por ello no se recomienda avanzar con esta indicación.

**Indicaciones alternativas a priorizar:**
- **Síndrome autoinflamatorio piógeno (PAPA/PAPASH):** nivel L3, *Proceed with Guardrails*, solo en entornos especializados, individualizados y con seguimiento de la respuesta.
- **Fiebre mediterránea familiar:** nivel L4, pregunta de investigación; mecanismo sólido, pero evidencia indirecta (principalmente canakinumab).
- **Síndrome autoinflamatorio no clasificado:** nivel L3, pregunta de investigación; evidencia retrospectiva y de casos.
- Las predicciones de infarto hepático, enfermedad venooclusiva hepática, peliosis hepática, mastocitosis sistémica agresiva (los artículos recuperados tratan sobre el síndrome de Schnitzler, no sobre mastocitosis) y artritis idiopática juvenil oligoarticular tienen evidencia nula o indirecta (*Hold*).

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) de anakinra
- Advertencias y contraindicaciones del prospecto de AEMPS, así como el texto de la indicación autorizada
- Ensayos clínicos o estudios específicos con anakinra (no solo canakinumab) en las indicaciones priorizadas
- Evaluación de la compatibilidad de vía de administración y de la similitud con la indicación original
- Plan de monitoreo de seguridad, con especial atención a las interacciones con corticosteroides, anticoagulantes y deferiprona
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


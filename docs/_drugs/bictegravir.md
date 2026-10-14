---
layout: default
title: Bictegravir
parent: Evidencia moderada (L3-L4)
nav_order: 104
evidence_level: L4
indication_count: 3
---

# Bictegravir
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

# Bictegravir: De Infección por VIH a Infección por el Virus de la Inmunodeficiencia Simia

## Resumen en Una Frase

Bictegravir es un inhibidor de la integrasa del VIH-1 (INSTI), utilizado originalmente para el tratamiento de la infección por VIH y el SIDA.
El modelo TxGNN predice que podría ser efectivo para la **infección por el virus de la inmunodeficiencia simia (SIV)**,
con **0 ensayos clínicos** y **3 publicaciones** (todas preclínicas o mecanísticas) que respaldan esta dirección de forma limitada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH / SIDA (según el grafo de conocimiento; los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Infección por el virus de la inmunodeficiencia simia |
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, bictegravir es un inhibidor de la transferencia de cadena de la integrasa (INSTI) del VIH-1, y su eficacia en la infección por VIH está comprobada. Se comercializa en España como parte de la combinación Biktarvy (bictegravir/emtricitabina/tenofovir alafenamida).

El SIV y el VIH-1 son lentivirus estrechamente emparentados, y sus integrasas son estructural y funcionalmente similares. Por ello, el mecanismo de los INSTI podría trasladarse al SIV. Un estudio in vitro (PMID 28923862) describe actividad antiviral de bictegravir frente a variantes de SIVmac239 resistentes a INSTI, y un trabajo estructural (PMID 32506843) explica cómo los INSTI se unen a las integrasas de VIH y SIV.

Es importante matizar que la evidencia es únicamente preclínica y mecanística, no clínica en pacientes. El SIV infecta a primates no humanos, por lo que la relevancia clínica en humanos es limitada; su valor principal es como modelo preclínico para la investigación del VIH.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | Estudio antiviral in vitro / preclínico | Antimicrobial Agents and Chemotherapy | Actividad antiviral de bictegravir y cabotegravir frente a SIVmac239 y VIH-1 resistentes a inhibidores de integrasa |
| [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/) | 2021 | Revisión (biología estructural) | The FEBS Journal | Estructuras de intasomas de VIH/SIV que explican la unión de los INSTI y los mecanismos de escape viral; dolutegravir y bictegravir presentan alta barrera de resistencia |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Estudio preclínico en modelo animal | Frontiers in Immunology | Modelo de ratón humanizado de doble propósito para probar estrategias antivirales frente a SIV y VIH |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 181289001IP | BIKTARVY 50 MG/200 MG/25 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No especificada en los datos |
| 1181289001 | BIKTARVY 50 MG/200 MG/25 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No especificada en los datos |
| 181289001IP1 | BIKTARVY 50 MG/200 MG/25 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No especificada en los datos |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 81 interacciones; se muestran las principales de la lista disponible:
  - **Gravedad mayor**: antiácidos y suplementos con cationes polivalentes (hidróxido de aluminio, atapulgita, caolín, magaldrato, carbonato/cloruro/citrato de magnesio, sales de calcio como acetato, carbonato, citrato, gluconato, lactato, fosfato y glubionato) y hierro. Estos pueden reducir la absorción de bictegravir.
  - **Gravedad moderada**: aprepitant, claritromicina, dexametasona, eliglustat y fenilbutirato de glicerol.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia para SIV es solo preclínica y mecanística (L4), sin ensayos clínicos. Además, el SIV afecta a primates no humanos, por lo que la relevancia terapéutica en humanos es limitada y su valor se centra en la investigación del VIH. El puntaje alto de TxGNN (99.82%) es una predicción del modelo y no sustituye a la evidencia real.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de bictegravir
- Advertencias y contraindicaciones del prospecto de AEMPS, que son necesarias antes de cualquier cribado de seguridad
- Definir si el objetivo es un uso en modelos preclínicos de investigación (SIV/VIH) y no una indicación clínica humana
- Estudios in vivo en modelos animales que confirmen la eficacia frente a SIV

**Nota sobre otras predicciones:** el modelo también predijo el síndrome de inmunodeficiencia adquirida felina (nivel L5, sin evidencia y fuera del ámbito humano) y un trastorno del neurodesarrollo raro (nivel L5, sin vínculo mecanístico plausible, probable artefacto del grafo de conocimiento). Ambas se recomiendan en estado Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


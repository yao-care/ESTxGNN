---
layout: default
title: Toremifene
parent: Solo predicción del modelo (L5)
nav_order: 807
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Toremifene: nueva indicación predicha, Infección por VIH (nivel de evidencia L5). Indicación original: No disponible en los datos de la autorización (texto de indicación va…"
---

# Toremifene
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Toremifeno: De Cáncer de Mama (indicación original no registrada en la autorización) a Infección por VIH

## Resumen en Una Frase

Toremifeno es un modulador selectivo de los receptores de estrógenos, comercializado en España como FARESTON 60 mg comprimidos. Según la información conocida de la clase, se emplea en cáncer de mama, aunque el texto de indicación de la autorización no está disponible en los datos compilados.
El modelo TxGNN predice que podría ser efectivo para **infección por VIH**, pero actualmente solo hay **0 ensayos clínicos** y **1 publicación preclínica** (sobre criptococosis) que se relacionan indirectamente con esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de la autorización (texto de indicación vacío) |
| Nueva Indicación Predicha | Infección por VIH |
| Puntaje de Predicción TxGNN | 99.41% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, toremifeno es un antagonista/modulador de receptores de estrógenos de la misma familia que el tamoxifeno, y su eficacia en cáncer de mama hormonodependiente está establecida. Mecanísticamente, su aplicabilidad a VIH no está demostrada.

La única publicación disponible (PMID 24520056, 2014) describe que los antagonistas de receptores de estrógenos, incluidos tamoxifeno y toremifeno, son fungicidas frente a *Cryptococcus*, se unen a proteínas con dominio EF-hand (como la calmodulina) y presentan sinergia con fluconazol y anfotericina B in vitro. La criptococosis es una infección oportunista importante en personas con VIH avanzado, por lo que el vínculo con VIH es **indirecto**: apuntaría, en todo caso, a un posible adyuvante frente a una infección oportunista asociada, no a una actividad antiviral contra el VIH.

La alta puntuación de TxGNN (0,994) proviene de una predicción basada en grafos de conocimiento y no constituye por sí misma evidencia clínica. Los datos compilados no establecen ningún mecanismo de acción antiviral directa.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24520056](https://pubmed.ncbi.nlm.nih.gov/24520056/) | 2014 | Estudio preclínico (in vitro / animal) | mBio | Los antagonistas de receptores de estrógenos relacionados con tamoxifeno y toremifeno son fungicidas frente a *Cryptococcus*, se unen a proteínas EF-hand y presentan sinergia con fluconazol y anfotericina B |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 96004001 | FARESTON 60 mg COMPRIMIDOS | Comprimido | No disponible en los datos compilados |
| 96004002 | FARESTON 60 mg COMPRIMIDOS | Comprimido | No disponible en los datos compilados |

Ambas autorizaciones están vigentes, son de monofármaco y su titular es Orion Corporation.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia hormonal (modulador selectivo de receptores de estrógenos); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Bajo; no obstante, el grafo de conocimiento asocia el fármaco con leucopenia y trombocitopenia, por lo que conviene vigilarlas |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Hemograma, función hepática, calcemia, electrolitos (potasio) y ECG (intervalo QT) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento (no proceden del prospecto)**: síndrome de QT largo (incluido el familiar), torsades de pointes, trombocitopenia, déficit de potasio, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, leucopenia e hiperplasia endometrial.
- **Interacciones farmacológicas**: se identificaron 350 interacciones. Entre las de nivel **mayor** figuran dexametasona, claritromicina, levofloxacino, dolasetrón, palonosetrón, ácido picosulfúrico, polietilenglicol 3350 con electrolitos y sulfato de sodio. Entre las de nivel moderado figuran famotidina, cimetidina, pioglitazona, loperamida, aprepitant, bisacodilo, metreleptina, miconazol, nateglinida, lactitol y lactulosa. Metronidazol es de nivel menor.
- **Relevancia para VIH**: el elevado número de interacciones sugiere un riesgo sustancial con regímenes antirretrovirales (sustratos o inhibidores de CYP3A4 y fármacos que prolongan el QT).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (L5) y en un estudio preclínico sobre criptococosis, sin ensayos clínicos ni evidencia de actividad antiviral contra el VIH. Además, el riesgo de interacciones y de prolongación del QT es relevante en pacientes con tratamiento antirretroviral.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (advertencias y contraindicaciones) y la indicación autorizada, actualmente ausentes.
- Completar los datos del mecanismo de acción (por ejemplo, mediante DrugBank).
- Estudios in vitro de actividad anti-VIH, o bien reformular la hipótesis hacia infecciones oportunistas asociadas (criptococosis).
- Análisis detallado de interacciones con antirretrovirales y evaluación del riesgo de QT.
- Revisión de la relevancia de las contraindicaciones del grafo de conocimiento frente a la información oficial del prospecto.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


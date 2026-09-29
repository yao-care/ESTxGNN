---
layout: default
title: Prasugrel
parent: Solo predicción del modelo (L5)
nav_order: 433
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

# Prasugrel: De Inhibidor Plaquetario P2Y12 a Hipertensión Pulmonar

## Resumen en Una Frase

Prasugrel es un antiagregante plaquetario de la familia de las tienopiridinas (inhibidor del receptor P2Y12).
El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar**, pero la evidencia es muy débil: aunque se recuperaron **2 ensayos clínicos** y **2 publicaciones**, ninguno estudia prasugrel ni la hipertensión pulmonar, por lo que la predicción sigue siendo solo teórica.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Hipertensión pulmonar |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, prasugrel es una tienopiridina que bloquea el receptor plaquetario P2Y12 y reduce la agregación de las plaquetas. Su uso establecido está en la prevención de eventos trombóticos.

La activación plaquetaria y la trombosis in situ participan en algunas formas de hipertensión pulmonar. Por eso, mecanísticamente, un antiagregante podría tener un papel teórico en esta enfermedad.

Este vínculo es solo una hipótesis. No hay datos específicos de prasugrel que la respalden, y la puntuación alta de TxGNN es únicamente una predicción computacional.

## Evidencia de Ensayos Clínicos

Los dos ensayos recuperados fueron valorados como poco relevantes: no involucran prasugrel ni hipertensión pulmonar.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Completado | 300 | Estudio retrospectivo multicéntrico sobre la proporción de pacientes con trombosis asociada a cáncer que no serían elegibles para un estudio como CARAVAGGIO. No guarda relación con prasugrel ni con hipertensión pulmonar. |
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Completado | 500 | Estudio observacional transversal sobre el manejo de anticoagulantes orales no antagonistas de la vitamina K en ancianos con fibrilación auricular no valvular en España. No guarda relación con prasugrel ni con hipertensión pulmonar. |

## Evidencia de Literatura

Ambas publicaciones son estudios de cohorte y tampoco aportan evidencia directa.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohorte | Kardiologiia | Análisis del registro ACTIVE (más de 5.800 pacientes con COVID-19) sobre cómo influye el tratamiento previo de enfermedades cardiovasculares y otras comorbilidades en la gravedad y el desenlace de la infección. |
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohorte | Current Medical Research and Opinion | Factores asociados al uso, la adherencia y la persistencia de clopidogrel en pacientes con síndrome coronario agudo sometidos a intervención coronaria percutánea. |

## Información de Mercado en España

Prasugrel tiene 20 autorizaciones en España. Estas son las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 83790 | Prasugrel Swanpond Investments 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 83730 | Prasugrel Lesvi 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 08503009IP3 | Efient 10 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 83098 | Prasugrel Stada 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 82930 | Prasugrel Teva 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de hipertensión pulmonar se apoya solo en el modelo (nivel L5). Ningún ensayo ni publicación recuperados estudia prasugrel en esta enfermedad, y el vínculo con la trombosis in situ es únicamente teórico.

**Para avanzar se necesita:**
- Estudios preclínicos o clínicos que evalúen prasugrel o inhibidores P2Y12 en hipertensión pulmonar.
- Datos detallados del mecanismo de acción (MOA) desde DrugBank.
- Advertencias y contraindicaciones del prospecto de la AEMPS para el cribado de seguridad, con especial atención al riesgo de sangrado en una población no cardíaca.

**Otras predicciones del modelo:** la mejor respaldada es la **migraña** (puntaje TxGNN 99.88%, nivel L3, decisión "Research Question"). Existe una revisión retrospectiva de tienopiridinas en pacientes con migraña y foramen oval permeable, además de un piloto con ticagrelor, otro inhibidor P2Y12. Como línea de investigación, merece más atención que la hipertensión pulmonar. El resto de predicciones (por ejemplo, artritis reumatoide o lepra) están en nivel L5 y no tienen evidencia.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


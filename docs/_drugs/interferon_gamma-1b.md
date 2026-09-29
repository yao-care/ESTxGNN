---
layout: default
title: Interferon Gamma-1B
parent: Evidencia moderada (L3-L4)
nav_order: 287
evidence_level: L4
indication_count: 10
---

# Interferon Gamma-1B
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Interferón gamma-1b: De Enfermedad Granulomatosa a Cardiopatía

## Resumen en Una Frase

Interferón gamma-1b (Imukin) es una citoquina recombinante inmunomoduladora. Uno de los ensayos del paquete de evidencia lo describe como fármaco aprobado para la enfermedad granulomatosa, pero la ficha de AEMPS del paquete no recoge la indicación.
El modelo TxGNN predice que podría ser efectivo para **cardiopatía**, con una puntuación muy alta.
Sin embargo, **ningún ensayo clínico** prueba este fármaco en enfermedad cardíaca, y la literatura se limita a **reportes de caso** en los que el objetivo era una infección subyacente.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de AEMPS del paquete (el texto de indicación está vacío). Un ensayo del paquete lo describe como aprobado para enfermedad granulomatosa |
| Nueva Indicación Predicha | Cardiopatía |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, el interferón gamma es una citoquina que regula la respuesta inmunitaria y la inflamación. Su eficacia clínica se ha descrito en enfermedades con defecto inmunitario, como la enfermedad granulomatosa.

La señalización de IFN-gamma podría influir en la inflamación cardíaca o en complicaciones cardíacas de origen infeccioso, y esto es lo que daría cierta plausibilidad a la predicción. Pero es solo una hipótesis: los datos disponibles no dan apoyo directo.

Lo único cercano al ámbito cardíaco son reportes de caso. En ellos se habría usado IFN-gamma como inmunoterapia adyuvante en una endocarditis protésica por *M. chimaera* y en una pericarditis por *Aspergillus* en un niño con enfermedad granulomatosa crónica. En ambos casos el objetivo era la infección o la inmunodeficiencia de fondo, no la cardiopatía. La puntuación alta del modelo, por tanto, no equivale a evidencia terapéutica.

## Evidencia de Ensayos Clínicos

Se recuperaron 47 ensayos, casi todos sin relación con el fármaco (ejercicio, vacunas, otros medicamentos). Ninguno evalúa interferón gamma-1b en cardiopatía. Se muestran los más cercanos al fármaco o a la vía del IFN-gamma:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00021567](https://clinicaltrials.gov/study/NCT00021567) | Fase 2 | Completado | 20 | IFN gamma-1b inhalado más antibióticos frente a placebo en infección pulmonar por *Mycobacterium avium*. No es un ensayo cardíaco |
| [NCT03888664](https://clinicaltrials.gov/study/NCT03888664) | Fase 2 | Completado | 12 | Estudio piloto abierto de seguridad y eficacia de IFN gamma en ataxia de Friedreich. No es un ensayo cardíaco |
| [NCT07538336](https://clinicaltrials.gov/study/NCT07538336) | Fase 2 | Aún no recluta | 40 | Emapalumab (anti-IFN gamma) en disfunción aguda del aloinjerto pulmonar. Fármaco distinto, bloquea la vía |
| [NCT06996119](https://clinicaltrials.gov/study/NCT06996119) | Fase 1 | Aún no recluta | 15 | Emapalumab con ciclofosfamida postrasplante para prevenir la enfermedad injerto contra huésped. Fármaco distinto |
| [NCT06634108](https://clinicaltrials.gov/study/NCT06634108) | Fase 1/2 | Reclutando | 20 | Genisteína en inflamación de la insuficiencia cardíaca por amiloidosis TTR. Contexto cardíaco, pero sin interferón |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37180421](https://pubmed.ncbi.nlm.nih.gov/37180421/) | 2022 | Revisión sistemática | Ther Adv Rare Dis | Revisión de intervenciones evaluadas en ataxia de Friedreich. Relación indirecta con el fármaco |
| [31020218](https://pubmed.ncbi.nlm.nih.gov/31020218/) | 2018 | Reporte de caso | Eur Heart J Case Rep | Endocarditis protésica por *M. chimaera* tras cirugía cardíaca, primer caso español. El objetivo fue la infección, no la cardiopatía |
| [29456196](https://pubmed.ncbi.nlm.nih.gov/29456196/) | 2018 | Reporte de caso | J Cyst Fibros | Mejoría de la persistencia de *Exophiala dermatitidis* y del deterioro respiratorio con IFN-gamma en fibrosis quística |
| [28990950](https://pubmed.ncbi.nlm.nih.gov/28990950/) | 2017 | Reporte de caso | Turk Kardiyol Dern Ars | Pericarditis constrictiva por *Aspergillus* en una niña con enfermedad granulomatosa crónica |
| [21131468](https://pubmed.ncbi.nlm.nih.gov/21131468/) | 2011 | Cohorte | Am J Respir Crit Care Med | Validación de la prueba de marcha de 6 minutos en fibrosis pulmonar idiopática. No evalúa cardiopatía |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 60113 | IMUKIN 100 microgramos SOLUCIÓN INYECTABLE | Solución inyectable | Clinigen Healthcare B.V. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La puntuación TxGNN es muy alta (99.99%), pero no hay ningún ensayo que pruebe el fármaco en cardiopatía. Los únicos indicios son reportes de caso en los que el fármaco trataba una infección o una inmunodeficiencia, por lo que la evidencia se queda en L4.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de AEMPS (advertencias y contraindicaciones), porque sin ello no se puede pasar al cribado de seguridad
- Confirmar la indicación aprobada y el mecanismo de acción del fármaco (por ejemplo, vía DrugBank)
- Definir qué cardiopatía concreta se apunta (inflamatoria, infecciosa u otra), ya que "cardiopatía" es demasiado amplio
- Buscar estudios preclínicos o de mecanismo que vinculen la señalización de IFN-gamma con esa condición cardíaca
- Como referencia, el resto de las predicciones del modelo son todas de nivel L5, salvo el rango 5 (trastorno de síntesis de fucoglicanos, L4), y tampoco tienen apoyo directo

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


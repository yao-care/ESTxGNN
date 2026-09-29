---
layout: default
title: Ribociclib
parent: Evidencia moderada (L3-L4)
nav_order: 466
evidence_level: L4
indication_count: 4
---

# Ribociclib
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **4** 
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

# Ribociclib: De Cáncer de Mama HR+/HER2- a Leucemia Mieloide

## Resumen en Una Frase

Ribociclib es un inhibidor de CDK4/6, comercializado en España como Kisqali y utilizado en el cáncer de mama avanzado con receptores hormonales positivos y HER2 negativo (HR+/HER2-).
El modelo TxGNN predice que podría ser efectivo para **leucemia mieloide**, pero **no hay ensayos clínicos registrados** y solo hay **2 publicaciones relevantes** (un estudio in vitro y un reporte de caso que sugiere un riesgo, no un beneficio).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de mama HR+/HER2- (deducido de los ensayos y la literatura del pack; el texto de indicación de las autorizaciones AEMPS viene vacío) |
| Nueva Indicación Predicha | Leucemia mieloide |
| Puntaje de Predicción TxGNN | 99,35% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Ribociclib inhibe las quinasas dependientes de ciclina 4 y 6 (CDK4/6), que controlan el paso del ciclo celular de la fase G1 a la fase S. Al bloquearlas, detiene la proliferación de células tumorales. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el pack de evidencia, por lo que este razonamiento se basa en el conocimiento general de la clase.

Mecanísticamente, una proliferación dependiente del ciclo celular en los blastos mieloides podría ser sensible a la inhibición de CDK4/6. Es una hipótesis plausible, pero indirecta. La única evidencia específica es un estudio in vitro que explora los inhibidores de CDK4/6 frente a la resistencia farmacocinética en células de leucemia mieloide aguda (LMA).

Además, hay una señal de alerta. Un reporte de caso describe una LMA con eosinofilia surgida tras el tratamiento con un inhibidor de CDK4/6, en un paciente con hematopoyesis clonal de potencial indeterminado. Esto apunta a una posible preocupación de seguridad, no a un beneficio terapéutico. El puntaje alto de TxGNN es solo una predicción computacional.

Las otras predicciones del modelo (trombocitopenia y dos trastornos hereditarios de plaquetas) parecen reflejar efectos adversos hematológicos del fármaco, no oportunidades terapéuticas. No se desarrollan aquí.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32560251](https://pubmed.ncbi.nlm.nih.gov/32560251/) | 2020 | Preclínico (in vitro) | Cancers | Explora los inhibidores de CDK4/6 para superar la resistencia farmacocinética (transportadores ABCB1/ABCG2 y enzimas reductoras de carbonilo) en células de LMA |
| [30575100](https://pubmed.ncbi.nlm.nih.gov/30575100/) | 2019 | Reporte de caso | American Journal of Hematology | LMA con eosinofilia tras tratamiento con inhibidor de CDK4/6, atribuida a hematopoyesis clonal subyacente; señal de seguridad, no de eficacia |

Se excluyó un tercer resultado (PMID 41641105, adenocarcinoma vulvar) por no guardar relación con la leucemia mieloide.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 1171221005IP | KISQALI 200 MG comprimidos recubiertos con película | Comprimido recubierto con película | Novartis Europharm Limited |
| 1171221001IP1 | KISQALI 200 MG comprimidos recubiertos con película | Comprimido recubierto con película | Novartis Europharm Limited |
| 1171221001 | KISQALI 200 MG comprimidos recubiertos con película | Comprimido recubierto con película | Novartis Europharm Limited |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de quinasas CDK4/6) |
| Riesgo de Mielosupresión | Medio a alto. La literatura del pack describe mielosupresión (neutropenia, leucopenia, trombocitopenia, anemia) como toxicidad frecuente de los inhibidores de CDK4/6 |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial; función hepática y renal |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Señales de la literatura**: la mielosupresión es la toxicidad más documentada de la clase (metaanálisis de toxicidad hematológica y estudios de farmacovigilancia). Existe además un reporte de LMA con eosinofilia tras un inhibidor de CDK4/6.

Consultar el prospecto para información de seguridad sobre advertencias, contraindicaciones e interacciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en un puntaje del modelo, un estudio in vitro y un reporte de caso que apunta a un posible riesgo hematológico. No hay ensayos clínicos, y la mielosupresión propia del fármaco es una preocupación en un contexto de leucemia.

**Para avanzar se necesita:**
- Estudios preclínicos adicionales (in vitro e in vivo) de ribociclib en modelos de leucemia mieloide, con análisis de dependencia de Rb y CDK4/6
- Datos detallados del mecanismo de acción (MOA)
- Advertencias y contraindicaciones del prospecto de AEMPS
- Evaluación de la señal de seguridad hematológica, incluido el caso de LMA con eosinofilia
- Evidencia de ensayos clínicos, hoy inexistentes

*Los resultados son solo de referencia para investigación y no constituyen consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


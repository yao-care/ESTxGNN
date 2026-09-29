---
layout: default
title: Oxybutynin
parent: Solo predicción del modelo (L5)
nav_order: 399
evidence_level: L5
indication_count: 3
---

# Oxybutynin
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

# Oxybutynin: De Vejiga Hiperactiva a Síndrome de Piernas Inquietas

## Resumen en Una Frase

Oxybutynin es un antimuscarínico utilizado originalmente para tratar la vejiga hiperactiva.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de piernas inquietas**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, así que es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Vejiga hiperactiva (según la información farmacológica de la ficha del fármaco; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Síndrome de piernas inquietas |
| Puntaje de Predicción TxGNN | 99.74% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Oxybutynin actúa sobre los receptores muscarínicos humanos M1, M2, M3, M4 y M5 (genes CHRM1 a CHRM5). Es un antimuscarínico con acción antiespasmódica sobre el músculo liso, y su uso establecido es la vejiga hiperactiva. Los datos recibidos no incluyen una descripción detallada del mecanismo de acción.

**En este caso no se identifica una justificación mecanística sólida.** El síndrome de piernas inquietas se relaciona principalmente con la deficiencia de hierro cerebral y la disfunción dopaminérgica, y oxybutynin no actúa sobre esas vías. El puntaje alto de TxGNN (0.997) proviene solo del grafo de conocimiento y no está respaldado por ningún estudio en los datos disponibles.

Además, los efectos anticolinérgicos centrales podrían empeorar el sueño o los síntomas sensoriales, por lo que la dirección del efecto es incierta. Por eso se recomienda tratar esta predicción con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 57185 | DITROPAN 5 mg COMPRIMIDOS | Comprimido | Cheplapharm Arzneimittel GmbH |
| 03270001 | KENTERA 3,9 mg/24 HORAS, PARCHE TRANSDÉRMICO | Parche transdérmico | Teva B.V. |
| 85899 | VESOXX 1 MG/ML SOLUCIÓN INTRAVESICAL | Solución intravesical | Farco-Pharma GmbH |
| 62205 | DRESPLAN COMPRIMIDOS | Comprimido | Macure Healthcare Limited |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: no hay datos de interacciones fármaco-fármaco. Los 5 registros consultados corresponden a las dianas farmacológicas de oxybutynin (receptores muscarínicos M1 a M5).
- **Señal de seguridad relevante**: los efectos anticolinérgicos podrían empeorar el sueño o los síntomas sensoriales en el síndrome de piernas inquietas, según el análisis del modelo. Un caso publicado de esofagitis por reflujo asociado a oxybutynin (PMID 2360335) muestra un efecto adverso digestivo de este fármaco, aunque no se refiere a esta indicación.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5), sin ensayos ni literatura, y no tiene un vínculo mecanístico plausible con la fisiopatología del síndrome de piernas inquietas. Además, existe riesgo de que los efectos anticolinérgicos centrales empeoren los síntomas.

**Para avanzar se necesita:**
- Buscar y revisar estudios clínicos o preclínicos que relacionen antimuscarínicos con el síndrome de piernas inquietas.
- Obtener las advertencias y contraindicaciones del prospecto de la AEMPS, que es un paso bloqueante para la evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Valorar otras predicciones del mismo fármaco. Para la enfermedad ulcerosa péptica hay 3 publicaciones históricas (nivel L4), pero son antiguas y una de ellas describe un efecto adverso digestivo; para la gastroduodenitis no hay evidencia (L5). Ambas siguen en Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


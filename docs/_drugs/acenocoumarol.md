---
layout: default
title: Acenocoumarol
parent: Solo predicción del modelo (L5)
nav_order: 15
evidence_level: L5
indication_count: 3
---

# Acenocoumarol
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

# Acenocumarol: De Embolia Pulmonar y Trombofilia a Deficiencia de Cofactor II de la Heparina

## Resumen en Una Frase

Acenocumarol es un anticoagulante antagonista de la vitamina K, utilizado originalmente para la embolia pulmonar y la trombofilia.
El modelo TxGNN predice que podría ser efectivo para la **deficiencia de cofactor II de la heparina**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Embolia pulmonar y trombofilia (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Deficiencia de cofactor II de la heparina |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Acenocumarol es un antagonista de la vitamina K que inhibe VKORC1 y reduce la síntesis de los factores de coagulación dependientes de vitamina K (II, VII, IX y X) y de las proteínas C y S. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción; esta descripción procede del conocimiento farmacológico general del fármaco.

La deficiencia de cofactor II de la heparina es una trombofilia hereditaria en la que se pierde parte de la inhibición de la trombina. Una posible vía es que, al disminuir la generación de trombina mediante la depleción de factores, se compense la ausencia de este inhibidor. Esto es coherente con las indicaciones originales del fármaco (trombofilia y embolia pulmonar).

Esta relación es una inferencia basada en la farmacología y en la predicción del modelo. El puntaje elevado (99.84%) es una predicción computacional, no evidencia clínica.

### Otras predicciones del modelo

| Posición | Indicación predicha | Puntaje TxGNN | Nivel de Evidencia | Recomendación |
|------|------|------|------|------|
| 2 | Exceso de factor V con trombosis espontánea | 99.78% | L5 | Hold |
| 3 | Deficiencia de antitrombina tipo 2 | 99.77% | L5 | Hold |

- **Exceso de factor V:** el factor V no depende de la vitamina K, por lo que el beneficio sería indirecto (menor generación global de trombina).
- **Deficiencia de antitrombina tipo 2:** acenocumarol reduce los factores II y X, principales dianas de la antitrombina. Habría que revisar por separado la resistencia a la heparina y la necesidad de tratamiento puente inicial.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 58994 | SINTROM 1 mg COMPRIMIDOS | Comprimido | No disponible en los datos compilados |
| 88278 | ACENOCUMAROL AUROVITAS 1 MG COMPRIMIDOS EFG | Comprimido | No disponible en los datos compilados |
| 88315 | ACENOCUMAROL AUROVITAS 4 MG COMPRIMIDOS EFG | Comprimido | No disponible en los datos compilados |
| 25670 | SINTROM 4 mg COMPRIMIDOS | Comprimido | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 117 interacciones potenciales, todas sin nivel de gravedad clasificado. Entre las primeras listadas figuran: calcitriol, pantoprazol, morfina, metformina, omeprazol, lansoprazol, vancomicina, prednisona, hidrocortisona, cloruro de potasio, prednisolona, ranitidina, metronidazol, ácido acetilsalicílico, budesonida, dexametasona, rosiglitazona, lactulosa, simvastatina y rosuvastatina.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo TxGNN y en un razonamiento mecanístico, sin ensayos clínicos ni literatura (nivel L5). Además, faltan los datos de advertencias y contraindicaciones del prospecto, necesarios para el cribado de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas)
- Completar los datos del mecanismo de acción desde DrugBank
- Buscar ensayos clínicos y literatura específicos para la deficiencia de cofactor II de la heparina
- Evaluar la gravedad de las interacciones farmacológicas, dado el estrecho margen terapéutico de los antagonistas de la vitamina K
- Revisar la compatibilidad de vía de administración y la similitud con la indicación original
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


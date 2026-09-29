---
layout: default
title: Ioversol
parent: Solo predicción del modelo (L5)
nav_order: 290
evidence_level: L5
indication_count: 10
---

# Ioversol
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

# Ioversol: De Medio de Contraste Radiográfico a Susceptibilidad a la Osteoartritis

## Resumen en Una Frase

Ioversol es un medio de contraste radiográfico yodado no iónico, utilizado originalmente para obtener imágenes diagnósticas.
El modelo TxGNN predice que podría ser efectivo para **susceptibilidad a la osteoartritis**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción. Es una señal puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Medio de contraste radiográfico yodado no iónico (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Susceptibilidad a la osteoartritis |
| Puntaje de Predicción TxGNN | 99.67% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, ioversol es un contraste yodado no iónico. Su función es atenuar los rayos X para visualizar estructuras vasculares y tisulares, no modificar la biología de una enfermedad.

Por eso, **no se identifica un vínculo mecanístico** con la susceptibilidad genética a la osteoartritis. Ioversol no tiene acción antiinflamatoria ni condroprotectora conocida. El puntaje alto (99.67%) parece un artefacto del grafo de conocimiento y no refleja una relación farmacológica real.

Existe un contexto cercano en la segunda predicción del modelo, **osteoartritis** (99.63%). Los ensayos relacionados estudian la embolización de arterias geniculares (GAE) o la embolización con Lipiodol, un aceite yodado distinto. El posible beneficio en el dolor proviene del procedimiento de embolización. Como máximo, ioversol podría usarse como contraste para guiar la angiografía, y no es el agente evaluado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la susceptibilidad a la osteoartritis.

Como contexto, estos son los ensayos de la predicción vecina "osteoartritis". Ninguno evalúa ioversol como intervención terapéutica:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06497140](https://clinicaltrials.gov/study/NCT06497140) | Fase 3 | Reclutando | 130 | Embolización de arterias geniculares vs. simulacro en osteoartritis sintomática de rodilla |
| [NCT06859164](https://clinicaltrials.gov/study/NCT06859164) | Fase 2 | Reclutando | 50 | Estudio piloto aleatorizado de GAE vs. simulacro para el dolor de rodilla |
| [NCT06611007](https://clinicaltrials.gov/study/NCT06611007) | Fase 1/2 | Reclutando | 15 | Seguridad de la embolización con Lipiodol en osteoartritis digital refractaria |
| [NCT04733092](https://clinicaltrials.gov/study/NCT04733092) | Fase 1 | Completado | 22 | Emulsión de Lipiodol para embolizar hipervascularización inflamatoria en dolor de rodilla |

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la susceptibilidad a la osteoartritis.

Como contexto, la predicción vecina "osteoartritis" cuenta con un estudio, que tampoco evalúa ioversol:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | Ensayo prospectivo de un solo brazo | Diagnostic and Interventional Imaging | Ensayo LipioJoint-1: seguridad y eficacia de la embolización transitoria de arterias geniculares con una emulsión de aceite etiodizado en osteoartritis de rodilla |

## Información de Mercado en España

Se muestran 5 de las 8 autorizaciones. Ninguna incluye texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 60713 | OPTIRAY ULTRAJECT 240 mg/ml solución inyectable | Solución inyectable | Guerbet |
| 62068 | OPTIRAY 300 mg/ml solución inyectable | Solución inyectable | Guerbet |
| 58468 | OPTIRAY 240 mg/ml solución inyectable | Solución inyectable | Guerbet |
| 62069 | OPTIRAY 350 mg/ml solución inyectable | Solución inyectable | Guerbet |
| 62067 | OPTIRAY ULTRAJECT 350 mg/ml solución inyectable | Solución inyectable | Guerbet |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en las fuentes consultadas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos, literatura ni un mecanismo plausible (nivel L5). Ioversol es un agente de imagen sin efecto conocido sobre la susceptibilidad a la osteoartritis. Los ensayos de embolización cercanos evalúan un procedimiento, no este fármaco.

**Para avanzar se necesita:**
- Datos del mecanismo de acción que justifiquen un efecto biológico real, algo poco probable en un contraste yodado
- Ficha técnica de la AEMPS con advertencias y contraindicaciones para completar el cribado de seguridad
- Evidencia preclínica o clínica que evalúe ioversol como intervención, y no solo como guía de imagen
- Revisión de las siguientes predicciones del modelo. Varias no tienen evidencia, y otras son contextos de seguridad diagnóstica (por ejemplo, contraste yodado en enfermedad de células falciformes) sin valor terapéutico
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


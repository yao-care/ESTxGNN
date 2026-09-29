---
layout: default
title: Raloxifene
parent: Solo predicción del modelo (L5)
nav_order: 451
evidence_level: L5
indication_count: 4
---

# Raloxifene
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Raloxifeno: De Osteoporosis Posmenopáusica a Úlcera Duodenal

## Resumen en Una Frase

El raloxifeno es un modulador selectivo de los receptores de estrógenos, utilizado para prevenir y tratar la osteoporosis en mujeres posmenopáusicas y para reducir la incidencia de cáncer de mama invasivo en mujeres con alto riesgo.
El modelo TxGNN predice que podría ser efectivo para la **úlcera duodenal**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Osteoporosis posmenopáusica (según datos farmacológicos; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Úlcera duodenal |
| Puntaje de Predicción TxGNN | 99,72 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 15 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el campo específico del fármaco. Según la información farmacológica disponible, el raloxifeno se une a los receptores de estrógenos alfa (ESR1) y beta (ESR2), al receptor acoplado a proteína G GPER1 y es sustrato de la aldehído oxidasa 1 (AOX1). Su eficacia en osteoporosis posmenopáusica está establecida.

La relación con la úlcera duodenal es, por ahora, **especulativa**. Una posible vía sería la señalización de receptores de estrógenos en la protección de la mucosa gastroduodenal, pero ningún dato aportado la respalda. El puntaje alto del modelo probablemente refleja cercanía en el grafo de conocimiento y no un efecto farmacológico demostrado. Debe tratarse como una hipótesis para generar ideas, no como un hallazgo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 15 autorizaciones. El registro no incluye el texto de la indicación aprobada para ninguna de ellas.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 87122 | Raloxifeno Cinfamed 60 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 76962 | Raloxifeno Tarbis 60 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 75525 | Raloxifeno Kern Pharma 60 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 98073003 | Evista 60 mg comprimidos recubiertos con película | Comprimido recubierto |
| 82373 | Raloxifeno Aurovitas 60 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos ni literatura, y no hay un mecanismo plausible respaldado por los datos. Las otras tres predicciones (hipoalfalipoproteinemia, obstrucción duodenal y reflujo duodenogástrico, todas con puntaje cercano al 99,6 %) tampoco tienen evidencia.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), necesario antes de cualquier evaluación de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Realizar una búsqueda sistemática de literatura y ensayos sobre raloxifeno y patología gastroduodenal
- Evaluar la plausibilidad mecanística de la vía de receptores de estrógenos en la mucosa duodenal con estudios preclínicos

*Este informe es solo para fines de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


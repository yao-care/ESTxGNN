---
layout: default
title: Raloxifene
parent: Solo predicción del modelo (L5)
nav_order: 677
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Raloxifene: nueva indicación predicha, Úlcera duodenal (nivel de evidencia L5). Indicación original: Osteoporosis posmenopáusica (según las relaciones de indicación del g…"
monitor_inn: "Raloxifene"
predicted_indications: ["duodenal ulcer (disease)", "hypoalphalipoproteinemia", "duodenal obstruction", "duodenogastric reflux"]
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

# Raloxifeno: De Osteoporosis Posmenopáusica a Úlcera Duodenal

## Resumen en Una Frase

Raloxifeno es un modulador selectivo de los receptores de estrógenos (SERM), utilizado originalmente para el tratamiento de la osteoporosis posmenopáusica.
El modelo TxGNN predice que podría ser efectivo para **úlcera duodenal**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Osteoporosis posmenopáusica (según las relaciones de indicación del grafo de conocimiento, ya que los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Úlcera duodenal |
| Puntaje de Predicción TxGNN | 99.72% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 15 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción dentro de los datos compilados para este informe. Según la información conocida, raloxifeno es un SERM que interactúa con los receptores de estrógenos alfa (ESR1) y beta (ESR2), además del receptor acoplado a proteína G GPER1. También figura como sustrato de la aldehído oxidasa 1 (AOX1). Su eficacia en la osteoporosis posmenopáusica está bien establecida.

Sin embargo, **los datos no respaldan un vínculo mecanístico claro** con la úlcera duodenal. No se identifica una vía establecida hacia su fisiopatología (infección por *H. pylori*, secreción ácida, lesión por AINE). El puntaje alto del modelo (99.72%) refleja una predicción basada en el grafo de conocimiento, no una relación terapéutica verificada. La similitud con la indicación original está pendiente de evaluación.

Por ello, esta predicción debe considerarse una hipótesis exploratoria. Entre las otras predicciones del modelo, la hipoalfalipoproteinemia tiene una justificación biológica algo más plausible (efecto de raloxifeno sobre los lípidos), aunque tampoco cuenta con evidencia clínica en los datos compilados.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se listan 5 de las 15 autorizaciones vigentes (todas de principio activo único). Los textos de indicación aprobada no estaban disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 87122 | Raloxifeno Cinfamed 60 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos |
| 76962 | Raloxifeno Tarbis 60 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos |
| 75525 | Raloxifeno Kern Pharma 60 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos |
| 98073003 | Evista 60 mg comprimidos recubiertos con película | Comprimido recubierto | No disponible en los datos |
| 98074002 | Optruma 60 mg comprimidos recubiertos con película | Comprimido recubierto | No disponible en los datos |

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no provienen del texto del prospecto, por lo que deben confirmarse): enfermedades tromboembólicas y vasculares (tromboflebitis, embolia pulmonar, trombofilia, síndrome antifosfolípido, oclusión de la arteria retiniana, accidente cerebrovascular, infarto cerebral, ataque isquémico transitorio, insuficiencia vertebrobasilar, trastornos cerebrovasculares, enfermedad coronaria), hipertensión, fibrilación auricular, hipertrigliceridemia, enfermedad hepática, enfermedad de la vesícula biliar y deterioro de la función renal.
- **Interacciones farmacológicas**: los datos compilados muestran únicamente interacciones farmacodinámicas con dianas (GPER1, ESR1, ESR2 y AOX1), no interacciones con otros fármacos de relevancia clínica.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es de nivel L5: solo se apoya en el modelo, sin ensayos ni literatura, y no existe un vínculo mecanístico plausible entre un SERM y la úlcera duodenal. Además, el perfil de contraindicaciones vasculares y hepáticas exige cautela.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del fármaco para analizar un posible vínculo mecanístico
- Revisión de las advertencias y contraindicaciones del prospecto de la AEMPS
- Búsqueda sistemática de literatura y ensayos preclínicos sobre raloxifeno y patología gastroduodenal
- Considerar priorizar otras predicciones con mayor plausibilidad biológica (p. ej., hipoalfalipoproteinemia) antes de invertir en esta indicación
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


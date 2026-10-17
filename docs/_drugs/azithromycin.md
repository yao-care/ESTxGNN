---
layout: default
title: Azithromycin
parent: Solo predicción del modelo (L5)
nav_order: 84
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Azithromycin: nueva indicación predicha, Síndrome de hiperviscosidad policlonal (nivel de evidencia L5). Indicación original: Infección estreptocócica (indicaciones originales según el grafo de c…"
monitor_inn: "Azithromycin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Azithromycin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Azitromicina: De Infecciones Estreptocócicas a Síndrome de Hiperviscosidad Policlonal

## Resumen en Una Frase

Azitromicina es un antibiótico macrólido, utilizado originalmente para tratar infecciones bacterianas como las estreptocócicas, la neumonía bacteriana y la conjuntivitis.
El modelo TxGNN predice que podría ser efectivo para **síndrome de hiperviscosidad policlonal** (la predicción de mayor puntaje), pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección estreptocócica (indicaciones originales según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal |
| Puntaje de Predicción TxGNN | 99.81% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la azitromicina es un antibiótico macrólido con actividad antibacteriana y propiedades antiinflamatorias e inmunomoduladoras descritas. Su eficacia en infecciones bacterianas está bien establecida.

Para el síndrome de hiperviscosidad policlonal, **no se identifica un vínculo mecanístico plausible**: las acciones antibacterianas e inmunomoduladoras de la azitromicina no tienen relación establecida con la hiperviscosidad sérica. El puntaje alto (99.81%) refleja una predicción basada en el grafo de conocimiento, no evidencia biológica o clínica.

Conviene señalar otras predicciones del mismo análisis con mayor respaldo indirecto, que podrían merecer evaluación prioritaria:
- **Enfermedad hematológica congénita (enfermedad de células falciformes)**: plausible por efectos antiinflamatorios que podrían reducir el síndrome torácico agudo, aunque los dos ensayos específicos fueron retirados sin participantes.
- **Peste septicémica**: existe un estudio de susceptibilidad in vitro, pero con actividad deficiente de azitromicina frente a *Yersinia pestis*.
- **Gammapatía monoclonal**: un estudio preclínico muestra que los macrólidos bloquean el flujo autofágico y sensibilizan células de mieloma a bortezomib.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para el síndrome de hiperviscosidad policlonal.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 66065 | Azitromicina Normon 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 70190 | Azitromicina Sun 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 82363 | Azitromicina Teva 250 mg comprimidos dispersables | Comprimido dispersable | No disponible |
| 65636 | Azitromicina Sandoz 500 mg polvo para suspensión oral en sobre EFG | Polvo para suspensión oral | No disponible |
| 85006 | Azitromicina Tecnigen 500 mg polvo para solución para perfusión EFG | Polvo para solución para perfusión | No disponible |

Se muestran 5 de las 20 autorizaciones vigentes (todas de medicamentos de un solo principio activo). También está comercializado Zitromax 250 mg (Pfizer), polvo para suspensión oral en sobre. Hay presentaciones orales, dispersables e intravenosas.

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de riesgo según el grafo de conocimiento** (no proceden del texto del prospecto): síndrome de QT largo (incluido el familiar), torsades de pointes, enfermedad hepática, enfermedad de la vesícula biliar, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal, miastenia gravis, enfermedad de la unión neuromuscular, trastornos de la audición y enfermedades del sistema auditivo.
- **Interacciones / farmacología**: se han descrito interacciones farmacológicas con el receptor de motilina (MLNR) y con el receptor del sabor amargo TAS2R4. No son interacciones medicamentosas clínicas clásicas, sino dianas farmacológicas.

Es imprescindible consultar el prospecto para las advertencias y contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (síndrome de hiperviscosidad policlonal) tiene solo respaldo computacional (L5), sin ensayos, sin literatura y sin mecanismo plausible. No hay base para avanzar con esta indicación.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto oficial de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), ya que su ausencia impide el cribado de seguridad.
- Completar los datos del mecanismo de acción.
- Evaluar de forma prioritaria candidatas alternativas con más respaldo indirecto (p. ej., enfermedad de células falciformes con síndrome torácico agudo) y, si procede, replantear el ensayo piloto retirado.
- Antes de cualquier uso, valorar el riesgo cardiaco (QT) y hepático.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


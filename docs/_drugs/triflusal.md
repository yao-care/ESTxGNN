---
layout: default
title: Triflusal
parent: Solo predicción del modelo (L5)
nav_order: 827
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Triflusal: nueva indicación predicha, Exceso de factor V con trombosis espontánea (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
---

# Triflusal
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Triflusal: De Indicación Original No Especificada a Exceso de Factor V con Trombosis Espontánea

## Resumen en Una Frase

Triflusal es un antiagregante plaquetario comercializado en España; los datos compilados no recogen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **exceso de factor V con trombosis espontánea**, pero no hay **ningún ensayo clínico** ni **publicación** que respalde esta predicción concreta.
Se trata de una predicción puramente computacional (nivel de evidencia L5).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Exceso de factor V con trombosis espontánea |
| Puntaje de Predicción TxGNN | 99.60% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 10 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente de datos principal. Según la información farmacológica conocida, triflusal es un antiagregante plaquetario que inhibe de forma irreversible la COX-1 plaquetaria (reduciendo el tromboxano A2). Su metabolito activo, HTB, inhibe la fosfodiesterasa y preserva la producción endotelial de prostaciclina y óxido nítrico. Estos mecanismos podrían reducir la trombosis dependiente de las plaquetas.

Sin embargo, el exceso de factor V es un trastorno de la cascada de coagulación, y no existe evidencia mecanística ni clínica directa que vincule el triflusal con esta enfermedad. La relación con la indicación original no ha sido evaluada. El puntaje elevado de TxGNN (0.996) es solo una predicción computacional, y cualquier beneficio sería, en el mejor de los casos, una protección antiplaquetaria complementaria.

### Otras indicaciones predichas (para contexto)

| Rango | Enfermedad | Puntaje TxGNN | Nivel de Evidencia | Recomendación |
|---|---|---|---|---|
| 2 | Deficiencia de cofactor II de la heparina | 99.59% | L5 | Hold |
| 3 | Deficiencia de antitrombina tipo 2 | 99.59% | L5 | Hold |
| 4 | Trombofilia | 99.45% | L4 | Pregunta de investigación |
| 5 | Artritis reumatoide | 99.29% | L5 | Hold |

La trombofilia es la predicción con más respaldo indirecto: una publicación de 1993 (PMID 8200721) describe el efecto del triflusal sobre la función plaquetaria en pacientes con riesgo trombogénico por hiperagregación plaquetaria. Es solo evidencia farmacodinámica indirecta.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (exceso de factor V con trombosis espontánea).

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 68135 | DISGREN 600 mg polvo y disolvente para solución oral | Polvo y disolvente para solución oral | No especificada |
| 65268 | Triflusal Ratiopharm 300 mg cápsulas EFG | Cápsula dura | No especificada |
| 76110 | Triflusal Pensa 300 mg cápsulas duras EFG | Cápsula dura | No especificada |
| 65248 | Anpeval 300 mg cápsulas duras EFG | Cápsula dura | No especificada |
| 68092 | Triflusal Teva 300 mg cápsulas EFG | Cápsula dura | No especificada |

Se muestran 5 de las 10 autorizaciones vigentes (todas de monofármaco). Las restantes corresponden a Triflusal Abamed, Triflusal Cinfa, Disgren 300 mg, Triflusal Farmalider y Triflusal Aristo.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo TxGNN, sin ensayos clínicos ni literatura, y el mecanismo antiplaquetario del triflusal no corrige el defecto de la cascada de coagulación propio del exceso de factor V.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (indicaciones aprobadas, advertencias y contraindicaciones), ya que su ausencia impide el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión sistemática de la literatura sobre triflusal en trombofilias y trastornos de la coagulación hereditarios.
- Valorar priorizar la trombofilia (nivel L4) como pregunta de investigación generadora de hipótesis antes que las demás predicciones.
- Evaluar la compatibilidad de las vías de administración y la similitud con la indicación original, hoy pendientes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


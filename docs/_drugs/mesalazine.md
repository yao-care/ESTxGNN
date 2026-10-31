---
layout: default
title: Mesalazine
parent: Solo predicción del modelo (L5)
nav_order: 508
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-31
monitor_inn: "Mesalazine"
predicted_indications: ["congenital hypotrichosis with juvenile macular dystrophy", "osteoarthritis", "rheumatoid arthritis", "seborrheic keratosis", "vulvar inverted follicular keratosis", "pseudoachondroplasia"]
description: "Mesalazine: nueva indicación predicha, Hipotricosis congénita con distrofia macular juvenil (congenital hypotrichosis with juvenile macular dystrophy) (nivel de evidencia L5). Indicación original: No…"
---

# Mesalazine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Mesalazine: Hipotricosis congénita con distrofia macular juvenil (congenital hypotrichosis with juvenile macular dystrophy)
{: .text-alpha }

## Resumen en Una Frase

Mesalazina (5-ASA, ácido 5-aminosalicílico) se utiliza originalmente para tratar la colitis ulcerosa y otras enfermedades inflamatorias intestinales.
El modelo TxGNN predice que podría ser efectiva para **hipotricosis congénita con distrofia macular juvenil**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata de una predicción puramente computacional.

> **Nota:** La indicación con mayor puntaje es una enfermedad genética ultrarrara sin vínculo mecanístico identificado. Entre las demás predicciones, la **artritis reumatoide** (nivel L4) y la **artrosis** (L5) son las que cuentan con algo de literatura asociada, aunque indirecta. Se comentan en la sección de conclusiones.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hipotricosis congénita con distrofia macular juvenil (congenital hypotrichosis with juvenile macular dystrophy) |
| Puntaje de Predicción TxGNN | 0.9965 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 10) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la mesalazina es el componente 5-ASA, con actividad antiinflamatoria local en la mucosa intestinal, y su eficacia en colitis ulcerosa está bien establecida. Los datos farmacológicos compilados indican interacción con el receptor PPAR-γ (receptor activado por proliferadores de peroxisomas gamma).

Para esta indicación concreta **no se identificó ningún vínculo mecanístico**. La hipotricosis congénita con distrofia macular juvenil es un trastorno genético ultrarraro (mutaciones en CDH3) sin una vía inflamatoria conocida que la mesalazina module. El puntaje alto de TxGNN (0,9965) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

---

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de principio activo único). No se dispone del texto de indicación aprobada en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 62670 | Pentasa 1 g granulado de liberación prolongada | Granulado de liberación modificada | No disponible |
| 74791 | Salofalk 3 g granulado de liberación prolongada | Granulado de liberación modificada | No disponible |
| 61335 | Claversal espuma rectal | Espuma rectal | No disponible |
| 85724 | Azzavix 1000 mg comprimidos gastrorresistentes | Comprimido gastrorresistente | No disponible |
| 88174 | Mecolvix 500 mg supositorios | Supositorio | No disponible |

---

## Consideraciones de Seguridad

- **Contraindicaciones/enfermedades de riesgo (según el grafo de conocimiento, no según prospecto):** enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, neutropenia, agranulocitosis, anemia (incluida la macrocítica), estenosis pilórica, nefrosis lipoidea, nefritis intersticial y piouréter.
- **Interacciones farmacológicas:** se registró una interacción farmacológica de tipo farmacodinámico con el receptor PPAR-γ (diana humana); no se dispone de un nivel de gravedad clínica.

Para información completa de advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal carece de ensayos, literatura y mecanismo plausible; es una enfermedad genética ultrarrara que no es previsiblemente tratable con un aminosalicilato antiinflamatorio. El nivel de evidencia es L5.

**Otras predicciones del modelo (para contexto):**

| Indicación | Puntaje TxGNN | Nivel | Valoración |
|---|---|---|---|
| Artrosis | 0,9963 | L5 | Hold. Mecanismo plausible pero no probado (inflamación sinovial, NF-κB/PPAR-γ); un único estudio transcriptómico de 2024 (PMID 38491514), sin ensayos clínicos. |
| Artritis reumatoide | 0,9957 | L4 | Pregunta de investigación. La literatura es mayoritariamente sobre sulfasalazina, farmacocinética y reacciones adversas; la actividad antirreumática se atribuye sobre todo a la sulfapiridina, no al 5-ASA. No demuestra beneficio. |

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de la mesalazina para analizar posibles vínculos mecanísticos.
- Advertencias y contraindicaciones del prospecto de la AEMPS (actualmente solo se dispone de datos del grafo de conocimiento), imprescindibles antes de cualquier evaluación de seguridad.
- Texto de indicación aprobada de las autorizaciones españolas.
- Si se desea priorizar, concentrar la revisión en artrosis y artritis reumatoide, con revisión sistemática de la literatura y estudios preclínicos antes de plantear ensayos; descartar la indicación principal salvo que aparezca nueva evidencia biológica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


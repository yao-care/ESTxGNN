---
layout: default
title: Aztreonam
parent: Solo predicción del modelo (L5)
nav_order: 61
evidence_level: L5
indication_count: 10
---

# Aztreonam
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

# Aztreonam: De Antibiótico Monobactámico a Hiperamilasemia

## Resumen en Una Frase

Aztreonam es un antibiótico monobactámico (betalactámico) que actúa contra bacterias Gram-negativas. El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que la predicción se apoya solo en el grafo de conocimiento.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Hiperamilasemia |
| Puntaje de Predicción TxGNN | 99.73% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada. Según la información conocida, aztreonam inhibe la proteína de unión a penicilina 3 (PBP3) de las bacterias, bloqueando la síntesis de la pared celular. No tiene efecto conocido sobre el metabolismo de la amilasa.

La hiperamilasemia es un hallazgo bioquímico (amilasa elevada en sangre), asociado por ejemplo a pancreatitis o a alteraciones de las glándulas salivales, no una infección bacteriana. No existe una relación mecanística plausible entre un antibacteriano y esta condición.

El puntaje alto de TxGNN (99.73%) proviene únicamente de relaciones en el grafo de conocimiento. Sin estudios que lo respalden, esta predicción debe considerarse probablemente un artefacto del modelo y no una hipótesis terapéutica sólida.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 09543002 | CAYSTON 75 mg polvo y disolvente para solución para inhalación por nebulizador | Polvo para solución para inhalación por nebulizador |
| 57781 | AZACTAM 1 g polvo para solución inyectable | Polvo para solución inyectable |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene respaldo clínico ni bibliográfico, y no existe una razón mecanística para que un antibacteriano actúe sobre la hiperamilasemia. No se recomienda avanzar con esta indicación.

**Para avanzar se necesita:**
- Evidencia real (estudios preclínicos o clínicos) que vincule aztreonam con el metabolismo de la amilasa.
- Datos de seguridad del prospecto de la AEMPS (advertencias y contraindicaciones).
- Datos detallados del mecanismo de acción desde DrugBank.

**Nota sobre otras predicciones del mismo fármaco:** entre las 10 indicaciones predichas, la mejor respaldada no es la de rango 1 sino la **uretritis gonocócica** (nivel L2, puntaje 99.59%). Cuenta con un ensayo Fase 2/3 completado en gonorrea faríngea ([NCT03867734](https://clinicaltrials.gov/study/NCT03867734), n=32) y un ensayo abierto de brazo único de 2020 ([PMID 33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/)). También hay varios estudios clínicos de los años 80 que indican eficacia con dosis única. Como límites, no existe una comparación aleatorizada de Fase 3, el ensayo moderno se centró en la faringe y se han descrito gonococos con alta resistencia a aztreonam ([PMID 11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/)). Se recomienda evaluarla en un informe aparte como pregunta de investigación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


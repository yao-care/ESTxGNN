---
layout: default
title: Valproic Acid
parent: Solo predicción del modelo (L5)
nav_order: 553
evidence_level: L5
indication_count: 10
---

# Valproic Acid
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

# Ácido valproico: De Trastornos Convulsivos a Neoplasia del Nervio Trigémino

## Resumen en Una Frase

El ácido valproico es un antiepiléptico de amplio espectro. Está aprobado para trastornos convulsivos, episodios maníacos del trastorno bipolar y migraña.
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino**, con **0 ensayos clínicos** y **1 publicación** que no aborda directamente esta indicación (trata sobre el síndrome de Sturge-Weber). La predicción carece de respaldo clínico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastornos convulsivos, episodios maníacos del trastorno bipolar y migraña (según los datos farmacológicos; las licencias de AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 99,97 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 14 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información farmacológica disponible, el ácido valproico es un inhibidor de la histona desacetilasa (HDAC), con HDAC1 como diana humana registrada. Se investiga como tratamiento en infección por VIH y en varios tipos de cáncer, además de sus usos aprobados como antiepiléptico.

La relación entre la indicación original y la nueva es débil. Los usos aprobados son neurológicos y psiquiátricos, y una neoplasia del nervio trigémino es un tumor. El único puente posible sería un efecto antineoplásico por inhibición de HDAC. El análisis del Evidence Pack lo califica de **especulativo y sin respaldo en los datos disponibles**.

El puntaje TxGNN es muy alto (99,97 %), pero no está apoyado por ningún dato clínico o preclínico recuperado. Debe tratarse como una hipótesis del modelo, no como una señal de eficacia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Serie de casos | Anales españoles de pediatría | Revisión de 14 casos de síndrome de Sturge-Weber seguidos durante 25 años, con sus características clínicas, evolución y respuesta terapéutica. No trata sobre tumores del trigémino, por lo que no respalda esta indicación. |

---

## Información de Mercado en España

Se listan 5 de las 14 autorizaciones. El registro no incluye texto de indicación aprobada para ninguna de ellas.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 84514 | Ácido Valproico Aurobindo 300 mg comprimidos de liberación prolongada EFG | Comprimido de liberación prolongada |
| 60350 | Depakine Crono 500 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada |
| 60352 | Depakine 100 mg/ml polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable |
| 48828 | Depakine 200 mg/ml solución oral | Solución oral |
| 68033 | Ácido Valproico Altan 400 mg polvo para solución inyectable EFG | Polvo para solución inyectable |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Los datos de interacciones del Evidence Pack solo registran a HDAC1 como diana farmacológica, no interacciones con otros medicamentos.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5). No hay ensayos clínicos, y la única publicación recuperada no guarda relación con la indicación. El vínculo mecanístico por inhibición de HDAC es especulativo.

**Para avanzar se necesita:**
- Datos preclínicos (líneas celulares o modelos animales) del ácido valproico en tumores del nervio trigémino o tumores nerviosos comparables.
- Datos detallados del mecanismo de acción, a partir de DrugBank.
- Revisión del prospecto de AEMPS para los datos de advertencias y contraindicaciones.
- Una revisión de literatura dirigida sobre ácido valproico y neoplasias del sistema nervioso.

Entre las otras indicaciones predichas, algunas tienen más respaldo que esta. Por ejemplo, la epilepsia visual alcanza nivel L3, aunque es en la práctica una extensión del uso antiepiléptico ya existente y no un reposicionamiento propiamente dicho.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


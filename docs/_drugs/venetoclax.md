---
layout: default
title: Venetoclax
parent: Evidencia moderada (L3-L4)
nav_order: 556
evidence_level: L4
indication_count: 10
---

# Venetoclax
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Venetoclax: De Indicación Original No Registrada a LLC/LLP de Centro Pregerminal

## Resumen en Una Frase

Venetoclax es un inhibidor de BCL-2 comercializado en España como Venclyxto, pero las autorizaciones del registro no incluyen el texto de la indicación original.
El modelo TxGNN predice que podría ser efectivo para la **leucemia linfocítica crónica/linfoma linfocítico pequeño (LLC/LLP) de centro pregerminal**.
La evidencia es muy limitada: **0 ensayos clínicos** y **1 publicación** (un estudio biológico que no evalúa venetoclax).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (el texto de indicación está vacío en las 5 autorizaciones) |
| Nueva Indicación Predicha | LLC/LLP de centro pregerminal |
| Puntaje de Predicción TxGNN | 99.55% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, venetoclax es un inhibidor selectivo de la proteína antiapoptótica BCL-2. Las células de LLC/LLP dependen de la sobreexpresión de BCL-2 para sobrevivir, por lo que mecanísticamente es plausible que el fármaco sea aplicable.

La única publicación disponible analiza la estructura y función del receptor de células B (BCR) tumoral en la LLC. Distingue los subgrupos de origen pregerminal (IGHV no mutado, peor pronóstico) y postgerminal (IGHV mutado, mejor pronóstico). Es un estudio biológico y traslacional, y **no prueba venetoclax** en este subgrupo molecular.

**Advertencia sobre la calidad del dato:** el campo de indicaciones originales está vacío. La LLC/LLP en general se considera una indicación ya aprobada de venetoclax, por lo que este caso probablemente no es un reposicionamiento genuino. La segunda predicción (LLC/LLP con hipermutación somática de IGHV) tiene exactamente el mismo puntaje y parece un nodo hermano de la misma ontología. Ninguna de las dos aporta una señal independiente de reposicionamiento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35158929](https://pubmed.ncbi.nlm.nih.gov/35158929/) | 2022 | Estudio biológico/traslacional | Cancers | Revisa la estructura y función del BCR tumoral en la LLC y distingue los subgrupos U-CLL (origen pregerminal, mal pronóstico) y M-CLL (origen postgerminal, buen pronóstico). No evalúa venetoclax. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 161138005 | VENCLYXTO 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en el registro |
| 161138007IP1 | VENCLYXTO 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en el registro |
| 161138004 | VENCLYXTO 50 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en el registro |
| 161138002 | VENCLYXTO 10 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en el registro |
| 161138007IP | VENCLYXTO 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en el registro |

Titular de todas las autorizaciones: AbbVie Deutschland GmbH & Co. KG.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de BCL-2) |
| Riesgo de Mielosupresión | Medio a alto. Una revisión de la literatura señala que el síndrome de lisis tumoral y la mielosupresión son las toxicidades más frecuentes. |
| Clasificación de Emetogenicidad | Baja (según la categoría del fármaco; confirmar en la ficha técnica) |
| Ítems de Monitoreo | Hemograma con diferencial, función hepática y renal, electrolitos, ácido úrico, fósforo, potasio y calcio (riesgo de lisis tumoral) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto y la normativa local de manejo de fármacos antineoplásicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la única publicación no evalúa venetoclax en este subgrupo. Además, la predicción parece un artefacto de la ontología (LLC/LLP ya es un uso generalmente aprobado), no un reposicionamiento real.

**Para avanzar se necesita:**
- Corregir el campo de indicaciones originales y verificar la indicación aprobada de LLC/LLP en la ficha técnica de la AEMPS.
- Descargar y analizar la ficha técnica de la AEMPS para completar advertencias y contraindicaciones (bloqueante para el cribado de seguridad).
- Obtener el mecanismo de acción desde DrugBank.
- Buscar datos específicos del subtipo pregerminal (IGHV no mutado) antes de cualquier decisión.

**Otras predicciones del mismo Evidence Pack con más apoyo (a priorizar):**
- **Leucemia mieloide** (L2): incluye un ensayo aleatorizado de fase 2 (NCT04266795) y uno de fase 2/3 (NCT05805098). Decisión: Proceed with Guardrails, con vigilancia de resistencia (MCL-1, TP53), mielosupresión, infecciones y lisis tumoral.
- **Linfoma folicular** y **leucemia mieloide crónica BCR-ABL1 positiva** (L2 ambas): solo hay estudios de fase 1/2, en su mayoría de un solo brazo. Se clasifican como pregunta de investigación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


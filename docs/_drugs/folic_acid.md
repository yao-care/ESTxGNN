---
layout: default
title: Folic Acid
parent: Solo predicción del modelo (L5)
nav_order: 354
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Folic Acid: nueva indicación predicha, Enfermedad metabólica de la biotina (nivel de evidencia L5). Indicación original: Deficiencia de vitaminas / anemia por deficiencia de ácido fólico (se…"
monitor_inn: "Folic acid"
predicted_indications: ["biotin metabolic disease"]
---

# Folic Acid
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Ácido fólico: De Deficiencia de Vitaminas a Enfermedad Metabólica de la Biotina
{: .text-alpha }

## Resumen en Una Frase

El ácido fólico es una vitamina del grupo B utilizada originalmente para tratar deficiencias vitamínicas y anemias carenciales (como la anemia por deficiencia de ácido fólico).
El modelo TxGNN predice que podría ser efectivo para la **enfermedad metabólica de la biotina**,
pero no hay **ningún ensayo clínico** y solo existen **19 publicaciones** de carácter general (mayoritariamente revisiones), por lo que la evidencia es únicamente predictiva.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Deficiencia de vitaminas / anemia por deficiencia de ácido fólico (según la base de conocimiento del modelo; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Enfermedad metabólica de la biotina |
| Puntaje de Predicción TxGNN | 0.9949 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 5 de 7) |
| Número de Autorizaciones | 7 (vigentes: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el ácido fólico es una vitamina hidrosoluble del grupo B que actúa como cofactor en el metabolismo de un carbono (síntesis de nucleótidos y metionina), y su eficacia en las anemias carenciales y deficiencias vitamínicas está bien establecida.

La biotina es también una vitamina hidrosoluble del grupo B, cofactor de las carboxilasas. Ambas vitaminas comparten cercanía en la red de conocimiento (rutas de metabolismo de un carbono y carboxilación), lo que explica el puntaje alto del modelo. Además, la literatura menciona interacciones metabólicas entre vitaminas del grupo B (por ejemplo, la relación entre B12, folato y biotina).

Sin embargo, esta predicción debe interpretarse con cautela: el ácido fólico no sustituye la función de la biotina. Las deficiencias de carboxilasas dependientes de biotina, de biotinidasa o de holocarboxilasa sintetasa se tratan con biotina, no con folato. Lo más probable es que la predicción refleje similitud de clase (vitaminas del grupo B) y no un mecanismo terapéutico específico. La ausencia de datos de mecanismo de acción limita aún más la validación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Las publicaciones disponibles son principalmente revisiones generales sobre vitaminas; ninguna evalúa directamente el ácido fólico como tratamiento de enfermedades metabólicas de la biotina.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39828265](https://pubmed.ncbi.nlm.nih.gov/39828265/) | 2025 | Metaanálisis (revisión paraguas) | Asia Pac J Clin Nutr | Síntesis de metaanálisis sobre vitaminas hidrosolubles y control glucémico en diabetes tipo 2; resultados previos inconsistentes |
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Revisión | Handb Clin Neurol | Trastornos sensibles a vitaminas (cobalamina, folato, biotina, B1 y E); errores innatos del metabolismo vitamínico |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Revisión | Int J Mol Sci | Deficiencia de B12 y sistema nervioso; menciona el papel de la B12 con biotina y folato en reacciones bioquímicas |
| [37123774](https://pubmed.ncbi.nlm.nih.gov/37123774/) | 2023 | Revisión | Cureus | Relación entre vitaminas y diabetes tipo 2; niveles bajos de tiamina, piridoxina y biotina |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Revisión | Endocr Metab Immune Disord Drug Targets | Vitaminas (individuales o combinadas) y diabetes tipo 2 |
| [41692080](https://pubmed.ncbi.nlm.nih.gov/41692080/) | 2026 | Revisión | Clin Dermatol | Papel de las vitaminas del grupo B en el metabolismo celular y la síntesis de eritrocitos |
| [14989256](https://pubmed.ncbi.nlm.nih.gov/14989256/) | 2004 | Revisión | Arch Biochem Biophys | Suplementos de micronutrientes (B12, folato, B6, etc.) y daño al ADN |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Revisión | Acta Vitaminol Enzymol | Vitaminas en enfermedades metabólicas: malabsorción, errores del metabolismo y síndromes dependientes de vitaminas |
| [38350491](https://pubmed.ncbi.nlm.nih.gov/38350491/) | 2025 | Cohorte | Nutr Rev | Estado de micronutrientes en niños con desnutrición grave |
| [16183151](https://pubmed.ncbi.nlm.nih.gov/16183151/) | 2006 | Estudio preclínico (ratas) | Int J Cardiol | El ácido fólico reduce la expresión de VCAM-1 en la aorta de ratas con hiperhomocisteinemia |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 64808 | ZOLICO 400 MICROGRAMOS COMPRIMIDOS | Comprimido | No disponible |
| 86528 | ACIDO FOLICO ARISTO 5 MG COMPRIMIDOS | Comprimido | No disponible |
| 68965 | BIALFOLI 5 mg COMPRIMIDOS | Comprimido | No disponible |
| 11265 | ACFOL 5 mg COMPRIMIDOS | Comprimido | No disponible |
| 52788 | ACIDO FÓLICO ASPOL 10MG CÁPSULAS DURAS | Cápsula dura | No disponible |

Existen 7 autorizaciones vigentes en total (todas de monofármaco); aquí se muestran las 5 principales.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proviene del prospecto)**: el modelo asocia el fármaco con contraindicaciones en enfermedades como anemia hemolítica, enfermedad renal, diabetes mellitus, cetoacidosis diabética, úlcera péptica, enfermedad inflamatoria intestinal, colitis ulcerosa, hemocromatosis hereditaria, enfermedad de Wilson, nefrolitiasis, hipercalcemia, hiperparatiroidismo, sarcoidosis, anemia falciforme, hiperoxaluria primaria y trastorno bipolar, entre otras. Estas asociaciones requieren verificación con la ficha técnica, ya que algunas parecen reflejar relaciones de clase y no contraindicaciones propias del ácido fólico.
- **Interacciones farmacológicas** (100 registradas; se muestran las principales):
  - Pancrelipasa: moderada
  - Sulfasalazina: leve
  - Otras con nivel no clasificado: calcitriol, pantoprazol, glimepirida, mesalazina, acarbosa, morfina, metformina, omeprazol, sucralfato, lansoprazol, vancomicina, lactulosa, prednisona, simvastatina, entre otras.

Consultar el prospecto para las advertencias y contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5): no hay ensayos clínicos, la literatura es indirecta y el razonamiento mecanístico sugiere que se trata de similitud de clase entre vitaminas, ya que las enfermedades metabólicas de la biotina se tratan con biotina.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), requisito previo para el cribado de seguridad
- Datos del mecanismo de acción del ácido fólico (por ejemplo, desde DrugBank)
- Estudios preclínicos o mecanísticos que justifiquen un papel del folato en trastornos del metabolismo de la biotina
- Revisión de la literatura específica sobre deficiencia de biotinidasa/holocarboxilasa sintetasa y folato
- Considerar si otra indicación predicha tiene una base más sólida
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


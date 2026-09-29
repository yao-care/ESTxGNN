---
layout: default
title: Pravastatin
parent: Evidencia moderada (L3-L4)
nav_order: 434
evidence_level: L4
indication_count: 9
---

# Pravastatin
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **9** 
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

# Pravastatina: De Hipercolesterolemia a Hipercolesterolemia Familiar Homocigota

## Resumen en Una Frase

La pravastatina es una estatina que se usa para tratar la hipercolesterolemia y reducir el riesgo cardiovascular.
El modelo TxGNN predice que podría ser efectiva para la **hipercolesterolemia familiar homocigota**,
pero solo hay **1 ensayo clínico** (que evalúa otro fármaco, alirocumab) y **13 publicaciones** sin evidencia directa con pravastatina en esta enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en las autorizaciones de AEMPS. Según farmacología (GtoPdb): hipercolesterolemia y reducción del riesgo cardiovascular |
| Nueva Indicación Predicha | Hipercolesterolemia familiar homocigota |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de un campo detallado de mecanismo de acción en el paquete de datos. Según la información farmacológica, la pravastatina inhibe la HMG-CoA reductasa (HMGCR), la enzima limitante de la síntesis de colesterol, y aumenta los receptores hepáticos de LDL. También es sustrato del transportador hepático OATP1B1 (SLCO1B1).

La relación entre ambas indicaciones es clara en lo conceptual: en las dos hay un LDL-colesterol elevado. Sin embargo, la forma homocigota se debe a la ausencia o el defecto grave del receptor de LDL (LDLR). Como la pravastatina depende de aumentar esos receptores, se espera una respuesta limitada, sobre todo en pacientes sin actividad residual del receptor.

Por tanto, la predicción tiene un puntaje alto en el grafo de conocimiento, pero el mecanismo la respalda solo de forma parcial. Además, no existen ensayos con pravastatina en la forma homocigota. La literatura sobre estatinas en niños con hipercolesterolemia familiar cubre sobre todo la forma heterocigota.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Fase 3 | Completado | 18 | Alirocumab (inhibidor de PCSK9) cada 2 semanas en niños y adolescentes de 8 a 17 años con hipercolesterolemia familiar homocigota, sobre el tratamiento de base. No evalúa pravastatina |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Revisión sistemática | Cochrane Database Syst Rev | Estatinas en niños con hipercolesterolemia familiar; se centra sobre todo en la forma heterocigota |
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Revisión sistemática | Cochrane Database Syst Rev | Versión anterior de la misma revisión sobre estatinas en niños con hipercolesterolemia familiar |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guía clínica | Endocr Pract | Guía AACE/ACE para el manejo de la dislipidemia y la prevención cardiovascular |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Revisión | Clin Ther | Rosuvastatina, con indicación en hipercolesterolemia primaria, dislipidemia mixta e hipercolesterolemia familiar homocigota. No trata de pravastatina |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Revisión | Drugs | Rosuvastatina frente a otras estatinas, incluida pravastatina, en hipercolesterolemia |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Revisión | Am J Cardiovasc Drugs | Ezetimiba, inhibidor de la absorción intestinal de colesterol |
| [14647533](https://pubmed.ncbi.nlm.nih.gov/14647533/) | 2003 | Revisión | Cardiovasc Drug Rev | Ezetimiba como inhibidor de la absorción de colesterol de primera clase |
| [15067249](https://pubmed.ncbi.nlm.nih.gov/15067249/) | 2003 | Revisión | Ann Endocrinol | Ezetimiba y terapias combinadas con estatinas en casos graves de dislipidemia |
| [31358055](https://pubmed.ncbi.nlm.nih.gov/31358055/) | 2019 | Preclínico (modelo iPSC) | Stem Cell Res Ther | Hepatocitos derivados de iPSC con déficit de LDLR para modelar la hipercolesterolemia familiar y su corrección con CRISPR |
| [34425670](https://pubmed.ncbi.nlm.nih.gov/34425670/) | 2021 | Estudio genético | Iran Biomed J | Nueva variante de splicing en LDLRAP1 en una familia con hipercolesterolemia familiar |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 66521 | PRAVASTATINA TARBIS 40 mg COMPRIMIDOS EFG | Comprimido | Tarbis Farma S.L. |
| 81468 | PRAVASTATINA AUROVITAS 20 MG COMPRIMIDOS EFG | Comprimido | Aurovitas Spain, S.A.U. |
| 60162 | BRISTACOL 20 mg COMPRIMIDOS | Comprimido | Exeltis Healthcare S.L. |
| 70376 | PRAVASTATINA KORHISPANA 10 mg COMPRIMIDOS EFG | Comprimido | Korhispana S.L. |
| 68535 | PRAVASTATINA QUALIGEN 10 mg COMPRIMIDOS EFG | Comprimido | Neuraxpharm Spain S.L. |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la base de datos registra dos elementos farmacológicos, no fármacos concretos: la diana HMG-CoA reductasa (HMGCR) y el transportador hepático OATP1B1 (SLCO1B1). Este último es relevante porque los inhibidores de OATP1B1 pueden aumentar la exposición a pravastatina. No se especifica nivel de gravedad.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Solo hay una predicción del modelo, sin evidencia directa. El único ensayo registrado evalúa alirocumab, y la literatura consiste en revisiones de otros hipolipemiantes y estudios de estatinas en hipercolesterolemia familiar sobre todo heterocigota. Además, el mecanismo de la pravastatina depende del receptor de LDL, que en la forma homocigota está ausente o es defectuoso.

**Para avanzar se necesita:**
- Confirmar la indicación autorizada actual de pravastatina en el prospecto de AEMPS. Los datos de indicación y de seguridad (advertencias y contraindicaciones) no están disponibles en el paquete y bloquean el cribado de seguridad.
- Buscar estudios con pravastatina en pacientes con hipercolesterolemia familiar homocigota, estratificados por actividad residual del LDLR.
- Contrastar con las terapias ya establecidas para esta forma (por ejemplo, inhibidores de PCSK9 como alirocumab) para valorar si aportaría algo.
- Nota: en este mismo paquete, otras dos predicciones tienen evidencia más sólida y nivel L2 con recomendación *Proceed with Guardrails*: la dislipidemia asociada al VIH (con ensayos y ECA con pravastatina) y la hipercolesterolemia familiar heterocigota. Conviene evaluarlas por separado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Trastuzumab Emtansine
parent: Solo predicción del modelo (L5)
nav_order: 541
evidence_level: L5
indication_count: 4
---

# Trastuzumab Emtansine
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

# Trastuzumab emtansina: De Cáncer de Mama HER2-Positivo a Cáncer de Mama con Receptor de Progesterona Positivo

## Resumen en Una Frase

Trastuzumab emtansina (T-DM1, comercializado como Kadcyla) es un conjugado anticuerpo-fármaco anti-HER2. Su uso establecido, según los ensayos y la literatura del paquete de evidencia, es el cáncer de mama HER2-positivo. El modelo TxGNN predice que podría ser efectivo para el **cáncer de mama con receptor de progesterona positivo**, con **4 ensayos clínicos** y **16 publicaciones** asociados. Ningún ensayo aislado confirma el papel de T-DM1 en el subgrupo PR-positivo, así que la evidencia es indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los textos de autorización de la AEMPS (están vacíos). Se toma como referencia el cáncer de mama HER2-positivo, según los ensayos y la literatura aportados |
| Nueva Indicación Predicha | Cáncer de mama con receptor de progesterona positivo |
| Puntaje de Predicción TxGNN | 99,82 % |
| Nivel de Evidencia | L2 (condicionado, ver nota más abajo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Proceed with Guardrails |

**Nota sobre el nivel de evidencia:** L2 es el nivel asignado en el paquete. El único ensayo de Fase 3 completado (NCT03726879) tiene el título truncado, por lo que no se puede confirmar el papel de T-DM1. Si no se confirma, el nivel para esta indicación concreta sería más bajo.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la farmacología general, T-DM1 es un anticuerpo anti-HER2 unido a DM1, un inhibidor de microtúbulos. El fármaco entra en las células que sobreexpresan HER2 y allí libera su carga citotóxica.

Su actividad depende del estado de **HER2**, no del estado del receptor de progesterona (PR). La indicación predicha es razonable solo como el subgrupo **HER2+/receptor hormonal positivo**. Este subgrupo está descrito en la literatura aportada, por ejemplo en la revisión sobre HR+/HER2+ (PMID 33726508), que menciona T-DM1 entre las terapias anti-HER2 novedosas.

El puntaje TxGNN es casi idéntico en los cuatro subtipos de cáncer de mama evaluados (≈0,998). Por tanto, **no discrimina** entre PR-positivo, PR-negativo u otros subtipos. Debe leerse como una señal general de cáncer de mama HER2-dependiente y no como una predicción específica de PR.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Fase 2 | Activo, sin reclutamiento | 164 | T-DM1 + pertuzumab preoperatorio en cáncer de mama temprano HER2-positivo, para estudiar el impacto de la heterogeneidad de HER2. Población relevante, pero el subgrupo PR-positivo no se aísla en los datos |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Fase 3 | Completado | 454 | Estudio aleatorizado, doble ciego, con placebo (IMpassion050): atezolizumab frente a placebo con quimioterapia neoadyuvante y trastuzumab + pertuzumab en cáncer de mama temprano HER2-positivo. El papel de T-DM1 y la población PR-positiva no se pueden confirmar |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Fase 2 | Terminado | 139 | Estudio de desescalada de quimioterapia adyuvante (DECRESCENDO) en enfermedad HER2+, ER-negativa y ganglios negativos. La población no corresponde a una indicación PR-positiva |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | Completado | 1151 | Estudio retrospectivo no intervencionista sobre la prevalencia de HER2-low en cáncer de mama metastásico. No aporta evidencia de eficacia de T-DM1 |

---

## Evidencia de Literatura

No hay ECA entre las publicaciones aportadas. Se priorizan las guías y revisiones sobre los reportes de caso.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guía (ASCO) | J Clin Oncol | Actualización de las recomendaciones de terapia sistémica en cáncer de mama avanzado HER2-positivo |
| [29939838](https://pubmed.ncbi.nlm.nih.gov/29939838/) | 2018 | Guía (ASCO) | J Clin Oncol | Actualización de la guía de terapia sistémica en cáncer de mama avanzado HER2-positivo, con revisión sistemática de 622 artículos |
| [24799465](https://pubmed.ncbi.nlm.nih.gov/24799465/) | 2014 | Guía (ASCO) | J Clin Oncol | Guía original de la ASCO sobre terapia sistémica en cáncer de mama avanzado HER2-positivo |
| [28259011](https://pubmed.ncbi.nlm.nih.gov/28259011/) | 2017 | Guía (biomarcadores, EGTM) | Eur J Cancer | Recomienda medir ER y PR en todos los cánceres invasivos para seleccionar terapia endocrina. Para toda terapia anti-HER2, incluido T-DM1, exige determinar HER2 |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Revisión | Pharmacol Res | Inhibidores dirigidos y citotóxicos en cáncer de mama. El manejo depende del estado de HER2, HR, ER y PR |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Revisión (HR+/HER2+) | Future Oncol | Tendencias de tratamiento en HR+/HER2+. Menciona neratinib y trastuzumab emtansina como terapias anti-HER2 novedosas |
| [34215766](https://pubmed.ncbi.nlm.nih.gov/34215766/) | 2021 | Sin clasificar (datos del ensayo ChangeHER, práctica real) | Sci Rep | Relevancia pronóstica de ganar positividad de HER2 en cáncer de mama metastásico tratado con pertuzumab y/o T-DM1 |
| [25873876](https://pubmed.ncbi.nlm.nih.gov/25873876/) | 2015 | Sin clasificar (parece reporte de caso) | Case Rep Oncol | T-DM1 a dosis reducida en disfunción hepática aguda. El título indica que fue activo y seguro en ese contexto |
| [41499317](https://pubmed.ncbi.nlm.nih.gov/41499317/) | 2026 | Cohorte (neratinib) | Oncology | Tendencias de prescripción de neratinib adyuvante en HR+/HER2+. Indirecta: el fármaco estudiado no es T-DM1 |
| [24892840](https://pubmed.ncbi.nlm.nih.gov/24892840/) | 2013 | Sin clasificar (parece revisión) | Clin Adv Hematol Oncol | Novedades en cáncer de mama metastásico, con clasificación por inmunohistoquímica (ER, HER2, triple negativo) |

---

## Información de Mercado en España

Los textos de indicación aprobada están vacíos en los datos de la AEMPS, por lo que no se muestra esa columna. El paquete indica 6 autorizaciones, pero detalla solo 5, que son las que se listan.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 113885001 | KADCYLA 100 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | Roche Registration GmbH |
| 113885001IP | KADCYLA 100 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | Roche Registration GmbH |
| 113885001IP1 | KADCYLA 100 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | Roche Registration GmbH |
| 113885002 | KADCYLA 160 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | Roche Registration GmbH |
| 113885002IP | KADCYLA 160 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | Roche Registration GmbH |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida: conjugado anticuerpo-fármaco anti-HER2 con carga citotóxica (DM1, inhibidor de microtúbulos) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto. La literatura aportada describe un caso con disfunción hepática (PMID 25873876) |
| Protección en Manejo | Consultar el prospecto y aplicar las normas de manejo de medicamentos citotóxicos de cada centro |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
T-DM1 tiene una base clínica sólida en cáncer de mama HER2-positivo y está comercializado en España. Para el subgrupo PR-positivo la evidencia es indirecta: no hay ensayo que aísle ese subgrupo y el puntaje TxGNN no distingue entre subtipos. El avance solo es defendible si se restringe a enfermedad HER2-positiva confirmada.

**Para avanzar se necesita:**
- **Salvaguarda principal:** confirmar el estado HER2-positivo y aplicar la evidencia solo dentro del entorno HER2+ aprobado. El estado de PR no debe ser el criterio de selección.
- Verificar el papel real de T-DM1 en NCT03726879 y en los demás ensayos del subgrupo, y confirmar si hay datos del subgrupo HR+/HER2+.
- Obtener las advertencias y contraindicaciones del prospecto de la AEMPS. Este vacío de datos es **bloqueante** para el cribado de seguridad.
- Completar el mecanismo de acción desde DrugBank y los textos de indicación aprobada de las autorizaciones.
- Nota sobre otros subtipos: el paquete asigna nivel L1 a la entrada de cáncer de mama PR-negativo, con varios ensayos de Fase 3 en HER2+ donde T-DM1 es base o comparador. Esa evidencia no se traslada automáticamente al subgrupo PR-positivo, aunque apoya la lógica de que la eficacia sigue a HER2.

*Los resultados de este informe son solo de referencia para investigación y no constituyen consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


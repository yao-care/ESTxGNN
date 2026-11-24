---
layout: default
title: Tegafur
parent: Solo predicción del modelo (L5)
nav_order: 768
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
monitor_inn: "TEGAFUR"
predicted_indications: ["cecum villous adenoma", "cecum neuroendocrine tumor G1", "lipoma of colon", "cecal disease", "colon leiomyoma", "benign neoplasm of cecum", "colonic lymphangioma", "cavernous hemangioma of colon"]
description: "Tegafur: nueva indicación predicha, Cecum villous adenoma (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 1)"
---

# Tegafur
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Tegafur: Cecum villous adenoma
{: .text-alpha }

## Resumen en Una Frase

Tegafur es un profármaco oral del 5-fluorouracilo (5-FU), originalmente utilizado para el tratamiento del cáncer gástrico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Cecum villous adenoma |
| Puntaje de Predicción TxGNN | 0.9986 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Tegafur es (traducción no oficial): «Inhibidor del ARN; inhibidor de la timidilato sintasa; inhibidor del ADN». Texto original en inglés: "RNA inhibitor; Thymidylate synthase inhibitor; DNA inhibitor" ([ChEMBL CHEMBL20883 (tegafur): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL20883), CC BY-SA 3.0; consultado el 2026-11-19). Según la información conocida, tegafur es un profármaco del 5-FU, un antimetabolito que inhibe la timidilato sintasa. Su eficacia en cáncer gástrico está establecida y, mecanísticamente, es aplicable al cáncer de colon, un tumor clásicamente sensible a las fluoropirimidinas.

Tegafur se usa en regímenes orales establecidos: UFT (tegafur-uracilo), donde el uracilo inhibe la degradación del 5-FU mediada por DPD, y S-1 (tegafur con gimeracilo y oteracilo). Ambos se han estudiado ampliamente en cáncer colorrectal.

Conviene señalar que el fármaco ya se emplea clínicamente en este contexto, por lo que se trata más de una extensión de indicación dentro de la misma familia de cánceres (adenocarcinoma gastrointestinal) que de un reposicionamiento verdaderamente novedoso.

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes de los 16 compilados.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00378716](https://clinicaltrials.gov/study/NCT00378716) | Fase 3 | Completado | 1608 | UFT + leucovorina vs. 5-FU + leucovorina en cáncer de colon resecado estadio II/III |
| [NCT00152230](https://clinicaltrials.gov/study/NCT00152230) | Fase 3 | Completado | 900 | UFT adyuvante vs. cirugía sola en cáncer colorrectal Dukes C (NSAS-CC) |
| [NCT00392899](https://clinicaltrials.gov/study/NCT00392899) | Fase 3 | Completado | 2025 | UFT adyuvante vs. observación en cáncer de colon estadio II resecado |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Fase 3 | Completado | 1535 | UFT + leucovorina vs. TS-1 como adyuvante en cáncer de colon estadio III |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Fase 3 | Desconocido | 1191 | SOX (oxaliplatino + S-1) vs. XELOX como adyuvante en cáncer colorrectal estadio III |
| [NCT00385970](https://clinicaltrials.gov/study/NCT00385970) | Fase 3 | Desconocido | 380 | UFT + PSK vs. UFT + leucovorina en cáncer colorrectal estadio IIB/III |
| [NCT00209742](https://clinicaltrials.gov/study/NCT00209742) | Fase 3 | Desconocido | 340 | Comparación de UFT+LV, UFT+LV/UFT y UFT+LV+PSK/UFT+PSK en estadio III |
| [NCT00905047](https://clinicaltrials.gov/study/NCT00905047) | Fase 3 | Completado | 89 | Estudio cruzado de preferencia: capecitabina vs. UFT con ácido folínico en cáncer colorrectal avanzado |
| [NCT01225744](https://clinicaltrials.gov/study/NCT01225744) | Fase 2 | Completado | 47 | Cetuximab, irinotecán, oxaliplatino y UFT en primera línea de cáncer colorrectal metastásico |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Fase 2 | Desconocido | 40 | S-1 + bevacizumab en cáncer colorrectal irresecable o recurrente tras fracaso previo |

## Evidencia de Literatura

Se muestran las 10 publicaciones más relevantes de las 20 compiladas.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | Cohorte nacional y metaanálisis | Medicine | UFT vs. 5-FU como adyuvante en cáncer de colon estadio II/III (base de datos de seguros de Taiwán) |
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | ECA fase 3 | Clin Colorectal Cancer | SOX vs. UFT/LV como adyuvante en cáncer de colon estadio III de alto riesgo (ACTS-CC 02) |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | ECA fase 3 (seguimiento) | ESMO Open | Supervivencia a 5 años de ACTS-CC 02: SOX no fue superior a UFT/LV en supervivencia libre de enfermedad |
| [10089948](https://pubmed.ncbi.nlm.nih.gov/10089948/) | 1999 | Metaanálisis de datos individuales | Jpn J Clin Oncol | Fluoropirimidinas orales como adyuvante tras resección curativa de cáncer colorrectal |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Revisión | Surg Today | UFT como quimioterapia adyuvante en tumores sólidos: evidencia clínica y mecanismo de acción |
| [16111469](https://pubmed.ncbi.nlm.nih.gov/16111469/) | 2005 | Revisión | Expert Rev Anticancer Ther | Opciones de quimioterapia por estadio en cáncer de colon |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Consenso/guía | Clin Colorectal Cancer | Adaptación de guías internacionales para cáncer colorrectal metastásico en Asia |
| [36676634](https://pubmed.ncbi.nlm.nih.gov/36676634/) | 2022 | Cohorte | Medicina (Kaunas) | Beneficio de UFT adyuvante en cáncer de colon estadio IIA frente a observación |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | ECA | Int J Clin Oncol | Inmunoquimioterapia (OK-432) y quimioterapia adyuvante con pirimidinas orales (HCFU, UFT) en cáncer colorrectal |
| [11320674](https://pubmed.ncbi.nlm.nih.gov/11320674/) | 2001 | Reporte de caso (evento adverso) | Cancer Chemother Pharmacol | Anemia hemolítica asociada a UFT en cáncer de colon metastásico |

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 54192 | UTEFOS 400 mg CAPSULAS DURAS | CÁPSULA DURA | Mylan Pharmaceuticals S.L. | Comercializada |

Se muestra la única autorización con este principio activo en los datos de CIMA (AEMPS).

<!-- licenses:end -->

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, clase fluoropirimidina; profármaco del 5-FU) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal (recomendación general para fluoropirimidinas) |
| Protección en Manejo | Seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Advertencias de la literatura**: se ha descrito un caso de anemia hemolítica asociada a UFT en un paciente con cáncer de colon metastásico (reporte de caso).
- **Interacciones farmacológicas**: no se encontraron interacciones registradas en la consulta realizada.

Para el resto de la información de seguridad (advertencias y contraindicaciones oficiales), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Varios ECA de fase 3 completados (por ejemplo, NCT00378716, NCT00152230, NCT00392899 y NCT00660894) evalúan directamente regímenes con tegafur en cáncer de colon, lo que respalda un nivel de evidencia L1. Sin embargo, la mayoría de la evidencia procede de UFT o S-1 y no de tegafur en monoterapia, y faltan los datos oficiales de seguridad de la autorización española.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), que es un requisito previo para el cribado de seguridad.
- Obtener datos del mecanismo de acción desde DrugBank.
- Confirmar el texto de indicación aprobado de la autorización 54192 (UTEFOS) y su coherencia con el uso en cáncer de colon.
- Revisar los resultados publicados de los ensayos de fase 3 completados para confirmar eficacia y perfil de seguridad.
- Plan de monitoreo hematológico y de toxicidad, con atención a la actividad de DPD.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; la versión anterior se guarda en el registro) | [ChEMBL CHEMBL20883 (tegafur): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL20883) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Fuentes de datos
nav_order: 93
permalink: /sources/
description: "Fuentes de datos en las que se basa ESTxGNN: datos de registro de la AEMPS, TxGNN, ClinicalTrials.gov, PubMed y DrugBank."
---

# Fuentes de datos

<div class="key-takeaway">
Cada conclusión puede rastrearse hasta una fuente de datos pública: nada es una caja negra.
</div>

---

## Resumen de fuentes

<table class="comparison-table">
<thead>
<tr><th>Tipo</th><th>Fuente</th><th>Uso</th></tr>
</thead>
<tbody>
<tr><td>Datos de registro</td><td><a href="https://www.aemps.gob.es/">AEMPS</a></td><td>Lista de medicamentos autorizados y principios activos de España</td></tr>
<tr><td>Modelo de predicción</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Predicción de asociaciones medicamento&ndash;enfermedad</td></tr>
<tr><td>Ensayos clínicos</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Gradación de la evidencia (NCT)</td></tr>
<tr><td>Literatura</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Gradación de la evidencia (PMID)</td></tr>
<tr><td>Información de medicamentos</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Asignación de principios activos y datos de dianas</td></tr>
<tr><td>Interacciones</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Datos de interacciones entre medicamentos</td></tr>
</tbody>
</table>

---

## Licencias

Cada fuente tiene su propia licencia; consúltela antes de citar:

- **TxGNN**: uso académico; cite a Huang et al. (2023)
- **ClinicalTrials.gov / PubMed**: datos públicos de los NIH de EE. UU.
- **DrugBank**: uso no comercial sujeto a sus condiciones de licencia
- **AEMPS**: sujeto a las condiciones de datos abiertos del organismo regulador de España

---

## Frecuencia de actualización

| Datos | Frecuencia |
|------|-----------|
| Datos de registro | Según los publique el organismo regulador |
| Evidencia de ensayos / literatura | Recopilada de nuevo periódicamente |
| Datos de interacciones | Revisados trimestralmente |

---

## Cita académica

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## Sobre el desarrollador

Esta plataforma está desarrollada y operada por **藥提醒科技有限公司** (yao.care, número de registro
mercantil 83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

ESTxGNN es el sitio de España de la línea de productos «TxGNN Drug Repurposing» de la empresa.
El mismo sistema está desplegado en 30 países y regiones, cada uno denominado `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN, etc.) en `{cc}txgnn.yao.care`.
Descripción general del producto: <https://www.yao.care/medical/txgnn/>.

El modelo TxGNN en sí fue desarrollado por el Zitnik Lab de Harvard Medical School y publicado
en *Nature Medicine*. Esta plataforma es el sistema de producción que 藥提醒科技有限公司 ha construido sobre ese
modelo, y abarca la integración de datos nacionales de registro de medicamentos, la predicción dual
mediante grafo de conocimiento y aprendizaje profundo, la gradación de la evidencia con PubMed /
ClinicalTrials y la integración con la historia clínica electrónica mediante SMART on FHIR.

---

<div class="disclaimer">
<strong>Descargo de responsabilidad</strong><br>
Este informe tiene únicamente fines de consulta para la investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste la medicación por su cuenta. Cualquier decisión de reposicionamiento de medicamentos requiere una validación clínica completa y una revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>

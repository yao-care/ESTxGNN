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

<!-- site-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
## España: datos de este sitio

Este sitio publica informes de **{{ site.data.drug_stats.total_drugs }}** medicamentos que figuran en los datos de registro de [AEMPS](https://www.aemps.gob.es/) (España).

Informes por nivel de evidencia:

| Nivel de evidencia | Informes | Proporción |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

32 pares medicamento–enfermedad predichos en este sitio no aparecen en ningún otro de los 30 sitios TxGNN.

<!-- site-data:end -->

## Resumen de fuentes

<table class="comparison-table">
<thead>
<tr><th>Tipo</th><th>Fuente</th><th>Uso</th></tr>
</thead>
<tbody>
<tr><td>Datos de registro</td><td><a href="https://www.aemps.gob.es/">AEMPS</a></td><td>Medicamentos autorizados en España, sus principios activos y su estado de autorización y comercialización (CIMA)</td></tr>
<tr><td>Modelo de predicción</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Predicción de asociaciones medicamento&ndash;enfermedad</td></tr>
<tr><td>Ensayos clínicos</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Gradación de la evidencia (NCT)</td></tr>
<tr><td>Literatura</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Gradación de la evidencia (PMID)</td></tr>
<tr><td>Información de medicamentos</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Asignación de principios activos y datos de dianas</td></tr>
<tr><td>Interacciones</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Datos de interacciones entre medicamentos</td></tr>
</tbody>
</table>

---

## Datos locales de este sitio

Los medicamentos de España y su estado proceden de CIMA, el servicio de información de medicamentos de
la AEMPS, a través de su API REST pública.

| Elemento | Detalle |
|------|---------|
| Conjunto de datos | CIMA: listado de medicamentos (API REST pública) |
| Publicador | AEMPS |
| Descarga | <https://cima.aemps.es/cima/rest/medicamentos> (se recorren todas las páginas) |
| Identificador de producto | Número de registro |
| Actualización | Descarga automática semanal (cada lunes); el estado se toma de CIMA: Revocada, Suspendida, Autorizada (comercializada) o Autorizada (no comercializada) |

---

## Licencias

Cada fuente tiene su propia licencia; consúltela antes de citar:

- **TxGNN**: uso académico; cite a Huang et al. (2024)
- **ClinicalTrials.gov / PubMed**: datos públicos de los NIH de EE. UU.
- **DrugBank**: uso no comercial sujeto a sus condiciones de licencia
- **AEMPS**: sujeto a las condiciones de datos abiertos del organismo regulador de España

---

## Frecuencia de actualización

| Datos | Frecuencia |
|------|-----------|
| CIMA de la AEMPS | Semanal (cada lunes) |
| Evidencia de ensayos / literatura | Recopilada de nuevo periódicamente |
| Datos de interacciones | Revisados trimestralmente |

---

## Cita académica

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

---

## Sobre el desarrollador

Esta plataforma está desarrollada y operada por **藥提醒科技有限公司** (yao.care). Consulte la página
<a href="{{ '/about/' | relative_url }}">Acerca de</a> para conocer los antecedentes completos de la empresa y de la metodología.

---

<div class="disclaimer">
<strong>Descargo de responsabilidad</strong><br>
Este informe tiene únicamente fines de consulta para la investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste la medicación por su cuenta. Cualquier decisión de reposicionamiento de medicamentos requiere una validación clínica completa y una revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>

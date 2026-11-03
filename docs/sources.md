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

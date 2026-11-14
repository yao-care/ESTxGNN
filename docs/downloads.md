---
layout: default
title: Descargas
nav_order: 94
permalink: /downloads/
description: "Descargas de datos abiertos de ESTxGNN: recursos FHIR, resultados de predicción e índice de búsqueda."
---

# Descargas

<div class="key-takeaway">
Las predicciones se publican en formato FHIR R4, listas para integrarse con sistemas de historia clínica electrónica.
</div>

---

<!-- site-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
## España: datos de este sitio

Este sitio publica informes de **{{ site.data.drug_stats.total_drugs }}** medicamentos que figuran en los datos de registro de [AEMPS](https://www.aemps.gob.es/) (España).

Conjunto de datos: [AEMPS: CIMA](https://cima.aemps.es/cima/rest/medicamentos); se descarga y se compara automáticamente cada semana (los lunes). Detalles: [Fuentes de datos]({{ '/sources/' | relative_url }}).

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

## Recursos FHIR

Este sitio publica las predicciones como recursos FHIR R4, consumibles directamente por aplicaciones SMART on FHIR:

| Recurso | Ruta | Descripción |
|----------|------|-------------|
| CapabilityStatement | `/fhir/metadata` | Declaración de capacidades del servidor FHIR |
| MedicationKnowledge | `/fhir/MedicationKnowledge/` | Recursos de medicamentos |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/` | Indicaciones predichas |
| Bundle | `/fhir/Bundle/all-predictions.json` | Todas las predicciones agrupadas |

---

## Índice de búsqueda

`/data/search-index.json` proporciona un índice de búsqueda de medicamentos e indicaciones para que construya su propia
interfaz de consulta.

---

## Condiciones de uso

<ol class="actionable-steps">
<li>Los datos de este sitio son <strong>solo para consulta con fines de investigación</strong> y no deben utilizarse como base para decisiones médicas.</li>
<li>Al citar, acredite a ESTxGNN (藥提醒科技有限公司) y cite el artículo original de TxGNN.</li>
<li>Los datos derivados siguen sujetos a las condiciones de licencia de cada fuente original (véase <a href="{{ '/sources/' | relative_url }}">Fuentes de datos</a>).</li>
</ol>

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

---
layout: default
title: Guía de uso
nav_order: 92
permalink: /guide/
description: "Guía de uso de ESTxGNN: cómo buscar medicamentos, leer los niveles de evidencia e interpretar las recomendaciones."
---

# Guía de uso

<div class="key-takeaway">
Consulte primero el nivel de evidencia, después la recomendación y, por último, lea la literatura de origen.
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

## Buscar un medicamento

<ol class="actionable-steps">
<li>Utilice el buscador situado en la parte superior de la página (los nombres genéricos de los principios activos coinciden mejor que los nombres comerciales).</li>
<li>O consulte la lista completa en <a href="{{ '/drugs/' | relative_url }}">Todos los medicamentos</a>.</li>
<li>También puede navegar por nivel de evidencia: <a href="{{ '/evidence-high/' | relative_url }}">alta</a>, <a href="{{ '/evidence-medium/' | relative_url }}">moderada</a>, <a href="{{ '/evidence-low/' | relative_url }}">solo predicción del modelo</a>.</li>
</ol>

---

## Cómo leer un informe

<p class="key-answer" data-question="¿Qué significan los niveles de evidencia L1 a L5?">
Cada informe de medicamento enumera las nuevas indicaciones predichas, y cada indicación lleva un nivel de
evidencia L1&ndash;L5. <strong>L1 significa que ya la respaldan múltiples ensayos controlados aleatorizados de fase 3; L5 significa
solo predicción del modelo, sin evidencia en humanos.</strong> Los criterios completos están en la página de
<a href="{{ '/methodology/' | relative_url }}">Metodología</a>.
</p>

| Si ve | Significa | Acción sugerida |
|-----------|----------|------------------|
| L1 / L2 | Existe evidencia de ensayos clínicos | Revise los registros NCT y PMID de origen |
| L3 / L4 | Evidencia observacional o preclínica | Trátelo como una pista de investigación |
| L5 | Solo predicción del modelo | Solo para generar hipótesis; no sirve de referencia clínica |

---

## Citación y trazabilidad

Cada elemento de evidencia de un informe lleva un identificador trazable:

- **Número NCT**: enlaza con el registro de ClinicalTrials.gov
- **PMID**: enlaza con el registro de PubMed
- **DrugBank ID**: enlaza con los datos de medicamentos y dianas

Lea la literatura de origen para confirmar el contexto antes de citar cualquier conclusión de esta plataforma.
Para la lista completa de bases de datos y registros utilizados, consulte <a href="{{ '/sources/' | relative_url }}">Fuentes de datos</a>.

---

## Preguntas frecuentes

<p class="key-answer" data-question="¿Pueden usarse las predicciones en la práctica clínica?">
<strong>No.</strong> Las predicciones de esta plataforma son pistas de investigación, no consejo clínico. Cualquier
aplicación clínica del reposicionamiento de medicamentos debe pasar por una validación completa mediante ensayos clínicos y
una revisión regulatoria.
</p>

<p class="key-answer" data-question="¿Por qué no encuentro un medicamento concreto?">
Un principio activo debe poder asignarse al vocabulario de DrugBank para incluirse en la predicción. Los extractos vegetales,
las vacunas, los excipientes y otros elementos no catalogados por DrugBank no aparecen en esta plataforma.
</p>

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

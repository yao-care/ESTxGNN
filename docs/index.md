---
layout: default
title: Predicciones de Reposicionamiento de Medicamentos
nav_order: 1
description: "Predicciones de reposicionamiento de medicamentos impulsadas por IA para España. Análisis basado en evidencia de medicamentos aprobados para posibles nuevas indicaciones terapéuticas."
permalink: /
---

# Predicciones de Reposicionamiento de Medicamentos — España

Este proyecto utiliza el modelo TxGNN (aprendizaje profundo) para predecir posibles nuevos usos terapéuticos para medicamentos aprobados en España.

**Descargo de Responsabilidad**: Este contenido es solo para fines de investigación y no constituye consejo médico. Todas las predicciones de reposicionamiento de medicamentos requieren validación clínica antes de su aplicación.

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## España: qué cubre este sitio

Este sitio publica informes de **{{ site.data.drug_stats.total_drugs }}** medicamentos que figuran en los datos de registro de [AEMPS](https://www.aemps.gob.es/) (España).

### Datos locales de este sitio

| Elemento | Detalle |
|------|---------|
| Conjunto de datos | CIMA: listado de medicamentos (API REST pública) |
| Publicador | AEMPS |
| Descarga | <https://cima.aemps.es/cima/rest/medicamentos> (se recorren todas las páginas) |
| Identificador de producto | Número de registro |
| Actualización | Descarga automática semanal (cada lunes); el estado se toma de CIMA: Revocada, Suspendida, Autorizada (comercializada) o Autorizada (no comercializada) |

Detalles: [Fuentes de datos]({{ '/sources/' | relative_url }}).

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

### Medicamentos con mayor nivel de evidencia en este sitio

| Medicamento | Nivel de evidencia |
|---|---|
| [Bendamustine](/drugs/bendamustine/) | L1 |
| [Bromfenac](/drugs/bromfenac/) | L1 |
| [Bupropion](/drugs/bupropion/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Grazoprevir](/drugs/grazoprevir/) | L1 |
| [Ribavirin](/drugs/ribavirin/) | L1 |
| [Clofarabine](/drugs/clofarabine/) | L1 |
| [Doxorubicin](/drugs/doxorubicin/) | L1 |
| [Ketorolac](/drugs/ketorolac/) | L1 |
| [Tacrolimus](/drugs/tacrolimus/) | L1 |

### Medicamentos que solo cubre este sitio entre los 30 sitios TxGNN

| Medicamento | Nivel de evidencia |
|---|---|
| [Niflumic Acid](/drugs/niflumic-acid/) | L5 |
| [Bentazepam](/drugs/bentazepam/) | L5 |
| [Tramazoline](/drugs/tramazoline/) | L5 |
| [Brotizolam](/drugs/brotizolam/) | L5 |
| [Medazepam](/drugs/medazepam/) | L5 |
| [Almasilate](/drugs/almasilate/) | L5 |
| [Vincamine](/drugs/vincamine/) | L5 |

<!-- local-home:end -->

## Sobre el desarrollador

Esta plataforma está desarrollada y operada por **藥提醒科技有限公司** (yao.care). Consulte la página
<a href="{{ '/about/' | relative_url }}">Acerca de</a> para conocer los antecedentes completos de la empresa y de la metodología.

---
layout: default
title: Todos los medicamentos
nav_order: 20
permalink: /drugs/
description: "Todos los informes de validación de medicamentos y las estadísticas de niveles de evidencia de ESTxGNN."
---
{% assign l1_count = site.drugs | where: "evidence_level", "L1" | size %}
{% assign l2_count = site.drugs | where: "evidence_level", "L2" | size %}
{% assign l3_count = site.drugs | where: "evidence_level", "L3" | size %}
{% assign l4_count = site.drugs | where: "evidence_level", "L4" | size %}
{% assign l5_count = site.drugs | where: "evidence_level", "L5" | size %}

# Todos los medicamentos

{{ site.drugs.size }} informes de validación de medicamentos

---

## Desglose por nivel de evidencia

| Nivel de evidencia | Medicamentos | Descripción |
|---------|--------|------|
| **L1** | {{ l1_count }} | Múltiples ECA / revisiones sistemáticas |
| **L2** | {{ l2_count }} | Un único ECA / ensayos de fase 2 |
| **L3** | {{ l3_count }} | Estudios observacionales / series de casos amplias |
| **L4** | {{ l4_count }} | Estudios preclínicos / mecanicistas |
| **L5** | {{ l5_count }} | Solo predicción del modelo |

---

## Lista completa de medicamentos

{% assign all_drugs = site.drugs | sort: 'title' %}

| Medicamento | Nivel de evidencia | Indicaciones |
|---------|---------|---------|
{% for drug in all_drugs %}| [{{ drug.title }}]({{ drug.url | relative_url }}) | {{ drug.evidence_level }} | {{ drug.indication_count }} |
{% endfor %}

---

<div class="disclaimer">
<strong>Descargo de responsabilidad</strong><br>
Este informe tiene únicamente fines de consulta para la investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste la medicación por su cuenta. Cualquier decisión de reposicionamiento de medicamentos requiere una validación clínica completa y una revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>

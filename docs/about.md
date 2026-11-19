---
layout: default
title: Acerca de
nav_order: 90
permalink: /about/
description: "ESTxGNN es una plataforma de predicción de reposicionamiento de medicamentos desarrollada por 藥提醒科技有限公司 (yao.care), construida sobre el modelo TxGNN de Harvard, que cubre los medicamentos autorizados por la AEMPS en España."
---

# Acerca de

<div class="key-takeaway">
Acelerar la validación de la evidencia del reposicionamiento de medicamentos con IA: de la predicción a la evidencia de un vistazo.
</div>

---

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## España: los datos de este sitio en cifras

Datos locales: [AEMPS: CIMA](https://cima.aemps.es/cima/rest/medicamentos). Los datos locales son las autorizaciones de la AEMPS en CIMA, que distingue medicamentos comercializados, autorizados no comercializados y revocados o suspendidos. Aquí solo cuentan como vigentes los comercializados; los autorizados no comercializados se cuentan aparte.

| Concepto | Valor |
|---|---|
| Medicamentos con informe publicado | {{ site.data.local_facts.drugs_total }} |
| Medicamentos presentes en los datos locales | {{ site.data.local_facts.licence.drugs_with_data }} |
| …con al menos un registro comercializadas | {{ site.data.local_facts.licence.drugs_with_current }} |
| …con registros pero ninguno comercializadas | {{ site.data.local_facts.licence.drugs_none_current }} |
| Medicamentos ausentes de los datos locales | {{ site.data.local_facts.licence.drugs_without_data }} |
| Registros locales (autorizaciones de la AEMPS (CIMA)) | {{ site.data.local_facts.licence.items_total }} |
| …de ellos comercializadas | {{ site.data.local_facts.licence.items_current }} |
| Entradas del registro de revisiones | {{ site.data.local_facts.reviews.records }} |
| Páginas con entradas de revisión | {{ site.data.local_facts.reviews.public_pages_with_records }} |
| Pares medicamento–enfermedad predichos que no figuran en ningún otro sitio TxGNN | {{ site.data.local_facts.cross.unique_pairs }} |

{% if site.data.local_facts.top_licensed.size > 0 %}Medicamentos con más autorizaciones de la AEMPS (CIMA) comercializadas: {% for r in site.data.local_facts.top_licensed %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.lv }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Últimas correcciones del registro de revisiones: {% for r in site.data.local_facts.recent_reviews limit: 8 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

Ejemplos de predicciones que ningún otro sitio TxGNN incluye para el mismo medicamento: [Almasilate]({{ '/drugs/almasilate/' | relative_url }}) → gastroduodenitis, [Bentazepam]({{ '/drugs/bentazepam/' | relative_url }}) → insomnio, [Brotizolam]({{ '/drugs/brotizolam/' | relative_url }}) → Delirio por abstinencia de alcohol, [Medazepam]({{ '/drugs/medazepam/' | relative_url }}) → insomnio, [Niflumic Acid]({{ '/drugs/niflumic-acid/' | relative_url }}) → Raynaud disease, [Tramazoline]({{ '/drugs/tramazoline/' | relative_url }}) → Urticaria alérgica, [Vincamine]({{ '/drugs/vincamine/' | relative_url }}) → subarachnoid hemorrhage (disease).

<!-- local-facts:end -->

## Contexto

<p class="key-answer" data-question="¿Qué es ESTxGNN?">
<strong>ESTxGNN</strong> es una plataforma de apoyo a la investigación en reposicionamiento de medicamentos,
construida sobre el modelo TxGNN publicado en <em>Nature Medicine</em> por el Zitnik Lab de la Universidad
de Harvard. Predice la ampliación de indicaciones de los medicamentos autorizados por la AEMPS en España.
Más allá de las puntuaciones de predicción de la IA, la plataforma integra evidencia clínica de
ClinicalTrials.gov y PubMed para que los investigadores puedan evaluar rápidamente su credibilidad.
</p>

<p class="key-answer" data-question="¿Qué medicamentos autorizados por la AEMPS se están probando ya en ensayos clínicos para una indicación nueva?">
La <a href="{{ '/drugs/' | relative_url }}">lista completa de medicamentos</a> de esta plataforma recoge, para cada medicamento autorizado por la AEMPS, si ya existen ensayos clínicos registrados en ClinicalTrials.gov que investigan una indicación nueva no autorizada. Cada ficha enlaza los NCT de origen junto con el nivel de evidencia correspondiente.
</p>

Consulte el <a href="/methodology/">proceso de predicción y gradación de la evidencia</a> o la
<a href="/guide/">guía de uso</a> para saber cómo leer un informe de medicamento.

---

<!-- local-condensed:start（母目錄 .claude/gen_local_pages_20261119.py；原共用段落縮寫，勿手改）-->
## Sobre el desarrollador

Esta plataforma la desarrolla y opera **藥提醒科技有限公司** (yao.care, registro 83620786, Taichung, Taiwán) como uno de los 30 sitios por país y región de su línea de productos TxGNN ([presentación del producto](https://www.yao.care/medical/txgnn/)).

---

## El método en breve

Las predicciones provienen de TxGNN, un modelo de redes neuronales de grafos del Zitnik Lab de la Facultad de Medicina de Harvard (Huang et al., *Nature Medicine* 2024, [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)); cada indicación predicha se clasifica de L1 a L5 con ClinicalTrials.gov y PubMed. Modelo, niveles y reglas: [Metodología]({{ '/methodology/' | relative_url }}). Conjuntos de datos, descargas y licencias: [Fuentes de datos]({{ '/sources/' | relative_url }}).
<!-- local-condensed:end -->

---

## Contacto

- **GitHub Issues**: <https://github.com/yao-care/ESTxGNN/issues>
- **Desarrollador**: 藥提醒科技有限公司 (<https://www.yao.care>, service@yao.care)
- **Descripción general del producto**: <https://www.yao.care/medical/txgnn/>

---

<div class="disclaimer">
<strong>Descargo de responsabilidad</strong><br>
Este informe tiene únicamente fines de consulta para la investigación académica y <strong>no constituye consejo médico</strong>. Siga siempre las indicaciones de su médico; nunca ajuste la medicación por su cuenta. Cualquier decisión de reposicionamiento de medicamentos requiere una validación clínica completa y una revisión regulatoria.
<br><br>
<small>Revisado por: 藥提醒科技有限公司 (yao.care)</small>
</div>

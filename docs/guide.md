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

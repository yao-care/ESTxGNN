---
layout: default
title: Brotizolam
parent: Solo predicción del modelo (L5)
nav_order: 85
evidence_level: L5
indication_count: 6
---

# Brotizolam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Brotizolam: De Indicación Original No Registrada a Insomnio

## Resumen en Una Frase

Brotizolam es una benzodiazepina de acción corta (tienotriazolodiazepina) con efecto sedante-hipnótico. En España se comercializa como SINTONAL 0,25 mg comprimidos, pero los datos disponibles no recogen su texto de indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **insomnio**, con **3 ensayos clínicos** y **3 publicaciones** asociados. Es la confirmación de un uso ya establecido en otras regiones (Lendormin), no un reposicionamiento novedoso.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrada en los datos de AEMPS (el texto de indicación está vacío) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99,94% |
| Nivel de Evidencia | L2 (ver nota) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

> **Nota sobre el nivel de evidencia:** el Evidence Pack indica L1, pero solo un ECA de Fase 3 está completado y con brotizolam de forma directa (NCT00347295). El otro ensayo de Fase 3 (NCT02776228) tiene estado desconocido y no es específico de brotizolam. Según las reglas (L1 exige ≥2 ECAs de Fase 3 completados), corresponde **L2**.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados de mecanismo de acción en DrugBank. Según la información de la literatura, brotizolam es un modulador alostérico positivo del receptor GABA-A. Al potenciar la señalización GABAérgica inhibitoria produce efectos sedantes e hipnóticos. Estudios preclínicos también describen actividad ansiolítica, anticonvulsiva y miorrelajante.

El insomnio es precisamente el uso para el que brotizolam se desarrolló como hipnótico, y ya está comercializado con esa finalidad en otras regiones. Los estudios clínicos muestran mejoría de la estructura y la duración del sueño, y una eficacia comparable a la de otros hipnóticos como el triazolam.

Por tanto, esta predicción es coherente con el mecanismo y con la evidencia clínica existente. Su valor principal es confirmar un uso establecido. Como la indicación aprobada por AEMPS no consta en los datos, conviene verificarla en la ficha técnica oficial.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00347295](https://clinicaltrials.gov/study/NCT00347295) | Fase 3 | Completado | 253 | ECA doble ciego, doble simulación, multicéntrico: brotizolam (Lendormin) frente a estazolam en pacientes ambulatorios con insomnio (seguridad y eficacia) |
| [NCT02224014](https://clinicaltrials.gov/study/NCT02224014) | N/A | Completado | 485 | Encuesta poscomercialización de Lendormin D: seguridad y eficacia en insomnio en práctica clínica habitual |
| [NCT02776228](https://clinicaltrials.gov/study/NCT02776228) | Fase 3 | Desconocido | 200 | Tratamiento corto con benzodiazepinas tras cirugía cardíaca y prevalencia de insomnio; no es específico de brotizolam |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26171909](https://pubmed.ncbi.nlm.nih.gov/26171909/) | 2015 | Revisión sistemática | Cochrane Database of Systematic Reviews | Efectos de opioides, hipnóticos y sedantes sobre la respiración durante el sueño en adultos con apnea obstructiva del sueño; relevante para la seguridad |
| [8992838](https://pubmed.ncbi.nlm.nih.gov/8992838/) | 1996 | Estudio clínico | Zh Nevrol Psikhiatr Im S S Korsakova | En 25 pacientes con insomnio neurótico, 0,25 mg durante 10 días mejoraron la estructura del sueño (duración y eficiencia) y la valoración subjetiva |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Revisión | Acta Psychiatr Scand Suppl | Uso clínico de hipnóticos: indicaciones y necesidad de contar con distintos perfiles farmacocinéticos de benzodiazepinas |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 58229 | SINTONAL 0,25 mg comprimidos | Comprimido | No especificada en los datos disponibles |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ECA de Fase 3 completado (n=253), una encuesta poscomercialización (n=485) y estudios clínicos que respaldan el uso hipnótico de brotizolam en insomnio. Se trata de un uso ya establecido, pero las salvaguardas de seguridad de las benzodiazepinas siguen siendo necesarias y faltan los datos de ficha técnica de AEMPS.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de AEMPS (indicación aprobada, advertencias y contraindicaciones), un vacío de datos bloqueante para el cribado de seguridad.
- Confirmar el mecanismo de acción en DrugBank.
- Confirmar que el ensayo NCT00347295 y la publicación PMID 23025837 (ECA doble ciego en pacientes ambulatorios con insomnio) corresponden al mismo estudio, y verificar comparador y criterio de valoración principal.
- Aplicar las salvaguardas siguientes:
  - Riesgo de dependencia y tolerancia.
  - Sedación al día siguiente.
  - Depresión respiratoria, sobre todo en trastornos respiratorios del sueño.
  - Precaución en personas mayores.

Las demás indicaciones predichas (delirio por abstinencia alcohólica, abuso de antidepresivos, de barbitúricos y de alucinógenos, y ansiedad) tienen evidencia L4-L5 y recomendación Hold o Research Question. No se evalúan en este informe.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


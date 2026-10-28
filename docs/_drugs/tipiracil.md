---
layout: default
title: Tipiracil
parent: Solo predicción del modelo (L5)
nav_order: 797
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "tipiracil"
predicted_indications: ["cecum villous adenoma", "lipoma of colon", "rectosigmoid junction neoplasm", "cecum neuroendocrine tumor G1", "colonic lymphangioma", "cecal disease", "colon leiomyoma", "benign neoplasm of cecum", "cavernous hemangioma of colon", "colorectal gastrointestinal stromal tumor"]
description: "Tipiracil: nueva indicación predicha, Cecum villous adenoma (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Tipiracil
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Tipiracil: Cecum villous adenoma
{: .text-alpha }

## Resumen en Una Frase

Tipiracilo es un componente de la combinación trifluridina/tipiracilo (Lonsurf), utilizada originalmente para el tratamiento del cáncer colorrectal.
El modelo TxGNN predice que podría ser efectivo para **adenoma velloso del ciego**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Cecum villous adenoma |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 4 de 6) |
| Número de Autorizaciones | 6 (vigentes: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, tipiracilo es un inhibidor de la timidina fosforilasa que se administra junto con trifluridina (TAS-102): evita la degradación de la trifluridina y aumenta su exposición. La trifluridina, un análogo nucleosídico de timidina, se incorpora al ADN y ejerce el efecto citotóxico.

El adenoma velloso es una lesión benigna precursora del cáncer colorrectal, por lo que la relación con la indicación original es solo anatómica y de continuidad de la enfermedad. El puntaje del modelo es muy alto, pero no está respaldado por ensayos ni literatura.

Desde el punto de vista clínico, la predicción es débil: estas lesiones se tratan habitualmente mediante resección endoscópica, y un tratamiento citotóxico no resulta racional para una lesión benigna. La predicción debe considerarse una hipótesis, no una indicación realista.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1161096001 | LONSURF 15 MG/6,14 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 1161096006 | LONSURF 20 MG/8,19 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 1161096003 | LONSURF 15 MG/6,14 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 1161096001IP | LONSURF 15 MG/6,14 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 1161096003IP | LONSURF 15 MG/6,14 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |

Titular: Les Laboratoires Servier. Hay una autorización adicional (1161096004, Lonsurf 20 mg/8,19 mg), hasta completar las 6 vigentes.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (combinación de análogo nucleosídico de timidina con inhibidor de timidina fosforilasa) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto (en la literatura se describen leucopenia y neutropenia con la combinación) |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 14 registros de interacción, 13 de ellos de nivel moderado. Entre los principales: cimetidina, tafenoquina, ketoconazol, brigatinib, crizotinib, encorafenib, etinilestradiol, lenvatinib, acetato de medroxiprogesterona, acetato de megestrol, ribociclib, rucaparib y vandetanib. El registro restante corresponde a una anotación farmacológica de unión a la proteína no estructural 15 de coronavirus (SARS-CoV-2), sin nivel de gravedad clínica asignado.
- Un caso publicado describe vasculitis leucocitoclástica con púrpura de Henoch-Schönlein de aparición tardía tras el tratamiento con trifluridina/tipiracilo (PMID 30677817).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos ni literatura, y carece de lógica clínica: se trataría una lesión benigna, manejada con resección endoscópica, con un citotóxico. El riesgo-beneficio es desfavorable.

**Para avanzar se necesita:**
- Datos del mecanismo de acción verificados (DrugBank)
- Prospecto de la AEMPS con advertencias y contraindicaciones
- Evidencia preclínica o clínica específica en adenoma velloso
- Una justificación clínica de por qué un citotóxico sería preferible a la resección endoscópica

**Nota sobre otras predicciones:** *neoplasia de la unión rectosigmoidea* y *enfermedad cecal* (nivel L4) son subsitios anatómicos del cáncer colorrectal ya aprobado, por lo que no constituyen un reposicionamiento real. Las demás predicciones (lipoma de colon, tumor neuroendocrino G1 del ciego, linfangioma, leiomioma, hemangioma cavernoso, GIST colorrectal) carecen de respaldo mecanístico y de evidencia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


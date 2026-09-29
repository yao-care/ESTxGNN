---
layout: default
title: Emedastine
parent: Solo predicción del modelo (L5)
nav_order: 197
evidence_level: L5
indication_count: 2
---

# Emedastine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Emedastina: De Indicación Original No Registrada a Urticaria Alérgica

## Resumen en Una Frase

Emedastina es un antihistamínico antagonista selectivo de los receptores H1. En España está comercializada como colirio (Emadine), pero los datos recibidos no incluyen su indicación aprobada.
El modelo TxGNN predice que podría ser eficaz para la **urticaria alérgica**, con **0 ensayos clínicos registrados** y **4 publicaciones** que respaldan esta dirección, entre ellas un ensayo aleatorizado en urticaria crónica idiopática.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99,96 % |
| Nivel de Evidencia | L2 (un ECA publicado frente a loratadina, con emedastina oral; fase no indicada) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la literatura recuperada (PMID 19558341), la emedastina es un antagonista selectivo del receptor H1 de histamina. Tiene una actividad anticolinérgica mínima y se ha usado en rinitis alérgica, conjuntivitis alérgica, urticaria, dermatitis alérgica y prurito. Este dato conviene verificarlo en DrugBank.

En la urticaria, la liberación de histamina por los mastocitos causa los habones y el picor. Bloquear el receptor H1 es, por tanto, un mecanismo plausible y coherente con el alto puntaje del modelo. La relación con la indicación original no se puede evaluar, porque esa indicación no figura en los datos.

La literatura sugiere además un posible efecto sobre la remodelación tisular en enfermedades alérgicas, pero es un efecto secundario al mecanismo H1. También se predice la **urticaria por frío** (puntaje 99,82 %). Esa predicción se apoya solo en el efecto de clase de los antihistamínicos y no tiene evidencia específica de emedastina.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|---------|
| [17229605](https://pubmed.ncbi.nlm.nih.gov/17229605/) | 2006 | ECA | Eur J Dermatol | Emedastina difumarato oral (2 mg dos veces al día) frente a loratadina (10 mg al día) durante 4 semanas en 192 pacientes con urticaria crónica idiopática. A la semana, más pacientes con emedastina tenían 0-10 % de afectación cutánea (57,1 % vs 38,2 %; p = 0,0019) y puntuación total de síntomas de 0-1 (83,3 % vs 64,5 %; p = 0,0134). |
| [19558341](https://pubmed.ncbi.nlm.nih.gov/19558341/) | 2009 | Revisión | Expert Opin Pharmacother | Revisión de la emedastina como antihistamínico H1 selectivo en enfermedades alérgicas (incluida la urticaria), sin efectos cardiovasculares adversos y con actividad anticolinérgica mínima. Explora un posible efecto sobre la remodelación tisular. |
| [24720119](https://pubmed.ncbi.nlm.nih.gov/24720119/) | 2013 | Revisión | Przegl Lek | Análisis de las discrepancias entre las guías de expertos, las fichas técnicas y la evidencia de eficacia de los fármacos en urticaria. |
| [14499249](https://pubmed.ncbi.nlm.nih.gov/14499249/) | 2003 | Preclínico (murino) | Clin Immunol | Estudio en ratones sobre el efecto de antialérgicos y antihistamínicos, entre ellos la emedastina, en la eosinofilia cutánea en sensibilidad por contacto. Es indirecto para la urticaria. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 98095001IP | EMADINE 0,5 MG/ML COLIRIO EN SOLUCIÓN | Colirio en solución | Alcon Laboratories Ltd (UK) |
| 98095001 | EMADINE 0,5 MG/ML COLIRIO EN SOLUCIÓN | Colirio en solución | Immedica Pharma AB |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La emedastina tiene un mecanismo plausible y un ECA positivo en urticaria crónica idiopática, pero con la forma oral. En España solo hay un colirio autorizado, así que la vía de administración no es compatible con la indicación predicha. Además, faltan los datos de seguridad del prospecto (bloqueante para el cribado de seguridad).

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones).
- Confirmar el mecanismo de acción en DrugBank.
- Verificar si existe una formulación oral disponible o autorizable en España, ya que la evidencia clínica corresponde a la vía oral.
- Confirmar la fase del ECA de 2006 y revisar la evidencia complementaria (ensayos registrados o literatura adicional).
- Para urticaria por frío, no avanzar salvo que aparezca evidencia específica (nivel L5, Hold).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


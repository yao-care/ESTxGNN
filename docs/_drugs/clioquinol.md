---
layout: default
title: Clioquinol
parent: Evidencia moderada (L3-L4)
nav_order: 190
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-14
description: "Clioquinol: nueva indicación predicha, Candidiasis cutánea (nivel de evidencia L4). Indicación original: Tiña del pie, tiña del cuerpo, tiña…"
monitor_inn: "clioquinol"
predicted_indications: ["Majocchi granuloma", "ectothrix infectious disease", "endothrix infectious disease"]
---

# Clioquinol
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **7** 
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

## Clioquinol: De Dermatofitosis (Tiña del Pie y del Cuerpo) a Candidiasis Cutánea
{: .text-alpha }

## Resumen en Una Frase

Clioquinol es un derivado halogenado de la 8-hidroxiquinolina, utilizado originalmente como antifúngico y antibacteriano tópico en infecciones dermatofíticas como la tiña del pie y la tiña del cuerpo.
El modelo TxGNN predice que podría ser efectivo para **candidiasis cutánea**, pero actualmente no hay ensayos clínicos y solo existe **1 publicación**, de carácter indirecto, que respalda esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tiña del pie, tiña del cuerpo, tiña, dermatofitosis de la ingle y la zona perianal (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Candidiasis cutánea |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, clioquinol es un compuesto quelante de metales (cobre, zinc y hierro) con actividad antifúngica y antibacteriana, su uso en dermatofitosis superficiales está establecido, y mecanísticamente podría ser aplicable a la candidiasis cutánea.

La alteración de la homeostasis metálica en las células fúngicas podría extenderse razonablemente a especies de *Candida*. Tanto las dermatofitosis como la candidiasis cutánea son infecciones fúngicas superficiales de la piel, lo que apoya la plausibilidad de la predicción.

Este vínculo es una inferencia y no un hecho establecido: la única literatura disponible es un artículo de 1988 sobre prevención de la infección ocupacional por *Candida albicans*, que constituye evidencia indirecta.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2978600](https://pubmed.ncbi.nlm.nih.gov/2978600/) | 1988 | Informe de prevención/salud ocupacional (no ECA) | Przeglad dermatologiczny | Estudio in vitro de aditivos para jabones de tocador frente a cepas de *C. albicans* aisladas de pacientes; evalúa el efecto fungicida y las propiedades del jabón. Evidencia indirecta |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 54860 | MENADERM OTOLOGICO 0,25 mg/10 mg/ml gotas óticas en solución | Gotas óticas en solución | No disponible |
| 52444 | MENADERM CLIO 0,25 mg/30 mg/g CREMA | Crema | No disponible |
| 51784 | CUATROCREM CREMA | Crema | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): insuficiencia suprarrenal, enfermedad de Addison, atrofia cutánea, telangiectasia, enfermedad capilar, telangiectasia hemorrágica hereditaria, enfermedad vascular periférica, claudicación intermitente y enfermedad arterial periférica. Varias de ellas probablemente reflejen componentes corticoides de las asociaciones y no clioquinol por sí solo; deben verificarse.
- **Precaución por historial de neurotoxicidad**: el uso oral de clioquinol se asoció con SMON (neuropatía mielo-óptica subaguda).
- **Interacciones farmacológicas**: no se encontraron interacciones registradas.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones oficiales no disponibles).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en TxGNN, pero la evidencia se limita a un artículo de 1988 de relevancia indirecta, sin ensayos clínicos y con mecanismo de acción no confirmado. Por ahora se trata de una pregunta de investigación.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicaciones autorizadas), lo que actualmente bloquea el cribado de seguridad
- Completar los datos del mecanismo de acción (consulta a DrugBank)
- Estudios in vitro de actividad de clioquinol frente a *Candida* spp. y, de resultar favorables, ensayos clínicos en candidiasis cutánea
- Evaluar la seguridad de la exposición tópica, dado el historial de neurotoxicidad

**Nota sobre otras predicciones:** la indicación **micosis superficial** (TxGNN 99.18%, nivel L4) cuenta con un estudio preclínico de 2021 (*Mycoses*, PMID [33772895](https://pubmed.ncbi.nlm.nih.gov/33772895/)) que evaluó clioquinol combinado con ciclopirox y terbinafina en modelos alternativos de dermatofitosis, con datos de actividad y toxicidad. Es la que presenta mejor ajuste mecanístico con las indicaciones actuales. Las demás (granuloma de Majocchi, enfermedades ectothrix y endothrix, dermatofitosis de cuero cabelludo o barba, tiña profunda) son solo predicciones del modelo (L5), con penetración tópica limitada en folículo y tejido profundo, por lo que se recomienda mantenerlas en espera.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


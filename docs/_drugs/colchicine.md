---
layout: default
title: Colchicine
parent: Solo predicción del modelo (L5)
nav_order: 206
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Colchicine: nueva indicación predicha, Malaria por Plasmodium falciparum (nivel de evidencia L5). Indicación original: Gota y fiebre mediterránea familiar (según las indicaciones originale…"
monitor_inn: "Colchicine"
predicted_indications: ["Plasmodium falciparum malaria", "dermatofibrosarcoma protuberans"]
---

# Colchicine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Colchicina: De Gota a Malaria por Plasmodium falciparum
{: .text-alpha }

## Resumen en Una Frase

La colchicina es un fármaco oral utilizado originalmente para tratar la gota y la fiebre mediterránea familiar.
El modelo TxGNN predice que podría ser efectiva para la **malaria por Plasmodium falciparum**, pero **no hay ensayos clínicos** y solo **2 publicaciones** de laboratorio, ninguna de las cuales evalúa la colchicina como tratamiento antipalúdico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Gota y fiebre mediterránea familiar (según las indicaciones originales del grafo de conocimiento; los textos de las autorizaciones españolas no incluyen indicación) |
| Nueva Indicación Predicha | Malaria por Plasmodium falciparum |
| Puntaje de Predicción TxGNN | 99.60% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada para este informe. Según lo conocido, la colchicina es un inhibidor de la polimerización de microtúbulos, y entre sus dianas farmacológicas figura la tubulina beta de clase I (TUBB). Su eficacia en la gota y la fiebre mediterránea familiar está bien establecida, y mecanísticamente podría ser aplicable a la malaria.

El vínculo que sugiere el modelo es plausible. El parásito *Plasmodium* depende de la tubulina y los microtúbulos para dividirse e invadir las células. Un fármaco que altera los microtúbulos podría, en teoría, afectar al parásito. La relación con las indicaciones originales (enfermedades inflamatorias) es débil, porque la colchicina se usa en ellas por su efecto antiinflamatorio sobre los neutrófilos y no por una acción antiparasitaria.

Esta hipótesis no tiene respaldo experimental directo en los datos disponibles. Las dos publicaciones recuperadas estudian la curcumina y el gen pfmdr1 en células de mamífero, no la colchicina. Además, el estrecho margen terapéutico y la toxicidad conocida de la colchicina serían una barrera importante para un uso antipalúdico. El puntaje de 99.60% es solo una predicción computacional.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | Estudio in vitro (curcumina, no colchicina) | PLoS One | La curcumina altera los microtúbulos de *P. falciparum*. Apoya la tubulina como diana en el parásito, pero no evalúa la colchicina. |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | Estudio in vitro / celular | Mol Cell Biol | La expresión del gen plasmodial pfmdr1 en células de mamífero se asocia a mayor sensibilidad a cloroquina. No evalúa la colchicina. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 86658 | Colchicina Tiofarma 1 mg comprimidos | Comprimido |
| 33720 | Colchicina Seid 1 mg comprimidos | Comprimido |
| 86430 | Colcamexx 0,5 mg comprimidos EFG | Comprimido |
| 86659 | Colchicina Tiofarma 0,5 mg comprimidos | Comprimido |
| 78947 | Colchicina Seid 0,5 mg comprimidos | Comprimido |

Se muestran 5 de las 8 autorizaciones vigentes, todas de principio activo único. No hay autorizaciones canceladas.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN; no proceden del texto del prospecto):
  - Hepáticas y renales: insuficiencia hepática, función renal alterada, nefropatía aguda por uratos.
  - Hematológicas: enfermedad hematológica, trombocitopenia, leucopenia, agranulocitosis, neutropenia (incluidas diversas formas congénitas), anemia aplásica.
  - Musculares: miopatía, enfermedad muscular y del músculo esquelético, rabdomiólisis, parálisis periódica familiar.
  - Digestivas: úlcera péptica, enfermedades diarreicas.
  - Otras: fascitis nodular.
- **Interacciones Farmacológicas**: los datos disponibles describen dianas farmacológicas de la colchicina (receptores de glicina GLRA1 y GLRA2, TAS2R4, TAS2R46, BRD4 y tubulina beta clase I), no interacciones con otros medicamentos. No se dispone de una lista de interacciones clínicamente relevantes.
- **Margen terapéutico**: según el análisis de la predicción, la colchicina tiene un índice terapéutico estrecho y toxicidad conocida.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5). No hay ensayos clínicos ni estudios que evalúen la colchicina frente a *P. falciparum*. Además, su estrecho margen terapéutico y sus contraindicaciones hematológicas, hepáticas y renales plantean un obstáculo importante.

**Para avanzar se necesita:**
- Estudios in vitro de actividad de la colchicina frente a cultivos de *P. falciparum*, incluidas cepas resistentes a cloroquina.
- Datos de selectividad: concentración eficaz frente al parásito comparada con la toxicidad en células humanas.
- Datos detallados del mecanismo de acción y del prospecto (advertencias y contraindicaciones oficiales).
- Evaluación de la viabilidad de alcanzar concentraciones antipalúdicas con una exposición segura.

**Otras predicciones del modelo (para contexto):**
- *Fiebre mediterránea familiar autosómica dominante*: es una variante de una indicación ya establecida, por lo que no constituye reposicionamiento real. Evidencia L4, basada sobre todo en revisiones.
- *Dermatofibrosarcoma protuberans*: sin ensayos ni literatura, y sin vínculo mecanístico establecido (L5, Hold).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


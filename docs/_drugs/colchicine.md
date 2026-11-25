---
layout: default
title: Colchicine
parent: Solo predicción del modelo (L5)
nav_order: 206
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-25
monitor_inn: "Colchicine"
predicted_indications: ["Plasmodium falciparum malaria", "dermatofibrosarcoma protuberans"]
description: "Colchicine: nueva indicación predicha, Malaria por Plasmodium falciparum (Plasmodium falciparum malaria) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 9 (comercializadas: 3; autorizadas no comercializadas: 4)"
---

# Colchicine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Colchicine: Malaria por Plasmodium falciparum (Plasmodium falciparum malaria)
{: .text-alpha }

## Resumen en Una Frase

La colchicina es un fármaco oral utilizado originalmente para tratar la gota y la fiebre mediterránea familiar.
El modelo TxGNN predice que podría ser efectiva para la **malaria por Plasmodium falciparum**, pero **no hay ensayos clínicos** y solo **2 publicaciones** de laboratorio, ninguna de las cuales evalúa la colchicina como tratamiento antipalúdico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Malaria por Plasmodium falciparum (Plasmodium falciparum malaria) |
| Puntaje de Predicción TxGNN | 0.9960 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 3 de 9; autorizadas no comercializadas: 4; revocadas o suspendidas: 2) |
| Número de Autorizaciones | 9 (comercializadas: 3) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Colchicine (traducción no oficial): «Se ha postulado que la eficacia de la colchicina como tratamiento de la gota se debe a su capacidad para bloquear las respuestas inflamatorias mediadas por neutrófilos inducidas por los cristales de urato monosódico en el líquido sinovial. La colchicina altera la polimerización de la β-tubulina en microtúbulos, lo que impide la activación, la desgranulación y la migración de los neutrófilos a los sitios de inflamación.» Texto original en inglés: "Colchicine’s effectiveness as a treatment for gout has been postulated to be due to its ability to block neutrophil-mediated inflammatory responses induced by monosodium urate crystals in synovial fluid. Colchicine disrupts the polymerization of β-tubulin into microtubules, thereby preventing the activation, degranulation, and migration of neutrophils to sites of inflammation." ([DailyMed: Mitigare (colchicine) prescribing information, Hikma Specialty USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cb5f9d85-6b81-49f8-bcd6-17b7bfbc10f2), versión del 2026-10-16; consultado el 2026-11-19). Según lo conocido, la colchicina es un inhibidor de la polimerización de microtúbulos, y entre sus dianas farmacológicas figura la tubulina beta de clase I (TUBB). Su eficacia en la gota y la fiebre mediterránea familiar está bien establecida, y mecanísticamente podría ser aplicable a la malaria.

El vínculo que sugiere el modelo es plausible. El parásito *Plasmodium* depende de la tubulina y los microtúbulos para dividirse e invadir las células. Un fármaco que altera los microtúbulos podría, en teoría, afectar al parásito. La relación con las indicaciones originales (enfermedades inflamatorias) es débil, porque la colchicina se usa en ellas por su efecto antiinflamatorio sobre los neutrófilos y no por una acción antiparasitaria.

Esta hipótesis no tiene respaldo experimental directo en los datos disponibles. Las dos publicaciones recuperadas estudian la curcumina y el gen pfmdr1 en células de mamífero, no la colchicina. Además, el estrecho margen terapéutico y la toxicidad conocida de la colchicina serían una barrera importante para un uso antipalúdico. El puntaje de 0.9960 es solo una predicción computacional.

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

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 33720 | COLCHICINA SEID 1 mg COMPRIMIDOS | COMPRIMIDO | Seid S.A. | Comercializada |
| 78947 | COLCHICINA SEID 0,5 MG COMPRIMIDOS | COMPRIMIDO | Seid S.A. | Comercializada |
| 90154 | COLCHICINA INDOCO 0,5 MG COMPRIMIDOS EFG | COMPRIMIDO | Indoco Remedies Czech S.R.O. | Comercializada |
| 86658 | COLCHICINA TIOFARMA 1 MG COMPRIMIDOS | COMPRIMIDO | Tiofarma B.V. | Autorizada, no comercializada |
| 86659 | COLCHICINA TIOFARMA 0,5 MG COMPRIMIDOS | COMPRIMIDO | Tiofarma B.V. | Autorizada, no comercializada |
| 88127 | COLCHICINA STRIDES 0,5 MG COMPRIMIDOS EFG | COMPRIMIDO | Strides Pharma (Cyprus) Limited | Autorizada, no comercializada |
| 91260 | COLCHICINA ASPIRE 0,5 MG COMPRIMIDOS EFG | COMPRIMIDO | Aspire Pharma (Malta) Limited | Autorizada, no comercializada |
| 86430 | COLCAMEXX 0,5 MG COMPRIMIDOS EFG | COMPRIMIDO | Pharmaselect International Beteiligungs Gmbh | Suspendida |
| 84475 | COLCHICINA RIA 1 MG COMPRIMIDOS EFG | COMPRIMIDO | Ria Generics Limited | Suspendida |

Se muestran las 9 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

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

<!-- review:begin es-lic-20261105-colchicine-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Se muestran 5 de las 8 autorizaciones vigentes, todas de principio activo único. No hay autorizaciones canceladas." Eliminado: afirmaba que el medicamento no está autorizado o comercializado en España, o que sus autorizaciones están revocadas o suspendidas, lo que no coincide con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-colchicine-1 -->

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

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Eliminado: "Se muestran 5 de las 8 autorizaciones vigentes, todas de principio activo único. No hay autorizaciones canceladas" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Mitigare (colchicine) prescribing information, Hikma Specialty USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=cb5f9d85-6b81-49f8-bcd6-17b7bfbc10f2) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


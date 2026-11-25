---
layout: default
title: Vancomycin
parent: Solo predicción del modelo (L5)
nav_order: 839
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-25
monitor_inn: "Vancomycin"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "typhoid fever", "blood group incompatibility", "streptococcal pneumonia", "premalignant hematological system disease"]
description: "Vancomycin: nueva indicación predicha, Esclerodermia difusa (diffuse scleroderma) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 12 (comercializadas: 7; autorizadas no comercializadas: 3)"
---

# Vancomycin
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

## Vancomycin: Esclerodermia difusa (diffuse scleroderma)
{: .text-alpha }

## Resumen en Una Frase

Vancomicina es un antibiótico glucopéptido, originalmente utilizado para tratar la colitis por *Clostridium difficile*, infecciones estafilocócicas, endocarditis y artritis bacteriana.
El modelo TxGNN predice que podría ser efectivo para **esclerodermia difusa**, pero **no hay ensayos clínicos** y solo **1 publicación** (un reporte de caso sin relación directa con el tratamiento de la esclerodermia) acompaña esta predicción.
La evidencia es únicamente computacional y la predicción carece de plausibilidad mecanística.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Esclerodermia difusa (diffuse scleroderma) |
| Puntaje de Predicción TxGNN | 0.9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 7 de 12; autorizadas no comercializadas: 3; revocadas o suspendidas: 2) |
| Número de Autorizaciones | 12 (comercializadas: 7) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Vancomycin (traducción no oficial): «La vancomicina es un fármaco antibacteriano. […] La acción bactericida de la vancomicina se debe principalmente a la inhibición de la biosíntesis de la pared celular. Además, la vancomicina altera la permeabilidad de la membrana celular bacteriana y la síntesis de ARN.» Texto original en inglés: "Vancomycin is an antibacterial drug. […] The bactericidal action of vancomycin results primarily from inhibition of cell-wall biosynthesis. In addition, vancomycin alters bacterial-cell-membrane permeability and RNA synthesis." ([DailyMed: Tyzavan (vancomycin) prescribing information, Hikma Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=72e9c5e2-07cc-4a8b-ba64-b2e7619ea560), versión del 2026-08-19; consultado el 2026-11-19). Según la información conocida, la vancomicina es un antibiótico glucopéptido que inhibe la síntesis de la pared celular de bacterias grampositivas, y su eficacia en infecciones por grampositivos y colitis por *C. difficile* está bien establecida.

Sin embargo, **la predicción no resulta razonable desde el punto de vista biológico**. La esclerodermia difusa (esclerosis sistémica) es una enfermedad autoinmune y fibrótica, sin un componente bacteriano que la vancomicina pueda tratar. El análisis de los datos indica que no existe un vínculo mecanístico plausible y que el puntaje alto de TxGNN parece ser un artefacto del modelo TxGNN (aprendizaje profundo).

La única publicación recuperada describe un caso de eritrodermia con sepsis y eosinofilia, que no aborda el tratamiento de la esclerodermia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Reporte de caso | The American Journal of Case Reports | Caso de erupción exfoliativa difusa con sepsis y eosinofilia en un varón de 56 años (posible eritrodermia); no trata la esclerodermia |

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 85651 | VANCOMICINA NORMON 1000 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION EFG | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Laboratorios Normon S.A. | Comercializada |
| 67283 | VANCOMICINA SALA 1.000 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION EFG | POLVO PARA SOLUCIÓN INYECTABLE | Laboratorio Reig Jofre, S.A. | Comercializada |
| 67282 | VANCOMICINA SALA 500 MG POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN EFG | POLVO PARA SOLUCIÓN INYECTABLE | Laboratorio Reig Jofre, S.A. | Comercializada |
| 90305 | VANGOZYR 125 MG CAPSULAS DURAS | CÁPSULA DURA | Mabo Farma S.A. | Comercializada |
| 85652 | VANCOMICINA NORMON 500 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION EFG | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Laboratorios Normon S.A. | Comercializada |
| 78672 | VANCOMICINA MIP 500 MG POLVO PARA SOLUCION PARA PERFUSION EFG | POLVO PARA SOLUCIÓN PARA PERFUSIÓN | Mip Pharma Gmbh | Comercializada |
| 78671 | VANCOMICINA MIP 1000 MG POLVO PARA SOLUCION PARA PERFUSION EFG | POLVO PARA SOLUCIÓN PARA PERFUSIÓN | Mip Pharma Gmbh | Comercializada |
| 90304 | VANGOZYR 250 MG CAPSULAS DURAS | CÁPSULA DURA | Mabo Farma S.A. | Autorizada, no comercializada |
| 91205 | VANCOMICINA NORIDEM 1000 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION EFG | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Noridem Enterprises Limited | Autorizada, no comercializada |
| 91206 | VANCOMICINA NORIDEM 500 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION EFG | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Noridem Enterprises Limited | Autorizada, no comercializada |

Se muestran 10 de 12 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de riesgo (según el grafo de conocimiento, no el prospecto)**: enfermedad renal, piouréter, neutropenia, agranulocitosis, trastornos de la audición y enfermedades del sistema auditivo.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones; entre las principales:
  - **Mayores**: inmunoglobulina G humana (intravenosa), inmunoglobulina humana antineurotoxina botulínica A/B y vacuna viva de *Vibrio cholerae* (cepa CVD 103-HgR).
  - **Moderadas**: AINE (ketorolaco, ibuprofeno, diclofenaco, celecoxib), anfotericina B (incluido el complejo lipídico), aminoglucósidos y polipéptidos (amikacina, capreomicina, bacitracina), carboplatino, metformina, estrógenos (etinilestradiol, estradiol), mesalazina, balsalazida, ibandronato y colestiramina.

<!-- review:begin es-lic-20261105-vancomycin-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Se muestran 5 de las 10 autorizaciones vigentes, todas de principio activo único." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-vancomycin-1 -->

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura relevante, y no existe un mecanismo biológico plausible que vincule un antibiótico antibacteriano con la fibrosis autoinmune de la esclerodermia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y de advertencias y contraindicaciones del prospecto de la AEMPS.
- Evidencia preclínica o clínica que justifique un vínculo entre vancomicina y la esclerodermia (actualmente inexistente).
- Revisar otras indicaciones predichas con mayor plausibilidad biológica, como la **neumonía estreptocócica** (nivel L4, actividad frente a grampositivos). Aun así, podría tratarse más de una extensión de uso existente que de un reposicionamiento genuino. Las predicciones para salmonelosis, fiebre tifoidea y paratifoidea carecen de fundamento, ya que son bacterias gramnegativas intrínsecamente resistentes a la vancomicina.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Eliminado: "Se muestran 5 de las 10 autorizaciones vigentes, todas de principio activo único" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Tyzavan (vancomycin) prescribing information, Hikma Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=72e9c5e2-07cc-4a8b-ba64-b2e7619ea560) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


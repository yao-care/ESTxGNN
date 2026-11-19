---
layout: default
title: Telavancin
parent: Solo predicción del modelo (L5)
nav_order: 769
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-20
monitor_inn: "telavancin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "septicemic plague", "premalignant hematological system disease", "hematological disease associated with an acquired peripheral neuropathy", "monoclonal gammopathy", "congenital hematological disorder"]
description: "Telavancin: nueva indicación predicha, Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 2 (comercializadas: 0)"
---

# Telavancin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Telavancin: Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)
{: .text-alpha }

## Resumen en Una Frase

Telavancina es un antibiótico lipoglucopéptido, originalmente utilizado para el tratamiento de la neumonía bacteriana y la neumonía por *Staphylococcus aureus*.
El modelo TxGNN predice que podría ser efectivo para **síndrome de hiperviscosidad policlonal**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) |
| Puntaje de Predicción TxGNN | 0.9963 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado (registros anulados: 2 de 2) |
| Número de Autorizaciones | 2 (comercializadas: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Telavancin (traducción no oficial): «La telavancina es un fármaco antibacteriano. […] La telavancina inhibe la biosíntesis de la pared celular al unirse a precursores del peptidoglicano de etapa tardía, incluido el lípido II. La telavancina también se une a la membrana bacteriana y altera la función de barrera de la membrana. Interacciones con otros fármacos antibacterianos Las investigaciones in vitro no demostraron antagonismo entre la telavancina y la amikacina, el aztreonam, la cefepima, la ceftriaxona, la ciprofloxacina, la gentamicina, el imipenem, el meropenem, la oxacilina, la piperacilina/tazobactam, la rifampicina y la trimetoprima/sulfametoxazol cuando se evaluaron en diversas combinaciones frente a estafilococos, estreptococos y enterococos sensibles a la telavancina.» Texto original en inglés: "Telavancin is an antibacterial drug. […] Telavancin inhibits cell wall biosynthesis by binding to late-stage peptidoglycan precursors, including lipid II. Telavancin also binds to the bacterial membrane and disrupts membrane barrier function. Interactions with Other Antibacterial Drugs In vitro investigations demonstrated no antagonism between telavancin and amikacin, aztreonam, cefepime, ceftriaxone, ciprofloxacin, gentamicin, imipenem, meropenem, oxacillin, piperacillin/tazobactam, rifampin, and trimethoprim/sulfamethoxazole when tested in various combinations against telavancin-susceptible staphylococci, streptococci, and enterococci." ([DailyMed: Vibativ (telavancin hydrochloride) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5359b759-db7c-4672-9e8a-59c93869bd91), versión del 2025-12-19; consultado el 2026-11-19). Según la información conocida, telavancina es un antibiótico lipoglucopéptido que inhibe la síntesis de la pared celular bacteriana y altera la integridad de la membrana, con eficacia demostrada en infecciones por bacterias Gram-positivas como la neumonía.

La hiperviscosidad policlonal se debe a niveles elevados de inmunoglobulinas o proteínas séricas. Este proceso no es una diana del mecanismo antibacteriano de telavancina, por lo que **no se identifica un vínculo mecanístico plausible** entre la indicación original y la nueva.

El puntaje elevado (0.9963) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni clínica. Otras predicciones del modelo (hiperamilasemia, analbuminemia congénita, gammapatía monoclonal, entre otras) presentan el mismo patrón: puntajes altos sin respaldo mecanístico. La única con cierta plausibilidad indirecta es la peste septicémica, aunque *Yersinia pestis* es Gram-negativa y existen tratamientos eficaces establecidos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

<!-- review:begin es-lic-20261105-telavancin-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Ambas autorizaciones están vigentes, corresponden a medicamentos de principio activo único y su titular es Theravance Biopharma Ireland Limited." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. El medicamento tiene 2 autorizaciones (comercializadas: 0); las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-telavancin-1 -->

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 111705001 | Vibativ 250 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |
| 111705002 | Vibativ 750 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): hipertensión, síndrome de QT largo (incluido el familiar), torsades de pointes, enfermedad renal y deterioro de la función renal, piouréter, diabetes mellitus, cetoacidosis diabética, colitis por *Clostridium difficile* y enterocolitis necrosante perinatal.
- **Interacciones farmacológicas**: se registraron 131 interacciones. Entre las principales:
  - **Mayor**: dolasetrón.
  - **Moderadas**: ondansetrón, palonosetrón, levofloxacino, claritromicina, famotidina, loperamida, mesalazina, sulfasalazina, balsalazida, olsalazina, bisacodilo, ácido picosulfúrico, polietilenglicol, sulfato de sodio, lactitol, lactulosa y aceite de ricino.
  - **Menor**: metronidazol.

  Varias de estas interacciones (antieméticos y quinolonas/macrólidos) son coherentes con el riesgo de prolongación del intervalo QT.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos, literatura y vínculo mecanístico plausible (nivel de evidencia L5). El puntaje alto del modelo no basta para avanzar, y el perfil de seguridad (QT, función renal) exige cautela.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del fármaco
- Advertencias y contraindicaciones oficiales del prospecto de la AEMPS
- Una hipótesis biológica que justifique el efecto sobre la hiperviscosidad, con datos in vitro o en modelos animales
- Valorar otras indicaciones predichas con mayor plausibilidad antes de invertir recursos en esta

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Ambas autorizaciones están vigentes, corresponden a medicamentos de principio activo único y su titular es Theravance Biopharma Ireland Limi" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Vibativ (telavancin hydrochloride) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5359b759-db7c-4672-9e8a-59c93869bd91) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


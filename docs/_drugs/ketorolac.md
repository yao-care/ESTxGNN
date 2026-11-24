---
layout: default
title: Ketorolac
parent: Evidencia alta (L1-L2)
nav_order: 442
evidence_level: L1
indication_count: 3
last_modified_at: 2026-11-24
description: "Ketorolac: nueva indicación predicha, Trastorno de cefalea (headache disorder) (nivel de evidencia L1). Indicación original: Conjuntivitis atópica…"
monitor_inn: "ketorolac"
predicted_indications: ["headache disorder", "rosacea conjunctivitis", "trigeminal autonomic cephalalgia"]
---

# Ketorolac
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **3** 
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

## Ketorolaco: De Conjuntivitis Atópica a Trastorno de Cefalea
{: .text-alpha }

## Resumen en Una Frase

Ketorolaco es un antiinflamatorio no esteroideo (AINE), originalmente asociado al tratamiento de la conjuntivitis atópica, papilar y vernal.
El modelo TxGNN predice que podría ser efectivo para **Trastorno de Cefalea** (principalmente migraña y cefalea tensional),
con **17 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Conjuntivitis atópica, papilar y vernal (según la base de conocimiento del modelo; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Trastorno de cefalea (headache disorder) |
| Puntaje de Predicción TxGNN | 0.9943 |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 4 de 8; revocadas o suspendidas: 4) |
| Número de Autorizaciones | 8 (comercializadas: 4) |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Clinical Pharmacology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Ketorolac (traducción no oficial): «El ketorolaco trometamina es un antiinflamatorio no esteroideo (AINE) que presenta actividad analgésica en modelos animales. El mecanismo de acción del ketorolaco, al igual que el de otros AINE, no se conoce por completo, pero puede estar relacionado con la inhibición de la prostaglandina sintetasa.» Texto original en inglés: "Ketorolac tromethamine is a nonsteroidal anti-inflammatory drug (NSAID) that exhibits analgesic activity in animal models. The mechanism of action of ketorolac, like that of other NSAIDs, is not completely understood but may be related to prostaglandin synthetase inhibition." ([DailyMed: Toronova Ii Suik (ketorolac tromethamine) prescribing information, Advanced Rx of Tennessee, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49dd153c-10e8-505b-e063-6394a90a595f), versión del 2026-11-13; consultado el 2026-11-19). Según la farmacología conocida, ketorolaco es un inhibidor no selectivo de COX-1 y COX-2. Al bloquear la síntesis de prostaglandinas, reduce la sensibilización periférica y central y la inflamación neurogénica implicadas en la migraña y la cefalea tensional. Este mecanismo se infiere de la farmacología conocida del fármaco y no de los datos suministrados.

La indicación original (conjuntivitis de tipo inflamatorio/alérgico) y la nueva indicación comparten un componente de inflamación mediada por prostaglandinas, aunque los tejidos y las vías de administración son distintos. En el caso de la cefalea, la evidencia proviene sobre todo de la vía parenteral (intravenosa o intramuscular) e intranasal, no de la presentación oftálmica.

Cabe señalar que la predicción es plausible y está respaldada por ensayos y guías clínicas. Sin embargo, la ficha técnica española no aporta textos de indicación, por lo que no se puede confirmar si la cefalea figura entre las indicaciones autorizadas.

## Evidencia de Ensayos Clínicos

Se muestran los ensayos más relevantes (de 17 identificados), priorizando los que evalúan ketorolaco directamente.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01596166](https://clinicaltrials.gov/study/NCT01596166) | Fase 4 | Completado | 56 | Ketorolaco IV más metoclopramida en migraña pediátrica en urgencias |
| [NCT01807234](https://clinicaltrials.gov/study/NCT01807234) | Fase 4 | Completado | 72 | Ketorolaco en spray nasal vs. sumatriptán nasal y placebo en migraña aguda |
| [NCT01011673](https://clinicaltrials.gov/study/NCT01011673) | Fase 4 | Completado | 123 | Metoclopramida/difenhidramina vs. ketorolaco solo en cefalea tensional |
| [NCT00483717](https://clinicaltrials.gov/study/NCT00483717) | Fase 2 | Completado | 173 | Ketorolaco intranasal vs. placebo, doble ciego, en migraña aguda |
| [NCT02358681](https://clinicaltrials.gov/study/NCT02358681) | Fase 3 | Completado | 59 | Ketorolaco intranasal vs. intravenoso (no inferioridad) en migraña pediátrica |
| [NCT01267864](https://clinicaltrials.gov/study/NCT01267864) | Fase 4 | Completado | 330 | Valproato IV vs. metoclopramida IV vs. ketorolaco IV en migraña aguda |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Fase 4 | Desconocido | 60 | Ketamina vs. ketorolaco en cefalea tensional |
| [NCT06083571](https://clinicaltrials.gov/study/NCT06083571) | Fase 2 | Terminado | 41 | Cóctel nasal con ketorolaco vs. ketorolaco IV en migraña pediátrica |
| [NCT03066544](https://clinicaltrials.gov/study/NCT03066544) | Fase 1/2 | Desconocido | 50 | Respondedores y no respondedores en estatus migrañoso en práctica real |
| [NCT02681211](https://clinicaltrials.gov/study/NCT02681211) | N/A | Desconocido | 80 | Acupuntura auricular vs. medicación IV para estatus migrañoso pediátrico |

Nota: los ensayos NCT04353505, NCT01534806 y NCT05983354 fueron retirados sin participantes y no aportan datos.

<!-- review:begin es-lic-20261105-ketorolac-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Hay 8 autorizaciones vigentes en total, todas de principio activo único." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-ketorolac-1 -->

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guía | Headache | Actualización 2025 de la guía de la American Headache Society sobre tratamiento parenteral de la migraña en urgencias |
| [35138658](https://pubmed.ncbi.nlm.nih.gov/35138658/) | 2022 | Revisión sistemática/Metaanálisis | Acad Emerg Med | Eficacia de ketorolaco parenteral en el ataque agudo de migraña |
| [23298250](https://pubmed.ncbi.nlm.nih.gov/23298250/) | 2013 | Revisión sistemática | Headache | Efectividad de ketorolaco parenteral en migraña aguda, con evidencia previa conflictiva |
| [37849443](https://pubmed.ncbi.nlm.nih.gov/37849443/) | 2024 | Revisión sistemática/Metaanálisis | Adv Clin Exp Med | Comparación de ketorolaco IV frente a metoclopramida en adultos con migraña |
| [24433525](https://pubmed.ncbi.nlm.nih.gov/24433525/) | 2014 | Revisión sistemática | Headache | Tratamiento parenteral de la cefalea tensional episódica |
| [35670115](https://pubmed.ncbi.nlm.nih.gov/35670115/) | 2022 | ECA | Headache | Metoclopramida sola vs. combinada con ketorolaco en migraña pediátrica en urgencias |
| [30783794](https://pubmed.ncbi.nlm.nih.gov/30783794/) | 2019 | ECA | Neurol Sci | Dexametasona, metoclopramida, ketorolaco y clorpromazina IV para alivio del dolor y prevención de recurrencia |
| [41100185](https://pubmed.ncbi.nlm.nih.gov/41100185/) | 2025 | ECA | Cephalalgia | Bloqueo del nervio occipital mayor añadido a terapia triple en migraña aguda |
| [24875925](https://pubmed.ncbi.nlm.nih.gov/24875925/) | 2015 | Revisión sistemática | Cephalalgia | Recomendaciones de la Canadian Headache Society para migraña en urgencias |
| [1514724](https://pubmed.ncbi.nlm.nih.gov/1514724/) | 1992 | ECA | Ann Emerg Med | Ketorolaco IM vs. meperidina e hidroxizina en migraña aguda |

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 70102 | KETOROLACO TROMETAMOL NORMON 30 mg/ml SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Laboratorios Normon S.A. | Comercializada |
| 58976 | TORADOL 30 mg/1 ml SOLUCION INYECTABLE | SOLUCIÓN INYECTABLE | Atnahs Pharma Netherlands Bv. | Comercializada |
| 70105 | KETOROLACO TROMETAMOL QUALIGEN 10 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Neuraxpharm Spain S.L. | Comercializada |
| 61690 | ACULAR 5 mg/ml COLIRIO EN SOLUCION | COLIRIO EN SOLUCIÓN | Abbvie Spain, S.L.U. | Comercializada |
| 84357 | KETOROLACO KABI 30 MG/ML SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Fresenius Kabi España, S.A.U. | Suspendida |
| 334 295-9 | ACULAR COLIRIO | COLIRIO EN SOLUCIÓN | Allergan France | Revocada |
| 70103 | KETOROLACO TROMETAMOL QUALIGEN 30 MG/ML SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Neuraxpharm Spain S.L. | Revocada |
| 70098 | KETOROLACO TROMETAMOL ACCORD 30 MG/ML SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Accord Healthcare S.L.U. | Revocada |

Se muestran las 8 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en la base de conocimiento** (no proceden del texto del prospecto): hipertensión, úlcera gástrica y enfermedad ulcerosa péptica activa, enfermedad hepática, enfermedad de la vesícula biliar, artritis reumatoide, enfermedad inflamatoria intestinal, asma (intrínseca y alérgica), diabetes mellitus y cetoacidosis diabética, trastornos de la coagulación y hemofilia, ictus y enfermedad cerebrovascular, infarto de miocardio y trombosis coronaria, hemoglobinopatías y anemias, insuficiencia renal, enfermedad cardiovascular y cardíaca, y síndrome de ojo seco.
- **Interacciones farmacológicas**: se registran 222 interacciones. Entre las principales:
  - **Mayor**: ácido acetilsalicílico.
  - **Moderadas**: corticoides (betametasona, budesonida, dexametasona, hidrocortisona), sulfonilureas (acetohexamida, clorpropamida, glimepirida, glipizida, glibenclamida), balsalazida, exenatida, fenfluramina y dexfenfluramina, kanamicina y levofloxacino.
  - **Menores**: famotidina, ranitidina, cimetidina y linaclotida.
- Un informe de caso en la literatura describe toxicidad por litio al coadministrarse con ketorolaco.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen varios ensayos de Fase 3/4 completados, revisiones sistemáticas, metaanálisis y guías clínicas que respaldan el uso de ketorolaco en migraña y cefalea tensional (nivel L1). Sin embargo, el perfil de riesgo de los AINE (gastrointestinal, renal, cardiovascular y hemorrágico) exige salvaguardas.

**Para avanzar se necesita:**
- Obtener y revisar la ficha técnica de la AEMPS (indicaciones, advertencias y contraindicaciones), que actualmente no está disponible.
- Confirmar si la cefalea figura entre las indicaciones autorizadas en España o si sería un uso fuera de indicación.
- Obtener datos del mecanismo de acción desde DrugBank.
- Definir criterios de exclusión y de duración máxima de tratamiento para poblaciones de riesgo (renal, cardiovascular, gastrointestinal, embarazo, pediatría).

---

### Otras indicaciones predichas (para referencia)

- **Conjuntivitis rosácea** (puntaje 0.9940): sin ensayos ni literatura. Nivel L5, decisión **Hold**.
- **Cefalalgia trigémino-autonómica** (puntaje 0.9939): único ensayo retirado sin participantes y literatura marginal. Nivel L4, decisión **Hold**.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Eliminado: "Hay 8 autorizaciones vigentes en total, todas de principio activo único" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Toronova Ii Suik (ketorolac tromethamine) prescribing information, Advanced Rx of Tennessee, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49dd153c-10e8-505b-e063-6394a90a595f) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


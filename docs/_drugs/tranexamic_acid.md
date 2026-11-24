---
layout: default
title: Tranexamic Acid
parent: Solo predicción del modelo (L5)
nav_order: 813
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "tranexamic acid"
predicted_indications: ["amenorrhea (disease)"]
description: "Tranexamic Acid: nueva indicación predicha, Amenorrea (amenorrhea (disease)) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 10 (comercializadas: 5; autorizadas no comercializadas: 3)"
---

# Tranexamic Acid
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Tranexamic Acid: Amenorrea (amenorrhea (disease))
{: .text-alpha }

## Resumen en Una Frase

El ácido tranexámico es un antifibrinolítico utilizado originalmente en el contexto de la endometriosis y comercializado en España en múltiples formulaciones.
El modelo TxGNN predice que podría ser efectivo para **Amenorrea**, pero actualmente no hay ensayos clínicos registrados y solo **2 publicaciones** (ambas revisiones) abordan el tema de forma indirecta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Amenorrea (amenorrhea (disease)) |
| Puntaje de Predicción TxGNN | 0.9919 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 5 de 10; autorizadas no comercializadas: 3; revocadas o suspendidas: 2) |
| Número de Autorizaciones | 10 (comercializadas: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Tranexamic Acid (traducción no oficial): «El ácido tranexámico es un derivado sintético del aminoácido lisina que disminuye la disolución de la fibrina hemostática por la plasmina. En presencia de ácido tranexámico, los sitios de unión del receptor de lisina de la plasmina para la fibrina están ocupados, lo que impide la unión a los monómeros de fibrina y, de este modo, preserva y estabiliza la estructura de la matriz de fibrina.» Texto original en inglés: "Tranexamic acid is a synthetic lysine amino acid derivative, which diminishes the dissolution of hemostatic fibrin by plasmin. In the presence of tranexamic acid, the lysine receptor binding sites of plasmin for fibrin are occupied, preventing binding to fibrin monomers, thus preserving and stabilizing fibrin's matrix structure." ([DailyMed: Cyklokapron (tranexamic acid) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e89a7d9-4da4-42aa-b7f8-c602c24eefe5), versión del 2025-09-03; consultado el 2026-11-19). Según la información conocida, el ácido tranexámico es un antifibrinolítico, análogo de la lisina, que bloquea la unión del plasminógeno a la fibrina y reduce el sangrado menstrual abundante.

Sin embargo, **la plausibilidad biológica de esta predicción es baja**. La amenorrea (ausencia de menstruación) es lo opuesto a un trastorno hemorrágico, por lo que un vínculo terapéutico directo es poco creíble. La única conexión razonable es indirecta: en pacientes con trastornos de la coagulación, con anticoagulación o con neoplasias hematológicas, el ácido tranexámico puede formar parte de un régimen de profilaxis o supresión de la menstruación junto con agentes hormonales, reduciendo el sangrado, no tratando la amenorrea en sí.

El puntaje elevado de TxGNN (0,9919) proviene del modelo TxGNN (aprendizaje profundo) y probablemente refleja similitudes que el modelo aprendió entre enfermedades relacionadas (trastornos menstruales como la endometriosis o el sangrado uterino anormal), no evidencia biológica ni una señal terapéutica real. La falta de datos de mecanismo de acción original limita una validación mecanística adicional.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Revisión | Menopause | Revisión de terapias farmacológicas para el sangrado uterino anormal; los agentes no hormonales son eficaces y generalmente bien tolerados, y la elección depende de la etiología, la cantidad de sangrado, la necesidad de anticoncepción y el estado perimenopáusico |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Revisión | J Oncol Pharm Pract | Abordaje sistemático de la profilaxis y supresión de la menstruación en pacientes premenopáusicas con cáncer hematológico; escasez de datos comparativos entre terapias |

Ninguna de las dos publicaciones evalúa el ácido tranexámico como tratamiento de la amenorrea.

<!-- review:begin es-lic-20261105-tranexamic_acid-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Se muestran 5 de las 10 autorizaciones vigentes (todas de principio activo único)." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-tranexamic_acid-1 -->

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 80781 | ACIDO TRANEXAMICO ZENTIVA 500 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Zentiva K.S. | Comercializada |
| 86353 | MEDSAMIC 100 MG/ML SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Medochemie Limited | Comercializada |
| 90522 | ACIDO TRANEXAMICO VIATRIS 100 MG/ML SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Viatris Healthcare Limited | Comercializada |
| 53939 | AMCHAFIBRIN 500 mg SOLUCION INYECTABLE | SOLUCIÓN INYECTABLE | Viatris Healthcare Limited | Comercializada |
| 88279 | AMCHAFIBRIN 500 MG COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Viatris Healthcare Limited | Comercializada |
| 89608 | TANTIRAMIX 500 MG COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Adamed Pharma S.A. | Autorizada, no comercializada |
| 85520 | ACIDO TRANEXAMICO BAXTER 100 MG/ML SOLUCION INYECTABLE EFG | SOLUCION INYECTABLE Y PARA PERFUSION | Baxter Holding B.V. | Autorizada, no comercializada |
| 89178 | NEXAG 1.000 MG GRANULADO RECUBIERTO EN SOBRES | GRANULADO RECUBIERTO EN SOBRE | Cemag Care | Autorizada, no comercializada |
| 53940 | AMCHAFIBRIN 500 mg COMPRIMIDOS | COMPRIMIDO | Meda Pharma S.L. | Revocada |
| 83427 | ACIDO TRANEXAMICO AUROVITAS 100 MG/ML SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Aurovitas Spain, S.A.U. | Revocada |

Se muestran las 10 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): hipertensión, trastornos de ansiedad, porfiria, enfermedad hepática y de la vesícula biliar, hiperglucemia y diabetes mellitus (incluida la cetoacidosis diabética), edema cerebral, hipertrigliceridemia e hiperlipidemia, carcinoma de mama femenino, tromboflebitis, migraña, enfermedad coronaria, obesidad, cáncer de endometrio, ictus y trastornos cerebrovasculares.
- **Interacciones farmacológicas** (35 registradas; se muestran las principales):
  - **Mayor**: estrógenos y anticonceptivos hormonales (etinilestradiol, estradiol, estrógenos conjugados, noretisterona, drospirenona, etonogestrel, dietilestilbestrol, estrona, estramustina), complejo coagulante anti-inhibidor, complejo de factor IX humano y carfilzomib.
  - **Moderada**: alteplasa y anistreplasa (trombolíticos, por efecto farmacodinámico opuesto).

Destaca el riesgo trombótico al combinar con estrógenos o progestágenos, relevante porque el régimen de supresión menstrual suele incluir agentes hormonales. Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (nivel L4), sin ensayos clínicos y con literatura indirecta. Además, el mecanismo antifibrinolítico es biológicamente contrario a la naturaleza de la amenorrea, por lo que el puntaje alto probablemente es un artefacto del modelo TxGNN (aprendizaje profundo).

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones oficiales), lo cual es un requisito bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar las indicaciones aprobadas en España, ausentes en los datos actuales.
- Reevaluar si el objetivo real es la supresión del sangrado menstrual en poblaciones específicas (por ejemplo, cáncer hematológico) y, de ser así, replantear la indicación y buscar estudios que la respalden.
- Evaluar el riesgo trombótico en combinación con terapias hormonales.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Eliminado: "Se muestran 5 de las 10 autorizaciones vigentes (todas de principio activo único)" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Cyklokapron (tranexamic acid) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e89a7d9-4da4-42aa-b7f8-c602c24eefe5) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Allopurinol
parent: Solo predicción del modelo (L5)
nav_order: 39
evidence_level: L5
indication_count: 10
monitor_inn: "Allopurinol"
predicted_indications: ["hepatic porphyria", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "idiopathic copper-associated cirrhosis", "hepatoportal sclerosis", "primitive portal vein thrombosis", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "idiopathic eosinophilic myositis"]
last_modified_at: 2026-11-24
description: "Allopurinol: nueva indicación predicha, porfiria hepática (hepatic porphyria) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Allopurinol
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

## Alopurinol: inhibidor de la xantina oxidasa → porfiria hepática (hepatic porphyria)
{: .text-alpha }

## Resumen en Una Frase

Alopurinol es un inhibidor de la xantina oxidasa (enzima XDH) que se comercializa en España en comprimidos.
El modelo TxGNN predice que podría ser efectivo para **porfiria hepática (hepatic porphyria)**,
pero actualmente solo hay **2 publicaciones** indirectas (una hipótesis y un estudio en ratas) y **ningún ensayo clínico** que lo respalden.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | porfiria hepática (hepatic porphyria) |
| Puntaje de Predicción TxGNN | 0.9995 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 11; autorizadas no comercializadas: 4; revocadas o suspendidas: 5) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Allopurinol (traducción no oficial): «El alopurinol es un análogo estructural de la base púrica natural hipoxantina. El alopurinol y su metabolito oxipurinol inhiben la xantina oxidasa, la enzima responsable de la conversión de hipoxantina en xantina y de xantina en ácido úrico, el producto final del metabolismo de las purinas en los seres humanos.» Texto original en inglés: "Allopurinol is a structural analogue of the natural purine base, hypoxanthine. Allopurinol and its oxypurinol metabolite inhibitor xanthine oxidase, the enzyme responsible for the conversion of hypoxanthine to xanthine and of xanthine to uric acid, the end product of purine metabolism in humans." ([DailyMed: Aloprim (allopurinol) prescribing information, Mylan Institutional LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=10cc918f-aa44-415b-932d-2404695ac449), versión del 2022-02-18; consultado el 2026-11-19). Según la información farmacológica compilada, alopurinol actúa sobre la xantina deshidrogenasa/oxidasa (gen XDH), enzima del metabolismo de las purinas.

El vínculo con la porfiria hepática es indirecto y especulativo. Una publicación de 2019 plantea, como hipótesis, actuar sobre la 5-aminolevulinato sintasa (ALAS), enzima limitante de la síntesis del hemo, mediante triptófano e inhibidores del uso del hemo. Otro trabajo, de 1992, en rata, estudia cómo la carbamazepina agrava las porfirias hepáticas. Ninguno de los dos estudia el alopurinol en esta enfermedad.

Además, en la literatura se ha discutido que el alopurinol podría perturbar el metabolismo del hemo, por lo que el sentido del efecto es incierto y podría incluso ser perjudicial. El puntaje elevado es una predicción computacional, sin datos clínicos humanos que la sustenten.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Revisión/Hipótesis | Medical Hypotheses | Propone dirigirse a la ALAS hepática mediante triptófano o inhibidores del uso del hemo por la triptófano 2,3-dioxigenasa como posible terapia de porfirias hepáticas agudas |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Estudio animal (rata) | Biochemical Pharmacology | La carbamazepina, a dosis muy bajas, altera el metabolismo del hemo hepático y agrava las porfirias hepáticas |

Ninguna de estas publicaciones evalúa el alopurinol en porfiria hepática.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 69156 | ALOPURINOL TEVA 100 mg COMPRIMIDOS EFG | COMPRIMIDO | Teva Pharma S.L.U. | Comercializada |
| 84086 | ALOPURINOL CINFAMED 300 MG COMPRIMIDOS EFG | COMPRIMIDO | Laboratorios Cinfa S.A. | Comercializada |
| 69155 | ALOPURINOL TEVA 300 mg COMPRIMIDOS EFG | COMPRIMIDO | Teva Pharma S.L.U. | Comercializada |
| 88128 | ALOPURINOL TARBIS 100 MG COMPRIMIDOS EFG | COMPRIMIDO | Tarbis Farma S.L. | Comercializada |
| 61424 | ALOPURINOL SUN 100 mg COMPRIMIDOS EFG | COMPRIMIDO | Sun Pharmaceutical Industries (Europe) B.V. | Comercializada |
| 64461 | ALOPURINOL KERN PHARMA 300 mg COMPRIMIDOS EFG | COMPRIMIDO | Kern Pharma S.L. | Comercializada |
| 56360 | ZYLORIC 300 mg COMPRIMIDOS | COMPRIMIDO | Faes Farma S.A. | Comercializada |
| 43775 | ZYLORIC 100 mg COMPRIMIDOS | COMPRIMIDO | Faes Farma S.A. | Comercializada |
| 83686 | ALOPURINOL AUROVITAS 300 MG COMPRIMIDOS EFG | COMPRIMIDO | Aurovitas Spain, S.A.U. | Comercializada |
| 63222 | ALOPURINOL NORMON 300 mg COMPRIMIDOS EFG | COMPRIMIDO | Laboratorios Normon S.A. | Comercializada |

Se muestran 10 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

Los datos compilados muestran autorizaciones de medicamentos con alopurinol como único principio activo, todos en forma de comprimido (la lista puede ser parcial). Entre los productos figuran, por ejemplo, Zyloric 100 mg y 300 mg (Faes Farma) y diversas presentaciones genéricas (EFG) de Cinfa, Teva, Accord, Stada, Bluefish, Normon, Kern Pharma y otros laboratorios. Los registros no incluyen el texto de la indicación aprobada.

<!-- review:begin es-lic-20261124c-allopurinol-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Los datos compilados muestran 20 autorizaciones de medicamentos con alopurinol como único principio activo, todos en forma de comprimido (la lista puede ser parcial)." Corregido: la cifra solo correspondía a las autorizaciones recogidas para este informe (una parte del total); según el listado completo de CIMA (AEMPS), datos del 2026-11-23, hay más autorizaciones con este principio activo. Las cifras recogidas están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261124c-allopurinol-1 -->

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: la consulta se completó; solo se registra la interacción farmacológica con su diana, la xantina deshidrogenasa (XDH), sin interacciones con otros fármacos.
- **Alertas adicionales**: el modelo asocia el fármaco con posible riesgo en enfermedad hepática, enfermedad de la vesícula biliar, función renal alterada, vasculitis por hipersensibilidad (incluida la vasculitis cutánea leucocitoclástica y alérgica) y enfermedad anti-membrana basal glomerular. Estas relaciones no proceden del texto del prospecto y deben verificarse en este.

Consultar el prospecto para el resto de información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni estudios que evalúen directamente el alopurinol en porfiria hepática; los dos trabajos disponibles son indirectos, por lo que el nivel de evidencia es L5. Además, la dirección del efecto es incierta, con posible perturbación del metabolismo del hemo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y estudios preclínicos que evalúen el efecto del alopurinol sobre la ALAS y el metabolismo del hemo
- Revisión de la ficha técnica (advertencias y contraindicaciones) y evaluación de seguridad específica en pacientes con porfiria
- Evidencia clínica o de series de casos en porfiria hepática antes de reconsiderar la decisión

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Aloprim (allopurinol) prescribing information, Mylan Institutional LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=10cc918f-aa44-415b-932d-2404695ac449) |
| 2026-11-24 | «20 autorizaciones» → sin cifras | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


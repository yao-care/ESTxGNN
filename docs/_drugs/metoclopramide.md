---
layout: default
title: Metoclopramide
parent: Solo predicción del modelo (L5)
nav_order: 517
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "Metoclopramide"
predicted_indications: ["gastroduodenitis", "peptic ulcer perforation"]
description: "Metoclopramide: nueva indicación predicha, Gastroduodenitis (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 8 (comercializadas: 8)"
---

# Metoclopramide
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

## Metoclopramide: Gastroduodenitis
{: .text-alpha }

## Resumen en Una Frase

Metoclopramida es un procinético (antagonista dopaminérgico D2 y agonista 5-HT4) utilizado originalmente para la enfermedad por reflujo gastroesofágico y la esofagitis.
El modelo TxGNN predice que podría ser efectivo para **Úlcera gástrica**, pero actualmente solo existe **1 ensayo clínico** (indirectamente relacionado, sobre visualización endoscópica) y literatura mayoritariamente indirecta, por lo que la evidencia es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Gastroduodenitis |
| Puntaje de Predicción TxGNN | 0.9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 8 de 8) |
| Número de Autorizaciones | 8 (comercializadas: 8) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Metoclopramide (traducción no oficial): «La metoclopramida estimula la motilidad del tracto gastrointestinal superior sin estimular las secreciones gástricas, biliares ni pancreáticas. El mecanismo de acción exacto de la metoclopramida en el tratamiento del reflujo gastroesofágico y de la gastroparesia diabética aguda y recurrente no se ha establecido por completo.» Texto original en inglés: "Metoclopramide stimulates motility of the upper gastrointestinal tract without stimulating gastric, biliary, or pancreatic secretions. The exact mechanism of action of metoclopramide in the treatment of gastroesophageal reflux and acute and recurrent diabetic gastroparesis has not been fully established." ([DailyMed: Reglan (metoclopramide hydrochloride) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de55c133-eb08-4a35-91a2-5dc093027397), versión del 2026-02-09; consultado el 2026-11-19). Según la farmacología conocida y los datos de interacción con dianas, la metoclopramida actúa sobre los receptores D2 (antagonista), 5-HT4 (agonista) y 5-HT3. Esto aumenta la motilidad gastroduodenal, acelera el vaciamiento gástrico y eleva el tono del esfínter esofágico inferior.

La relación con la indicación original es de vecindad fisiopatológica: el reflujo y la úlcera gástrica afectan al tracto digestivo superior, y el vaciamiento gástrico retardado o el reflujo biliar pueden contribuir a ambos. Sin embargo, **la metoclopramida no suprime el ácido ni protege la mucosa, y no hay evidencia de que cure úlceras**. Solo existe un estudio en ratas (PMID 2730234) con efecto protector en modelos de úlcera inducida.

El puntaje alto del modelo probablemente refleja la proximidad en la red de conocimiento con las indicaciones originales (reflujo/esofagitis) y no un efecto terapéutico distinto. El único ensayo registrado evalúa la metoclopramida como premedicación para mejorar la visualización endoscópica en hemorragia digestiva alta, un uso procedimental y no tratamiento de la úlcera.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Fase 4 | Desconocido | 60 | Ensayo aleatorizado doble ciego de metoclopramida como premedicación en hemorragia digestiva alta, para reducir la necesidad de repetir endoscopia, radiología intervencionista o cirugía y mejorar la visibilidad. Relevancia indirecta (grado B). |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [786607](https://pubmed.ncbi.nlm.nih.gov/786607/) | 1976 | Revisión | Drugs | Revisión de propiedades farmacológicas y uso clínico de la metoclopramida, incluido su papel facilitando la endoscopia urgente en hemorragia digestiva alta |
| [19445547](https://pubmed.ncbi.nlm.nih.gov/19445547/) | 2009 | Revisión sistemática | Paediatr Drugs | Manejo farmacológico del reflujo gastroesofágico en niños |
| [12825960](https://pubmed.ncbi.nlm.nih.gov/12825960/) | 2003 | Revisión | Drugs | Gastroparesia diabética y opciones terapéuticas limitadas |
| [15001829](https://pubmed.ncbi.nlm.nih.gov/15001829/) | 2004 | Revisión | Digestion | Manejo del reflujo gastroesofágico en niños |
| [11879596](https://pubmed.ncbi.nlm.nih.gov/11879596/) | 2002 | Revisión | Curr Treat Options Gastroenterol | Dispepsia funcional (no ulcerosa) y papel de los procinéticos |
| [8686797](https://pubmed.ncbi.nlm.nih.gov/8686797/) | 1996 | Revisión | Am J Surg | Retraso del vaciamiento gástrico tras cirugía gástrica |
| [579607](https://pubmed.ncbi.nlm.nih.gov/579607/) | 1978 | Simposio/Revisión | Can J Surg | Tratamiento médico de la úlcera péptica; la metoclopramida acelera el vaciamiento gástrico |
| [6782467](https://pubmed.ncbi.nlm.nih.gov/6782467/) | 1981 | Estudio cruzado doble ciego | MMW Munch Med Wochenschr | En 12 voluntarios sanos, ni domperidona ni metoclopramida modificaron significativamente la gastrina sérica ni la secreción ácida |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | Estudio preclínico (ratas) | Arch Int Pharmacodyn Ther | Efecto protector frente a úlceras inducidas por aspirina y ligadura pilórica en ratas |
| [3970596](https://pubmed.ncbi.nlm.nih.gov/3970596/) | 1985 | Serie de casos | Ann Surg | Gastritis y esofagitis por reflujo enterogástrico espontáneo |
| [8095331](https://pubmed.ncbi.nlm.nih.gov/8095331/) | 1993 | Revisión | Postgrad Med | Estrategias para úlceras y esofagitis refractarias a regímenes estándar |

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 78556 | METOCLOPRAMIDA KERN PHARMA 10MG/2ML SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Kern Pharma S.L. | Comercializada |
| 69265 | METOCLOPRAMIDA PENSA 1 mg/ml SOLUCION ORAL EFG | SOLUCIÓN ORAL | Towa Pharmaceutical S.A. | Comercializada |
| 69266 | METOCLOPRAMIDA KERN PHARMA 1 mg/ml SOLUCION ORAL EFG | SOLUCIÓN ORAL | Kern Pharma S.L. | Comercializada |
| 89715 | METOCLOPRAMIDA BASI 5 MG/ML SOLUCION INYECTABLE Y PARA PERFUSION EFG | SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN | Laboratorios Basi Industria Farmaceutica S.A. | Comercializada |
| 41446 | PRIMPERAN 10 mg COMPRIMIDOS | COMPRIMIDO | Sanofi Aventis S.A. | Comercializada |
| 40257 | PRIMPERAN 1mg /ml SOLUCION ORAL | SOLUCIÓN ORAL | Sanofi Aventis S.A. | Comercializada |
| 75665 | METOCLOPRAMIDA ACCORD 10 MG COMPRIMIDOS EFG | COMPRIMIDO | Accord Healthcare S.L.U. | Comercializada |
| 40256 | PRIMPERAN 10 mg /2 ml SOLUCION INYECTABLE | SOLUCIÓN INYECTABLE | Sanofi Aventis S.A. | Comercializada |

Se muestran las 8 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Hay 8 autorizaciones vigentes en total, todas de principio activo único. Entre las autorizaciones figuran Primperan 1 mg/ml solución oral (40257), Metoclopramida Accord 10 mg comprimidos EFG (75665) y Primperan 10 mg/2 ml solución inyectable (40256).

<!-- review:begin es-lic-20261124b-metoclopramide-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Las tres restantes son Primperan 1 mg/ml solución oral (40257), Metoclopramida Accord 10 mg comprimidos EFG (75665) y Primperan 10 mg/2 ml solución inyectable (40256)." Corregido: la frase hablaba de autorizaciones que no figuraban en la tabla anterior (por ejemplo, «la sexta», «las restantes» u «otras»). La tabla de Información de Mercado en España se genera desde el 2026-11-24 por programa a partir de los datos de CIMA (AEMPS) y las incluye; las cifras actuales están en el Resumen rápido. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261124b-metoclopramide-1 -->

---

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto):** enfermedad de Parkinson y trastornos parkinsonianos, discinesia tardía, distonía de torsión, síndrome neuroléptico maligno, epilepsia, feocromocitoma y paraganglioma, hipertensión, porfiria, cirrosis hepática, insuficiencia renal, trastornos de ansiedad y distímicos, úlcera péptica activa, y deficiencias metabólicas raras (déficit de piruvato deshidrogenasa E3 y metahemoglobinemia por déficit de metahemoglobina reductasa).
- **Perforación:** el aumento de la motilidad gástrica está generalmente contraindicado ante perforación u obstrucción, lo que hace inadecuado el uso en perforación ulcerosa.
- **Interacciones:** la información disponible describe solo la afinidad por dianas farmacológicas (receptores 5-HT4, D2, 5-HT3A y 5-HT3AB), sin interacciones medicamentosas clínicas específicas.

Para advertencias formales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe evidencia directa de que la metoclopramida cure la úlcera gástrica; el único ensayo evalúa un uso procedimental y la literatura es indirecta o preclínica. El puntaje elevado del modelo parece reflejar proximidad en la red, no un efecto terapéutico propio. Además, la "úlcera péptica activa" figura entre las contraindicaciones del grafo de conocimiento.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones formales), pendiente y bloqueante para el cribado de seguridad
- Completar los datos del mecanismo de acción
- Ensayos clínicos que evalúen cicatrización de úlceras o desenlaces clínicos, no solo visualización endoscópica
- Aclarar la contradicción con la contraindicación en úlcera péptica activa
- Considerar, como alternativa de menor riesgo, un uso acotado como adyuvante previo a la endoscopia en hemorragia digestiva alta, evaluando los resultados de los ensayos de 2024 y 2026

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Reglan (metoclopramide hydrochloride) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de55c133-eb08-4a35-91a2-5dc093027397) |
| 2026-11-24 | «Las tres restantes son» → «Entre las autorizaciones figuran» | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


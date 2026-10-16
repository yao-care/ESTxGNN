---
layout: default
title: Metoclopramide
parent: Evidencia moderada (L3-L4)
nav_order: 517
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Metoclopramide: nueva indicación predicha, Úlcera gástrica (nivel de evidencia L4). Indicación original: Enfermedad por reflujo gastroesofágico…"
monitor_inn: "Metoclopramide"
predicted_indications: ["gastric ulcer (disease)", "gastroduodenitis", "peptic ulcer disease", "gastrojejunal ulcer", "peptic ulcer perforation"]
---

# Metoclopramide
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **5** 
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

# Metoclopramida: De Enfermedad por Reflujo Gastroesofágico a Úlcera Gástrica

## Resumen en Una Frase

Metoclopramida es un procinético (antagonista dopaminérgico D2 y agonista 5-HT4) utilizado originalmente para la enfermedad por reflujo gastroesofágico y la esofagitis.
El modelo TxGNN predice que podría ser efectivo para **Úlcera gástrica**, pero actualmente solo existe **1 ensayo clínico** (indirectamente relacionado, sobre visualización endoscópica) y literatura mayoritariamente indirecta, por lo que la evidencia es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad por reflujo gastroesofágico, esofagitis (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Úlcera gástrica |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada para este informe. Según la farmacología conocida y los datos de interacción con dianas, la metoclopramida actúa sobre los receptores D2 (antagonista), 5-HT4 (agonista) y 5-HT3. Esto aumenta la motilidad gastroduodenal, acelera el vaciamiento gástrico y eleva el tono del esfínter esofágico inferior.

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

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 78556 | Metoclopramida Kern Pharma 10 mg/2 ml solución inyectable EFG | Solución inyectable | No disponible |
| 69265 | Metoclopramida Pensa 1 mg/ml solución oral EFG | Solución oral | No disponible |
| 69266 | Metoclopramida Kern Pharma 1 mg/ml solución oral EFG | Solución oral | No disponible |
| 89715 | Metoclopramida Basi 5 mg/ml solución inyectable y para perfusión EFG | Solución inyectable y para perfusión | No disponible |
| 41446 | Primperan 10 mg comprimidos | Comprimido | No disponible |

Hay 8 autorizaciones vigentes en total, todas de principio activo único. Las tres restantes son Primperan 1 mg/ml solución oral (40257), Metoclopramida Accord 10 mg comprimidos EFG (75665) y Primperan 10 mg/2 ml solución inyectable (40256).

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


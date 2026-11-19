---
layout: default
title: Budesonide
parent: Solo predicción del modelo (L5)
nav_order: 122
evidence_level: L5
indication_count: 10
monitor_inn: "Budesonide"
predicted_indications: ["atopic eczema", "bronchitis", "dermatitis, atopic", "polyp of vocal cord", "polyp of middle ear", "epulis", "fibroepithelial polyp", "uterine polyp", "polyp of frontal sinus", "polyp of external auditory canal"]
last_modified_at: 2026-11-20
description: "Budesonide: nueva indicación predicha, eccema atópico (atopic eczema) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Budesonide
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

## Budesonida: glucocorticoide de acción local → eccema atópico (atopic eczema)
{: .text-alpha }

## Resumen en Una Frase

Budesonida es un glucocorticoide sintético con acción antiinflamatoria e inmunosupresora, utilizado por vías inhalada, nasal, oral y rectal.
El modelo TxGNN predice que podría ser efectivo para **eccema atópico (atopic eczema)**,
pero actualmente hay **0 ensayos clínicos** y solo **1 estudio preclínico de formulación** que aborde directamente esta indicación.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | eccema atópico (atopic eczema) |
| Puntaje de Predicción TxGNN | 0.9996 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 19; revocadas o suspendidas: 1) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Budesonide (traducción no oficial): «La budesonida es un corticosteroide antiinflamatorio que presenta una potente actividad glucocorticoide y una débil actividad mineralocorticoide. En modelos estándar in vitro y en animales, la budesonida tiene una afinidad por el receptor de glucocorticoides aproximadamente 200 veces mayor y una potencia antiinflamatoria tópica 1000 veces mayor que el cortisol (ensayo de edema auricular inducido por aceite de crotón en ratas).» Texto original en inglés: "Budesonide is an anti-inflammatory corticosteroid that exhibits potent glucocorticoid activity and weak mineralocorticoid activity. In standard in vitro and animal models, budesonide has approximately a 200-fold higher affinity for the glucocorticoid receptor and a 1000-fold higher topical anti-inflammatory potency than cortisol (rat croton oil ear edema assay)." ([DailyMed: Budesonide Inhalation Suspension (budesonide) prescribing information, Cipla USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c52c5382-1400-44b9-95be-a30e1cf706da), versión del 2026-06-10; consultado el 2026-11-19). Según la información farmacológica compilada, budesonida actúa sobre el receptor de glucocorticoides (NR3C2 y NR3C1 incluidos entre sus dianas, junto con el receptor de mineralocorticoides y el de progesterona), lo que explica su efecto antiinflamatorio e inmunosupresor.

La inflamación de la piel en el eccema atópico está impulsada en gran medida por una respuesta inmunitaria de tipo Th2. Un glucocorticoide potente podría, en teoría, reducir esa inflamación. Además, los corticosteroides tópicos ya son un tratamiento establecido para el eccema, por lo que el puntaje elevado refleja sobre todo un efecto de clase y no evidencia específica de budesonida.

Cabe señalar que "dermatitis, atopic" figura como otra entrada de la lista de predicciones y corresponde a la misma enfermedad con distinta denominación; ambas deberían fusionarse en una revisión posterior.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

La literatura recuperada es mayoritariamente indirecta (esofagitis eosinofílica, alergia de contacto, supresión adrenal). Se muestran las publicaciones más pertinentes:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Estudio preclínico de formulación | Gels | Nanopartículas de budesonida en hidrogeles para terapia local de dermatitis atópica; único estudio directamente relacionado |
| [9496795](https://pubmed.ncbi.nlm.nih.gov/9496795/) | 1998 | Estudio abierto longitudinal | Pediatric Dermatology | Evalúa el efecto de budesonida tópica sobre el crecimiento a corto plazo en 14 niños con dermatitis atópica |
| [16428071](https://pubmed.ncbi.nlm.nih.gov/16428071/) | 2006 | Estudio in vitro | International Immunopharmacology | Budesonida, pero no tacrolimus, afecta las funciones inmunitarias de queratinocitos humanos normales |
| [21062310](https://pubmed.ncbi.nlm.nih.gov/21062310/) | 2010 | ECA (veterinario) | J Vet Pharmacol Ther | Acondicionador de budesonida al 0,025 % en perros con dermatitis atópica; mejora de lesiones y prurito |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Revisión | Neuroimmunomodulation | Corticosteroides intranasales y supresión adrenal |
| [14616123](https://pubmed.ncbi.nlm.nih.gov/14616123/) | 2003 | Revisión | Allergy | Alergia a corticosteroides en pacientes con asma |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Estudio de pruebas epicutáneas | Contact Dermatitis | Budesonida como marcador de hipersensibilidad a corticosteroides; tendencia decreciente de alergia |
| [37927648](https://pubmed.ncbi.nlm.nih.gov/37927648/) | 2023 | Reporte de caso | Cureus | Angioedema y urticaria inducidos por esteroides en un paciente con dermatitis atópica |

## Información de Mercado en España

Budesonida está comercializada en España con autorizaciones vigentes de medicamentos de un solo principio activo. La lista de autorizaciones puede ser parcial. Entre los productos principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61728 | ENTOCORD 3 mg cápsulas de liberación modificada | Cápsula dura de liberación modificada | No registrada en los datos locales |
| 83987 | Budesonida Aldo-Unión 100 µg/pulsación | Suspensión para inhalación en envase a presión | No registrada en los datos locales |
| 88386 | Intestifalk 4 mg supositorios | Supositorio | No registrada en los datos locales |
| 1171254003 | Jorveza 1 mg comprimido bucodispersable | Comprimido bucodispersable | No registrada en los datos locales |
| 59298 | Pulmicort 0,25 mg/ml | Suspensión para inhalación por nebulizador | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones farmacológicas / farmacología**: budesonida se une al receptor de glucocorticoides, al receptor de mineralocorticoides y al receptor de progesterona.
- **Seguridad en la literatura**: se describen alergia de contacto a corticosteroides (budesonida se usa como marcador de hipersensibilidad), reacciones de hipersensibilidad inmediata, supresión del eje hipotálamo-hipofisario-adrenal con corticosteroides intranasales y posible efecto sobre el crecimiento en niños con uso tópico.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos de budesonida en eccema atópico, y la única publicación directa es un estudio preclínico de formulación. El puntaje elevado refleja principalmente un efecto de clase de los corticosteroides, ya establecidos en esta enfermedad.

**Para avanzar se necesita:**
- Datos del mecanismo de acción detallados y del prospecto (advertencias y contraindicaciones)
- Fusionar las entradas duplicadas "atopic eczema" y "dermatitis, atopic" y definir claramente la indicación
- Estudios clínicos controlados de budesonida tópica frente a corticosteroides tópicos estándar
- Evaluación de compatibilidad de vía de administración (las formas comercializadas en España no incluyen una formulación dérmica) y de riesgos de sensibilización de contacto y absorción sistémica

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Budesonide Inhalation Suspension (budesonide) prescribing information, Cipla USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c52c5382-1400-44b9-95be-a30e1cf706da) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


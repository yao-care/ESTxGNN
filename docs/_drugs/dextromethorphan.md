---
layout: default
title: Dextromethorphan
parent: Solo predicción del modelo (L5)
nav_order: 244
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-12
monitor_inn: "Dextromethorphan"
predicted_indications: ["nasal cavity disease", "faucial diphtheria", "trigeminal autonomic cephalalgia", "cervical disc degenerative disorder", "allergic urticaria"]
description: "Dextromethorphan: nueva indicación predicha, Enfermedad de la cavidad nasal (nasal cavity disease) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Dextromethorphan
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Dextromethorphan: Enfermedad de la cavidad nasal (nasal cavity disease)
{: .text-alpha }

## Resumen en Una Frase

Dextrometorfano es un antitusivo de uso muy extendido, cuyas indicaciones originales incluyen rinitis alérgica, rinitis vasomotora, faringitis, resfriado común, nasofaringitis y cefalea.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de la cavidad nasal**, con **0 ensayos clínicos** y **0 publicaciones** que respalden actualmente esta dirección.
La predicción se basa únicamente en el modelo (nivel de evidencia L5).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal (nasal cavity disease) |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 17; autorizadas no comercializadas: 1; revocadas o suspendidas: 2) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para dextromethorphan hydrobromide, bupropion hydrochloride (combinación que contiene Dextromethorphan) (traducción no oficial): «Dextrometorfano es un antagonista no competitivo del receptor NMDA (un receptor ionotrópico de glutamato) y un agonista del receptor sigma-1. El mecanismo de dextrometorfano en el tratamiento del TDM y de la agitación asociada a la demencia debida a la enfermedad de Alzheimer no está claro.» Texto original en inglés: "Dextromethorphan is an uncompetitive antagonist of the NMDA receptor (an ionotropic glutamate receptor) and a sigma-1 receptor agonist. The mechanism of dextromethorphan in the treatment of MDD and agitation associated with dementia due to Alzheimer’s disease is unclear." ([DailyMed: Auvelity (dextromethorphan hydrobromide, bupropion hydrochloride) prescribing information, Axsome Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dcefda7c-9a68-278e-e053-2995a90aec79), versión del 2026-08-17; consultado el 2026-11-19). Según la información conocida, el dextrometorfano actúa como antagonista del receptor NMDA y agonista del receptor sigma-1, con actividad antitusiva central. Los datos farmacológicos compilados también lo asocian con GluN2C (GRIN2C), TAS2R1 y SIGMAR1.

La puntuación proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas (rinitis y rinitis vasomotora), no evidencia biológica. La enfermedad de la cavidad nasal es una categoría amplia que engloba esas condiciones, por lo que el resultado podría reflejar en gran parte un solapamiento con indicaciones existentes y no un uso realmente nuevo.

No se ha establecido un vínculo mecanístico directo entre el dextrometorfano y la patología nasal. Sin ensayos ni literatura, la razonabilidad de la predicción no puede verificarse.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Los textos de indicación aprobada no están disponibles en los datos compilados.

<!-- review:begin es-lic-20261105-dextromethorphan-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Se listan 5 de las 20 autorizaciones vigentes (todas de principio activo único). Los textos de indicación aprobada no están disponibles en los datos compilados." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-dextromethorphan-1 -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 57623 | Cinfatos Antitusivo 2 mg/ml solución oral | Solución oral | No disponible |
| 83679 | Intertos 15 mg comprimidos | Comprimido | No disponible |
| 67400 | Bicasan 2 mg/ml jarabe | Jarabe | No disponible |
| 24381 | Propalcof 15 mg comprimidos | Comprimido | No disponible |
| 57174 | Bisolvon Antitusivo 2 mg/ml jarabe | Jarabe | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no provienen del prospecto): hipertensión, síndrome de QT largo (incluido el familiar), torsades de pointes, insuficiencia y enfermedad hepática, epilepsia, EPOC, úlcera gástrica y péptica, enfermedad renal, pancreatitis, enfermedad de la vesícula biliar, trombocitopenia, insuficiencia suprarrenal (enfermedad de Addison), hipotiroidismo, enfermedad inflamatoria intestinal, déficit de potasio, diabetes y cetoacidosis diabética, hiperplasia prostática benigna, bronquitis y trastornos hipotensivos, entre otras.
- **Interacciones y dianas farmacológicas**: se identificaron 3 dianas, GluN2C (GRIN2C), TAS2R1 y el receptor sigma-1 (SIGMAR1). Son interacciones de tipo farmacológico con dianas, no interacciones con otros fármacos con nivel de gravedad asignado.

Las advertencias y contraindicaciones del prospecto de la AEMPS no están disponibles; consultar el prospecto para la información de seguridad oficial.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje TxGNN muy alto, pero carece de ensayos clínicos y de literatura (nivel L5), y probablemente refleja la cercanía con indicaciones nasales ya conocidas más que una nueva indicación. Además, la información de seguridad del prospecto y el mecanismo de acción no están disponibles.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), ya que su ausencia bloquea el cribado de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, consultando DrugBank).
- Realizar una búsqueda sistemática de literatura y ensayos sobre dextrometorfano en patología nasal.
- Aclarar si la «enfermedad de la cavidad nasal» aporta algo realmente distinto de las indicaciones de rinitis ya conocidas.
- Evaluar la compatibilidad de las vías de administración y formas farmacéuticas, hoy pendiente.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Se listan 5 de las 20 autorizaciones vigentes (todas de principio activo único)" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Auvelity (dextromethorphan hydrobromide, bupropion hydrochloride) prescribing information, Axsome Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=dcefda7c-9a68-278e-e053-2995a90aec79) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Latanoprost
parent: Solo predicción del modelo (L5)
nav_order: 456
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
monitor_inn: "LATANOPROST"
predicted_indications: ["visceral calciphylaxis", "hypotrichosis simplex of the scalp", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "congenital hypotrichosis milia", "angiodysplasia of stomach", "blue toe syndrome", "lymphangiectasis"]
description: "Latanoprost: nueva indicación predicha, Visceral calciphylaxis (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Latanoprost
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

## Latanoprost: Visceral calciphylaxis
{: .text-alpha }

## Resumen en Una Frase

Latanoprost es un análogo de la prostaglandina F2-alfa, utilizado originalmente para tratar el glaucoma de ángulo abierto y la hipertensión ocular.
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Visceral calciphylaxis |
| Puntaje de Predicción TxGNN | 0.9983 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 10; autorizadas no comercializadas: 7; revocadas o suspendidas: 3) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Latanoprost (traducción no oficial): «El latanoprost es un análogo de la prostaglandina F 2α que se cree que reduce la presión intraocular (PIO) al aumentar el drenaje del humor acuoso. Los estudios en animales y en seres humanos sugieren que el principal mecanismo de acción es el aumento del drenaje uveoescleral.» Texto original en inglés: "Latanoprost is a prostaglandin F 2α analogue that is believed to reduce the intraocular pressure (IOP) by increasing the outflow of aqueous humor. Studies in animals and man suggest that the main mechanism of action is increased uveoscleral outflow." ([DailyMed: Xelpros (latanoprost) prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=34ad5cf6-4df0-4104-bddd-4c7631133ded), versión del 2025-12-18; consultado el 2026-11-19). Según la información conocida, latanoprost es un análogo de la prostaglandina F2-alfa que reduce la presión intraocular al aumentar el drenaje uveoescleral del humor acuoso.

El glaucoma hereditario primario (por ejemplo, el glaucoma congénito primario) cursa con presión intraocular elevada, por lo que el mecanismo es biológicamente plausible. Sin embargo, esta indicación es muy cercana a la original (glaucoma de ángulo abierto), de modo que el puntaje alto probablemente refleja el solapamiento con la indicación ya aprobada y **no constituye una señal genuina de reposicionamiento**.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

<!-- review:begin es-lic-20261105-latanoprost-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Se listan 5 de las 20 autorizaciones vigentes (todas de un solo principio activo, colirios):" Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-latanoprost-1 -->

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20130076 | Monoprost 50 microgramos/ml colirio en solución en envase unidosis (Laboratoires Thea) | Colirio en solución | No disponible en los datos |
| 76616 | Monoprost 50 microgramos/ml colirio en solución en envase unidosis (Laboratoires Thea) | Colirio en solución | No disponible en los datos |
| 89747 | Latanoprost Yonsung 50 microgramos/ml (Yonsung GmbH) | Colirio en solución en envase unidosis | No disponible en los datos |
| 73959 | Latanoprost Cinfa 50 microgramos/ml (Laboratorios Cinfa) | Colirio en solución | No disponible en los datos |
| 1231763001 | Catiolanze 50 microgramos/ml (Santen Oy) | Colirio en emulsión | No disponible en los datos |

## Consideraciones de Seguridad

- **Enfermedades con relación de contraindicación en el grafo de conocimiento** (no proviene del texto del prospecto): uveítis, enfermedad del iris, enfermedad del cuerpo ciliar, panuveítis, edema macular retiniano, edema macular quístico, iritis y conjuntivitis (incluida la conjuntivitis contagiosa aguda).
- **Interacciones farmacológicas**: se identificaron 100 interacciones potenciales, todas con nivel de gravedad "desconocido" (fuente: DDInter). Entre las primeras figuran calcitriol, glimepirida, doxiciclina, clotrimazol, lansoprazol, cimetidina, atropina, pantoprazol, mesalazina y acarbosa. Sin clasificación de gravedad, su relevancia clínica no puede valorarse.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (nivel L5, sin ensayos ni literatura) y la indicación es prácticamente una extensión de la ya aprobada, por lo que no aporta un reposicionamiento real. Además, falta información de seguridad del prospecto, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones del prospecto de AEMPS (descargar y analizar el PDF)
- Completar los datos del mecanismo de acción desde DrugBank
- Revisar la literatura y los registros de ensayos sobre latanoprost en glaucoma congénito/hereditario, especialmente en población pediátrica
- Evaluar la relevancia clínica de las interacciones, hoy sin clasificar
- Considerar, entre los candidatos de la lista, la hipotricosis del cuero cabelludo (mecanismo plausible similar a bimatoprost en pestañas) como línea de investigación más prometedora desde el punto de vista del reposicionamiento

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Se listan 5 de las 20 autorizaciones vigentes (todas de un solo principio activo, colirios):" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Xelpros (latanoprost) prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=34ad5cf6-4df0-4104-bddd-4c7631133ded) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


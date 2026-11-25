---
layout: default
title: Pertuzumab
parent: Solo predicción del modelo (L5)
nav_order: 629
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-25
monitor_inn: "PERTUZUMAB"
predicted_indications: ["ectomesenchymoma", "malignant cutaneous granular cell skin tumor", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma"]
description: "Pertuzumab: nueva indicación predicha, Ectomesenchymoma (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 8 (comercializadas: 5; autorizadas no comercializadas: 3)"
---

# Pertuzumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Pertuzumab: Ectomesenchymoma
{: .text-alpha }

## Resumen en Una Frase

Pertuzumab es un anticuerpo monoclonal dirigido contra HER2, utilizado originalmente para el tratamiento del carcinoma de mama HER2 positivo.
El modelo TxGNN predice que podría ser efectivo para el **subtipo de carcinoma de mama de tipo normal (normal-like)**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción específica. Se apoya únicamente en el puntaje del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Ectomesenchymoma |
| Puntaje de Predicción TxGNN | 0.9971 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 5 de 8; autorizadas no comercializadas: 3) |
| Número de Autorizaciones | 8 (comercializadas: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Pertuzumab se une al subdominio II de HER2 e impide su dimerización con otros receptores de la familia (en particular HER3). Esto bloquea las vías de señalización PI3K/AKT y MAPK en tumores que dependen de HER2. Por ello es plausible su uso en cáncer de mama impulsado por HER2. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Pertuzumab (traducción no oficial): «El pertuzumab se dirige al dominio de dimerización extracelular (subdominio II) de la proteína del receptor 2 del factor de crecimiento epidérmico humano (HER2) y, de este modo, bloquea la heterodimerización dependiente de ligando de HER2 con otros miembros de la familia HER, incluidos EGFR, HER3 y HER4. Como resultado, el pertuzumab inhibe la señalización intracelular iniciada por ligando a través de dos vías de señalización principales: la de la proteína cinasa activada por mitógenos (MAP) y la de la fosfoinositida 3-cinasa (PI3K).» Texto original en inglés: "Pertuzumab targets the extracellular dimerization domain (Subdomain II) of the human epidermal growth factor receptor 2 protein (HER2) and, thereby, blocks ligand-dependent heterodimerization of HER2 with other HER family members, including EGFR, HER3, and HER4. As a result, pertuzumab inhibits ligand-initiated intracellular signaling through two major signal pathways, mitogen-activated protein (MAP) kinase, and phosphoinositide 3-kinase (PI3K)." ([DailyMed: Perjeta (pertuzumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=17f85d17-ab71-4f5b-9fe3-0b8c822f69ff), versión del 2026-04-30; consultado el 2026-11-19).

La nueva indicación predicha es un subtipo molecular dentro del cáncer de mama, es decir, está relacionada con la indicación original. Sin embargo, el subtipo de tipo normal suele ser HER2-bajo o HER2-negativo, y no se ha demostrado dependencia de HER2 en él. El mecanismo de pertuzumab, que requiere la presencia de HER2 como diana, no respalda de forma directa su eficacia aquí.

En consecuencia, el vínculo se basa solo en la predicción de TxGNN. En sentido amplio, la indicación también coincide con el cáncer de mama ya aprobado, por lo que no constituye un reposicionamiento claro.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Las autorizaciones corresponden a PERJETA 420 MG concentrado para solución para perfusión (titular: Roche Registration GmbH) y a POHERDY 420 MG concentrado para solución para perfusión (titular: Organon N.V.). Los datos compilados no incluyen el texto de la indicación aprobada.

<!-- review:begin es-lic-20261124b-pertuzumab-1 -->

> **Corrección de revisión (2026-11-25)**: Texto original: "Se muestran 5 de las 6 autorizaciones vigentes, todas de PERJETA 420 MG concentrado para solución para perfusión (titular: Roche Registration GmbH)." Corregido: se elimina la descripción de las filas de la tabla anterior y el número de autorizaciones; se conserva el resto del contenido. La tabla de Información de Mercado en España se genera desde el 2026-11-24 por programa a partir de los datos de CIMA (AEMPS); las cifras actuales están en el Resumen rápido y bajo la tabla. Actualizado el 2026-11-25: se incorporan a los datos las autorizaciones de CIMA (AEMPS) posteriores a marzo de 2026 (incluidas importaciones paralelas) con el mismo criterio de recogida, y la frase anterior ya no coincidía con ellas. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261124b-pertuzumab-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 113813001IP2 | PERJETA 420 MG CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Roche Registration Gmbh | Comercializada |
| 113813001IP4 | PERJETA 420 MG CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Roche Registration Gmbh | Comercializada |
| 113813001 | PERJETA 420 MG CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Roche Registration Gmbh | Comercializada |
| 113813001IP | PERJETA 420 MG CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Roche Registration Gmbh | Comercializada |
| 113813001IP1 | PERJETA 420 MG CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Roche Registration Gmbh | Comercializada |
| 113813001IP3 | PERJETA 420 MG CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Roche Registration Gmbh | Autorizada, no comercializada |
| 113813001IP5 | PERJETA 420 MG CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Roche Registration Gmbh | Autorizada, no comercializada |
| 1252008001 | POHERDY 420 MG CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Organon N.V. | Autorizada, no comercializada |

Se muestran las 8 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-HER2) |
| Riesgo de Mielosupresión | Bajo como agente dirigido; la neutropenia se asocia sobre todo a la quimioterapia con la que se combina (p. ej., docetaxel) |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Función cardíaca (fracción de eyección del ventrículo izquierdo), hemograma cuando se combina con quimioterapia, función hepática y renal |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: Idelalisib (nivel moderado).

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación predicha (subtipo normal-like) se apoya solo en el puntaje del modelo (L5), sin ensayos ni literatura. Además, este subtipo suele carecer de sobreexpresión de HER2, la diana del fármaco.

Otras predicciones del mismo análisis tienen más respaldo, pero corresponden a subconjuntos de la indicación ya aprobada (HER2 positivo) y no a un reposicionamiento real:
- **Cáncer de mama con receptor de progesterona positivo:** nivel L1 y recomendación "Proceed with Guardrails". Incluye un ensayo de Fase 3 completado (NCT04629846, 517 pacientes), que compara un biosimilar con pertuzumab de referencia.
- **Cáncer de mama con receptor de progesterona negativo:** nivel L1 y recomendación "Proceed with Guardrails". Cuenta con el mismo ensayo de Fase 3 y con el ensayo de Fase 2 DECRESCENDO (NCT04675827, terminado).

**Para avanzar se necesita:**
- Confirmar el estado de HER2 en el subtipo normal-like y si existe dependencia de esta vía.
- Revisar la bibliografía y los registros de ensayos específicos para esta indicación.
- Obtener del prospecto de la AEMPS las advertencias y contraindicaciones, y el texto de las indicaciones aprobadas.
- Completar los datos del mecanismo de acción y la similitud con la indicación original.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Perjeta (pertuzumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=17f85d17-ab71-4f5b-9fe3-0b8c822f69ff) |
| 2026-11-25 | Eliminado: descripción de la tabla anterior y número de autorizaciones; se conserva el resto | Corregido (revisado el 2026-11-25; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


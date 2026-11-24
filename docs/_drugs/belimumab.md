---
layout: default
title: Belimumab
parent: Solo predicción del modelo (L5)
nav_order: 90
evidence_level: L5
indication_count: 6
monitor_inn: "BELIMUMAB"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "severe nonproliferative diabetic retinopathy", "autosomal dominant macrothrombocytopenia"]
last_modified_at: 2026-11-24
description: "Belimumab: nueva indicación predicha, trastorno primario de liberación plaquetaria (primary release disorder of platelets) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 3 (comercializadas: 3)"
---

# Belimumab
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

## Belimumab: inhibidor de BLyS (BAFF) → trastorno primario de liberación plaquetaria (primary release disorder of platelets)
{: .text-alpha }

## Resumen en Una Frase

Belimumab es un anticuerpo monoclonal que inhibe BLyS (BAFF), un factor de supervivencia de los linfocitos B.
El modelo TxGNN predice que podría ser efectivo para **trastorno primario de liberación plaquetaria (primary release disorder of platelets)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | trastorno primario de liberación plaquetaria (primary release disorder of platelets) |
| Puntaje de Predicción TxGNN | 0,9996 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 3 de 3) |
| Número de Autorizaciones | 3 (comercializadas: 3) |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Belimumab (traducción no oficial): «BENLYSTA es un inhibidor específico de BLyS que bloquea la unión del BLyS soluble, un factor de supervivencia de los linfocitos B, a sus receptores en los linfocitos B. BENLYSTA no se une directamente a los linfocitos B, sino que, al unirse al BLyS, inhibe la supervivencia de los linfocitos B, incluidos los linfocitos B autorreactivos, y reduce la diferenciación de los linfocitos B en células plasmáticas productoras de inmunoglobulinas.» Texto original en inglés: "BENLYSTA is a BLyS-specific inhibitor that blocks the binding of soluble BLyS, a B-cell survival factor, to its receptors on B cells. BENLYSTA does not bind B cells directly, but by binding BLyS, BENLYSTA inhibits the survival of B cells, including autoreactive B cells, and reduces the differentiation of B cells into immunoglobulin-producing plasma cells." ([DailyMed: Benlysta (belimumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2fa3c528-1777-4628-8a55-a69dae2381a3), versión del 2026-10-30; consultado el 2026-11-19). Según la información conocida, belimumab inhibe BLyS (BAFF), con lo que reduce la supervivencia de los linfocitos B y la producción de autoanticuerpos.

Los trastornos primarios de liberación plaquetaria son defectos de la función plaquetaria (anomalías en la secreción de gránulos), generalmente hereditarios o adquiridos, y no se explican principalmente por la actividad de los linfocitos B ni por autoanticuerpos. Por ello no se ha establecido un vínculo mecanístico plausible con la inhibición de BLyS.

El puntaje elevado del modelo TxGNN parece reflejar una predicción basada en la estructura de la red, sin respaldo clínico ni bibliográfico en los datos compilados para este informe. La prediccion debe considerarse una hipótesis sin sustento mecanístico por el momento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 11700001 | BENLYSTA 120 mg POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Glaxosmithkline (Ireland) Limited | Comercializada |
| 11700002 | BENLYSTA 400 mg POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Glaxosmithkline (Ireland) Limited | Comercializada |
| 111700004 | BENLYSTA 200 MG SOLUCION INYECTABLE EN PLUMA PRECARGADA | SOLUCIÓN INYECTABLE EN PLUMA PRECARGADA | Glaxosmithkline (Ireland) Limited | Comercializada |

Se muestran las 3 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 69 interacciones en total; entre las principales mostradas en los datos:
  - Gravedad **mayor**: adalimumab, baricitinib, certolizumab pegol, vacuna BCG (cepa Tice, viva).
  - Gravedad **moderada**: roflumilast, toxoide tetánico, alefacept, alemtuzumab, anakinra, azatioprina, canakinumab, vacuna contra el ántrax, entre otras.
  - Gravedad **menor**: sales de zinc (acetato, gluconato, sulfato y cloruro).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni publicación que estudie esta enfermedad, y no hay un vínculo mecanístico plausible entre la inhibición de BLyS y un defecto de la función plaquetaria. El puntaje alto del modelo por sí solo no basta para avanzar.

**Para avanzar se necesita:**
- Evidencia preclínica o clínica que estudie directamente el trastorno primario de liberación plaquetaria
- Una hipótesis mecanística que justifique el papel de BLyS en esta enfermedad
- Datos de mecanismo de acción y de advertencias y contraindicaciones del prospecto de AEMPS
- Evaluación de seguridad en la población objetivo, incluyendo las interacciones con inmunosupresores y vacunas vivas

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Benlysta (belimumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2fa3c528-1777-4628-8a55-a69dae2381a3) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


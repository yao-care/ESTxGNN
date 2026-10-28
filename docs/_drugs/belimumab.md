---
layout: default
title: Belimumab
parent: Solo predicción del modelo (L5)
nav_order: 90
evidence_level: L5
indication_count: 6
monitor_inn: "BELIMUMAB"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "severe nonproliferative diabetic retinopathy", "autosomal dominant macrothrombocytopenia"]
last_modified_at: 2026-10-27
description: "Belimumab: nueva indicación predicha, trastorno primario de liberación plaquetaria (primary release disorder of platelets) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
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
| Estado de Mercado en Espana | Comercializado (registros vigentes: 3 de 3) |
| Número de Autorizaciones | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, belimumab inhibe BLyS (BAFF), con lo que reduce la supervivencia de los linfocitos B y la producción de autoanticuerpos.

Los trastornos primarios de liberación plaquetaria son defectos de la función plaquetaria (anomalías en la secreción de gránulos), generalmente hereditarios o adquiridos, y no se explican principalmente por la actividad de los linfocitos B ni por autoanticuerpos. Por ello no se ha establecido un vínculo mecanístico plausible con la inhibición de BLyS.

El puntaje elevado del modelo TxGNN parece reflejar una predicción basada en la estructura de la red, sin respaldo clínico ni bibliográfico en los datos compilados para este informe. La prediccion debe considerarse una hipótesis sin sustento mecanístico por el momento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 11700001 | BENLYSTA 120 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No registrada en los datos locales |
| 11700002 | BENLYSTA 400 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No registrada en los datos locales |
| 111700004 | BENLYSTA 200 mg solución inyectable en pluma precargada | Solución inyectable en pluma precargada | No registrada en los datos locales |

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


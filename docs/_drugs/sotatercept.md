---
layout: default
title: Sotatercept
parent: Solo predicción del modelo (L5)
nav_order: 746
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Sotatercept: nueva indicación predicha, Leucemia linfoblástica aguda (nivel de evidencia L5). Indicación original: No disponible (el texto de indicación de las autorizaciones AEMPS est…"
monitor_inn: "SOTATERCEPT"
predicted_indications: ["acute lymphoblastic leukemia (disease)", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "drug-induced osteoporosis", "diabetic cataract", "HER2 positive breast carcinoma", "transitional cell carcinoma", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant"]
---

# Sotatercept
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

## Sotatercept: De Indicación Original No Especificada a Leucemia Linfoblástica Aguda
{: .text-alpha }

## Resumen en Una Frase

Sotatercept es una proteína de fusión del receptor de activina tipo IIA unido a Fc (ActRIIA-Fc), comercializada en España como Winrevair. En los datos compilados para este informe no consta el texto de su indicación original.
El modelo TxGNN predice que podría ser efectivo para **leucemia linfoblástica aguda**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (el texto de indicación de las autorizaciones AEMPS está vacío) |
| Nueva Indicación Predicha | Leucemia linfoblástica aguda |
| Puntaje de Predicción TxGNN | 0,9978 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 2) |
| Número de Autorizaciones | 2 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Sotatercept es una proteína de fusión ActRIIA-Fc que captura activina y factores de diferenciación de crecimiento (GDF), con el fin de reequilibrar la señalización BMP/activina. Los datos compilados no incluyen una descripción detallada del mecanismo de acción registrada, por lo que esta descripción procede del análisis de racionalidad de la predicción.

El vínculo con la leucemia linfoblástica aguda es **especulativo**. La señalización de la familia activina/TGF-beta influye en la hematopoyesis, pero no existen datos mecanísticos ni clínicos directos que apoyen un beneficio en esta enfermedad. Modular la diferenciación hematopoyética podría incluso ser contraproducente. El puntaje alto de TxGNN refleja solo una predicción computacional.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 1241850001 | WINREVAIR 45 MG POLVO Y DISOLVENTE PARA SOLUCION INYECTABLE | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Merck Sharp & Dohme B.V. | Comercializada |
| 1241850003 | WINREVAIR 60 MG POLVO Y DISOLVENTE PARA SOLUCION INYECTABLE | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Merck Sharp & Dohme B.V. | Comercializada |

Se muestran las 2 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como aspecto cualitativo del análisis de la predicción: sotatercept se ha asociado con telangiectasias y eventos hemorrágicos (p. ej., epistaxis, sangrado gingival) por sus efectos sobre la biología vascular. Esto es relevante sobre todo para las indicaciones oculares predichas (retinopatía diabética).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para leucemia linfoblástica aguda se basa solo en el modelo (L5), sin ensayos, literatura ni respaldo mecanístico directo. Además, la modulación de la diferenciación hematopoyética podría ser contraproducente.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), y confirmar la indicación aprobada de las autorizaciones.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión bibliográfica dirigida y estudios preclínicos que respalden un vínculo mecanístico con la leucemia linfoblástica aguda.
- Valorar otras predicciones del modelo con mayor plausibilidad biológica, como la osteoporosis inducida por fármacos (señalización de activina en el remodelado óseo), que también requiere verificación bibliográfica. Las predicciones de carcinoma urotelial forman un grupo correlacionado y no deben considerarse apoyo independiente.
- Evaluar el riesgo hemorrágico/vascular antes de considerar usos oftalmológicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


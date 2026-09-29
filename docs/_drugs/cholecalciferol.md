---
layout: default
title: Cholecalciferol
parent: Solo predicción del modelo (L5)
nav_order: 124
evidence_level: L5
indication_count: 7
---

# Cholecalciferol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Colecalciferol: De Deficiencia de Vitamina D a Hipoparatiroidismo Aislado Familiar por Alteración de la Secreción de PTH

## Resumen en Una Frase

El colecalciferol (vitamina D3) se usa para tratar la deficiencia de vitamina D. Esta indicación procede de datos farmacológicos, porque las autorizaciones de la AEMPS no incluyen texto de indicación.
El modelo TxGNN predice que podría ser efectivo para el **hipoparatiroidismo aislado familiar por alteración de la secreción de PTH**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** específicas que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Deficiencia de vitamina D (según datos farmacológicos; los textos de indicación de la AEMPS están vacíos) |
| Nueva Indicación Predicha | Hipoparatiroidismo aislado familiar por alteración de la secreción de PTH |
| Puntaje de Predicción TxGNN | 99.79% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el colecalciferol es un precursor de la vitamina D. Su eficacia en la deficiencia de vitamina D y el raquitismo está comprobada, y mecanísticamente podría ser aplicable a trastornos del calcio como el hipoparatiroidismo.

La relación entre ambas indicaciones es plausible. Los metabolitos de la vitamina D se usan en el hipoparatiroidismo para restaurar el equilibrio del calcio, y un fármaco de esta clase podría explicar el puntaje alto del modelo.

Sin embargo, hay una limitación importante. El colecalciferol nativo necesita la 1-alfa-hidroxilación renal, que depende de la PTH, y en esta enfermedad ese paso está alterado. Los análogos activos (calcitriol, alfacalcidol) son los agentes biológicamente relevantes. El puntaje podría reflejar una asociación a nivel de clase y no evidencia específica del colecalciferol.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones. Los textos de indicación aprobada figuran vacíos en el registro.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 86565 | DELCRIN 50.000 UI/2,5 ML SOLUCION ORAL | Solución oral |
| 89921 | DITRALIA 25.000 UI PELICULAS BUCODISPERSABLES | Película bucodispersable |
| 82411 | THORENS 25.000 UI/2,5 ML SOLUCION ORAL | Solución oral |
| 81395 | BENFEROL 400 UI CAPSULAS BLANDAS | Cápsula blanda |
| 81820 | VIDESIL 25.000 UI SOLUCION ORAL | Solución oral |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5), sin ensayos ni literatura específicos. Además, el mecanismo presenta un obstáculo: la activación renal dependiente de PTH está alterada en esta enfermedad, y los análogos activos son los agentes relevantes.

Otras predicciones del mismo análisis tienen algo más de respaldo, pero es indirecto (nivel L4, decisión "Research Question"):
- **Raquitismo hipofosfatémico:** los ensayos prueban sobre todo burosumab o vitamina D activa, no colecalciferol.
- **Osteodistrofia renal:** la evidencia es indirecta y podría ser ya un uso de soporte estándar.

**Para avanzar se necesita:**
- Ficha técnica de la AEMPS con advertencias y contraindicaciones (falta actualmente).
- Datos del mecanismo de acción desde DrugBank.
- Búsqueda bibliográfica específica de colecalciferol en hipoparatiroidismo, y comparación con calcitriol y alfacalcidol.
- Definir si el objetivo es reposición nutricional como adyuvante o una indicación de reposicionamiento distinta.
- Plan de monitorización de calcemia y calciuria por el riesgo de hipercalcemia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


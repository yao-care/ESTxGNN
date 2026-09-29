---
layout: default
title: Prucalopride
parent: Solo predicción del modelo (L5)
nav_order: 446
evidence_level: L5
indication_count: 10
---

# Prucalopride
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Prucaloprida: De Estreñimiento Crónico a Hipoalfalipoproteinemia

## Resumen en Una Frase

Prucaloprida es un agonista del receptor 5-HT4, utilizado por vía oral una vez al día en adultos con estreñimiento crónico (incluido el estreñimiento crónico idiopático) en los que los laxantes no son eficaces.
El modelo TxGNN predice que podría ser efectivo para **hipoalfalipoproteinemia** (niveles bajos de colesterol HDL), pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción basada solo en el grafo de conocimiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Estreñimiento crónico (según la información farmacológica del fármaco; los textos de indicación de las licencias españolas están vacíos) |
| Nueva Indicación Predicha | Hipoalfalipoproteinemia |
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información farmacológica disponible, prucaloprida actúa sobre el receptor 5-HT4 (gen *HTR4*) y es un procinético gastrointestinal cuya eficacia en el estreñimiento crónico está comprobada. Sin embargo, mecanísticamente no se identifica una vía plausible que lo conecte con la hipoalfalipoproteinemia.

No existe una relación conocida entre el agonismo del receptor 5-HT4 y el metabolismo de las HDL. La indicación original (un trastorno de la motilidad intestinal) y la nueva (un trastorno del metabolismo lipídico) no guardan similitud clínica ni fisiopatológica. La similitud con la indicación original figura como pendiente de análisis.

El puntaje alto de TxGNN (99.82%, posición 3696 en el ranking global) debe interpretarse con cautela. Es un resultado del grafo de conocimiento sin respaldo experimental ni clínico, y podría reflejar un artefacto del modelo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 09581002 | RESOLOR 2 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | Takeda Pharmaceuticals International AG Ireland Branch |
| 09581001 | RESOLOR 1 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | Takeda Pharmaceuticals International AG Ireland Branch |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni literatura para hipoalfalipoproteinemia (nivel L5) y no existe un vínculo mecanístico plausible con el agonismo 5-HT4. El puntaje alto de TxGNN por sí solo no basta para avanzar.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones). Es una brecha bloqueante para el cribado de seguridad.
- Obtener el mecanismo de acción detallado desde DrugBank.
- Establecer un vínculo mecanístico creíble entre el receptor 5-HT4 y el metabolismo de las HDL, o descartar la predicción.

**Nota sobre otras predicciones del mismo fármaco:** entre las 10 principales, las más defendibles son las relacionadas con amiloidosis (amiloidosis, L4, "Pregunta de Investigación"; amiloidosis primaria, L4, Hold). La lógica es solo sintomática: un procinético podría aliviar la dismotilidad intestinal o la pseudoobstrucción intestinal crónica asociada. No hay evidencia de que prucaloprida modifique el depósito de amiloide o el curso de la enfermedad, y los resúmenes de la literatura recuperada no permiten verificar contenido específico sobre prucaloprida. Las demás predicciones (hipercolesterolemia familiar homocigota, úlcera duodenal, candidiasis oral, entre otras) son solo predicciones del modelo, sin evidencia.

*Los resultados de este informe son solo para referencia de investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


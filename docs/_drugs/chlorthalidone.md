---
layout: default
title: Chlorthalidone
parent: Solo predicción del modelo (L5)
nav_order: 123
evidence_level: L5
indication_count: 10
---

# Chlorthalidone
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

# Clortalidona: De Hipertensión Arterial a Glaucoma Hereditario Primario

## Resumen en Una Frase

Clortalidona es un diurético tipo tiazida que se usa sobre todo como antihipertensivo y para reducir edemas. El modelo TxGNN predice que podría ser efectivo para el **glaucoma hereditario primario**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial y edema (según datos farmacológicos; los textos de indicación de las autorizaciones de AEMPS no están disponibles) |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados del mecanismo de acción en el Evidence Pack. Según la información farmacológica disponible, la clortalidona es un diurético de acción tiazídica que se usa solo o combinado con otros antihipertensivos, y que también reduce edemas de distintas causas. Además, la base farmacológica la vincula con varias anhidrasas carbónicas humanas (CA1, CA4, CA7, CA12 y CA14) y con la enzima NAPEPLD.

El único vínculo plausible con el glaucoma es esa inhibición débil de la anhidrasa carbónica, que en teoría podría reducir la producción de humor acuoso. Es una hipótesis especulativa, sin respaldo en ningún ensayo ni publicación de los datos recibidos.

Hay dos razones para dudar de la relevancia clínica. El glaucoma hereditario primario es un trastorno genético del desarrollo, y es poco probable que un diurético sistémico actúe sobre él. Además, el puntaje alto probablemente refleja conectividad en el grafo de conocimiento y no una relación terapéutica real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 89953 | Clortalidona Glenmark 12,5 mg comprimidos | Comprimido | Glenmark Arzneimittel GmbH |
| 89952 | Clortalidona Glenmark 50 mg comprimidos EFG | Comprimido | Glenmark Arzneimittel GmbH |
| 89954 | Clortalidona Glenmark 25 mg comprimidos EFG | Comprimido | Glenmark Arzneimittel GmbH |
| 45843 | Higrotona 50 mg comprimidos | Comprimido | Amdipharm Limited |
| 83330 | Clortalidona Tecnigen 50 mg comprimidos EFG | Comprimido | Tecnimede España Industria Farmacéutica S.A. |

Los textos de indicación aprobada no están disponibles en los registros recibidos, por lo que no se incluyen en la tabla.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No hay advertencias ni contraindicaciones disponibles, y los datos recibidos no incluyen interacciones farmacológicas clínicas. Las seis entradas de la consulta corresponden a dianas farmacológicas (anhidrasas carbónicas y NAPEPLD), no a interacciones con otros medicamentos.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5): no hay ensayos ni literatura, y el mecanismo propuesto es especulativo y poco compatible con un trastorno genético del desarrollo. Existen además terapias establecidas para el glaucoma. Entre las otras predicciones, la más respaldada es la **cardiopatía pulmonar crónica** (L3, estado "Research Question"), con una publicación de 1967 sobre clortalidona en insuficiencia cardíaca por cor pulmonale crónico. Sería una pregunta de investigación más razonable que el glaucoma.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS para completar advertencias, contraindicaciones e indicaciones autorizadas (bloqueante para el cribado de seguridad).
- Obtener el mecanismo de acción desde DrugBank para evaluar el vínculo mecanístico.
- Buscar estudios preclínicos o clínicos sobre clortalidona (o tiazidas) y presión intraocular.
- Valorar priorizar la evaluación de cardiopatía pulmonar crónica frente al glaucoma.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


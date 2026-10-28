---
layout: default
title: Ioversol
parent: Solo predicción del modelo (L5)
nav_order: 428
evidence_level: L5
indication_count: 9
monitor_inn: "IOVERSOL"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "brachyolmia", "hemoglobinopathy", "brachyolmia-amelogenesis imperfecta syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "alopecia"]
last_modified_at: 2026-10-23
description: "Ioversol: nueva indicación predicha, Osteoartritis (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
---

# Ioversol
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

## Ioversol: De Indicación Original No Registrada a Osteoartritis
{: .text-alpha }

## Resumen en Una Frase

Ioversol es un medio de contraste yodado no iónico comercializado en España (marca Optiray), pero los datos compilados para este informe no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **osteoartritis**, pero no hay ensayos clínicos del propio ioversol y solo **1 publicación** relacionada, que estudia una embolización con aceite etiodizado (no ioversol).
La predicción debe considerarse puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Osteoartritis |
| Puntaje de Predicción TxGNN | 0,9963 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 6 de 8) |
| Número de Autorizaciones | 8 (vigentes: 6) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, ioversol es un medio de contraste yodado no iónico de uso diagnóstico por imagen, sin actividad farmacológica antiinflamatoria o condroprotectora conocida.

La única publicación vinculada (LipioJoint-1, PMID 38102013) estudia la embolización de arterias geniculares con una emulsión de aceite etiodizado (Lipiodol), no con ioversol. Cualquier conexión es indirecta, como mucho a través del papel de los contrastes yodados en procedimientos de imagen o embolización.

El puntaje alto de TxGNN (0,9963) es una predicción computacional del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades articulares relacionadas, no evidencia biológica; no refleja un mecanismo terapéutico plausible para ioversol. Como ningún estudio citado aborda directamente ioversol en osteoartritis, el nivel de evidencia es L5.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | Ensayo clínico (procedimiento intervencionista; no evalúa ioversol) | Diagnostic and Interventional Imaging | Evalúa la seguridad y eficacia de la embolización transitoria de arterias geniculares con una emulsión de aceite etiodizado en osteoartritis de rodilla. No estudia ioversol. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 62068 | OPTIRAY 300 mg/ml solución inyectable | Solución inyectable | No disponible |
| 62069 | OPTIRAY 350 mg/ml solución inyectable | Solución inyectable | No disponible |
| 62067 | OPTIRAY ULTRAJECT 350 mg/ml solución inyectable | Solución inyectable | No disponible |
| 60714 | OPTIRAY ULTRAJECT 320 mg/ml solución inyectable | Solución inyectable | No disponible |
| 62070 | OPTIRAY ULTRAJECT 300 mg/ml solución inyectable | Solución inyectable | No disponible |

Se muestran 5 de las 8 autorizaciones; las otras 3 son: 58469 (OPTIRAY 320 mg/ml, vigente) y dos canceladas (60713 y 58468). Todas son del titular Guerbet.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las principales, de nivel **Mayor**: metformina, anfotericina B (incluidas las formulaciones lipídica, de sulfato de colesterilo y liposomal), mesalazina, balsalazida, olsalazina, sulfasalazina, vancomicina, kanamicina, neomicina, estreptomicina y polimixina B. De nivel **Moderado**: manitol. Con nivel sin clasificar: atropina, famotidina, ácido acetilsalicílico, morfina y omeprazol.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5): no hay ensayos clínicos, la única publicación no estudia ioversol y no existe un mecanismo plausible que conecte un contraste yodado inerte con la osteoartritis.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (indicaciones, advertencias y contraindicaciones)
- Datos del mecanismo de acción desde DrugBank
- Estudios preclínicos o clínicos que evalúen directamente ioversol en osteoartritis
- Confirmar que la señal del modelo no sea un artefacto del modelo TxGNN (aprendizaje profundo)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Mebendazole
parent: Solo predicción del modelo (L5)
nav_order: 495
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Mebendazole: nueva indicación predicha, Acné (nivel de evidencia L5). Indicación original: Enterobiasis, ascariasis y tricuriasis (según el grafo de conocimiento"
monitor_inn: "Mebendazole"
predicted_indications: ["acne (disease)"]
---

# Mebendazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Mebendazol: De Enterobiasis, Ascariasis y Tricuriasis a Acné

## Resumen en Una Frase

Mebendazol es un antihelmíntico originalmente utilizado para tratar infecciones parasitarias intestinales (enterobiasis, ascariasis y tricuriasis).
El modelo TxGNN predice que podría ser efectivo para **acné**,
pero actualmente **no hay ensayos clínicos** y solo hay **1 publicación** (un reporte de caso sobre esparganosis, no relacionado directamente con acné) que se relaciona con esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enterobiasis, ascariasis y tricuriasis (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Acné |
| Puntaje de Predicción TxGNN | 99.20% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Mebendazol es un antihelmíntico de uso establecido en parasitosis intestinales, y su eficacia en esas indicaciones es conocida. Generalmente se le describe como inhibidor de la polimerización de la tubulina en los helmintos, aunque esto no figura en los datos compilados y debe verificarse.

No se ha establecido un vínculo mecanístico creíble entre mebendazol y el acné. Cualquier hipótesis, como un efecto antiinflamatorio o antiproliferativo por alteración de los microtúbulos, es especulativa y no está verificada. La similitud entre la indicación original (infecciones parasitarias) y el acné (enfermedad inflamatoria de la piel) no está evaluada.

El puntaje de TxGNN (99.20%) es solo una predicción del modelo y no está respaldado por evidencia clínica ni mecanística.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7072899](https://pubmed.ncbi.nlm.nih.gov/7072899/) | 1982 | Reporte de caso | The American Journal of Tropical Medicine and Hygiene | Caso de esparganosis proliferativa humana en Venezuela, con lesiones nodulares y papulares de aspecto similar al acné, abscesos subcutáneos, anemia y eosinofilia. No evalúa mebendazol como tratamiento del acné. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 53775 | LOMPER 20 mg/ml suspensión oral | Suspensión oral | No disponible en los datos compilados |
| 51200 | LOMPER 100 mg comprimidos | Comprimido | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no del prospecto)**: enfermedad hepática y enfermedad de la vesícula biliar.
- **Interacciones Farmacológicas**: se identificaron 10 interacciones.
  - Moderadas: metronidazol, yoduro I-131, yoduro I-123, fenobarbital, carbamazepina, ritonavir, fosfenitoína, fenitoína y primidona.
  - Leve: cimetidina.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5): no hay ensayos clínicos, la única publicación no respalda el uso en acné y no existe un vínculo mecanístico establecido. Además, falta la información de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones) para completar el cribado de seguridad.
- Confirmar el mecanismo de acción en DrugBank y evaluar su plausibilidad en acné.
- Realizar una búsqueda bibliográfica dirigida (estudios preclínicos o clínicos de mebendazol en acné o dermatología).
- Evaluar la compatibilidad de la vía de administración (oral frente a la tópica habitual en acné).
- Valorar la relevancia de las contraindicaciones hepáticas y biliares y las interacciones con inductores enzimáticos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


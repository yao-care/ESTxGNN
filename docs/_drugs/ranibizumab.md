---
layout: default
title: Ranibizumab
parent: Solo predicción del modelo (L5)
nav_order: 456
evidence_level: L5
indication_count: 10
---

# Ranibizumab
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

# Ranibizumab: De Indicación Original No Registrada a Retinopatía Diabética No Proliferativa Grave

## Resumen en Una Frase

Ranibizumab es un anticuerpo anti-VEGF de administración intravítrea. Su indicación original no figura en los datos de autorización recibidos.
El modelo TxGNN predice que podría ser efectivo para **retinopatía diabética no proliferativa grave**,
con **6 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección, incluido un ensayo aleatorizado de Fase 3 específico para esta indicación (PAVILION).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Retinopatía diabética no proliferativa grave |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L1 (con matices: solo un ensayo de Fase 3 evalúa directamente el fármaco en esta indicación) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 11 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el campo de DrugBank. Según la información conocida, ranibizumab neutraliza el VEGF-A, y su eficacia en enfermedades oculares con edema y neovascularización ha sido estudiada ampliamente. Mecanísticamente, podría ser aplicable a la retinopatía diabética.

En la retinopatía diabética, el VEGF favorece la permeabilidad vascular retiniana, la no perfusión y la neovascularización. Esto es coherente con los niveles elevados de VEGF en suero y vítreo descritos en la literatura. Bloquear el VEGF-A con ranibizumab puede frenar o revertir esos procesos.

La evidencia respalda esta lógica. El ensayo PAVILION (Fase 3, sistema de liberación sostenida de ranibizumab frente a observación en NPDR sin edema macular) probó el fármaco directamente en la indicación predicha. Los análisis post hoc de RIDE/RISE muestran además regresión de la gravedad de la retinopatía con ranibizumab.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04503551](https://clinicaltrials.gov/study/NCT04503551) | Fase 3 | Completado | 174 | Ensayo aleatorizado del sistema de liberación sostenida de ranibizumab (PDS) frente a un comparador en retinopatía diabética sin edema macular central. Prueba directa en la indicación objetivo. |
| [NCT00444600](https://clinicaltrials.gov/study/NCT00444600) | Fase 3 | Completado | 691 | DRCR Protocol I: ranibizumab o triamcinolona con láser en edema macular diabético. Datos sólidos de eficacia y seguridad en enfermedad ocular diabética, pero el objetivo es el edema, no la NPDR grave. |
| [NCT02634333](https://clinicaltrials.gov/study/NCT02634333) | Fase 3 | Completado | 399 | Tratamiento anti-VEGF para prevenir complicaciones que amenazan la visión en ojos de alto riesgo. Población pertinente, pero el agente probablemente es otro anti-VEGF (apoyo de clase). |
| [NCT03452657](https://clinicaltrials.gov/study/NCT03452657) | Fase 3 | Desconocido | 118 | Ranibizumab intravítreo frente a inyección simulada para prevenir retinopatía diabética de alto riesgo. Estado desconocido. |
| [NCT02834663](https://clinicaltrials.gov/study/NCT02834663) | Fase 4 | Completado | 25 | Estudio piloto unicéntrico de ranibizumab en edema macular con NPDR; evalúa microaneurismas y área de no perfusión. Muestra pequeña. |
| [NCT05222633](https://clinicaltrials.gov/study/NCT05222633) | N/A | Desconocido | 1000 | Estudio observacional anti-VEGF en la práctica real (DMAE exudativa, retinopatía diabética proliferativa y otras). Aporta poca evidencia específica para NPDR. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | ECA | JAMA Ophthalmology | Ensayo PAVILION: sistema de liberación sostenida de ranibizumab frente a observación en NPDR sin edema macular. |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2024 | Revisión sistemática y metaanálisis | Health Technology Assessment | Compara fármacos anti-VEGF con fotocoagulación láser en retinopatía diabética. |
| [40347224](https://pubmed.ncbi.nlm.nih.gov/40347224/) | 2025 | Revisión sistemática y análisis económico | Health Technology Assessment | Anti-VEGF frente a láser en retinopatía proliferativa y no proliferativa, con análisis económico. |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Revisión | Expert Opinion on Biological Therapy | Los anti-VEGF han transformado el tratamiento de la retinopatía diabética y del edema macular diabético; se revisa la evidencia de ranibizumab. |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | Metaanálisis (post hoc de ECA) | Ophthalmology Retina | Relación entre la gravedad basal de la retinopatía y el tiempo hasta la resolución del edema con ranibizumab en ensayos de Fase 3. |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | Análisis post hoc de ECA | Clinical Ophthalmology | Predictores de mejoría temprana de la retinopatía con ranibizumab en RIDE y RISE. |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | Informe a 5 años de ECA | Retina | Cambios en la gravedad de la retinopatía diabética a 5 años en ojos tratados con ranibizumab (DRCR.net Protocol I). |
| [28448655](https://pubmed.ncbi.nlm.nih.gov/28448655/) | 2017 | Análisis secundario de ECA | JAMA Ophthalmology | Cambio de la retinopatía a 2 años comparando aflibercept, bevacizumab y ranibizumab. |
| [37278412](https://pubmed.ncbi.nlm.nih.gov/37278412/) | 2023 | Simulación | BMJ Open Ophthalmology | Modelo del impacto a largo plazo del tratamiento anti-VEGF proactivo en NPDR grave frente a esperar a la fase proliferativa. |
| [40466685](https://pubmed.ncbi.nlm.nih.gov/40466685/) | 2025 | Estudio observacional | Georgian Medical News | Anti-VEGF combinado con panfotocoagulación en 120 pacientes con retinopatía diabética grave o proliferativa. |

## Información de Mercado en España

Se muestran 5 de las 11 autorizaciones.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1221691001 | Ximluci 10 mg/ml solución inyectable | Solución inyectable | No especificada en los datos |
| 1221673001 | Ranivisio 10 mg/ml solución inyectable | Solución inyectable | No especificada en los datos |
| 106374003IP | Lucentis 10 mg/ml solución inyectable en jeringa precargada | Solución inyectable | No especificada en los datos |
| 1252012001 | Ranluspec 10 mg/ml solución inyectable | Solución inyectable | No especificada en los datos |
| 1211572003 | Byooviz 10 mg/ml solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No especificada en los datos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como observación de la literatura recuperada (no como advertencia oficial), se describió un caso de síndrome de bloqueo capsular tras una inyección intravítrea de ranibizumab, y un estudio pequeño (n=13) evaluó la opacidad del cristalino con este fármaco.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo aleatorizado de Fase 3 completado que prueba ranibizumab directamente en NPDR (PAVILION), además de ensayos de Fase 3 en enfermedad ocular diabética y análisis post hoc que muestran regresión de la gravedad. La evidencia es más sólida para la retinopatía diabética, con o sin edema macular, que para la prevención de complicaciones que amenazan la visión.

Las otras nueve indicaciones predichas (principalmente distintos tipos de catarata y enfermedad hemorrágica del recién nacido) quedan en **Hold**. Sus puntuaciones altas parecen artefactos de proximidad en el grafo, sin mecanismo plausible ni evidencia terapéutica.

**Para avanzar se necesita:**
- Confirmar localmente el estado regulatorio de esta indicación en España (los textos de indicación de las autorizaciones están vacíos).
- Obtener advertencias y contraindicaciones del prospecto de la AEMPS (bloqueo actual para el cribado de seguridad).
- Completar los datos del mecanismo de acción desde DrugBank.
- Definir el plan de administración: liberación sostenida, seguridad de la inyección intravítrea y adherencia al seguimiento.
- Confirmar si los ensayos NCT02634333 y NCT03452657 evalúan ranibizumab específicamente, y el estado del NCT03452657.

*Los resultados son solo para referencia de investigación y no constituyen consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


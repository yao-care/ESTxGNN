---
layout: default
title: Rosuvastatin
parent: Solo predicción del modelo (L5)
nav_order: 476
evidence_level: L5
indication_count: 10
---

# Rosuvastatin
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

# Rosuvastatina: De Hiperlipidemia a Deficiencia de la Proteína de Transferencia de Ésteres de Colesterol (CETP)

## Resumen en Una Frase

La rosuvastatina es una estatina, utilizada originalmente para tratar la hiperlipidemia primaria, la dislipidemia mixta y la hipertrigliceridemia.
El modelo TxGNN predice que podría ser efectiva para la **deficiencia de la proteína de transferencia de ésteres de colesterol (CETP)**, pero hay **0 ensayos clínicos** y solo **2 publicaciones**, ambas sin relación real con esta enfermedad ni con el fármaco.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperlipidemia primaria, dislipidemia mixta e hipertrigliceridemia (según la referencia farmacológica; las autorizaciones de AEMPS no traen texto de indicación) |
| Nueva Indicación Predicha | Deficiencia de la proteína de transferencia de ésteres de colesterol (CETP) |
| Puntaje de Predicción TxGNN | 99.54% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

La rosuvastatina inhibe la enzima HMG-CoA reductasa (gen *HMGCR*). Así reduce la síntesis hepática de colesterol, aumenta los receptores hepáticos de LDL y baja el LDL-C. Es un mecanismo bien establecido para la hipercolesterolemia.

**Con los datos disponibles, esta predicción no resulta convincente.** La deficiencia de CETP se caracteriza por HDL-C elevado, no por LDL-C alto, y bajar el LDL con estatinas no es un tratamiento reconocido para ella. Aunque el puntaje de TxGNN es muy alto, no se identifica un vínculo mecanístico plausible entre el fármaco y esta enfermedad. Lo más probable es que el modelo la haya asociado por su cercanía al metabolismo lipídico en general.

Las dos publicaciones recuperadas tratan de otras enfermedades (deficiencia de Apo AI y deficiencia de lipasa hepática) y no aportan apoyo real a esta indicación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21122686](https://pubmed.ncbi.nlm.nih.gov/21122686/) | 2010 | Reporte de caso / Revisión | Journal of Clinical Lipidology | Deficiencia completa de Apo AI en una familia iraquí mandea, causada por una nueva mutación sin sentido en *APOA1*. Los dos homocigotos tuvieron presentaciones clínicas muy distintas. No trata CETP ni rosuvastatina. |
| [22798447](https://pubmed.ncbi.nlm.nih.gov/22798447/) | 2010 | Reporte de caso | BMJ Case Reports | Deficiencia de lipasa hepática en un varón de origen árabe de Oriente Medio. Reporta actividad y masa de CETP en este paciente, pero no evalúa rosuvastatina como tratamiento. |

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones. Ninguna incluye texto de indicación aprobada en los datos recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 82539 | Rosuvastatina Vir 5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 82543 | Rosuvastatina Farmaprojects 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 86107 | Vaxar 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 86108 | Vaxar 20 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 86110 | Vaxar 5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (L5). No hay ensayos clínicos, no existe un mecanismo plausible y la literatura recuperada es irrelevante. El puntaje alto de TxGNN no compensa esta falta de respaldo.

**Para avanzar se necesita:**
- Una hipótesis mecanística que justifique usar una estatina en la deficiencia de CETP, dado que esta enfermedad cursa con HDL-C elevado
- Revisión de la literatura específica sobre estatinas en deficiencia de CETP
- Datos de seguridad del prospecto de AEMPS (advertencias y contraindicaciones), que no estaban disponibles
- Reconciliar la indicación original con la ficha técnica, porque las autorizaciones no incluyen texto de indicación

**Nota:** en el mismo análisis, la hipercolesterolemia familiar (segunda predicción) tiene evidencia L1, con ensayos de Fase 3 de rosuvastatina en población pediátrica. Esa candidata merece evaluación prioritaria frente a esta.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


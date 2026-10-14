---
layout: default
title: Glatiramer
parent: Solo predicción del modelo (L5)
nav_order: 377
evidence_level: L5
indication_count: 1
---

# Glatiramer
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Glatiramero: De Esclerosis Múltiple a Hemoglobinopatía

## Resumen en Una Frase

Glatiramero (acetato de glatiramero) es un inmunomodulador comercializado en España cuyo uso conocido se centra en la esclerosis múltiple; la ficha de autorización consultada no incluye el texto de indicación.
El modelo TxGNN predice que podría ser efectivo para **hemoglobinopatía**, pero actualmente no hay **ensayos clínicos** registrados y solo hay **1 publicación** con relación indirecta con esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las autorizaciones de AEMPS (el texto de indicación está vacío); el uso conocido del fármaco es la esclerosis múltiple |
| Nueva Indicación Predicha | Hemoglobinopatía |
| Puntaje de Predicción TxGNN | 99.03% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Glatiramero es un inmunomodulador, una mezcla aleatoria de polímeros de cuatro aminoácidos. Se cree que desvía las respuestas de los linfocitos T hacia fenotipos Th2/reguladores y que compite con los antígenos de la mielina por la presentación en el MHC. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe; la descripción anterior procede del análisis mecanístico de la propia predicción.

**La predicción no tiene, a día de hoy, un respaldo mecanístico creíble.** Las hemoglobinopatías (por ejemplo, la anemia falciforme y la talasemia) son trastornos causados principalmente por mutaciones en los genes de la globina y por patología del glóbulo rojo. La modulación inmunitaria no es un eje terapéutico reconocido en ellas. El puntaje elevado de TxGNN (0.990) es únicamente una predicción computacional y no está respaldado por evidencia clínica ni mecanística.

La única publicación vinculada trata sobre trastornos inmunitarios tras suspender natalizumab en esclerosis múltiple, y no evalúa glatiramero en hemoglobinopatía. Su relación con esta indicación probablemente es incidental: la paciente descrita tenía antecedentes de beta talasemia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [28372806](https://pubmed.ncbi.nlm.nih.gov/28372806/) | 2017 | Revisión / reporte de caso | Revue neurologique | Describe a una mujer de 35 años con esclerosis múltiple y antecedentes de beta talasemia, bulimia y asma, que presentó múltiples trastornos inmunitarios tras suspender natalizumab. No evalúa glatiramero en hemoglobinopatía. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 80933 | Glatiramero Viatris 20 mg/ml solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No disponible |
| 79515 | Copaxone 40 mg/ml solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No disponible |
| 82703 | Glatiramero Viatris 40 mg/ml solución inyectable en jeringa precargada | Solución inyectable en jeringa precargada | No disponible |
| 65983 | Copaxone 20 mg/ml solución inyectable | Solución inyectable | No disponible |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificó 1 interacción de nivel **Mayor** con **natalizumab** (fuente: DDInter).

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos clínicos ni evidencia mecanística, y la única publicación vinculada es incidental. No hay una base razonable para avanzar en hemoglobinopatía por ahora.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de glatiramero que permitan evaluar un posible vínculo con la fisiopatología de las hemoglobinopatías
- Estudios preclínicos o de mecanismo que justifiquen un papel de la modulación inmunitaria en esta indicación
- Obtener y revisar el prospecto de AEMPS (advertencias, contraindicaciones e indicaciones aprobadas)
- Aclarar la relación entre la indicación original y la predicha, y la compatibilidad de vía de administración
- Revisión de la relevancia de la literatura vinculada, que actualmente es incidental
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


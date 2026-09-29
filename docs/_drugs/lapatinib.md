---
layout: default
title: Lapatinib
parent: Solo predicción del modelo (L5)
nav_order: 305
evidence_level: L5
indication_count: 1
---

# Lapatinib
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

# Lapatinib: De Indicación Original (no disponible en el registro) a Dermatofibrosarcoma Protuberans

## Resumen en Una Frase

Lapatinib es un inhibidor de tirosina quinasa dual (EGFR/HER2) comercializado en España, pero el registro local no incluye el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **dermatofibrosarcoma protuberans (DFSP)**, con un puntaje alto (99.30%).
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción, que se apoya solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de las autorizaciones AEMPS están vacíos) |
| Nueva Indicación Predicha | Dermatofibrosarcoma protuberans |
| Puntaje de Predicción TxGNN | 99.30% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, lapatinib es un inhibidor dual de EGFR y HER2. La indicación original no pudo confirmarse con los datos locales.

El DFSP suele estar impulsado por la fusión COL1A1-PDGFB, que activa de forma constitutiva el receptor PDGFR-beta. El tratamiento dirigido establecido para este mecanismo es imatinib. Lapatinib no tiene actividad directa conocida sobre PDGFR-beta.

Cualquier vínculo mecanístico sería indirecto, por ejemplo mediante la interacción entre la señalización de EGFR y las vías posteriores de otros receptores tirosina quinasa (MAPK, PI3K-AKT). Esta hipótesis es especulativa y no está verificada. El puntaje alto podría reflejar cercanía en el grafo de conocimiento con otros inhibidores de quinasas, y no un mecanismo validado. Por eso la predicción debe tratarse con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 07440005 | TYVERB 250 mg comprimidos recubiertos con película (Novartis Europharm Limited) | Comprimido masticable | No especificada en el registro |
| 88047 | LAPATINIB STADA 250 mg comprimidos recubiertos con película EFG (Laboratorio Stada S.L.) | Comprimido recubierto con película | No especificada en el registro |
| 07440002 | TYVERB 250 mg comprimidos recubiertos con película (Novartis Europharm Limited) | Comprimido recubierto con película | No especificada en el registro |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa EGFR/HER2) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única base de la predicción es el puntaje de TxGNN, sin ensayos clínicos ni literatura (nivel L5). El mecanismo conocido de lapatinib (EGFR/HER2) no se vincula directamente con el motor molecular del DFSP (PDGFR-beta), donde ya existe una terapia dirigida establecida (imatinib).

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de AEMPS (advertencias, contraindicaciones e indicación aprobada), pendiente para el cribado de seguridad
- Obtener los datos de mecanismo de acción desde DrugBank
- Buscar literatura y ensayos sobre lapatinib en DFSP o sarcomas relacionados
- Reunir evidencia preclínica que justifique la vía indirecta propuesta (crosstalk EGFR y señalización de RTK en modelos de DFSP)
- Comparar el posible beneficio frente al estándar actual (imatinib)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


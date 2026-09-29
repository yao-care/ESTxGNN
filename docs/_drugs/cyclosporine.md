---
layout: default
title: Cyclosporine
parent: Evidencia moderada (L3-L4)
nav_order: 151
evidence_level: L4
indication_count: 7
---

# Cyclosporine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **7** 
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

# Ciclosporina: De Inmunosupresión en Trasplante a Enfermedad Granulomatosa Crónica Autosómica Recesiva

## Resumen en Una Frase

La ciclosporina es un inmunosupresor inhibidor de la calcineurina, utilizado clásicamente para prevenir el rechazo de trasplantes. El modelo TxGNN predice que podría ser efectiva para la **enfermedad granulomatosa crónica autosómica recesiva**, pero solo respaldan esta dirección **1 ensayo clínico** de Fase 1 (no específico de la enfermedad) y **1 publicación** sobre trasplante de progenitores hematopoyéticos. No hay evidencia directa de que la ciclosporina trate el defecto de fondo de la enfermedad.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en las autorizaciones de AEMPS (texto de indicación vacío). Según la información farmacológica: inmunosupresión en trasplante, artritis reumatoide y psoriasis graves |
| Nueva Indicación Predicha | Enfermedad granulomatosa crónica, autosómica recesiva |
| Puntaje de Predicción TxGNN | 99,68 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 13 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, la ciclosporina es un inhibidor de la calcineurina que bloquea la activación de los linfocitos T. Su eficacia como inmunosupresor en trasplantes está comprobada, y se usa de forma habitual para prevenir la enfermedad injerto contra huésped (EICH) tras un trasplante alogénico de progenitores hematopoyéticos.

La relación con la nueva indicación es indirecta. El trasplante de progenitores hematopoyéticos es una opción curativa para la enfermedad granulomatosa crónica, y la ciclosporina forma parte del régimen de apoyo. Sin embargo, este papel es de **cuidado de apoyo en el trasplante**, no de tratamiento del defecto de la enfermedad (deficiencia de NADPH oxidasa).

Por tanto, la predicción del modelo probablemente refleja esa asociación con el trasplante, no un efecto terapéutico directo. No existe evidencia de que la ciclosporina trate por sí misma la enfermedad granulomatosa crónica.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01917708](https://clinicaltrials.gov/study/NCT01917708) | Fase 1 | Completado | 10 | Abatacept combinado con ciclosporina y micofenolato como profilaxis de EICH en niños con trasplante de progenitores hematopoyéticos no emparentado por enfermedades no malignas. No es específico de la enfermedad granulomatosa crónica y la ciclosporina no es el agente investigado (relevancia: C) |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22078471](https://pubmed.ncbi.nlm.nih.gov/22078471/) | 2012 | Cohorte retrospectiva | J Allergy Clin Immunol | Supervivencia excelente tras trasplante de progenitores de donante hermano o no emparentado en enfermedad granulomatosa crónica. Evalúa el trasplante, no la ciclosporina como tratamiento |

## Información de Mercado en España

Hay 13 autorizaciones en total. Se muestran las 5 principales. El registro no incluye el texto de indicación aprobada de ninguna de ellas.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 56800 | SANDIMMUN 50 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en el registro |
| 89655 | CEQUA 0,9 mg/ml colirio en solución en envase unidosis | Colirio en solución en envase unidosis | No disponible en el registro |
| 60318 | SANDIMMUN NEORAL 50 mg cápsulas blandas | Cápsula blanda | No disponible en el registro |
| 78331 | CIQORIN 100 mg cápsulas blandas EFG | Cápsula blanda | No disponible en el registro |
| 1241857001 | VEVIZYE 1 mg/ml colirio en solución | Colirio en solución | No disponible en el registro |

## Consideraciones de Seguridad

- **Interacciones farmacológicas / dianas y transportadores**: la consulta se completó con 7 registros. Son datos de farmacología (dianas y transportadores con los que interactúa la ciclosporina), no interacciones clasificadas por nivel de gravedad:
  - Transportadores: ABCG2, OATP1B1 (SLCO1B1), OATP1B3 (SLCO1B3) y el cotransportador de sodio/ácidos biliares SLC10A1.
  - Otras dianas: FPR1, peptidilprolil isomerasa A (PPIA) y peptidilprolil isomerasa D (PPID).
  - Los transportadores ABCG2 y OATP pueden ser relevantes para interacciones con otros fármacos.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene una puntuación alta (99,68 %), pero solo la respaldan un ensayo de Fase 1 no específico y un estudio de cohorte sobre trasplante. La ciclosporina actúa aquí como apoyo del trasplante, sin evidencia de que trate la enfermedad en sí.

**Para avanzar se necesita:**
- Obtener y revisar la ficha técnica de AEMPS (advertencias y contraindicaciones), que actualmente falta.
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar evidencia específica del efecto de la ciclosporina en la enfermedad granulomatosa crónica, más allá del contexto de trasplante.
- Confirmar las indicaciones aprobadas de cada autorización de AEMPS para definir con claridad la indicación original.

**Otras predicciones del modelo:**
- El aneurisma cerebral (puntuación 99,50 %) figura como pregunta de investigación. Hay estudios pequeños en hemorragia subaracnoidea, pero un estudio en ratones indica que la función de los linfocitos T no es necesaria para la formación del aneurisma, lo que debilita la base mecanística.
- El resto de predicciones (síndrome de microftalmia colobomatosa-displasia rizomélica, eritrodermia ictiosiforme congénita, eritroblastosis fetal, síndrome de braquidactilia-sindactilia y prolapso de glándula lagrimal) son solo predicciones del modelo, sin ensayos ni literatura de respaldo relevante.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


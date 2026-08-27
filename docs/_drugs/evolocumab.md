---
layout: default
title: Evolocumab
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 6
---

# Evolocumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Evolocumab: Hacia Hemofilia Sintomática en Portadoras Femeninas (Predicción TxGNN)

## Resumen en Una Frase

La indicación original de Evolocumab no consta en los datos disponibles en este Evidence Pack (el fármaco no está comercializado en España y no hay licencias registradas). El modelo TxGNN predice que podría ser efectivo para **Hemofilia Sintomática en Portadoras Femeninas**, pero esta dirección no cuenta actualmente con **ningún ensayo clínico** ni **ninguna publicación** de respaldo, y el propio análisis mecanístico del sistema señala esta asociación como probable ruido del grafo de conocimiento.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en este Evidence Pack (dato pendiente) |
| Nueva Indicación Predicha | Hemofilia Sintomática en Portadoras Femeninas |
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

No se dispone de datos detallados y confirmados sobre el mecanismo de acción de Evolocumab en este Evidence Pack (pendiente de consulta a la API de DrugBank). No obstante, el propio análisis de racionalidad mecanística generado para esta predicción identifica a Evolocumab como un anticuerpo monoclonal inhibidor de PCSK9, cuya acción farmacológica conocida se centra en la vía de reciclaje del receptor de LDL para reducir el colesterol LDL.

Según ese mismo análisis, **no existe solapamiento mecanístico conocido** entre la inhibición de PCSK9 y la fisiopatología de la hemofilia sintomática en portadoras (que depende de deficiencias de Factor VIII/IX). El propio sistema clasifica esta asociación como posible **ruido de conexión en el grafo de conocimiento** (una relación espuria generada probablemente a través de nodos compartidos de tipo vascular/endotelial), y no como una hipótesis terapéutica fundamentada.

Es importante notar que este patrón se repite en las 5 direcciones adicionales generadas por TxGNN para este fármaco: en ningún caso hay solapamiento mecanístico claro, y en el caso de "thrombocytopenic purpura" el propio análisis advierte que la trombocitopenia es más bien una señal de seguridad conocida de los anticuerpos anti-PCSK9 que una señal de eficacia. A continuación se resumen las demás direcciones predichas, incluidas por transparencia:

| Rank | Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Veredicto del Análisis |
|------|------|------|------|------|
| 2 | Familial apolipoprotein C-II deficiency | 99.50% | L5 | Relación forzada, sin solapamiento de vía molecular |
| 3 | Thrombocytopenic purpura | 99.42% | L5 | Posible señal de riesgo, no de eficacia |
| 4 | Factor XI deficiency | 99.29% | L5 | Sin solapamiento mecanístico ni literatura de soporte |
| 5 | Hemophilia A with vascular abnormality | 99.22% | L5 | Hipótesis mecanística especulativa, sin evidencia directa |
| 6 | Disease of catalytic activity | 99.08% | L5 | Nodo de ontología genérico, no es una indicación clínica accionable |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Evolocumab no está actualmente comercializado en España según los datos disponibles en este Evidence Pack (0 autorizaciones registradas, estado: no comercializado).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos de advertencias, contraindicaciones e interacciones farmacológicas (DDI) de Evolocumab aún no han sido incorporados a este Evidence Pack; su obtención desde el prospecto oficial está marcada como brecha bloqueante para la evaluación de seguridad (S1).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- Todas las direcciones predichas se encuentran en nivel de evidencia L5 (solo predicción del modelo, sin ensayos clínicos ni literatura real de respaldo), y la principal candidata está señalada por el propio análisis mecanístico como probable ruido del grafo de conocimiento en lugar de una hipótesis terapéutica plausible.
- El fármaco no está comercializado en España y falta información de seguridad crítica (advertencias/contraindicaciones), lo que impide avanzar a la evaluación de seguridad S1.

**Para avanzar se necesita:**
- Resolver la brecha bloqueante DG001: obtener el prospecto oficial (advertencias, contraindicaciones) para permitir la evaluación de seguridad S1.
- Resolver la brecha DG002: confirmar el mecanismo de acción vía API de DrugBank.
- Búsqueda dirigida de evidencia mecanística o preclínica real (no solo asociación por grafo) antes de considerar cualquier candidata de este lote para las siguientes etapas.
- Reevaluar si tiene sentido continuar invirtiendo en estas 6 direcciones dado que ninguna cuenta con respaldo mecanístico sólido ni evidencia clínica/bibliográfica.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Lorlatinib
parent: 僅模型預測 (L5)
nav_order: 172
evidence_level: L5
indication_count: 10
---

# Lorlatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Lorlatinib: De Cáncer de Pulmón ALK/ROS1-Positivo a Fibromatosis Gingival

## Resumen en Una Frase

Lorlatinib es un inhibidor de tirosina-cinasa de tercera generación dirigido a ALK/ROS1, cuya eficacia en cáncer de pulmón no microcítico (NSCLC) ALK-positivo está ampliamente documentada en la literatura recogida en este evidence pack (ensayo CROWN, fase 3). El modelo TxGNN predice como principal candidato **Fibromatosis Gingival**, con una puntuación de 99.81%, pero **sin ningún ensayo clínico ni publicación** que respalde esta dirección, y el propio análisis del pipeline indica que no existe relación mecanística conocida entre la vía ALK/ROS1 y esta enfermedad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de pulmón no microcítico (NSCLC) ALK/ROS1-positivo *(no consta en ficha regulatoria de España; deducido del contexto bibliográfico del propio evidence pack)* |
| Nueva Indicación Predicha | Fibromatosis Gingival |
| Puntaje de Predicción TxGNN | 99.81% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción (campo MOA marcado como *Data Gap*). Según la información contenida en la literatura de este evidence pack, lorlatinib es un inhibidor de tirosina-cinasa de tercera generación dirigido a ALK y ROS1, cuya eficacia en NSCLC ALK-positivo ha sido demostrada de forma robusta (estudio CROWN, fase 3).

Sin embargo, para la indicación predicha en primer lugar —**fibromatosis gingival**— el propio análisis del pipeline concluye que **no existe relación mecanística plausible**: esta enfermedad se asocia principalmente a mutaciones del gen SOS1 y a alteraciones del metabolismo del colágeno, vías completamente ajenas a la señalización ALK/ROS1 que bloquea lorlatinib. No hay ningún ensayo clínico ni publicación que conecte ambos conceptos; la predicción proviene únicamente de la similitud calculada por el modelo TxGNN, sin ningún tipo de corroboración externa.

En consecuencia, esta predicción concreta no tiene, por ahora, una base biológica identificable que justifique avanzar en su investigación.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Lorlatinib no está comercializado en España (0 autorizaciones registradas en el evidence pack), por lo que no existe información de producto ni indicación aprobada localmente que resumir.

---

## Citotoxicidad

Lorlatinib pertenece al grupo de los antineoplásicos (inhibidor de tirosina-cinasa dirigido, usado en NSCLC ALK/ROS1-positivo según la literatura recogida).

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina-cinasa ALK/ROS1) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Ítems de Monitoreo | Perfil lipídico (hipercolesterolemia/hipertrigliceridemia descritas en literatura de farmacovigilancia), función hepática y renal, función respiratoria (casos de SDRA descritos), estado cognitivo/de ánimo |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Los campos formales de seguridad (advertencias clave, contraindicaciones, interacciones farmacológicas) están vacíos en las fuentes consultadas (TFDA/prospecto no localizado). Consultar el prospecto para información de seguridad oficial.

No obstante, durante la búsqueda bibliográfica de este evidence pack aparecieron de forma incidental varias señales de seguridad sobre lorlatinib (en publicaciones asociadas erróneamente a otras indicaciones, ver sección de Conclusión): síndrome de dificultad respiratoria aguda (SDRA), dislipidemia/síndrome metabólico (hipercolesterolemia, hipertrigliceridemia, aumento de peso) y síndrome nefrótico. Son señales de nivel de reporte de caso / farmacovigilancia (FAERS), no datos de ficha técnica oficial, por lo que deben tomarse como orientativas.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación de mayor puntuación TxGNN (fibromatosis gingival, 99.81%) carece por completo de respaldo clínico o mecanístico. Además, al revisar el conjunto de las 10 indicaciones predichas para este fármaco en el evidence pack, se detecta un patrón sistemático de problemas de calidad de datos: varias etiquetas de enfermedad parecen ser errores de mapeo ontológico del pipeline TxGNN, que en realidad recuperan literatura sobre la indicación *ya aprobada* de NSCLC ALK+/ROS1+ (rank 5, ensayo CROWN), sobre neuroblastoma pediátrico ALK-mutado (rank 6), sobre demencia frontotemporal sin relación con el fármaco (rank 8), o sobre reacciones adversas del propio lorlatinib mal etiquetadas como indicación (rank 10). Solo la candidata "lung hilum carcinoma" (rank 4) presenta una hipótesis mecanística mínimamente plausible (posible subtipo anatómico de NSCLC ALK+), pero respaldada únicamente por 1 caso clínico.

**Para avanzar se necesita:**
- Corregir el mapeo de ontología de enfermedades del pipeline TxGNN (múltiples etiquetas erróneas identificadas en este mismo lote)
- Obtener datos estructurados de MOA desde DrugBank (actualmente Data Gap)
- Localizar y procesar el prospecto/ficha técnica de TFDA para advertencias y contraindicaciones formales (Data Gap bloqueante, DG001)
- Si se desea explorar "lung hilum carcinoma" (rank 4), evaluarla como posible extensión anatómica de la indicación ya aprobada, no como reposicionamiento nuevo
- Considerar reevaluar por separado "neuroblastoma pediátrico ALK-mutado" con la etiqueta correcta, dado que cuenta con ensayos fase 1/2 reales (actualmente oculto bajo la etiqueta errónea "lung germ cell tumor")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Ravulizumab
parent: 僅模型預測 (L5)
nav_order: 238
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab: De Sindrome Hemolitico Uremico Atipico (aHUS) y Hemoglobinuria Paroxistica Nocturna (HPN) a Neutropenia Congenita Grave Autosomica Recesiva por Deficiencia de G6PC3

## Resumen en Una Frase

Ravulizumab es un anticuerpo monoclonal inhibidor del complemento C5, utilizado originalmente para el sindrome hemolitico uremico atipico (aHUS) y la hemoglobinuria paroxistica nocturna (HPN), tal como se menciona en el analisis mecanistico del propio Evidence Pack. El modelo TxGNN predice que podria ser efectivo para la **Neutropenia Congenita Grave Autosomica Recesiva por Deficiencia de G6PC3**, pero esta direccion actualmente **no cuenta con ningun ensayo clinico ni publicacion cientifica** que la respalde.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Sindrome Hemolitico Uremico Atipico (aHUS) y Hemoglobinuria Paroxistica Nocturna (HPN) |
| Nueva Indicacion Predicha | Neutropenia Congenita Grave Autosomica Recesiva por Deficiencia de G6PC3 |
| Puntaje de Prediccion TxGNN | 99.96% |
| Nivel de Evidencia | L5 (solo prediccion del modelo, sin estudios reales) |
| Estado de Mercado en Espana | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

No se dispone de una ficha tecnica formal del mecanismo de accion de ravulizumab en este Evidence Pack (dato pendiente de DrugBank). No obstante, el propio analisis mecanistico generado para cada candidato senala de forma consistente que ravulizumab actua como **inhibidor del complemento C5**, bloqueando la formacion del complejo de ataque de membrana (C5b-9/MAC). Esta es la base farmacologica de sus indicaciones aprobadas, aHUS y HPN, ambas enfermedades mediadas por activacion descontrolada del complemento.

La neutropenia congenita grave autosomica recesiva por deficiencia de G6PC3, en cambio, es una enfermedad de origen metabolico: el defecto enzimatico genera estres del reticulo endoplasmico y apoptosis prematura de los neutrofilos, sin que exista una via de activacion del complemento involucrada en su fisiopatologia.

Segun la propia justificacion mecanistica del modelo, esta prediccion **no se apoya en una relacion biologica directa**, sino en una proximidad indirecta dentro del grafo de conocimiento (posible agrupamiento semantico en torno a "enfermedades de neutrofilos"). Es decir, el alto puntaje de TxGNN refleja una asociacion estadistica del modelo, no una hipotesis mecanistica solida. Esto se refleja tambien en que los 10 candidatos predichos en este paquete comparten el mismo patron: puntajes muy altos, pero nivel de evidencia L5 y ausencia total de ensayos clinicos o literatura de respaldo.

---

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Informacion de Mercado en Espana

Ravulizumab **no esta comercializado actualmente en Espana** segun los registros consultados (0 autorizaciones encontradas), por lo que no hay informacion de producto local disponible en este momento.

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad. La busqueda de advertencias, contraindicaciones e interacciones farmacologicas (DDI) no arrojo resultados en las fuentes consultadas para este informe.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La prediccion se encuentra en nivel de evidencia L5 (solo modelo, sin ensayos ni literatura de respaldo) y en etapa de decision S0. Ademas, existe un vacio de datos de caracter bloqueante (advertencias/contraindicaciones del prospecto de la agencia reguladora) que impide completar siquiera la evaluacion inicial de seguridad (S1). Con la evidencia mecanistica descrita como indirecta y sin ningun estudio real disponible, no se justifica avanzar mas alla de la observacion.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha tecnica oficial con advertencias y contraindicaciones (vacio de datos bloqueante)
- Datos formales del mecanismo de accion desde DrugBank para confirmar y detallar la via de inhibicion de C5
- Al menos un estudio preclinico o de mecanismo que conecte la inhibicion del complemento con la fisiopatologia de la neutropenia por deficiencia de G6PC3
- Monitoreo continuo de nuevas publicaciones o registros de ensayos clinicos, dado que actualmente no existe ninguno para esta indicacion
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


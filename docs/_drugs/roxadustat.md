---
layout: default
title: Roxadustat
parent: 僅模型預測 (L5)
nav_order: 249
evidence_level: L5
indication_count: 4
---

# Roxadustat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# ROXADUSTAT: De Anemia Renal a Sindrome de Ojo Seco

## Resumen en Una Frase

Roxadustat es un inhibidor de la prolil-hidroxilasa de HIF (HIF-PHI), utilizado terapeuticamente para la anemia renal (segun el contexto clinico de los ensayos disponibles; no consta como indicacion registrada formalmente en esta base de datos).
El modelo TxGNN predice que podria ser efectivo para el **Sindrome de Ojo Seco**,
pero actualmente solo existe **1 ensayo clinico indirecto** y **ninguna publicacion** que respalde esta direccion.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Anemia renal (uso terapeutico conocido segun el contexto de los ensayos; sin registro formal disponible en esta base) |
| Nueva Indicacion Predicha | Sindrome de Ojo Seco |
| Puntaje de Prediccion TxGNN | 99.51% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Espana | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

No hay datos estructurados de DrugBank sobre el mecanismo de accion (MOA) en este Evidence Pack (brecha de datos de severidad Alta). Sin embargo, la propia anotacion de TxGNN describe a roxadustat como un **inhibidor de la prolil-hidroxilasa de HIF (HIF-PHI)**, que estabiliza HIF-1α/HIF-2α para estimular la produccion endogena de eritropoyetina (EPO), mecanismo por el cual trata la anemia asociada a enfermedad renal cronica.

La via HIF esta tambien implicada, en teoria, en la regulacion de la angiogenesis de la superficie ocular y en la secrecion lipidica de las glandulas de Meibomio, lo que ofrece una posible base mecanistica para el sindrome de ojo seco. No obstante, esta conexion es puramente especulativa: el unico ensayo disponible no evalua roxadustat como tratamiento del ojo seco, sino que estudia la funcion de las glandulas de Meibomio en pacientes con anemia renal (que podrian o no estar en tratamiento con roxadustat). La anemia y la enfermedad renal cronica son en si mismas factores de riesgo conocidos de ojo seco, lo que introduce una variable de confusion no controlada en esta evidencia.

---

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06287879](https://clinicaltrials.gov/study/NCT06287879) | No aplica | Desconocido | 50 | Estudio observacional sobre la funcion y morfologia de las glandulas de Meibomio en pacientes con anemia renal (tratados con EPO o roxadustat) que presentan sintomas de ojo seco. **No evalua la eficacia de roxadustat sobre el ojo seco**; la relevancia se califica como Grado C (asociacion indirecta, sin objetivo interventivo, con variables de confusion no controladas). |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Informacion de Mercado en Espana

Roxadustat no cuenta actualmente con autorizacion de comercializacion en Espana (0 autorizaciones registradas en la base de datos consultada).

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad (no hay advertencias, contraindicaciones ni interacciones farmacologicas disponibles en esta base de datos; la ficha tecnica de TFDA no ha podido consultarse — brecha de datos bloqueante).

**Senal mecanistica relevante:** entre las indicaciones adicionales predichas por el modelo (no evaluadas en este informe como candidato principal) se encuentra el carcinoma escamocelular. La estabilizacion de HIF-1α/2α es un mecanismo conocido de progresion tumoral y angiogenesis en canceres solidos, por lo que esa prediccion debe interpretarse como una **alerta de seguridad mecanistica** (similitud farmacologica con el mecanismo de la enfermedad) y no como una oportunidad terapeutica. Se recomienda tenerlo en cuenta en cualquier evaluacion de riesgo-beneficio de roxadustat en poblaciones oncologicas o con lesiones premalignas.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La unica evidencia clinica disponible es un estudio observacional de relevancia indirecta (Grado C) que no prueba eficacia, no existe literatura de respaldo, y persisten brechas de datos bloqueantes (ficha tecnica/advertencias de seguridad) que impiden una evaluacion de seguridad inicial (S1).

**Para avanzar se necesita:**
- Ficha tecnica de TFDA con advertencias y contraindicaciones (brecha bloqueante DG001)
- Confirmacion del mecanismo de accion via DrugBank (brecha DG002)
- Un ensayo clinico disenado especificamente para evaluar roxadustat como tratamiento del sindrome de ojo seco (no como hallazgo secundario en pacientes con anemia renal)
- Evaluacion de riesgo oncologico antes de cualquier uso en poblaciones con antecedentes de neoplasias, dado el mecanismo HIF compartido con la progresion tumoral
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


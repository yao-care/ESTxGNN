---
layout: default
title: Siponimod
parent: 僅模型預測 (L5)
nav_order: 259
evidence_level: L5
indication_count: 8
---

# Siponimod
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Siponimod: De Esclerosis Multiple Secundariamente Progresiva a Hipertension Pulmonar

## Resumen en Una Frase

Siponimod es un modulador selectivo de los receptores S1P1/S1P5, actualmente indicado para la esclerosis multiple secundariamente progresiva (segun se menciona en el analisis de otra indicacion candidata de este mismo informe; el farmaco no esta comercializado en España y no hay ficha tecnica local disponible). El modelo TxGNN predice que podria ser efectivo para **Hipertension Pulmonar**, pero actualmente **no existe ningun ensayo clinico ni publicacion** que respalde esta direccion — se trata de una prediccion puramente algoritmica.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Esclerosis multiple secundariamente progresiva (referencia indirecta hallada en el racional de otra indicacion candidata; sin confirmacion en ficha tecnica española) |
| Nueva Indicacion Predicha | Hipertension Pulmonar |
| Puntaje de Prediccion TxGNN | 99.68% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion original en este informe (dato marcado como brecha de informacion, DG002). Segun la informacion parcial disponible en el analisis de otras indicaciones candidatas, siponimod actua como modulador selectivo de los receptores de esfingosina-1-fosfato (S1P1/S1P5), un mecanismo compartido con otros farmacos de su clase (p. ej. fingolimod) que regulan el trafico linfocitario y tienen efectos conocidos sobre el tono vascular.

La via de señalizacion S1P esta mecanisticamente relacionada con el remodelado vascular, lo que ofrece una hipotesis teorica plausible de vinculo con la hipertension pulmonar. Sin embargo, esta conexion es puramente especulativa: el conjunto de datos revisado no contiene ningun ensayo clinico ni publicacion cientifica que evalue siponimod en hipertension pulmonar. El puntaje elevado del modelo TxGNN (99.68%) refleja unicamente una asociacion aprendida por la red, no evidencia clinica real.

Por este motivo, esta prediccion se clasifica en el nivel de evidencia mas bajo (L5) y no debe interpretarse como una senal de eficacia, sino como una hipotesis de investigacion sin respaldo experimental actual.

---

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Informacion de Mercado en España

Siponimod no cuenta con autorizaciones de comercializacion registradas en España (0 autorizaciones, estado de mercado: no comercializado). No hay informacion de producto, forma farmaceutica ni indicacion aprobada disponible para tabular.

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

*Nota: el analisis de otra indicacion candidata dentro de este mismo informe (angina de Prinzmetal) señala que los moduladores S1P como siponimod tienen un riesgo conocido de bradicardia y bloqueo auriculoventricular en la primera dosis. Este dato no proviene de la ficha tecnica local (no disponible, brecha DG001) sino de referencia cruzada dentro del propio analisis, por lo que debe verificarse contra fuente oficial antes de su uso clinico.*

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La prediccion de hipertension pulmonar se basa unicamente en el puntaje del modelo TxGNN, sin ningun ensayo clinico ni publicacion que la respalde (nivel de evidencia L5). No existe base experimental suficiente para avanzar a evaluacion de seguridad o eficacia en este momento.

**Para avanzar se necesita:**
- Ficha tecnica/prospecto oficial de la AEMPS (brecha bloqueante DG001) para habilitar la evaluacion de seguridad inicial (S1)
- Datos detallados del mecanismo de accion desde DrugBank (brecha DG002)
- Estudios preclinicos o de mecanismo que vinculen especificamente la modulacion S1P1/S1P5 con la fisiopatologia de la hipertension pulmonar
- Monitoreo continuo de nuevas publicaciones y registros de ensayos clinicos para esta combinacion farmaco-indicacion
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


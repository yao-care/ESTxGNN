---
layout: default
title: Selinexor
parent: 僅模型預測 (L5)
nav_order: 254
evidence_level: L5
indication_count: 1
---

# Selinexor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Selinexor: De Mieloma Multiple a Osteoporosis Inducida por Farmacos

## Resumen en Una Frase

Selinexor es un inhibidor selectivo de la exportacion nuclear (XPO1/CRM1), utilizado clinicamente en combinacion con dexametasona para el mieloma multiple y el linfoma difuso de celulas B grandes. El modelo TxGNN predice una asociacion con **Osteoporosis Inducida por Farmacos**, pero actualmente **no existe ningun ensayo clinico ni publicacion** que respalde esta direccion — la puntuacion se basa unicamente en el modelo predictivo.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Mieloma Multiple / Linfoma Difuso de Celulas B Grandes (uso clinico conocido; no registrado en los campos estructurados del Evidence Pack) |
| Nueva Indicacion Predicha | Osteoporosis Inducida por Farmacos |
| Puntaje de Prediccion TxGNN | 99.22% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion en el Evidence Pack (campo `original_moa` marcado como carencia de datos). Segun la informacion conocida, selinexor es un inhibidor selectivo de XPO1/CRM1 (clase SINE), utilizado habitualmente junto con dexametasona en el tratamiento del mieloma multiple y el linfoma difuso de celulas B grandes.

Esta combinacion terapeutica (selinexor + dexametasona) es en si misma un regimen con riesgo conocido de perdida osea, y los efectos adversos frecuentes de selinexor — anorexia, perdida de peso y fatiga — podrian contribuir teoricamente a un deterioro del estado oseo.

Sin embargo, esto sugiere mas bien una relacion de **toxicidad inducida por el farmaco** que una oportunidad de reposicionamiento terapeutico. La puntuacion elevada de TxGNN (99.22%) no permite distinguir entre ambas posibilidades sin literatura de respaldo, por lo que esta senal debe interpretarse como una posible alerta de seguridad y no como evidencia de eficacia.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificacion de Citotoxicidad | Terapia dirigida (inhibidor selectivo de exportacion nuclear XPO1/CRM1, clase SINE) |
| Riesgo de Mielosupresion | Consultar las advertencias y precauciones del prospecto |
| Clasificacion de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Proteccion en Manejo | Consultar las advertencias y precauciones del prospecto (manejo de agentes antineoplasicos) |

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

*Nota: la falta de datos de advertencias/contraindicaciones (TFDA) constituye una brecha bloqueante que impide actualmente la evaluacion inicial de seguridad (S1) de este candidato.*

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La prediccion se apoya exclusivamente en el modelo TxGNN (L5), sin ningun ensayo clinico ni publicacion de respaldo, y la asociacion planteada (osteoporosis inducida) sugiere mas una senal de toxicidad que una oportunidad terapeutica. Ademas, la ausencia de datos de seguridad (TFDA) es una brecha bloqueante que impide continuar la evaluacion.

**Para avanzar se necesita:**
- Datos de advertencias, contraindicaciones y prospecto de TFDA (brecha bloqueante DG001)
- Registro estructurado del mecanismo de accion (MOA) desde DrugBank (DG002)
- Busqueda dirigida de literatura/farmacovigilancia sobre perdida osea asociada a selinexor, para aclarar si la senal es de eficacia o de toxicidad
- Confirmacion de si esta indicacion debe tratarse como senal de seguridad (farmacovigilancia) en lugar de candidato de reposicionamiento
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


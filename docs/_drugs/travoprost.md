---
layout: default
title: Travoprost
parent: 僅模型預測 (L5)
nav_order: 284
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: De Glaucoma de Angulo Abierto/Hipertension Ocular a Calcifilaxis Visceral

## Resumen en Una Frase

Travoprost es un analogo de prostaglandina de uso oftalmico topico, utilizado originalmente para reducir la presion intraocular en glaucoma de angulo abierto e hipertension ocular. El modelo TxGNN predice que podria ser efectivo para **Calcifilaxis Visceral**, pero actualmente **no existe ningun ensayo clinico ni publicacion** que respalde esta direccion — se trata unicamente de una senal computacional sin evidencia real.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Glaucoma de angulo abierto / hipertension ocular (uso oftalmico topico) |
| Nueva Indicacion Predicha | Calcifilaxis Visceral |
| Puntaje de Prediccion TxGNN | 99.9998% |
| Nivel de Evidencia | L5 |
| Estado de Mercado Local | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Travoprost es un profarmaco del analogo de PGF2α que, tras su hidrolisis, activa el receptor prostanoide FP. Este mecanismo reduce la presion intraocular al aumentar el flujo de salida uveoescleral, y la senalizacion PGF2α/FP tambien participa en la regulacion del tono vascular en algunos lechos vasculares (con efectos de contraccion o relajacion segun el tejido).

Sin embargo, no existe en este momento ninguna relacion mecanistica documentada entre la activacion del receptor FP y la calcifilaxis (una enfermedad de calcificacion vascular/microtrombosis cutanea y visceral). La calcifilaxis involucra vias fisiopatologicas distintas (metabolismo de calcio-fosforo, calcificacion de la media arteriolar, trombosis microvascular) que no se solapan de forma conocida con la farmacologia ocular de travoprost.

En consecuencia, esta prediccion debe entenderse como una senal exploratoria generada por el modelo, sin respaldo mecanistico ni clinico verificado hasta la fecha.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La prediccion se basa unicamente en el puntaje del modelo TxGNN (rank 20 de la lista de candidatos), sin ningun ensayo clinico, estudio observacional o literatura que la respalde, y sin un mecanismo de accion establecido que conecte travoprost con la calcifilaxis. El nivel de evidencia (L5) y la etapa de decision (S0) no son suficientes para avanzar a evaluacion de seguridad.

**Para avanzar se necesita:**
- Datos de mecanismo de accion (MOA) verificados de DrugBank, actualmente marcados como brecha de datos (DG002)
- Advertencias y contraindicaciones del prospecto de TFDA/agencia reguladora local, actualmente bloqueante (DG001)
- Estudios preclinicos que exploren una via mecanistica plausible entre agonismo del receptor FP y calcificacion vascular/microtrombosis
- Nota: dentro del mismo Evidence Pack, el candidato de rango inferior "vascular disease" (rank 35) cuenta con 15 ensayos y 20 publicaciones, aunque el analisis indica que todos corresponden a la indicacion original (glaucoma/IOP) mal clasificada bajo ese nombre de enfermedad — no constituye evidencia de reposicionamiento real, pero merece revision separada si se continua este candidato
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


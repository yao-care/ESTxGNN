---
layout: default
title: Calcipotriol
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
---

# Calcipotriol
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

# Calcipotriol: De Psoriasis a Queratosis Seborreica

## Resumen en Una Frase

Calcipotriol es un analogo topico de la vitamina D3, tradicionalmente empleado en el tratamiento de la psoriasis.
El modelo TxGNN predice que podria ser efectivo para **Queratosis Seborreica**,
con **0 ensayos clinicos registrados** y **6 publicaciones** que actualmente respaldan esta direccion.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Psoriasis (uso topico; no hay autorizaciones registradas en España para confirmar el texto oficial de indicacion) |
| Nueva Indicacion Predicha | Queratosis Seborreica |
| Puntaje de Prediccion TxGNN | 99.96% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Espana | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Proceed with Guardrails |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion en el Evidence Pack. Segun la informacion conocida, calcipotriol es un analogo de la vitamina D3 utilizado por via topica, cuya eficacia en psoriasis esta bien establecida; actua a traves del receptor de vitamina D (VDR) regulando la proliferacion y diferenciacion de los queratinocitos.

La queratosis seborreica es un tumor epitelial benigno de crecimiento lento, caracterizado precisamente por una proliferacion excesiva de queratinocitos — el mismo tipo celular que calcipotriol regula en la psoriasis. Esta similitud mecanistica hace plausible la prediccion del modelo TxGNN.

La literatura disponible refuerza esta hipotesis: varios estudios documentan el uso de calcipotriol (y otros analogos de vitamina D3 como tacalcitol y maxacalcitol) en el tratamiento de queratosis seborreica/verrugas seniles, con un articulo (PMID 16043912) que propone explicitamente la induccion de apoptosis como via de accion adicional a la regulacion de la diferenciacion celular.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36752725](https://pubmed.ncbi.nlm.nih.gov/36752725/) | 2023 | Estudio Clinico (Eficacia/Seguridad) | The Australasian journal of dermatology | Serie de 12 pacientes con queratosis seborreica facial tratados con pomada de calcipotriol 0.005% (3-8 meses); regresion completa de las lesiones, remision de 6 a 10 anos. |
| [15090020](https://pubmed.ncbi.nlm.nih.gov/15090020/) | 2004 | Estudio Clinico Comparativo | International journal of dermatology | Comparacion de crioterapia estandar frente a calcipotrieno, tazaroteno e imiquimod topicos en queratosis seborreica. |
| [16043912](https://pubmed.ncbi.nlm.nih.gov/16043912/) | 2005 | Estudio Clinico Mecanistico | The Journal of dermatology | Vitamina D3 topica (tacalcitol, calcipotriol, maxacalcitol) eficaz en verrugas seniles (queratosis seborreica); de 116 casos tratados 3-12 meses, 35 (30.2%) mostraron respuesta, posiblemente por induccion de apoptosis. |
| [10721662](https://pubmed.ncbi.nlm.nih.gov/10721662/) | 2000 | Reporte de Caso | The Journal of dermatology | Respuesta marcada a pomada de calcipotriol en queratosis liquenoide cronica, dermatosis rara con componente seborreico-like. |
| [21534378](https://pubmed.ncbi.nlm.nih.gov/21534378/) | 2011 | Reporte de Caso | JAAPA | Vineta clinica de queratosis seborreica presentada como erupcion pruriginosa moteada en las espinillas. |
| [15577148](https://pubmed.ncbi.nlm.nih.gov/15577148/) | 2004 | Serie de Casos/Revision | Clinical calcium | Revision sobre aplicacion topica de formas activas de vitamina D3 (tacalcitol, calcipotriol, maxacalcitol) en verrugas seniles/queratosis seborreica. |

## Informacion de Mercado en Espana

Calcipotriol no cuenta actualmente con autorizaciones de comercializacion registradas en Espana (0 autorizaciones en el Evidence Pack), por lo que no es posible presentar informacion de productos comercializados.

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Proceed with Guardrails**

**Justificacion:**
Existe un cuerpo consistente de evidencia clinica de nivel L3 (estudios comparativos, series de casos y estudios mecanisticos, incluyendo una serie con seguimiento de hasta 10 anos) que respalda la eficacia topica de calcipotriol en queratosis seborreica, aunque aun no existen ensayos clinicos aleatorizados registrados ni comercializacion en Espana.

**Para avanzar se necesita:**
- Datos del mecanismo de accion (MOA) verificados via DrugBank
- Warnings/contraindicaciones y perfil de interacciones (actualmente sin datos)
- Confirmacion del estado regulatorio y texto de indicacion original via AEMPS/TFDA (el farmaco no esta comercializado en Espana)
- Diseno de un ensayo clinico prospectivo/aleatorizado que confirme la senal observada en series de casos
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Carfilzomib
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 5
---

# Carfilzomib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Carfilzomib: De Mieloma Multiple a Melanoma

## Resumen en Una Frase

Carfilzomib es un inhibidor de proteasoma utilizado originalmente en el tratamiento del mieloma multiple.
El modelo TxGNN predice que podria ser efectivo para **Melanoma**,
con **0 ensayos clinicos** pero **5 publicaciones** (evidencia preclinica/mecanistica) que actualmente respaldan esta direccion.

Nota de alcance: TxGNN genero 5 candidatos relacionados con melanoma para este farmaco (CMM7, melanoma leptomeningeo pediatrico, melanoma uveal epitelioide, melanoma vulvar y melanoma general). Los primeros 4 no tienen ninguna evidencia real asociada (ensayos = 0, literatura = 0, etapa S0, recomendacion Hold) y corresponden a subtipos muy raros o a un locus de susceptibilidad genetica, no a una indicacion tratable directa. Solo "Melanoma" (rank 5) cuenta con literatura de respaldo y alcanzo la etapa S1; por eso este informe se centra en dicho candidato.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Mieloma Multiple |
| Nueva Indicacion Predicha | Melanoma |
| Puntaje de Prediccion TxGNN | 99.03% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Espana | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Segun la informacion recogida en la evidencia asociada a esta prediccion, carfilzomib es un inhibidor de proteasoma de segunda generacion e irreversible: inhibe la actividad chymotrypsin-like del proteasoma 26S, bloquea la via NF-kB e induce la respuesta a proteinas mal plegadas (UPR) junto con apoptosis por via mitocondrial. Su eficacia en mieloma multiple es un hecho farmacologico bien establecido; los datos estructurados de MOA y de indicacion original no fueron capturados en este Evidence Pack (ver vacios de datos DG002).

El mieloma multiple y el melanoma comparten una caracteristica que sustenta la hipotesis de reposicionamiento: ambos son tipos tumorales con alto recambio proteico y sensibilidad a estres proteotoxico. Las celulas de melanoma, especialmente bajo activacion de la via BRAF/MAPK, dependen fuertemente de la degradacion proteasomal para sobrevivir, lo que las haria vulnerables a la inhibicion del proteasoma.

Esta hipotesis ya cuenta con precedente mecanistico en la clase farmacologica: bortezomib, otro inhibidor de proteasoma, ha mostrado en estudios preclinicos inducir apoptosis en celulas de melanoma. La literatura disponible para carfilzomib en melanoma es, sin embargo, exclusivamente preclinica (in vitro / in silico) y no incluye ningun ensayo clinico en humanos, por lo que la evidencia respalda la plausibilidad biologica pero no la eficacia clinica.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | In Vitro (linea celular B16-F1) | Biology | Carfilzomib combinado con bortezomib induce apoptosis en celulas de melanoma B16-F1, con activacion de caspasas 3, 8, 9 y 12 |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | In Silico (docking molecular/dinamica) | J Biomol Struct Dyn | Cribado de reposicionamiento de farmacos mediante docking molecular contra dianas quinasa en 10 tipos de cancer, incluido melanoma |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | In Vitro/Mecanistico | Matrix Biol | Bortezomib y carfilzomib activan la via NF-kB e inducen expresion de heparanasa asociada a fenotipo tumoral agresivo |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | In Vitro (regulacion genica) | Mol Cancer Res | El gen ZFAND2A/AIRAP regula la supervivencia celular en melanoma humano via la E3-ligasa cIAP2, en contexto de estres proteotoxico |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | In Vitro (PROTAC) | Leukemia | Moleculas quimericas dirigidas a proteinas BET son activas en modelos preclinicos de mieloma multiple, con degradacion proteasomal |

## Informacion de Mercado en Espana

Carfilzomib no cuenta con autorizaciones de comercializacion registradas en Espana (estado: No comercializado, 0 autorizaciones).

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificacion de Citotoxicidad | Terapia dirigida (inhibidor de proteasoma de segunda generacion) |
| Riesgo de Mielosupresion | Consultar las advertencias y precauciones del prospecto |
| Clasificacion de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Proteccion en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La evidencia disponible para carfilzomib en melanoma es exclusivamente preclinica/mecanistica (nivel L4), sin ningun ensayo clinico en humanos. El farmaco no esta comercializado en Espana y faltan datos criticos de seguridad (advertencias TFDA, contraindicaciones, interacciones), lo que impide una evaluacion de seguridad inicial (vacio bloqueante DG001).

**Para avanzar se necesita:**
- Ficha tecnica/prospecto de TFDA con advertencias y contraindicaciones (DG001, bloqueante)
- Confirmacion del mecanismo de accion via DrugBank (DG002)
- Estudios preclinicos in vivo (modelos animales de melanoma) que confirmen la senal observada in vitro
- Al menos un ensayo clinico de fase temprana en melanoma humano antes de reconsiderar la etapa de decision
- Reevaluar los otros 4 candidatos relacionados (CMM7, melanoma leptomeningeo pediatrico, melanoma uveal epitelioide, melanoma vulvar) solo si aparece evidencia real; actualmente permanecen en Hold por ausencia total de datos
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


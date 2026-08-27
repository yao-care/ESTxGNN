---
layout: default
title: Zanamivir
parent: 僅模型預測 (L5)
nav_order: 297
evidence_level: L5
indication_count: 2
---

# Zanamivir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Zanamivir: De Antiviral para Influenza a Pielonefritis

## Resumen en Una Frase

Zanamivir es un inhibidor de la neuraminidasa viral, conocido por su uso como antiviral en el tratamiento y profilaxis de la influenza A/B.
El modelo TxGNN predice que podria ser efectivo para **Pielonefritis**,
pero actualmente **no hay ningun ensayo clinico ni publicacion** que respalde directamente esta direccion, y el analisis mecanistico disponible indica que no existe una relacion conocida entre el mecanismo antiviral del farmaco y la fisiopatologia bacteriana de esta condicion.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No consta en registros formales (Zanamivir no esta comercializado en Taiwan); segun la descripcion mecanistica adjunta al evidence pack, su uso conocido es como antiviral frente a influenza |
| Nueva Indicacion Predicha | Pielonefritis |
| Puntaje de Prediccion TxGNN | 99.84% (rank 3481) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Taiwan | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos estructurados sobre el mecanismo de accion (campo `original_moa` marcado como vacio, brecha de datos de severidad **High**). Segun la informacion narrativa disponible en el evidence pack, Zanamivir actua como inhibidor de la neuraminidasa viral, una proteina de superficie del virus de la influenza, bloqueando la liberacion de nuevas particulas virales de las celulas infectadas.

La pielonefritis, en cambio, es mayoritariamente una infeccion bacteriana ascendente del tracto urinario que afecta al rinon. No existe una neuraminidasa bacteriana homologa relevante ni una via inflamatoria urinaria conocida sobre la que actue este farmaco. El propio analisis mecanistico incluido en el evidence pack concluye explicitamente que **no hay evidencia de un mecanismo compartido** entre ambas condiciones.

En consecuencia, esta prediccion de TxGNN debe interpretarse como una senal de alto puntaje estadistico sin respaldo mecanistico ni de evidencia real (ensayos clinicos = 0, literatura = 0), lo que justifica una recomendacion de **Hold** en esta etapa (`decision_stage: S0`).

---

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Senal Secundaria Detectada (Segundo Candidato del Modelo)

El evidence pack incluye un segundo candidato de menor prioridad que se resume aqui por transparencia, dado que cuenta con literatura asociada (aunque no directamente relevante):

**Trastorno del metabolismo de la tirosina** — Puntaje TxGNN: 99.02% (rank 12601) — Nivel de Evidencia: L5 — Recomendacion: Hold

Este trastorno es una anomalia metabolica congenita (deficiencia enzimatica hepatica, p. ej. FAH, TAT, HPD) sin relacion bioquimica con la inhibicion viral de neuraminidasa. La literatura recuperada no aborda este trastorno metabolico, sino resistencia antiviral y metodos de deteccion de neuraminidasa, por lo que se considera un probable falso positivo del modelo:

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23675925](https://pubmed.ncbi.nlm.nih.gov/23675925/) | 2013 | Revision | Infectious Disorders Drug Targets | Resistencia a oseltamivir por mutacion H275Y en neuraminidasa; no aborda metabolismo de tirosina |
| [25727669](https://pubmed.ncbi.nlm.nih.gov/25727669/) | 2015 | Otro (metodologia de deteccion) | J Mol Recognit | Ensayo de resonancia de plasmon superficial para medir inhibicion de neuraminidasa (mutante H274Y) |
| [21367898](https://pubmed.ncbi.nlm.nih.gov/21367898/) | 2011 | Otro (genotipo viral/patogenicidad) | Journal of Virology | Mutacion N294S en neuraminidasa y su efecto en patogenicidad de H5N1 |

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
Ambos candidatos predichos por TxGNN presentan Nivel de Evidencia L5 (solo prediccion del modelo, sin ensayos clinicos ni literatura directamente relevante) y etapa de decision S0. El propio analisis mecanistico incluido en el evidence pack concluye que no existe relacion biologica plausible entre el mecanismo antiviral de Zanamivir y ninguna de las dos indicaciones propuestas (pielonefritis bacteriana y trastorno congenito del metabolismo de la tirosina).

**Para avanzar se necesita:**
- Obtener el texto de advertencias/contraindicaciones del prospecto TFDA (brecha bloqueante DG001, impide la evaluacion inicial de seguridad S1)
- Documentar formalmente el mecanismo de accion via API de DrugBank (brecha DG002, severidad High)
- Buscar evidencia preclinica o clinica real y especifica que vincule Zanamivir con pielonefritis o con trastornos del metabolismo de la tirosina (actualmente inexistente)
- Reevaluar la prediccion si surgen nuevos datos; en su ausencia, ambos candidatos deben considerarse probables falsos positivos del modelo
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


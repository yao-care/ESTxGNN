---
layout: default
title: Andexanet Alfa
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 4
---

# Andexanet Alfa
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

# Andexanet Alfa: De Reversión de Anticoagulantes (Inhibidores del Factor Xa) a Hemofilia

> **Nota metodológica:** El Evidence Pack contiene 4 indicaciones predichas por TxGNN. Las 3 de mayor puntaje bruto (Glanzmann thrombasthenia, trastorno primario de liberación plaquetaria, enfermedad de von Willebrand tipo plaquetario) están en fase S0, nivel de evidencia L5 (0 ensayos, 0 literatura) y el propio modelo señala en su razonamiento que probablemente son artefactos de agrupación del grafo de conocimiento en torno a nodos de "sangrado/hemostasia", sin relación mecanística real. La única candidata que alcanzó fase S1 con evidencia real es **Hemofilia** (rank 4), por lo que este informe se centra en ella. Las otras tres se resumen brevemente al final.

## Resumen en Una Frase

Andexanet alfa es un agente de reversión usado para neutralizar el efecto anticoagulante de los inhibidores del factor Xa (apixabán, rivaroxabán) en caso de hemorragia grave. El modelo TxGNN predice, a través de su mecanismo secundario de unión al TFPI (inhibidor de la vía del factor tisular), un posible efecto prohemostático relevante en **Hemofilia**, con **0 ensayos clínicos** y **11 publicaciones** indirectas respaldando actualmente esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Reversión de la anticoagulación por inhibidores del factor Xa (uso como antídoto en hemorragia grave) |
| Nueva Indicación Predicha | Hemofilia |
| Puntaje de Predicción TxGNN | 99.10% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Prediccion?

El campo oficial de mecanismo de acción (MOA) está marcado como brecha de datos (DG002, severidad *High*), por lo que la siguiente explicación se basa en la información mecanística que sí aparece en el razonamiento de la propia predicción. Andexanet alfa es una proteína señuelo recombinante derivada del factor Xa: secuestra a los inhibidores directos del factor Xa (apixabán, rivaroxabán, edoxabán) y revierte su efecto anticoagulante. Además, tiene una acción secundaria conocida de unión y neutralización del TFPI (*tissue factor pathway inhibitor*), lo que puede potenciar la generación de trombina por la vía factor tisular/FVIIa.

La hemofilia A/B se caracteriza por deficiencia de factor VIII o IX, lo que limita la generación de trombina por la vía intrínseca. La neutralización de TFPI es una estrategia terapéutica ya validada clínicamente en hemofilia: marstacimab, un anticuerpo anti-TFPI, obtuvo su primera aprobación en octubre de 2024 en EE. UU. para profilaxis de hemofilia A/B sin inhibidores (PMID 39715914). Dado que andexanet alfa comparte esa misma actividad anti-TFPI como efecto secundario de su estructura señuelo de FXa, existe una analogía mecanística razonable para explorar un efecto prohemostático en hemofilia.

Sin embargo, esta es una extrapolación indirecta: la literatura disponible describe principalmente el uso de andexanet alfa como antídoto de anticoagulantes y su interferencia en pruebas de laboratorio de FVIII/FIX, no estudios de tratamiento directo de hemofilia. No existe ningún ensayo clínico registrado que pruebe esta hipótesis, de ahí el nivel de evidencia L4 (basado en mecanismo/analogía, no en estudios clínicos directos).

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39715914](https://pubmed.ncbi.nlm.nih.gov/39715914/) | 2025 | Revisión | Drugs | Primera aprobación de marstacimab (anti-TFPI) para profilaxis de hemofilia A/B sin inhibidores, validando la vía anti-TFPI como estrategia terapéutica en hemofilia |
| [38620086](https://pubmed.ncbi.nlm.nih.gov/38620086/) | 2024 | Cohorte | Circulation | Subanálisis de ANNEXA-4: eficacia y seguridad de andexanet alfa en hemorragia gastrointestinal aguda bajo inhibidores del factor Xa |
| [31962376](https://pubmed.ncbi.nlm.nih.gov/31962376/) | 2020 | Cohorte | Haemophilia | Andexanet alfa neutraliza la interferencia de rivaroxabán en pruebas de FVIII/FIX, relevante para el diagnóstico de hemofilia en pacientes anticoagulados |
| [33742436](https://pubmed.ncbi.nlm.nih.gov/33742436/) | 2021 | Revisión | Thrombosis and Haemostasis | Actualización ICSH sobre medición de anticoagulantes orales directos, incluye recomendaciones sobre agentes de reversión como andexanet alfa |
| [36819179](https://pubmed.ncbi.nlm.nih.gov/36819179/) | 2023 | Revisión | EJHaem | Revisión de protocolos hospitalarios del Reino Unido para el uso clínico de andexanet alfa |
| [31298165](https://pubmed.ncbi.nlm.nih.gov/31298165/) | 2019 | Revisión | Curr Pharm Des | Consideraciones anestésicas perioperatorias sobre nuevos agentes hemostáticos, incluyendo andexanet alfa |
| [30309890](https://pubmed.ncbi.nlm.nih.gov/30309890/) | 2018 | Revisión | Blood | Revisión sobre reversión de agentes anti-factor Xa y necesidades no cubiertas en pacientes con trauma |
| [31446606](https://pubmed.ncbi.nlm.nih.gov/31446606/) | 2019 | Revisión | Intern Emerg Med | Revisión de agentes de reversión para hemorragia mayor asociada a anticoagulantes orales |
| [28277769](https://pubmed.ncbi.nlm.nih.gov/28277769/) | 2017 | Revisión | Br J Hosp Med | Revisión sobre reversión de anticoagulantes orales directos |
| [27254626](https://pubmed.ncbi.nlm.nih.gov/27254626/) | 2016 | Revisión | Dtsch Med Wochenschr | Actualización sobre trastornos de coagulación en UCI, menciona idarucizumab y otros agentes de reversión |

## Informacion de Mercado en Espana

Andexanet alfa no está actualmente comercializado en España (0 autorizaciones registradas).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. (La ficha técnica/prospecto oficial no ha podido incorporarse aún — brecha bloqueante DG001.)

## Otras Predicciones TxGNN de Mayor Puntaje (No Evaluadas en Profundidad)

| Indicación | Puntaje TxGNN | Nivel de Evidencia | Motivo de exclusión |
|---|---|---|---|
| Glanzmann thrombasthenia | 99.77% | L5 | Defecto de GPIIb/IIIa plaquetario; sin relación mecanística con la vía Factor Xa/TFPI; 0 ensayos, 0 literatura |
| Trastorno primario de liberación plaquetaria | 99.76% | L5 | Defecto intrínseco plaquetario; sin relación con vía de coagulación de andexanet alfa; 0 ensayos, 0 literatura |
| Enfermedad de von Willebrand tipo plaquetario | 99.65% | L5 | Mecanismo en interacción GPIb-VWF, no en factor Xa; 0 ensayos, 0 literatura |

## Conclusion y Proximos Pasos

**Decisión: Hold**

**Justificación:**
Solo existe una analogía mecanística indirecta (actividad secundaria anti-TFPI) respaldada por literatura sobre reversión de anticoagulantes, sin ningún ensayo clínico ni estudio preclínico que pruebe directamente el efecto de andexanet alfa en hemofilia. El fármaco tampoco está comercializado en España y falta el prospecto oficial para evaluación de seguridad (DG001, bloqueante).

**Para avanzar se necesita:**
- Estudio preclínico/traslacional que confirme el efecto prohemostático de andexanet alfa vía neutralización de TFPI en un modelo de hemofilia
- Obtención del prospecto/ficha técnica oficial (TFDA/AEMPS) para completar la evaluación de seguridad S1 (DG001)
- Confirmación del mecanismo de acción oficial vía DrugBank (DG002)
- Evaluación de viabilidad práctica (vía de administración IV, coste, perfil de dosificación) frente al uso actual como antídoto de urgencia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


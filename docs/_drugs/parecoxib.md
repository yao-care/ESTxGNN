---
layout: default
title: Parecoxib
parent: 僅模型預測 (L5)
nav_order: 212
evidence_level: L5
indication_count: 4
---

# Parecoxib
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

# Parecoxib: De Dolor Postoperatorio Agudo a Migraña

## Resumen en Una Frase

Parecoxib es un inhibidor selectivo de la COX-2 (profármaco de valdecoxib), utilizado originalmente para el tratamiento a corto plazo del dolor postoperatorio agudo por vía parenteral.
El modelo TxGNN predice que podría ser efectivo para **Migraña**,
con **0 ensayos clínicos registrados** y **1 publicación** (un estudio piloto aleatorizado) que actualmente respalda esta dirección.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicación Original | Dolor postoperatorio agudo, tratamiento a corto plazo (no hay ficha técnica registrada en España) |
| Nueva Indicación Predicha | Migraña |
| Puntaje de Predicción TxGNN | 99.55% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción específico de parecoxib en la Evidence Pack. Según la información conocida del sector, parecoxib es un profármaco de valdecoxib y actúa como inhibidor selectivo de la ciclooxigenasa-2 (COX-2), bloqueando la síntesis de prostaglandinas proinflamatorias. Fue desarrollado originalmente para el tratamiento a corto plazo del dolor postoperatorio agudo por vía parenteral.

La migraña comparte con el dolor postoperatorio un componente fisiopatológico común: la inflamación neurogénica y la sensibilización periférica y central mediada por prostaglandinas, particularmente a través del sistema trigeminovascular. Los antiinflamatorios no esteroideos (AINE) ya cuentan con una base clínica establecida en el tratamiento agudo de la migraña, y la inhibición selectiva de COX-2 puede considerarse una extensión mecanística dentro de esa misma clase terapéutica.

Cabe destacar que el modelo también generó puntuaciones altas para subtipos relacionados (migraña con aura de tronco encefálico, susceptibilidad genética a la migraña) y para hipertensión pulmonar, pero estos carecen de evidencia clínica o literaria directa sobre parecoxib y se consideran de menor prioridad (nivel L4-L5) frente a la migraña general, que cuenta con un estudio piloto aleatorizado específico.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21996647](https://pubmed.ncbi.nlm.nih.gov/21996647/) | 2011 | ECA | Clinical Neuropharmacology | Estudio piloto que compara parecoxib intravenoso (40 mg), sumatriptán subcutáneo y rizatriptán oral (comprimido de disolución rápida, 10 mg) en el tratamiento del ataque agudo de migraña. |

## Informacion de Mercado en Espana

Parecoxib no está actualmente comercializado en España (0 autorizaciones registradas en la fuente consultada), por lo que no hay una tabla de autorizaciones que presentar.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusion y Proximos Pasos

**Decisión: Hold**

**Justificación:**
- La evidencia de eficacia es incipiente (nivel L2): solo existe un estudio piloto aleatorizado (2011), sin ensayos clínicos registrados específicamente para migraña.
- Existe una brecha bloqueante en los datos de seguridad (advertencias, contraindicaciones e interacciones no disponibles), por lo que no es posible completar la evaluación de seguridad inicial (S1) requerida antes de avanzar.

**Para avanzar se necesita:**
- Ficha técnica oficial con advertencias, contraindicaciones y posología, para completar la evaluación de seguridad S1.
- Datos estructurados del mecanismo de acción (MOA) desde DrugBank.
- Confirmación de las vías de administración disponibles frente a las requeridas para el tratamiento agudo de migraña (parecoxib es actualmente de uso parenteral/hospitalario).
- Un ensayo clínico adicional o de mayor tamaño muestral que confirme el hallazgo piloto de 2011 antes de considerar "Proceed with Guardrails".
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


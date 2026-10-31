---
layout: default
title: Dexketoprofen
parent: Solo predicción del modelo (L5)
nav_order: 241
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
monitor_inn: "dexketoprofen"
predicted_indications: ["tendinitis", "fibromyalgia", "myositis fibrosa", "idiopathic granulomatous myositis", "rheumatoid arthritis", "migraine disorder", "headache disorder", "migraine with brainstem aura", "exostosis", "congenital hypotrichosis milia"]
description: "Dexketoprofen: nueva indicación predicha, Tendinitis (nivel de evidencia L4)."
---

# Dexketoprofen
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Dexketoprofeno: De AINE Analgésico (indicación original no disponible) a Tendinitis
{: .text-alpha }

## Resumen en Una Frase

Dexketoprofeno es un antiinflamatorio no esteroideo (AINE) comercializado en España en múltiples formas (comprimidos, solución oral, inyectable y perfusión). Los datos compilados para este informe no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **tendinitis**, pero actualmente hay **0 ensayos clínicos** y **1 publicación** indirecta que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Tendinitis |
| Puntaje de Predicción TxGNN | 0.9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 15) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según lo conocido, dexketoprofeno es un AINE que inhibe la ciclooxigenasa (COX-1/COX-2) y reduce la inflamación y el dolor mediados por prostaglandinas.

La tendinitis es una inflamación del tendón, por lo que un fármaco que reduce la inflamación y el dolor mediados por prostaglandinas es mecanísticamente plausible. Esta plausibilidad es general: no hay estudios que evalúen dexketoprofeno específicamente en tendinitis.

La única publicación vinculada estudia dolor musculoesquelético no traumático en urgencias, donde la tendinitis aparece solo como una de varias causas posibles. Es evidencia indirecta, y el puntaje alto de TxGNN debe interpretarse como una hipótesis, no como confirmación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30744914](https://pubmed.ncbi.nlm.nih.gov/30744914/) | 2019 | ECA | The American Journal of Emergency Medicine | Compara dexketoprofeno intravenoso con paracetamol para aliviar el dolor musculoesquelético agudo no traumático en urgencias. La tendinitis se menciona solo como una de sus posibles causas, por lo que la evidencia es indirecta. |

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes, todas de producto único (sin combinaciones) y ninguna cancelada. Los datos compilados no incluyen el texto de indicación aprobada de ninguna de ellas.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 60930 | Ketesse 25 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 66821 | Enandol 25 mg granulado para solución oral | Granulado para solución oral |
| 64888 | Ketesse 50 mg/2 ml solución inyectable y para perfusión | Solución inyectable |
| 83328 | Dexketoprofeno B. Braun 50 mg/100 ml solución para perfusión | Solución para perfusión |
| 77593 | Dexketoprofeno Combix 25 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para tendinitis solo existe la predicción del modelo y un único ECA indirecto sobre dolor musculoesquelético general, sin ensayos clínicos específicos. Con este respaldo no es posible avanzar a una evaluación de seguridad ni a una decisión de reposicionamiento.

**Para avanzar se necesita:**
- Estudios o ensayos clínicos de dexketoprofeno específicamente en tendinitis.
- Datos de advertencias y contraindicaciones del prospecto de la AEMPS, aún pendientes y necesarios para la evaluación de seguridad.
- Datos detallados del mecanismo de acción (MOA) desde DrugBank.
- Texto de la indicación aprobada en España, para establecer la relación con la indicación original.
- Considerar priorizar otra indicación predicha por el modelo: la **migraña** (puntaje TxGNN 0.9987) tiene nivel de evidencia L1, 5 ensayos clínicos (en su mayoría de Fase 4, con dexketoprofeno intravenoso en urgencias) y varios ECAs y un metanálisis. Su recomendación en los datos es "Proceed with Guardrails". Las cautelas serían que la evidencia se refiere al tratamiento del ataque agudo, que los ensayos son mayormente hospitalarios con formulación intravenosa, y que se aplican las precauciones habituales de los AINE (gastrointestinales, renales y cardiovasculares).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


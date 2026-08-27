---
layout: default
title: Clopidogrel
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 8
---

# Clopidogrel
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

# Clopidogrel: De Prevención de Eventos Trombóticos a Migraña (Trastorno Migrañoso)

> **Nota de alcance:** TxGNN generó 8 indicaciones candidatas para clopidogrel. La de mayor puntaje bruto ("migraña con aura de tronco encefálico", rank 1) no tiene ningún ensayo clínico dedicado (0 registrados). Este informe se centra en **"migraña" (trastorno migrañoso general)**, rank 2, por ser la indicación con evidencia clínica sustancialmente más sólida y una recomendación de decisión explícita ("Proceed with Guardrails") en el propio paquete de evidencia.

## Resumen en Una Frase

Clopidogrel es un antiplaquetario (antagonista del receptor P2Y12) utilizado originalmente para la prevención de eventos aterotrombóticos en síndrome coronario agudo e ictus isquémico. El modelo TxGNN predice que podría ser efectivo para **Migraña** (particularmente en pacientes con foramen oval permeable/shunt derecha-izquierda), con **8 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección, incluyendo un ensayo clínico fase 4 completado (CANOA).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Prevención de eventos aterotrombóticos (síndrome coronario agudo e ictus isquémico) — referencia contextual de la literatura incluida en el paquete de evidencia |
| Nueva Indicación Predicha | Migraña (Trastorno Migrañoso), especialmente con foramen oval permeable (FOP) |
| Puntaje de Predicción TxGNN | 99.44% |
| Nivel de Evidencia | L1 |
| Estado de Mercado (Taiwán) | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## Por qué es Razonable esta Predicción?

No hay un dato estructurado de mecanismo de acción original en la base de referencia (data gap). No obstante, la propia evidencia recopilada en este paquete describe consistentemente a clopidogrel como un **antagonista del receptor P2Y12 que inhibe la agregación plaquetaria**, usado clínicamente para prevenir eventos trombóticos en síndrome coronario agudo e ictus isquémico.

La hipótesis de reposicionamiento se apoya en un mecanismo bien documentado: en pacientes con foramen oval permeable (FOP) o comunicación interauricular (CIA), un shunt derecha-izquierda permite que microémbolos y sustancias vasoactivas (p. ej. metabolitos de serotonina) eviten el filtro pulmonar y lleguen directamente a la circulación cerebral, lo que se considera un desencadenante de migraña con aura. Al inhibir la agregación plaquetaria y reducir la microembolización, clopidogrel podría disminuir la frecuencia de crisis migrañosas en esta subpoblación específica — un mecanismo distinto de su indicación cardiovascular original, pero fisiopatológicamente coherente con ella.

Esta relación no es meramente teórica: el ensayo fase 4 CANOA (NCT00799045, n=220) probó directamente clopidogrel + aspirina vs. aspirina sola para prevenir migraña de novo tras cierre percutáneo de CIA, con publicaciones en JAMA (2015) y JAMA Cardiology (2021). Es importante notar que esta evidencia es más robusta en el subgrupo con shunt derecha-izquierda que en la población general de migraña sin esta característica anatómica.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) | Fase 4 | Completado | 220 | Estudio CANOA: clopidogrel + aspirina vs. aspirina sola para prevenir migraña de novo tras cierre transcatéter de CIA — evidencia directa más robusta del paquete |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Fase 4 | Desconocido | 50 | Evalúa directamente la eficacia profiláctica de clopidogrel en migraña con shunt derecha-izquierda; resultado no publicado |
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) | Fase 4 | Desconocido | 1000 | Estudio COMPETE: compara anticoagulación vs. antiagregación vs. terapia antimigrañosa en pacientes con FOP; gran tamaño muestral, resultado pendiente |
| [NCT04946734](https://clinicaltrials.gov/study/NCT04946734) | Fase 3 | Activo, no reclutando | 440 | Estudio SPRING: cierre de FOP vs. tratamiento médico (incluye antiagregantes) para alivio de migraña |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Fase 3 | Completado | 664 | Cierre de FOP/anticoagulantes vs. antiagregantes para prevenir recurrencia de ictus; población y mecanismo relacionados, criterio principal no es migraña |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | No aplica | Terminado | 7 | Cierre de FOP con oclusor GORE CARDIOFORM para migraña; clopidogrel no es la intervención principal, muestra muy pequeña |
| [NCT02777359](https://clinicaltrials.gov/study/NCT02777359) | Fase 2 | Desconocido | 100 | Cierre percutáneo de FOP de alto riesgo para tratar migraña; clopidogrel solo como coadyuvante postprocedimiento |
| [NCT02670161](https://clinicaltrials.gov/study/NCT02670161) | Fase 4 | Reclutando por invitación | 3300 | Registro de mejora de calidad en neurología vía historia clínica electrónica; no es ensayo de intervención directo |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26551304](https://pubmed.ncbi.nlm.nih.gov/26551304/) | 2015 | ECA | JAMA | Ensayo CANOA original: clopidogrel + aspirina reduce migraña de novo tras cierre de CIA |
| [32965476](https://pubmed.ncbi.nlm.nih.gov/32965476/) | 2021 | ECA | JAMA Cardiology | Seguimiento a 1 año del CANOA; el beneficio no se sostiene tras suspender clopidogrel a los 3 meses |
| [26908949](https://pubmed.ncbi.nlm.nih.gov/26908949/) | 2016 | ECA | European Heart Journal | Ensayo PRIMA: cierre percutáneo de FOP en migraña con aura refractaria a tratamiento médico |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | ECA | Cephalalgia | Ensayo piloto aleatorizado: clopidogrel como profilaxis de migraña |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Cohorte | Heart | Observación original: clopidogrel reduce migraña con aura tras cierre transcatéter de FOP/CIA |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Serie de Casos | J Investig Med | Clopidogrel como profilaxis complementaria eficaz en migraña refractaria con FOP |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Revisión | Headache | Revisión sistemática del papel de antitrombóticos en la prevención de migraña |
| [40144614](https://pubmed.ncbi.nlm.nih.gov/40144614/) | 2025 | Revisión | Indian J Thorac Cardiovasc Surg | Revisión sistemática de cefalea de novo tras cierre transcatéter de CIA |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Cohorte Retrospectiva | Cephalalgia | Clopidogrel como terapia primaria en migrañosos con lesiones de shunt derecha-izquierda |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Estudio Piloto | Neurology | Estudio TRACTOR: ticagrelor (tienopiridina relacionada) en migraña refractaria/FOP, tras hallazgos previos con clopidogrel |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. (No hay advertencias, contraindicaciones ni interacciones farmacológicas registradas en la base de referencia; la obtención del prospecto TFDA está identificada como brecha bloqueante — ver Próximos Pasos.)

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
- Existe un ensayo fase 4 completado (CANOA, n=220) con resultado positivo publicado en JAMA, más dos ensayos fase 4 en curso de gran tamaño (COMPETE n=1000, SPRING fase 3 n=440), lo que da un nivel de evidencia L1. Sin embargo, el beneficio parece limitado a la subpoblación con shunt derecha-izquierda (FOP/CIA) y no sostenido tras suspender el fármaco (según seguimiento a 1 año), por lo que no se recomienda avanzar sin salvaguardas.

**Para avanzar se necesita:**
- Obtener el prospecto/apartado de advertencias TFDA (DG001, brecha bloqueante) — requisito indispensable antes de la evaluación de seguridad S1
- Confirmar el mecanismo de acción detallado desde DrugBank (DG002)
- Seguir los resultados pendientes de COMPETE y SPRING (finalización estimada 2025)
- Definir el subgrupo objetivo (pacientes con FOP/shunt confirmado) en lugar de migraña general, dado que la evidencia no respalda un efecto generalizado
- Evaluar estrategia de acceso a mercado, ya que el fármaco no está actualmente comercializado bajo este registro (0 autorizaciones)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


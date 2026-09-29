---
layout: default
title: Vernakalant
parent: Solo predicción del modelo (L5)
nav_order: 557
evidence_level: L5
indication_count: 6
---

# Vernakalant
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Vernakalant: De Fibrilación Auricular de Inicio Reciente a Ictus (Trastorno Cerebrovascular)

## Resumen en Una Frase

Vernakalant es un antiarrítmico de acción selectiva auricular, utilizado para la cardioversión farmacológica de la fibrilación auricular (FA) de inicio reciente.
El modelo TxGNN predice que podría ser efectivo para **ictus (stroke disorder)**, pero los **3 ensayos clínicos** y **7 publicaciones** encontrados tratan sobre la FA y **ninguno evalúa el ictus como desenlace**. La predicción se explica probablemente por la asociación entre FA e ictus en el grafo de conocimiento, no por un efecto terapéutico demostrado.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta texto de indicación en el registro de AEMPS. Según la literatura del paquete: cardioversión de la FA de inicio reciente |
| Nueva Indicación Predicha | Ictus (stroke disorder) |
| Puntaje de Predicción TxGNN | 99,83% |
| Nivel de Evidencia | L4 (solo evidencia indirecta; sin datos directos en ictus) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de un mecanismo de acción curado en el registro de DrugBank. Según la descripción general del paquete de evidencia, vernakalant es un bloqueador mixto de canales de sodio y potasio con predominio auricular. Esto explica su uso para convertir la FA a ritmo sinusal.

La relación con el ictus es **indirecta**. La FA es un importante factor de riesgo de ictus, por lo que controlar el ritmo podría influir en ese riesgo. Sin embargo, ningún dato disponible demuestra que vernakalant prevenga o trate el ictus, ni que mejore sus desenlaces.

El puntaje TxGNN tan alto (0,998) probablemente refleja la asociación FA–ictus en el grafo de conocimiento y no un efecto terapéutico directo. Debe interpretarse con cautela.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04485195](https://clinicaltrials.gov/study/NCT04485195) | Fase 4 | Completado | 350 | RAFF4: vernakalant vs. procainamida i.v. para FA aguda en urgencias. El objetivo es la cardioversión y su seguridad, sin desenlace de ictus |
| [NCT01447862](https://clinicaltrials.gov/study/NCT01447862) | Fase 4 | Completado | 101 | Vernakalant vs. ibutilida en FA de inicio reciente. Criterio principal: conversión a ritmo sinusal |
| [NCT01646281](https://clinicaltrials.gov/study/NCT01646281) | Fase 4 | Desconocido | 70 | Vernakalant vs. flecainida sobre la contractilidad auricular tras la cardioversión. Vínculo teórico con el riesgo tromboembólico, pero no se evaluó el ictus y el estado no está verificado |

Los tres ensayos se clasificaron con relevancia baja (C) para ictus. Solo respaldan la indicación en FA.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27292602](https://pubmed.ncbi.nlm.nih.gov/27292602/) | 2016 | Cohorte | Am J Emerg Med | Seguridad y eficacia de la cardioversión farmacológica de FA de inicio reciente en urgencias, con seguimiento de tromboembolia o muerte a 30 días |
| [17371199](https://pubmed.ncbi.nlm.nih.gov/17371199/) | 2007 | Revisión | Expert Opin Investig Drugs | Propiedades del mecanismo y desarrollo de vernakalant como agente antifibrilatorio auricular selectivo |
| [22576674](https://pubmed.ncbi.nlm.nih.gov/22576674/) | 2012 | Revisión | Curr Hypertens Rep | Ensayos recientes en FA e hipertensión; menciona la FA como factor de riesgo de ictus y los antiarrítmicos nuevos (dronedarona, vernakalant) |
| [22166900](https://pubmed.ncbi.nlm.nih.gov/22166900/) | 2012 | Revisión | Lancet | Manejo de la FA: estratificación del riesgo de ictus y tromboprofilaxis con anticoagulantes orales |
| [23553811](https://pubmed.ncbi.nlm.nih.gov/23553811/) | 2013 | Revisión | Pharmacotherapy | Actualización clínica sobre el manejo de la FA |
| [19678722](https://pubmed.ncbi.nlm.nih.gov/19678722/) | 2009 | Revisión | J Manag Care Pharm | Manejo farmacológico de la FA: opciones establecidas y emergentes |
| [25024989](https://pubmed.ncbi.nlm.nih.gov/25024989/) | 2014 | Revisión | Heart Lung Vessels | Avances de 2013 en anestesia cardiotorácica; incluye la oclusión de la orejuela auricular izquierda para reducir el ictus |

Ninguna publicación demuestra un efecto de vernakalant sobre el ictus. Todas abordan el contexto de la FA.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 10645002 | BRINAVESS 20 mg/ml (Advanz Pharma Limited) | Concentrado para solución para perfusión | No consta en el registro |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas.

Como observación general del análisis del paquete (no procede del prospecto), el bloqueo de canales de sodio puede provocar bradicardia o enlentecimiento de la conducción. Este riesgo sería relevante en pacientes con disfunción del nodo sinusal.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Los estudios disponibles respaldan a vernakalant en la cardioversión de la FA, pero ninguno evalúa el ictus. La predicción se apoya sobre todo en la relación FA–ictus del grafo de conocimiento. Las otras cinco predicciones (síndrome del seno enfermo, susceptibilidad obsoleta al ictus isquémico, sarcoglicanopatía, síndrome de Wildervanck y amiloidosis ABri) son de nivel L5, sin evidencia. Además, una de ellas es un término ontológico obsoleto y otra podría ser un riesgo de seguridad en lugar de una indicación.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), pendiente y bloqueante para el cribado de seguridad.
- Obtener el mecanismo de acción desde una fuente curada (DrugBank).
- Buscar evidencia directa sobre desenlaces de ictus con vernakalant, o justificar si el objetivo real es la prevención del ictus asociado a la FA.
- Definir la indicación original con el texto aprobado en AEMPS, ausente en el registro actual.

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


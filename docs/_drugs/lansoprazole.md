---
layout: default
title: Lansoprazole
parent: Solo predicción del modelo (L5)
nav_order: 451
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
monitor_inn: "Lansoprazole"
predicted_indications: ["duodenal obstruction"]
description: "Lansoprazole: nueva indicación predicha, Duodenal obstruction (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Lansoprazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Lansoprazole: Duodenal obstruction
{: .text-alpha }

## Resumen en Una Frase

Lansoprazol es un inhibidor de la bomba de protones, utilizado originalmente para el tratamiento de la úlcera gástrica, la úlcera duodenal, la enfermedad por reflujo gastroesofágico y el síndrome de Zollinger-Ellison.
El modelo TxGNN predice que podría ser efectivo para **reflujo duodenogástrico**,
pero actualmente no hay **ningún ensayo clínico** y solo **1 publicación** general (una revisión sobre inhibidores de la bomba de protones, no específica de esta condición).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Duodenal obstruction |
| Puntaje de Predicción TxGNN | 0.9968 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 13) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Lansoprazol es un inhibidor de la bomba de protones que suprime la secreción de ácido gástrico. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción, pero esta es la función conocida de la clase y es la base de sus indicaciones aprobadas en patología ácido-péptica.

El reflujo duodenogástrico (reflujo biliar) depende sobre todo de la motilidad pilórica y duodenal y de la exposición a bilis, más que de una hipersecreción ácida. Por ello, el vínculo mecanístico es **indirecto**: suprimir el ácido podría aliviar síntomas y reducir el daño de la mucosa causado por la exposición combinada a ácido y bilis, pero no corrige el reflujo del contenido duodenal en sí.

El puntaje TxGNN muy alto (0.9968) probablemente refleja la proximidad en la red del lansoprazol a indicaciones aprobadas relacionadas con el reflujo (enfermedad por reflujo gastroesofágico, esofagitis, úlcera péptica) y no una evidencia independiente. Debe interpretarse con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Revisión | European Journal of Clinical Pharmacology | Actualización del uso clínico y la farmacocinética de los inhibidores de la bomba de protones: tratamiento de primera elección en úlcera péptica, infección por *H. pylori*, reflujo gastroesofágico, lesiones por AINE y síndrome de Zollinger-Ellison. No es específica del reflujo duodenogástrico. |

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de medicamentos monocomponente). Los textos de indicación aprobada no están disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 66127 | Lansoprazol Sandoz 15 mg cápsulas gastrorresistentes EFG | Cápsula dura gastrorresistente | No disponible |
| 77739 | Lansoprazol Flas Salvat 30 mg comprimidos bucodispersables | Comprimido bucodispersable | No disponible |
| 36286-00-00IP | Opiren 30 mg cápsulas | Cápsula dura gastrorresistente | No disponible |
| 61219 | Pro Ulco 30 mg cápsulas gastrorresistentes | Cápsula dura | No disponible |
| 62316 | Estomil 15 mg cápsulas duras gastrorresistentes EFG | Cápsula dura | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento** (no proceden del prospecto, deben verificarse): hipertensión, síndrome de QT largo, torsades de pointes, insuficiencia hepática, porfirias, enfermedad renal, enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, osteoporosis, trastornos de coagulación, ictus e infarto de miocardio, anemias, colitis por *Clostridium difficile*, miastenia gravis, entre otras.
- **Interacciones farmacológicas**: se registraron 100 interacciones. Entre las incluidas en la muestra revisada, las de nivel **mayor** son con **acalabrutinib** y **atazanavir**. Entre las de nivel moderado figuran hidroclorotiazida, anfotericina B, amikacina, anfetamina, ampicilina, fenofibrato, apalutamida, aprepitant, atorvastatina, bosutinib, brigatinib y bromocriptina. Entre las de nivel menor figuran ácido acetilsalicílico, axitinib, brivaracetam y cianocobalamina.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones oficiales).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo y en una revisión general sin relación específica con la condición. No hay ensayos clínicos, y el vínculo mecanístico es indirecto porque el reflujo duodenogástrico no se debe principalmente a hipersecreción ácida.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), pues es un requisito previo para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda bibliográfica específica de inhibidores de la bomba de protones en reflujo duodenogástrico o biliar.
- Valorar la relevancia clínica real frente a alternativas terapéuticas existentes.
- Evaluar el riesgo de interacciones (acalabrutinib, atazanavir) y de las comorbilidades señaladas.

*Nota: la segunda predicción del modelo, obstrucción duodenal (puntaje 0.9968, nivel L5), no tiene vínculo mecanístico claro, ni ensayos ni literatura; la obstrucción es de naturaleza mecánica y su tratamiento es endoscópico o quirúrgico. No se recomienda priorizarla (Hold).*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


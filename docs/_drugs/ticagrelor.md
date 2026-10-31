---
layout: default
title: Ticagrelor
parent: Solo predicción del modelo (L5)
nav_order: 793
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-31
monitor_inn: "TICAGRELOR"
predicted_indications: ["intracranial arteriosclerosis", "Monckeberg arteriosclerosis", "priapism", "ischemic disease", "May-Thurner syndrome", "livedo reticularis", "vascular ectasia", "angiodysplasia", "venous thromboembolism"]
description: "Ticagrelor: nueva indicación predicha, Arteriosclerosis intracraneal (intracranial arteriosclerosis) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Ticagrelor
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Ticagrelor: Arteriosclerosis intracraneal (intracranial arteriosclerosis)
{: .text-alpha }

## Resumen en Una Frase

Ticagrelor es un antiagregante plaquetario inhibidor del receptor P2Y12, utilizado originalmente en el síndrome coronario agudo y en la enfermedad arterial periférica.
El modelo TxGNN predice que podría ser efectivo para **arteriosclerosis intracraneal**,
con **2 ensayos clínicos** y **2 publicaciones** que actualmente respaldan esta dirección, de los cuales solo uno es un ensayo de Fase 3 que sigue en curso.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Arteriosclerosis intracraneal (intracranial arteriosclerosis) |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 según la clasificación asignada en los datos compilados; a mi juicio, con las reglas de nivel, estaría más cerca de L3 (ver nota abajo) |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 12) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Proceed with Guardrails |

> **Nota sobre el nivel de evidencia:** los datos compilados asignan L1, pero para esta indicación concreta no hay ningún ECA de Fase 3 completado (el único ensayo de Fase 3, CAPTIVA, sigue activo). Los respaldos publicados son un estudio de cohorte y un artículo de diseño de ensayo. El nivel L1 debe interpretarse con cautela.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, ticagrelor es un inhibidor reversible del receptor plaquetario P2Y12, lo que reduce la agregación plaquetaria y la formación de trombos sobre placas ateroscleróticas.

Su eficacia en el síndrome coronario agudo y en la enfermedad arterial periférica es la base de sus indicaciones originales. La arteriosclerosis intracraneal comparte el mismo sustrato fisiopatológico (placa aterosclerótica con riesgo de trombosis), por lo que el mecanismo antitrombótico es mecanísticamente aplicable.

Un apoyo adicional es el ensayo CHANCE-2 (PMID 34708996), que respalda ticagrelor frente a clopidogrel en portadores de pérdida de función de CYP2C19 con ictus o AIT. El principal riesgo a vigilar es la hemorragia intracraneal.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) (CAPTIVA) | Fase 3 | Activo, sin reclutamiento | 1683 | Compara rivaroxabán, ticagrelor o ambos frente a clopidogrel para reducir a 1 año el ictus isquémico, la hemorragia intracerebral o la muerte vascular. Aún sin resultados; el papel exacto de ticagrelor en el brazo antiagregante no está confirmado solo por el título. |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | N/A | Reclutando | 100 | Piloto de selección de inhibidor P2Y12 guiada por genotipo frente a clopidogrel convencional en enfermedad aterosclerótica intracraneal sintomática. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Cohorte | J Neurointerv Surg | Experiencia con ticagrelor 60 mg dos veces al día más aspirina 81 mg frente al régimen estándar de aspirina y clopidogrel en el stenting intracraneal. |
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | Diseño de ensayo | Int J Stroke | Diseño y avance temprano del ensayo CAPTIVA; el tratamiento habitual (clopidogrel + aspirina 90 días) mantiene un riesgo elevado de ictus recurrente a 12 meses. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 110655009 | BRILIQUE 60 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 89560 | TIKATA 60 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos compilados |
| 90621 | Ticagrelor Aurovitas 60 mg EFG | Comprimido recubierto con película | No disponible en los datos compilados |
| 89354 | Ticagrelor Normon 90 mg EFG | Comprimido recubierto con película | No disponible en los datos compilados |
| 86152 | Ticagrelor Stada 90 mg EFG | Comprimido recubierto con película | No disponible en los datos compilados |

Hay 20 autorizaciones vigentes, todas de monofármaco (60 mg y 90 mg, en su mayoría genéricos EFG); se muestran las 5 principales.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar y hemorragia intracraneal.
- **Interacciones farmacológicas:** se identificaron 100 interacciones. Entre las principales:
  - **Mayor:** claritromicina.
  - **Moderadas:** ácido acetilsalicílico, morfina, simvastatina, dexametasona, budesonida, aprepitant, miconazol, clotrimazol, saxagliptina, cisaprida, rolapitant, entre otras.
  - **Menores:** naloxegol, prucaloprida.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones oficiales).

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo antitrombótico es plausible y existe un ensayo de Fase 3 de gran tamaño (CAPTIVA) que evalúa directamente ticagrelor en esta población, pero todavía no hay resultados. La hemorragia intracraneal es un riesgo relevante y figura como contraindicación en el grafo de conocimiento.

**Para avanzar se necesita:**
- Resultados de CAPTIVA (finalización prevista en enero de 2027) y confirmación del papel de ticagrelor en sus brazos.
- Datos del mecanismo de acción y de las advertencias y contraindicaciones del prospecto de la AEMPS.
- Estratificación del riesgo hemorrágico, duración adecuada de la doble antiagregación y consideración del genotipo CYP2C19.
- Plan de manejo de las interacciones relevantes (inhibidores potentes de CYP3A4 como claritromicina, y otros antitrombóticos).

---

**Otras indicaciones predichas (contexto):** *enfermedad isquémica* (L1, abundante evidencia, aunque en gran parte se solapa con la indicación ya aprobada de síndrome coronario agudo, por lo que es más una extensión que un reposicionamiento verdadero; Proceed with Guardrails); *ectasia vascular* y *tromboembolismo venoso* (L4, pregunta de investigación); *arteriosclerosis de Mönckeberg*, *priapismo*, *síndrome de May-Thurner*, *livedo reticularis*, *oclusión vascular mesentérica* y *angiodisplasia* (L5, Hold; en angiodisplasia además existe preocupación de seguridad por el riesgo de sangrado).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


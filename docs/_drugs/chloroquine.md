---
layout: default
title: Chloroquine
parent: Solo predicción del modelo (L5)
nav_order: 173
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "Chloroquine"
predicted_indications: ["rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid nodulosis", "juvenile chronic polyarthritis", "juvenile idiopathic arthritis"]
description: "Chloroquine: nueva indicación predicha, Artritis idiopática juvenil poliarticular con factor reumatoide positivo (rheumatoid factor-positive polyarticular juve… (nivel de evidencia L5). Indicación or…"
---

# Chloroquine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Chloroquine: Artritis idiopática juvenil poliarticular con factor reumatoide positivo (rheumatoid factor-positive polyarticular juvenile idiopathic arthritis)
{: .text-alpha }

## Resumen en Una Frase

La cloroquina es un antipalúdico con actividad inmunomoduladora, utilizado originalmente para el tratamiento de la malaria, la artritis reumatoide y el lupus eritematoso.
El modelo TxGNN predice que podría ser efectiva para la **artritis idiopática juvenil poliarticular con factor reumatoide positivo**,
pero actualmente **no hay ensayos clínicos** y solo **1 publicación** recuperada (un estudio de cohorte sobre leflunomida, que no evalúa la cloroquina), por lo que la evidencia directa es prácticamente nula.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Artritis idiopática juvenil poliarticular con factor reumatoide positivo (rheumatoid factor-positive polyarticular juvenile idiopathic arthritis) |
| Puntaje de Predicción TxGNN | 0.9941 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Chloroquine (traducción no oficial): «La cloroquina, una 4-aminoquinolina, es un agente antiprotozoario. Se desconoce el mecanismo preciso por el cual la cloroquina ejerce su actividad. La cloroquina puede ejercer su efecto contra las especies de Plasmodium concentrándose en las vesículas ácidas del parásito e inhibiendo la polimerización del hemo.» Texto original en inglés: "Chloroquine, a 4-aminoquinoline, is an anti-protozoal agent. The precise mechanism by which chloroquine exhibits activity is not known. Chloroquine, may exert its effect against Plasmodium species by concentrating in the acid vesicles of the parasite and by inhibiting polymerization of heme." ([DailyMed: chloroquine phosphate prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=06c69e2b-211b-4746-9f3a-f86d36520570), versión del 2026-10-21; consultado el 2026-11-19). Según la información conocida, la cloroquina es un antipalúdico con efectos inmunomoduladores: eleva el pH lisosomal, inhibe el procesamiento de antígenos y la presentación mediante MHC de clase II, y reduce la señalización de los receptores tipo Toll y la producción de citocinas proinflamatorias.

La cloroquina ya se utiliza en la artritis reumatoide del adulto. La artritis idiopática juvenil poliarticular con factor reumatoide positivo comparte rasgos de sinovitis autoinmune con esta enfermedad, por lo que la extensión es biológicamente plausible. El puntaje elevado de TxGNN probablemente refleja esta cercanía con la indicación ya establecida.

Debe subrayarse que no se aportó evidencia directa del uso de cloroquina en este subtipo. La plausibilidad es mecanística, no clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24334641](https://pubmed.ncbi.nlm.nih.gov/24334641/) | 2014 | Cohorte | The Journal of Rheumatology | Experiencia prospectiva a largo plazo en práctica real con leflunomida en artritis idiopática juvenil; no evalúa la cloroquina |

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 15797 | RESOCHIN 155 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | COMPRIMIDO RECUBIERTO | Kern Pharma S.L. | Comercializada |

Se muestra la única autorización con este principio activo en los datos de CIMA (AEMPS).

<!-- licenses:end -->

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del texto del prospecto): epilepsia, porfiria (incluida la hereditaria), enfermedad hepática, enfermedad de la vesícula biliar, enfermedades oculares y de la retina (retinitis, escotoma, trastornos visuales, ceguera), trastornos auditivos, psoriasis y parapsoriasis, neutropenia, agranulocitosis, leucopenia, anemia (incluida la macrocítica), deficiencia de G6PD, enfermedad por depósito de glucógeno, cistinuria, galactosemia y abuso o dependencia de sustancias.
- **Interacciones farmacológicas**: la consulta no identificó interacciones fármaco-fármaco clínicas. Solo figuran dos interacciones farmacológicas con dianas (MRGPRX1 y TAS2R3), sin relevancia clínica establecida.
- **Señales de seguridad en la literatura relacionada**: se ha descrito un bloqueo auriculoventricular de tercer grado durante el tratamiento con cloroquina en una paciente con artritis crónica juvenil (informe de caso). Dado el perfil retiniano y cardíaco, se requiere especial cautela en población pediátrica.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje de TxGNN es alto y el mecanismo es plausible por su cercanía con la artritis reumatoide, no existen ensayos clínicos ni evidencia directa de cloroquina en este subtipo; la única publicación recuperada trata de otro fármaco. Además, los riesgos retiniano y cardíaco son preocupantes en niños.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias y contraindicaciones) antes de cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción del fármaco.
- Realizar una revisión dirigida de la evidencia con hidroxicloroquina (el antipalúdico más usado en reumatología) en artritis idiopática juvenil, para decidir si merece la pena plantear la pregunta con cloroquina.
- Buscar evidencia clínica directa (estudios observacionales o ensayos) de cloroquina en artritis idiopática juvenil poliarticular con factor reumatoide positivo.
- Definir un plan de monitorización oftalmológica y cardíaca para uso pediátrico.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: chloroquine phosphate prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=06c69e2b-211b-4746-9f3a-f86d36520570) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


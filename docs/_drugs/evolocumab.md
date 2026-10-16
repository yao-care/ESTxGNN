---
layout: default
title: Evolocumab
parent: Solo predicción del modelo (L5)
nav_order: 322
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Evolocumab: nueva indicación predicha, Forma sintomática de hemofilia en mujeres portadoras (nivel de evidencia L5). Indicación original: Hipercolesterolemia familiar homocigota"
monitor_inn: "EVOLOCUMAB"
predicted_indications: ["symptomatic form of hemophilia in female carriers", "familial apolipoprotein C-II deficiency", "thrombocytopenic purpura", "factor XI deficiency", "hemophilia A with vascular abnormality", "disease of catalytic activity"]
---

# Evolocumab
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

# Evolocumab: De Hipercolesterolemia Familiar Homocigota a Hemofilia Sintomática en Portadoras

## Resumen en Una Frase

Evolocumab es un anticuerpo monoclonal que inhibe PCSK9, utilizado originalmente para el tratamiento de la hipercolesterolemia familiar homocigota y la dislipidemia sindrómica.
El modelo TxGNN predice que podría ser efectivo para la **forma sintomática de hemofilia en mujeres portadoras**, pero actualmente no hay **ningún ensayo clínico ni publicación** que respalde esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipercolesterolemia familiar homocigota; dislipidemia sindrómica |
| Nueva Indicación Predicha | Forma sintomática de hemofilia en mujeres portadoras |
| Puntaje de Predicción TxGNN | 99,82% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Evolocumab es un anticuerpo monoclonal dirigido contra PCSK9 (proproteína convertasa subtilisina/kexina tipo 9). Al bloquear esta proteína, aumenta la disponibilidad de receptores de LDL en el hígado y reduce el colesterol LDL. Los datos compilados no incluyen una descripción detallada del mecanismo de acción, pero la diana (PCSK9) está bien identificada.

Con la información disponible, **no se identifica un vínculo mecanístico plausible** entre esta vía y la nueva indicación. La hemofilia en mujeres portadoras se debe a una actividad reducida del factor VIII o IX (herencia ligada al cromosoma X), algo ajeno a la vía PCSK9/receptor de LDL. El puntaje elevado de TxGNN (0,998) es solo una predicción del grafo de conocimiento y no está respaldado por una justificación biológica ni por datos clínicos.

Por tanto, esta predicción debe considerarse especulativa. Otras predicciones del modelo (deficiencia familiar de apolipoproteína C-II, púrpura trombocitopénica, deficiencia de factor XI, hemofilia A con anomalía vascular y "enfermedad de actividad catalítica") tampoco cuentan con ensayos ni literatura. Solo la deficiencia de apoC-II guarda una relación conceptual indirecta, por ser un trastorno lipídico, aunque evolocumab no corregiría su defecto principal (la activación de la lipoproteína lipasa). "Enfermedad de actividad catalítica" es una categoría demasiado amplia para ser accionable.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1151016003 | REPATHA 140 MG solución inyectable en pluma precargada | Solución inyectable en pluma precargada | No disponible en los datos compilados |
| 1151016003IP | REPATHA 140 MG solución inyectable en pluma precargada | Solución inyectable en pluma precargada | No disponible en los datos compilados |
| 1151016002 | REPATHA 140 MG solución inyectable en pluma precargada | Solución inyectable en pluma precargada | No disponible en los datos compilados |

Titular: Amgen Europe B.V. Las tres autorizaciones están vigentes.

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: la consulta se completó y devolvió un único registro, que corresponde a la interacción farmacológica con la diana (PCSK9), no a una interacción con otro medicamento. No se identificaron interacciones con otros fármacos.

Para advertencias y contraindicaciones, consultar el prospecto. Además, el uso de un anticuerpo hipolipemiante en trastornos hemorrágicos plantearía cuestiones de seguridad sin resolver.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos, literatura ni un vínculo mecanístico plausible entre la inhibición de PCSK9 y la hemofilia en portadoras. Un puntaje alto en TxGNN no compensa esta falta de respaldo.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción y un análisis que justifique un vínculo biológico con la coagulación.
- Revisión del prospecto de la AEMPS (advertencias y contraindicaciones), pendiente y necesaria antes de cualquier cribado de seguridad.
- Estudios preclínicos o de mecanismo que apoyen la hipótesis.
- Valorar priorizar otras candidatas con mayor plausibilidad biológica, como la deficiencia de apoC-II, con una evaluación realista de su beneficio.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


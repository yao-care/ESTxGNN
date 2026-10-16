---
layout: default
title: Niflumic Acid
parent: Solo predicción del modelo (L5)
nav_order: 564
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Niflumic Acid: nueva indicación predicha, Enfermedad de Raynaud (nivel de evidencia L5). Indicación original: No disponible en la autorización de AEMPS (referencia externa: artrit…"
---

# Niflumic Acid
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Ácido niflúmico: De Indicación Original No Especificada a Enfermedad de Raynaud

## Resumen en Una Frase

El ácido niflúmico es un antiinflamatorio no esteroideo (AINE) comercializado en España en cápsulas de 250 mg (NIFLACTOL), cuya ficha disponible no recoge el texto de la indicación aprobada. En otras fuentes se describe su uso en artritis reumatoide.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad de Raynaud**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; la evidencia es solo la predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la autorización de AEMPS (referencia externa: artritis reumatoide) |
| Nueva Indicación Predicha | Enfermedad de Raynaud |
| Puntaje de Predicción TxGNN | 99.77% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información conocida, el ácido niflúmico es un AINE que inhibe la ciclooxigenasa (COX) y reduce la síntesis de prostaglandinas. Además, los datos farmacológicos compilados indican que interactúa con varios canales iónicos: canales de cloruro activados por calcio (CaCC/ANO1), canales ClC-1, ClC-Ka y ClC-Kb, canales de potasio (KNa1.2 y Kv7.1) y canales TRP (TRPA1 y TRPC4). Cabe señalar que algunos de estos datos proceden de estudios en rata o ratón, y que la fuente indica que no se encontraron datos de afinidad en dianas humanas que confirmen su mecanismo principal.

La enfermedad de Raynaud se caracteriza por vasoespasmo en los vasos periféricos. Dado que el ácido niflúmico podría modular el tono del músculo liso vascular mediante el bloqueo de canales de cloruro y la inhibición de COX, existe una hipótesis mecanística plausible. Sin embargo, este vínculo es especulativo y no cuenta con respaldo clínico.

El puntaje elevado de TxGNN (99.77%) es una predicción computacional y no sustituye a la evidencia experimental o clínica. La similitud con la indicación original no ha podido evaluarse por falta de datos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 49818 | NIFLACTOL 250 mg CÁPSULAS | Cápsula dura | No especificada en los datos disponibles |

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas y dianas**: los datos compilados no recogen interacciones con otros medicamentos, sino interacciones farmacológicas con dianas moleculares (8 registros): KNa1.2 (KCNT2), TRPA1, TRPC4, Kv7.1 (KCNQ1), ClC-1, ClC-Ka, ClC-Kb y CaCC (ANO1). No se dispone de datos de afinidad en dianas humanas.
- **Riesgo de clase (AINE)**: los AINE conllevan en general riesgo renal (menor perfusión renal dependiente de prostaglandinas, nefrotoxicidad e hiperpotasemia), además de riesgos gastrointestinales y cardiovasculares. Esta información es de clase y no procede de la ficha técnica de este producto.

Consultar el prospecto para obtener información detallada de advertencias y contraindicaciones.

---

## Otras Indicaciones Predichas (Referencia)

Todas con nivel de evidencia L5, sin ensayos ni literatura, y recomendación Hold:

| Rank | Indicación Predicha | Puntaje TxGNN | Comentario |
|------|------|------|------|
| 2 | Angina de Prinzmetal | 99.55% | Vasoespasmo coronario; hipótesis sin respaldo clínico |
| 3 | Trastorno de cefalea | 99.39% | Plausible por efecto analgésico de clase AINE; categoría amplia |
| 4 | Cefalalgia autonómica trigeminal | 99.29% | Vínculo indirecto; respuestas terapéuticas específicas (p. ej., indometacina) |
| 5 | Enfermedad de vasos pequeños cerebrales tipo 1 (con o sin anomalías oculares) | 99.26% | Trastorno monogénico raro (COL4A1); sin vínculo mecanístico claro |
| 6 | Síndrome autosómico dominante de hematuria familiar, tortuosidad arteriolar retiniana y contracturas | 99.25% | Vasculopatía genética rara (COL4A1); sin base mecanística |
| 7 | Nefropatía diabética | 99.13% | Riesgo renal de los AINE; beneficio improbable |
| 8 | Trastorno de migraña | 99.04% | La más plausible por el uso de AINE en migraña aguda, aunque sin datos específicos del fármaco |

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para la enfermedad de Raynaud se basa únicamente en el modelo TxGNN (nivel L5), sin ensayos clínicos ni literatura, sin datos de mecanismo de acción confirmados y sin información de seguridad de la ficha técnica. No es posible avanzar hasta completar estas lagunas.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicación aprobada), lo que es imprescindible antes de cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda bibliográfica específica del ácido niflúmico en enfermedad de Raynaud y vasoespasmo, así como en migraña y cefalea (la indicación mecanísticamente más plausible según el análisis).
- Revisar los registros de ensayos clínicos para detectar estudios relacionados.
- Evaluar el perfil de riesgo renal, cardiovascular y gastrointestinal propio de los AINE en las poblaciones objetivo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


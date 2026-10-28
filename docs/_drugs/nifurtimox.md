---
layout: default
title: Nifurtimox
parent: Solo predicción del modelo (L5)
nav_order: 565
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Nifurtimox: nueva indicación predicha, Analbuminemia congénita (nivel de evidencia L5). Indicación original: Enfermedad de Chagas"
monitor_inn: "NIFURTIMOX"
predicted_indications: ["congenital analbuminemia", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "blood group incompatibility", "monoclonal gammopathy", "premalignant hematological system disease", "hematological disease associated with an acquired peripheral neuropathy"]
---

# Nifurtimox
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Nifurtimox: De Enfermedad de Chagas a Analbuminemia Congénita
{: .text-alpha }

## Resumen en Una Frase

Nifurtimox es un antiprotozoario utilizado originalmente para el tratamiento de la enfermedad de Chagas.
El modelo TxGNN predice que podría ser efectivo para **analbuminemia congénita**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Chagas |
| Nueva Indicación Predicha | Analbuminemia congénita |
| Puntaje de Predicción TxGNN | 0.9958 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 2 de 2) |
| Número de Autorizaciones | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, nifurtimox es un antiprotozoario de la clase de los nitrofuranos y su eficacia en la enfermedad de Chagas es la indicación original conocida. Su actividad se atribuye generalmente a la nitrorreducción y al estrés oxidativo en los tripanosomas, aunque este punto no figura en los datos compilados para este informe.

La analbuminemia congénita es un trastorno genético raro de la síntesis de albúmina. No se identifica una relación farmacológica plausible entre la acción antiprotozoaria de nifurtimox y esta enfermedad, ni una similitud con la indicación original.

El puntaje alto del modelo (0.9958) es una predicción computacional que no está corroborada por ensayos clínicos ni por literatura. Debe interpretarse con cautela, ya que el puntaje proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Otras indicaciones predichas, todas con nivel L5 y sin evidencia clínica ni bibliográfica: hiperviscosidad policlonal (99.47%), hiperamilasemia (99.47%), incompatibilidad de grupo sanguíneo (99.24%), gammapatía monoclonal (99.16%), enfermedad hematológica premaligna (99.11%) y enfermedad hematológica asociada a neuropatía periférica adquirida (99.06%). En este último caso, la neuropatía periférica es un efecto adverso conocido de nifurtimox, lo que va en contra de un papel terapéutico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 89506 | LAMPIT 120 MG COMPRIMIDOS | Comprimido | No especificada en los datos compilados |
| 89507 | LAMPIT 30 MG COMPRIMIDOS | Comprimido | No especificada en los datos compilados |

Ambas autorizaciones están vigentes y pertenecen a Bayer Hispania S.L.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (5 registradas):
  - **Etanol**: gravedad mayor.
  - **Ritonavir**: gravedad moderada.
  - **Tipranavir**: gravedad moderada.
  - **Bifidobacterium longum infantis**: gravedad moderada.
  - **Lactobacillus acidophilus**: gravedad moderada.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni literatura (nivel L5), no existe una conexión mecanística plausible entre nifurtimox y la analbuminemia congénita, y faltan los datos de seguridad del prospecto necesarios para continuar la evaluación.

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones del prospecto de la AEMPS (descargar y analizar el PDF).
- Completar los datos del mecanismo de acción (consultar la API de DrugBank).
- Realizar una revisión de literatura preclínica para determinar si existe alguna base biológica que relacione nifurtimox con la síntesis de albúmina.
- Reevaluar la prioridad de esta indicación frente a otras candidatas, dado que ninguna de las siete predicciones cuenta con evidencia de apoyo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


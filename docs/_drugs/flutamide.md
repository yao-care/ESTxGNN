---
layout: default
title: Flutamide
parent: Solo predicción del modelo (L5)
nav_order: 351
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
monitor_inn: "Flutamide"
predicted_indications: ["fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "prostate leiomyoma", "benign prostate phyllodes tumor", "HIV infectious disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection"]
description: "Flutamide: nueva indicación predicha, Fibroma of prostate (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Flutamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Flutamide: Fibroma of prostate
{: .text-alpha }

## Resumen en Una Frase

La flutamida es un antiandrógeno no esteroideo, utilizado originalmente para el tratamiento del cáncer de próstata.
El modelo TxGNN predice que podría ser efectiva para **susceptibilidad al cáncer de próstata/cáncer cerebral**,
pero **no hay ensayos clínicos ni publicaciones** que respalden específicamente esta predicción, por lo que se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Fibroma of prostate |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 3) |
| Número de Autorizaciones | 3 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información farmacológica compilada, la flutamida actúa como antagonista del receptor de andrógenos (AR). Su metabolito activo, la hidroxiflutamida, bloquea la señalización androgénica en los tejidos dependientes de andrógenos. Su eficacia en el cáncer de próstata, solo o combinada con un agonista de LHRH, está bien establecida.

La nueva indicación predicha combina dos componentes. El primero es un fenotipo de susceptibilidad al cáncer de próstata, estrechamente relacionado con la indicación original, y por tanto el bloqueo del AR resulta mecanísticamente plausible. El segundo es la susceptibilidad al cáncer cerebral, para la cual **no se ha identificado ningún vínculo mecanístico** con el bloqueo del AR.

El puntaje del modelo es muy alto, pero no se aportaron ensayos ni literatura que lo sustenten. Debe interpretarse como una señal exploratoria y no como evidencia de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación predicha.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación predicha.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59594 | GRISETIN 250 mg comprimidos recubiertos con película (Faes Farma S.A.) | Comprimido recubierto con película | No especificada en los datos disponibles |
| 59593 | PROSTACUR comprimidos (Mylan Pharmaceuticals S.L.) | Comprimido | No especificada en los datos disponibles |
| 62912 | FLUTAMIDA CINFA 250 mg comprimidos EFG (Laboratorios Cinfa S.A.) | Comprimido | No especificada en los datos disponibles |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia hormonal (antiandrógeno no esteroideo); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Función hepática (la hepatotoxicidad es el riesgo principal, con advertencia en recuadro); se recomienda además consultar en el prospecto otros parámetros hematológicos |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Advertencias Principales**: la evaluación del perfil beneficio-riesgo señala la hepatotoxicidad (advertencia en recuadro) como la preocupación principal. Esto limita el beneficio en contextos no oncológicos o benignos.
- **Contraindicaciones (según el grafo de conocimiento, no el texto del prospecto)**: insuficiencia hepática, enfermedad hepática, enfermedad de la vesícula biliar, metahemoglobinemia (incluida la causada por déficit de metahemoglobina reductasa), sulfohemoglobinemia, hiperbilirrubinemia (incluida la hereditaria), síndrome de Gilbert, déficit de G6PD, enfermedad por depósito de glucógeno, cistinuria, galactosemia y déficit de piruvato deshidrogenasa E3.
- **Interacciones Farmacológicas**: la consulta se completó, pero solo devolvió la diana farmacológica (receptor de andrógenos, AR). No se identificaron interacciones con otros fármacos.

Para la información de seguridad oficial, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en TxGNN, pero se encuentra en nivel L5: no hay ensayos ni literatura específicos, y el componente de cáncer cerebral carece de vínculo mecanístico conocido. La flutamida además conlleva un riesgo hepático relevante.

**Para avanzar se necesita:**
- Aclarar la definición y la relevancia clínica del fenotipo "susceptibilidad al cáncer de próstata/cáncer cerebral" y justificar o separar el componente de cáncer cerebral.
- Obtener el prospecto oficial de la AEMPS (advertencias, contraindicaciones y textos de indicación aprobada).
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión sistemática de la literatura y del registro de ensayos para esta indicación.
- Valorar, de forma separada, otras predicciones del modelo con más respaldo. Por ejemplo, "neoplasia benigna del sistema reproductor" (nivel L3, con estudios clínicos pequeños y antiguos en hiperplasia prostática benigna) y la categoría de "cáncer de órgano reproductor masculino" (que corresponde a la indicación original, no a un reposicionamiento real).
- Definir un plan de monitoreo hepático si se avanzara en cualquier indicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


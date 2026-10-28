---
layout: default
title: Tenecteplase
parent: Solo predicción del modelo (L5)
nav_order: 774
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
monitor_inn: "tenecteplase"
predicted_indications: ["congenital coronary artery anomaly", "coronary stenosis", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyropoikilocytosis, hereditary", "pyruvate kinase deficiency of red cells"]
description: "Tenecteplase: nueva indicación predicha, Congenital coronary artery anomaly (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Tenecteplase
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

## Tenecteplase: Congenital coronary artery anomaly
{: .text-alpha }

## Resumen en Una Frase

Tenecteplasa es un activador del plasminógeno tisular específico de la fibrina, originalmente utilizado para el tratamiento del infarto de miocardio y la trombosis coronaria.
El modelo TxGNN predice que podría ser efectivo para **infarto de miocardio posteroinferior**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden específicamente esta indicación; el apoyo es solo indirecto, por tratarse de un subtipo anatómico de la indicación ya conocida.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Congenital coronary artery anomaly |
| Puntaje de Predicción TxGNN | 0.9961 |
| Nivel de Evidencia | L5 (solo predicción del modelo, sin estudios específicos; la plataforma lo clasifica como L4 por inferencia desde la indicación madre) |
| Estado de Mercado en España | Comercializado (registros vigentes: 3 de 3) |
| Número de Autorizaciones | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la tenecteplasa es un activador del plasminógeno tisular específico de la fibrina que lisa los trombos coronarios oclusivos, y su eficacia en el infarto de miocardio es conocida.

El infarto posteroinferior es un subtipo anatómico del infarto de miocardio, causado igualmente por oclusión trombótica coronaria. Mecanísticamente, la trombólisis es aplicable, y esta indicación estaría prácticamente cubierta por la indicación general de infarto.

No se recuperaron ensayos ni literatura para este subtipo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 00169006 | METALYSE 10.000 UNIDADES (50 MG) | Polvo y disolvente para solución inyectable | No disponible en los datos |
| 1000169007 | METALYSE 5.000 UNIDADES (25 MG) | Polvo para solución inyectable | No disponible en los datos |
| 00169005 | METALYSE 8.000 UNIDADES (40 MG) | Polvo y disolvente para solución inyectable | No disponible en los datos |

Las tres autorizaciones están vigentes, son de monofármaco y pertenecen a Boehringer Ingelheim International GmbH.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 137 interacciones en total. Entre las mostradas:
  - **Mayores**: apixabán, betrixabán, abciximab, acalabrutinib, avapritinib, deferasirox, ibritumomab tiuxetán, tositumomab (incluido I-131). Todas implican principalmente un riesgo aumentado de hemorragia.
  - **Moderadas**: ácido acetilsalicílico, ibuprofeno, ketorolaco, celecoxib, diclofenaco tópico, ácido aminocaproico, ácidos grasos omega-3, fenfluramina, dexfenfluramina y sibutramina.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe evidencia específica (ensayos o literatura) para el infarto posteroinferior; el puntaje alto proviene de la proximidad con la indicación ya conocida de infarto de miocardio. Además, al ser un subtipo de una indicación existente, no constituye un reposicionamiento genuino y es más una pregunta de investigación que una oportunidad de desarrollo.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicaciones autorizadas), cuya ausencia bloquea el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar si la indicación autorizada de infarto agudo de miocardio ya cubre los subtipos anatómicos, lo que haría innecesario un nuevo desarrollo.
- Buscar estudios o subanálisis de ensayos de infarto con elevación del ST que describan la localización posteroinferior.
- Priorizar, si se desea explorar otras predicciones, la de estenosis coronaria (evidencia nivel L3, con estudios de tenecteplasa intracoronaria durante ICP primaria), y descartar las predicciones sin plausibilidad mecanística (anomalía coronaria congénita, deleción cromosómica, anemias hemolíticas hereditarias y talasemia).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


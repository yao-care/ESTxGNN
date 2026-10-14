---
layout: default
title: Fenfluramine
parent: Solo predicción del modelo (L5)
nav_order: 329
evidence_level: L5
indication_count: 4
---

# Fenfluramine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Fenfluramina: De Obesidad a Síndrome de Microdeleción Proximal 16p11.2

## Resumen en Una Frase

Fenfluramina es un fármaco serotoninérgico que se utilizó originalmente como supresor del apetito para el tratamiento de la obesidad (incluida la obesidad monogénica) y que hoy se comercializa en España para otro uso.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de microdeleción proximal 16p11.2**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Obesidad (trastorno de obesidad y obesidad monogénica, según el grafo de conocimiento; el texto de indicación autorizado en España no está disponible) |
| Nueva Indicación Predicha | Síndrome de microdeleción proximal 16p11.2 |
| Puntaje de Predicción TxGNN | 99,93% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la fenfluramina actúa sobre la vía serotoninérgica (liberación de serotonina y actividad sobre receptores 5-HT). Las fuentes farmacológicas consultadas vinculan el fármaco con las enzimas triptófano hidroxilasa 1 y 2 (TPH1 y TPH2), aunque no se encontraron datos públicos de bioactividad que confirmen un diana molecular principal.

La deleción 16p11.2 se asocia con obesidad, trastornos del neurodesarrollo y epilepsia. Esto crea un vínculo plausible: el fármaco se usó contra la obesidad y hoy se emplea como antiepiléptico en síndromes como el de Dravet (aprobado por la FDA en 2020 para pacientes de 2 años o más) y el de Lennox-Gastaut (recomendado por NICE en el Reino Unido en febrero 2025). Por tanto, podría ser relevante tanto para el fenotipo de obesidad como para el de crisis epilépticas.

Sin embargo, este razonamiento es una inferencia externa a los datos aportados y no está respaldado por evidencia directa en este síndrome. El puntaje del modelo es muy alto, pero no sustituye a estudios reales.

Otras predicciones del modelo (hipervitaminosis, hipertelorismo obsoleto y frontorrinia) presentan puntajes similares (≈99,8–99,9%), pero no se identificó un vínculo mecanístico plausible y probablemente son artefactos del grafo de conocimiento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1201491001 | FINTEPLA 2,2 mg/ml solución oral (Ucb Pharma) | Solución oral | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proviene del prospecto): hipertensión, hipertensión pulmonar, abuso/dependencia de sustancias, diabetes mellitus tipo 1 y tipo 2, cetoacidosis diabética y glaucoma.
- **Interacciones / farmacología**: se identificaron dos relaciones con dianas serotoninérgicas (triptófano hidroxilasa 1 y 2); no se dispone de niveles de gravedad de interacción.

Consultar el prospecto para el resto de la información de seguridad, ya que no se dispone de advertencias ni contraindicaciones oficiales de la AEMPS.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero carece de ensayos clínicos y literatura (nivel L5), y el vínculo mecanístico es solo inferido. Además, faltan datos de seguridad oficiales y el fármaco tiene antecedentes de retirada del mercado como anorexígeno.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicación autorizada), pendiente para el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Realizar una búsqueda sistemática de literatura y ensayos en el síndrome 16p11.2
- Evaluar la compatibilidad de la vía de administración (solución oral) con la población objetivo
- Valorar el riesgo cardiovascular (valvulopatía e hipertensión pulmonar) en la población candidata antes de cualquier estudio
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


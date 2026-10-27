---
layout: default
title: Lenograstim
parent: Solo predicción del modelo (L5)
nav_order: 460
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Lenograstim: nueva indicación predicha, Trastorno de liberación primaria de plaquetas (nivel de evidencia L5). Indicación original: No disponible en los datos de las autorizaciones de AEMPS (texto de…"
monitor_inn: "LENOGRASTIM"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease", "severe nonproliferative diabetic retinopathy"]
---

# Lenograstim
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

## Lenograstim: De Indicación Original No Especificada a Trastorno de Liberación Primaria de Plaquetas
{: .text-alpha }

## Resumen en Una Frase

Lenograstim es un factor estimulante de colonias de granulocitos (G-CSF) recombinante humano, comercializado en España con el nombre Granocyte. En los datos compilados para este informe no consta el texto de su indicación original.
El modelo TxGNN predice que podría ser efectivo para el **trastorno de liberación primaria de plaquetas**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de las autorizaciones de AEMPS (texto de indicación vacío) |
| Nueva Indicación Predicha | Trastorno de liberación primaria de plaquetas |
| Puntaje de Predicción TxGNN | 99,91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, lenograstim es un G-CSF recombinante que actúa sobre el receptor de G-CSF, estimulando la proliferación y diferenciación de los progenitores de neutrófilos (linaje granulocítico).

Los trastornos de liberación plaquetaria son defectos cualitativos de la función plaquetaria, relacionados con la secreción del contenido de los gránulos. Este no es un objetivo conocido del G-CSF. No se ha identificado ninguna vía biológica que conecte el fármaco con esta enfermedad, por lo que la razonabilidad mecanística es **baja**. El puntaje elevado de TxGNN refleja probablemente la proximidad en el grafo de conocimiento entre trastornos relacionados con plaquetas, y no una relación causal demostrada.

### Otras predicciones del modelo (para contexto)

| Enfermedad predicha | Puntaje TxGNN | Nivel de Evidencia | Comentario |
|------|------|------|------|
| Trastorno de liberación primaria de plaquetas | 99,91% | L5 | Sin vínculo mecanístico conocido |
| Trombastenia de Glanzmann | 99,89% | L5 | Defecto genético de la integrina αIIbβ3; G-CSF no actúa sobre este receptor |
| Pseudoenfermedad de von Willebrand | 99,88% | L5 | Mutación con ganancia de función en GP1BA; sin interacción conocida con el eje GPIb-VWF |
| Retinopatía diabética no proliferativa grave | 99,61% | L5 | Vínculo especulativo por la movilización de progenitores de médula ósea; la dirección del efecto es incierta, pues podría favorecer la neovascularización patológica |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 60672 | Granocyte 13 millones de UI polvo y disolvente para solución inyectable o perfusión | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 60211 | Granocyte 34 millones de UI polvo y disolvente para solución inyectable o perfusión | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico plausible entre el G-CSF y los defectos de función plaquetaria. Además, no se dispone de datos de seguridad ni de las indicaciones autorizadas.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), actualmente una carencia crítica para el cribado de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, mediante DrugBank).
- Realizar una revisión sistemática de la literatura que busque evidencia preclínica o clínica de G-CSF en trastornos plaquetarios.
- Evaluar la compatibilidad de la vía de administración y la similitud con la indicación original.
- Si se desea explorar otra línea, valorar por separado la hipótesis de retinopatía diabética, teniendo en cuenta el riesgo de neovascularización patológica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Lenograstim
parent: Solo predicción del modelo (L5)
nav_order: 460
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
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

Lenograstim es un factor estimulante de colonias de granulocitos (G-CSF) recombinante humano, con el nombre Granocyte. Actualmente no está comercializado en España: solo constan autorizaciones canceladas. En los datos compilados para este informe no consta el texto de su indicación original.
El modelo TxGNN predice que podría ser efectivo para el **trastorno de liberación primaria de plaquetas**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de las autorizaciones de AEMPS (texto de indicación vacío) |
| Nueva Indicación Predicha | Trastorno de liberación primaria de plaquetas |
| Puntaje de Predicción TxGNN | 0,9991 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado (registros anulados: 2 de 2) |
| Número de Autorizaciones | 2 (comercializadas: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Lenograstim es (traducción no oficial): «Agonista del receptor del factor estimulante de colonias de granulocitos». Texto original en inglés: "Granulocyte colony stimulating factor receptor agonist" ([ChEMBL CHEMBL2109128 (lenograstim): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2109128), CC BY-SA 3.0; consultado el 2026-11-19). Según la información conocida, lenograstim es un G-CSF recombinante que actúa sobre el receptor de G-CSF, estimulando la proliferación y diferenciación de los progenitores de neutrófilos (linaje granulocítico).

Los trastornos de liberación plaquetaria son defectos cualitativos de la función plaquetaria, relacionados con la secreción del contenido de los gránulos. Este no es un objetivo conocido del G-CSF. No se ha identificado ninguna vía biológica que conecte el fármaco con esta enfermedad, por lo que la razonabilidad mecanística es **baja**. La puntuación elevada del modelo TxGNN (deep learning) puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas con las plaquetas, y no evidencia biológica ni una relación causal demostrada.

### Otras predicciones del modelo (para contexto)

| Enfermedad predicha | Puntaje TxGNN | Nivel de Evidencia | Comentario |
|------|------|------|------|
| Trastorno de liberación primaria de plaquetas | 0,9991 | L5 | Sin vínculo mecanístico conocido |
| Trombastenia de Glanzmann | 0,9989 | L5 | Defecto genético de la integrina αIIbβ3; G-CSF no actúa sobre este receptor |
| Pseudoenfermedad de von Willebrand | 0,9988 | L5 | Mutación con ganancia de función en GP1BA; sin interacción conocida con el eje GPIb-VWF |
| Retinopatía diabética no proliferativa grave | 0,9961 | L5 | Vínculo especulativo por la movilización de progenitores de médula ósea; la dirección del efecto es incierta, pues podría favorecer la neovascularización patológica |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 60672 | GRANOCYTE 13 MILLONES DE UI POLVO Y DISOLVENTE PARA SOLUCION INYECTABLE O PERFUSION | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Italfarmaco S.A. | Revocada |
| 60211 | GRANOCYTE 34 MILLONES DE UI POLVO Y DISOLVENTE PARA SOLUCION INYECTABLE O PERFUSION | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Italfarmaco S.A. | Revocada |

Se muestran las 2 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; la versión anterior se guarda en el registro) | [ChEMBL CHEMBL2109128 (lenograstim): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2109128) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


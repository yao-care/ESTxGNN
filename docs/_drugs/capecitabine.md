---
layout: default
title: Capecitabine
parent: Solo predicción del modelo (L5)
nav_order: 138
evidence_level: L5
indication_count: 1
monitor_inn: "Capecitabine"
predicted_indications: ["gastric adenocarcinoma and proximal polyposis of the stomach"]
last_modified_at: 2026-10-31
description: "Capecitabine: nueva indicación predicha, Gastric adenocarcinoma and proximal polyposis of the stomach (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Capecitabine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Capecitabine: Gastric adenocarcinoma and proximal polyposis of the stomach
{: .text-alpha }

## Resumen en Una Frase

Capecitabina es un profármaco oral del 5-fluorouracilo, con relaciones registradas en el grafo de conocimiento para cáncer gástrico y metástasis de tumor maligno de colon.
El modelo TxGNN predice que podría ser efectivo para **adenocarcinoma gástrico y poliposis proximal del estómago (GAPPS)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Gastric adenocarcinoma and proximal polyposis of the stomach |
| Puntaje de Predicción TxGNN | 0.9994 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 7) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Capecitabina es un profármaco del 5-fluorouracilo (5-FU) que inhibe la timidilato sintasa (TYMS), enzima clave en la síntesis de ADN, lo que afecta a las células de división rápida. Los datos compilados confirman TYMS como diana farmacológica. No se dispone de datos detallados sobre el mecanismo de acción en la fuente de datos principal, por lo que esta descripción se basa en el conocimiento farmacológico general.

El puntaje tan alto probablemente refleja la cercanía con estas relaciones ya existentes más que una señal nueva de reposicionamiento.

El GAPPS es un síndrome hereditario raro asociado a mutaciones en el promotor 1B de *APC*. No hay datos mecanísticos que vinculen capecitabina con el componente de poliposis. Cualquier beneficio se limitaría al tratamiento del adenocarcinoma, no a modificar el fenotipo poliposo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de al menos 20 autorizaciones (lista parcial). Los textos de indicación aprobada no figuran en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Estado |
|---------|------|------|-----------|
| 89070 | Capecitabina Tarbis 150 mg | Comprimido recubierto con película | Vigente |
| 76108 | Capecitabina Kern Pharma 150 mg | Comprimido recubierto con película | Vigente |
| 76109 | Capecitabina Kern Pharma 500 mg | Comprimido recubierto con película | Vigente |
| 80078 | Capecitabina Normon 500 mg | Comprimido recubierto con película | Vigente |
| 112762020 | Capecitabina Accord 150 mg | Comprimido recubierto con película | Vigente |


## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (fluoropirimidina, profármaco del 5-FU) |
| Riesgo de Mielosupresión | Medio a alto (el grafo de conocimiento registra neutropenia, trombocitopenia, agranulocitosis y anemia como contraindicaciones relacionadas) |
| Clasificación de Emetogenicidad | Baja a media |
| Items de Monitoreo | Hemograma con diferencial, función hepática y renal, bilirrubina; actividad de DPD cuando proceda |
| Protección en Manejo | Seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Contraindicaciones registradas en el grafo de conocimiento** (no proceden del texto de la ficha técnica): enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, enfermedad infecciosa, neutropenia, agranulocitosis, enfermedad arterial coronaria, anemia (incluida la macrocítica), hiperbilirrubinemia (incluida la hereditaria), síndrome de Gilbert, insuficiencia renal, paro cardíaco súbito, enfermedad de conducción cardíaca, enterocolitis necrosante, estomatitis y deficiencia de dihidropirimidina deshidrogenasa.
- **Interacciones farmacológicas**: solo se registra la relación farmacológica con la diana timidilato sintasa (TYMS); no hay interacciones fármaco-fármaco con nivel de gravedad.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo, sin estudios que aborden directamente el GAPPS (nivel L5). El puntaje alto parece reflejar la superposición con el cáncer gástrico ya conocido, y no hay vínculo mecanístico con la poliposis.

**Para avanzar se necesita:**
- Revisar el prospecto oficial de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas)
- Datos del mecanismo de acción completos
- Búsqueda de estudios o series de casos de fluoropirimidinas en GAPPS o adenocarcinoma gástrico hereditario
- Definir si la indicación de interés es el adenocarcinoma (ya cubierto por el cáncer gástrico) o la poliposis, para la cual no hay sustento mecanístico
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


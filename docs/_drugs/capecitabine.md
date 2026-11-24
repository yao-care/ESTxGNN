---
layout: default
title: Capecitabine
parent: Solo predicción del modelo (L5)
nav_order: 138
evidence_level: L5
indication_count: 1
monitor_inn: "Capecitabine"
predicted_indications: ["gastric adenocarcinoma and proximal polyposis of the stomach"]
last_modified_at: 2026-11-24
description: "Capecitabine: nueva indicación predicha, Gastric adenocarcinoma and proximal polyposis of the stomach (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
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
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 7; autorizadas no comercializadas: 10; revocadas o suspendidas: 3) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Capecitabina es un profármaco del 5-fluorouracilo (5-FU) que inhibe la timidilato sintasa (TYMS), enzima clave en la síntesis de ADN, lo que afecta a las células de división rápida. Los datos compilados confirman TYMS como diana farmacológica. Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Capecitabine (traducción no oficial): «La capecitabina se metaboliza a fluorouracilo in vivo. Tanto las células normales como las tumorales metabolizan el fluorouracilo a monofosfato de 5-fluoro-2'-desoxiuridina (FdUMP) y trifosfato de 5-fluorouridina (FUTP). Estos metabolitos causan daño celular mediante dos mecanismos diferentes.» Texto original en inglés: "Capecitabine is metabolized to fluorouracil in vivo. Both normal and tumor cells metabolize fluorouracil to 5-fluoro-2'-deoxyuridine monophosphate (FdUMP) and 5-fluorouridine triphosphate (FUTP). These metabolites cause cell injury by two different mechanisms." ([DailyMed: Xeloda (capecitabine) prescribing information, H2-Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e702d84d-7162-4751-bf37-d724cc7e45a5), versión del 2026-02-05; consultado el 2026-11-19).

El puntaje tan alto probablemente refleja la cercanía con estas relaciones ya existentes más que una señal nueva de reposicionamiento.

El GAPPS es un síndrome hereditario raro asociado a mutaciones en el promotor 1B de *APC*. No hay datos mecanísticos que vinculen capecitabina con el componente de poliposis. Cualquier beneficio se limitaría al tratamiento del adenocarcinoma, no a modificar el fenotipo poliposo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de al menos 20 autorizaciones (lista parcial). Los textos de indicación aprobada no figuran en los datos compilados.

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 89070 | CAPECITABINA TARBIS 150 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Tarbis Farma S.L. | Comercializada |
| 76108 | CAPECITABINA KERN PHARMA 150 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Kern Pharma S.L. | Comercializada |
| 76109 | CAPECITABINA KERN PHARMA 500 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Kern Pharma S.L. | Comercializada |
| 112762020 | CAPECITABINA ACCORD 150 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Accord Healthcare S.L.U. | Comercializada |
| 80078 | CAPECITABINA NORMON 500 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorios Normon S.A. | Comercializada |

Se muestran 5 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Xeloda (capecitabine) prescribing information, H2-Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e702d84d-7162-4751-bf37-d724cc7e45a5) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


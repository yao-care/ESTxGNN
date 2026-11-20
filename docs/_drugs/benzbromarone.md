---
layout: default
title: Benzbromarone
parent: Solo predicción del modelo (L5)
nav_order: 97
evidence_level: L5
indication_count: 1
monitor_inn: "benzbromarone"
predicted_indications: ["hypouricemia, renal"]
last_modified_at: 2026-11-20
description: "Benzbromarone: nueva indicación predicha, hipouricemia renal (hypouricemia, renal) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 1)"
---

# Benzbromarone
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

## Benzbromarona: inhibidor de URAT1 (uricosúrico) → hipouricemia renal (hypouricemia, renal)
{: .text-alpha }

## Resumen en Una Frase

Benzbromarona es un uricosúrico que inhibe el transportador de urato URAT1 y se comercializa en España en comprimidos.
El modelo TxGNN predice que podría ser efectivo para **hipouricemia renal (hypouricemia, renal)**,
pero no hay ensayos clínicos y la literatura disponible describe la enfermedad y usa el fármaco solo como prueba diagnóstica, sin estudiar un beneficio terapéutico. La dirección de la predicción es mecanísticamente contraria a lo esperable.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | hipouricemia renal (hypouricemia, renal) |
| Puntaje de Predicción TxGNN | 0.9907 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Benzbromarone es (traducción no oficial): «Inhibidor del miembro 12 de la familia 22 de transportadores de solutos». Texto original en inglés: "Solute carrier family 22 member 12 inhibitor" ([ChEMBL CHEMBL388590 (benzbromarone): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL388590), CC BY-SA 3.0; consultado el 2026-11-19). Según la información conocida, benzbromarona es un inhibidor potente de URAT1 (SLC22A12) que aumenta la excreción renal de ácido úrico y reduce el urato sérico.

La hipouricemia renal se caracteriza por una pérdida excesiva de urato por el riñón, causada con mayor frecuencia por variantes de pérdida de función en URAT1 o GLUT9. Por ello, farmacológicamente benzbromarona imitaría o agravaría el defecto de base en lugar de corregirlo.

El puntaje alto (0.9907) probablemente refleja una asociación entre la diana del fármaco (URAT1) y el gen de la enfermedad, y no una relación terapéutica. El modelo parece haber captado un vínculo mecanístico en sentido inverso. En principio, el tratamiento estaría contraindicado, pues estos pacientes ya tienen riesgo de lesión renal aguda inducida por ejercicio y de nefrolitiasis.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

La literatura sobre hipouricemia renal es abundante, pero se trata de revisiones, series y casos. En ellos benzbromarona se emplea como herramienta diagnóstica (prueba de supresión con benzbromarona/pirazinamida) y no como tratamiento.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Revisión | Clinical Rheumatology | Actualización sobre hipouricemia (urato sérico < 2 mg/dL) y su etiología, dirigida al reumatólogo |
| [8976099](https://pubmed.ncbi.nlm.nih.gov/8976099/) | 1996 | Revisión | Nihon Rinsho | Concepto y clasificación de las alteraciones del metabolismo del urato |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cohorte | JASN | Análisis clínico y genético de 32 pacientes con hipouricemia renal; mutaciones en SLC22A12 (URAT1) |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Reporte de caso | Am J Kidney Dis | Dos hermanos con hipouricemia renal hereditaria e insuficiencia renal aguda inducida por ejercicio |
| [10879667](https://pubmed.ncbi.nlm.nih.gov/10879667/) | 2000 | Serie de casos | Clin Nephrol | Hipouricemia renal con insuficiencia renal aguda por ejercicio y disfunción renal crónica |
| [4009341](https://pubmed.ncbi.nlm.nih.gov/4009341/) | 1985 | Serie de casos | J Pediatr | Cuatro niños con hipouricemia renal hereditaria; benzbromarona no modificó los cocientes de aclaramiento |
| [8863890](https://pubmed.ncbi.nlm.nih.gov/8863890/) | 1996 | Reporte de caso | Acta Paediatr | Insuficiencia renal aguda recurrente tras ejercicio; la prueba benzbromarona/pirazinamida sugirió un defecto de reabsorción presecretora |
| [3380222](https://pubmed.ncbi.nlm.nih.gov/3380222/) | 1988 | Reporte de caso | Nephron | Defecto renal aislado del transporte de urato; el aclaramiento aumentó aún más con benzbromarona |
| [8893184](https://pubmed.ncbi.nlm.nih.gov/8893184/) | 1996 | Reporte de caso | Nephron | Transporte de ácido úrico en síndrome de Fanconi con hipouricemia renal, analizado con pirazinamida y benzbromarona |
| [12862209](https://pubmed.ncbi.nlm.nih.gov/12862209/) | 2003 | Reporte de caso | Hypertens Res | Insuficiencia renal aguda por ejercicio en un paciente con hipouricemia renal idiopática bajo losartán y triclormetiazida |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 49386 | URINORM 100 mg COMPRIMIDOS | Comprimido | No registrada en los datos locales |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como advertencia mecanística derivada de la literatura revisada, los pacientes con hipouricemia renal ya presentan riesgo de lesión renal aguda inducida por ejercicio y de nefrolitiasis; un uricosúrico podría agravar la pérdida renal de urato.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos ni estudios que evalúen benzbromarona como tratamiento de la hipouricemia renal, y el mecanismo (inhibición de URAT1) apunta en sentido contrario al defecto de la enfermedad, por lo que el puntaje alto no respalda un beneficio terapéutico.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados desde fuentes farmacológicas
- Advertencias y contraindicaciones del prospecto de AEMPS
- Un análisis que explique el sentido de la asociación fármaco-enfermedad y confirme si el fármaco agravaría la enfermedad
- Evidencia directa que respalde un beneficio terapéutico, antes de considerar cualquier estudio clínico

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; la versión anterior se guarda en el registro) | [ChEMBL CHEMBL388590 (benzbromarone): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL388590) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


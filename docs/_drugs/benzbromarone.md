---
layout: default
title: Benzbromarone
parent: Solo predicción del modelo (L5)
nav_order: 97
evidence_level: L5
indication_count: 1
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Benzbromarona: De Hiperuricemia y Gota a Hipouricemia Renal

## Resumen en Una Frase

Benzbromarona es un uricosúrico utilizado originalmente para el tratamiento de la gota y la hiperuricemia.
El modelo TxGNN predice que podría ser efectivo para **hipouricemia renal**, pero **no hay ensayos clínicos** y solo hay **18 publicaciones** de apoyo indirecto (revisiones, casos clínicos y estudios fisiológicos, en los que la benzbromarona se usa como herramienta diagnóstica, no como tratamiento).
Además, el análisis mecanístico sugiere que la predicción probablemente refleja una asociación del grafo en sentido inverso, no una relación terapéutica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Gota e hiperuricemia (según las relaciones de indicación del grafo de conocimiento; el texto de indicación de la autorización no está disponible) |
| Nueva Indicación Predicha | Hipouricemia renal |
| Puntaje de Predicción TxGNN | 99,07% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, benzbromarona es un inhibidor potente del transportador de urato 1 (URAT1, SLC22A12), que aumenta la excreción renal de ácido úrico y reduce la uricemia. Por ello se utiliza en gota e hiperuricemia.

La hipouricemia renal se caracteriza por una pérdida excesiva de urato por el riñón, habitualmente causada por variantes de pérdida de función en URAT1 o GLUT9. Farmacológicamente, la benzbromarona **imitaría o agravaría el defecto subyacente en lugar de corregirlo**. La puntuación alta de TxGNN (0,99) refleja probablemente una asociación en el grafo entre la diana del fármaco (URAT1) y el gen de la enfermedad, y no una relación terapéutica: el modelo parece haber capturado un vínculo mecanístico en dirección equivocada.

Esto concuerda con la literatura disponible: en los casos publicados, la benzbromarona se emplea en pruebas funcionales (junto con pirazinamida) para clasificar el defecto de transporte de urato, no para tratar la enfermedad. Además, estos pacientes ya tienen riesgo de insuficiencia renal aguda inducida por ejercicio y de nefrolitiasis, por lo que el tratamiento estaría, en principio, contraindicado.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se muestran las publicaciones más relevantes (ninguna es un ECA; se priorizan revisiones y estudios de cohorte).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Revisión | Clinical Rheumatology | Actualización sobre hipouricemia (urato sérico < 2 mg/dL) y su etiología para el reumatólogo |
| [8976099](https://pubmed.ncbi.nlm.nih.gov/8976099/) | 1996 | Revisión | Nihon Rinsho | Concepto y clasificación de las alteraciones del metabolismo del urato |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cohorte | J Am Soc Nephrol | Análisis clínico y genético de 32 pacientes con hipouricemia renal; mutaciones en SLC22A12 (URAT1) |
| [4009341](https://pubmed.ncbi.nlm.nih.gov/4009341/) | 1985 | Serie de casos | J Pediatr | En niños con hipouricemia renal hereditaria, ni pirazinamida ni benzbromarona modificaron de forma relevante los cocientes de aclaramiento |
| [10879667](https://pubmed.ncbi.nlm.nih.gov/10879667/) | 2000 | Serie de casos | Clin Nephrol | Hipouricemia renal con insuficiencia renal aguda inducida por ejercicio y disfunción renal crónica |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Caso clínico | Am J Kidney Dis | Dos hermanos con hipouricemia renal hereditaria e insuficiencia renal aguda por ejercicio |
| [8863890](https://pubmed.ncbi.nlm.nih.gov/8863890/) | 1996 | Caso clínico | Acta Paediatr | Episodios recurrentes de insuficiencia renal aguda tras ejercicio; prueba benzbromarona/pirazinamida sugiere defecto de reabsorción presecretora |
| [3380222](https://pubmed.ncbi.nlm.nih.gov/3380222/) | 1988 | Caso clínico | Nephron | Defecto renal aislado de transporte de urato; el aclaramiento de urato aumentó aún más con benzbromarona |
| [8893184](https://pubmed.ncbi.nlm.nih.gov/8893184/) | 1996 | Caso clínico | Nephron | Transporte de urato en síndrome de Fanconi con hipouricemia renal, analizado con pirazinamida y benzbromarona |
| [9144014](https://pubmed.ncbi.nlm.nih.gov/9144014/) | 1997 | Serie de casos | Intern Med | Dos casos de hipouricemia renal con nefrolitiasis; la benzbromarona aumentó el aclaramiento de urato (prueba diagnóstica) |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 49386 | URINORM 100 mg COMPRIMIDOS | Comprimido | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

No obstante, desde el punto de vista mecanístico, la benzbromarona aumenta la excreción renal de urato, por lo que en pacientes con hipouricemia renal podría agravar la pérdida de urato y los riesgos asociados descritos en la literatura (insuficiencia renal aguda inducida por ejercicio y nefrolitiasis).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos, y el análisis mecanístico indica que el fármaco fenocopiaría la enfermedad en lugar de tratarla. La evidencia disponible usa la benzbromarona solo como herramienta diagnóstica.

**Para avanzar se necesita:**
- Una justificación mecanística que contradiga el análisis actual (por ahora no hay base para un efecto terapéutico).
- Datos de mecanismo de acción verificados (por ejemplo, desde DrugBank).
- Advertencias y contraindicaciones del prospecto de la AEMPS, indispensables para cualquier evaluación de seguridad.
- Descartar formalmente la indicación como falso positivo del modelo antes de invertir más recursos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


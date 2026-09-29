---
layout: default
title: Phenylephrine
parent: Solo predicción del modelo (L5)
nav_order: 421
evidence_level: L5
indication_count: 3
---

# Phenylephrine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Fenilefrina: De Descongestión Nasal a Enfermedad de la Cavidad Nasal

## Resumen en Una Frase

La fenilefrina es un agonista adrenérgico alfa-1 que se usa como descongestionante nasal y midriático oftálmico. Las autorizaciones de AEMPS del Evidence Pack no incluyen texto de indicación.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de la cavidad nasal**, con **7 ensayos clínicos** y **8 publicaciones** asociados. La evidencia es mayoritariamente indirecta: casi todos los estudios evalúan combinaciones (como cofenilcaína) o comparadores distintos de la fenilefrina.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las autorizaciones de AEMPS (texto de indicación vacío). Según la farmacología: descongestión nasal |
| Nueva Indicación Predicha | Enfermedad de la cavidad nasal |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L2 (según el Evidence Pack; en la práctica débil, ver notas) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 9 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

La fenilefrina es un agonista de los receptores adrenérgicos alfa-1 (ADRA1A, ADRA1B y ADRA1D). Su activación produce vasoconstricción de la mucosa, lo que reduce la congestión y el sangrado y mejora la visualización endoscópica y quirúrgica. El Evidence Pack no incluye un campo detallado de mecanismo de acción, por lo que esta descripción se basa en los datos farmacológicos de los receptores diana y en el racional del modelo.

La relación entre la indicación conocida (descongestión nasal) y la nueva (enfermedad de la cavidad nasal) es muy estrecha. Por eso este caso es solo parcialmente un reposicionamiento genuino: se acerca más a una extensión del uso tópico ya establecido.

La evidencia disponible se refiere sobre todo a la fenilefrina como componente de productos combinados, por ejemplo cofenilcaína (fenilefrina + lidocaína) para la preparación tópica antes de procedimientos nasales. Por tanto, no permite atribuir el efecto a la fenilefrina sola.

## Evidencia de Ensayos Clínicos

Solo los ensayos con relevancia B tienen alguna conexión posible con la fenilefrina. El resto tienen relevancia C.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03380715](https://clinicaltrials.gov/study/NCT03380715) | N/A | Completado | 106 | Cofenilcaína (fenilefrina + lidocaína) en spray vs. nebulización nasal antes de nasoendoscopia rígida. Prueba un producto con fenilefrina en la cavidad nasal, pero compara vías de administración y la combinación confunde el efecto |
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Fase 2 | Completado | 21 | Estudio cruzado aleatorizado, doble ciego, de un antagonista H3 sobre la congestión en rinitis alérgica estacional. No se puede confirmar que la fenilefrina sea una intervención; verificar los brazos antes de usarlo |
| [NCT03228914](https://clinicaltrials.gov/study/NCT03228914) | Fase 4 | Completado | 20 | Oximetazolina tópica al 0,05 % vs. un comparador (truncado, posiblemente fenilefrina) sobre pérdida de sangre y visualización en cirugía endoscópica sinusal. Papel de la fenilefrina no confirmado |
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Fase 3 | Completado | 16 | Cocaína, lidocaína/xilometazolina y suero salino para analgesia intranasal. No hay evidencia de que la fenilefrina sea un brazo |
| [NCT06457100](https://clinicaltrials.gov/study/NCT06457100) | Fase 1/2 | Desconocido | 60 | Infusión perioperatoria de esmolol vs. lidocaína en cirugía endoscópica sinusal. No es una intervención con fenilefrina |
| [NCT02993770](https://clinicaltrials.gov/study/NCT02993770) | N/A | Desconocido | 120 | Dacriocistorrinostomía endonasal-endoscópica vs. externa. Comparación de técnicas quirúrgicas; la fenilefrina no es la intervención evaluada |
| [NCT03962634](https://clinicaltrials.gov/study/NCT03962634) | Fase 2 | Terminado | 3 | Kovanaze (tetracaína + oximetazolina) vs. articaína en anestesia pulpar. Otro fármaco, otra indicación |

Un octavo ensayo, [NCT04104789](https://clinicaltrials.gov/study/NCT04104789), repite el diseño Kovanaze vs. articaína. Fue retirado con 0 participantes y no aporta datos.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [15854186](https://pubmed.ncbi.nlm.nih.gov/15854186/) | 2005 | ECA | Int J Clin Pract | Spray de cofenilcaína vs. placebo antes de nasofibroendoscopia flexible en 98 pacientes. Se evaluó dolor, sabor y molestia global |
| [25133491](https://pubmed.ncbi.nlm.nih.gov/25133491/) | 2014 | ECA | PLoS One | Ácido tranexámico tópico sobre el sangrado y el campo quirúrgico en cirugía endoscópica sinusal por rinosinusitis crónica. No evalúa fenilefrina directamente |
| [37970776](https://pubmed.ncbi.nlm.nih.gov/37970776/) | 2023 | Revisión | Vestn Otorinolaringol | Enfoque patogénico del tratamiento de enfermedades inflamatorias de la nariz y los senos paranasales |
| [40899890](https://pubmed.ncbi.nlm.nih.gov/40899890/) | 2025 | Estudio experimental y clínico | Vestn Otorinolaringol | Seguridad y eficacia del spray Polydexa con fenilefrina en rinosinusitis aguda |
| [37184554](https://pubmed.ncbi.nlm.nih.gov/37184554/) | 2023 | Cohorte | Vestn Otorinolaringol | Estado endoscópico de la mucosa nasal tras el uso de Polydexa con fenilefrina (dexametasona + neomicina + polimixina B + fenilefrina) |
| [9780066](https://pubmed.ncbi.nlm.nih.gov/9780066/) | 1998 | Cohorte | Int J Pediatr Otorhinolaryngol | Rinometría acústica de la cavidad nasal y la nasofaringe tras adenoidectomía y amigdalectomía |
| [1375136](https://pubmed.ncbi.nlm.nih.gov/1375136/) | 1992 | Estudio in vitro | Clin Otolaryngol Allied Sci | Efecto de fármacos de uso nasal sobre la frecuencia de batido ciliar in vitro |
| [7378007](https://pubmed.ncbi.nlm.nih.gov/7378007/) | 1980 | Reporte de caso | Arch Ophthalmol | Toxicidad por cocaína intranasal durante dacriocistorrinostomía; un paciente sufrió además una reacción a fenilefrina intranasal |

## Información de Mercado en España

Hay 9 autorizaciones en total; se muestran las 5 principales. El Evidence Pack no incluye texto de indicación aprobada para ninguna de ellas, por lo que la última columna muestra el fabricante.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 84673 | Minims Fenilefrina Hidrocloruro 100 mg/ml colirio en solución | Colirio en solución | Bausch + Lomb Ireland Limited |
| 85084 | Fenilefrina Aguettant 100 microgramos/ml solución inyectable y para perfusión | Solución inyectable y para perfusión | Laboratoire Aguettant |
| 70638 | Hidrocloruro de Fenilefrina Altan 10 mg/ml solución inyectable | Solución inyectable | Altan Pharmaceuticals SA |
| 60227 | Mirazul 1,25 mg/ml colirio en solución | Colirio en solución | Laboratorio de Aplicaciones Farmacodinámicas S.A. |
| 34185 | Colircusí Fenilefrina 100 mg/ml colirio en solución | Colirio en solución | M4 Pharma S.L. |

Entre las formas farmacéuticas registradas también figuran la solución inyectable en jeringa precargada y la solución para pulverización nasal.

## Consideraciones de Seguridad

Consultar el prospecto para la información de seguridad. El Evidence Pack no contiene advertencias, contraindicaciones ni interacciones farmacológicas del prospecto de AEMPS. Los datos de interacciones incluidos corresponden solo a receptores diana, no a interacciones con otros fármacos.

Una señal de la literatura: el reporte de caso [7378007](https://pubmed.ncbi.nlm.nih.gov/7378007/) describe toxicidad tras cocaína intranasal, con una reacción adicional a fenilefrina intranasal. Los autores advierten que combinar simpaticomiméticos o fármacos moduladores alfa con cocaína es peligroso, sobre todo en pacientes con enfermedad cardiovascular hipertensiva.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo (vasoconstricción alfa-1 de la mucosa) es plausible y coincide con el uso tópico ya establecido. Aun así, no hay un ensayo que pruebe la fenilefrina sola en esta indicación. La evidencia procede de combinaciones como cofenilcaína, y el nivel L2 debe leerse con cautela.

**Para avanzar se necesita:**
- Verificar los brazos de intervención de NCT00562120 y NCT03228914, para confirmar si la fenilefrina participa.
- Obtener evidencia de fenilefrina en monoterapia, o un diseño que separe su efecto del de los anestésicos asociados.
- Descargar y analizar el prospecto de AEMPS (advertencias, contraindicaciones e interacciones) antes del cribado de seguridad.
- Confirmar la indicación original aprobada y la compatibilidad de vías de administración.

**Otras indicaciones predichas:** *laringofaringitis aguda* (puntaje 99.97 %, sin ensayos ni literatura, L5) y *cefalalgia autonómica trigeminal* (puntaje 99.30 %, L4) quedan en **Hold**. En la segunda, la literatura usa la fenilefrina solo como sonda farmacológica diagnóstica de la función simpática pupilar, no como tratamiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


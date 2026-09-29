---
layout: default
title: Loxapine
parent: Solo predicción del modelo (L5)
nav_order: 335
evidence_level: L5
indication_count: 10
---

# Loxapine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Loxapina: De Agitación en Esquizofrenia o Trastorno Bipolar a Trastorno Bipolar Afectivo Maníaco

## Resumen en Una Frase

Loxapina es un antipsicótico de primera generación, comercializado en España como polvo para inhalación (Adasuve) para la agitación aguda asociada a esquizofrenia o trastorno bipolar.
El modelo TxGNN predice que podría ser efectivo para el **trastorno bipolar afectivo maníaco**, con **0 ensayos clínicos registrados** en el Evidence Pack y **18 publicaciones** relacionadas.
Esta predicción se parece más a una confirmación de la indicación ya autorizada que a un verdadero reposicionamiento.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Agitación asociada a esquizofrenia o trastorno bipolar (según la literatura; el texto de indicación de AEMPS no está disponible en el registro) |
| Nueva Indicación Predicha | Trastorno bipolar afectivo maníaco |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L1 (con reservas, ver más abajo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

No se dispone de un campo detallado de mecanismo de acción en DrugBank, pero los datos farmacológicos muestran que loxapina se une a receptores dopaminérgicos (D2, D3, D4) y serotoninérgicos (5-HT2A, 5-HT2C, 5-HT6, 5-HT7). También se une al receptor de histamina H1 y al canal KNa1.1 (KCNT1). El antagonismo D2/5-HT2A es el perfil típico de los antipsicóticos.

Los antipsicóticos son una clase establecida para la manía aguda y la agitación en el trastorno bipolar, por lo que el ajuste mecanístico es sólido. Esquizofrenia y trastorno bipolar comparten síntomas psicóticos y de agitación que responden a la modulación dopaminérgica y serotoninérgica.

Hay una limitación importante. La literatura cubre la loxapina inhalada para la **agitación** asociada al trastorno bipolar I, no los síntomas centrales de la manía ni el tratamiento de mantenimiento. Además, la agitación ya es una indicación consistente con la ficha técnica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en el Evidence Pack.

La literatura sí cita dos ensayos de Fase III aleatorizados, doble ciego y controlados con placebo: [NCT00628589](https://clinicaltrials.gov/study/NCT00628589) (esquizofrenia) y [NCT00721955](https://clinicaltrials.gov/study/NCT00721955) (trastorno bipolar I). Aparecen solo a través de PMID 29163985, no como registros suministrados. Por eso el nivel L1 descansa en esas citas secundarias.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22226343](https://pubmed.ncbi.nlm.nih.gov/22226343/) | 2012 | Revisión de 2 ECA de Fase III | Int J Clin Pract | Análisis de tamaños del efecto de loxapina inhalada en agitación por esquizofrenia o trastorno bipolar |
| [29163985](https://pubmed.ncbi.nlm.nih.gov/29163985/) | 2017 | Análisis de respondedores de 2 ECA de Fase III | BJPsych Open | Loxapina inhalada 5 o 10 mg redujo la agitación (PANSS-EC) frente a placebo en 314 pacientes con trastorno bipolar I y 344 con esquizofrenia |
| [29724638](https://pubmed.ncbi.nlm.nih.gov/29724638/) | 2018 | ECA (PLACID) | Eur Neuropsychopharmacol | Loxapina inhalada frente a aripiprazol intramuscular en pacientes agitados con esquizofrenia o trastorno bipolar I |
| [27151529](https://pubmed.ncbi.nlm.nih.gov/27151529/) | 2016 | Revisión sistemática y metaanálisis | Hum Psychopharmacol | Evaluación de intervenciones farmacológicas a corto plazo para la agitación en esquizofrenia o trastorno bipolar |
| [23740380](https://pubmed.ncbi.nlm.nih.gov/23740380/) | 2013 | Revisión del fármaco | CNS Drugs | Adasuve, aprobado en EE. UU. y la UE para agitación aguda; concentración plasmática máxima en una mediana de 2 minutos |
| [31496709](https://pubmed.ncbi.nlm.nih.gov/31496709/) | 2019 | Revisión | Neuropsychiatr Dis Treat | Seguridad, eficacia y aceptación por el paciente de loxapina inhalada en agitación por esquizofrenia o trastorno bipolar I |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Revisión | Acta Psychiatr Scand | Opciones de tratamiento basadas en evidencia para la manía bipolar (estabilizadores del ánimo y antipsicóticos) |
| [30721526](https://pubmed.ncbi.nlm.nih.gov/30721526/) | 2019 | Revisión de expertos | Drugs R D | Loxapina inhalada para agitación aguda en trastorno bipolar y esquizofrenia, en el contexto de las guías actuales |
| [35913401](https://pubmed.ncbi.nlm.nih.gov/35913401/) | 2022 | Revisión | Expert Rev Neurother | Cincuenta años de experiencia con loxapina para la tranquilización rápida no coercitiva |
| [37581475](https://pubmed.ncbi.nlm.nih.gov/37581475/) | 2023 | Revisión | Expert Opin Pharmacother | Mejora del tratamiento farmacológico de la agitación asociada al trastorno bipolar |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 113823002 | ADASUVE 9,1 MG POLVO PARA INHALACIÓN (UNIDOSIS) | Polvo para inhalación (unidosis) | Ferrer Internacional S.A. |
| 113823004 | ADASUVE 9,1 MG POLVO PARA INHALACIÓN (UNIDOSIS) | Polvo para inhalación (unidosis) | Ferrer Internacional S.A. |

El registro no incluye el texto de la indicación aprobada para ninguna de las dos autorizaciones.

## Consideraciones de Seguridad

- **Perfil de unión a receptores** (no son interacciones con otros fármacos): D2, D3, D4, 5-HT2A, 5-HT2C, 5-HT6, 5-HT7, H1 y KNa1.1. La afinidad por H1 sugiere sedación.
- **Vía inhalada**: el análisis del Evidence Pack señala riesgo de broncoespasmo y la necesidad de monitorización tipo REMS.

No hay datos de advertencias, contraindicaciones ni interacciones fármaco-fármaco. Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Los ECA de Fase III citados en la literatura respaldan la loxapina inhalada para la agitación en trastorno bipolar I, y el ajuste mecanístico D2/5-HT2A es fuerte. Los datos apoyan la indicación de agitación y la vía inhalada, no la loxapina oral para la manía.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de AEMPS (advertencias, contraindicaciones e indicación autorizada).
- Verificar directamente los ensayos NCT00628589 y NCT00721955, y registrar los ECA de Fase III como evidencia primaria.
- Definir si el objetivo es la manía nuclear o el mantenimiento, ya que la evidencia actual no los cubre.
- Establecer un plan de monitorización del broncoespasmo para la vía inhalada.

Las otras 9 predicciones (retinopatías, miopías, hidranencefalia, entre otras) quedan en **Hold** con nivel L5. No tienen vínculo mecanístico plausible y el puntaje alto parece un artefacto del grafo de conocimiento. Las 15 publicaciones recuperadas para la distrofia retiniana son revisiones oftalmológicas genéricas que no mencionan la loxapina.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


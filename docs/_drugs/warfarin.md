---
layout: default
title: Warfarin
parent: Evidencia moderada (L3-L4)
nav_order: 861
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-14
description: "Warfarin: nueva indicación predicha, Deficiencia de cofactor 2 de la heparina (nivel de evidencia L4). Indicación original: Embolia pulmonar…"
monitor_inn: "warfarin"
predicted_indications: ["heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "thrombophilia", "rheumatoid arthritis", "breast fibrocystic disease", "benign mammary dysplasia"]
---

# Warfarin
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **7** 
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

# Warfarina: De Enfermedad Tromboembólica a Deficiencia de Cofactor 2 de la Heparina

## Resumen en Una Frase

Warfarina es un anticoagulante oral antagonista de la vitamina K, originalmente utilizado para el tratamiento de la embolia pulmonar, la enfermedad trombótica y la embolia intracraneal.
El modelo TxGNN predice que podría ser efectivo para **deficiencia de cofactor 2 de la heparina**, aunque hasta ahora solo existen **0 ensayos clínicos** y **3 publicaciones** (todas informes de casos) que respaldan esta dirección.
Entre las indicaciones predichas, la mejor respaldada es la **trombofilia** (1 ensayo de Fase 3 y numerosas revisiones), que se comenta en las secciones siguientes.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Embolia pulmonar, enfermedad trombótica y embolia intracraneal (según el grafo de conocimiento; los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Deficiencia de cofactor 2 de la heparina |
| Puntaje de Predicción TxGNN | 99.87% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados en los datos compilados. Según la información conocida, la warfarina inhibe la síntesis de los factores de coagulación dependientes de la vitamina K (II, VII, IX y X), y su eficacia en la prevención y el tratamiento de la enfermedad tromboembólica está bien establecida.

La deficiencia de cofactor 2 de la heparina es una trombofilia hereditaria en la que se reduce la inhibición de la trombina. Reducir la síntesis de factores procoagulantes es biológicamente plausible como profilaxis secundaria a largo plazo. Se trata de una extensión de los usos trombóticos ya aprobados y no de un mecanismo nuevo, y el puntaje elevado del modelo probablemente refleja esa proximidad.

La evidencia directa, sin embargo, se limita a informes de casos antiguos y aislados, por lo que no permite establecer eficacia ni seguridad en esta población concreta.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la deficiencia de cofactor 2 de la heparina.

Como referencia, para la cuarta indicación predicha (trombofilia) existe un ensayo relevante:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00895505](https://clinicaltrials.gov/study/NCT00895505) | Fase 3 | Desconocido | 300 | Estrategia guiada por dímero D para decidir la duración de la profilaxis secundaria del tromboembolismo venoso tras una trombosis venosa profunda no provocada; apoyo indirecto |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2214444](https://pubmed.ncbi.nlm.nih.gov/2214444/) | 1990 | Reporte de caso | Kyobu geka | Trombosis del ventrículo derecho en una paciente de 14 años con deficiencia familiar de cofactor II de la heparina; se extirpó quirúrgicamente un trombo |
| [2033902](https://pubmed.ncbi.nlm.nih.gov/2033902/) | 1991 | Reporte de caso | Nihon Kyobu Shikkan Gakkai zasshi | Mujer de 48 años con deficiencia congénita y embolias pulmonares recurrentes; recibió warfarina durante 7 años y luego heparina a dosis baja |
| [11570053](https://pubmed.ncbi.nlm.nih.gov/11570053/) | 2001 | Reporte de caso (familiar) | Journal of UOEH | Familia con trombosis múltiple, una niña tratada con warfarina que presentó una nueva trombosis a los 7 años |

Estas publicaciones describen casos clínicos y no permiten concluir eficacia. Para otras indicaciones predichas, la literatura más relevante incluye una revisión de la ISTH sobre anticoagulantes orales directos en trombofilia grave (PMID 39233011, 2024).

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 63063 | ALDOCUMAR 3 mg COMPRIMIDOS | Comprimido | No disponible en los datos compilados |
| 63064 | ALDOCUMAR 5 mg COMPRIMIDOS | Comprimido | No disponible en los datos compilados |
| 32864 | ALDOCUMAR 10 mg COMPRIMIDOS | Comprimido | No disponible en los datos compilados |
| 63062 | ALDOCUMAR 1 mg COMPRIMIDOS | Comprimido | No disponible en los datos compilados |

Las cuatro autorizaciones son de Laboratorio Aldo Unión S.L., monofármaco y vigentes.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): hipertensión, insuficiencia hepática y enfermedad hepática, colestasis, enfermedad de la vesícula biliar, insuficiencia cardíaca congestiva, hipotiroidismo, síndrome nefrótico, insuficiencia renal, trastornos de la coagulación sanguínea, anemia (incluida la macrocítica), hiperlipidemia, trastornos psicóticos y mentales, abuso de sustancias, enfermedades del tejido conectivo, óseas y del cartílago, y enfermedad diarreica crónica.
- **Interacciones farmacológicas**: se registraron 865 interacciones. Entre las principales:
  - **Mayores**: ácido acetilsalicílico y metronidazol.
  - **Moderadas**: ranitidina, rabeprazol, doxiciclina, hidrocortisona, metformina, amoxicilina, bupropión, aprepitant, mesalazina, triamcinolona, dexametasona, betametasona, budesonida y ácido quenodesoxicólico, entre otras.
  - **Menores**: acarbosa, albiglutida y ácido ascórbico.
- **Señales adicionales de la literatura**: necrosis cutánea inducida por warfarina (frecuente en deficiencias de proteína C/S), teratogenicidad en el embarazo y mayor riesgo hemorrágico con danazol.

Para advertencias y contraindicaciones del texto oficial, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es mecanísticamente plausible, pero la evidencia directa se reduce a tres informes de casos antiguos, sin ensayos clínicos (nivel L4). Además, la advertencias y contraindicaciones del prospecto no están disponibles, lo que impide una evaluación de seguridad completa.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas).
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisar sistemáticamente la literatura sobre warfarina en deficiencias de antitrombina y cofactor II de la heparina, incluyendo estudios observacionales.
- Evaluar poblaciones específicas: embarazo, síndrome antifosfolípido y comparación con anticoagulantes orales directos.
- Considerar otras predicciones: la **trombofilia** (L1 según la clasificación automática, aunque el único ensayo de Fase 3 tiene estado desconocido y apoya el escenario solo indirectamente) merece evaluación propia. Las predicciones para artritis reumatoide, enfermedad fibroquística de la mama y displasia mamaria benigna carecen de vínculo terapéutico, pues la evidencia recuperada corresponde a interacciones farmacológicas, y no deben considerarse respaldadas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


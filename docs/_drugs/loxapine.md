---
layout: default
title: Loxapine
parent: Solo predicción del modelo (L5)
nav_order: 489
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Loxapine: nueva indicación predicha, Trastorno afectivo bipolar maníaco (nivel de evidencia L5). Indicación original: Esquizofrenia, trastorno bipolar…"
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

# Loxapina: De Esquizofrenia y Trastorno Bipolar a Trastorno Afectivo Bipolar Maníaco

## Resumen en Una Frase

Loxapina es un antipsicótico de primera generación (dibenzoxazepina), originalmente utilizado en el tratamiento de la esquizofrenia, el trastorno bipolar y el trastorno afectivo mayor.
El modelo TxGNN predice que podría ser efectivo para el **trastorno afectivo bipolar maníaco**, con **0 ensayos clínicos** registrados y **20 publicaciones** en los datos compilados.
Cabe señalar que el trastorno bipolar ya es una indicación original, por lo que esta predicción no constituye un reposicionamiento en sentido estricto.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Esquizofrenia, trastorno bipolar, trastorno afectivo mayor (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Trastorno afectivo bipolar maníaco |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L1 (asignado por conocimiento externo; ver nota abajo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Proceed with Guardrails |

> **Nota sobre el nivel de evidencia:** los datos compilados no incluyen ensayos clínicos verificados. El nivel L1 se basa en los dos ensayos de Fase 3 con loxapina inhalada para la agitación en trastorno bipolar, conocidos externamente y citados solo de forma indirecta por las revisiones incluidas. Con los datos verificables, el nivel sería más prudente (L3, estudios de revisión).

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente principal. Según la información conocida, loxapina es un antipsicótico de la clase de las dibenzoxazepinas. Los datos farmacológicos compilados indican afinidad por los receptores dopaminérgicos D2, D3 y D4, los serotoninérgicos 5-HT2A, 5-HT2C, 5-HT6 y 5-HT7, y el receptor histaminérgico H1, además del canal de potasio KNa1.1 (KCNT1).

El antagonismo dopaminérgico D2 y serotoninérgico 5-HT2A es coherente con los efectos antimaníacos y antiagitación. La esquizofrenia y el trastorno bipolar comparten sintomatología (psicosis, agitación), y los antipsicóticos se usan de forma establecida en los episodios maníacos.

La literatura se centra sobre todo en la formulación inhalada (Adasuve) para la agitación aguda asociada a trastorno bipolar o esquizofrenia. Esto es una indicación sintomática más acotada que la manía en general.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Se muestran 10 publicaciones representativas (de 20 disponibles). Todas son revisiones o análisis; ninguna es un ensayo clínico primario.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27151529](https://pubmed.ncbi.nlm.nih.gov/27151529/) | 2016 | Revisión sistemática y metaanálisis | Human Psychopharmacology | Evalúa intervenciones farmacológicas a corto plazo para la agitación en esquizofrenia o trastorno bipolar |
| [22226343](https://pubmed.ncbi.nlm.nih.gov/22226343/) | 2012 | Análisis de tamaños de efecto de 2 ECA de Fase 3 | Int J Clin Pract | Describe la eficacia de loxapina inhalada en agitación asociada a esquizofrenia o trastorno bipolar |
| [23740380](https://pubmed.ncbi.nlm.nih.gov/23740380/) | 2013 | Revisión | CNS Drugs | Adasuve fue aprobado en EE. UU. y la UE para agitación aguda en bipolar o esquizofrenia; concentración máxima en unos 2 min; resume dos ECA doble ciego |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Revisión | Acta Psychiatr Scand | Opciones basadas en evidencia para la manía bipolar y elección de estabilizador del ánimo y antipsicótico |
| [30721526](https://pubmed.ncbi.nlm.nih.gov/30721526/) | 2019 | Revisión | Drugs in R&D | Revisión de expertos sobre loxapina inhalada en agitación aguda en bipolar y esquizofrenia |
| [31496709](https://pubmed.ncbi.nlm.nih.gov/31496709/) | 2019 | Revisión | Neuropsychiatr Dis Treat | Seguridad, eficacia y aceptabilidad por parte del paciente de loxapina inhalada |
| [38301034](https://pubmed.ncbi.nlm.nih.gov/38301034/) | 2024 | Revisión | Prim Care Companion CNS Disord | Alternativas a la vía intramuscular para la agitación aguda en esquizofrenia y bipolar |
| [35913401](https://pubmed.ncbi.nlm.nih.gov/35913401/) | 2022 | Revisión | Expert Rev Neurother | Cincuenta años de experiencia con loxapina en la tranquilización rápida no coercitiva |
| [28208695](https://pubmed.ncbi.nlm.nih.gov/28208695/) | 2017 | Revisión clínica | Int J Mol Sci | Eficacia y tolerabilidad de loxapina inhalada en la agitación aguda en trastornos psiquiátricos |
| [30497838](https://pubmed.ncbi.nlm.nih.gov/30497838/) | 2019 | Estudio retrospectivo (41 pacientes) | Eur Neuropsychopharmacol | Loxapina inhalada redujo la agitación en 10 minutos en pacientes con trastorno de personalidad |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 113823002 | ADASUVE 9,1 mg polvo para inhalación (unidosis) | Polvo para inhalación (unidosis) | No disponible en los datos |
| 113823004 | ADASUVE 9,1 mg polvo para inhalación (unidosis) | Polvo para inhalación (unidosis) | No disponible en los datos |

Ambas autorizaciones corresponden al titular Ferrer Internacional S.A. y están vigentes.

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (según el grafo de conocimiento, no según el prospecto):** epilepsia, hiperplasia benigna de próstata, abuso o dependencia de sustancias, carcinoma de mama femenino, enfermedad cardiovascular, cardiopatía, glaucoma, síndrome neuroléptico maligno, enfermedad de Alzheimer, discinesia tardía, discinesia linguo-facial-bucal e hiperprolactinemia (incluidas las formas familiar y adquirida, y el tumor hipofisario productor de prolactina).
- **Formulación inhalada:** riesgo de broncoespasmo, por lo que se restringe a pacientes sin enfermedad de las vías respiratorias (programa REMS en EE. UU.).
- **Interacciones farmacológicas:** se identificaron 9 registros, que corresponden a interacciones farmacodinámicas con dianas (receptores 5-HT2A, 5-HT2C, 5-HT6, 5-HT7, D2, D3, D4, H1 y KNa1.1), no a interacciones con otros fármacos. Se requiere revisión específica de la medicación concomitante, especialmente depresores del SNC y otros antipsicóticos.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Loxapina ya tiene como indicación original el trastorno bipolar, y la formulación inhalada está comercializada en España para la agitación asociada. La evidencia verificable en los datos son revisiones; el nivel L1 depende de ensayos de Fase 3 conocidos externamente, por lo que debe confirmarse.

**Para avanzar se necesita:**
- Verificar directamente los ensayos pivotales de Fase 3 de loxapina inhalada (registros y publicaciones primarias).
- Obtener el prospecto de la AEMPS (advertencias, contraindicaciones e indicación autorizada), ya que los textos de indicación están vacíos.
- Completar los datos del mecanismo de acción desde DrugBank.
- Definir criterios de exclusión por enfermedad respiratoria y un plan de monitorización de seguridad (broncoespasmo, sedación, efectos extrapiramidales, prolactina).
- Aclarar si la indicación objetivo es la manía en general o únicamente la agitación aguda asociada, ya que la evidencia disponible respalda sobre todo esta última.

---

### Nota sobre otras predicciones

Las otras nueve predicciones (rangos 2 a 10, p. ej., distrofia retiniana, hidranencefalia, miopía ligada al X, enfermedad de Charcot-Marie-Tooth tipo 1G) tienen puntajes TxGNN altos (≈99.9%), pero carecen de ensayos clínicos y de literatura, y no presentan un vínculo mecanístico plausible. Todas se clasifican como L5 con decisión **Hold**.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


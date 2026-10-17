---
layout: default
title: Theophylline
parent: Solo predicción del modelo (L5)
nav_order: 789
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Theophylline: nueva indicación predicha, Enfermedad trombótica (nivel de evidencia L5). Indicación original: Asma (según las indicaciones originales del grafo de conocimiento"
monitor_inn: "Theophylline"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
---

# Theophylline
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Teofilina: De Asma a Enfermedad Trombótica

## Resumen en Una Frase

La teofilina es una xantina utilizada desde hace décadas como broncodilatador en el tratamiento del asma, la bronquitis y el enfisema.
El modelo TxGNN predice que podría ser efectiva para **enfermedad trombótica**, pero **no hay ensayos clínicos** y las **19 publicaciones** recuperadas no evalúan la teofilina como tratamiento antitrombótico. La predicción carece por ahora de respaldo clínico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Asma (según las indicaciones originales del grafo de conocimiento; los textos de indicación de las autorizaciones no están disponibles en los datos compilados) |
| Nueva Indicación Predicha | Enfermedad trombótica |
| Puntaje de Predicción TxGNN | 99.62% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados del mecanismo de acción en la ficha del fármaco. Los datos de farmacología compilados indican que la teofilina interactúa con los receptores de adenosina A1, A2A, A2B y A3. Según el análisis mecanístico del informe, es además un inhibidor no selectivo de las fosfodiesterasas (PDE) y un antagonista de los receptores de adenosina.

El vínculo con la trombosis es **teórico**. La inhibición de PDE aumenta el AMPc en las plaquetas, lo que podría reducir su agregación. Sin embargo, el antagonismo de la adenosina podría actuar en sentido contrario, porque la adenosina también inhibe la agregación plaquetaria. La relación con el asma, una enfermedad de la vía aérea, es indirecta, y la literatura recuperada no prueba la teofilina como terapia antitrombótica.

En conclusión, el puntaje alto del modelo (99.62%) no está respaldado por evidencia clínica y debe interpretarse con mucha cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Se recuperaron 19 publicaciones. Ninguna es un ensayo clínico de teofilina en enfermedad trombótica, y la mayoría menciona la teofilina solo de forma tangencial. Se listan las 10 más pertinentes.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [4776567](https://pubmed.ncbi.nlm.nih.gov/4776567/) | 1973 | No clasificado | Minerva Cardioangiologica | Acción hemocinética y metabólica de un derivado nicotinato de teofilina en arteriopatía periférica obliterante crónica (derivado, no teofilina pura) |
| [5136470](https://pubmed.ncbi.nlm.nih.gov/5136470/) | 1971 | No clasificado | Cardiologia Pratica | Efectos cardiocirculatorios de un éster nicotínico de hidroxietil-teofilina en angiopatías cerebrales y periféricas |
| [5605983](https://pubmed.ncbi.nlm.nih.gov/5605983/) | 1967 | No clasificado | Annali di Ottalmologia e Clinica Oculistica | Control electrorretinográfico de la acción del nicotinato de teofilina en enfermedades vasculares de la retina |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Estudio in vitro | General Pharmacology | Interacción de milrinona y adenosina en la inhibición de la agregación plaquetaria mediada por AMPc (no evalúa teofilina directamente) |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Revisión | CRC Critical Reviews in Biochemistry | Prostaglandinas, plaquetas y aterosclerosis; el AMPc plaquetario como mecanismo antiagregante |
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Revisión | Clinical Pharmacokinetics | Farmacocinética de la ticlopidina, antiagregante plaquetario (otro fármaco) |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Método de laboratorio | British Journal of Haematology | Radioinmunoensayo del factor plaquetario 4; la teofilina se usa solo como componente del anticoagulante de la muestra |
| [6241135](https://pubmed.ncbi.nlm.nih.gov/6241135/) | 1984 | Observacional | Cor et Vasa | Subpoblaciones de linfocitos T (resistentes a teofilina) en pacientes con infarto, arteriopatía periférica y tromboflebitis |
| [32824700](https://pubmed.ncbi.nlm.nih.gov/32824700/) | 2020 | Laboratorio/Métodos | Cells | Efecto de la anticoagulación y del procesamiento de muestras en la cuantificación de microARN sanguíneos |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | Laboratorio | Platelets | Medición de CLEC-2 soluble en plasma humano como marcador de activación plaquetaria |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1891 | EUFILINA VENOSA 200 mg solución inyectable | Solución inyectable |
| 56165 | THEO-DUR 200 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada |
| 56166 | THEO-DUR 300 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada |
| 45303 | ELIXIFILIN 5,33 mg/ml solución oral | Solución oral |
| 31900 | TEROMOL RETARD 300 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada |

Hay 6 autorizaciones vigentes, todas de monofármaco. La tabla muestra las 5 principales; la sexta es THEO-DUR 100 mg (nº 56199). Los textos de indicación aprobada no están disponibles en los datos compilados.

---

## Consideraciones de Seguridad

- **Contraindicaciones o precauciones según el grafo de conocimiento** (no proceden del texto del prospecto): hipertensión, insuficiencia y enfermedad hepática, epilepsia, trastornos de ansiedad y neuróticos, trastornos psicóticos y esquizoafectivos, porfiria, enfermedad renal, enfermedad de la vesícula biliar, trombocitopenia, neutropenia y agranulocitosis, hipotiroidismo, úlcera péptica, glaucoma de ángulo abierto, diabetes mellitus y cetoacidosis diabética, hiperplasia prostática benigna, dermatitis herpetiforme.
- **Interacciones farmacológicas**: la consulta de interacciones se completó, pero devolvió solo datos de afinidad por los receptores de adenosina (A1, A2A, A2B, A3), no interacciones con otros fármacos.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto. Cabe destacar que la trombocitopenia figura entre las condiciones de precaución, lo que merece atención en un contexto hematológico o trombótico.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5): no hay ensayos clínicos y la literatura recuperada no evalúa la teofilina como antitrombótico. El mecanismo es teórico y contradictorio, porque la inhibición de PDE podría reducir la agregación plaquetaria mientras que el antagonismo de adenosina podría oponerse a ese efecto.

**Para avanzar se necesita:**
- Estudios preclínicos que midan el efecto de la teofilina en agregación plaquetaria y trombosis, a concentraciones terapéuticas.
- Datos detallados del mecanismo de acción (MOA), que faltan en la ficha del fármaco.
- Las advertencias y contraindicaciones oficiales del prospecto de la AEMPS, que aún no se han incorporado.
- Un análisis de la relación riesgo-beneficio frente a los antitrombóticos establecidos, dado el estrecho margen terapéutico de la teofilina.
- Una revisión de otras indicaciones predichas: la enfermedad pulmonar obstructiva tiene la mayor evidencia (nivel L1, ensayos de Fase 3 como NCT01599871), pero corresponde en gran parte a la indicación original y no es un verdadero reposicionamiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Theophylline
parent: Solo predicción del modelo (L5)
nav_order: 789
evidence_level: L5
indication_count: 6
monitor_inn: "Theophylline"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
last_modified_at: 2026-10-23
description: "Theophylline: nueva indicación predicha, Enfermedad trombótica (nivel de evidencia L5). Indicación original: Asma, bronquitis, enfisema pulmonar y otras enfermedades pulmonares"
---

# Theophylline
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Teofilina: De Asma y Enfermedades Broncopulmonares a Enfermedad Trombótica
{: .text-alpha }

## Resumen en Una Frase

La teofilina es un fármaco broncodilatador, registrado en el grafo de conocimiento para asma, bronquitis, enfisema pulmonar y otras enfermedades pulmonares.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad trombótica**, pero **no hay ensayos clínicos** y la literatura recuperada **no estudia la teofilina como antitrombótico**, por lo que la predicción carece de respaldo clínico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Asma, bronquitis, enfisema pulmonar y otras enfermedades pulmonares (relaciones registradas en el grafo de conocimiento; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Enfermedad trombótica |
| Puntaje de Predicción TxGNN | 0,9962 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 5 de 6) |
| Número de Autorizaciones | 6 (vigentes: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

La teofilina es un inhibidor no selectivo de la fosfodiesterasa y antagonista de los receptores de adenosina (A1, A2A, A2B y A3). Actualmente no se dispone de datos detallados del mecanismo de acción en las fuentes de fármacos, pero estas dianas farmacológicas sí están documentadas.

En teoría, el aumento de AMPc en las plaquetas podría reducir su agregación. Sin embargo, el antagonismo de la adenosina puede contrarrestar el efecto antiplaquetario de la propia adenosina, por lo que la dirección neta del efecto es incierta.

La relación entre las enfermedades respiratorias originales y la enfermedad trombótica es débil. La literatura recuperada trata sobre la farmacocinética de la ticlopidina, biomarcadores plaquetarios, métodos de ensayo y un sensor para detectar teofilina; ninguna prueba la teofilina como antitrombótico. El puntaje elevado de TxGNN es una predicción computacional sin respaldo clínico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Ninguna publicación estudia directamente la teofilina en enfermedad trombótica. Se listan las más relevantes por tipo, con la advertencia de que su relación es indirecta:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Revisión | Clinical Pharmacokinetics | Farmacocinética de la ticlopidina, antiagregante plaquetario; no evalúa teofilina |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Revisión | CRC Critical Reviews in Biochemistry | Prostaglandinas, plaquetas y aterosclerosis (tromboxano A2 y prostaciclina) |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | Cohorte | Inflammatory Bowel Diseases | Agregados plaqueta-leucocito en enfermedad inflamatoria intestinal |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | Cohorte | Rheumatology (Oxford) | Activación de plaquetas y neutrófilos en la enfermedad de Behçet |
| [32824700](https://pubmed.ncbi.nlm.nih.gov/32824700/) | 2020 | Metodología | Cells | Efecto de la anticoagulación y el procesamiento de muestras en la cuantificación de microARN |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | Metodología | Platelets | Medición de CLEC-2 soluble en plasma humano |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Metodología | British Journal of Haematology | Radioinmunoensayo del factor plaquetario 4 (la teofilina se usa solo como anticoagulante de la muestra) |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Método analítico | Analytica Chimica Acta | Aptasensor electroquímico para detectar teofilina |

## Información de Mercado en España

Los textos de indicación aprobada de estas autorizaciones están vacíos en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 56165 | THEO-DUR 200 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | No disponible |
| 56166 | THEO-DUR 300 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | No disponible |
| 45303 | ELIXIFILIN 5,33 mg/ml solución oral | Solución oral | No disponible |
| 31900 | TEROMOL RETARD 300 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | No disponible |
| 56199 | THEO-DUR 100 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | No disponible |

Además existe una autorización cancelada (1891, EUFILINA VENOSA 200 mg solución inyectable).

## Consideraciones de Seguridad

- **Contraindicaciones registradas en el grafo de conocimiento** (no proceden del texto del prospecto): hipertensión, insuficiencia hepática, epilepsia, trastornos de ansiedad, porfiria, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, hipotiroidismo, úlcera péptica, glaucoma de ángulo abierto, trastornos psicóticos y esquizoafectivos, diabetes mellitus y cetoacidosis diabética, hiperplasia prostática benigna, neutropenia y agranulocitosis.
- **Perfil farmacológico**: la teofilina actúa sobre los receptores de adenosina A1, A2A, A2B y A3.

Es necesario consultar el prospecto para las advertencias y contraindicaciones oficiales. Además, la teofilina tiene un margen terapéutico estrecho y requiere monitorización de sus concentraciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico ni estudio que evalúe la teofilina en enfermedad trombótica, y el efecto neto sobre la agregación plaquetaria es mecanísticamente incierto. El puntaje de 0,9962 es solo una predicción computacional (nivel L5).

**Para avanzar se necesita:**
- Estudios preclínicos de agregación plaquetaria y trombosis con teofilina
- Datos detallados del mecanismo de acción
- Texto del prospecto con advertencias y contraindicaciones oficiales de la AEMPS
- Revisión de la seguridad, dado el margen terapéutico estrecho y la contraindicación registrada en trombocitopenia

## Otras Predicciones Evaluadas (Contexto)

| Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Observación |
|------|------|------|------|
| Enfermedad de la cavidad nasal | 0,9953 | L5 | Un estudio humano (PMID 9648963) de teofilina de liberación lenta en provocación nasal con alérgeno en rinitis alérgica; eficacia no confirmada |
| Laringotraqueítis | 0,9951 | L5 | Sin literatura ni ensayos |
| Enfermedad traqueal | 0,9949 | L3 | Datos in vitro y un estudio retrospectivo veterinario; sin evidencia humana definida |
| Faringitis | 0,9946 | L4 | Literatura dominada por macrólidos; sin datos de teofilina en faringitis |
| Laringofaringitis aguda | 0,9935 | L5 | Sin literatura ni ensayos |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


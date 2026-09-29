---
layout: default
title: Theophylline
parent: Solo predicción del modelo (L5)
nav_order: 525
evidence_level: L5
indication_count: 7
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Teofilina: De Obstrucción Reversible de las Vías Aéreas a Enfermedad Trombótica

## Resumen en Una Frase

La teofilina es una xantina utilizada desde hace décadas como broncodilatador en asma, enfisema y bronquitis crónica.
El modelo TxGNN predice que podría ser efectiva para **enfermedad trombótica**, pero se trata solo de una predicción basada en grafos: **0 ensayos clínicos** y **ninguna publicación que evalúe directamente la teofilina en trombosis**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de AEMPS (los textos de indicación están vacíos). Según la base farmacológica consultada: síntomas y obstrucción reversible de las vías aéreas (asma, enfisema, bronquitis crónica) |
| Nueva Indicación Predicha | Enfermedad trombótica |
| Puntaje de Predicción TxGNN | 99,62% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

La teofilina es un inhibidor no selectivo de fosfodiesterasas (PDE) y un antagonista de los receptores de adenosina (A1, A2A, A2B y A3). En las plaquetas, la inhibición de PDE eleva el AMPc, un mecanismo que en teoría reduce la activación y agregación plaquetaria.

La relación con la indicación original es indirecta. El uso respiratorio se apoya en la broncodilatación, no en efectos antitrombóticos. La hipótesis es plausible desde la biología plaquetaria, pero la literatura recuperada no la pone a prueba en pacientes. El puntaje alto de TxGNN (0,996) es solo una predicción del grafo y no sustituye a la evidencia clínica.

El único dato experimental cercano es un modelo canino de trombosis coronaria, donde la aminofilina potenció el efecto antitrombótico de la prostaciclina. Es un estudio preclínico de 1983 con un derivado de la teofilina.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

No se identificaron ECA ni estudios clínicos de teofilina en enfermedad trombótica. La lista siguiente muestra los resultados más cercanos al tema; la mayoría son indirectos.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6313894](https://pubmed.ncbi.nlm.nih.gov/6313894/) | 1983 | Preclínico (modelo canino) | J Pharmacol Exp Ther | La aminofilina potenció el efecto antitrombótico de la prostaciclina en trombosis coronaria inducida en perros |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Estudio in vitro | Gen Pharmacol | Milrinona y adenosina inhiben la respuesta plaquetaria humana a través del AMPc; no evalúa teofilina como tratamiento |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Revisión | CRC Crit Rev Biochem | Equilibrio entre tromboxano A2 y prostaciclina en plaquetas y aterosclerosis; contexto mecanístico general |
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Revisión | Clin Pharmacokinet | Farmacocinética de la ticlopidina, un antiagregante; no trata de teofilina |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Método analítico | Br J Haematol | La teofilina se usa como componente del anticoagulante para medir el factor plaquetario 4; es un uso de laboratorio |
| [15475744](https://pubmed.ncbi.nlm.nih.gov/15475744/) | 2004 | Cohorte | Inflamm Bowel Dis | Agregados plaqueta-leucocito en enfermedad inflamatoria intestinal; relación indirecta |
| [21719422](https://pubmed.ncbi.nlm.nih.gov/21719422/) | 2011 | Cohorte | Rheumatology (Oxford) | Activación plaquetaria y de neutrófilos en la enfermedad de Behçet; relación indirecta |
| [6241135](https://pubmed.ncbi.nlm.nih.gov/6241135/) | 1984 | Estudio observacional | Cor Vasa | Subtipos de linfocitos T resistentes a teofilina, más frecuentes en infarto y tromboflebitis; es un marcador inmunológico, no un efecto terapéutico |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | Método analítico | Platelets | Medición de sCLEC-2 como marcador de activación plaquetaria; no evalúa teofilina |
| [26764324](https://pubmed.ncbi.nlm.nih.gov/26764324/) | 2016 | Estudio in vitro | J Nutr | El extracto de ajo envejecido inhibe la agregación plaquetaria; no evalúa teofilina |

## Información de Mercado en España

Se listan 5 de las 6 autorizaciones registradas. Los textos de indicación aprobada no constan en los datos recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1891 | EUFILINA VENOSA 200 mg SOLUCIÓN INYECTABLE | Solución inyectable | No disponible |
| 56165 | THEO-DUR 200 mg COMPRIMIDOS DE LIBERACION PROLONGADA | Comprimido de liberación prolongada | No disponible |
| 56166 | THEO-DUR 300 mg COMPRIMIDOS DE LIBERACION PROLONGADA | Comprimido de liberación prolongada | No disponible |
| 45303 | ELIXIFILIN 5,33 MG/ML SOLUCION ORAL | Solución oral | No disponible |
| 31900 | TEROMOL RETARD 300 MG COMPRIMIDOS DE LIBERACIÓN PROLONGADA | Comprimido de liberación prolongada | No disponible |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos de AEMPS sobre advertencias y contraindicaciones no están disponibles.

Como referencia, en el análisis de otra indicación predicha (enfermedad pulmonar obstructiva) se señalaron como salvaguardas el margen terapéutico estrecho, la monitorización de niveles séricos y las interacciones vinculadas a CYP1A2 (por ejemplo, macrólidos y fluoroquinolonas).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para enfermedad trombótica no cuenta con ensayos clínicos ni con literatura que pruebe directamente la teofilina en trombosis (nivel L5). El único apoyo es un mecanismo plausible (inhibición de PDE y aumento de AMPc plaquetario) y un estudio preclínico antiguo con aminofilina.

**Para avanzar se necesita:**
- Estudios preclínicos o in vitro que evalúen la teofilina en agregación plaquetaria y trombosis.
- Descargar y analizar el prospecto de AEMPS para completar advertencias, contraindicaciones e indicaciones autorizadas.
- Consolidar los datos de mecanismo de acción de DrugBank.
- Evaluar el balance riesgo-beneficio, dado el margen terapéutico estrecho de la teofilina.

Entre las demás predicciones del modelo, la enfermedad pulmonar obstructiva (nivel L1, Proceed with Guardrails) corresponde en la práctica a una indicación ya establecida. La enfermedad de la cavidad nasal (nivel L2) es la candidata con más respaldo clínico entre las que suponen un reposicionamiento real.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Fulvestrant
parent: Solo predicción del modelo (L5)
nav_order: 251
evidence_level: L5
indication_count: 10
---

# Fulvestrant
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

# Fulvestrant: De Cáncer de Mama con Receptores Hormonales Positivos a Infección por VIH

## Resumen en Una Frase

Fulvestrant es un antagonista y degradador del receptor de estrógenos, utilizado en el cáncer de mama con receptores hormonales positivos (indicación tomada del análisis del Evidence Pack, no del texto de las autorizaciones de la AEMPS, que está vacío).
El modelo TxGNN predice que podría ser efectivo para **infección por VIH**, pero actualmente hay **0 ensayos clínicos** y **1 publicación** que no trata sobre VIH (estudia HTLV-1), por lo que la predicción carece de respaldo real.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de mama con receptores hormonales positivos (según el análisis del Evidence Pack; las autorizaciones de la AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Infección por VIH |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 17 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Fulvestrant es un antagonista y degradador del receptor de estrógenos. Se usa de forma establecida en el cáncer de mama con receptores hormonales positivos. No se dispone de datos detallados del mecanismo de acción en DrugBank para este informe.

Con los datos aportados, **no se puede establecer una relación mecanística** entre el bloqueo del receptor de estrógenos y una acción antiviral contra el VIH. El puntaje alto proviene únicamente de la predicción del grafo de conocimiento y no de evidencia específica del fármaco.

Esta predicción debe leerse con cautela. Un puntaje del 99.91% no implica eficacia clínica. La única publicación asociada trata sobre la mielopatía asociada a HTLV-1, un retrovirus distinto, y no aporta evidencia sobre VIH.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Análisis multi-ómico de cohortes (preprint) | Research Square | Análisis de biología de sistemas sobre la mielopatía asociada a HTLV-1 y sus dianas terapéuticas. No estudia VIH ni fulvestrant, por lo que su relevancia es indirecta. |

---

## Información de Mercado en España

Se muestran 5 de las 17 autorizaciones registradas.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 84420 | Fulvestrant Stada 250 mg solución inyectable en jeringa precargada EFG | Solución inyectable | — |
| 87273 | Fulvestrant Hikma 250 mg solución inyectable en jeringa precargada EFG | Solución inyectable en jeringa precargada | — |
| 1171253001 | Fulvestrant Mylan 250 mg solución inyectable en jeringa precargada EFG | Solución inyectable | — |
| 80910 | Fulvestrant Teva 250 mg solución inyectable en jeringa precargada EFG | Solución inyectable en jeringa precargada | — |
| 83884 | Strantas 250 mg solución inyectable en jeringa precargada EFG | Solución inyectable | — |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia hormonal dirigida (antagonista y degradador del receptor de estrógenos); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para VIH se apoya solo en el modelo TxGNN (L5). No hay ensayos clínicos, la única publicación trata sobre otro virus, y no existe un vínculo mecanístico sustentado. Además, no se han revisado aún las advertencias ni contraindicaciones de la AEMPS.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de la AEMPS para obtener advertencias, contraindicaciones y el texto de indicación aprobada.
- Obtener el mecanismo de acción desde DrugBank para evaluar un posible vínculo con el VIH.
- Buscar evidencia preclínica (in vitro o en modelos animales) específica de fulvestrant en VIH antes de plantear cualquier estudio.
- Como alternativa, valorar otras predicciones del mismo fármaco. La artritis reumatoide (L4) tiene una justificación preclínica plausible pero no probada, con dirección del efecto incierta. La predicción de "neoplasia endocrina múltiple" parece un artefacto de mapeo de términos, ya que los ensayos encontrados son de cáncer de mama y no de síndromes MEN.

---

*Este informe es solo para referencia de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


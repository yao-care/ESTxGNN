---
layout: default
title: Fulvestrant
parent: Evidencia moderada (L3-L4)
nav_order: 365
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-28
description: "Fulvestrant: nueva indicación predicha, Infección por VIH (nivel de evidencia L4). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "FULVESTRANT"
predicted_indications: ["HIV infectious disease", "multiple endocrine neoplasia", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "rheumatoid arthritis", "acne (disease)", "brachydactyly-syndactyly syndrome", "hemoglobinopathy", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Fulvestrant
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

## Fulvestrant: De Indicación Original No Especificada a Infección por VIH
{: .text-alpha }

## Resumen en Una Frase

Fulvestrant es un antagonista y degradador selectivo del receptor de estrógenos, comercializado en España en inyección precargada de 250 mg. Los datos compilados no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **infección por VIH**, pero la evidencia se limita a **2 publicaciones** (una sobre un virus distinto, el HTLV-1, y otra de laboratorio) y **ningún ensayo clínico**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Infección por VIH |
| Puntaje de Predicción TxGNN | 0.9991 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | Comercializado (registros vigentes: 12 de 17) |
| Número de Autorizaciones | 17 (vigentes: 12) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Por conocimiento general, fulvestrant es un degradador selectivo del receptor de estrógenos (SERD) que bloquea y promueve la degradación del receptor de estrógenos alfa (ERα). Se utiliza en cáncer de mama con receptores hormonales positivos, aunque este uso no figura en los textos de indicación de las autorizaciones españolas recopiladas.

La hipótesis para el VIH es que ERα se expresa en los linfocitos T CD4+ y podría influir en la transcripción y la latencia del virus. Un estudio in vitro reciente (PMID 42430506) analiza el efecto de ligandos del receptor, entre ellos fulvestrant, y de agentes que revierten la latencia sobre ERα en estas células. Es un indicio plausible, pero preclínico e indirecto.

El otro artículo (PMID 40343334) trata del HTLV-1, un retrovirus distinto, y solo guarda una relación lejana con la predicción. No hay datos que demuestren beneficio clínico en personas con VIH.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [42430506](https://pubmed.ncbi.nlm.nih.gov/42430506/) | 2026 | Estudio in vitro / mecanístico | JCI Insight | Evalúa el efecto del estrógeno, de fulvestrant y de agentes reversores de la latencia del VIH sobre ERα en linfocitos T CD4+ |
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Análisis multiómico de cohortes (HTLV-1, no VIH) | Research Square | Análisis de mecanismos de la mielopatía asociada a HTLV-1; relación solo indirecta con el VIH |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 03269001 | FASLODEX 250 mg/5 ml solución inyectable | Solución inyectable en jeringa precargada | No disponible |
| 03269001IP | FASLODEX 250 mg solución inyectable | Solución inyectable en jeringa precargada | No disponible |
| 84420 | Fulvestrant Stada 250 mg solución inyectable en jeringa precargada EFG | Solución inyectable | No disponible |
| 87273 | Fulvestrant Hikma 250 mg solución inyectable en jeringa precargada EFG | Solución inyectable en jeringa precargada | No disponible |
| 80910 | Fulvestrant Teva 250 mg solución inyectable en jeringa precargada EFG | Solución inyectable en jeringa precargada | No disponible |

Se muestran 5 de las 17 autorizaciones vigentes (todas de medicamento monofármaco).

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia endocrina dirigida (degradador selectivo del receptor de estrógenos); no es citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; las contraindicaciones del grafo de conocimiento sugieren vigilar la función hepática y los parámetros de coagulación y plaquetas |
| Protección en Manejo | Consultar el prospecto y las regulaciones locales de manejo |

## Consideraciones de Seguridad

- **Contraindicaciones inferidas del grafo de conocimiento (no proceden del prospecto)**: enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia y trastornos de la coagulación sanguínea.
- **Interacciones farmacológicas**: se identificaron 92 posibles interacciones, todas con nivel de gravedad desconocido. Entre las más relevantes figuran warfarina, ácido acetilsalicílico, dexametasona, prednisona, metformina, simvastatina, bupropión, ondansetrón, omeprazol y pantoprazol. Conviene prestar especial atención a warfarina y ácido acetilsalicílico dado el posible riesgo hemorrágico.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de VIH tiene una puntuación alta (0.9991), pero la evidencia es solo preclínica e indirecta (nivel L4), sin ensayos clínicos. Además, no se dispone del prospecto con advertencias y contraindicaciones, lo que impide completar el cribado de seguridad. Las demás predicciones son aún más débiles: el ranking 2 (neoplasia endocrina múltiple) se basa en ensayos de cáncer de mama sin relación real, y la artritis reumatoide muestra evidencia parcialmente contradictoria, ya que el bloqueo de estrógenos agravó la inflamación en un modelo animal.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas).
- Obtener datos del mecanismo de acción desde DrugBank.
- Estudios in vitro y en modelos animales que confirmen el efecto de fulvestrant sobre la latencia del VIH.
- Valoración de la ruta de administración (inyección intramuscular) frente a las necesidades terapéuticas en VIH, que requieren tratamiento crónico.
- Evaluación de los posibles efectos de la supresión estrogénica en poblaciones con VIH, especialmente mujeres.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


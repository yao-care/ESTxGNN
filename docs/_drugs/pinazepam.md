---
layout: default
title: Pinazepam
parent: Evidencia moderada (L3-L4)
nav_order: 639
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-14
description: "Pinazepam: nueva indicación predicha, Insomnio (nivel de evidencia L4). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "PINAZEPAM"
predicted_indications: ["insomnia (disease)", "alcohol withdrawal delirium", "antidepressant type abuse", "hallucinogen abuse", "barbiturate abuse", "anxiety", "sleep disorder, initiating and maintaining sleep"]
---

# Pinazepam
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **7** 
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

# Pinazepam: De Indicación Original No Especificada a Insomnio

## Resumen en Una Frase

Pinazepam es una benzodiazepina que actúa como profármaco de la N-desmetildiazepam (nordazepam), comercializada en España, aunque los datos compilados no recogen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **insomnio**, con un puntaje muy alto pero **sin ensayos clínicos ni publicaciones** específicos para esta indicación.
La evidencia se limita a la predicción del modelo y a la plausibilidad mecanística de la clase.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99,95% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen una descripción detallada del mecanismo de acción en la ficha del fármaco. Según la información farmacológica conocida y la literatura revisada, pinazepam es una 1,4-benzodiazepina con un grupo propargilo en la posición N-1. Actúa como profármaco: se convierte en N-desmetildiazepam, un metabolito de acción prolongada que modula positivamente de forma alostérica los receptores GABA-A.

Este mecanismo sustenta los efectos ansiolíticos, sedantes e hipnóticos de la clase. Por ello, la relación con el insomnio es mecanísticamente plausible. La larga duración del metabolito activo podría favorecer el mantenimiento del sueño, pero también plantea el riesgo de sedación residual al día siguiente.

Conviene señalar que el insomnio es probablemente un uso coherente con la ficha de una benzodiazepina comercializada, más que un reposicionamiento genuino. Además, el puntaje elevado de TxGNN es solo una predicción del modelo, sin estudios específicos en esta indicación.

### Otras indicaciones predichas (contexto)

| Indicación predicha | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|
| Delirio por abstinencia alcohólica | 99,68% | L5 | Las benzodiazepinas son tratamiento estándar; apoyo solo por extrapolación de clase |
| Abuso de antidepresivos | 99,46% | L5 | Sin fundamento mecanístico claro; probable artefacto del grafo de conocimiento |
| Abuso de alucinógenos | 99,46% | L5 | Solo uso sintomático de la agitación; no trata el trastorno |
| Abuso de barbitúricos | 99,46% | L5 | Tolerancia cruzada vía GABA-A; plausibilidad solo de clase |
| Ansiedad | 99,34% | L4 | Literatura farmacológica y de revisión; probablemente indicación original |
| Trastorno del sueño (inicio y mantenimiento) | 99,04% | L4 | Mismo mecanismo que el insomnio |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para insomnio.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para insomnio.

Como referencia, para la indicación de **ansiedad** (rango 6) se recuperaron 20 publicaciones, todas de carácter farmacológico, farmacocinético o toxicológico. Las más relevantes:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6147192](https://pubmed.ncbi.nlm.nih.gov/6147192/) | 1984 | Revisión | Clin Ther | Revisión de propiedades farmacológicas y eficacia terapéutica; menor toxicidad que diazepam y efecto hipnótico y de deterioro motor limitados |
| [28903606](https://pubmed.ncbi.nlm.nih.gov/28903606/) | 2017 | Revisión | Drug Metab Rev | Perfil metabólico de oxazepam y benzodiazepinas relacionadas, incluida pinazepam |
| [26359](https://pubmed.ncbi.nlm.nih.gov/26359/) | 1978 | Preclínico | Arzneimittelforschung | En ratas, pinazepam fue más de dos veces más activo que diazepam en reducir la respuesta emocional condicionada |
| [240369](https://pubmed.ncbi.nlm.nih.gov/240369/) | 1975 | Preclínico | Arzneimittelforschung | Menor toxicidad y menor actividad hipnótica y miorrelajante que diazepam |
| [6809477](https://pubmed.ncbi.nlm.nih.gov/6809477/) | 1982 | Farmacología | Eur J Clin Pharmacol | Pinazepam actúa como profármaco de N-desmetildiazepam en voluntarios sanos |
| [6147314](https://pubmed.ncbi.nlm.nih.gov/6147314/) | 1983 | Farmacocinética | Int J Clin Pharmacol Res | Cinética tras dosis oral única de 10 mg en seis voluntarios sanos |
| [6150857](https://pubmed.ncbi.nlm.nih.gov/6150857/) | 1984 | Farmacocinética | Eur J Clin Pharmacol | Transferencia placentaria en 25 mujeres a término |
| [2569399](https://pubmed.ncbi.nlm.nih.gov/2569399/) | 1989 | Farmacocinética | Eur J Drug Metab Pharmacokinet | Transferencia placentaria y distribución en conejas gestantes y fetos |
| [6124406](https://pubmed.ncbi.nlm.nih.gov/6124406/) | 1982 | Preclínico | Drug Metab Dispos | Disposición y efecto de primer paso hepático en rata |
| [12907](https://pubmed.ncbi.nlm.nih.gov/12907/) | 1976 | Ensayo abierto | Clin Ter | Ensayo clínico abierto con pinazepam (sin resumen disponible) |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 53884 | DUNA 2,5 mg cápsulas duras | Cápsula dura | No disponible en los datos compilados |
| 53885 | DUNA 5 mg cápsulas duras | Cápsula dura | No disponible en los datos compilados |
| 53886 | DUNA 10 mg cápsulas duras | Cápsula dura | No disponible en los datos compilados |

Titular: Meiji Pharma Spain S.A. Las tres autorizaciones son monofármaco y están vigentes.

---

## Consideraciones de Seguridad

Consultar el prospecto para obtener información de seguridad.

Como aspectos generales de la clase, que no proceden de la ficha del producto: la literatura y el análisis del modelo señalan el potencial de abuso y dependencia de las benzodiazepinas, así como el riesgo de sedación residual por el metabolito de acción prolongada. Los datos incluyen además estudios de transferencia placentaria (humana y animal), relevantes para el uso en el embarazo. No se encontraron interacciones farmacológicas registradas en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
El insomnio se apoya solo en la predicción del modelo y en la plausibilidad mecanística de la clase (nivel L4), sin ensayos ni literatura específicos. Además, probablemente corresponde a un uso ya acorde con la ficha de una benzodiazepina comercializada, por lo que no constituye un reposicionamiento genuino.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (indicaciones aprobadas, advertencias y contraindicaciones), un vacío de datos bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar si insomnio y ansiedad ya constan en la ficha técnica española.
- Buscar ensayos clínicos y literatura específicos de pinazepam en insomnio.
- Evaluar de forma explícita el riesgo de dependencia, abuso y sedación residual antes de cualquier avance.
- Descartar las predicciones de abuso de sustancias (antidepresivos, alucinógenos, barbitúricos), que parecen artefactos del grafo de conocimiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


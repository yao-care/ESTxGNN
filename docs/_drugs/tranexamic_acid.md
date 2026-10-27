---
layout: default
title: Tranexamic Acid
parent: Evidencia moderada (L3-L4)
nav_order: 813
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Tranexamic Acid: nueva indicación predicha, Amenorrea (nivel de evidencia L4). Indicación original: Endometriosis (según el grafo de conocimiento"
monitor_inn: "tranexamic acid"
predicted_indications: ["amenorrhea (disease)"]
---

# Tranexamic Acid
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **1** 
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

## Ácido tranexámico: De Endometriosis a Amenorrea
{: .text-alpha }

## Resumen en Una Frase

El ácido tranexámico es un antifibrinolítico utilizado originalmente en el contexto de la endometriosis (según las indicaciones del grafo de conocimiento) y comercializado en España en múltiples formulaciones.
El modelo TxGNN predice que podría ser efectivo para **Amenorrea**, pero actualmente no hay ensayos clínicos registrados y solo **2 publicaciones** (ambas revisiones) abordan el tema de forma indirecta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Endometriosis (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99,19% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 10 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, el ácido tranexámico es un antifibrinolítico, análogo de la lisina, que bloquea la unión del plasminógeno a la fibrina y reduce el sangrado menstrual abundante.

Sin embargo, **la plausibilidad biológica de esta predicción es baja**. La amenorrea (ausencia de menstruación) es lo opuesto a un trastorno hemorrágico, por lo que un vínculo terapéutico directo es poco creíble. La única conexión razonable es indirecta: en pacientes con trastornos de la coagulación, con anticoagulación o con neoplasias hematológicas, el ácido tranexámico puede formar parte de un régimen de profilaxis o supresión de la menstruación junto con agentes hormonales, reduciendo el sangrado, no tratando la amenorrea en sí.

El puntaje elevado de TxGNN (0,99) probablemente refleja la proximidad en el grafo de conocimiento entre trastornos menstruales (endometriosis, sangrado uterino anormal) y no una señal terapéutica real. La falta de datos de mecanismo de acción original limita una validación mecanística adicional.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Revisión | Menopause | Revisión de terapias farmacológicas para el sangrado uterino anormal; los agentes no hormonales son eficaces y generalmente bien tolerados, y la elección depende de la etiología, la cantidad de sangrado, la necesidad de anticoncepción y el estado perimenopáusico |
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Revisión | J Oncol Pharm Pract | Abordaje sistemático de la profilaxis y supresión de la menstruación en pacientes premenopáusicas con cáncer hematológico; escasez de datos comparativos entre terapias |

Ninguna de las dos publicaciones evalúa el ácido tranexámico como tratamiento de la amenorrea.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 53940 | AMCHAFIBRIN 500 mg COMPRIMIDOS | Comprimido | No disponible |
| 89608 | TANTIRAMIX 500 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible |
| 85520 | ÁCIDO TRANEXÁMICO BAXTER 100 MG/ML SOLUCIÓN INYECTABLE EFG | Solución inyectable y para perfusión | No disponible |
| 80781 | ÁCIDO TRANEXÁMICO ZENTIVA 500 mg COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | Comprimido recubierto con película | No disponible |
| 83427 | ÁCIDO TRANEXÁMICO AUROVITAS 100 MG/ML SOLUCIÓN INYECTABLE EFG | Solución inyectable | No disponible |

Se muestran 5 de las 10 autorizaciones vigentes (todas de principio activo único).

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): hipertensión, trastornos de ansiedad, porfiria, enfermedad hepática y de la vesícula biliar, hiperglucemia y diabetes mellitus (incluida la cetoacidosis diabética), edema cerebral, hipertrigliceridemia e hiperlipidemia, carcinoma de mama femenino, tromboflebitis, migraña, enfermedad coronaria, obesidad, cáncer de endometrio, ictus y trastornos cerebrovasculares.
- **Interacciones farmacológicas** (35 registradas; se muestran las principales):
  - **Mayor**: estrógenos y anticonceptivos hormonales (etinilestradiol, estradiol, estrógenos conjugados, noretisterona, drospirenona, etonogestrel, dietilestilbestrol, estrona, estramustina), complejo coagulante anti-inhibidor, complejo de factor IX humano y carfilzomib.
  - **Moderada**: alteplasa y anistreplasa (trombolíticos, por efecto farmacodinámico opuesto).

Destaca el riesgo trombótico al combinar con estrógenos o progestágenos, relevante porque el régimen de supresión menstrual suele incluir agentes hormonales. Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (nivel L4), sin ensayos clínicos y con literatura indirecta. Además, el mecanismo antifibrinolítico es biológicamente contrario a la naturaleza de la amenorrea, por lo que el puntaje alto probablemente es un artefacto del grafo de conocimiento.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones oficiales), lo cual es un requisito bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar las indicaciones aprobadas en España, ausentes en los datos actuales.
- Reevaluar si el objetivo real es la supresión del sangrado menstrual en poblaciones específicas (por ejemplo, cáncer hematológico) y, de ser así, replantear la indicación y buscar estudios que la respalden.
- Evaluar el riesgo trombótico en combinación con terapias hormonales.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


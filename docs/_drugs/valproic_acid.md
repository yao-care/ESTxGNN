---
layout: default
title: Valproic Acid
parent: Solo predicción del modelo (L5)
nav_order: 837
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Valproic Acid: nueva indicación predicha, Neoplasia del nervio trigémino (nivel de evidencia L5). Indicación original: Epilepsia, trastorno bipolar maníaco…"
monitor_inn: "Valproic acid"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "micturation-induced seizures", "thinking seizures", "orgasm-induced seizures", "eating seizures", "audiogenic seizures", "reading seizures"]
---

# Valproic Acid
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

# Ácido valproico: De Epilepsia a Neoplasia del Nervio Trigémino

## Resumen en Una Frase

El ácido valproico es un fármaco antiepiléptico de amplio espectro, utilizado originalmente para el tratamiento de la epilepsia, la epilepsia de ausencia y los episodios maníacos del trastorno bipolar.
El modelo TxGNN predice que podría ser efectivo para **neoplasia del nervio trigémino**, pero actualmente **no hay ensayos clínicos** y solo **1 publicación** (una serie de casos sobre el síndrome de Sturge-Weber, que no trata de esta indicación) está vinculada a la predicción. La evidencia es, en la práctica, solo la predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Epilepsia, trastorno bipolar maníaco, epilepsia de ausencia (según el grafo de conocimiento; el texto de indicación de las autorizaciones españolas no está disponible) |
| Nueva Indicación Predicha | Neoplasia del nervio trigémino |
| Puntaje de Predicción TxGNN | 99,97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 14 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el ácido valproico es un antiepiléptico de amplio espectro cuya eficacia en epilepsia está bien establecida. Su acción antiepiléptica se atribuye al refuerzo de la transmisión GABAérgica, al bloqueo de canales de sodio y a la modulación de canales de calcio tipo T. Además, es un inhibidor de la histona desacetilasa (HDAC1 figura como diana en los datos farmacológicos), y esta propiedad se investiga como estrategia en diversos cánceres e infección por VIH.

La relación entre la indicación original y la nueva es débil. La epilepsia es un trastorno neurológico funcional, mientras que la neoplasia del nervio trigémino es un tumor. El único vínculo mecanístico plausible es el efecto antitumoral preclínico de los inhibidores de HDAC, que es teórico y para el cual no se aporta evidencia específica en tumores del trigémino.

La única publicación vinculada (PMID 9157801) es una serie de 14 casos de síndrome de Sturge-Weber de 1997, un trastorno neurocutáneo vascular en el que el valproato se usa solo para controlar las convulsiones. No respalda la predicción. El puntaje alto del modelo parece reflejar la cercanía en el grafo de conocimiento con trastornos neurológicos, no evidencia real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Serie de casos | Anales Españoles de Pediatría | Revisión de 14 casos de síndrome de Sturge-Weber en 25 años (características clínicas, evolución y respuesta terapéutica). No aborda tumores del nervio trigémino. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 84514 | Ácido valproico Aurobindo 300 mg comprimidos de liberación prolongada EFG | Comprimido de liberación prolongada | No disponible |
| 60350 | Depakine Crono 500 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada | No disponible |
| 60352 | Depakine 100 mg/ml polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | No disponible |
| 48828 | Depakine 200 mg/ml solución oral | Solución oral | No disponible |
| 68033 | Ácido valproico Altan 400 mg polvo para solución inyectable EFG | Polvo para solución inyectable | No disponible |

Se muestran 5 de las 14 autorizaciones vigentes (todas de principio activo único, ninguna cancelada).

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): trastornos de ansiedad, trastornos neuróticos, trastorno distímico, deficiencia de carbamoil fosfato sintetasa I, porfiria hereditaria y trastornos del metabolismo de porfirinas, enfermedad renal, piouréter, hiperargininemia, enfermedades hematológicas, pancreatitis, citrulinemia, trastorno cognitivo, enfermedad hepática, enfermedad de la vesícula biliar y trombocitopenia.
- **Interacciones farmacológicas**: la consulta se completó con un único registro, que corresponde a la interacción farmacológica con su diana HDAC1 (inhibición de histona desacetilasa 1), no a una interacción con otro medicamento.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5): no hay ensayos clínicos y la única publicación vinculada no trata de tumores del trigémino. Además, el perfil de contraindicaciones (hepáticas, hematológicas, pancreáticas) exige cautela en un contexto oncológico.

**Para avanzar se necesita:**
- Evidencia preclínica específica del efecto de inhibidores de HDAC/ácido valproico en tumores del nervio trigémino o tumores relacionados.
- Datos del mecanismo de acción y de advertencias y contraindicaciones del prospecto de la AEMPS.
- Una revisión de la literatura más específica sobre tumores del trigémino, ya que la publicación actual no es pertinente.
- Evaluación de seguridad para poblaciones con enfermedad hepática, trombocitopenia o riesgo de pancreatitis.

> Nota: entre las demás predicciones, la **neuralgia del trigémino** (puntaje 99,83%, nivel L4) y la **epilepsia de sobresalto** (puntaje 99,81%, nivel L3) cuentan con más respaldo bibliográfico. La epilepsia visual (L3) cae esencialmente dentro de la indicación existente de epilepsia, por lo que no es un reposicionamiento genuino.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


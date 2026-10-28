---
layout: default
title: Rasburicase
parent: Solo predicción del modelo (L5)
nav_order: 685
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Rasburicase: nueva indicación predicha, Hipouricemia renal (nivel de evidencia L5). Indicación original: Hiperuricemia (enfermedad obsoleta…"
monitor_inn: "rasburicase"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "hepatic porphyria", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "primitive portal vein thrombosis", "hepatopulmonary syndrome", "hepatoportal sclerosis", "renal tubular acidosis", "disorder of phenylalanine metabolism"]
---

# Rasburicase
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Rasburicasa: De Hiperuricemia (obsoleta) a Hipouricemia Renal
{: .text-alpha }

## Resumen en Una Frase

Rasburicasa es una urato oxidasa recombinante, originalmente utilizada para el tratamiento de la hiperuricemia.
El modelo TxGNN predice que podría ser efectiva para **hipouricemia renal**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; además, el análisis mecanístico sugiere que esta predicción es, en realidad, una señal de contraindicación y no una oportunidad de reposicionamiento.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperuricemia (enfermedad obsoleta, según la base de conocimiento TxGNN; el texto de indicación aprobado por la AEMPS no está disponible) |
| Nueva Indicación Predicha | Hipouricemia renal |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 2) |
| Número de Autorizaciones | 2 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados en las fuentes consultadas. Según la información conocida, la rasburicasa es una enzima urato oxidasa recombinante que convierte el ácido úrico en alantoína, más soluble, con lo que reduce el ácido úrico sérico. Su eficacia en la hiperuricemia es el fundamento de su uso original.

Sin embargo, en este caso **la predicción no resulta mecanísticamente razonable**. La hipouricemia renal es un estado de ácido úrico sérico ya bajo, causado por un defecto en la reabsorción renal de urato (por ejemplo, variantes de SLC22A12/URAT1 o SLC2A9). Reducir aún más el ácido úrico no trataría la enfermedad y podría empeorarla, además de añadir riesgo de lesión renal aguda inducida por el ejercicio.

El puntaje elevado de TxGNN (0.9999 para Hipouricemia renal) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas (vía compartida del ácido úrico), no evidencia biológica ni una justificación terapéutica plausible. Debe interpretarse como una **señal de contraindicación mecanística**, no como una oportunidad de reposicionamiento.

### Otras predicciones del modelo

Las demás indicaciones predichas también tienen nivel de evidencia L5, sin ensayos ni literatura, y recomendación Hold:

| Indicación predicha | Puntaje TxGNN | Valoración mecanística |
|------|------|------|
| Deficiencia parcial de hipoxantina-guanina fosforribosiltransferasa | 0.9997 | Único vínculo biológicamente coherente (reducción aguda del ácido úrico), pero la rasburicasa es una proteína inmunógena de uso corto (1-5 días), mientras que la enfermedad es crónica y se maneja con alopurinol o febuxostat; tampoco actúa sobre la hipoxantina y la xantina acumuladas |
| Porfiria hepática | 0.9997 | Sin vínculo mecanístico claro |
| Cirrosis idiopática asociada al cobre | 0.9997 | Sin vínculo plausible; el peróxido de hidrógeno generado podría añadir estrés oxidativo teórico |
| Hipertensión portal no cirrótica familiar de inicio temprano | 0.9997 | Sin vínculo mecanístico |
| Trombosis primitiva de la vena porta | 0.9997 | Sin vínculo; la rasburicasa no tiene acción antitrombótica |
| Síndrome hepatopulmonar | 0.9997 | Sin vínculo mecanístico |
| Esclerosis hepatoportal | 0.9997 | Sin vínculo mecanístico |
| Acidosis tubular renal | 0.9985 | Sin vínculo directo; riesgo adicional de hemólisis y metahemoglobinemia en deficiencia de G6PD |
| Trastorno del metabolismo de la fenilalanina | 0.9983 | Sin vínculo mecanístico |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 00170002 | FASTURTEC 1,5 MG/ML polvo y disolvente para concentrado para solución para perfusión | Polvo y disolvente para concentrado para solución para perfusión | No disponible en los datos compilados |
| 00170001 | FASTURTEC 1,5 MG/ML polvo y disolvente para concentrado para solución para perfusión | Polvo y disolvente para concentrado para solución para perfusión | No disponible en los datos compilados |

Ambas autorizaciones están vigentes y corresponden a monofármaco (fabricante: Sanofi Winthrop Industrie).

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (13 registradas): 
  - **Mayores**: prilocaína y ácido nitroso (riesgo asociado probablemente a metahemoglobinemia).
  - **Moderadas**: anestésicos locales tópicos/oftálmicos/nasales (tetracaína oftálmica y tópica, lidocaína tópica y oftálmica, benzocaína, cocaína tópica y nasal, proparacaína, oxibuprocaína, cinchocaína) e idelalisib.
- **Riesgo mecanístico relacionado con la nueva indicación**: en hipouricemia renal, la reducción adicional del ácido úrico podría empeorar el cuadro y aumentar el riesgo de lesión renal aguda por ejercicio. En otras predicciones se señala el riesgo de hemólisis y metahemoglobinemia en deficiencia de G6PD.

Para advertencias y contraindicaciones formales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos ni literatura, y el análisis mecanístico indica que reducir más el ácido úrico en la hipouricemia renal carece de lógica terapéutica y podría ser perjudicial. Ninguna de las otras nueve indicaciones predichas presenta un respaldo que justifique avanzar.

**Para avanzar se necesita:**
- Descartar formalmente la hipouricemia renal como candidata y registrarla como señal de contraindicación mecanística.
- Obtener el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada), actualmente pendiente.
- Obtener datos del mecanismo de acción desde DrugBank.
- Si se desea explorar la deficiencia parcial de HPRT, revisar la literatura sobre uso agudo de rasburicasa y evaluar inmunogenicidad y alternativas establecidas (alopurinol, febuxostat).
- Verificar la compatibilidad de vía de administración (actualmente pendiente) y la similitud con la indicación original.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


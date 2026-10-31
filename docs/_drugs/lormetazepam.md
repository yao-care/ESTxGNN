---
layout: default
title: Lormetazepam
parent: Evidencia alta (L1-L2)
nav_order: 485
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-31
description: "Lormetazepam: nueva indicación predicha, Insomnio (nivel de evidencia L1). Indicación original: No disponible en los textos de autorización compilados (el uso hipnót…"
monitor_inn: "LORMETAZEPAM"
predicted_indications: ["insomnia (disease)", "alcohol withdrawal delirium", "hallucinogen abuse", "barbiturate abuse", "antidepressant type abuse", "anxiety", "cauda equina syndrome", "anxiety disorder", "sleep disorder, initiating and maintaining sleep", "benign paroxysmal torticollis of infancy"]
---

# Lormetazepam
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
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

## Lormetazepam: De Insomnio a Insomnio (Indicación ya establecida)
{: .text-alpha }

## Resumen en Una Frase

Lormetazepam es una benzodiazepina hipnótica comercializada en España, cuya indicación original no figura en el texto de las autorizaciones compiladas, pero que se utiliza clásicamente para el insomnio.
El modelo TxGNN predice como primera indicación el **insomnio**, con **2 ensayos clínicos** y **3 publicaciones** directamente asociados. Es una indicación ya establecida, por lo que no se trata de un reposicionamiento en sentido estricto.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los textos de autorización compilados (el uso hipnótico para el insomnio se deduce del perfil del fármaco) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 17) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, lormetazepam es una benzodiazepina que modula positivamente los receptores GABA-A, lo que produce efectos sedante-hipnóticos. Esto coincide directamente con el tratamiento del insomnio.

La predicción del insomnio no es un reposicionamiento real: es el uso establecido y comercializado del fármaco. El modelo TxGNN, por tanto, redescubre la indicación conocida, y está respaldada por ensayos de fase 3 con comparador activo.

Otras predicciones del modelo (ansiedad, trastorno de ansiedad, trastorno del sueño de inicio y mantenimiento) son mecanísticamente plausibles por el mismo efecto GABAérgico. Varias de las demás (abuso de alucinógenos, síndrome de cauda equina, tortícolis paroxística benigna de la infancia) carecen de fundamento mecanístico creíble; sus puntuaciones provienen del modelo TxGNN (deep learning) y pueden reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00679900](https://clinicaltrials.gov/study/NCT00679900) | Fase 3 | Completado | 283 | Eplivanserina 5 mg vs lormetazepam 1 mg durante 4 semanas en insomnio primario crónico con dificultad de mantenimiento del sueño; compara somnolencia matutina, seguridad, insomnio de rebote y abstinencia |
| [NCT00788515](https://clinicaltrials.gov/study/NCT00788515) | Fase 3 | Terminado | 33 | Volinanserina 2 mg vs lormetazepam 1 mg en insomnio de mantenimiento; terminado antes de tiempo, con poca potencia estadística |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | ECA | J Int Med Res | Lormetazepam 1 mg superó a diazepam 5 mg en reducir la latencia del sueño y prolongar el sueño ininterrumpido en 100 pacientes ambulatorios |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Revisión | Acta Psychiatr Scand Suppl | Uso clínico de hipnóticos y necesidad de contar con distintos perfiles farmacocinéticos |
| [2873832](https://pubmed.ncbi.nlm.nih.gov/2873832/) | 1986 | Cohorte | Br J Clin Pract | Transferencia de usuarios crónicos de nitrazepam a lormetazepam |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 89877 | Lormetazepam Alter 2 mg comprimidos EFG | Comprimido | No disponible |
| 63332 | Noctamid 2,5 mg/ml gotas orales en solución | Gotas orales en solución | No disponible |
| 75732 | Lormetazepam Stada 1 mg comprimidos EFG | Comprimido | No disponible |
| 88831 | Lormetazepam Tecnigen 1 mg comprimidos EFG | Comprimido | No disponible |
| 58639 | Loramet 2 mg comprimidos | Comprimido | No disponible |

Hay 20 autorizaciones vigentes en total, todas de monofármaco (sin combinaciones) y ninguna cancelada.

---

## Consideraciones de Seguridad

Consultar el prospecto para informar la seguridad. Los datos compilados no incluyen advertencias, contraindicaciones ni interacciones farmacológicas.

Como orientación de cautela derivada de la literatura revisada: riesgo de dependencia, insomnio de rebote, efectos residuales al día siguiente (somnolencia, deterioro psicomotor y de memoria) y mayor riesgo en personas de edad avanzada.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El insomnio está respaldado por un ensayo de fase 3 completado (283 participantes) en el que lormetazepam es comparador activo, además de un segundo ensayo de fase 3 terminado prematuramente y literatura clínica. Se trata de una indicación ya establecida, por lo que la decisión se centra en gestionar el riesgo. El resto de las indicaciones predichas quedan en *Hold* (abuso de sustancias, cauda equina, tortícolis paroxística infantil) o como pregunta de investigación (ansiedad, trastorno de ansiedad).

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS para confirmar indicaciones, advertencias y contraindicaciones
- Datos detallados del mecanismo de acción (MOA)
- Limitar la duración del tratamiento y monitorizar dependencia, insomnio de rebote y efectos residuales
- Precaución específica en pacientes de edad avanzada (caídas, deterioro cognitivo)
- Para ansiedad: ensayos específicos de lormetazepam, dado que la evidencia actual son revisiones y estudios farmacológicos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


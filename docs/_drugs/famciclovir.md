---
layout: default
title: Famciclovir
parent: Solo predicción del modelo (L5)
nav_order: 324
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "FAMCICLOVIR"
predicted_indications: ["post-infectious neuralgia", "sequela of COVID-19", "hepatitis C induced liver cirrhosis", "malignant pleural mesothelioma", "AIDS-related disorder", "malignant epithelioid mesothelioma", "chickenpox", "sarcomatoid mesothelioma", "malignant visceral pleura tumor"]
description: "Famciclovir: nueva indicación predicha, Neuralgia postinfecciosa (post-infectious neuralgia) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Famciclovir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Famciclovir: Neuralgia postinfecciosa (post-infectious neuralgia)
{: .text-alpha }

## Resumen en Una Frase

Famciclovir es un antiviral oral (profármaco del penciclovir), originalmente utilizado para el tratamiento del herpes zóster.
El modelo TxGNN predice que podría ser efectivo para **neuralgia postinfecciosa (postherpética)**, pero actualmente solo hay **1 ensayo clínico** relacionado, que no evalúa famciclovir, y **ninguna publicación** que respalde directamente esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Neuralgia postinfecciosa (post-infectious neuralgia) |
| Puntaje de Predicción TxGNN | 0.9975 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 9 de 13) |
| Número de Autorizaciones | 13 (vigentes: 9) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, famciclovir es un profármaco del penciclovir, que en su forma trifosfato inhibe la ADN polimerasa del virus varicela-zóster (VZV). Esta es la base de su eficacia en el herpes zóster.

La neuralgia postherpética es la complicación más frecuente del herpes zóster y persiste más de 90 días tras resolverse el episodio agudo. Mecanísticamente, el tratamiento antiviral temprano podría reducir la gravedad del episodio agudo y, posiblemente, el riesgo de neuralgia posterior.

Sin embargo, el único ensayo vinculado (NCT03120962) evalúa oxicodona para prevenir la neuralgia postherpética, no famciclovir, por lo que no aporta evidencia directa sobre este fármaco. La predicción se apoya sobre todo en la relación biológica entre ambas enfermedades.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | No aplica | Desconocido | 140 | Uso temprano de oxicodona en la fase aguda del herpes zóster para prevenir la neuralgia postherpética. Famciclovir no es la intervención evaluada; solo relevancia contextual |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61597 | FAMVIR 125 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 60609 | FAMVIR 250 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 65027 | FAMVIR 500 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 71964 | Famciclovir Normon 250 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 76997 | Famciclovir Tecnigen 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |

Se muestran 5 de las 13 autorizaciones vigentes (todas de medicamentos con un único principio activo; ninguna cancelada).

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación en el grafo de conocimiento**: enfermedad renal y piouréter (no proviene del texto del prospecto, debe confirmarse con la ficha técnica).
- **Interacciones Farmacológicas**: se identificaron 84 posibles interacciones, todas con nivel de gravedad desconocido. Entre las principales figuran calcitriol, doxiciclina, clotrimazol, pantoprazol, glimepirida, morfina, metformina, omeprazol, palonosetrón, rosiglitazona, lansoprazol y vancomicina.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en TxGNN, pero la evidencia es de nivel L4: el único ensayo relacionado no evalúa famciclovir y no hay literatura de apoyo. Además, no se dispone del texto de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y revisar las advertencias y contraindicaciones de la ficha técnica de la AEMPS
- Completar los datos del mecanismo de acción
- Buscar y evaluar estudios que analicen específicamente famciclovir (o antivirales análogos) en la prevención o el tratamiento de la neuralgia postherpética
- Valorar la seguridad en poblaciones con insuficiencia renal, dada la señal del modelo TxGNN (aprendizaje profundo), que puede reflejar similitudes aprendidas entre enfermedades relacionadas, no evidencia biológica

---

### Nota Complementaria: Otras Indicaciones Predichas

Entre las demás predicciones, solo **varicela** alcanza el nivel L1 (decisión: Proceed with Guardrails), con puntaje TxGNN de 0.9911. Se respalda en dos ensayos de Fase 3 completados:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00098046](https://clinicaltrials.gov/study/NCT00098046) | Fase 3 | Completado | 76 | Farmacocinética y seguridad de una formulación pediátrica oral de famciclovir en niños de 1 a 12 años con infección por VZV |
| [NCT01327144](https://clinicaltrials.gov/study/NCT01327144) | Fase 3 | Completado | 177 | Famciclovir 500 mg frente a aciclovir en herpes zóster: eficacia y seguridad |

Estos estudios son de zóster o de farmacocinética/seguridad, no ensayos de eficacia en varicela primaria, y el tratamiento estándar (aciclovir/valaciclovir) debe tenerse en cuenta. El resto de las predicciones (COVID-19 persistente, cirrosis por hepatitis C, mesoteliomas y tumor pleural visceral) carecen de fundamento mecanístico o evidencia, y se mantienen en Hold. La predicción de trastorno relacionado con el SIDA queda como pregunta de investigación, con apoyo indirecto limitado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


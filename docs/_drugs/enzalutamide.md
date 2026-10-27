---
layout: default
title: Enzalutamide
parent: Solo predicción del modelo (L5)
nav_order: 293
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Enzalutamide: nueva indicación predicha, Susceptibilidad al cáncer de próstata/cáncer cerebral (nivel de evidencia L5). Indicación original: Cáncer de próstata"
monitor_inn: "Enzalutamide"
predicted_indications: ["prostate leiomyoma", "Brenner tumor", "fibroma of prostate", "benign reproductive system neoplasm", "benign prostate phyllodes tumor"]
---

# Enzalutamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Enzalutamida: De Cáncer de Próstata a Susceptibilidad al Cáncer de Próstata/Cáncer Cerebral
{: .text-alpha }

## Resumen en Una Frase

Enzalutamida es un inhibidor del receptor de andrógenos, utilizado originalmente para el tratamiento del cáncer de próstata.
El modelo TxGNN predice que podría ser efectivo para **susceptibilidad al cáncer de próstata/cáncer cerebral**, un fenotipo de susceptibilidad y no una enfermedad tratable en sentido estricto,
con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección actualmente.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de próstata |
| Nueva Indicación Predicha | Susceptibilidad al cáncer de próstata/cáncer cerebral |
| Puntaje de Predicción TxGNN | 99.71% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 17 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Enzalutamida es un inhibidor del receptor de andrógenos (AR), que es su diana farmacológica. Está aprobada para el cáncer de próstata, incluidos el cáncer de próstata resistente a la castración y el sensible a hormonas. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada, más allá de su acción sobre el AR.

La predicción probablemente refleja que el nodo de "susceptibilidad al cáncer de próstata" está muy cerca de la indicación original en el grafo de conocimiento. No se encontró ningún vínculo con el cáncer cerebral. Además, una susceptibilidad es un fenotipo genético y no una enfermedad que se trate con un fármaco.

Por ello, la puntuación alta debe interpretarse con cautela. Es probable que sea un artefacto del grafo y no una señal terapéutica nueva.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 17 autorizaciones vigentes (todas de principio activo único). Los textos de indicación aprobada no estaban disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 89057 | Enzalutamida Sandoz 80 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 113846002 | Xtandi 40 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 89615 | Enzalutamida Accord 40 mg cápsulas blandas EFG | Cápsula blanda |
| 1241842002 | Enzalutamida Viatris 40 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 113846001 | Xtandi 40 mg cápsulas blandas | Cápsula blanda |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia hormonal dirigida (inhibidor del receptor de andrógenos); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura. Además, la indicación predicha es un fenotipo de susceptibilidad y no una enfermedad tratable. Otras predicciones del mismo fármaco, como "cáncer de órgano reproductor masculino", sí cuentan con ensayos de Fase 3, pero estos corresponden en su mayoría a la indicación ya aprobada (cáncer de próstata) y no aportan un reposicionamiento nuevo.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA)
- Textos de indicación, advertencias y contraindicaciones del prospecto de la AEMPS
- Evidencia clínica o preclínica que vincule el bloqueo del AR con la nueva indicación
- Reevaluar las demás predicciones del modelo, priorizando indicaciones que sean enfermedades tratables y distintas del cáncer de próstata
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Pamidronic Acid
parent: Solo predicción del modelo (L5)
nav_order: 607
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
monitor_inn: "pamidronic acid"
predicted_indications: ["HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection"]
description: "Pamidronic Acid: nueva indicación predicha, Infección por VIH (HIV infectious disease) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Pamidronic Acid
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Pamidronic Acid: Infección por VIH (HIV infectious disease)
{: .text-alpha }

## Resumen en Una Frase

El ácido pamidrónico es un bisfosfonato utilizado originalmente para la hipercalcemia humoral de origen maligno y la enfermedad ósea de Paget.
El modelo TxGNN predice que podría ser efectivo para **infección por VIH**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Infección por VIH (HIV infectious disease) |
| Puntaje de Predicción TxGNN | 0.9973 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 3 de 3) |
| Número de Autorizaciones | 3 (vigentes: 3) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el ácido pamidrónico es un bisfosfonato nitrogenado. Esta clase inhibe la resorción ósea y su eficacia en la hipercalcemia maligna y la enfermedad de Paget está establecida.

Un vínculo mecanístico plausible, pero no verificado, es que los bisfosfonatos nitrogenados inhiben la farnesil pirofosfato sintasa y la vía del mevalonato. Esto podría afectar la prenilación de proteínas y la función de las células inmunitarias. La pérdida ósea asociada al VIH es un problema clínico relacionado pero distinto, en el que los bisfosfonatos se usan como protección ósea, no como tratamiento antiviral.

Con una puntuación TxGNN muy alta (0.9973) pero sin ningún estudio clínico ni literatura de apoyo, esta predicción debe considerarse una asociación computacional, no una hipótesis respaldada por datos.

Otras predicciones del modelo TxGNN (deep learning), todas con nivel L5 y sin evidencia: trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y disminución de la sustancia blanca cortical (0.9959), síndrome de inmunodeficiencia adquirida felina (0.9945) e infección por el virus de inmunodeficiencia simia (0.9945). Las dos últimas son indicaciones veterinarias o de modelo animal. Las puntuaciones provienen del modelo TxGNN (deep learning) y pueden reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 64945 | Pamidronato Hospira 3 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |
| 64946 | Pamidronato Hospira 6 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |
| 64947 | Pamidronato Hospira 9 mg/ml concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos compilados |

Las tres autorizaciones están vigentes, son de monofármaco y pertenecen a Pfizer S.L.

## Consideraciones de Seguridad

- **Contraindicaciones / enfermedades de riesgo según el grafo de conocimiento** (no proceden del texto del prospecto): enfermedad renal, piouréter, deficiencia de potasio, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, periodontitis, osteonecrosis de la mandíbula e hipofosfatemia.
- **Interacciones farmacológicas**: se identificaron 166 interacciones en total. Las principales, de nivel moderado, incluyen:
  - Anfotericina B (y sus formulaciones lipídicas, liposomal y de sulfato de colesterilo)
  - Aminoglucósidos (kanamicina, neomicina, estreptomicina) y vancomicina
  - Polimixina B
  - Salicilatos y derivados de aminosalicilatos (ácido acetilsalicílico, mesalazina, balsalazida, olsalazina, sulfasalazina)
  - Exenatida

  Otras interacciones de nivel no clasificado: calcitriol, doxiciclina, clotrimazol, pantoprazol y sucralfato. Muchas de las combinaciones moderadas implican potencial nefrotóxico aditivo.
- No se dispone de las advertencias ni de las contraindicaciones del prospecto de la AEMPS; deben consultarse directamente.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para VIH se basa solo en el modelo (nivel L5), sin ensayos ni literatura. Además, el único vínculo plausible (protección ósea en pérdida ósea asociada al VIH) no equivale a una indicación antiviral.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas).
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión sistemática de la literatura sobre bisfosfonatos en VIH (pérdida ósea frente a efecto antiviral o inmunomodulador).
- Valorar si el objetivo es la salud ósea en pacientes con VIH, lo que sería un posicionamiento distinto y más realista.
- Evaluar la seguridad renal y dental (osteonecrosis de la mandíbula) en la población con VIH, dada su vulnerabilidad renal y las interacciones con fármacos nefrotóxicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


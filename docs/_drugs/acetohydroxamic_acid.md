---
layout: default
title: Acetohydroxamic Acid
parent: Solo predicción del modelo (L5)
nav_order: 19
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Acetohydroxamic Acid: nueva indicación predicha, Uretritis por Ureaplasma (nivel de evidencia L5). Indicación original: Infección del tracto urinario (según el grafo de conocimiento"
monitor_inn: "acetohydroxamic acid"
predicted_indications: ["Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis"]
---

# Acetohydroxamic Acid
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

## Ácido acetohidroxámico: De Infección del Tracto Urinario a Uretritis por Ureaplasma
{: .text-alpha }

## Resumen en Una Frase

El ácido acetohidroxámico es un inhibidor de la ureasa, originalmente utilizado en el contexto de la infección del tracto urinario.
El modelo TxGNN predice que podría ser efectivo para **uretritis por Ureaplasma**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección del tracto urinario (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Uretritis por Ureaplasma |
| Puntaje de Predicción TxGNN | 99,63% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información farmacológica conocida, el ácido acetohidroxámico inhibe la ureasa, una enzima que degrada la urea en amoníaco. Esto reduce la alcalinización local de la orina y la formación de cálculos de estruvita asociados a infecciones por bacterias productoras de ureasa.

*Ureaplasma urealyticum* produce ureasa, por lo que existe un vínculo biológico plausible: inhibir la enzima podría reducir la producción de amoníaco y la irritación tisular asociada. Sin embargo, este vínculo se infiere de la farmacología general de la ureasa y de la predicción del modelo (puntaje 0,996), no de datos clínicos.

Conviene ser prudente: la uretritis por Ureaplasma se trata habitualmente con antibióticos (por ejemplo, doxiciclina o azitromicina), y la inhibición de la ureasa no es una estrategia establecida para erradicar el microorganismo.

Otras indicaciones predichas, con el mismo nivel de evidencia L5 (solo predicción) y recomendación Hold:
- **Uretritis gonocócica** (99,63%): *Neisseria gonorrhoeae* no es un patógeno dependiente de ureasa; el puntaje alto probablemente refleja la asociación del fármaco con la infección urinaria en el grafo, no un mecanismo específico.
- **Enfermedad inflamatoria uterina** (99,54%): suele ser polimicrobiana; no hay un papel establecido para la inhibición de la ureasa.
- **Pielonefritis xantogranulomatosa** (99,46%): es la más plausible mecanísticamente, por su asociación con cálculos obstructivos y bacterias productoras de ureasa (p. ej., *Proteus mirabilis*). Aun así, el tratamiento es principalmente quirúrgico más antibióticos, y cualquier uso sería coadyuvante.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 56204 | URONEFREX 125 mg CÁPSULAS | Cápsula dura | No disponible en los datos compilados |
| 56203 | URONEFREX 250 mg CÁPSULAS | Cápsula dura | No disponible en los datos compilados |

Ambas autorizaciones están vigentes, corresponden a monofármaco y pertenecen a Ferrer Internacional S.A.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): trombocitopenia, abuso/dependencia de sustancias, anemia, anemia macrocítica, leucopenia, anemia hemolítica y flebitis.
- **Interacciones farmacológicas** (5 identificadas):

| Fármaco | Nivel |
|------|------|
| Cladribina | Mayor |
| Alemtuzumab | Moderado |
| Ocrelizumab | Moderado |
| Omacetaxina mepesuccinato | Moderado |
| Ustekinumab | Moderado |

- Como consideración adicional señalada en la evaluación de la pielonefritis xantogranulomatosa: riesgo conocido de teratogenicidad y de anemia hemolítica.

Las advertencias y contraindicaciones del prospecto no están disponibles en los datos compilados; consultar el prospecto de la AEMPS para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las cuatro indicaciones predichas se sustentan solo en la predicción del modelo (nivel L5), sin ensayos clínicos ni literatura. Además, el perfil hematológico del fármaco (contraindicaciones en anemia, leucopenia y trombocitopenia) exige una revisión de seguridad cuidadosa antes de avanzar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), dato bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Realizar una revisión sistemática de la literatura sobre inhibición de la ureasa en *Ureaplasma* y, con prioridad, en la pielonefritis xantogranulomatosa.
- Evaluar la compatibilidad de la vía de administración y la similitud con la indicación original.
- Valorar el uso exclusivamente coadyuvante a los antibióticos, con un plan de monitoreo hematológico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


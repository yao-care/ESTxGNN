---
layout: default
title: Celecoxib
parent: Solo predicción del modelo (L5)
nav_order: 161
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-31
monitor_inn: "CELECOXIB"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "hypermobility of coccyx", "brachyolmia", "rheumatoid nodulosis", "WHIM syndrome"]
description: "Celecoxib: nueva indicación predicha, Displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) (nivel de evidencia L5). Indicación original: No consta en los dato…"
---

# Celecoxib
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

## Celecoxib: Displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type)
{: .text-alpha }

## Resumen en Una Frase

Celecoxib es un antiinflamatorio no esteroideo (AINE) inhibidor selectivo de la COX-2, utilizado originalmente en enfermedades articulares inflamatorias como la artritis reumatoide, la espondilitis anquilosante y la artrosis.
El modelo TxGNN predice que podría ser efectivo para la **displasia acromesomélica tipo Hunter-Thompson**, una enfermedad esquelética genética rara, pero **no existe ningún ensayo clínico ni publicación** que respalde esta dirección: se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) |
| Puntaje de Predicción TxGNN | 0.9988 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 12) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, celecoxib es un inhibidor selectivo de la ciclooxigenasa-2 (COX-2). Reduce la síntesis de prostaglandinas inflamatorias y, con ello, el dolor y la inflamación articular. Su eficacia en artritis reumatoide, espondilitis anquilosante, artrosis y artritis idiopática juvenil está bien establecida.

La displasia acromesomélica tipo Hunter-Thompson es un trastorno esquelético hereditario causado por variantes en el gen *CDMP1/GDF5*. Afecta al desarrollo del cartílago y del hueso, y no es una enfermedad inflamatoria. No se conoce un mecanismo por el cual inhibir la COX-2 pueda corregir o modificar su curso.

**Conclusión sobre la razonabilidad:** el puntaje alto del modelo TxGNN (aprendizaje profundo) (0.9988) probablemente refleja similitudes que el modelo aprendió entre enfermedades óseas y articulares relacionadas, no evidencia biológica ni una base mecanística plausible. En el mejor de los casos, celecoxib podría ofrecer alivio sintomático del dolor musculoesquelético, pero eso es especulativo y no está respaldado por datos específicos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Celecoxib está comercializado en España con 20 autorizaciones vigentes (todas de monofármaco, ninguna cancelada), en forma de cápsula dura de 100 mg o 200 mg. Los registros no incluyen texto de indicación aprobada. Se muestran las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 63073 | CELEBREX 200 mg cápsulas duras | Cápsula dura | Viatris Healthcare Limited |
| 3400935437068IP1 | CELEBREX 200 mg cápsulas duras | Cápsula dura | Pfizer Holding France |
| 63891 | ARTILOG 200 mg cápsulas duras | Cápsula dura | Viatris Healthcare Limited |
| 76749 | Celecoxib Teva 200 mg cápsulas duras EFG | Cápsula dura | Teva Pharma S.L.U. |
| 77596 | Celecoxib Pensa 200 mg cápsulas duras EFG | Cápsula dura | Pensa Pharma, S.A.U |

---

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación o precaución (según el grafo de conocimiento, no el texto del prospecto):**
  - Cardiovasculares: hipertensión, insuficiencia cardíaca congestiva, infarto de miocardio, enfermedad cardiovascular, ictus y trastornos cerebrovasculares.
  - Digestivas: úlcera péptica activa.
  - Renales y hepáticas: enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar.
  - Respiratorias: asma.
  - Hematológicas: anemia, hemoglobinopatías.
  - Otras: abuso o dependencia de sustancias.
- **Interacciones farmacológicas:** se registran 100 interacciones. Entre las principales:
  - **Mayor:** eliglustat.
  - **Moderadas:** hidrocortisona, metformina, antidiabéticos orales (acetohexamida, clorpropamida, glimepirida, glipizida, gliburida, nateglinida), exenatida, cimetidina, levofloxacino, metronidazol, kanamicina, naltrexona, mesalazina, balsalazida, olsalazina, fenfluramina y dexfenfluramina.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos, de literatura y de una base mecanística plausible. Se trata de una enfermedad genética esquelética no inflamatoria, en la que no hay motivo establecido para esperar beneficio de la inhibición de la COX-2. Además, el perfil de seguridad cardiovascular, gastrointestinal y renal de celecoxib exige una justificación clara para cualquier nuevo uso.

**Para avanzar se necesita:**
- Una hipótesis mecanística que vincule la inhibición de la COX-2 con la vía *GDF5/CDMP1*, respaldada por estudios preclínicos.
- Datos detallados del mecanismo de acción (MOA) del fármaco.
- Revisión de las advertencias y contraindicaciones del prospecto oficial de la AEMPS.
- Una revisión de la literatura específica sobre esta enfermedad y sobre el papel de las prostaglandinas en ella.

**Nota:** entre las demás predicciones de celecoxib, la mejor respaldada es la espondilopatía inflamatoria (espondilitis anquilosante o espondiloartritis axial), con 4 ensayos de Fase 3/4 completados y evidencia L1. Sin embargo, es esencialmente una indicación ya existente del fármaco, no un reposicionamiento nuevo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


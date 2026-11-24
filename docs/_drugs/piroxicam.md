---
layout: default
title: Piroxicam
parent: Solo predicción del modelo (L5)
nav_order: 644
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "PIROXICAM"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "WHIM syndrome", "rheumatoid nodulosis", "juvenile idiopathic arthritis"]
description: "Piroxicam: nueva indicación predicha, Colobomatous microphthalmia-rhizomelic dysplasia syndrome (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 9 (comercializadas: 1)"
---

# Piroxicam
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

## Piroxicam: Colobomatous microphthalmia-rhizomelic dysplasia syndrome
{: .text-alpha }

## Resumen en Una Frase

Piroxicam es un antiinflamatorio no esteroideo (AINE) utilizado originalmente para la artritis reumatoide, la artrosis y otras artropatías.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de microftalmía colobomatosa-displasia rizomélica**, una displasia ocular y esquelética muy rara, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| Puntaje de Predicción TxGNN | 1.0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 9; revocadas o suspendidas: 8) |
| Número de Autorizaciones | 9 (comercializadas: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Piroxicam (traducción no oficial): «El piroxicam tiene propiedades analgésicas, antiinflamatorias y antipiréticas. El mecanismo de acción de Piroxicam Cápsulas, al igual que el de otros AINE, no se comprende por completo, pero implica la inhibición de la ciclooxigenasa (COX-1 y COX-2).» Texto original en inglés: "Piroxicam has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of Piroxicam Capsules, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: piroxicam prescribing information, Sportpharm LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=41425352-2a59-43ef-bccc-f8cc69e72be4), versión del 2026-09-29; consultado el 2026-11-19). Según la información conocida, piroxicam es un AINE inhibidor no selectivo de la ciclooxigenasa (COX), con eficacia sintomática establecida en artritis reumatoide y artrosis. Reduce la inflamación y el dolor al disminuir la síntesis de prostaglandinas.

**En este caso no se identificó un vínculo mecanístico plausible.** La enfermedad predicha es un síndrome genético raro del desarrollo, con alteraciones esqueléticas y oculares. La inhibición de COX no tiene un papel conocido en su patogenia. El puntaje del modelo TxGNN (aprendizaje profundo) es muy alto (1,0000), pero puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica ni una relación terapéutica real.

Como el mecanismo de acción original tampoco está documentado en los datos disponibles, la predicción no puede verificarse mecanísticamente. Debe considerarse una hipótesis generada por el modelo, sin respaldo clínico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 58986 | SALVACAM 5mg/g GEL | GEL | Laboratorios Salvat S.A. | Comercializada |
| 62418 | PIROXICAM CINFA 20 mg COMPRIMIDOS DISPERSABLES EFG | COMPRIMIDO DISPERSABLE | Laboratorios Cinfa S.A. | Suspendida |
| 58708 | SASULEN 5 MG/G GEL | GEL | Laboratorios Veris S.A. | Revocada |
| 55382 | FELDENE 10 MG CAPSULAS DURAS | CÁPSULA DURA | Pfizer S.L. | Revocada |
| 55806 | FELDENE 20 MG CAPSULAS DURAS | CÁPSULA DURA | Pfizer S.L. | Revocada |
| 58198 | IMPRONTAL 5 mg/g CREMA | CREMA | Meda Pharma S.L. | Revocada |
| 58085 | FELDENE 20 MG/ML SOLUCION INYECTABLE | SOLUCIÓN INYECTABLE | Pfizer S.L. | Revocada |
| 60070 | FELDENE FLAS 20 mg LIOFILIZADO ORAL | LIOFILIZADO ORAL | Pfizer S.L. | Revocada |
| 57797 | FELDEGEL 5 mg/g GEL | GEL | Pfizer S.L. | Revocada |

Se muestran las 9 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Entre las autorizaciones hay formulaciones tópicas (geles y crema): SASULEN 5 mg/g gel, SALVACAM 5 mg/g gel, IMPRONTAL 5 mg/g crema y FELDEGEL 5 mg/g gel.

<!-- review:begin es-lic-20261105-piroxicam-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Se muestran 5 de las 9 autorizaciones vigentes (todas de principio activo único)." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-piroxicam-1 -->

<!-- review:begin es-lic-20261124b-piroxicam-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Las demás autorizaciones corresponden a formulaciones tópicas (geles y crema):" Corregido: la frase hablaba de autorizaciones que no figuraban en la tabla anterior (por ejemplo, «la sexta», «las restantes» u «otras»). La tabla de Información de Mercado en España se genera desde el 2026-11-24 por programa a partir de los datos de CIMA (AEMPS) y las incluye; las cifras actuales están en el Resumen rápido. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261124b-piroxicam-1 -->

---

## Consideraciones de Seguridad

- **Condiciones de riesgo asociadas (grafo de conocimiento, no texto del prospecto):** el grafo asocia piroxicam con contraindicación o precaución en las siguientes condiciones:
  - **Cardiovasculares:** hipertensión, insuficiencia cardíaca congestiva, infarto de miocardio, trombosis coronaria, enfermedad cardiovascular y cardíaca, ictus, trastornos cerebrovasculares e infarto cerebral.
  - **Hepáticas y biliares:** enfermedad hepática, insuficiencia hepática aguda, hepatitis, lesión hepática inducida por fármacos y enfermedad de la vesícula biliar.
  - **Renales:** enfermedad renal y piouréter.
  - **Hematológicas:** trastornos de la coagulación, enfermedad trombótica, hemoglobinopatías y anemias.
  - **Gastrointestinales:** úlcera péptica activa.
  - **Otras:** trastornos de la visión y ceguera, y abuso o dependencia de sustancias.
- **Interacciones farmacológicas:** se identificaron 100 interacciones en total. Entre las principales (muestra de 20):
  - **Moderadas:** corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), ácido acetilsalicílico, metformina, glimepirida, clorpropamida, aprepitant, mesalazina, balsalazida, citrato y bicarbonato de potasio, ácido picosulfúrico y polietilenglicol con electrolitos.
  - **Menores:** famotidina, ranitidina, cimetidina y linaclotida.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no hay un mecanismo plausible que vincule la inhibición de COX con esta displasia genética. Además, el perfil de seguridad de un AINE, con riesgos cardiovasculares, renales, hepáticos y gastrointestinales, no se justifica sin un beneficio terapéutico demostrable.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de piroxicam y un análisis mecanístico formal frente a la fisiopatología de la enfermedad.
- Evidencia preclínica o clínica específica de la nueva indicación. Hasta ahora no existe.
- Las advertencias y contraindicaciones del prospecto de la AEMPS, para completar la evaluación de seguridad.

**Nota complementaria:** entre las predicciones del modelo, la **artritis idiopática juvenil** (puntaje 0,9993) es la única con literatura recuperada. Incluye estudios pediátricos de los años 80 y 90, como un estudio multicéntrico de piroxicam frente a naproxeno y un estudio farmacocinético en niños, además de metaanálisis en red de AINE. Su nivel de evidencia sería L3, pero solo como opción sintomática, no modificadora de la enfermedad. Podría valorarse como pregunta de investigación aparte, sin alterar la decisión de este informe.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Eliminado: "Se muestran 5 de las 9 autorizaciones vigentes (todas de principio activo único)" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: piroxicam prescribing information, Sportpharm LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=41425352-2a59-43ef-bccc-f8cc69e72be4) |
| 2026-11-24 | «Las demás autorizaciones corresponden a» → «Entre las autorizaciones hay» | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


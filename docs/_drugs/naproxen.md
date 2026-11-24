---
layout: default
title: Naproxen
parent: Solo predicción del modelo (L5)
nav_order: 552
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "Naproxen"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome"]
description: "Naproxen: nueva indicación predicha, Síndrome de braquidactilia-sindactilia (brachydactyly-syndactyly syndrome) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 8 (comercializadas: 5; autorizadas no comercializadas: 1)"
---

# Naproxen
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

## Naproxen: Síndrome de braquidactilia-sindactilia (brachydactyly-syndactyly syndrome)
{: .text-alpha }

## Resumen en Una Frase

Naproxeno es un antiinflamatorio no esteroideo (AINE) utilizado originalmente para tratar la bursitis, la artritis reumatoide, la espondilitis anquilosante, la tendinitis, la gota y otros trastornos musculoesqueléticos y dolorosos.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de braquidactilia-sindactilia**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de braquidactilia-sindactilia (brachydactyly-syndactyly syndrome) |
| Puntaje de Predicción TxGNN | 0.9935 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 5 de 8; autorizadas no comercializadas: 1; revocadas o suspendidas: 2) |
| Número de Autorizaciones | 8 (comercializadas: 5) |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Naproxen (traducción no oficial): «El naproxeno tiene propiedades analgésicas, antiinflamatorias y antipiréticas. El mecanismo de acción de NAPRELAN, al igual que el de otros AINE, no se comprende por completo, pero implica la inhibición de la ciclooxigenasa (COX-1 y COX-2).» Texto original en inglés: "Naproxen has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of NAPRELAN, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Naprelan (naproxen sodium) prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b8a51c9a-488e-4377-a041-436f6a2f8893), versión del 2026-01-08; consultado el 2026-11-19). Según la información conocida, naproxeno es un inhibidor no selectivo de la ciclooxigenasa (COX-1 y COX-2), que reduce la síntesis de prostaglandinas y produce efectos antiinflamatorios y analgésicos. Su eficacia en trastornos inflamatorios y dolorosos del aparato locomotor está comprobada.

Los síndromes de braquidactilia-sindactilia son malformaciones esqueléticas congénitas causadas por defectos genéticos del desarrollo. La inhibición de COX no corrige estas vías, por lo que **los datos disponibles no respaldan un vínculo mecanístico plausible**. En el mejor de los casos, el beneficio se limitaría al alivio sintomático del dolor, lo cual no constituye una señal de reposicionamiento.

Es probable que el puntaje alto (0.9935), obtenido del modelo TxGNN (aprendizaje profundo), refleje similitudes que el modelo aprendió entre enfermedades relacionadas, como las indicaciones musculoesqueléticas de naproxeno (artritis, artropatía), y no una justificación biológica. Las otras tres predicciones de mayor puntaje (síndrome de microftalmia colobomatosa-displasia rizomélica, displasia acromesomélica tipo Hunter-Thompson y síndrome de braquiolmia-amelogénesis imperfecta) son también trastornos genéticos raros del desarrollo, igualmente sin evidencia ni vínculo mecanístico, y todas se mantienen en nivel L5 y decisión Hold.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 68435 | NAPROXENO NORMON 500 mg COMPRIMIDOS EFG | COMPRIMIDO | Laboratorios Normon S.A. | Comercializada |
| 85570 | NAPROXENO AUROVITAS 500 MG COMPRIMIDOS EFG | COMPRIMIDO | Aurovitas Spain, S.A.U. | Comercializada |
| 56267 | NAPROSYN 500 mg COMPRIMIDOS | COMPRIMIDO | Atnahs Pharma Netherlands Bv. | Comercializada |
| 54246 | LUNDIRAN 250 mg Cápsulas duras | CÁPSULA DURA | Industria Quimica Y Farmaceutica Vir S.A. | Comercializada |
| 61370 | NAPROXENO TEVA-RATIOPHARM 500 mg COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Teva Pharma S.L.U. | Comercializada |
| 86455 | NAPROXENO INFECTOPHARM 50 MG/ML SUSPENSION ORAL | SUSPENSIÓN ORAL | Infectopharm Arzneimittel Und Consilium Gmbh | Autorizada, no comercializada |
| 77727 | LIDET 500 MG COMPRIMIDOS GASTRORRESISTENTES EFG | COMPRIMIDO GASTRORRESISTENTE | Aristo Pharma Iberia S.L. | Suspendida |
| 80806 | NAPROXENO AUROBINDO 500 MG COMPRIMIDOS EFG | COMPRIMIDO | Laboratorios Aurobindo S.L.U. | Revocada |

Se muestran las 8 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Entre las autorizaciones figuran también Lundiran 250 mg cápsulas duras, Naproxeno Teva-Ratiopharm 500 mg comprimidos recubiertos con película y Naproxeno Infectopharm 50 mg/ml suspensión oral.

<!-- review:begin es-lic-20261105-naproxen-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Se muestran 5 de las 8 autorizaciones vigentes (todas de monofármaco). Las otras tres corresponden a Lundiran 250 mg cápsulas duras, Naproxeno Teva-Ratiopharm 500 mg comprimidos recubiertos con película y Naproxeno Infectopharm 50 mg/ml suspensión oral." Corregido: la frase hablaba de autorizaciones que no figuraban en la tabla anterior (por ejemplo, «la sexta», «las restantes» u «otras»). La tabla de Información de Mercado en España se genera desde el 2026-11-24 por programa a partir de los datos de CIMA (AEMPS) y las incluye; las cifras actuales están en el Resumen rápido. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-naproxen-1 -->

## Consideraciones de Seguridad

- **Contraindicaciones señaladas por el grafo de conocimiento** (no proceden del prospecto): hipertensión, insuficiencia hepática y enfermedad hepática, enfermedad renal, insuficiencia cardíaca congestiva, enfermedad coronaria, infarto de miocardio, ictus y trastornos cerebrovasculares, trastornos de la coagulación, anemia, diabetes mellitus y cetoacidosis diabética, osteoporosis, epilepsia, enfermedad de la vesícula biliar, hiperplasia prostática benigna, obesidad y abuso de sustancias, entre otras.
- **Interacciones farmacológicas**: los datos de interacción solo recogen las dianas farmacológicas de naproxeno (COX-1/PTGS1 y COX-2/PTGS2); no se identificaron interacciones con otros fármacos.

Consultar el prospecto para información completa sobre advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre la inhibición de COX y una malformación congénita del desarrollo esquelético. Además, los datos de seguridad del prospecto no están disponibles.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA)
- Evidencia preclínica o clínica que respalde un vínculo biológico con la nueva indicación
- Advertencias y contraindicaciones del prospecto de la AEMPS para completar la evaluación de seguridad
- Textos de indicación aprobada de las autorizaciones españolas
- Evaluación de compatibilidad de vía de administración y de similitud con las indicaciones originales

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | «Las otras tres corresponden a» → «figuran también» | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Naprelan (naproxen sodium) prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b8a51c9a-488e-4377-a041-436f6a2f8893) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


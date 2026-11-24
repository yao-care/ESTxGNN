---
layout: default
title: Ceftriaxone
parent: Solo predicción del modelo (L5)
nav_order: 159
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
monitor_inn: "Ceftriaxone"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "chronic otitis media"]
description: "Ceftriaxone: nueva indicación predicha, hiperamilasemia (hyperamylasemia) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Ceftriaxone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Ceftriaxone: hiperamilasemia (hyperamylasemia)
{: .text-alpha }

## Resumen en Una Frase

Ceftriaxona es un antibiótico cefalosporínico de uso inyectable, utilizado en infecciones bacterianas.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia (hyperamylasemia)**, pero no hay ensayos clínicos registrados y la literatura recuperada es indirecta, por lo que la evidencia es solo de predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | hiperamilasemia (hyperamylasemia) |
| Puntaje de Predicción TxGNN | 0.9939 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 17; revocadas o suspendidas: 3) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Ceftriaxone (traducción no oficial): «La ceftriaxona es un fármaco antibacteriano. […] La ceftriaxona es un agente bactericida que actúa mediante la inhibición de la síntesis de la pared celular bacteriana. La ceftriaxona tiene actividad en presencia de algunas betalactamasas, tanto penicilinasas como cefalosporinasas, de bacterias gramnegativas y grampositivas.» Texto original en inglés: "Ceftriaxone is an antibacterial drug. […] Ceftriaxone is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Ceftriaxone has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: Ceftriaxone And Dextrose (ceftriaxone) prescribing information, B. Braun Medical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=67153914-16bc-490d-82d7-638061618467), versión del 2022-01-13; consultado el 2026-11-19). Por su clase, ceftriaxona es una cefalosporina que actúa contra bacterias, y su utilidad está establecida en infecciones bacterianas.

La hiperamilasemia es un hallazgo de laboratorio (elevación de amilasa en sangre), no una infección. No existe un vínculo mecanístico plausible entre la acción antibacteriana de ceftriaxona y la corrección de este hallazgo. El puntaje elevado del modelo es únicamente una predicción computacional.

Por tanto, la predicción debe considerarse una hipótesis sin respaldo mecanístico ni clínico en los datos compilados para este informe.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [7522351](https://pubmed.ncbi.nlm.nih.gov/7522351/) | 1994 | Cohorte | Southern Medical Journal | En 38 pacientes con hemorragia intracraneal, 25 presentaron lipasa elevada y 17 también amilasa elevada, sin pancreatitis. No evalúa ceftriaxona. |
| [10458061](https://pubmed.ncbi.nlm.nih.gov/10458061/) | 1999 | Estudio clínico | Bratislavske Lekarske Listy | Profilaxis con ceftriaxona 1 g en 30 pacientes tras papilosfinterotomía endoscópica frente a 30 sin antibiótico; contexto de prevención de infección, no tratamiento de hiperamilasemia. |
| [36263834](https://pubmed.ncbi.nlm.nih.gov/36263834/) | 2023 | Reporte de caso | Revista Española de Enfermedades Digestivas | Síndrome de Weil con hemorragia digestiva alta; no demuestra que ceftriaxona trate la hiperamilasemia. |

Ninguna de estas publicaciones estudia directamente ceftriaxona como tratamiento de la hiperamilasemia.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 83903 | CEFTRIAXONA QILU 1 G POLVO PARA SOLUCION INYECTABLE Y PARA PERFUSION EFG | POLVO PARA SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN | Qilu Pharma Spain S.L. | Comercializada |
| 63251 | CEFTRIAXONA LDP TORLAN 500 MG POLVO Y DISOLVENTE PARA SOLUCION INYECTABLE INTRAVENOSA EFG | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Ldp Laboratorios Torlan S.A. | Comercializada |
| 64950 | CEFTRIAXONA SALA 2 G POLVO PARA SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN EFG | POLVO PARA SOLUCIÓN PARA PERFUSIÓN | Laboratorio Reig Jofre, S.A. | Comercializada |
| 62635 | CEFTRIAXONA NORMON 1000 MG POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE Y PARA PERFUSION EFG | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Laboratorios Normon S.A. | Comercializada |
| 62636 | CEFTRIAXONA NORMON 500 MG POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE Y PARA PERFUSION EFG | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Laboratorios Normon S.A. | Comercializada |
| 64540 | CEFTRIAXONA FRESENIUS KABI 1 g POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE INTRAMUSCULAR EFG | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Fresenius Kabi España, S.A.U. | Comercializada |
| 62641 | CEFTRIAXONA NORMON 1000 MG POLVO Y SOLUCION PARA SOLUCION INYECTABLE INTRAMUSCULAR EFG | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Laboratorios Normon S.A. | Comercializada |
| 71057 | CEFTRIAXONA LDP TORLAN 250 MG POLVO Y DISOLVENTE PARA SOLUCION INYECTABLE INTRAVENOSA EFG | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Ldp Laboratorios Torlan S.A. | Comercializada |
| 83554 | MEDAXONE 2 G POLVO PARA SOLUCION INYECTABLE Y PARA PERFUSION EFG | POLVO PARA SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN | Medochemie Limited | Comercializada |
| 63252 | CEFTRIAXONA LDP TORLAN 1 G POLVO Y SOLUCION PARA SOLUCION INYECTABLE INTRAMUSCULAR EFG | POLVO Y SOLUCIÓN PARA SOLUCIÓN INYECTABLE | Ldp Laboratorios Torlan S.A. | Comercializada |

Se muestran 10 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

La lista puede ser parcial. Hay autorizaciones vigentes y otras revocadas; los datos de este informe solo recogen parte de ellas.

<!-- review:begin es-lic-20261124b-ceftriaxone-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Hay 17 autorizaciones vigentes y 3 canceladas." Corregido: la cifra solo correspondía a parte de las autorizaciones recogidas para este informe; según el listado completo de CIMA (AEMPS), datos del 2026-11-23, hay más autorizaciones con este principio activo. Las cifras recogidas están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261124b-ceftriaxone-1 -->

## Consideraciones de Seguridad

- **Interacciones farmacológicas (gravedad mayor)**: cloruro de calcio, glucoheptonato de calcio y gluconato de calcio.
- **Interacciones farmacológicas (gravedad moderada)**: kanamicina, neomicina, estreptomicina y ácido picosulfúrico.
- Se identificaron 100 interacciones en total; las anteriores son las de mayor relevancia entre las listadas.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni literatura que estudie ceftriaxona en hiperamilasemia, y no existe un mecanismo plausible que la respalde. La predicción se apoya únicamente en el puntaje del modelo (0,9939).

**Para avanzar se necesita:**
- Datos de mecanismo de acción que justifiquen un vínculo biológico con la hiperamilasemia
- Estudios clínicos o de cohortes que evalúen directamente ceftriaxona en esta condición
- Revisión del prospecto para advertencias y contraindicaciones antes de cualquier evaluación adicional

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Ceftriaxone And Dextrose (ceftriaxone) prescribing information, B. Braun Medical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=67153914-16bc-490d-82d7-638061618467) |
| 2026-11-24 | «17 autorizaciones vigentes y 3 canceladas» → sin cifras | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


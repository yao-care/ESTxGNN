---
layout: default
title: Dalbavancin
parent: Solo predicción del modelo (L5)
nav_order: 216
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "dalbavancin"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "otitis externa", "ophthalmic herpes zoster", "infectious mononucleosis", "orbital cellulitis"]
description: "Dalbavancin: nueva indicación predicha, Postinfectious vasculitis (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 7 (comercializadas: 5; autorizadas no comercializadas: 2)"
---

# Dalbavancin
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

## Dalbavancin: Postinfectious vasculitis
{: .text-alpha }

## Resumen en Una Frase

Dalbavancina es un antibiótico lipoglucopéptido, originalmente utilizado para tratar enfermedades de la piel causadas por infección.
El modelo TxGNN predice que podría ser efectivo para **vasculitis postinfecciosa**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es solo una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Postinfectious vasculitis |
| Puntaje de Predicción TxGNN | 0.9976 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 5 de 7; autorizadas no comercializadas: 2) |
| Número de Autorizaciones | 7 (comercializadas: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Dalbavancin (traducción no oficial): «La dalbavancina es un fármaco antibacteriano. […] La dalbavancina, un lipoglucopéptido semisintético, interfiere en la síntesis de la pared celular al unirse al extremo D-alanil-D-alanina del pentapéptido troncal del peptidoglucano naciente de la pared celular, lo que impide el entrecruzamiento. La dalbavancina es bactericida in vitro frente a Staphylococcus aureus y Streptococcus pyogenes a concentraciones similares a las mantenidas durante todo el tratamiento en seres humanos tratados según la pauta posológica recomendada.» Texto original en inglés: "Dalbavancin is an antibacterial drug. […] Dalbavancin, a semisynthetic lipoglycopeptide, interferes with cell wall synthesis by binding to the D-alanyl-D-alanine terminus of the stem pentapeptide in nascent cell wall peptidoglycan, thus preventing cross-linking. Dalbavancin is bactericidal in vitro against Staphylococcus aureus and Streptococcus pyogenes at concentrations similar to those sustained throughout treatment in humans treated according to the recommended dosage regimen." ([DailyMed: Dalvance (dalbavancin) prescribing information, Allergan, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4b4674d8-4d1e-4728-8465-d42ada33fa5c), versión del 2025-01-13; consultado el 2026-11-19). Según la información conocida, dalbavancina es un antibiótico lipoglucopéptido activo frente a bacterias Gram positivas, con eficacia comprobada en infecciones de piel y tejidos blandos, y actúa sobre la síntesis de la pared celular bacteriana.

La relación con la nueva indicación es débil. La vasculitis postinfecciosa suele ser de origen inmunomediado y aparece después de la infección, por lo que un antibiótico no tendría un papel mecanístico directo, salvo que una infección persistente por Gram positivos fuera el desencadenante. El puntaje alto de TxGNN (0,9976) es únicamente una predicción computacional.

Otras predicciones del modelo (con el mismo nivel L5) incluyen trastorno posbacteriano, síndrome postinfeccioso, estenosis uretral infecciosa, miocardiopatía de Chagas, síndrome hemolítico urémico asociado a infección, otitis externa, herpes zóster oftálmico, mononucleosis infecciosa y celulitis orbitaria. De estas, la celulitis orbitaria es el vínculo mecanístico más plausible (S. aureus, incluido MRSA, y estreptococos), aunque sin evidencia aportada sobre penetración orbitaria; el resto carece de base mecanística sólida (virus, parásitos o procesos inmunológicos/fibróticos).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 89574 | DALBAVANCINA ACCORD 500 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION EFG | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Accord Healthcare S.L.U. | Comercializada |
| 90523 | DALBAVANCINA ZENTIVA 500 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION EFG | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Zentiva K.S. | Comercializada |
| 90493 | DALBAVANCINA ADVANZ PHARMA 500 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION EFG | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Advanz Pharma Limited | Comercializada |
| 114986001 | XYDALBA 500 MG DE POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Abbvie Deutschland Gmbh & Co. Kg | Comercializada |
| 89545 | DALBAVANCINA SALA 500 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION EFG | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Laboratorio Reig Jofre, S.A. | Comercializada |
| 90291 | DALBAVANCINA BAXTER 500 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION EFG | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Baxter Holding B.V. | Autorizada, no comercializada |
| 89988 | DALBAVANCINA TEVA 500 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION EFG | POLVO PARA CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Teva B.V. | Autorizada, no comercializada |

Se muestran las 7 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Entre las autorizaciones figuran también Dalbavancina Sala y Dalbavancina Teva.

<!-- review:begin es-lic-20261124b-dalbavancin-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Se muestran 5 de las 7 autorizaciones vigentes (también están autorizadas Dalbavancina Sala y Dalbavancina Teva)." Corregido: la frase hablaba de autorizaciones que no figuraban en la tabla anterior (por ejemplo, «la sexta», «las restantes» u «otras»). La tabla de Información de Mercado en España se genera desde el 2026-11-24 por programa a partir de los datos de CIMA (AEMPS) y las incluye; las cifras actuales están en el Resumen rápido. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261124b-dalbavancin-1 -->

## Consideraciones de Seguridad

- **Interacciones Farmacológicas** (3 interacciones de nivel moderado):
  - Ácido picosulfúrico
  - Etinilestradiol
  - Ácido micofenólico

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos ni literatura, y el mecanismo antibacteriano no explica una enfermedad inmunomediada postinfecciosa.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), indispensable para el cribado de seguridad
- Completar los datos del mecanismo de acción
- Revisión de literatura y casos clínicos sobre dalbavancina en vasculitis postinfecciosa
- Si se desea priorizar, explorar primero la celulitis orbitaria (revisión farmacocinética y de penetración tisular) como pregunta de investigación

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Dalvance (dalbavancin) prescribing information, Allergan, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4b4674d8-4d1e-4728-8465-d42ada33fa5c) |
| 2026-11-24 | Eliminado: descripción de la tabla anterior y número | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


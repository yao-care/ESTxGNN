---
layout: default
title: Fosaprepitant
parent: Solo predicción del modelo (L5)
nav_order: 357
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Fosaprepitant: nueva indicación predicha, Síndrome nefrogénico de antidiuresis inapropiada (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicació…"
monitor_inn: "FOSAPREPITANT"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "pneumocystosis", "leprosy", "Cryptococcal meningitis", "multiple endocrine neoplasia", "intracranial abscess", "retinitis", "Plasmodium falciparum malaria", "echinococcus granulosus infectious disease", "hyperargininemia"]
---

# Fosaprepitant
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

## Fosaprepitant: De Indicación Original No Especificada a Síndrome Nefrogénico de Antidiuresis Inapropiada
{: .text-alpha }

## Resumen en Una Frase

Fosaprepitant es un profármaco de aprepitant, un antagonista del receptor NK1, comercializado en España en perfusión intravenosa. En los datos compilados para este informe no consta el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **síndrome nefrogénico de antidiuresis inapropiada (NSIAD)**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada |
| Puntaje de Predicción TxGNN | 0.9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 5 de 6; autorizadas no comercializadas: 1) |
| Número de Autorizaciones | 6 (comercializadas: 5) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Fosaprepitant (traducción no oficial): «El fosaprepitant es un profármaco del aprepitant y, por consiguiente, sus efectos antieméticos son atribuibles al aprepitant. El aprepitant es un antagonista selectivo de alta afinidad de los receptores humanos de la sustancia P/neurocinina 1 (NK-1). El aprepitant tiene poca o ninguna afinidad por los receptores de serotonina (5-HT 3 ), de dopamina y de corticosteroides, que son las dianas de los tratamientos existentes para las náuseas y los vómitos inducidos por quimioterapia (NVIQ).» Texto original en inglés: "Fosaprepitant is a prodrug of aprepitant and accordingly, its antiemetic effects are attributable to aprepitant. Aprepitant is a selective high-affinity antagonist of human substance P/neurokinin 1 (NK-1) receptors. Aprepitant has little or no affinity for serotonin (5-HT 3 ), dopamine, and corticosteroid receptors, the targets of existing therapies for chemotherapy-induced nausea and vomiting (CINV)." ([DailyMed: Navitrux (fosaprepitant) prescribing information, AVYXA Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a41b7c3a-1376-43a7-b5b9-6ba2eba1e169), versión del 2026-07-29; consultado el 2026-11-19). Según la información conocida, fosaprepitant es un profármaco de aprepitant, un antagonista del receptor de neuroquinina 1 (NK1) que bloquea la señalización de la sustancia P.

El NSIAD se debe a mutaciones con ganancia de función en el receptor V2 de la vasopresina (AVPR2). **No se ha establecido un vínculo mecanístico directo**: el antagonismo de NK1 no tiene un papel conocido en la señalización del receptor V2. El elevado puntaje de TxGNN es únicamente una predicción del modelo TxGNN (aprendizaje profundo) y debe interpretarse con cautela.

Otras predicciones del modelo (neumocistosis, lepra, meningitis criptocócica, síndromes de neoplasia endocrina múltiple, absceso intracraneal, malaria por *P. falciparum*, equinococosis, hiperargininemia) tampoco cuentan con ensayos ni literatura. La excepción es la retinitis, con un estudio preclínico indirecto (nivel L4, ver más abajo).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

*Nota:* para la segunda indicación mejor puntuada con algún respaldo, la retinitis (puntaje TxGNN 0.9968), existe un estudio preclínico en ratones (PMID [32058829](https://pubmed.ncbi.nlm.nih.gov/32058829/), 2021, *Ocular Immunology and Inflammation*). En él, fosaprepitant bloqueó la expresión de NK1 inducida por radiación UVR-B en tejidos oculares. Es evidencia indirecta (lesión ocular por UV, no retinitis) y se clasifica como L4.

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 88344 | FOSAPREPITANT TARBIS 150 MG POLVO PARA SOLUCION PARA PERFUSION EFG | POLVO PARA SOLUCIÓN PARA PERFUSIÓN | Tarbis Farma S.L. | Comercializada |
| 07437003 | IVEMEND 150 MG POLVO PARA SOLUCION PARA PERFUSION | POLVO PARA SOLUCIÓN PARA PERFUSIÓN | Merck Sharp & Dohme B.V. | Comercializada |
| 86382 | FOSAPREPITANT HIKMA 150 MG POLVO PARA SOLUCION PARA PERFUSION EFG | POLVO PARA SOLUCIÓN PARA PERFUSIÓN | Hikma Farmaceutica (Portugal) S.A. | Comercializada |
| 83380 | FOSAPREPITANT ACCORD 150 MG POLVO PARA SOLUCION PARA PERFUSION EFG | POLVO PARA SOLUCIÓN PARA PERFUSIÓN | Accord Healthcare S.L.U. | Comercializada |
| 84452 | FOSAPREPITANT ZENTIVA 150 MG POLVO PARA SOLUCION PARA PERFUSION EFG | POLVO PARA SOLUCIÓN PARA PERFUSIÓN | Zentiva K.S. | Comercializada |
| 88054 | FOSAPREPITANT TECNIGEN 150 MG POLVO PARA SOLUCION PARA PERFUSION EFG | POLVO PARA SOLUCIÓN PARA PERFUSIÓN | Tecnimede España Industria Farmaceutica S.A. | Autorizada, no comercializada |

Se muestran las 6 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Entre las autorizaciones figura Fosaprepitant Zentiva (nº 84452).

<!-- review:begin es-lic-20261124-fosaprepitant-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Se muestran 5 de las 6 autorizaciones vigentes (la sexta es Fosaprepitant Zentiva, nº 84452)." Eliminado: la frase describía qué filas mostraba la tabla anterior. La tabla de Información de Mercado en España se genera desde el 2026-11-24 por programa a partir de los datos de CIMA (AEMPS), ordenada por estado, y ya incluye Fosaprepitant Zentiva (nº 84452). Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261124-fosaprepitant-1 -->

---

## Consideraciones de Seguridad

- **Contraindicaciones (grafo de conocimiento):** el grafo de conocimiento TxGNN señala insuficiencia hepática como enfermedad asociada a contraindicación. No proviene del texto del prospecto.
- **Interacciones Farmacológicas:** se identificaron 100 interacciones en total. Entre las principales mostradas:
  - **Mayores:** eliglustat, naloxegol.
  - **Moderadas:** corticoides (hidrocortisona, betametasona, budesonida, dexametasona, triamcinolona), claritromicina, cimetidina, rabeprazol, lansoprazol, miconazol, dronabinol, alosetrón, pioglitazona, saxagliptina, glimepirida, nateglinida y naldemedina.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para NSIAD se basa solo en el modelo (nivel L5), sin ensayos ni literatura, y el mecanismo conocido (antagonismo de NK1) no se relaciona con el defecto del receptor V2. No hay base para avanzar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), actualmente un vacío bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, vía DrugBank).
- Establecer una hipótesis mecanística plausible entre NK1 y la señalización de AVPR2 y evaluarla en estudios preclínicos.
- Valorar si otra indicación predicha con algún respaldo preclínico (retinitis) merece priorización como pregunta de investigación.
- Revisar las interacciones mayores (eliglustat, naloxegol) y la contraindicación en insuficiencia hepática en cualquier plan futuro.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Navitrux (fosaprepitant) prescribing information, AVYXA Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a41b7c3a-1376-43a7-b5b9-6ba2eba1e169) |
| 2026-11-24 | Eliminado: descripción de la tabla anterior («se muestran 5 de las 6…; la sexta es…») | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


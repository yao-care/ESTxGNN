---
layout: default
title: Cidofovir
parent: Solo predicción del modelo (L5)
nav_order: 179
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-20
description: "Cidofovir: nueva indicación predicha, Colangitis esclerosante (nivel de evidencia L5). Indicación original: No disponible en los datos compilados para este informe (el texto de…"
monitor_inn: "CIDOFOVIR"
predicted_indications: ["sclerosing cholangitis", "rheumatoid arthritis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Cidofovir
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

## Cidofovir: De Indicación Original No Registrada a Colangitis Esclerosante
{: .text-alpha }

## Resumen en Una Frase

Cidofovir es un análogo nucleotídico antiviral que inhibe la ADN polimerasa viral y que actualmente está comercializado en España como concentrado para solución para perfusión.
El modelo TxGNN predice que podría ser efectivo para **colangitis esclerosante**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados para este informe (el texto de indicación de la autorización está vacío) |
| Nueva Indicación Predicha | Colangitis esclerosante |
| Puntaje de Predicción TxGNN | 0.9994 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Cidofovir (traducción no oficial): «El cidofovir suprime la replicación del citomegalovirus (CMV) mediante la inhibición selectiva de la síntesis del ADN viral. Los datos bioquímicos respaldan la inhibición selectiva de la ADN polimerasa del CMV por el difosfato de cidofovir, el metabolito intracelular activo del cidofovir.» Texto original en inglés: "Cidofovir suppresses cytomegalovirus (CMV) replication by selective inhibition of viral DNA synthesis. Biochemical data support selective inhibition of CMV DNA polymerase by cidofovir diphosphate, the active intracellular metabolite of cidofovir." ([DailyMed: Cidofovir (cidofovir anhydrous) prescribing information, Mylan Institutional LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=56541229-8c1a-4550-8951-2415ed08e7e9), versión del 2021-04-15; consultado el 2026-11-19). Según la información conocida, cidofovir es un análogo nucleotídico que inhibe la ADN polimerasa viral, y se utiliza como antiviral en infecciones por citomegalovirus y otros virus de ADN.

La colangitis esclerosante es principalmente una enfermedad de origen inmunomediado. Un vínculo plausible sería solo indirecto, por ejemplo una colangiopatía de origen viral (como CMV) en pacientes inmunodeprimidos. Por ello, la justificación mecanística directa es débil.

El puntaje TxGNN muy alto (0.9994) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; no está respaldado por evidencia clínica ni bibliográfica. Además, la nefrotoxicidad significativa de cidofovir va en contra de su uso en este contexto.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para colangitis esclerosante.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 81303 | Cidofovir Zentiva 75 mg/ml concentrado para solución para perfusión EFG | Concentrado para solución para perfusión | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (relaciones fármaco-enfermedad de TxGNN/PrimeKG, no del texto del prospecto): enfermedad renal, piouréter, trastorno acidótico y acidosis láctica adquirida.
- **Interacciones farmacológicas**: se identificaron 55 interacciones en total. Entre las principales, de nivel **Mayor**:
  - Anfotericina B (incluidas las formulaciones lipídica, de sulfato de colesterilo y liposomal)
  - Aminoglucósidos: kanamicina, neomicina, estreptomicina
  - Polimixina B y vancomicina
  - Salicilatos y derivados de la 5-ASA: mesalazina, balsalazida, olsalazina, sulfasalazina
  - Quelantes del hierro: deferasirox, deferoxamina
  - Medios de contraste y radiofármacos: diatrizoato, iodipamida, iobenguano (I-131)
  
  De nivel **Moderado**: exenatida y trospio.

  Muchas de estas combinaciones comparten el riesgo de toxicidad renal aditiva.
- Consultar el prospecto para el resto de la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para colangitis esclerosante es solo computacional (nivel L5), sin ensayos ni literatura de respaldo, con un mecanismo directo poco plausible y un perfil de nefrotoxicidad desfavorable.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y de la indicación autorizada, obtenidos del prospecto y de DrugBank
- Advertencias y contraindicaciones del prospecto de la AEMPS
- Estudios preclínicos o series de casos que apoyen un papel antiviral en colangiopatías (por ejemplo, de origen por CMV)
- Evaluación del balance beneficio-riesgo renal en pacientes con enfermedad hepatobiliar

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Cidofovir (cidofovir anhydrous) prescribing information, Mylan Institutional LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=56541229-8c1a-4550-8951-2415ed08e7e9) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


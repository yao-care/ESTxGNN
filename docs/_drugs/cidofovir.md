---
layout: default
title: Cidofovir
parent: Solo predicción del modelo (L5)
nav_order: 179
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
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
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, cidofovir es un análogo nucleotídico que inhibe la ADN polimerasa viral, y se utiliza como antiviral en infecciones por citomegalovirus y otros virus de ADN.

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


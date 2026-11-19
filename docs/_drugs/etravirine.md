---
layout: default
title: Etravirine
parent: Solo predicción del modelo (L5)
nav_order: 320
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-05
monitor_inn: "Etravirine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "benign prostate phyllodes tumor", "obsolete familial combined hyperlipidemia"]
description: "Etravirine: nueva indicación predicha, Síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome) (nivel de evidencia L5). Indicación original: No consta en los datos …"
---

# Etravirine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Etravirine: Síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome)
{: .text-alpha }

## Resumen en Una Frase

Etravirina es un inhibidor no nucleosídico de la transcriptasa inversa (ITINN), originalmente utilizado para el tratamiento de la infección por VIH y el SIDA.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina**, una indicación veterinaria,
sin **ensayos clínicos** ni **publicaciones** que respalden actualmente esta dirección; la predicción se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome) |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 2; autorizadas no comercializadas: 1) |
| Número de Autorizaciones | 2 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Etravirine (traducción no oficial): «La etravirina es un fármaco antirretroviral. […] La etravirina es un INNTI del VIH-1. La etravirina se une directamente a la transcriptasa inversa (TI) y bloquea las actividades de ADN polimerasa dependientes de ARN y dependientes de ADN al provocar una alteración del sitio catalítico de la enzima. La etravirina no inhibe las ADN polimerasas humanas α, β y γ.» Texto original en inglés: "Etravirine is an antiretroviral drug. […] Etravirine is an NNRTI of HIV-1. Etravirine binds directly to reverse transcriptase (RT) and blocks the RNA-dependent and DNA-dependent DNA polymerase activities by causing a disruption of the enzyme's catalytic site. Etravirine does not inhibit the human DNA polymerases α, β, and γ." ([DailyMed: Intelence (etravirine) prescribing information, Janssen Products LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6a9cbc29-9f15-4b24-8d86-206b82887f3d), versión del 2023-08-15; consultado el 2026-11-19). Según la información conocida, la etravirina es un ITINN que inhibe la transcriptasa inversa del VIH-1, y su eficacia en la infección por VIH ha sido comprobada.

El virus de la inmunodeficiencia felina (VIF) es un lentivirus, por lo que existe cierta cercanía biológica con el VIH. Sin embargo, los ITINN suelen tener poca actividad frente a lentivirus distintos del VIH-1, de modo que el vínculo es solo una predicción del modelo basada en similitud entre enfermedades, sin datos que la respalden.

Además, se trata de una indicación veterinaria, fuera del alcance del reposicionamiento de fármacos en humanos. Esta predicción debe interpretarse con mucha cautela.

### Otras predicciones del modelo (contexto)

- **Infección por virus de inmunodeficiencia simia (VIS)** (0.9998, nivel L4): solo hay un estudio in vitro de nanopartículas con combinaciones antirretrovirales (PMID 26529558), con relevancia indirecta. Los ITINN suelen ser poco activos frente al VIS y el VIH-2 por polimorfismos naturales de resistencia.
- La literatura disponible trata de seguridad, resistencia y casos en embarazo, no de eficacia nueva.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal predicha (síndrome de inmunodeficiencia adquirida felina).

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 08468001 | INTELENCE 100 MG COMPRIMIDOS | Comprimido | No disponible en los datos compilados |
| 08468002 | INTELENCE 200 MG COMPRIMIDOS | Comprimido | No disponible en los datos compilados |

Titular: Janssen-Cilag International N.V. Ambas autorizaciones son de medicamento único y están vigentes.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): hepatitis C crónica, infección por virus de la hepatitis C, hepatitis B crónica, enfermedad del sistema nervioso periférico y neuropatía periférica.
- **Interacciones farmacológicas**: se identificaron 100 interacciones potenciales. Entre las de nivel moderado destacan:
  - Inhibidores de la bomba de protones: omeprazol, rabeprazol.
  - Antagonistas H2: cimetidina (ranitidina es de nivel menor).
  - Corticosteroides: hidrocortisona, dexametasona, betametasona, triamcinolona.
  - Antidiabéticos: pioglitazona, glimepirida, clorpropamida, saxagliptina, linagliptina.
  - Otros: claritromicina, aprepitant, metronidazol, dronabinol, eliglustat, naloxegol, naldemedina.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no están disponibles en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal no tiene ensayos clínicos ni literatura, el nivel de evidencia es L5, la indicación es veterinaria y el mecanismo (los ITINN son poco activos frente a lentivirus no VIH-1) la hace poco plausible.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y de la actividad antiviral frente al VIF.
- Advertencias y contraindicaciones del prospecto de la AEMPS (carencia bloqueante para el cribado de seguridad).
- Textos de indicación aprobada de las autorizaciones españolas.
- Confirmar si la indicación veterinaria está dentro del alcance del programa; de lo contrario, priorizar candidatas humanas con mayor respaldo (p. ej., VIH en embarazo, que es una extensión de la indicación aprobada con seguridad por evaluar).

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Intelence (etravirine) prescribing information, Janssen Products LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6a9cbc29-9f15-4b24-8d86-206b82887f3d) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


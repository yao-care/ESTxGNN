---
layout: default
title: Tenofovir Alafenamide
parent: Solo predicción del modelo (L5)
nav_order: 776
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "Tenofovir alafenamide"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
description: "Tenofovir Alafenamide: nueva indicación predicha, Síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome) (nivel de evidencia L5). Indicación original: No consta en…"
---

# Tenofovir Alafenamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Tenofovir Alafenamide: Síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome)
{: .text-alpha }

## Resumen en Una Frase

Tenofovir alafenamida es un inhibidor nucleotídico de la transcriptasa inversa, originalmente utilizado para el tratamiento de la infección por VIH/sida (en España está comercializado como Vemlidy).
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta predicción. Se trata además de una indicación veterinaria.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome) |
| Puntaje de Predicción TxGNN | 0.9989 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Tenofovir Alafenamide (traducción no oficial): «El tenofovir alafenamida es un fármaco antiviral contra el virus de la hepatitis B. […] El tenofovir alafenamida es un profármaco fosfonamidato del tenofovir (análogo del monofosfato de 2'-desoxiadenosina). El tenofovir alafenamida, como compuesto lipofílico permeable a las células, entra en los hepatocitos primarios por difusión pasiva y mediante los transportadores de captación hepática OATP1B1 y OATP1B3.» Texto original en inglés: "Tenofovir alafenamide is an antiviral drug against the hepatitis B virus. […] Tenofovir alafenamide is a phosphonamidate prodrug of tenofovir (2'-deoxyadenosine monophosphate analog). Tenofovir alafenamide as a lipophilic cell-permeant compound enters primary hepatocytes by passive diffusion and by the hepatic uptake transporters OATP1B1 and OATP1B3." ([DailyMed: Vemlidy (tenofovir alafenamide) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=72e6b33c-0351-4070-9172-eeaa186c01d2), versión del 2025-07-14; consultado el 2026-11-19). Según la información conocida, tenofovir alafenamida es un profármaco de tenofovir que actúa como inhibidor nucleotídico de la transcriptasa inversa (NRTI), y su eficacia en la infección por VIH está establecida.

El virus de la inmunodeficiencia felina (FIV) es un lentivirus que, al igual que el VIH, depende de la transcriptasa inversa para replicarse. Por ello, mecanísticamente es plausible que el fármaco tenga actividad, y el alto puntaje de TxGNN refleja esta similitud con la indicación original.

Sin embargo, esta es una indicación veterinaria, que queda fuera del reposicionamiento de fármacos en humanos, y no se aportó ninguna evidencia directa. La predicción debe considerarse solo una hipótesis computacional.

**Otras predicciones del modelo (para contexto):**
- **Infección por virus de inmunodeficiencia símica (SIV)** (puntaje 0,9989, nivel L4): 8 publicaciones preclínicas en macacos y ratones humanizados (PrEP oral y tópica, profilaxis posexposición, implantes, remisión de SHIV). Respaldan la actividad antiviral en modelos animales, pero son evidencia traslacional de la indicación VIH ya existente, no una nueva indicación humana.
- **Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y disminución de la sustancia blanca cortical** (puntaje 0,9987, nivel L5): no se identificó un vínculo mecanístico claro; la predicción carece de sustento.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la indicación predicha.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación predicha (síndrome de inmunodeficiencia adquirida felina).

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 1161154001 | VEMLIDY 25 MG COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Gilead Sciences Ireland Unlimited Company | Comercializada |

Se muestra la única autorización con este principio activo en los datos de CIMA (AEMPS).

<!-- licenses:end -->

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Los datos compilados registran una interacción farmacológica de tipo farmacológico con el receptor del gusto amargo TAS2R39 (el fármaco actúa como ligando); no se trata de una interacción medicamentosa con relevancia clínica establecida y no se dispone de nivel de gravedad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal se apoya únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y corresponde a una indicación veterinaria fuera del alcance del reposicionamiento en humanos. Las publicaciones preclínicas sobre SIV/SHIV refuerzan la actividad antiviral conocida, pero no constituyen una nueva indicación humana.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank
- Advertencias y contraindicaciones del prospecto de la AEMPS (necesarias para cualquier cribado de seguridad)
- Texto de la indicación aprobada de la autorización en España
- Decidir si la indicación veterinaria está dentro del alcance; de lo contrario, priorizar predicciones con relevancia en humanos
- Estudios in vitro o in vivo en FIV si se quisiera explorar la hipótesis veterinaria

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Vemlidy (tenofovir alafenamide) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=72e6b33c-0351-4070-9172-eeaa186c01d2) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


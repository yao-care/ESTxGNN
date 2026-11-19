---
layout: default
title: Azithromycin
parent: Solo predicción del modelo (L5)
nav_order: 84
evidence_level: L5
indication_count: 10
monitor_inn: "Azithromycin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
last_modified_at: 2026-11-05
description: "Azithromycin: nueva indicación predicha, síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: al menos 20"
---

# Azithromycin
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

## Azitromicina: antibiótico macrólido → síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)
{: .text-alpha }

## Resumen en Una Frase

Azitromicina es un antibiótico macrólido de uso antibacteriano.
El modelo TxGNN predice que podría ser efectivo para **síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome)**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | síndrome de hiperviscosidad policlonal (polyclonal hyperviscosity syndrome) |
| Puntaje de Predicción TxGNN | 0.9981 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 12; autorizadas no comercializadas: 2; revocadas o suspendidas: 6) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según las secciones «Mechanism of Action» y «Microbiology» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Azithromycin (traducción no oficial): «La azitromicina es un fármaco antibacteriano macrólido. […] La azitromicina actúa uniéndose al ARNr 23S de la subunidad ribosómica 50S de los microorganismos sensibles, lo que inhibe la síntesis de proteínas bacterianas e impide el ensamblaje de la subunidad ribosómica 50S.» Texto original en inglés: "Azithromycin is a macrolide antibacterial drug. […] Azithromycin acts by binding to the 23S rRNA of the 50S ribosomal subunit of susceptible microorganisms inhibiting bacterial protein synthesis and impeding the assembly of the 50S ribosomal subunit." ([DailyMed: Zithromax (azithromycin dihydrate) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8d24bacb-feff-4c6a-b8df-625e1435387a), versión del 2026-09-09; consultado el 2026-11-19). Según la información conocida, azitromicina es un macrólido con actividad antibacteriana y efectos inmunomoduladores y antiinflamatorios.

Los datos compiladas para este informe no muestran un vínculo mecanístico plausible entre estas acciones y la hiperviscosidad sérica. El puntaje alto (0.9981) refleja solo una predicción basada en el modelo, sin respaldo de estudios reales. Por ello, la razonabilidad biológica de esta predicción es débil y debe tratarse como una hipótesis sin sustento.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Hay autorizaciones vigentes en España (13 vigentes según los datos locales; el listado puede ser parcial). Principales presentaciones:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 66065 | Azitromicina Normon 500 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No registrada en los datos locales |
| 82363 | Azitromicina Teva 250 mg comprimidos dispersables | Comprimido dispersable | No registrada en los datos locales |
| 65636 | Azitromicina Sandoz 500 mg polvo para suspensión oral en sobre EFG | Polvo para suspensión oral | No registrada en los datos locales |
| 85006 | Azitromicina Tecnigen 500 mg polvo para solución para perfusión EFG | Polvo para solución para perfusión | No registrada en los datos locales |
| 59620 | Zitromax 250 mg polvo para suspensión oral en sobre | Polvo para suspensión oral | No registrada en los datos locales |

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: los datos compilados solo recogen interacciones farmacológicas con dianas (receptor de motilina y TAS2R4), sin interacciones con otros medicamentos de relevancia clínica.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos clínicos ni literatura, y no se identifica un mecanismo plausible que vincule la azitromicina con la hiperviscosidad policlonal. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Una hipótesis mecanística justificada entre la azitromicina y la hiperviscosidad sérica
- Estudios preclínicos o clínicos que evalúen directamente esta enfermedad
- Datos del mecanismo de acción (MOA)
- Advertencias y contraindicaciones del prospecto de la AEMPS para el análisis de seguridad

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Zithromax (azithromycin dihydrate) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8d24bacb-feff-4c6a-b8df-625e1435387a) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


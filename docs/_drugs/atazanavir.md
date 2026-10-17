---
layout: default
title: Atazanavir
parent: Solo predicción del modelo (L5)
nav_order: 72
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Atazanavir: nueva indicación predicha, Síndrome de inmunodeficiencia adquirida felina (nivel de evidencia L5). Indicación original: Infección por VIH / SIDA (según el grafo de conocimiento"
monitor_inn: "ATAZANAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
---

# Atazanavir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Atazanavir: De Infección por VIH a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Atazanavir es un inhibidor de la proteasa del VIH-1, utilizado originalmente para el tratamiento de la infección por VIH y el SIDA.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción concreta; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH / SIDA (según el grafo de conocimiento; los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 19 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, atazanavir es un inhibidor de la proteasa del VIH-1, su eficacia en la infección por VIH ha sido comprobada, y mecanísticamente podría ser aplicable a otros lentivirus.

El virus de la inmunodeficiencia felina (FIV) es un lentivirus con una proteasa relacionada con la del VIH-1, por lo que existe una justificación mecanística teórica. Sin embargo, la proteasa del FIV difiere en especificidad de sustrato y sensibilidad a los inhibidores, y no se aportaron datos que respalden la actividad de atazanavir frente a ella.

El puntaje elevado de TxGNN probablemente refleja la cercanía en la red de conocimiento con el VIH/SIDA, y no una evidencia independiente. Además, se trata de una enfermedad veterinaria, por lo que su relevancia para el reposicionamiento en humanos es limitada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

*Nota:* para la segunda predicción (infección por virus de inmunodeficiencia simia) solo se identificó un estudio en macacos tratados con terapia antirretroviral combinada (PMID 20497048, 2010), que es indirecto y no aísla el efecto de atazanavir.

## Información de Mercado en España

Se listan 5 de las 19 autorizaciones vigentes (todas de principio activo único):

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 03267004 | REYATAZ 150 mg cápsulas duras | Cápsula dura | No especificada en los datos |
| 03267002 | REYATAZ 100 mg cápsulas duras | Cápsula dura | No especificada en los datos |
| 03267006 | REYATAZ 200 mg cápsulas duras | Cápsula dura | No especificada en los datos |
| 03267008 | REYATAZ 300 mg cápsulas duras | Cápsula dura | No especificada en los datos |
| 80655 | Atazanavir Teva 300 mg cápsulas duras EFG | Cápsula dura | No especificada en los datos |

## Consideraciones de Seguridad

- **Posibles enfermedades de precaución (según el grafo de conocimiento, no texto del prospecto)**: insuficiencia y enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, diabetes mellitus, cetoacidosis diabética, hepatitis B y C crónicas, hemofilia, hiperbilirrubinemia (incluido síndrome de Gilbert), nefrolitiasis, nefropatía aguda por uratos, bloqueo auriculoventricular y acidosis láctica.
- **Interacciones farmacológicas**: se registraron 100 interacciones; entre las de nivel **Mayor** destacan famotidina, ranitidina, rabeprazol, omeprazol (antiácidos/inhibidores de la bomba de protones, por reducción de la absorción), loperamida, triamcinolona y budesonida. Entre las de nivel **Moderado** figuran acarbosa, hidrocortisona, metformina, pioglitazona, alosetrón, aprepitant, betametasona, hidróxido de aluminio y carbonato de calcio.

Para advertencias y contraindicaciones formales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal se basa solo en el modelo (nivel L5), sin ensayos ni literatura, y corresponde a una enfermedad veterinaria con diferencias relevantes en la proteasa viral. Las otras predicciones con literatura (VIH congénito, complejo relacionado con el SIDA) solapan con la indicación ya aprobada, por lo que no constituyen un reposicionamiento real.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y de la actividad de atazanavir frente a la proteasa del FIV (estudios enzimáticos y celulares in vitro).
- Evidencia preclínica o clínica específica en la indicación predicha.
- Textos de indicación y advertencias/contraindicaciones del prospecto de la AEMPS.
- Definir si el interés es veterinario o humano, ya que la indicación predicha no es aplicable a humanos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Darunavir
parent: Solo predicción del modelo (L5)
nav_order: 223
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-31
monitor_inn: "DARUNAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
description: "Darunavir: nueva indicación predicha, Síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome) (nivel de evidencia L5). Indicación original: No consta en los datos l…"
---

# Darunavir
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

## Darunavir: Síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome)
{: .text-alpha }

## Resumen en Una Frase

Darunavir es un inhibidor de la proteasa del VIH-1, utilizado originalmente para el tratamiento de la infección por VIH y el SIDA.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina**, aunque se trata de una indicación veterinaria.
Actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta predicción; solo se dispone de la señal del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome) |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 6) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, darunavir es un inhibidor de la proteasa del VIH-1, su eficacia en la infección por VIH ha sido comprobada, y mecanísticamente podría ser aplicable a otros lentivirus con proteasas aspárticas.

El virus de la inmunodeficiencia felina (FIV) también codifica una proteasa aspártica, por lo que existe una lógica mecanística plausible. Sin embargo, la proteasa del FIV difiere de la del VIH-1 en especificidad de sustrato y sensibilidad a los inhibidores, y los datos disponibles no respaldan la unión de darunavir a ella.

Cabe señalar que se trata de una indicación veterinaria, con relevancia limitada para el reposicionamiento en medicina humana. Como contexto, la infección por el virus de la inmunodeficiencia de los simios (SIV) obtuvo el mismo puntaje y cuenta con cuatro estudios preclínicos en macacos (nivel L4), pero son indirectos: evalúan regímenes combinados de antirretrovirales y no darunavir en solitario.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (síndrome de inmunodeficiencia adquirida felina).

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de medicamentos de un solo principio activo, en comprimidos recubiertos con película):

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 06380003 | PREZISTA 400 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 06380004 | PREZISTA 150 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 106380007 | PREZISTA 800 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 85186 | Darunavir Tarbis 800 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 83578 | Darunavir Dr. Reddys 600 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del texto del prospecto): insuficiencia hepática, enfermedad hepática, cirrosis hepática, enfermedad de la vesícula biliar, hiperglucemia, diabetes mellitus, cetoacidosis diabética, hepatitis C (aguda y crónica), hepatitis B crónica, hipertrigliceridemia y hemofilia (incluida la forma sintomática en portadoras).
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Entre las 20 reveladas, la más relevante es **cisaprida (gravedad mayor)**. Las restantes son de gravedad moderada e incluyen antidiabéticos (acarbosa, metformina, pioglitazona, alogliptina, saxagliptina, canagliflozina, dapagliflozina, clorpropamida, acetohexamida, albiglutida), corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), aprepitant y claritromicina.
- Las advertencias y contraindicaciones del prospecto de la AEMPS no están disponibles; consultar el prospecto para esa información.
- Por la clase farmacológica, y según se señala en el análisis de la indicación de hiperlipidemia, los inhibidores de la proteasa se asocian a alteraciones lipídicas, lo que debe tenerse en cuenta.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el puntaje del modelo (nivel L5), sin ensayos ni literatura, y corresponde a una indicación veterinaria con escasa relevancia para el reposicionamiento en humanos. Además, la compatibilidad de darunavir con la proteasa del FIV no está respaldada por los datos.

**Para avanzar se necesita:**
- Estudios de actividad in vitro de darunavir frente a la proteasa del FIV.
- Datos detallados del mecanismo de acción (MOA).
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones) para completar la evaluación de seguridad.
- Verificar en los textos completos el papel de darunavir en los estudios con macacos (SIV), si se quisiera explorar esa línea.
- Definir si una indicación veterinaria entra en el alcance del programa de reposicionamiento; en caso contrario, priorizar otras candidatas.
- Las otras predicciones (trastorno del neurodesarrollo raro e hiperlipidemia familiar combinada, esta última obsoleta en la ontología) carecen de vínculo mecanístico plausible y no se recomienda priorizarlas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


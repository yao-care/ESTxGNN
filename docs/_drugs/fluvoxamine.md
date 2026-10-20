---
layout: default
title: Fluvoxamine
parent: Solo predicción del modelo (L5)
nav_order: 353
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fluvoxamine: nueva indicación predicha, Trastorno esquizoide de la personalidad (nivel de evidencia L5). Indicación original: Fobia social…"
monitor_inn: "Fluvoxamine"
predicted_indications: ["schizoid personality disorder", "histrionic personality disorder (disease)", "schizotypal personality disorder", "paranoid personality disorder", "anxiety disorder", "agoraphobia", "benign paroxysmal torticollis of infancy", "dependent personality disorder", "narcissistic personality disorder", "endogenous depression"]
---

# Fluvoxamine
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

# Fluvoxamina: De Fobia Social y Trastorno Obsesivo-Compulsivo a Trastorno Esquizoide de la Personalidad

## Resumen en Una Frase

La fluvoxamina es un inhibidor selectivo de la recaptación de serotonina (ISRS), utilizado originalmente para la fobia social, los trastornos fóbicos y el trastorno obsesivo-compulsivo (TOC).
El modelo TxGNN predice que podría ser eficaz para el **trastorno esquizoide de la personalidad**,
pero actualmente hay **0 ensayos clínicos** y **1 publicación** de apoyo indirecto, por lo que se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Fobia social, trastorno fóbico y trastorno obsesivo-compulsivo (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no estaban disponibles) |
| Nueva Indicación Predicha | Trastorno esquizoide de la personalidad |
| Puntaje de Predicción TxGNN | 99,997 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen una descripción detallada del mecanismo de acción. Sí muestran que la fluvoxamina actúa sobre el transportador de serotonina (SERT, gen *SLC6A4*), que inhibe, y que tiene alta afinidad por el receptor sigma-1 (*SIGMAR1*), sobre el que parece actuar como agonista. Es un ISRS cuya eficacia está demostrada en la fobia social y el TOC.

El modelo asocia estas indicaciones con el trastorno esquizoide de la personalidad porque comparten un entorno de enfermedades psiquiátricas y dianas serotoninérgicas dentro del grafo de conocimiento. Es una similitud estadística del grafo, no una justificación farmacológica probada.

No se ha establecido un vínculo mecanístico directo. La única publicación asociada (PMID 10929788) describe los trastornos de personalidad en pacientes con trastorno dismórfico corporal, algunos de los cuales participaron en un estudio con fluvoxamina. No evalúa la fluvoxamina como tratamiento del trastorno esquizoide.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10929788](https://pubmed.ncbi.nlm.nih.gov/10929788/) | 2000 | Estudio de cohorte | Comprehensive Psychiatry | Evaluó trastornos y rasgos de personalidad en 148 personas con trastorno dismórfico corporal, 26 de las cuales participaron en un estudio de tratamiento con fluvoxamina. No prueba la fluvoxamina para el trastorno esquizoide. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 57233 | DUMIROX 50 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 58212 | DUMIROX 100 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 63277 | FLUVOXAMINA SANDOZ 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 63276 | FLUVOXAMINA SANDOZ 50 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |

Las cuatro autorizaciones son de medicamentos con un solo principio activo y están vigentes. Pertenecen a Viatris Healthcare Limited (Dumirox) y Sandoz Farmacéutica S.A. (Fluvoxamina Sandoz).

## Consideraciones de Seguridad

- **Contraindicaciones o enfermedades de riesgo según el grafo de conocimiento** (no proceden del texto del prospecto): epilepsia, trastorno bipolar, trastorno afectivo mayor, enfermedad hepática, enfermedad de la vesícula biliar, trastornos de la coagulación, síndrome neuroléptico maligno, síndrome de secreción inapropiada de ADH, síndrome nefrogénico de antidiuresis inapropiada y síndrome serotoninérgico.
- **Perfil farmacológico**: la fluvoxamina se une al transportador de serotonina (SERT) y al receptor sigma-1. Los datos compilados no incluyen interacciones medicamentosas clínicas específicas.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en el modelo, pero no cuenta con ensayos clínicos y solo con una publicación indirecta que no evalúa la fluvoxamina para este trastorno. La evidencia es de nivel L5 (solo predicción del modelo).

**Para avanzar se necesita:**
- Estudios clínicos o series de casos que prueben directamente la fluvoxamina en el trastorno esquizoide de la personalidad.
- Una justificación mecanística específica que vaya más allá de la cercanía en el grafo de conocimiento.
- Las advertencias y contraindicaciones oficiales del prospecto de la AEMPS, así como los textos de indicación aprobados.
- Datos detallados del mecanismo de acción.

**Nota adicional:** en las demás predicciones de este análisis hay candidatos con evidencia más sólida, ambos con decisión *Proceed with Guardrails*:
- **Trastorno de ansiedad**: nivel L1, con ensayos de Fase 3 y metaanálisis.
- **Agorafobia**: nivel L2, con ensayos aleatorizados doble ciego en trastorno de pánico.

También destaca la **depresión endógena** (nivel L2), con un ensayo de Fase 2 en curso (NCT04160377). Estos tres casos son sobre todo extensiones de la familia de indicaciones originales, más que un reposicionamiento nuevo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


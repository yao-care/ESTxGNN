---
layout: default
title: Mirtazapine
parent: Solo predicción del modelo (L5)
nav_order: 358
evidence_level: L5
indication_count: 3
---

# Mirtazapine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Mirtazapina: De Trastorno Depresivo Mayor a Síndrome de Ohdo y Variantes

## Resumen en Una Frase

La mirtazapina es un antidepresivo cuyo uso clínico descrito es el tratamiento del trastorno depresivo mayor.
El modelo TxGNN predice que podría ser efectiva para el **síndrome de Ohdo y variantes**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es una predicción exclusivamente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno depresivo mayor (según los datos de farmacología; los textos de indicación de las autorizaciones de la AEMPS están vacíos) |
| Nueva Indicación Predicha | Síndrome de Ohdo y variantes |
| Puntaje de Predicción TxGNN | 99.42% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro del fármaco. Los datos de farmacología muestran que la mirtazapina tiene mayor afinidad por los adrenoceptores α2 (A, B y C, con antagonismo) y por los receptores serotoninérgicos 5-HT2A y 5-HT2C. En general también se describe un antagonismo sobre 5-HT3 y H1, aunque este dato no está en el registro.

**No se ha establecido un vínculo mecanístico** entre este perfil de receptores y el síndrome de Ohdo. Este síndrome (relacionado con KAT6B) es un trastorno de regulación de la cromatina con manifestaciones del desarrollo, y no se identificó ninguna conexión farmacológica plausible. El puntaje alto (0.994) proviene solo del grafo de conocimiento y no constituye evidencia clínica.

Las otras dos predicciones del modelo tampoco tienen respaldo:
- **Blefarofimosis con discapacidad intelectual, tipo Ohdo** (99.11%): es casi un duplicado de la primera, por lo que ambos puntajes no son evidencia independiente. No hay fundamento para un beneficio sintomático ni modificador de la enfermedad.
- **Tortícolis paroxística benigna de la infancia** (99.11%): es un equivalente migrañoso asociado a canalopatía CACNA1A. La modulación serotoninérgica y adrenérgica tiene una relación laxa con la migraña, pero no está verificada para la mirtazapina. Además, la enfermedad es autolimitada y faltan datos de seguridad en lactantes.

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones registradas. El registro no incluye el texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 90891 | Mirtazapina Stada 45 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en el registro |
| 71841 | Mirtazapina Flas Kern Pharma 15 mg comprimidos bucodispersables EFG | Comprimido bucodispersable | No disponible en el registro |
| 89479 | Mirtazapina Sandoz 30 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en el registro |
| 69802 | Mirtazapina Qualigen 15 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en el registro |
| 66982 | Mirtazapina Alter 15 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en el registro |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5): no hay ensayos clínicos, no hay literatura y no se ha identificado un vínculo mecanístico plausible. Las predicciones adicionales del mismo caso también carecen de respaldo, y en la de tortícolis infantil la falta de datos de seguridad pediátrica agrava el riesgo.

**Para avanzar se necesita:**
- Obtener del prospecto de la AEMPS las advertencias y contraindicaciones, y las indicaciones aprobadas de cada autorización.
- Completar los datos del mecanismo de acción (MOA) desde DrugBank.
- Una revisión de literatura que busque evidencia preclínica o mecanística que vincule la mirtazapina con la vía de KAT6B o con la regulación de la cromatina.
- Volver a evaluar la candidatura solo si aparece evidencia que respalde un vínculo mecanístico; de lo contrario, priorizar otras candidaturas.

*Este informe es solo para referencia de investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


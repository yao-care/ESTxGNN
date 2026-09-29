---
layout: default
title: Secnidazole
parent: Solo predicción del modelo (L5)
nav_order: 485
evidence_level: L5
indication_count: 7
---

# Secnidazole
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Secnidazol: De Antimicrobiano 5-nitroimidazol (Infecciones Anaerobias y Protozoarias) a Vaginitis Atrófica Posmenopáusica

## Resumen en Una Frase

Secnidazol es un antimicrobiano de la familia de los 5-nitroimidazoles, dirigido a infecciones anaerobias y protozoarias. La ficha de AEMPS no incluye el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **vaginitis atrófica posmenopáusica**, pero para esta indicación hay **0 ensayos clínicos** y **0 publicaciones** que respalden la predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Vaginitis atrófica posmenopáusica |
| Puntaje de Predicción TxGNN | 99,70% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro del fármaco. Según la información conocida, secnidazol es un 5-nitroimidazol que se reduce dentro de organismos anaerobios y protozoos y les daña el ADN. Por eso se usa en infecciones como la vaginosis bacteriana y la tricomoniasis.

**En este caso la predicción no es razonable.** La vaginitis atrófica se debe a la falta de estrógenos y al adelgazamiento del epitelio vaginal, no a una infección anaerobia o protozoaria. No existe un vínculo mecanístico plausible entre la acción antimicrobiana de secnidazol y esta enfermedad.

El puntaje alto de TxGNN (99,70%) es solo una predicción del modelo. Probablemente refleja la cercanía, en el grafo de conocimiento, con nodos de infecciones vaginales, y no un efecto terapéutico real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 90874 | DEIRON 2 G GRANULADO EN SOBRE (Faes Farma S.A.) | Granulado en sobre | No especificada en el registro |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. La consulta de interacciones farmacológicas no devolvió resultados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos ni publicaciones para vaginitis atrófica posmenopáusica y no existe un mecanismo plausible. La predicción parece un artefacto del grafo de conocimiento, por lo que no se recomienda avanzar con esta indicación.

**Otras predicciones del mismo análisis:**
- **Flujo vaginal** (puntaje 99,41%) y **vulvovaginitis tricomonal** (puntaje 99,37%) tienen nivel L1 y recomendación *Proceed with Guardrails*. Las respaldan ensayos de Fase 3 controlados con placebo, como el de vaginosis bacteriana (PMID 28867602) y el de tricomoniasis (PMID 33768237). Son más bien confirmaciones de un uso ya establecido que un reposicionamiento real.
- Para el flujo vaginal, la indicación debe definirse por etiología (vaginosis bacteriana o tricomoniasis) y no solo por el síntoma.
- **Candidiasis vulvovaginal** (nivel L3) sigue como pregunta de investigación. El único ensayo de Fase 3 usa la combinación con fluconazol y no permite aislar el efecto de secnidazol.
- El resto de las predicciones (úlcera vulvar, neoplasia vulvar, leucoplasia vaginal) quedan en L5 con recomendación Hold.

**Para avanzar se necesita:**
- Obtener del prospecto de AEMPS las advertencias, contraindicaciones y la indicación aprobada de DEIRON.
- Completar los datos de mecanismo de acción desde DrugBank.
- Para cualquier indicación con evidencia, redactar un plan con confirmación diagnóstica (PCR de ácidos nucleicos o microscopía), tratamiento de parejas y consejería sobre alcohol, embarazo y lactancia.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


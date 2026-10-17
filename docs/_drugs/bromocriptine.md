---
layout: default
title: Bromocriptine
parent: Solo predicción del modelo (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bromocriptine: nueva indicación predicha, Defecto congénito de glucosilación con fucosilación defectuosa (nivel de evidencia L5). Indicación original: Enfermedad de Parkinson (según el grafo de conoc…"
monitor_inn: "Bromocriptine"
predicted_indications: ["congenital disorder of glycosylation with defective fucosylation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "retinal dystrophy with or without extraocular anomalies", "atypical glycine encephalopathy", "myopia 26, X-linked, female-limited", "hydranencephaly (disease)", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "schizophrenia", "syndromic myopia"]
---

# Bromocriptine
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

# Bromocriptina: De Enfermedad de Parkinson a Defecto Congénito de Glucosilación con Fucosilación Defectuosa

## Resumen en Una Frase

Bromocriptina es un agonista dopaminérgico D2, originalmente utilizado para tratar la enfermedad de Parkinson, la hiperprolactinemia y la acromegalia.
El modelo TxGNN predice que podría ser efectiva para el **defecto congénito de glucosilación con fucosilación defectuosa**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Parkinson (según el grafo de conocimiento; el texto de indicación de las autorizaciones españolas no está disponible) |
| Nueva Indicación Predicha | Defecto congénito de glucosilación con fucosilación defectuosa |
| Puntaje de Predicción TxGNN | 99.83% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, bromocriptina es un derivado ergotínico que actúa principalmente como agonista de los receptores dopaminérgicos D2 (con actividad adicional sobre receptores D1, D3-D5, serotoninérgicos 5-HT y adrenérgicos α2). Su eficacia en la enfermedad de Parkinson, la hiperprolactinemia y la acromegalia está bien establecida.

Para la nueva indicación predicha **no se ha identificado ningún vínculo mecanístico plausible**. La enfermedad es un trastorno congénito de la glucosilación y no existe una conexión conocida entre la agonista dopaminérgico y las vías de fucosilación. El puntaje de TxGNN es muy alto (0.998), pero refleja únicamente una asociación computacional en el grafo de conocimiento, sin respaldo clínico ni bibliográfico. Esta predicción debe considerarse una hipótesis sin fundamento mecanístico actual.

### Otras predicciones del modelo (contexto)

Entre las 10 principales predicciones, solo algunas cuentan con algún dato asociado:

- **Distrofia retiniana con o sin anomalías extraoculares (puntaje 99.82%, L4):** un estudio preclínico de 2024 (Nature Communications) con una combinación de tamsulosina, metoprolol y bromocriptina, y un reporte de 1991 sobre el síndrome de Goldmann-Favre tratado con ciclosporina A y bromocriptina. Evidencia débil, sin datos humanos controlados.
- **Esquizofrenia (puntaje 99.73%, L4):** un ensayo de Fase 4 abierto (NCT03575000, n=15, aún sin reclutar) evalúa bromocriptina adyuvante para alteraciones metabólicas (prediabetes) en pacientes con esquizofrenia, no para la psicosis. Existe un reporte de caso de esquizofrenia inducida por bromocriptina, lo que plantea una preocupación de seguridad psiquiátrica.
- El resto (miopía, hidranencefalia, Charcot-Marie-Tooth, encefalopatía atípica por glicina, etc.) carece de evidencia propia; el único artículo vinculado a hidranencefalia es una revisión sobre prolactinomas gigantes, probablemente una coincidencia espuria.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 54633 | PARLODEL 2,5 mg COMPRIMIDOS | Comprimido | No disponible en los datos compilados |
| 56200 | PARLODEL 5 mg CÁPSULAS | Cápsula dura | No disponible en los datos compilados |

Ambas autorizaciones están vigentes, son monofármaco y su titular es Exeltis Healthcare S.L.

## Consideraciones de Seguridad

- **Contraindicaciones asociadas en el grafo de conocimiento** (no proceden del texto del prospecto): trastornos hipertensivos e hipertensión, enfermedad hepática, enfermedad de la vesícula biliar, enfermedad arterial coronaria, accidente cerebrovascular y trastornos cerebrovasculares, infarto cerebral, preeclampsia (leve y grave) y síndrome HELLP.
- **Perfil farmacológico/interacciones:** se registraron 16 interacciones de tipo farmacológico con dianas de bromocriptina: receptores serotoninérgicos (5-HT1A, 1B, 1D, 2A, 2B, 2C, 6, 7), adrenérgicos α2 (A, B, C) y dopaminérgicos (D1-D5). No se dispone de interacciones con otros fármacos clasificadas por nivel de gravedad.
- **Preocupación psiquiátrica:** existe un reporte de caso de psicosis/esquizofrenia inducida por bromocriptina (PMID 8120934), relevante si se considerara cualquier uso en trastornos psiquiátricos.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal se basa solo en el modelo computacional (L5), sin ensayos, literatura ni vínculo mecanístico conocido entre el agonismo dopaminérgico D2 y la fucosilación.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y análisis de un posible vínculo con las vías de glucosilación/fucosilación
- Estudios preclínicos (in vitro o en modelos celulares) que justifiquen la hipótesis
- Texto de indicaciones y advertencias/contraindicaciones del prospecto de AEMPS
- Priorizar, si se desea explorar reposicionamiento, candidatas con algún respaldo (distrofia retiniana, con evidencia preclínica; esquizofrenia con comorbilidad metabólica, con evaluación de seguridad psiquiátrica)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


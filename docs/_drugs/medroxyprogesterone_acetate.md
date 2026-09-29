---
layout: default
title: Medroxyprogesterone Acetate
parent: Solo predicción del modelo (L5)
nav_order: 339
evidence_level: L5
indication_count: 10
---

# Medroxyprogesterone Acetate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Acetato de medroxiprogesterona: Hacia Amenorrea (indicación original no registrada en los datos)

## Resumen en Una Frase

El acetato de medroxiprogesterona (MPA) es un progestágeno sintético comercializado en España por Pfizer en inyectable y comprimidos, pero los datos recibidos no traen su indicación original.
El modelo TxGNN predice que podría ser efectivo para **amenorrea**, con **9 ensayos clínicos** registrados y **ninguna publicación** asociada a esta indicación.
Solo un ensayo de Fase 3 (terminado antes de tiempo) mide directamente la amenorrea como resultado.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible: los textos de indicación de las 4 autorizaciones vienen vacíos |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L2 (el paquete de datos indica L1; ver nota en la Conclusión) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el MPA es un progestágeno. La retirada de un progestágeno provoca sangrado en un endometrio preparado con estrógenos, y la exposición prolongada induce atrofia endometrial o amenorrea.

Esto convierte la predicción en algo más cercano a un uso ya conocido que a un reposicionamiento clásico. El paquete de datos señala que el MPA ya figura en ficha técnica para amenorrea secundaria. La ausencia de indicaciones originales en los datos es un vacío de información, no prueba de que no exista uso aprobado.

La principal cautela es que el único ensayo de Fase 3 directamente relevante (NCT02449161) se terminó con solo 60 pacientes y no hay resultados disponibles en los datos suministrados.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02449161](https://clinicaltrials.gov/study/NCT02449161) | Fase 3 | Terminado | 60 | ECA de MPA tras ablación endometrial, con la tasa de amenorrea endometrial como resultado. Directamente relevante, pero con poca potencia estadística por la terminación temprana |
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Fase 4 | Completado | 42 | Sangrado por retirada de progestágeno antes de inducir la ovulación con clomifeno en mujeres con oligo/amenorrea. El papel del MPA se infiere de un título truncado |
| [NCT00808132](https://clinicaltrials.gov/study/NCT00808132) | Fase 3 | Completado | 1886 | Bazedoxifeno/estrógenos conjugados en mujeres posmenopáusicas. El MPA probablemente es comparador, así que la relación con la amenorrea es indirecta |
| [NCT01463202](https://clinicaltrials.gov/study/NCT01463202) | Fase 4 | Completado | 184 | Momento de administración posparto de DMPA y lactancia. La amenorrea es un efecto secundario, no el objetivo |
| [NCT03018366](https://clinicaltrials.gov/study/NCT03018366) | Fase 2 | Completado | 29 | Riesgo cardiovascular en mujeres jóvenes con amenorrea hipotalámica funcional. El uso de MPA no está claro |
| [NCT00392093](https://clinicaltrials.gov/study/NCT00392093) | Fase 4 | Completado | 108 | Terapia hormonal y actividad del lupus en mujeres perimenopáusicas y posmenopáusicas. La amenorrea no es el objetivo |
| [NCT01300676](https://clinicaltrials.gov/study/NCT01300676) | Fase 2/3 | Completado | 79 | Miel Tualang frente a terapia hormonal en seguridad posmenopáusica. No relevante |
| [NCT07020429](https://clinicaltrials.gov/study/NCT07020429) | No aplica | Aún sin reclutar | 276 | Fórmula herbal china en insuficiencia ovárica prematura. El MPA sería, como mucho, comparador |
| [NCT06671548](https://clinicaltrials.gov/study/NCT06671548) | Fase 3 | Reclutando | 120 | Relugolix en sangrado menstrual abundante por miomas. No se puede confirmar el vínculo con el MPA |

Se omite NCT02792153 (Fase 1, retirado, 0 inscritos) por no aportar evidencia.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 46983 | DEPO-PROGEVERA 150 mg/ml | Suspensión inyectable | Pfizer S.L. |
| 59139 | PROGEVERA 10 mg | Comprimido | Pfizer S.L. |
| 42643 | PROGEVERA 5 mg | Comprimido | Pfizer S.L. |
| 57258 | FARLUTAL 500 mg | Comprimido | Pfizer S.L. |

Los textos de indicación aprobada de estas autorizaciones vienen vacíos en los datos, por lo que no se incluye esa columna.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. La consulta de interacciones farmacológicas no devolvió resultados.

Como contexto tomado de la literatura sobre otras indicaciones predichas, la combinación de estrógeno con MPA se asocia a mayor riesgo de cáncer de mama. Esto debe tenerse en cuenta en cualquier uso prolongado.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ECA de Fase 3 directamente relevante, pero terminado prematuramente con 60 pacientes y sin resultados disponibles. El resto de los ensayos es indirecto. El paquete de datos asigna L1; por las reglas de nivel (≥2 ECAs de Fase 3 completados) solo hay un Fase 3 completado y es indirecto, por lo que aquí se asigna L2. Además, el MPA ya parece estar autorizado para amenorrea secundaria, lo que respalda la plausibilidad clínica.

**Para avanzar se necesita:**
- Descargar el prospecto de la AEMPS para confirmar la indicación autorizada, las advertencias y las contraindicaciones.
- Completar los datos del mecanismo de acción (DrugBank).
- Obtener los resultados o datos publicados de NCT02449161 y revisar literatura específica de amenorrea con MPA.
- Definir un plan de monitoreo de seguridad mamaria y endometrial.

**Otras predicciones (todas en Hold):** las lesiones benignas de mama (enfermedad fibroquística, displasia mamaria benigna, adenosis) tienen evidencia escasa y antigua, con posible efecto proliferativo en mama. Las formas de endometriosis solo tienen predicción del modelo o evidencia indirecta. Las predicciones de hipoplasia renal son probables falsos positivos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


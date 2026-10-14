---
layout: default
title: Silodosin
parent: Solo predicción del modelo (L5)
nav_order: 735
evidence_level: L5
indication_count: 6
---

# Silodosin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Silodosina: De Hiperplasia Prostática Benigna a Hipertricosis Universal Congénita tipo Ambras

## Resumen en Una Frase

Silodosina es un antagonista selectivo del adrenoceptor alfa-1A, originalmente utilizado para el tratamiento de la hiperplasia prostática benigna (HPB).
El modelo TxGNN predice que podría ser efectivo para la **hipertricosis universal congénita tipo Ambras**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperplasia prostática benigna (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Silodosina es un antagonista selectivo del adrenoceptor alfa-1A, con afinidad por los subtipos alfa-1A, alfa-1B y alfa-1D según los datos farmacológicos compilados. Su acción sobre el músculo liso de próstata y cuello vesical mejora el flujo urinario en la HPB. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada.

La relación con la nueva indicación es débil. El síndrome de Ambras es un trastorno congénito raro causado por reordenamientos genómicos que afectan la regulación de TRPS1, lo que altera el desarrollo del folículo piloso. Los datos compilados no conectan el bloqueo alfa-1A con esta vía, ni existe un papel establecido del antagonismo adrenérgico alfa-1 en el crecimiento del cabello.

Por tanto, el puntaje muy alto de TxGNN (0.9999) refleja inferencia basada en el grafo, no una justificación biológica ni clínica. No debe interpretarse como evidencia de eficacia.

### Otras predicciones del modelo (todas L5, Hold)

| Rango | Indicación Predicha | Puntaje TxGNN | Comentario |
|---|---|---|---|
| 2 | Hipertricosis | 99.99% | Sin vínculo mecanístico; causas heterogéneas |
| 3 | Síndrome malformativo con componente odontológico/periodontal | 99.99% | Sin vínculo plausible |
| 4 | Síndrome con malformación de Dandy-Walker como rasgo principal | 99.98% | Defecto estructural; exposición del SNC limitada |
| 5 | Anomalía genética aislada del tallo piloso | 99.98% | Defectos estructurales de queratina |
| 6 | Tricomegalia familiar aislada | 99.23% | Rasgo familiar raro, sin relación con la señalización alfa-1A |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas monofármaco, cápsula dura). Los textos de indicación aprobada no están disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 84053 | Silodosina Stada 8 mg cápsulas duras EFG | Cápsula dura | Laboratorio Stada S.L. |
| 85271 | Xilapro 4 mg cápsulas duras EFG | Cápsula dura | Adventia Pharma S.L. |
| 84377 | Sidarso 8 mg cápsulas duras EFG | Cápsula dura | Krka D.D. Novo Mesto |
| 09607011IP | Silodyx 8 mg cápsulas duras | Cápsula dura | Recordati Ireland Limited |
| 09608004 | Urorec 4 mg cápsulas duras | Cápsula dura | Recordati Ireland Limited |

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no provienen del prospecto): atrofia multisistémica, síndrome de taquicardia postural ortostática, hipotensión ortostática, insuficiencia hepática, enfermedad renal, piouréter y síndrome del iris flácido intraoperatorio.
- **Interacciones farmacológicas**: la consulta se completó y devolvió 3 registros, que corresponden a la farmacología de sus dianas (adrenoceptores alfa-1A, alfa-1B y alfa-1D), no a interacciones con otros fármacos. No se identificaron interacciones fármaco-fármaco con nivel de gravedad asignado.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones oficiales).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5): no hay ensayos clínicos, literatura ni vínculo mecanístico plausible entre el bloqueo alfa-1A y la hipertricosis tipo Ambras. Además, no se ha completado la revisión de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener advertencias y contraindicaciones del prospecto de la AEMPS (carencia bloqueante para el cribado de seguridad).
- Completar los datos del mecanismo de acción desde DrugBank.
- Establecer una hipótesis biológica que vincule la señalización adrenérgica alfa-1A con la vía TRPS1 y el desarrollo del folículo piloso, con estudios preclínicos.
- Evaluar la compatibilidad de la vía de administración y la similitud con la indicación original (pendientes).
- Revisar la relevancia de la contraindicación por hipotensión ortostática en una población con enfermedad congénita rara.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


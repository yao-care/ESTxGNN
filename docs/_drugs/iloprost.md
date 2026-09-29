---
layout: default
title: Iloprost
parent: Solo predicción del modelo (L5)
nav_order: 272
evidence_level: L5
indication_count: 9
---

# Iloprost
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

# Iloprost: De Hipertensión Pulmonar a Hipotricosis Simple del Cuero Cabelludo

## Resumen en Una Frase

Iloprost es un análogo de la prostaciclina que en España se comercializa en solución para inhalación por nebulizador y en concentrado para perfusión. Su uso conocido es la hipertensión pulmonar, pero el texto de indicación de las autorizaciones está vacío en los datos recibidos.
El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en las autorizaciones de la AEMPS (texto vacío). La literatura del paquete indica que iloprost está aprobado para hipertensión pulmonar en adultos; requiere confirmación |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo |
| Puntaje de Predicción TxGNN | 99,45% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, iloprost es un análogo de la prostaciclina con efectos vasodilatadores y antiagregantes plaquetarios. Su eficacia en hipertensión pulmonar está descrita en la literatura, pero no hay un vínculo mecanístico demostrado con la nueva indicación.

La única hipótesis es especulativa: la señalización de prostaciclina y prostaglandinas podría influir en el ciclo del folículo piloso. Esto no está establecido para iloprost.

Además, la hipotricosis simple es un trastorno genético. Un efecto vasodilatador o antiagregante difícilmente corregiría una causa hereditaria del folículo. El alto puntaje de TxGNN (99,45%) proviene solo del grafo de conocimiento y no está respaldado por estudios reales.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 86227 | Iloprost Zentiva 20 microgramos/ml | Solución para inhalación por nebulizador | Zentiva K.S. |
| 61596 | Ilomedin 50 microgramos/0,5 ml | Concentrado para solución para perfusión | Bayer Hispania S.L. |
| 03255004 | Ventavis 10 microgramos/ml | Solución para inhalación por nebulizador | Bayer AG |
| 86242 | Iloprost Rafarm 10 microgramos/ml | Solución para inhalación por nebulizador | Rafarm S.A. |
| 86226 | Iloprost Zentiva 10 microgramos/ml | Solución para inhalación por nebulizador | Zentiva K.S. |

Las autorizaciones no incluyen texto de indicación aprobada en los datos recibidos, por lo que se omite esa columna.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es de nivel L5: sin ensayos, sin literatura y sin un mecanismo plausible para un trastorno capilar genético. Con estos datos no hay base para avanzar.

**Para avanzar se necesita:**
- Confirmar las indicaciones autorizadas y la información de seguridad en la ficha técnica de la AEMPS.
- Obtener los datos del mecanismo de acción desde DrugBank.
- Realizar estudios preclínicos que sustenten un efecto en el folículo piloso, y valorar la vía de administración, dado que las formas disponibles son inhalada e intravenosa.
- Priorizar otras predicciones del mismo paquete con más respaldo:
  - Hipertensión arterial pulmonar asociada a cardiopatía congénita (L3, Proceed with Guardrails): 1 ensayo N/A con 42 pacientes y 20 publicaciones.
  - Hipertensión arterial pulmonar asociada a VIH: incluye un ensayo de Fase 3 completado (NCT00709956) cuyo fármaco y población deben verificarse.

*Este informe es solo para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Calcifediol
parent: Solo predicción del modelo (L5)
nav_order: 94
evidence_level: L5
indication_count: 4
---

# Calcifediol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Calcifediol: De Indicación Original No Disponible a Deficiencia de Vitamina D (término obsoleto)

## Resumen en Una Frase

Calcifediol (25-hidroxivitamina D3) es el metabolito circulante de la vitamina D. Está comercializado en España, pero los registros disponibles no especifican su indicación original.
El modelo TxGNN predice que podría ser efectivo para **deficiencia de vitamina D (término obsoleto en la ontología)**,
sin **ningún ensayo clínico** ni **publicación** que respalde esta predicción concreta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los registros recibidos |
| Nueva Indicación Predicha | Deficiencia de vitamina D (término obsoleto) |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 12 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, calcifediol es el precursor inmediato de la forma activa de la vitamina D (calcitriol) y el principal indicador circulante del estado de vitamina D. Mecanísticamente podría ser aplicable a la deficiencia de vitamina D, porque repone directamente ese metabolito.

Esa plausibilidad biológica probablemente explica el puntaje tan alto (0.9999). Sin embargo, el término de enfermedad figura como **obsoleto** en la ontología. Además, no hay ensayos ni literatura asociados y no se puede confirmar si la indicación ya está autorizada. Por eso la predicción no aporta información nueva y conviene mapearla a un concepto vigente de deficiencia de vitamina D antes de evaluarla más.

**Otras indicaciones predichas con más respaldo** (no son la indicación principal de este informe):

| Indicación | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|
| Acidosis tubular renal | 99.86% | L4 | Solo 3 publicaciones (casos y un método de laboratorio). Muestran osteomalacia asociada, no corrección de la acidosis. |
| Raquitismo hipofosfatémico hereditario | 99.76% | L4 | Literatura histórica, animal y casos. En la forma ligada al X, calcifediol solo serviría como complemento. |
| Raquitismo dependiente de vitamina D | 99.18% | L4 (etapa S1) | La más sólida mecanísticamente, sobre todo en el tipo 1B (déficit de 25-hidroxilasa, CYP2R1). Es improbable que ayude en el tipo 1A o el tipo 2. |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 12 autorizaciones. El texto de indicación aprobada no figura en los registros recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 90092 | Vitode Semanal 75 microgramos cápsulas blandas | Cápsula blanda |
| 88826 | Calcifediol Normogen 0,266 mg cápsulas blandas EFG | Cápsula blanda |
| 90091 | Vitode Semanal 100 microgramos cápsulas blandas | Cápsula blanda |
| 85519 | Rayaldee 30 microgramos cápsulas blandas de liberación prolongada | Cápsula blanda de liberación prolongada |
| 55315 | Hidroferol 0,1 mg/ml gotas orales en solución | Gotas orales en solución |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal tiene nivel de evidencia L5: el puntaje es muy alto, pero no hay ensayos ni literatura, y el término de enfermedad está obsoleto. La indicación con mejor fundamento mecanístico es el raquitismo dependiente de vitamina D tipo 1B, que se encuentra en etapa S1 como pregunta de investigación.

**Para avanzar se necesita:**
- Mapear el término obsoleto a un concepto vigente de deficiencia de vitamina D y repetir la búsqueda de ensayos y literatura.
- Obtener del prospecto de la AEMPS las indicaciones aprobadas, advertencias y contraindicaciones.
- Completar el mecanismo de acción desde DrugBank.
- Buscar evidencia específica de calcifediol por subtipo en el raquitismo dependiente de vitamina D, sobre todo el tipo 1B.
- Revisar la publicación que el paquete de evidencia cuenta pero no lista en el raquitismo hipofosfatémico (11 informadas, 10 incluidas).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


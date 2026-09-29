---
layout: default
title: Heparin
parent: Solo predicción del modelo (L5)
nav_order: 265
evidence_level: L5
indication_count: 2
---

# Heparin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Heparina: De Anticoagulación a Trombofilia por Deficiencia de Proteína C (Autosómica Recesiva)

## Resumen en Una Frase

La heparina es un anticoagulante de uso clínico general y está comercializada en España en formas inyectables y tópicas.
El modelo TxGNN predice que podría ser efectiva para la **trombofilia por deficiencia de proteína C, autosómica recesiva**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción del modelo sin evidencia adicional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Anticoagulante (según DrugBank; los textos de indicación de las autorizaciones de AEMPS están vacíos) |
| Nueva Indicación Predicha | Trombofilia por deficiencia de proteína C, autosómica recesiva |
| Puntaje de Predicción TxGNN | 99.29% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información conocida, la heparina actúa a través de la antitrombina (SERPINC1): potencia la inhibición de la trombina y del factor Xa. Los datos farmacológicos de DrugBank confirman a SERPINC1 como diana.

La deficiencia de proteína C es un trastorno de la coagulación que predispone a la trombosis, porque la proteína C es un anticoagulante natural. Por eso resulta plausible mecanísticamente que un anticoagulante como la heparina se proponga para esta condición. Pero esta es solo una lógica general de "anticoagulante para trombofilia".

Ningún ensayo ni publicación respalda este vínculo en la información suministrada. El puntaje alto del modelo (0.993) no equivale a evidencia clínica. Cualquier relación con la práctica clínica actual requiere verificación independiente en fuentes externas.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 58691 | Heparina Sódica Rovi 1000 UI/ml solución inyectable | Solución inyectable |
| 56465 | Heparina Sódica Sala 1.000 UI/ml | Solución inyectable |
| 58678 | Menaven 1000 UI/g gel | Gel (tópico) |
| 58679 | Menaven 1000 UI/g crema | Pomada |
| 58693 | Heparina Sódica Rovi 5000 UI/ml solución inyectable | Solución inyectable |

Hay 6 autorizaciones en total, y el paquete de datos detalla 5. Los textos de indicación aprobada no están disponibles. Las formas inyectables (vía sistémica) son las relevantes para una eventual indicación de trombofilia; las formas tópicas (gel y crema) no lo son.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó con 2 registros, ambos de tipo farmacológico (dianas) y no interacciones con otros medicamentos: SERPINC1 (antitrombina) y la glicoproteína Spike del SARS-CoV-2 (afinidad de unión descrita en DrugBank). No se identificaron interacciones medicamentosas clínicas.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero sin ensayos, sin literatura y sin datos de mecanismo (nivel L5), no hay base para avanzar. La heparina está ampliamente comercializada, pero no hay evidencia suministrada para esta indicación.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), un bloqueo para el cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Buscar de forma dirigida literatura y guías clínicas sobre el uso de heparina en la deficiencia de proteína C (incluida la forma grave)
- Confirmar la compatibilidad de la vía de administración y la similitud con la indicación original

**Nota sobre la segunda predicción (trastorno primario de liberación plaquetaria, puntaje 99.06%):** los ensayos y publicaciones asociados parecen obtenidos por palabras clave amplias de coagulación (profilaxis, HIT, COVID-19) y ninguno estudia la heparina como tratamiento para esa condición. Además, la dirección del efecto es dudosa o posiblemente perjudicial, ya que la heparina aumenta el riesgo hemorrágico y puede causar trombocitopenia (HIT). También se recomienda Hold, con evidencia L4.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Landiolol
parent: Solo predicción del modelo (L5)
nav_order: 302
evidence_level: L5
indication_count: 6
---

# Landiolol
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

# Landiolol: De Indicación Original No Registrada a Discinesia Linguo-Facial-Bucal

## Resumen en Una Frase

Landiolol es un betabloqueante intravenoso de acción ultracorta y alta selectividad beta-1. En los datos disponibles no consta el texto de su indicación aprobada en España.
El modelo TxGNN predice que podría ser efectivo para **discinesia linguo-facial-bucal**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (el texto de indicación de la autorización está vacío) |
| Nueva Indicación Predicha | Discinesia linguo-facial-bucal |
| Puntaje de Predicción TxGNN | 99,11% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados en el Evidence Pack. Según la información conocida, landiolol es un bloqueante beta-1 adrenérgico intravenoso, de acción ultracorta y cardioselectivo, pensado para uso agudo en entornos hospitalarios.

La relación con la nueva indicación es débil. Los betabloqueantes orales o no selectivos se han usado en algunos trastornos del movimiento inducidos por fármacos, pero nada vincula específicamente a landiolol con la discinesia orofacial. Además, su perfil de uso solo intravenoso y agudo encaja mal con una enfermedad crónica.

El puntaje alto (99,11%) probablemente refleja similitud a nivel de grafo con otros betabloqueantes, y no biología específica de landiolol. Otras predicciones del modelo siguen el mismo patrón, todas con nivel L5 y sin evidencia recuperada:

| Enfermedad predicha | Puntaje TxGNN | Comentario |
|------|------|------|
| Trastorno de tics crónico | 99,08% | Circuitos dopaminérgicos y cortico-estriatales, sin mecanismo beta-1 establecido |
| Trastornos de movimiento psicógenos | 99,05% | Vínculo teórico especulativo, vía modulación adrenérgica periférica |
| Ataques de escalofrío benignos | 99,04% | Cuadro benigno y autolimitado en lactantes, relación riesgo-beneficio muy desfavorable |
| Enfermedad extrapiramidal y de movimiento | 99,04% | Categoría amplia, la señal debería resolverse en subdiagnósticos concretos |
| Temblor ortostático primario | 99,00% | Beneficio limitado de los betabloqueantes, y landiolol es beta-1 selectivo y solo intravenoso |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 89271 | RAPIBLOC 300 MG POLVO PARA SOLUCION PARA PERFUSION | Polvo para solución para perfusión | No especificada en los datos disponibles |

Titular: Orpha-Devel Handels Und Vertriebs Gmbh.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas para este fármaco.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni literatura, y no hay un mecanismo plausible que conecte un betabloqueante intravenoso cardioselectivo de acción ultracorta con trastornos del movimiento crónicos. Faltan además los datos de seguridad y de la indicación original.

**Para avanzar se necesita:**
- Obtener del prospecto de AEMPS las advertencias, contraindicaciones y el texto de la indicación aprobada
- Completar los datos de mecanismo de acción desde DrugBank
- Realizar una búsqueda dirigida de literatura y ensayos sobre betabloqueantes en discinesias y temblores
- Evaluar la compatibilidad de la vía de administración (solo intravenosa) con el uso crónico
- Considerar la priorización de otras predicciones solo si aparece evidencia independiente

*Este informe es solo para fines de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


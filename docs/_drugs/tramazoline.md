---
layout: default
title: Tramazoline
parent: Solo predicción del modelo (L5)
nav_order: 537
evidence_level: L5
indication_count: 8
---

# Tramazoline
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Tramazolina: De Uso Nasal Tópico (Indicación Original No Registrada) a Urticaria Alérgica

## Resumen en Una Frase

Tramazolina es un agonista alfa-adrenérgico de tipo imidazolina que se comercializa en España como solución para pulverización nasal.
El modelo TxGNN predice que podría ser efectivo para **urticaria alérgica**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción basada solo en el grafo de conocimiento.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de la AEMPS (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Tramazolina es un agonista alfa-adrenérgico de tipo imidazolina que produce vasoconstricción local. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Las dos presentaciones autorizadas en España son pulverizadores nasales, coherentes con un uso como descongestionante de la mucosa nasal.

La urticaria alérgica depende sobre todo de la activación de los mastocitos y de las vías mediadas por histamina. Un vasoconstrictor nasal tópico no tiene un vínculo mecanístico claro con ese proceso. El puntaje alto de TxGNN refleja una asociación en el grafo, sin apoyo clínico ni bibliográfico.

Por ello, esta predicción debe leerse con cautela. No hay razones mecanísticas sólidas ni evidencia real que la sustenten, y la similitud con la indicación original aún no se ha evaluado.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Otras Indicaciones Predichas (Referencia)

| Rank | Indicación | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|------|
| 2 | Laringofaringitis aguda | 99.92% | L5 | Vasoconstricción mucosa débilmente plausible; el fármaco es de vía nasal y no hay evidencia en la zona laringofaríngea |
| 3 | Enfermedad de la cavidad nasal | 99.91% | L5 | Vínculo plausible con la farmacología descongestionante, pero el término es muy amplio y no hay datos de ninguna condición específica |
| 4 | Conjuntivitis rosácea | 99.68% | L5 | Otros vasoconstrictores imidazolínicos se usan en el enrojecimiento ocular, pero no hay datos oculares de tramazolina |
| 5 | Rinitis | 99.53% | L4 | Es la única con ensayos asociados; probablemente esté cerca del uso descongestionante ya conocido y no sea un reposicionamiento real |
| 6 | Urticaria por frío | 99.45% | L5 | Mediada por mastocitos; sin relevancia mecanística establecida |
| 7 | Trastorno de cefalea | 99.26% | L5 | Un posible beneficio sería indirecto (cefalea por congestión sinusal) |
| 8 | Cefalalgia trigémino-autonómica | 99.17% | L5 | Podría aliviar la congestión nasal asociada, pero no trata el mecanismo del dolor |

De los tres ensayos asociados a rinitis, solo NCT01971086 (estudio observacional de Rhinospray Plus en rinitis aguda, Hungría, n=300, completado) es potencialmente pertinente. La composición del producto no está confirmada en los datos y debe verificarse. Los otros dos (antibióticos tópicos en rinosinusitis crónica, retirado; omalizumab en polinosis por cedro japonés) no guardan relación con tramazolina.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 56731 | RHINOSPRAY EUCALIPTUS 1,18 mg/ml | Solución para pulverización nasal | Opella Healthcare Spain S.L. |
| 39574 | RHINOSPRAY 1,18 mg/ml | Solución para pulverización nasal | Opella Healthcare Spain S.L. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de urticaria alérgica es solo del modelo (L5), sin ensayos ni literatura, y no tiene un vínculo mecanístico plausible con un vasoconstrictor nasal. No hay datos de seguridad disponibles para avanzar.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), lo que actualmente bloquea el cribado de seguridad
- Obtener datos del mecanismo de acción desde DrugBank
- Confirmar la indicación original según el etiquetado
- Si se busca una indicación más viable, evaluar la rinitis (L4) como línea separada, verificando primero la composición de Rhinospray Plus en NCT01971086 y considerando el riesgo de congestión de rebote (rinitis medicamentosa) con el uso prolongado
- Definir la ruta de administración necesaria para cualquier nueva indicación, ya que la compatibilidad de vía está pendiente

*Este informe es solo para referencia de investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


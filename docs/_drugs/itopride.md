---
layout: default
title: Itopride
parent: Solo predicción del modelo (L5)
nav_order: 294
evidence_level: L5
indication_count: 4
---

# Itopride
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

# Itopride: De Indicación Original No Registrada a Enfermedad de Crohn del Intestino Delgado

## Resumen en Una Frase

Itopride es un fármaco comercializado en España (1 autorización) cuya indicación original no consta en los datos recibidos.
El modelo TxGNN predice que podría ser efectivo para **enfermedad de Crohn del intestino delgado**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Enfermedad de Crohn del intestino delgado |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 (solo predicción del modelo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información general, itopride es un procinético gastrointestinal, descrito como antagonista de dopamina D2 e inhibidor de la acetilcolinesterasa. Este dato proviene de conocimiento farmacológico general, no del Evidence Pack.

Con esa base, **no se identifica un vínculo mecanístico sólido** con la enfermedad de Crohn. La enfermedad de Crohn es una inflamación de origen inmunitario, y un procinético no actúa sobre ese proceso. Además, aumentar la motilidad podría ser indeseable si existen estenosis intestinales.

El puntaje TxGNN (0.999) es solo una predicción del modelo. Ningún ensayo clínico ni publicación lo corrobora, por lo que debe tratarse como una hipótesis sin verificar.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 86657 | PROGIT 50 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | Comprimido recubierto con película | No consta en los datos disponibles |

Titular: Kappler Pharma Consult GmbH.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Otras Predicciones del Modelo

Todas tienen evidencia L5 y ningún ensayo ni publicación asociados.

| Indicación Predicha | Puntaje TxGNN | Valoración |
|------|------|------|
| Insuficiencia venosa | 99.23% | Sin vínculo farmacológico plausible; probable artefacto del grafo de conocimiento |
| Aclorhidria | 99.16% | Vínculo débil e indirecto; un procinético no restaura la secreción ácida |
| Hernia de hiato | 99.02% | Plausibilidad indirecta a nivel de síntomas (vaciamiento gástrico y reflujo); no corrige el defecto anatómico. Clasificada como "Research Question" |

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para la enfermedad de Crohn del intestino delgado se basa solo en el modelo (L5). No hay ensayos, literatura ni vínculo mecanístico plausible, y el procinético no aborda la inflamación inmunomediada.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción desde DrugBank.
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un bloqueo para el cribado de seguridad.
- Confirmar la indicación original aprobada del producto.
- Hacer una búsqueda sistemática de ensayos y literatura sobre itopride en enfermedad de Crohn.
- Si se prioriza alguna predicción, la hernia de hiato es la única marcada como pregunta de investigación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


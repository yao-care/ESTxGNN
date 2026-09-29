---
layout: default
title: Iohexol
parent: Solo predicción del modelo (L5)
nav_order: 289
evidence_level: L5
indication_count: 2
---

# Iohexol
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

# Iohexol: De Medio de Contraste Diagnóstico a Insomnio

## Resumen en Una Frase

Iohexol es un medio de contraste yodado no iónico, hidrosoluble, que se utiliza como agente de diagnóstico por imagen. El modelo TxGNN predice que podría ser efectivo para el **insomnio**, con una puntuación muy alta (99,87 %). Sin embargo, actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Medio de contraste yodado para diagnóstico por imagen (los registros de AEMPS no incluyen el texto de indicación) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99,87 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, iohexol es un contraste yodado no iónico que no se metaboliza y se excreta sin cambios por vía renal. Su función es diagnóstica (opacificación en imagen), no farmacológica.

**No se identifica un vínculo mecanístico plausible** con el insomnio. Iohexol no tiene actividad conocida sobre las dianas relacionadas con el sueño (receptores GABA-A, orexina, histamina o melatonina). La puntuación alta de TxGNN proviene de asociaciones en el grafo de conocimiento, sin farmacología que la sustente.

Tampoco existe relación terapéutica entre la indicación original (diagnóstico por imagen) y el insomnio. Por eso esta predicción debe considerarse una señal del modelo sin respaldo mecanístico ni clínico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 62019 | OMNIPAQUE 350 mg Iodo/ml solución inyectable | Solución inyectable | GE Healthcare Bio-Sciences, S.A.U. |
| 62017 | OMNIPAQUE 240 mg Iodo/ml solución inyectable | Solución inyectable | GE Healthcare Bio-Sciences, S.A.U. |
| 62018 | OMNIPAQUE 300 mg Iodo/ml solución inyectable | Solución inyectable | GE Healthcare Bio-Sciences, S.A.U. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni literatura para insomnio, y no existe un mecanismo plausible. La puntuación de TxGNN por sí sola no basta para avanzar.

Como nota adicional, la segunda predicción (ansiedad, 99,25 %) tampoco tiene respaldo. Los seis ensayos y las publicaciones recuperados son coincidencias incidentales: iohexol se usa allí para medir la tasa de filtración glomerular (TFG) o como contraste en procedimientos, y nunca se evalúa como tratamiento. Todos se clasificaron con relevancia C y nivel L5.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), que es un vacío bloqueante para el cribado de seguridad
- Completar los datos de mecanismo de acción desde DrugBank
- Confirmar el texto de indicación aprobada de las tres autorizaciones
- Encontrar alguna evidencia preclínica o clínica que vincule iohexol con el sueño; de lo contrario, descartar esta candidatura
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


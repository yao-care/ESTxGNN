---
layout: default
title: Pioglitazone
parent: Solo predicción del modelo (L5)
nav_order: 427
evidence_level: L5
indication_count: 9
---

# Pioglitazone
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

# Pioglitazona: De Diabetes Mellitus Tipo 2 a Opsismodisplasia

## Resumen en Una Frase

Pioglitazona es un antidiabético oral de la familia de las tiazolidindionas, utilizado originalmente para el tratamiento de la diabetes mellitus tipo 2.
El modelo TxGNN predice que podría ser efectivo para **opsismodisplasia**, una displasia esquelética rara,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Diabetes mellitus tipo 2 (según datos farmacológicos; los textos de indicación de las autorizaciones de AEMPS no están disponibles) |
| Nueva Indicación Predicha | Opsismodisplasia |
| Puntaje de Predicción TxGNN | 99.59% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, pioglitazona es un agonista del receptor activado por proliferadores de peroxisomas gamma (PPAR-γ) y actúa como sensibilizador a la insulina. Su eficacia en la diabetes tipo 2 está comprobada. El único vínculo mecanístico disponible es su acción sobre PPAR-γ (y, según la base farmacológica, TRPM3), que no se ha relacionado con esta nueva indicación.

La opsismodisplasia es una displasia esquelética rara, típicamente asociada a mutaciones en INPPL1. Con los datos suministrados no se pudo identificar un vínculo plausible entre el agonismo de PPAR-γ y la fisiopatología de esta enfermedad. No hay similitud evidente con la indicación original.

Por ello, la puntuación alta (0.996) probablemente sea un artefacto del grafo de conocimiento y no una señal terapéutica real. Debe interpretarse como una hipótesis sin sustento, no como una candidata con racionalidad demostrada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 00150005 | ACTOS 30 mg COMPRIMIDOS | Comprimido | Cheplapharm Arzneimittel GmbH |
| 76481 | PIOGLITAZONA CINFA 15 MG COMPRIMIDOS EFG | Comprimido | Laboratorios Cinfa S.A. |
| 00150010IP | ACTOS 30 MG COMPRIMIDOS | Comprimido | Takeda Pharma A/S |
| 00151001 | GLUSTIN 15 mg COMPRIMIDOS | Comprimido | Takeda Pharma A/S |
| 76275 | PIOGLITAZONA AUROBINDO 15 MG COMPRIMIDOS EFG | Comprimido | Laboratorios Aurobindo S.L.U. |

Se muestran 5 de las 20 autorizaciones. El texto de indicación aprobada no está disponible en los datos recibidos.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no cuenta con ensayos, literatura ni un mecanismo plausible que vincule el agonismo de PPAR-γ con la opsismodisplasia (nivel L5, etapa S0). No hay base para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank y un análisis que justifique (o descarte) el vínculo con la vía de INPPL1.
- Descarga y análisis del prospecto de AEMPS (advertencias y contraindicaciones), necesarios antes de cualquier cribado de seguridad.
- Búsqueda dirigida de literatura preclínica sobre pioglitazona u otros agonistas PPAR-γ en displasias esqueléticas.
- Como aparte, las indicaciones predichas en lipodistrofias localizadas (rangos 5, 6, 7 y 8) tienen un racional biológico más plausible (adipogénesis mediada por PPAR-γ) y se han clasificado como preguntas de investigación. Podrían priorizarse antes que esta.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


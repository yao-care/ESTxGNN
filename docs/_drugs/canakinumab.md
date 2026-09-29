---
layout: default
title: Canakinumab
parent: Solo predicción del modelo (L5)
nav_order: 97
evidence_level: L5
indication_count: 10
---

# Canakinumab
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

# Canakinumab: Predicción de Reposicionamiento a Infarto Hepático

## Resumen en Una Frase

Canakinumab (comercializado como Ilaris) es un anticuerpo monoclonal humano que neutraliza la interleucina-1β (IL-1β). Los datos de autorización disponibles no indican su indicación original.
El modelo TxGNN predice que podría ser efectivo para **infarto hepático**, pero no hay **ningún ensayo clínico** y solo **1 publicación**, sin relación con esta enfermedad. Se trata de una predicción del modelo sin respaldo real.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Infarto hepático |
| Puntaje de Predicción TxGNN | 99,86 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Canakinumab actúa neutralizando la señalización de IL-1β, lo que suprime la inflamación en enfermedades autoinflamatorias. Este mecanismo proviene de la literatura recuperada, no de un campo de mecanismo de acción del fármaco.

En este caso, la predicción no tiene una base mecanística sólida. Los datos no documentan ningún mecanismo plausible mediado por IL-1β que explique un papel del fármaco en el infarto hepático. El puntaje alto del modelo (99,86 %) es solo una predicción. Además, no hay datos sobre la similitud con la indicación original.

Ninguno de los demás candidatos hepáticos de la lista (enfermedad venooclusiva hepática, peliosis hepática, angiosarcoma hepático) tiene evidencia que los respalde.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37354546](https://pubmed.ncbi.nlm.nih.gov/37354546/) | 2023 | ECA | JAMA | Ácido bempedoico para prevención primaria de eventos cardiovasculares en pacientes intolerantes a estatinas. No evalúa canakinumab ni infarto hepático, por lo que probablemente es una coincidencia de palabras clave. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 109564004 | ILARIS 150 MG/ML SOLUCION INYECTABLE | Solución inyectable | No especificada en los datos disponibles |
| 09564001 | ILARIS 150 mg POLVO PARA SOLUCION INYECTABLE | Polvo para solución inyectable | No especificada en los datos disponibles |

Titular de ambas autorizaciones: Novartis Europharm Limited.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para infarto hepático no tiene ensayos clínicos, la única publicación no guarda relación con el fármaco y no existe un vínculo mecanístico documentado con la inhibición de IL-1β. El nivel de evidencia es L5.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas), ya que sin él no se puede pasar al cribado de seguridad.
- Confirmar el mecanismo de acción en DrugBank.
- Una hipótesis biológica que vincule la IL-1β con el infarto hepático y estudios preclínicos que la respalden.

**Nota sobre otros candidatos del mismo análisis:** el candidato mejor respaldado es la **fiebre mediterránea familiar** (rank 6, L1, *Proceed with Guardrails*), con un ECA de fase 3 (PMID 29768139), revisiones sistemáticas y estudios de cohorte. Conviene evaluarlo por separado, verificando que el subtipo autosómico dominante coincida con la población estudiada. El **síndrome de Blau** (L3) y el síndrome autoinflamatorio con fiebre periódica y enterocolitis infantil (L4) quedan como preguntas de investigación (*Research Question*).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


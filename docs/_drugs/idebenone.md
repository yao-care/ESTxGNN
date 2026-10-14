---
layout: default
title: Idebenone
parent: Solo predicción del modelo (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
---

# Idebenone
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

# Idebenona: De Neuropatía Óptica Hereditaria de Leber a Porfiria Hepática

## Resumen en Una Frase

Idebenona es un análogo sintético de la benzoquinona de cadena corta, relacionado con la coenzima Q10, utilizado originalmente para el tratamiento de la neuropatía óptica hereditaria de Leber.
El modelo TxGNN predice que podría ser efectivo para **porfiria hepática**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata de una predicción exclusivamente del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Neuropatía óptica hereditaria de Leber (según el grafo de conocimiento; el texto de indicación autorizado en España no está disponible) |
| Nueva Indicación Predicha | Porfiria hepática |
| Puntaje de Predicción TxGNN | 99,92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, idebenona es un análogo sintético de la coenzima Q10 que actúa como transportador de electrones en la cadena respiratoria mitocondrial y como antioxidante. Su uso en la neuropatía óptica hereditaria de Leber, una enfermedad mitocondrial, se relaciona con esta función.

Un vínculo meramente especulativo con la porfiria hepática sería el estrés oxidativo y la disfunción mitocondrial en el daño hepático asociado a las porfirinas. Sin embargo, **los datos compilados para este informe no respaldan este vínculo**. La puntuación alta (99,92%) refleja la cercanía en la red del grafo de conocimiento y no una biología demostrada. La similitud con la indicación original está pendiente de evaluar.

## Otras Predicciones del Modelo (Referencia)

Todas se basan solo en el modelo, sin ensayos ni literatura, con nivel L5 y recomendación Hold:

| Rango | Enfermedad Predicha | Puntaje TxGNN |
|------|------|------|
| 2 | Trombosis portal primitiva | 99,92% |
| 3 | Hipertensión portal no cirrótica familiar de inicio temprano | 99,92% |
| 4 | Cirrosis idiopática asociada al cobre | 99,92% |
| 5 | Esclerosis hepatoportal | 99,92% |
| 6 | Síndrome hepatopulmonar | 99,92% |
| 7 | Miopatía necrosante inmunomediada | 99,76% |
| 8 | Síndrome de osteogénesis imperfecta, retinopatía, convulsiones y discapacidad intelectual | 99,75% |
| 9 | Síndrome antisintetasa | 99,75% |
| 10 | Miositis focal | 99,74% |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1151020001 | RAXONE 150 MG comprimidos recubiertos con película (Chiesi Farmaceutici S.P.A.) | Comprimido recubierto con película | No disponible en los datos compilados |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas ni contraindicaciones derivadas del grafo de conocimiento.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para porfiria hepática se sustenta únicamente en la puntuación del modelo (L5), sin ensayos clínicos, literatura ni vínculo mecanístico demostrado. Además, faltan los datos de seguridad del prospecto, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), un vacío bloqueante
- Obtener los datos del mecanismo de acción desde DrugBank
- Realizar una revisión sistemática de la literatura y buscar estudios preclínicos que relacionen idebenona con la porfiria hepática
- Evaluar la compatibilidad de la vía de administración y la similitud con la indicación original
- Considerar si alguna de las otras predicciones tiene una justificación biológica más plausible antes de priorizar recursos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


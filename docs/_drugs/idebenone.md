---
layout: default
title: Idebenone
parent: Solo predicción del modelo (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "idebenone"
predicted_indications: ["hepatic porphyria", "primitive portal vein thrombosis", "early-onset familial noncirrhotic portal hypertension", "idiopathic copper-associated cirrhosis", "hepatoportal sclerosis", "hepatopulmonary syndrome", "immune-mediated necrotizing myopathy", "osteogenesis imperfecta-retinopathy-seizures-intellectual disability syndrome", "antisynthetase syndrome", "focal myositis"]
description: "Idebenone: nueva indicación predicha, Porfiria hepática (hepatic porphyria) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Idebenone: Porfiria hepática (hepatic porphyria)
{: .text-alpha }

## Resumen en Una Frase

Idebenona es un análogo sintético de la benzoquinona de cadena corta, relacionado con la coenzima Q10, utilizado originalmente para el tratamiento de la neuropatía óptica hereditaria de Leber.
El modelo TxGNN predice que podría ser efectivo para **porfiria hepática**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata de una predicción exclusivamente del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Porfiria hepática (hepatic porphyria) |
| Puntaje de Predicción TxGNN | 0.9992 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Autorizado pero no comercializado (registros: 1) |
| Número de Autorizaciones | 1 (vigentes: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, idebenona es un análogo sintético de la coenzima Q10 que actúa como transportador de electrones en la cadena respiratoria mitocondrial y como antioxidante. Su uso en la neuropatía óptica hereditaria de Leber, una enfermedad mitocondrial, se relaciona con esta función.

Un vínculo meramente especulativo con la porfiria hepática sería el estrés oxidativo y la disfunción mitocondrial en el daño hepático asociado a las porfirinas. Sin embargo, **los datos compilados para este informe no respaldan este vínculo**. La puntuación alta (0,9992) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no una biología demostrada. La similitud con la indicación original está pendiente de evaluar.

## Otras Predicciones del Modelo (Referencia)

Todas se basan solo en el modelo, sin ensayos ni literatura, con nivel L5 y recomendación Hold:

| Rango | Enfermedad Predicha | Puntaje TxGNN |
|------|------|------|
| 2 | Trombosis portal primitiva | 0,9992 |
| 3 | Hipertensión portal no cirrótica familiar de inicio temprano | 0,9992 |
| 4 | Cirrosis idiopática asociada al cobre | 0,9992 |
| 5 | Esclerosis hepatoportal | 0,9992 |
| 6 | Síndrome hepatopulmonar | 0,9992 |
| 7 | Miopatía necrosante inmunomediada | 0,9976 |
| 8 | Síndrome de osteogénesis imperfecta, retinopatía, convulsiones y discapacidad intelectual | 0,9975 |
| 9 | Síndrome antisintetasa | 0,9975 |
| 10 | Miositis focal | 0,9974 |

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


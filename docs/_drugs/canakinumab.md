---
layout: default
title: Canakinumab
parent: Solo predicción del modelo (L5)
nav_order: 136
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Canakinumab: nueva indicación predicha, Infarto hepático (nivel de evidencia L5). Indicación original: Gota, síndromes periódicos asociados a criopirina…"
monitor_inn: "CANAKINUMAB"
predicted_indications: ["hepatic infarction", "hepatic veno-occlusive disease", "peliosis hepatis", "syndrome with combined immunodeficiency", "periodic fever-infantile enterocolitis-autoinflammatory syndrome", "familial Mediterranean fever, autosomal dominant", "extracutaneous mastocytoma", "Blau syndrome", "monosomy X", "liver angiosarcoma"]
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

# Canakinumab: De Gota y Síndromes Periódicos Autoinflamatorios a Infarto Hepático

## Resumen en Una Frase

Canakinumab es un anticuerpo monoclonal dirigido contra la interleucina-1β (IL-1β). Se ha usado en enfermedades autoinflamatorias como los síndromes periódicos asociados a criopirina (CAPS), la artritis idiopática juvenil sistémica, la fiebre mediterránea familiar y la gota.
El modelo TxGNN predice que podría ser efectivo para **infarto hepático**, con un puntaje muy alto (99,86 %).
Sin embargo, **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Gota, síndromes periódicos asociados a criopirina, artritis idiopática juvenil sistémica y otras fiebres periódicas hereditarias (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Infarto hepático |
| Puntaje de Predicción TxGNN | 99,86 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en las fuentes consultadas. Según la información conocida, canakinumab neutraliza la IL-1β, una citocina central en la inflamación. Su eficacia está comprobada en enfermedades autoinflamatorias mediadas por IL-1β, y mecanísticamente podría ser aplicable a procesos en los que esta vía contribuya al daño tisular.

La relación con el infarto hepático es especulativa. Una hipótesis plausible es que la inflamación dependiente de IL-1β participe en la lesión de tejidos isquémicos. Aun así, no hay evidencia directa que respalde el uso de canakinumab en esta enfermedad, y la indicación original (enfermedades autoinflamatorias hereditarias o metabólicas) difiere mucho de una lesión vascular y isquémica del hígado.

El puntaje del modelo es alto, pero refleja patrones del grafo de conocimiento y no confirmación clínica. La similitud con las indicaciones originales aún no se ha evaluado, y tampoco la compatibilidad de la vía de administración.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 109564004 | ILARIS 150 mg/ml solución inyectable | Solución inyectable | No especificada en los datos disponibles |
| 09564001 | ILARIS 150 mg polvo para solución inyectable | Polvo para solución inyectable | No especificada en los datos disponibles |

Ambas autorizaciones son de Novartis Europharm Limited, están vigentes y corresponden a monofármaco.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se han registrado 100 interacciones. Las principales, de nivel **moderado**, son:
  - Corticosteroides: hidrocortisona, triamcinolona (incluida la oftálmica), dexametasona, betametasona, budesonida, prednisolona y prednisona.
  - Simvastatina.
  - Anticoagulantes: warfarina, dicumarol, apixabán y rivaroxabán.
  - Radiofármacos y anticuerpos radiomarcados: ibritumomab tiuxetán, iobenguano (I-131), tositumomab y tositumomab (I-131).
  - De nivel **menor**: sales de zinc (acetato, gluconato y sulfato).

Para advertencias y contraindicaciones, consultar el prospecto. Dado que canakinumab bloquea la IL-1β, el riesgo de infecciones y de neutropenia debe revisarse en la ficha técnica.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para infarto hepático se basa solo en el modelo (nivel L5), sin ensayos ni literatura. El vínculo mecanístico es hipotético, así que no hay base para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y de la fisiopatología de la IL-1β en el infarto hepático.
- Estudios preclínicos o series de casos que apoyen la hipótesis.
- Revisión de advertencias y contraindicaciones del prospecto de la AEMPS.
- Evaluación de la similitud con las indicaciones originales y de la compatibilidad de la vía de administración.

**Nota sobre otras predicciones:** entre las 10 principales predicciones de TxGNN, la de **fiebre mediterránea familiar autosómica dominante** (puntaje 99,41 %) es la mejor respaldada. Cuenta con 3 ensayos de Fase 3 abiertos y completados en síndromes periódicos asociados a criopirina, además de revisiones, metaanálisis y estudios de cohorte en fiebre mediterránea familiar resistente a colchicina. Su evaluación sería «Proceed with Guardrails», con nivel L1 según los criterios del sistema. Los ensayos no son específicos de esa enfermedad y su aplicabilidad requiere confirmación. La predicción de **síndrome de Blau** tiene evidencia limitada a casos y series pequeñas (nivel L3).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


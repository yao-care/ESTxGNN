---
layout: default
title: Levocetirizine
parent: Solo predicción del modelo (L5)
nav_order: 465
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-31
monitor_inn: "Levocetirizine"
predicted_indications: ["rheumatoid arthritis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
description: "Levocetirizine: nueva indicación predicha, Artritis Reumatoide (rheumatoid arthritis) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Levocetirizine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Levocetirizine: Artritis Reumatoide (rheumatoid arthritis)
{: .text-alpha }

## Resumen en Una Frase

Levocetirizina es un antihistamínico, originalmente utilizado para el tratamiento de la rinitis alérgica, la rinitis vasomotora y la urticaria idiopática.
El modelo TxGNN predice que podría ser efectivo para **Artritis Reumatoide**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Artritis Reumatoide (rheumatoid arthritis) |
| Puntaje de Predicción TxGNN | 0.9973 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 12) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción del fármaco en los datos compilados para este informe. Según la farmacología general, la levocetirizina es un antagonista selectivo del receptor H1 de histamina, y su eficacia en rinitis alérgica y urticaria está bien establecida.

La relación con la artritis reumatoide es hipotética. La histamina y la actividad de los mastocitos se han relacionado con la inflamación sinovial, y el bloqueo H1 podría, en teoría, modular la permeabilidad vascular y la liberación de citocinas en la articulación. Sin embargo, la artritis reumatoide es una enfermedad autoinmune crónica cuyo mecanismo central difiere del de las enfermedades alérgicas tratadas originalmente.

El puntaje de TxGNN (0,9973) es solo una predicción del modelo, y no hay estudios que la respalden ni la refuten. Esta hipótesis debe considerarse exploratoria.

### Otras predicciones del modelo

Las otras dos predicciones con mayor puntaje son enfermedades congénitas raras: el síndrome de microftalmia colobomatosa con displasia rizomélica (0,9959) y el síndrome de braquidactilia-sindactilia (0,9952). No se identificó ningún vínculo mecanístico plausible entre el bloqueo H1 y estos trastornos del desarrollo; los puntajes provienen del modelo TxGNN (aprendizaje profundo) y pueden reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Ambas se mantienen en nivel L5 y en decisión Hold.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de principio activo único). Los textos de indicación aprobada no están disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 64286 | MUNTEL 5 mg comprimidos con cubierta pelicular | Comprimido recubierto con película |
| 64287 | XAZAL 5 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 67426 | XAZAL 5 mg/ml gotas orales en solución | Gotas orales en solución |
| 68153 | XAZAL 0,5 mg/ml solución oral | Solución oral |
| 83351 | Levocetirizina Substipharm 5 mg comprimidos bucodispersables EFG | Comprimido bucodispersable |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proviene del texto del prospecto): enfermedad renal, piouréter, enfermedad renal crónica, síndrome de insuficiencia renal crónica e insuficiencia renal terminal.
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total; las 20 mostradas son de nivel moderado, salvo hialuronidasa (menor). Entre las principales:
  - Depresores del sistema nervioso central y opioides: morfina (incluida la liposomal), fentanilo, dihidrocodeína, opio, difenoxina, difenoxilato y loperamida.
  - Cannabinoides: dronabinol y nabilona.
  - Otros antihistamínicos y sedantes: prometazina y clorfeniramina.
  - Etanol.
  - Otros: bupropión, metoclopramida, sibutramina, histamina y yoduro I-123/I-131.

La información de advertencias y contraindicaciones del prospecto no está disponible; consultar el prospecto de la AEMPS.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para artritis reumatoide se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura, y el vínculo mecanístico es hipotético. Además, falta la información de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), indispensable para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión sistemática de la literatura sobre histamina/receptores H1 en artritis reumatoide.
- Generar evidencia preclínica que respalde la hipótesis antes de plantear ensayos clínicos.
- Considerar especialmente la función renal en cualquier población de estudio, dadas las contraindicaciones señaladas en el grafo de conocimiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


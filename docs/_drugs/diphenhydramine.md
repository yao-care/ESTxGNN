---
layout: default
title: Diphenhydramine
parent: Solo predicción del modelo (L5)
nav_order: 255
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Diphenhydramine: nueva indicación predicha, Conjuntivitis rosácea (nivel de evidencia L5). Indicación original: Insomnio, rinitis vasomotora…"
monitor_inn: "diphenhydramine"
predicted_indications: ["rosacea conjunctivitis"]
---

# Diphenhydramine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Difenhidramina: De Insomnio y Rinitis Alérgica a Conjuntivitis Rosácea
{: .text-alpha }

## Resumen en Una Frase

La difenhidramina es un antihistamínico H1 de primera generación, utilizado originalmente para el insomnio, la rinitis (vasomotora y alérgica) y distintas formas de conjuntivitis (atópica, papilar y vernal).
El modelo TxGNN predice que podría ser efectivo para la **conjuntivitis rosácea**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Insomnio, rinitis vasomotora, rinitis alérgica y conjuntivitis atópica, papilar y vernal (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Conjuntivitis rosácea |
| Puntaje de Predicción TxGNN | 99.20% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la difenhidramina es un antagonista del receptor H1 de primera generación con efectos anticolinérgicos y sedantes, y su utilidad en conjuntivitis de origen alérgico está establecida. Por ello, un componente de inflamación ocular mediado por histamina podría, en teoría, ser aplicable a la conjuntivitis rosácea.

El puntaje elevado de TxGNN (99.20%) probablemente refleja la cercanía en la red de conocimiento con las indicaciones conjuntivales ya aprobadas, más que una base mecanística sólida. La rosácea ocular se asocia principalmente con disfunción de las glándulas de Meibomio, inestabilidad de la película lagrimal, colonización por Demodex y desregulación inmunitaria innata y neurovascular, con poca evidencia de un papel dominante de la histamina.

Además, los efectos anticolinérgicos de la difenhidramina podrían empeorar el ojo seco, que es una preocupación relevante en la enfermedad ocular asociada a la rosácea. En conjunto, la predicción no cuenta actualmente con una justificación mecanística clara. La similitud con el mecanismo original y la compatibilidad de vías de administración están pendientes de evaluación.

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
| 83596 | Difenhidramina Omega Pharma 50 mg comprimidos | Comprimido | No disponible en los datos |
| 61459 | Neosayomol 20 mg/g crema | Crema | No disponible en los datos |
| 38322 | Soñodor Difenhidramina 50 mg comprimidos | Comprimido | No disponible en los datos |
| 80485 | Dolomidina 500/25 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |
| 84763 | Antidol Noche 500 mg/25 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |

Existen 8 autorizaciones vigentes en total (todas de composición simple); se muestran las 5 principales.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 394 interacciones registradas. Entre las principales:
  - **Mayor gravedad**: citrato de potasio y eliglustat.
  - **Gravedad moderada**: anticolinérgicos y antiespasmódicos (hiosciamina, atropina, glicopirronio, diciclomina, clidinio, mepenzolato, metescopolamina), opioides (morfina, loperamida, eluxadolina), bupropión, lorcaserina, dronabinol, nabilona y metoclopramida.
- **Consideración adicional**: el efecto anticolinérgico de la difenhidramina podría agravar la sequedad ocular, lo que es relevante en la rosácea ocular.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura que la respalden. Además, la fisiopatología de la rosácea ocular no apunta claramente a la histamina, y el efecto anticolinérgico podría ser perjudicial.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), actualmente un vacío bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, mediante consulta a DrugBank).
- Revisión sistemática de literatura sobre antihistamínicos en rosácea ocular.
- Evaluar la compatibilidad de vías de administración (formulación oftálmica) y la similitud con las indicaciones originales.
- Valorar el riesgo de empeoramiento del ojo seco por efectos anticolinérgicos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


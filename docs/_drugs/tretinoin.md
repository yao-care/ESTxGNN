---
layout: default
title: Tretinoin
parent: Solo predicción del modelo (L5)
nav_order: 544
evidence_level: L5
indication_count: 10
---

# Tretinoin
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

# Tretinoína: De Usos Dermatológicos y Leucemia Promielocítica Aguda a Nodulosis Reumatoide

## Resumen en Una Frase

La tretinoína (ácido retinoico all-trans) se utiliza en trastornos cutáneos como el acné y la queratinización anómala, y como agente diferenciador en la leucemia promielocítica aguda.
El modelo TxGNN predice que podría ser efectiva para **nodulosis reumatoide**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción concreta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Las autorizaciones de la AEMPS no incluyen texto de indicación. Según datos farmacológicos: acné, daño por radiación UV, trastornos de la queratinización y leucemia promielocítica aguda |
| Nueva Indicación Predicha | Nodulosis reumatoide |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la tretinoína es un retinoide que actúa sobre receptores nucleares. Su eficacia en enfermedades de la piel y en la leucemia promielocítica aguda está establecida, y mecanísticamente podría ser aplicable a enfermedades inflamatorias e inmunomediadas. Los datos farmacológicos la vinculan con los receptores del ácido retinoico (RARα, RARβ y RARγ). También muestran interacción con PPARδ, RORβ, TR4 (NR2C2) y TLX (NR2E1).

La relación entre las indicaciones originales y la nodulosis reumatoide es indirecta. La nodulosis reumatoide es una afección inflamatoria asociada a la artritis reumatoide, y el ácido retinoico tiene actividad inmunomoduladora. Sin embargo, no hay ensayos ni literatura que vinculen la tretinoína con esta enfermedad. La predicción se apoya únicamente en el puntaje del modelo.

Conviene interpretar el resultado con cautela. Un puntaje alto indica una asociación en el grafo de conocimiento, no eficacia demostrada. La nodulosis reumatoide es solo la primera de diez candidatas, y la mayoría son artropatías o displasias esqueléticas sin evidencia propia.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 65396 | VESANOID 10 mg cápsulas blandas | Cápsula blanda | Cheplapharm Arzneimittel GmbH |
| 52751 | NEOCARE 4 mg/g crema | Crema | Industrial Farmacéutica Cantabria S.A. |
| 60140 | RETIRIDES 0,25 mg/g crema | Crema | Galenicum Derma S.L.U. |
| 60142 | RETIRIDES 1 mg/g crema | Crema | Galenicum Derma S.L.U. |
| 60141 | RETIRIDES 0,5 mg/g crema | Crema | Galenicum Derma S.L.U. |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Agente diferenciador antineoplásico (no citotóxico convencional), en su uso oncológico |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones farmacológicas:** la consulta se completó, pero los 7 registros son dianas farmacológicas, no interacciones con otros medicamentos. Son RARα, RARβ, RARγ, PPARδ, RORβ, TR4 (NR2C2) y TLX (NR2E1).
- **Población pediátrica:** para las candidatas de artritis idiopática juvenil, el uso sistémico de retinoides en niños implica riesgo de teratogenicidad y toxicidad esquelética. Habría que sopesarlo antes de cualquier desarrollo.
- **Sistema esquelético:** los retinoides pueden afectar negativamente al crecimiento esquelético, lo que es relevante para las candidatas de displasia esquelética.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para nodulosis reumatoide es solo del modelo (nivel L5), sin ensayos clínicos ni literatura que la respalden. Además, las advertencias y contraindicaciones oficiales no están disponibles, así que no se puede completar el cribado de seguridad.

Entre las candidatas, la **artrosis** es la única con literatura relevante (nivel L4): estudios genéticos y preclínicos sobre ALDH1A2 y ácido retinoico (PMID 36542696, 37418291). Sin embargo, la dirección del efecto es contradictoria, porque un estudio de 2025 (PMID 40564983) sugiere que un exceso de ácido retinoico podría dañar el cartílago. Por eso se trata como pregunta de investigación, no como candidata lista para avanzar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones).
- Obtener datos del mecanismo de acción desde DrugBank.
- Realizar una revisión sistemática de la literatura sobre retinoides en nodulosis reumatoide y artritis reumatoide.
- Definir la vía de administración compatible (oral frente a tópica), hoy sin evaluar.
- Si se prioriza la artrosis, aclarar la relación dosis-efecto del ácido retinoico en cartílago antes de proponer estudios clínicos.

*Este informe es solo para fines de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


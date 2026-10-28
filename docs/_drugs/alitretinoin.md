---
layout: default
title: Alitretinoin
parent: Solo predicción del modelo (L5)
nav_order: 38
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Alitretinoin: nueva indicación predicha, Amenorrea (nivel de evidencia L5). Indicación original: No disponible en los datos de autorización (el texto de indicación es…"
monitor_inn: "alitretinoin"
predicted_indications: ["amenorrhea (disease)", "acne (disease)", "atypical coarctation of aorta", "pregnancy associated osteoporosis", "aortic malformation", "postmenopausal osteoporosis", "autosomal dominant neovascular inflammatory vitreoretinopathy", "breast fibrocystic disease", "benign mammary dysplasia", "Worth syndrome"]
---

# Alitretinoin
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

## Alitretinoína: De Indicación Original No Registrada a Amenorrea
{: .text-alpha }

## Resumen en Una Frase

Alitretinoína (ácido 9-cis-retinoico) es un retinoide que se comercializa en España como cápsulas blandas (Toctino y genéricos); según la información farmacológica compilada, se usa en el eczema crónico grave de las manos refractario a corticoides tópicos potentes. El modelo TxGNN predice que podría ser efectivo para **amenorrea**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de autorización (el texto de indicación está vacío). La información farmacológica señala eczema crónico grave de las manos |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 0,9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 4 de 4) |
| Número de Autorizaciones | 4 (vigentes: 4) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Alitretinoína (9-cis-retinoico) es un agonista pan-retinoide que se une a los receptores del ácido retinoico (RARα, RARβ, RARγ) y a los receptores retinoides X (RXRα, RXRβ, RXRγ). Los datos compilados no incluyen una descripción detallada del mecanismo de acción, por lo que este resumen se basa en los datos de dianas farmacológicas.

Los retinoides pueden influir en la diferenciación de tejidos reproductivos, pero los datos no muestran ningún vínculo directo con la amenorrea. La relación con la indicación original (una enfermedad dermatológica inflamatoria) es débil, y la similitud con ella figura como pendiente de análisis.

Además, los retinoides son teratógenos, lo que supone una preocupación de seguridad importante en mujeres en edad fértil, la población en la que se plantearía este uso. El puntaje alto (0,9999) es solo una predicción computacional y no constituye evidencia clínica.

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
| 70844 | TOCTINO 30 mg cápsulas blandas | Cápsula blanda | No disponible |
| 84058 | Alitretinoína IFC 30 mg cápsulas blandas EFG | Cápsula blanda | No disponible |
| 70843 | TOCTINO 10 mg cápsulas blandas | Cápsula blanda | No disponible |
| 84057 | Alitretinoína IFC 10 mg cápsulas blandas EFG | Cápsula blanda | No disponible |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no del prospecto)**: el grafo de conocimiento asocia el fármaco con contraindicación en micosis fungoide y variantes, linfoma cutáneo primario de células T, micosis fungoide foliculotropa, reticulosis pagetoide localizada y enfermedad de la piel laxa granulomatosa.
- **Interacciones farmacológicas / dianas**: se identificaron 7 entradas farmacológicas: receptores RARα, RARβ y RARγ, receptores RXRα, RXRβ y RXRγ, y la subunidad 1 del complejo de la vitamina K epóxido reductasa (VKORC1). Esta última sugiere una posible interacción con anticoagulantes antagonistas de la vitamina K que conviene verificar.
- **Teratogenicidad**: los retinoides son teratógenos; es una preocupación de seguridad fundamental en mujeres en edad fértil.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para amenorrea se basa solo en el modelo (L5), sin ensayos ni literatura, sin vínculo mecanístico demostrado y con un conflicto de seguridad importante por la teratogenicidad en mujeres en edad fértil.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) y de un posible vínculo con la fisiopatología de la amenorrea
- Advertencias y contraindicaciones oficiales del prospecto de la AEMPS, así como las indicaciones aprobadas
- Estudios preclínicos o clínicos que respalden la indicación
- Evaluación de seguridad reproductiva y plan de prevención del embarazo
- Comparación con alternativas terapéuticas establecidas

---

**Nota sobre otras predicciones:** entre las otras indicaciones predichas, el **acné** es la única con respaldo indirecto (nivel L4, dos revisiones generales sobre retinoides en dermatología, sin estudios específicos de alitretinoína). Sin embargo, también quedó en decisión Hold por la teratogenicidad y la existencia de retinoides alternativos ya establecidos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


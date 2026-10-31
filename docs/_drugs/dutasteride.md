---
layout: default
title: Dutasteride
parent: Solo predicción del modelo (L5)
nav_order: 273
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
description: "Dutasteride: nueva indicación predicha, Hipertricosis universal congénita tipo Ambras (nivel de evidencia L5). Indicación original: Hiperplasia prostática benigna"
monitor_inn: "Dutasteride"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "migraine with brainstem aura", "familial isolated trichomegaly"]
---

# Dutasteride
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

## Dutasterida: De Hiperplasia Prostática Benigna a Hipertricosis Universal Congénita tipo Ambras
{: .text-alpha }

## Resumen en Una Frase

Dutasterida es un inhibidor dual de la 5-alfa-reductasa (tipos 1 y 2), utilizado originalmente para el tratamiento de la hiperplasia prostática benigna.
El modelo TxGNN predice que podría ser efectivo para la **hipertricosis universal congénita tipo Ambras**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hiperplasia prostática benigna |
| Nueva Indicación Predicha | Hipertricosis universal congénita tipo Ambras |
| Puntaje de Predicción TxGNN | 1,0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 10) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Dutasterida inhibe la 5-alfa-reductasa de tipo 1 y 2, enzimas que convierten la testosterona en dihidrotestosterona (DHT). Al reducir la DHT, disminuye el estímulo androgénico sobre la próstata, lo que explica su uso en la hiperplasia prostática benigna. Esa misma vía actúa sobre los folículos pilosos sensibles a andrógenos, por lo que existe una relación a nivel de tejido con el crecimiento del pelo.

Sin embargo, el síndrome de Ambras es una hipertricosis congénita asociada a alteraciones genéticas que afectan a la regulación de TRPS1 y no es principalmente una enfermedad dependiente de andrógenos. Reducir la DHT podría disminuir el vello terminal dependiente de andrógenos en algunas zonas, pero no necesariamente corregiría el fenotipo congénito, de modo que incluso el sentido del efecto es incierto.

El puntaje muy alto de TxGNN proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; no hay datos clínicos que lo respalden. Debe interpretarse con cautela. Los datos compilados para este informe no incluyen información detallada sobre el mecanismo de acción del fármaco.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal predicha.

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de un único principio activo, en cápsula blanda). Los datos compilados no incluyen el texto de la indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 65178 | AVIDART 0,5 mg cápsulas blandas | Cápsula blanda | Glaxosmithkline S.A. |
| 2578701 | AVIDART 0,5 mg cápsulas blandas | Cápsula blanda | Glaxosmithkline A.E.B.E. |
| 83259 | Dutasterida Tarbis 0,5 mg cápsulas blandas EFG | Cápsula blanda | Tarbis Farma S.L. |
| 77635 | Dutasterida Ratiopharm 0,5 mg cápsulas blandas EFG | Cápsula blanda | Teva Pharma S.L.U. |
| 81794 | DUTRYS 0,5 mg cápsulas blandas EFG | Cápsula blanda | Krka D.D. Novo Mesto |

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de precaución (según el grafo de conocimiento, no según el prospecto)**: atrofia multisistémica, síndrome de taquicardia postural ortostática, hipotensión ortostática, enfermedad hepática, enfermedad de la vesícula biliar, priapismo y síndrome del iris flácido intraoperatorio.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las de nivel moderado destacan aprepitant, cimetidina, claritromicina, clotrimazol y miconazol. Otras (calcitriol, pantoprazol, glimepirida, mesalazina, doxiciclina, morfina, metformina, omeprazol, rosiglitazona, lansoprazol, lactulosa, triamcinolona, prednisona, simvastatina e hidrocortisona) figuran con nivel no clasificado.
- **Nota adicional**: según el análisis de la predicción, existe una preocupación teratogénica (feminización de fetos masculinos), lo que desaconseja su uso en contextos del desarrollo.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura. Además, el mecanismo es débil: el síndrome de Ambras no es una condición dependiente de DHT y el efecto esperado es incierto.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) y un análisis mecanístico específico sobre la vía de TRPS1 y el crecimiento del pelo.
- Revisión de las advertencias y contraindicaciones del prospecto de la AEMPS.
- Evidencia preclínica o series de casos que muestren un efecto sobre el fenotipo de hipertricosis.
- Evaluar alternativas más plausibles con la misma lógica de acción, como hirsutismo (dependiente de andrógenos), y una evaluación de riesgo teratogénico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


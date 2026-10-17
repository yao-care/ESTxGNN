---
layout: default
title: Isotretinoin
parent: Solo predicción del modelo (L5)
nav_order: 435
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Isotretinoin: nueva indicación predicha, Hipertensión renovascular maligna (nivel de evidencia L5). Indicación original: Hipertensión / trastorno hipertensivo (según el grafo de conocimiento"
monitor_inn: "Isotretinoin"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Isotretinoin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Isotretinoína: De Hipertensión a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Según el grafo de conocimiento utilizado por el modelo, la isotretinoína figura con indicaciones originales de hipertensión y trastorno hipertensivo; sin embargo, en la práctica clínica es un retinoide empleado en dermatología (acné), por lo que esa indicación original debe tomarse con cautela.
El modelo TxGNN predice que podría ser efectiva para la **hipertensión renovascular maligna**, con **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.
La única base es el puntaje del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión / trastorno hipertensivo (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Hipertensión renovascular maligna |
| Puntaje de Predicción TxGNN | 99,01 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. La isotretinoína es un retinoide cuya farmacología conocida (supresión de las glándulas sebáceas, efectos sobre la diferenciación y proliferación celular) no guarda relación con el control de la presión arterial.

Las indicaciones originales de hipertensión que figuran en los datos son incoherentes con el uso clínico conocido de la isotretinoína y podrían ser un artefacto del grafo de conocimiento. Por ello, la relación entre la indicación original y la nueva indicación no puede considerarse mecanísticamente sólida.

La señalización de retinoides se ha explorado en modelos preclínicos de lesión y fibrosis renal, pero esto es especulativo y no está respaldado por evidencia en los datos compilados. Esto aplica también a la segunda predicción (enfermedad renal hipertensiva maligna, con el mismo puntaje de 99,01 %, lo que sugiere que ambos nodos están estrechamente relacionados en el grafo). La predicción debe tratarse con cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas son monofármaco, en cápsula blanda).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 67570 | ISOACNE 10 mg cápsulas blandas | Cápsula blanda | No disponible en los datos |
| 67878 | DERCUTANE 40 mg cápsulas blandas | Cápsula blanda | No disponible en los datos |
| 86649 | ISOTIORGA 40 mg cápsulas blandas | Cápsula blanda | No disponible en los datos |
| 78326 | DERCUTANE 30 mg cápsulas blandas | Cápsula blanda | No disponible en los datos |
| 82566 | ACNEMIN 10 mg cápsulas blandas EFG | Cápsula blanda | No disponible en los datos |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): trastornos de ansiedad, trastornos neuróticos y distímicos, trastornos psicóticos y mentales, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, pancreatitis, angioedema (incluido el hereditario), enfermedad inflamatoria intestinal, osteoporosis, lupus eritematoso sistémico, diabetes mellitus y cetoacidosis diabética, neutropenia y agranulocitosis, deficiencia de potasio y trastorno hipotensivo. Es relevante que figuren enfermedad renal y trastorno hipotensivo en relación con las indicaciones predichas.
- **Interacciones farmacológicas**: se registran 98 interacciones. Entre las de nivel **mayor** se encuentran doxiciclina, minociclina, tetraciclina y vitamina A. Entre las de nivel moderado se incluyen corticoides (betametasona, budesonida, dexametasona, hidrocortisona, prednisolona, prednisona, triamcinolona), warfarina, dicumarol, etanol, naltrexona, nitisinona, fostamatinib, ivacaftor, lumacaftor y abametapir tópico.
- **Otras consideraciones**: de forma general, la isotretinoína se asocia a teratogenicidad, elevación de lípidos y efectos hepáticos, que habría que ponderar cuidadosamente en pacientes con hipertensión grave o insuficiencia renal que reciben varios antihipertensivos.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única base es un puntaje alto del modelo (99,01 %), sin ensayos clínicos ni literatura, sin mecanismo de acción disponible y con una indicación original incoherente con el uso clínico conocido. Además, el perfil de seguridad de la isotretinoína plantea dudas importantes en pacientes con hipertensión maligna y afectación renal.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un vacío de datos bloqueante para el cribado de seguridad.
- Obtener los datos del mecanismo de acción (por ejemplo, desde DrugBank) para analizar un posible vínculo mecanístico.
- Verificar y corregir las indicaciones originales del grafo de conocimiento, que parecen un artefacto.
- Realizar una búsqueda sistemática de literatura y ensayos, incluidos estudios preclínicos de retinoides en daño renal e hipertensión.
- Evaluar la relación beneficio-riesgo en población con hipertensión maligna y enfermedad renal, considerando las interacciones y contraindicaciones señaladas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Benazepril
parent: Solo predicción del modelo (L5)
nav_order: 92
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Benazepril: nueva indicación predicha, Enfermedad renal hipertensiva maligna (nivel de evidencia L5). Indicación original: Hipertensión arterial (según el grafo de conocimiento"
monitor_inn: "BENAZEPRIL"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Benazepril
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Benazepril: De Hipertensión Arterial a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Benazepril es un inhibidor de la enzima convertidora de angiotensina (IECA), originalmente utilizado para el tratamiento de la hipertensión arterial.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (según el grafo de conocimiento; el texto de indicación de las autorizaciones españolas no está disponible) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99,65% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, benazepril pertenece a la clase de los IECA: bloquea la conversión de angiotensina I en angiotensina II, reduciendo la vasoconstricción y la activación del sistema renina-angiotensina-aldosterona (SRAA).

La enfermedad renal hipertensiva maligna implica hipertensión grave con activación del SRAA y daño renal, por lo que el bloqueo del SRAA es biológicamente plausible. Sin embargo, el puntaje elevado de TxGNN (0,9965) es una predicción computacional que probablemente se deba a la estrecha relación con la indicación ya aprobada de hipertensión. Es más una extensión de la indicación existente que un reposicionamiento genuino.

Otras predicciones del modelo tienen un respaldo igual o más débil:
- **Hipertensión renovascular maligna** (99,65%): plausible mecanísticamente, pero en estenosis bilateral de la arteria renal o riñón único los IECA pueden causar lesión renal aguda. Sin ensayos ni literatura.
- **Hipertensión pulmonar por enfermedad pulmonar o hipoxia** (99,60%): vínculo solo teórico. Las tres publicaciones recuperadas tratan fórmulas de medicina tradicional china en modelos de fibrosis renal y miocárdica; no involucran benazepril ni hipertensión pulmonar, por lo que no son evidencia relevante. Los IECA no son un tratamiento establecido y la vasodilatación sistémica podría empeorar la relación ventilación-perfusión.
- **Hipertensión pulmonar de mecanismo multifactorial incierto** (99,60%) y **síndrome de Braddock** (99,44%): sin fundamento mecanístico ni evidencia con los datos disponibles.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal. Las tres publicaciones recuperadas para la hipertensión pulmonar (PMID 38803876, 31007700 y 31317035) son estudios preclínicos con fórmulas herbales y no guardan relación con benazepril, por lo que no se consideran evidencia.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59552 | CIBACEN 20 mg comprimidos recubiertos con película | Comprimido | No disponible |
| 59551 | CIBACEN 5 mg comprimidos recubiertos con película | Comprimido | No disponible |
| 59553 | CIBACEN 10 mg comprimidos recubiertos con película | Comprimido | No disponible |

Titular: Meda Pharma S.L. Las tres autorizaciones son de medicamento con un solo principio activo y están vigentes.

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del texto del prospecto): angioedema (incluido el hereditario, el adquirido y el inducido por bloqueadores del SRAA), insuficiencia o enfermedad hepática, encefalopatía/coma hepático, enfermedad renal, anuria, pancreatitis, enfermedad de la vesícula biliar, lupus eritematoso sistémico, enfermedades del tejido conectivo, neutropenia y agranulocitosis, hipotensión, diabetes mellitus y cetoacidosis diabética, deficiencia de potasio, hiperparatiroidismo, osteítis fibrosa, enfermedades óseas y del cartílago, ictericia neonatal y piouréter.
- **Interacciones farmacológicas**: se identificaron 100 interacciones; las primeras 20 son de nivel moderado. Destacan los antidiabéticos (alogliptina, acetohexamida, clorpropamida, dapagliflozina, exenatida, glimepirida, glipizida, gliburida), numerosas insulinas (humana, aspart, degludec, detemir, glargina, glulisina, lispro, entre otras), hidrocortisona y glicerina.
- **Aspecto específico de la predicción**: en estenosis bilateral de la arteria renal o riñón único, los IECA pueden provocar lesión renal aguda, un riesgo relevante para las indicaciones renales y renovasculares propuestas.

No se dispone de advertencias principales ni de contraindicaciones del prospecto; consultar el prospecto de AEMPS para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las predicciones son solo computacionales (nivel L5), sin ensayos ni literatura relevante, y las de mayor puntaje son en gran medida extensiones de la indicación ya aprobada de hipertensión. Además, falta la información de seguridad del prospecto, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), que es un dato bloqueante.
- Obtener el mecanismo de acción desde DrugBank.
- Realizar una búsqueda dirigida de ensayos y literatura sobre benazepril en hipertensión maligna y nefropatía hipertensiva.
- Evaluar el riesgo renal en estenosis de la arteria renal para la indicación renovascular.
- Descartar o reevaluar las predicciones de hipertensión pulmonar y síndrome de Braddock por ausencia de respaldo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Rivaroxaban
parent: Solo predicción del modelo (L5)
nav_order: 708
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-31
monitor_inn: "rivaroxaban"
predicted_indications: ["rheumatoid arthritis", "gout", "HIV infectious disease", "brachydactyly-syndactyly syndrome"]
description: "Rivaroxaban: nueva indicación predicha, Artritis reumatoide (rheumatoid arthritis) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Rivaroxaban
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Rivaroxaban: Artritis reumatoide (rheumatoid arthritis)
{: .text-alpha }

## Resumen en Una Frase

Rivaroxabán es un inhibidor directo del factor Xa (anticoagulante oral), comercializado en España en múltiples presentaciones, aunque los datos compilados no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **artritis reumatoide**, con **0 ensayos clínicos** y **4 publicaciones**, ninguna de las cuales evalúa rivaroxabán como tratamiento de esta enfermedad.
La predicción se apoya únicamente en el puntaje del modelo y debe considerarse una hipótesis.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Artritis reumatoide (rheumatoid arthritis) |
| Puntaje de Predicción TxGNN | 0.9957 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 9) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Rivaroxabán es un inhibidor directo del factor Xa de la coagulación. Los datos compilados no incluyen una descripción detallada del mecanismo de acción original, por lo que el análisis mecanístico es limitado.

Existe un vínculo plausible, pero no probado, a través del eje coagulación-inflamación: la señalización del factor Xa y de la trombina (por ejemplo, vía PAR-1/PAR-2) podría contribuir a la inflamación sinovial y al depósito de fibrina. Además, las enfermedades autoinmunes se asocian con alteraciones en la generación de trombina (PMID 34175144).

Esto sustenta solo una hipótesis, no una afirmación de reposicionamiento. Ninguna de las publicaciones recuperadas evalúa rivaroxabán como tratamiento de la artritis reumatoide y no hay ensayos clínicos registrados.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Revisión | JAMA | Revisión sobre diagnóstico y tratamiento de la tromboembolia venosa de extremidades inferiores; no trata artritis reumatoide |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Revisión | La Revue de médecine interne | El ensayo de generación de trombina permite evaluar la hipercoagulabilidad en enfermedades autoinmunes; apoya el vínculo coagulación-autoinmunidad |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohorte | PloS one | Comparación de adherencia a rivaroxabán frente a apixabán en fibrilación auricular no valvular; no relacionado con artritis reumatoide |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Reporte de caso | Cureus | Paciente de 88 años con fibrilación auricular y artritis reumatoide (con esteroides orales) que presentó eventos embólicos pese a anticoagulación |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 91024 | ELMARDYA 15 MG + 20 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | Comprimido recubierto con película | No disponible |
| 89712 | RIVAROXABAN CINFA 15 MG CÁPSULAS DURAS EFG | Cápsula dura | No disponible |
| 90399 | RIVAROXABAN OLPHA 20 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | Comprimido recubierto con película | No disponible |
| 84258 | RIVAROXABAN AUROBINDO 10 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | Comprimido recubierto con película | No disponible |
| 08472008 | XARELTO 10 mg COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible |

Hay 20 autorizaciones vigentes en total (todas de medicamentos de un solo principio activo); aquí se muestran las 5 primeras.

---

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento del modelo** (no proceden del texto del prospecto): insuficiencia hepática, enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar y trastornos de la coagulación sanguínea.
- **Interacciones farmacológicas**: se identificaron 313 interacciones. Entre las de nivel **mayor** destacan:
  - Ácido acetilsalicílico
  - Cobicistat
  - Deferasirox
  - Ibritumomab tiuxetán
  - Tositumomab (I-131)

  Entre las de nivel **moderado** figuran aprepitant, dexametasona, cimetidina, claritromicina, eliglustat, miconazol, clotrimazol, rolapitant y sugammadex, entre otras.

Para el resto de la información de seguridad (advertencias y contraindicaciones oficiales), consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje TxGNN muy alto, pero no existen ensayos clínicos ni literatura que evalúe rivaroxabán en artritis reumatoide (nivel L5). Además, el perfil hemorrágico del fármaco exige una justificación sólida antes de explorar un uso nuevo.

**Para avanzar se necesita:**
- Estudios preclínicos que respalden el papel del factor Xa/trombina en la inflamación sinovial.
- Datos detallados del mecanismo de acción y del texto de las indicaciones aprobadas.
- Revisión de las advertencias y contraindicaciones del prospecto de la AEMPS.
- Evaluación del riesgo hemorrágico y de las interacciones en pacientes con artritis reumatoide (por ejemplo, con antiinflamatorios y corticoides).
- Si se avanza, un ensayo exploratorio de fase 2 con plan de monitoreo de seguridad.

---

### Nota sobre otras predicciones

Los datos compilados incluyen otras tres predicciones, todas con decisión **Hold** y sin respaldo clínico:
- **Gota** (0.9951, L5): sin ensayos ni literatura que respalde eficacia.
- **Infección por VIH** (0.9917, L4): la literatura trata de interacciones y riesgo de sangrado con antirretrovirales potenciados, no de un efecto terapéutico. El único ensayo (NCT00786422) es de fase 2 en trombosis venosa y no evalúa VIH.
- **Síndrome de braquidactilia-sindactilia** (0.9910, L5): sin ensayos, sin literatura y sin mecanismo plausible; probable artefacto del modelo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


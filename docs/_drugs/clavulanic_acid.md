---
layout: default
title: Clavulanic Acid
parent: Solo predicción del modelo (L5)
nav_order: 188
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
description: "Clavulanic Acid: nueva indicación predicha, Uretritis por Ureaplasma (nivel de evidencia L5). Indicación original: Infección del tracto urinario (según la base de conocimiento"
monitor_inn: "clavulanic acid"
predicted_indications: ["Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "urogenital tuberculosis", "celiac trunk compression syndrome", "abdominal ectopic pregnancy", "abdominal cystic lymphangioma", "lymph node palisaded myofibroblastoma", "disease of uterine broad ligament"]
---

# Clavulanic Acid
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

## Ácido clavulánico: De Infección del Tracto Urinario a Uretritis por Ureaplasma
{: .text-alpha }

## Resumen en Una Frase

El ácido clavulánico es un inhibidor de betalactamasas que se utiliza combinado con amoxicilina para tratar infecciones bacterianas, entre ellas la infección del tracto urinario y la neumonía bacteriana.
El modelo TxGNN predice que podría ser efectivo para **uretritis por Ureaplasma**, aunque no existen **ensayos clínicos** registrados y solo hay **4 publicaciones** de relevancia limitada.
La propia evaluación mecanística indica que esta predicción probablemente sea un artefacto de la red y que no está respaldada biológicamente.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección del tracto urinario (según la base de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Uretritis por Ureaplasma |
| Puntaje de Predicción TxGNN | 0,9993 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 13) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el ácido clavulánico es un inhibidor de betalactamasas que se combina con amoxicilina: protege al antibiótico de la degradación enzimática y amplía su espectro frente a bacterias productoras de estas enzimas. Su eficacia en infecciones urinarias y respiratorias bacterianas es conocida.

En este caso concreto, la predicción **no resulta razonable desde el punto de vista mecanístico**. *Ureaplasma* carece de pared celular y, por tanto, es intrínsecamente resistente a los betalactámicos. El ácido clavulánico no tiene actividad propia frente a este microorganismo. La puntuación alta del modelo se explica probablemente por la asociación en la red entre uretritis e infección urinaria, no por un efecto farmacológico real.

Entre las demás predicciones del modelo, la uretritis gonocócica es la biológicamente más plausible (el fármaco restaura la actividad de la amoxicilina frente a *Neisseria gonorrhoeae* productora de penicilinasa). Se menciona solo como contexto, pues el informe se centra en la predicción de mayor puntuación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21947096](https://pubmed.ncbi.nlm.nih.gov/21947096/) | 2011 | Revisión | Rev Esp Quimioter | Mejor tratamiento empírico de la uretritis en el centro de Madrid; no demuestra eficacia del ácido clavulánico frente a *Ureaplasma* |
| [19544099](https://pubmed.ncbi.nlm.nih.gov/19544099/) | 2009 | Revisión | Rev Esp Quimioter | Prevalencia y tendencia de los microorganismos causantes de uretritis en varones en Madrid (3 años) |
| [9669200](https://pubmed.ncbi.nlm.nih.gov/9669200/) | 1998 | Revisión | Int J Androl | Posible papel de las bacterias anaerobias en la prostatitis crónica |
| [34366085](https://pubmed.ncbi.nlm.nih.gov/34366085/) | 2021 | Reporte de caso | Infect Dis Now | Primera asociación de *Pasteurella bettyae* con uretritis y balanitis en hombres que tienen sexo con hombres |

Ninguna publicación evalúa el ácido clavulánico en uretritis por *Ureaplasma*.

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de medicamentos de un solo principio activo con amoxicilina/ácido clavulánico). El texto de indicación aprobada no está disponible en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 83523 | Amoxicilina/Ácido Clavulánico Aurovitas 875 mg/125 mg EFG | Comprimido recubierto con película | No disponible |
| 59515 | Augmentine 875 mg/125 mg | Comprimido recubierto con película | No disponible |
| 65136 | Amoxicilina/Ácido Clavulánico Sandoz 1000 mg/200 mg EFG | Polvo para solución inyectable y para perfusión | No disponible |
| 66565 | Amoxicilina/Ácido Clavulánico Cinfa 250 mg/62,5 mg EFG | Polvo para suspensión oral en sobres | No disponible |
| 89514 | Amoxicilina/Ácido Clavulánico Sandoz 100 mg/ml + 12,5 mg/ml EFG | Polvo para suspensión oral | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no del prospecto)**: enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal, colestasis (incluidas la colestasis intrahepática recurrente benigna y la familiar), mononucleosis infecciosa y síndrome de infección crónica por virus de Epstein-Barr.
- **Interacciones farmacológicas** (16 detectadas):
  - **Mayores**: leflunomida y teriflunomida.
  - **Moderadas**: naltrexona, balsalazida, asparaginasa de *E. coli*, brentuximab vedotina, clofarabina, epirubicina, idelalisib, interferón beta-1a e interferón beta-1b, pegaspargasa, peginterferón beta-1a, tioguanina, trabectedina y metotrexato.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura relevante, y es mecanísticamente inconsistente: *Ureaplasma* carece de pared celular y es intrínsecamente resistente a los betalactámicos.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco (consulta a DrugBank).
- Obtención y análisis del prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), pues sin ello no se puede completar el cribado de seguridad.
- Evidencia de sensibilidad in vitro o clínica de *Ureaplasma* a amoxicilina/clavulanato (poco probable).
- Priorizar candidatas más plausibles, como la uretritis gonocócica (nivel L3, evidencia antigua de los años 80 y de relevancia clínica actual limitada por las resistencias), si se desea explorar nuevas indicaciones.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


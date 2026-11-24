---
layout: default
title: Clavulanic Acid
parent: Solo predicción del modelo (L5)
nav_order: 188
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
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
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: al menos 13; autorizadas no comercializadas: 2; revocadas o suspendidas: 5) |
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

El texto de indicación aprobada no está disponible en los datos compilados.

<!-- review:begin es-lic-20261105-clavulanic_acid-1 -->

> **Corrección de revisión (2026-11-05)**: Texto original: "Se listan 5 de las 20 autorizaciones vigentes (todas de medicamentos de un solo principio activo con amoxicilina/ácido clavulánico). El texto de indicación aprobada no está disponible en los datos compilados." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-clavulanic_acid-1 -->

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 83523 | AMOXICILINA/ACIDO CLAVULANICO AUROVITAS 875 MG/125 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Aurovitas Spain, S.A.U. | Comercializada |
| 80066 | AMOXICILINA/ACIDO CLAVULANICO TAD 875 MG/125 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Tad Pharma Gmbh | Comercializada |
| 64425 | AMOXICILINA/ACIDO CLAVULANICO ARDINECLAV 500/125 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorio Reig Jofre, S.A. | Comercializada |
| 83994 | AMOXICILINA/ACIDO CLAVULANICO COMBIX 875 MG/125 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorios Combix S.L.U. | Comercializada |
| 65136 | AMOXICILINA/ACIDO CLAVULANICO SANDOZ 1000 mg/200 mg POLVO PARA SOLUCION INYECTABLE Y PARA PERFUSION EFG | POLVO PARA SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN | Sandoz Farmaceutica S.A. | Comercializada |
| 66565 | AMOXICILINA/ACIDO CLAVULANICO CINFA 250 mg /62,5 mg POLVO PARA SUSPENSION ORAL EN SOBRES EFG | POLVO PARA SUSPENSIÓN ORAL | Laboratorios Cinfa S.A. | Comercializada |
| 70189 | AMOXICILINA/ACIDO CLAVULANICO NORMON 500 mg /125 mg COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Laboratorios Normon S.A. | Comercializada |
| 59515 | AUGMENTINE 875 mg/125 mg COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Glaxosmithkline S.A. | Comercializada |
| 64712 | AMOXICILINA/ ACIDO CLAVULANICO VIATRIS 875/125 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Viatris Pharmaceuticals S.L. | Comercializada |
| 89514 | AMOXICILINA/ACIDO CLAVULANICO SANDOZ 100 MG/ML + 12,5 MG/ML POLVO PARA SUSPENSION ORAL EFG | POLVO PARA SUSPENSIÓN ORAL | Sandoz Farmaceutica S.A. | Comercializada |

Se muestran 10 de al menos 20 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas. Los datos de este informe solo incluyen parte de las autorizaciones.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-05 | Eliminado: "Se listan 5 de las 20 autorizaciones vigentes (todas de medicamentos de un solo principio activo con amoxicilina/ácido clavulánico)" | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


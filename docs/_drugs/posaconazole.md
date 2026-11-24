---
layout: default
title: Posaconazole
parent: Solo predicción del modelo (L5)
nav_order: 651
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "posaconazole"
predicted_indications: ["pneumocystosis"]
description: "Posaconazole: nueva indicación predicha, Neumocistosis (pneumocystosis) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 18 (comercializadas: 13; autorizadas no comercializadas: 3)"
---

# Posaconazole
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

## Posaconazole: Neumocistosis (pneumocystosis)
{: .text-alpha }

## Resumen en Una Frase

Posaconazol es un antifúngico azólico, utilizado originalmente para tratar y prevenir infecciones fúngicas como la aspergilosis, la candidiasis (incluida la oral), la histoplasmosis, la coccidioidomicosis y otras micosis.
El modelo TxGNN predice que podría ser efectivo para **neumocistosis**, pero la evidencia directa es **nula**: hay **1 ensayo clínico** que evalúa otro fármaco (rezafungina) y **5 publicaciones** de contexto general, ninguna con datos de posaconazol en esta indicación.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Neumocistosis (pneumocystosis) |
| Puntaje de Predicción TxGNN | 0.9977 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 13 de 18; autorizadas no comercializadas: 3; revocadas o suspendidas: 2) |
| Número de Autorizaciones | 18 (comercializadas: 13) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Posaconazol inhibe la enzima fúngica lanosterol 14-alfa-desmetilasa (CYP51), bloqueando la síntesis de ergosterol, un componente esencial de la membrana fúngica. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción del fármaco, por lo que este análisis se basa en el conocimiento farmacológico general de la clase azólica.

Aquí la predicción es **débil desde el punto de vista biológico**. *Pneumocystis jirovecii* carece de ergosterol en su membrana y utiliza colesterol, por lo que los azoles no tienen una diana directa plausible. El puntaje alto de TxGNN (0,9977) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Cualquier beneficio sería especulativo, por ejemplo, por actividad frente a hongos coinfectantes en pacientes inmunodeprimidos. La relación entre la indicación original (micosis por hongos con ergosterol) y la nueva (neumocistosis) es taxonómica y clínica, pero no mecanística.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Fase 3 | Completado | 602 | Estudio ReSPECT: rezafungina intravenosa frente al régimen antimicrobiano estándar para prevenir enfermedades fúngicas invasivas en trasplante alogénico de médula ósea. **No incluye posaconazol como brazo**, por lo que no aporta evidencia directa. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Revisión | Swiss Medical Weekly | Panorama de candidiasis, aspergilosis, criptococosis y neumonía por *Pneumocystis*; menciona que la profilaxis con posaconazol redujo las infecciones fúngicas invasivas en pacientes hemato-oncológicos de alto riesgo |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Revisión | Clinical Pharmacokinetics | Penetración de antifúngicos en el líquido epitelial pulmonar; datos farmacocinéticos, no de eficacia en neumocistosis |
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Guía | The Lancet Infectious Diseases | Recomendaciones de la Sociedad Británica de Micología Médica para el diagnóstico de enfermedades fúngicas graves (actualización 2025) |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Guía | Chinese Journal of Tuberculosis and Respiratory Diseases | Guía china 2025 para el diagnóstico y manejo de enfermedades fúngicas pulmonares invasivas |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohorte | Transplant Infectious Disease | Complicaciones infecciosas en la enfermedad injerto contra huésped aguda tras trasplante hepático |

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 105320004 | NOXAFIL 300 MG CONCENTRADO PARA SOLUCION PARA PERFUSION | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Merck Sharp & Dohme B.V. | Comercializada |
| 1191379002 | POSACONAZOL ACCORD 100 MG COMPRIMIDOS GASTRORRESISTENTES EFG | COMPRIMIDO GASTRORRESISTENTE | Accord Healthcare S.L.U. | Comercializada |
| 84701 | POSACONAZOL GLENMARK 40 MG/ML SUSPENSION ORAL EFG | SUSPENSIÓN ORAL | Glenmark Arzneimittel Gmbh | Comercializada |
| 85039 | POSACONAZOL FRESENIUS KABI 100 MG COMPRIMIDOS GASTRORRESISTENTES | COMPRIMIDO GASTRORRESISTENTE | Fresenius Kabi España, S.A.U. | Comercializada |
| 84646 | POSACONAZOL STADA 100 MG COMPRIMIDOS GASTRORRESISTENTES EFG | COMPRIMIDO GASTRORRESISTENTE | Laboratorio Stada S.L. | Comercializada |
| 90350 | POSACONAZOL VIVANTA 100 MG COMPRIMIDOS GASTRORRESISTENTES EFG | COMPRIMIDO GASTRORRESISTENTE | Vivanta Generics S.R.O. | Comercializada |
| 85374 | POSACONAZOL ABDI 100 MG COMPRIMIDOS GASTRORRESISTENTES | COMPRIMIDO GASTRORRESISTENTE | Abdi Farma Unipessoal Lda. | Comercializada |
| 90284 | POSACONAZOL ALMOVAR 100 MG COMPRIMIDOS GASTRORRESISTENTES EFG | COMPRIMIDO GASTRORRESISTENTE | Laboratorios Basi Industria Farmaceutica S.A. | Comercializada |
| 05320001 | NOXAFIL 40 MG/ML SUSPENSION ORAL | SUSPENSIÓN ORAL | Merck Sharp & Dohme B.V. | Comercializada |
| 84010 | POSACONAZOL ACCORD 300 MG CONCENTRADO PARA SOLUCION PARA PERFUSION EFG | CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Accord Healthcare S.L.U. | Comercializada |

Se muestran 10 de 18 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 269 interacciones. Entre las principales:
  - **Mayores**: loperamida, triamcinolona, budesonida.
  - **Moderadas**: famotidina, ranitidina, cimetidina, omeprazol, rabeprazol (antiácidos e inhibidores de la bomba de protones), hidrocortisona, dexametasona, betametasona, aprepitant, claritromicina, saxagliptina, bisacodilo, ácido picosulfúrico y polietilenglicol.

<!-- review:begin es-lic-20261105-posaconazole-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Hay 18 autorizaciones vigentes en total (todas de medicamento con un solo principio activo, ninguna cancelada); la tabla muestra las 5 principales." Eliminado: afirmaba que el medicamento no está autorizado o comercializado en España, o que sus autorizaciones están revocadas o suspendidas, lo que no coincide con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-posaconazole-1 -->

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5): el único ensayo identificado evalúa otro fármaco y la literatura es de contexto general. Además, *Pneumocystis* carece de ergosterol, por lo que el mecanismo de los azoles no tiene una diana plausible, y el alto puntaje del modelo TxGNN (aprendizaje profundo) puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

**Para avanzar se necesita:**
- Datos in vitro o preclínicos que demuestren actividad de posaconazol frente a *Pneumocystis jirovecii*.
- Estudios clínicos o series de casos de posaconazol en neumocistosis, frente a los tratamientos estándar (p. ej., cotrimoxazol).
- Obtener y revisar el prospecto de la AEMPS (advertencias y contraindicaciones) y los datos detallados del mecanismo de acción.
- Evaluar el impacto de las numerosas interacciones farmacológicas en poblaciones inmunodeprimidas polimedicadas.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Eliminado: "Hay 18 autorizaciones vigentes en total (todas de medicamento con un solo principio activo, ninguna cancelada); la tabla muestra las 5 princ" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


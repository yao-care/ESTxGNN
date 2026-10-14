---
layout: default
title: Posaconazole
parent: Solo predicción del modelo (L5)
nav_order: 651
evidence_level: L5
indication_count: 1
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Posaconazol: De Micosis Invasivas (Candidiasis y Aspergilosis) a Neumocistosis

## Resumen en Una Frase

Posaconazol es un antifúngico azólico, utilizado originalmente para tratar y prevenir infecciones fúngicas como la aspergilosis, la candidiasis (incluida la oral), la histoplasmosis, la coccidioidomicosis y otras micosis.
El modelo TxGNN predice que podría ser efectivo para **neumocistosis**, pero la evidencia directa es **nula**: hay **1 ensayo clínico** que evalúa otro fármaco (rezafungina) y **5 publicaciones** de contexto general, ninguna con datos de posaconazol en esta indicación.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Micosis invasivas y superficiales (aspergilosis, candidiasis, histoplasmosis, coccidioidomicosis, entre otras; según el grafo de conocimiento, ya que los textos de autorización no incluyen indicación) |
| Nueva Indicación Predicha | Neumocistosis |
| Puntaje de Predicción TxGNN | 99,77 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 18 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Posaconazol inhibe la enzima fúngica lanosterol 14-alfa-desmetilasa (CYP51), bloqueando la síntesis de ergosterol, un componente esencial de la membrana fúngica. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción del fármaco, por lo que este análisis se basa en el conocimiento farmacológico general de la clase azólica.

Aquí la predicción es **débil desde el punto de vista biológico**. *Pneumocystis jirovecii* carece de ergosterol en su membrana y utiliza colesterol, por lo que los azoles no tienen una diana directa plausible. El puntaje alto de TxGNN (0,998) probablemente refleja una asociación en el grafo con otras infecciones fúngicas, y no un mecanismo biológicamente respaldado.

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

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 105320004 | Noxafil 300 mg concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible |
| 05320001 | Noxafil 40 mg/ml suspensión oral | Suspensión oral | No disponible |
| 105320002 | Noxafil 100 mg comprimidos gastrorresistentes | Comprimido gastrorresistente | No disponible |
| 84010 | Posaconazol Accord 300 mg concentrado para solución para perfusión EFG | Concentrado para solución para perfusión | No disponible |
| 84646 | Posaconazol Stada 100 mg comprimidos gastrorresistentes EFG | Comprimido gastrorresistente | No disponible |

Hay 18 autorizaciones vigentes en total (todas de medicamento con un solo principio activo, ninguna cancelada); la tabla muestra las 5 principales.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 269 interacciones. Entre las principales:
  - **Mayores**: loperamida, triamcinolona, budesonida.
  - **Moderadas**: famotidina, ranitidina, cimetidina, omeprazol, rabeprazol (antiácidos e inhibidores de la bomba de protones), hidrocortisona, dexametasona, betametasona, aprepitant, claritromicina, saxagliptina, bisacodilo, ácido picosulfúrico y polietilenglicol.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5): el único ensayo identificado evalúa otro fármaco y la literatura es de contexto general. Además, *Pneumocystis* carece de ergosterol, por lo que el mecanismo de los azoles no tiene una diana plausible, y el alto puntaje de TxGNN parece una asociación de grafo.

**Para avanzar se necesita:**
- Datos in vitro o preclínicos que demuestren actividad de posaconazol frente a *Pneumocystis jirovecii*.
- Estudios clínicos o series de casos de posaconazol en neumocistosis, frente a los tratamientos estándar (p. ej., cotrimoxazol).
- Obtener y revisar el prospecto de la AEMPS (advertencias y contraindicaciones) y los datos detallados del mecanismo de acción.
- Evaluar el impacto de las numerosas interacciones farmacológicas en poblaciones inmunodeprimidas polimedicadas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


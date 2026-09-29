---
layout: default
title: Teriflunomide
parent: Evidencia alta (L1-L2)
nav_order: 521
evidence_level: L1
indication_count: 1
---

# Teriflunomide
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **1** 
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

# Teriflunomida: De Indicación Original No Registrada a Esclerosis Múltiple Remitente-Recurrente

## Resumen en Una Frase

Los datos de AEMPS no incluyen la indicación original de la teriflunomida. Según la información farmacológica disponible, se usa para reducir los brotes en la esclerosis múltiple (EM) recurrente.
El modelo TxGNN predice eficacia en **esclerosis múltiple remitente-recurrente (EMRR)**, con **28 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección.
Como el fármaco ya está comercializado para EM recurrente, este resultado confirma una indicación existente y no constituye un reposicionamiento propiamente dicho.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos (los textos de indicación de las autorizaciones AEMPS están vacíos) |
| Nueva Indicación Predicha | Esclerosis múltiple remitente-recurrente |
| Puntaje de Predicción TxGNN | 99.24% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados de mecanismo de acción en el registro del fármaco. Sin embargo, los datos farmacológicos y la literatura aportada indican que la teriflunomida inhibe de forma selectiva y reversible la enzima mitocondrial dihidroorotato deshidrogenasa (DHODH). Esto bloquea la síntesis de novo de pirimidinas y reduce la proliferación de linfocitos (Scott, *Drugs*, 2019). Según la farmacología general, y sin verificarlo contra los datos aportados, es además el metabolito activo de la leflunomida.

En la EMRR, la inflamación autoinmune está impulsada por linfocitos T y B activados. Al frenar la expansión de estas células, el mecanismo de la teriflunomida encaja con la fisiopatología de la enfermedad.

El puntaje TxGNN tan alto (0.992) es coherente con que la EM recurrente ya es una indicación conocida y comercializada. Los ensayos de fase 3 (incluido el pivotal controlado con placebo) y los estudios comparativos posteriores respaldan esa indicación.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Fase 3 | Completado | 1088 | Ensayo pivotal, doble ciego y controlado con placebo, sobre la reducción de recaídas y la progresión de la discapacidad en EM con recaídas |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Fase 3 | Completado | 324 | Teriflunomida (dos dosis) frente a interferón beta-1a, con evaluador ciego y extensión a largo plazo |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Fase 3 | Completado | 742 | Extensión a largo plazo del estudio pivotal para documentar la seguridad de 7 y 14 mg |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Fase 2 | Completado | 147 | Extensión de fase 2: seguridad y eficacia a largo plazo en EM con recaídas |
| [NCT04788615](https://clinicaltrials.gov/study/NCT04788615) | Fase 3 | Completado | 185 | Ofatumumab frente a DMT de primera línea en EM recién diagnosticada. El papel exacto de la teriflunomida no está confirmado |
| [NCT02490982](https://clinicaltrials.gov/study/NCT02490982) | N/A | Completado | 106 | Estudio observacional de efectividad de teriflunomida en la práctica clínica habitual en EMRR |
| [NCT03302442](https://clinicaltrials.gov/study/NCT03302442) | N/A | Completado | 3000 | Comparación observacional de dimetilfumarato y teriflunomida en la cohorte francesa de EM |
| [NCT02776072](https://clinicaltrials.gov/study/NCT02776072) | N/A | Completado | 2978 | Estudio retrospectivo global de resultados en la vida real con Tecfidera, Copaxone, Aubagio y Gilenya |
| [NCT01881191](https://clinicaltrials.gov/study/NCT01881191) | N/A | Completado | 50 | Efecto de teriflunomida sobre la patología de la sustancia gris mediante RM durante 12 meses |
| [NCT03561402](https://clinicaltrials.gov/study/NCT03561402) | N/A | Completado | 24 | Biomarcadores asociados a la actividad de la enfermedad en pacientes tratados con teriflunomida |

## Evidencia de Literatura

En los ECA comparativos más recientes, la teriflunomida actúa como comparador activo.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | ECA | N Engl J Med | Ofatumumab frente a teriflunomida en EM recurrente |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | ECA | N Engl J Med | Tolebrutinib frente a teriflunomida en EM recurrente |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | ECA | N Engl J Med | Ublituximab frente a teriflunomida en EM recurrente |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | ECA | Lancet Neurol | Evobrutinib frente a teriflunomida como comparador activo (dos ensayos de fase 3) |
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | ECA | JAMA Neurol | Estudio OPTIMUM: ponesimod frente a teriflunomida en EM recurrente |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Metaanálisis en red | Cochrane Database Syst Rev | Comparación de inmunomoduladores e inmunosupresores en EMRR |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Revisión | Drugs | Teriflunomida es eficaz y en general bien tolerada en EM recurrente, según ECA y datos de práctica real |
| [26758290](https://pubmed.ncbi.nlm.nih.gov/26758290/) | 2016 | Revisión | CNS Drugs | Revisión de la ficha técnica europea: resultados clínicos, seguridad y consideraciones prácticas |
| [37382446](https://pubmed.ncbi.nlm.nih.gov/37382446/) | 2023 | Revisión | Expert Rev Neurother | Teriflunomida como terapia oral de primera línea en EMRR pediátrica, aprobada en la UE |
| [33620411](https://pubmed.ncbi.nlm.nih.gov/33620411/) | 2021 | Revisión | JAMA | Revisión general del diagnóstico y tratamiento de la EM |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1221693002 | Teriflunomida Accord 14 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 89393 | Teriflunomida Viatris Pharmaceuticals 14 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 1130838006 | Aubagio 7 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 88844 | Teriflunomida Dr. Reddys 7 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 88753 | Teriflunomida Krka 14 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |

Se muestran 5 de las 20 autorizaciones. El texto de indicación aprobada no figura en los datos recibidos.

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: no se registran interacciones fármaco-fármaco. Solo consta la interacción farmacológica con su diana, la dihidroorotato deshidrogenasa (gen *DHODH*), coherente con su mecanismo de acción.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay varios ensayos de fase 3 completados, entre ellos el pivotal controlado con placebo, y metaanálisis y ECA comparativos que respaldan la eficacia en EM recurrente (nivel L1). Sin embargo, es una indicación ya comercializada y falta información de seguridad de AEMPS, por lo que conviene avanzar con salvaguardas.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS para completar advertencias y contraindicaciones (bloqueante para el cribado de seguridad).
- Confirmar el texto de la indicación aprobada en las autorizaciones y la indicación original del fármaco.
- Completar los datos de mecanismo de acción desde DrugBank.
- Revisar el rol de la teriflunomida en los ensayos con relevancia pendiente (por ejemplo, NCT04788615).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


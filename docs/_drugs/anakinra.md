---
layout: default
title: Anakinra
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
---

# Anakinra
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Anakinra: De Artritis Reumatoide a Fiebre Mediterránea Familiar

## Resumen en Una Frase

Anakinra es un antagonista recombinante del receptor de interleucina-1 (IL-1Ra), aprobado originalmente para el tratamiento de la artritis reumatoide y de enfermedades autoinflamatorias mediadas por IL-1.
El modelo TxGNN predice que también podría ser efectivo para la **Fiebre Mediterránea Familiar (FMF)**,
con **20 publicaciones** que actualmente respaldan esta dirección, aunque sin ensayos clínicos registrados en este paquete de evidencia.

*Nota: TxGNN generó 10 indicaciones candidatas para anakinra en este análisis; se selecciona la Fiebre Mediterránea Familiar como la más respaldada por evidencia real (nivel L3, frente a L4-L5 del resto).*

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis reumatoide (indicación global conocida; el paquete de evidencia no incluye datos de comercialización en España) |
| Nueva Indicación Predicha | Fiebre Mediterránea Familiar (autosómica recesiva) |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## Por qué es Razonable esta Predicción?

Actualmente el paquete de evidencia no incluye datos estructurados sobre el mecanismo de acción (MOA) de anakinra. Según la información farmacológica conocida, anakinra es un antagonista recombinante del receptor de interleucina-1 (IL-1Ra) que bloquea la unión de IL-1α e IL-1β a su receptor, interrumpiendo la cascada inflamatoria mediada por esta citocina.

La Fiebre Mediterránea Familiar es una enfermedad autoinflamatoria causada por mutaciones en el gen MEFV, que provocan una activación excesiva del inflamasoma de pirina y una liberación masiva de IL-1β. Al bloquear directamente el receptor de IL-1, anakinra actúa sobre la vía fisiopatológica central de la enfermedad, en lugar de tratar solo sus síntomas.

Esta relación mecanística ya cuenta con respaldo en la práctica clínica real: anakinra se utiliza fuera de indicación (off-label) en pacientes con FMF resistente o intolerante a colchicina, el tratamiento estándar de primera línea, lo que refuerza la plausibilidad biológica de la predicción del modelo TxGNN.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23322405](https://pubmed.ncbi.nlm.nih.gov/23322405/) | 2013 | Revisión | Clin Rev Allergy Immunol | Revisión del tratamiento biológico anti-IL-1β en FMF; posiciona anakinra en pacientes resistentes a colchicina |
| [21277619](https://pubmed.ncbi.nlm.nih.gov/21277619/) | 2011 | Serie de casos/Revisión | Semin Arthritis Rheum | Fármacos dirigidos a IL-1 (anakinra) eficaces en FMF, especialmente en resistencia a colchicina |
| [19033248](https://pubmed.ncbi.nlm.nih.gov/19033248/) | 2009 | Reporte de caso | Nephrol Dial Transplant | Tratamiento exitoso con anakinra en FMF, con buen desenlace tras trasplante renal |
| [23928237](https://pubmed.ncbi.nlm.nih.gov/23928237/) | 2013 | Reporte de caso | Joint Bone Spine | Miositis en paciente con FMF y espondiloartritis, tratada con éxito con anakinra |
| [21931121](https://pubmed.ncbi.nlm.nih.gov/21931121/) | 2012 | Serie de casos | Nephrol Dial Transplant | Efecto beneficioso marcado de inhibidor de IL-1 en FMF con amiloidosis e insuficiencia renal |
| [28585601](https://pubmed.ncbi.nlm.nih.gov/28585601/) | 2017 | Serie de casos | J Pak Med Assoc | Anakinra y canakinumab eficaces en 4 niños con FMF resistente a colchicina |
| [34550430](https://pubmed.ncbi.nlm.nih.gov/34550430/) | 2022 | Serie de casos | Rheumatol Int | Canakinumab eficaz en pacientes con FMF resistentes/intolerantes a colchicina y/o anakinra |
| [26572612](https://pubmed.ncbi.nlm.nih.gov/26572612/) | 2016 | Revisión | Curr Med Chem | Colchicina y agentes biológicos (incluyendo anti-IL-1) en el tratamiento de FMF |
| [23867542](https://pubmed.ncbi.nlm.nih.gov/23867542/) | 2014 | Revisión | Clin Pharmacol Ther | Nuevas terapias para FMF, de colchicina a agentes biológicos |
| [25945034](https://pubmed.ncbi.nlm.nih.gov/25945034/) | 2015 | Serie de casos | Drug Des Devel Ther | Canakinumab como terapia de rescate en FMF refractaria a tratamiento convencional |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La FMF tiene una base mecanística sólida (inflamasoma de pirina/IL-1β) y cuenta con 20 publicaciones, incluyendo múltiples series de casos y revisiones que documentan el uso real de anakinra en pacientes resistentes a colchicina. Sin embargo, la evidencia proviene de estudios observacionales y reportes de casos, no de ensayos clínicos aleatorizados, por lo que se recomienda avanzar con medidas de seguimiento adicionales.

**Para avanzar se necesita:**
- Datos de advertencias, contraindicaciones e interacciones farmacológicas (actualmente bloqueado — TFDA/AEMPS no ha sido consultado con éxito, gap DG001)
- Datos estructurados del mecanismo de acción (MOA) desde DrugBank (gap DG002)
- Confirmación del estatus regulatorio de anakinra para FMF en España, dado que actualmente no está comercializado
- Idealmente, datos de ensayos clínicos prospectivos o registros de vida real específicos para FMF resistente a colchicina
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


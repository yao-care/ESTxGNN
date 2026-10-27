---
layout: default
title: Imiquimod
parent: Solo predicción del modelo (L5)
nav_order: 411
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Imiquimod: nueva indicación predicha, Neoplasia premaligna (nivel de evidencia L5). Indicación original: Verruga común, infección anogenital por virus del papiloma humano…"
monitor_inn: "IMIQUIMOD"
predicted_indications: ["pre-malignant neoplasm", "benign neoplasm of buccal mucosa", "cervical neuroblastoma", "odontogenic cyst", "benign neoplasm of tongue", "nasopharyngeal teratoma", "cystic neoplasm", "inner ear neoplasm", "neoplasm of major salivary gland", "schwannoma of jugular foramen"]
---

# Imiquimod
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

## Imiquimod: De Verrugas Comunes y Queratosis Actínica a Neoplasia Premaligna
{: .text-alpha }

## Resumen en Una Frase

Imiquimod es un modificador de la respuesta inmune de aplicación tópica, utilizado originalmente para tratar verrugas anogenitales, queratosis actínica y carcinoma basocelular superficial.
El modelo TxGNN predice que podría ser efectivo para **neoplasia premaligna**,
con **2 ensayos clínicos** (Fase 3) y **9 publicaciones** que actualmente respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Verruga común, infección anogenital por virus del papiloma humano, carcinoma basocelular superficial multifocal y queratosis actínica (indicaciones del grafo de conocimiento; las autorizaciones españolas no incluyen texto de indicación) |
| Nueva Indicación Predicha | Neoplasia premaligna |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L1 según la clasificación del conjunto de datos (ver nota en la conclusión) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Imiquimod es un agonista del receptor Toll-like 7 (TLR7). Al activarlo, induce la liberación local de interferón alfa, TNF-alfa e IL-12 y favorece una respuesta inmune celular de tipo Th1. Los datos compilados no incluyen una descripción formal del mecanismo de acción del fármaco, pero este mecanismo está bien establecido en la literatura.

La indicación original (queratosis actínica, verrugas por VPH) y la nueva indicación (lesiones epiteliales premalignas) comparten una base: ambas son lesiones epiteliales displásicas o asociadas a VPH que pueden eliminarse mediante activación inmune local. La literatura recoge usos en neoplasia intraepitelial cervical, vulvar y anal, y en la papulosis bowenoide.

La predicción es, por tanto, una extensión natural de la indicación ya conocida hacia otras neoplasias intraepiteliales, y no un salto mecanístico.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Fase 3 | Terminado | 9 | Ensayo aleatorizado de imiquimod tópico en neoplasia intraepitelial cervical de alto grado. Directamente relevante, pero terminado con solo 9 participantes, por lo que no permite confirmar eficacia. |
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Fase 3 | Completado | 20 | Estudio abierto de imiquimod al 5% (3 días por semana) en queratosis actínica de cabeza. Apoyo complementario; sin grupo control y con muestra pequeña. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Intervenciones para la neoplasia intraepitelial del canal anal, condición premaligna asociada a VPH. |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Tratamientos médicos para la neoplasia intraepitelial vulvar de alto grado. |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Revisión | Int J Mol Sci | Tratamientos combinados con terapia fotodinámica en cáncer de piel no melanoma. |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Revisión | Semin Cutan Med Surg | Estrategias tópicas (incluido imiquimod) para cáncer de piel no melanoma y lesiones precursoras. |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Revisión | Skin Therapy Lett | Manejo actual de las queratosis actínicas, lesión premaligna cutánea. |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Reporte de caso | Int J STD AIDS | Tratamiento exitoso de neoplasia intraepitelial vulvar de alto grado con imiquimod al 5% en una receptora de trasplante renal. |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Reporte de caso | Int J STD AIDS | Aclaramiento de papulosis bowenoide del pene con imiquimod al 5%. |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclínico | Urol Oncol | Farmacocinética y farmacodinamia de agonistas TLR7 en un modelo de rata (uso intravesical). |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 88034 | IMIKERADERM 50 MG/G CREMA | Crema | No disponible en los datos compilados |
| 12783002 | ZYCLARA 3,75% CREMA | Crema | No disponible en los datos compilados |
| 98080001 | ALDARA 5% CREMA | Crema | No disponible en los datos compilados |
| 98080002 | ALDARA 5% CREMA | Crema | No disponible en los datos compilados |
| 78406 | IMUNOCARE 50 MG/G CREMA | Crema | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): trastornos asociados a fotosensibilidad (respuesta fotoparoxística, enfermedad por fotosensibilidad, quemadura solar), enfermedad autoinmune y enfermedad de injerto contra huésped.
- **Interacciones farmacológicas**: se identificaron 59 posibles interacciones, todas con nivel de gravedad no clasificado. Entre ellas figuran pantoprazol, morfina, omeprazol, prednisona, simvastatina, warfarina, clopidogrel, hidroxicloroquina e ibuprofeno.
- **Señales de la literatura**: hay reportes de eritema multiforme y de liquen planopilar asociados al uso de imiquimod. Un caso de conversión maligna de papilomatosis oral florida durante el tratamiento, junto con una revisión sobre la seguridad del uso fuera de indicación en lesiones orales, plantea cautela en mucosas.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo (activación de TLR7) es sólido y coherente con las indicaciones ya conocidas. Hay dos ensayos de Fase 3 y revisiones sistemáticas sobre neoplasias intraepiteliales. Sin embargo, los dos ensayos son pequeños, uno terminó prematuramente con 9 participantes y otro es abierto y sin control, por lo que no demuestran eficacia sólida. La clasificación L1 del conjunto de datos debe interpretarse con cautela: estrictamente, no hay dos ECAs de Fase 3 completados con resultados concluyentes.

**Para avanzar se necesita:**
- Ensayos controlados con muestra adecuada en neoplasias intraepiteliales específicas (cervical, vulvar, anal).
- Obtener las advertencias, contraindicaciones e indicaciones oficiales del prospecto de la AEMPS, que no están disponibles en los datos compilados.
- Datos formales del mecanismo de acción desde DrugBank.
- Evaluar la gravedad de las interacciones farmacológicas, hoy sin clasificar.
- Plan de vigilancia de seguridad, especialmente en mucosas, pacientes con enfermedad autoinmune, inmunosuprimidos y exposición solar.

**Nota sobre otras predicciones:** las demás indicaciones del modelo tienen evidencia más débil. La neoplasia benigna de mucosa bucal y el quiste odontogénico quedan como preguntas de investigación, y el resto (neuroblastoma cervical, teratoma nasofaríngeo, entre otras) se mantienen en espera (Hold) por falta de evidencia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


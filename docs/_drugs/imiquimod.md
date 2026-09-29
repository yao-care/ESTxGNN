---
layout: default
title: Imiquimod
parent: Solo predicción del modelo (L5)
nav_order: 276
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Imiquimod: De Indicación Original No Registrada a Neoplasia Premaligna

## Resumen en Una Frase

Imiquimod es un inmunomodulador de aplicación tópica, comercializado en España solo en forma de crema. Los datos de AEMPS recibidos no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **neoplasia premaligna**, con **19 ensayos clínicos** y **9 publicaciones** asociados. Solo una parte de ellos es directamente relevante: ensayos en neoplasia intraepitelial cervical (NIC), queratosis actínica y queilitis actínica.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de AEMPS están vacíos) |
| Nueva Indicación Predicha | Neoplasia premaligna |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L2 (el paquete de datos indica L1, pero no se cumple el criterio de ≥2 ECA de Fase 3 completados; ver nota abajo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Proceed with Guardrails |

> **Nota sobre el nivel de evidencia:** solo un ensayo de Fase 3 completado tiene un tamaño relevante (NCT01720407, n=259), y el tipo de lesión que estudia no puede confirmarse por el título truncado. El otro Fase 3 completado (NCT00175643) es de brazo único y abierto, no un ECA. El ensayo con mayor relevancia directa que cumple el criterio es el ECA de Fase 2 completado NCT03233412 (n=90). Por ello se asigna L2.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la farmacología conocida, imiquimod es un agonista del receptor tipo Toll 7 (TLR7). Induce interferón-alfa, TNF-alfa e IL-12 y activa la inmunidad innata y adaptativa local.

Este mecanismo es plausible para lesiones epiteliales premalignas, sobre todo las asociadas al virus del papiloma humano (VPH), como la neoplasia intraepitelial cervical (NIC), vulvar (VIN) y anal (AIN), y las lesiones tipo queratosis actínica. Una revisión preclínica sobre agonistas de TLR7 también los describe como tratamiento tópico de lesiones cutáneas (pre)malignas.

El apoyo procede de ensayos de Fase 2 y 3 y de revisiones Cochrane sobre neoplasia intraepitelial anogenital. Sin embargo, el ensayo de Fase 3 en NIC de alto grado se terminó con solo 9 pacientes, por lo que no permite extraer conclusiones de eficacia.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Fase 3 | Terminado | 9 | ECA de imiquimod tópico en NIC de alto grado. Terminado con solo 9 pacientes; sin poder estadístico para concluir eficacia |
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Fase 2 | Completado | 90 | ECA de imiquimod tópico en lesiones intraepiteliales cervicales de alto grado. Directamente relevante; el título truncado limita la especificidad |
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Fase 3 | Completado | 259 | Imiquimod neoadyuvante para reducir el tamaño de la escisión en lentigo maligno facial. Es el mayor conjunto de datos de Fase 3 |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Fase 2 | Completado | 5 | Estudio mecanístico sobre evasión inmune en lesiones por VPH (VIN 2/3 y verrugas anogenitales). Demasiado pequeño para mostrar eficacia |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Fase 3 | Desconocido | 145 | Curetaje más imiquimod frente a cirugía en carcinoma basocelular nodular. Es una neoplasia maligna, por lo que la evidencia es indirecta |
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Fase 3 | Completado | 20 | Estudio abierto de imiquimod 5% en queratosis actínicas de la cabeza (1 o 2 ciclos) |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Fase 4 | Desconocido | 20 | Imiquimod 3,75% tras crioterapia en queratosis actínicas hipertróficas de manos y antebrazos |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Fase 1 | Terminado | 49 | ECA de imiquimod 5%, 0,05% y nanoencapsulado en queilitis actínica |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Fase 1 temprana | Completado | 16 | Piloto de imiquimod neoadyuvante en carcinoma oral de células escamosas temprano. Coincide en el mecanismo, pero es cáncer establecido, no premalignidad |

Los otros 10 ensayos registrados usan imiquimod como adyuvante de vacunas (glioma, melanoma, próstata, pulmón) o combinado con otros agentes en tumores avanzados. No son relevantes para la indicación premaligna y no se listan.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Revisión (Cochrane) | Cochrane Database Syst Rev | Intervenciones para la neoplasia intraepitelial del canal anal, condición premaligna asociada a VPH |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Revisión (Cochrane) | Cochrane Database Syst Rev | Intervenciones médicas para la neoplasia intraepitelial vulvar de alto grado, sin consenso sobre el manejo óptimo |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Revisión | Skin Therapy Letter | Manejo actual de las queratosis actínicas, lesión premaligna cutánea; incluye terapias tópicas de campo |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Revisión | Semin Cutan Med Surg | Estrategias tópicas para cáncer de piel no melanoma y lesiones precursoras (fluorouracilo, diclofenaco, imiquimod, terapia fotodinámica) |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Revisión | Int J Mol Sci | Tratamientos combinados con terapia fotodinámica en cáncer de piel no melanoma |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclínico | Urol Oncol | Farmacocinética de dos agonistas de TLR7 en rata; los agonistas de TLR7 se usan en lesiones cutáneas (pre)malignas |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Reporte de caso | Int J STD AIDS | VIN de alto grado tratada con éxito con imiquimod 5% en una receptora de trasplante renal |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Reporte de caso | Int J STD AIDS | Papulosis bowenoide del pene con aclaramiento con imiquimod 5% |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 88034 | IMIKERADERM 50 MG/G CREMA | Crema | No disponible en los datos recibidos |
| 12783002 | ZYCLARA 3,75% CREMA | Crema | No disponible en los datos recibidos |
| 98080001 | ALDARA 5% CREMA | Crema | No disponible en los datos recibidos |
| 98080002 | ALDARA 5% CREMA | Crema | No disponible en los datos recibidos |
| 78406 | IMUNOCARE 50 MG/G CREMA | Crema | No disponible en los datos recibidos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un ECA de Fase 2 completado (n=90) en lesiones intraepiteliales cervicales de alto grado y un Fase 3 completado (n=259) en lentigo maligno. También hay ensayos en queratosis actínica y revisiones Cochrane en neoplasia intraepitelial anogenital. Pero el único ensayo de Fase 3 dirigido a NIC se terminó con 9 pacientes, y aún faltan los datos de seguridad de la ficha técnica de AEMPS. Por eso conviene avanzar solo con salvaguardas.

**Para avanzar se necesita:**
- Obtener y analizar las advertencias y contraindicaciones de las fichas técnicas de AEMPS, y confirmar las indicaciones aprobadas (bloqueante para el cribado de seguridad).
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar el tipo de lesión y el diseño de NCT01720407 y NCT03233412, que tienen títulos truncados.
- Definir la neoplasia premaligna concreta a evaluar (NIC, VIN, AIN, queratosis actínica u otra), porque el término de la predicción es demasiado amplio.
- Evaluar las señales de seguridad de la literatura: un caso de conversión maligna de papilomatosis oral durante el tratamiento, un caso de eritema multiforme y un caso de liquen planopilar.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


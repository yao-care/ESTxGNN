---
layout: default
title: Itraconazole
parent: Solo predicción del modelo (L5)
nav_order: 295
evidence_level: L5
indication_count: 1
---

# Itraconazole
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

# Itraconazol: De Infecciones Fúngicas a Neumocistosis

## Resumen en Una Frase

Itraconazol es un antifúngico azólico sistémico, usado por su clase farmacológica en infecciones fúngicas; los textos de indicación de las autorizaciones españolas no vienen en los datos recibidos.
El modelo TxGNN predice que podría ser efectivo para **neumocistosis**, pero sin ningún ensayo clínico registrado.
Hay **20 publicaciones** asociadas, casi todas revisiones o casos clínicos donde *Pneumocystis* aparece junto a otros patógenos, y ninguna prueba itraconazol para esta indicación.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en las autorizaciones de AEMPS recibidas (por su clase, antifúngico sistémico) |
| Nueva Indicación Predicha | Neumocistosis |
| Puntaje de Predicción TxGNN | 99.34% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 13 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados del mecanismo de acción en el Evidence Pack. Por conocimiento general, itraconazol inhibe la enzima fúngica CYP51 (lanosterol 14-alfa-desmetilasa) y bloquea la síntesis de ergosterol, un componente clave de la membrana de los hongos.

Aquí la razonabilidad es **débil**. La membrana de *Pneumocystis jirovecii* contiene muy poco ergosterol y sobre todo colesterol, así que los azoles no son un tratamiento ni una profilaxis reconocidos para la neumonía por *Pneumocystis*. El tratamiento estándar es trimetoprima-sulfametoxazol.

El puntaje alto de TxGNN es una predicción del grafo de conocimiento, no una confirmación clínica. Probablemente refleja co-ocurrencia en la literatura: itraconazol aparece en trabajos sobre profilaxis antifúngica e infecciones oportunistas, donde *Pneumocystis* se discute junto a *Histoplasma*, *Aspergillus* y otros patógenos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Los resúmenes disponibles no muestran itraconazol como tratamiento o profilaxis eficaz frente a *Pneumocystis*.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | ECA | HIV Medicine | Ensayo fase III doble ciego frente a placebo de itraconazol para prevenir infecciones fúngicas profundas en pacientes con VIH; el fragmento disponible no informa resultados y no evalúa neumocistosis como objetivo |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohorte | Transplantation Proceedings | Experiencia de un centro con infecciones fúngicas invasivas tras trasplante renal |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Revisión | Drugs | Terapia y profilaxis de infecciones por protozoos sistémicos, incluido *P. carinii* |
| [15250025](https://pubmed.ncbi.nlm.nih.gov/15250025/) | 2004 | Revisión | Clinical Infectious Diseases | Trimetoprima-sulfametoxazol es muy eficaz para prevenir la neumonía por *P. carinii* en neutropenia febril |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Revisión | BMJ Clinical Evidence | Profilaxis primaria y secundaria de infecciones oportunistas en VIH |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Revisión | Seminars in Respiratory Infections | Infecciones tras trasplante de pulmón y su prevención |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Revisión | Current Clinical Topics in Infectious Diseases | Profilaxis y tratamiento de infecciones en receptores de trasplante de médula ósea |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Revisión | Clinical Pharmacokinetics | Penetración de antifúngicos y otros antiinfecciosos en el líquido de revestimiento epitelial pulmonar |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Reporte de caso | Frontiers in Immunology | Coinfección por *Talaromyces marneffei* y *P. jirovecii* en un niño con mutación de STAT1 |
| [40949034](https://pubmed.ncbi.nlm.nih.gov/40949034/) | 2025 | Reporte de caso | Germs | Coinfección pulmonar por *P. jirovecii* e *Histoplasma capsulatum* en paciente VIH-negativo inmunodeprimido |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 71234 | ITRACONAZOL NORMON 100 mg CAPSULAS DURAS EFG | Cápsula dura | No disponible en los datos recibidos |
| 65762 | ITRACONAZOL ALTER 100 mg CAPSULAS DURAS EFG | Cápsula dura | No disponible en los datos recibidos |
| 78838 | ITRACONAZOL TECNIGEN 100 MG CAPSULAS DURAS EFG | Cápsula dura | No disponible en los datos recibidos |
| 59591 | HONGOSERIL 100 mg CAPSULAS | Cápsula dura | No disponible en los datos recibidos |
| 77459 | ITRAGERM 50 MG CAPSULAS DURAS | Cápsula dura | No disponible en los datos recibidos |

Existen además formas de concentrado para solución para perfusión entre las presentaciones registradas.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos para esta indicación, la literatura no respalda el uso de itraconazol frente a *Pneumocystis*, y la biología conocida (poco ergosterol en *Pneumocystis*) contradice la predicción. Existe una alternativa estándar establecida (trimetoprima-sulfametoxazol). El puntaje TxGNN por sí solo no basta para avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS (advertencias, contraindicaciones e indicaciones aprobadas) para completar el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Evidencia preclínica que muestre actividad de itraconazol frente a *P. jirovecii*; sin ella, no se justifica ir a clínica.
- Revisión manual de la literatura para confirmar que la señal se debe a co-ocurrencia y no a un efecto real.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


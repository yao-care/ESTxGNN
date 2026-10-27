---
layout: default
title: Mitomycin
parent: Solo predicción del modelo (L5)
nav_order: 535
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Mitomycin: nueva indicación predicha, Carcinoma pseudopapilar sólido del páncreas (nivel de evidencia L5). Indicación original: Adenocarcinoma pancreático (según el grafo de conocimiento"
monitor_inn: "mitomycin"
predicted_indications: ["solid pseudopapillary carcinoma of pancreas", "osteoclastic giant cell tumor of pancreas", "pancreatic carcinoma with mixed differentiation", "pancreatic intraductal papillary-mucinous carcinoma", "mixed ductal-endocrine carcinoma of pancreas", "pancreatic signet ring cell adenocarcinoma", "undifferentiated pancreatic carcinoma", "malignant exocrine pancreas neoplasm", "pancreatic intraductal papillary-mucinous neoplasm", "pancreatic acinar cell cystadenocarcinoma"]
---

# Mitomycin
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

## Mitomicina: De Adenocarcinoma Pancreático a Carcinoma Pseudopapilar Sólido del Páncreas
{: .text-alpha }

## Resumen en Una Frase

Mitomicina es un antibiótico antitumoral citotóxico, originalmente utilizado en el tratamiento del adenocarcinoma pancreático.
El modelo TxGNN predice que podría ser efectivo para el **carcinoma pseudopapilar sólido del páncreas**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Adenocarcinoma pancreático (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Carcinoma pseudopapilar sólido del páncreas |
| Puntaje de Predicción TxGNN | 99.86% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 11 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la mitomicina es un agente alquilante que forma enlaces cruzados en el ADN, con actividad citotóxica general. Su eficacia en el adenocarcinoma pancreático constituye la base de la predicción, y mecanísticamente podría ser aplicable a otros tumores pancreáticos.

Sin embargo, los tumores pseudopapilares sólidos son en su mayoría de bajo grado y se tratan principalmente con cirugía. Esto limita el valor de una extrapolación basada únicamente en la actividad citotóxica. No existen ensayos ni literatura que apoyen un beneficio de la quimioterapia en esta enfermedad.

Otras predicciones de alto puntaje (todas con puntajes entre 99.82% y 99.86%) son variantes tumorales pancreáticas: tumor de células gigantes osteoclásticas, carcinoma con diferenciación mixta, carcinoma ductal-endocrino mixto, adenocarcinoma de células en anillo de sello, carcinoma indiferenciado, neoplasia exocrina maligna, neoplasias mucinosas papilares intraductales y cistadenocarcinoma de células acinares. Todas comparten la misma lógica de extrapolación y ninguna cuenta con evidencia directa.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal. Para otras indicaciones predichas existe solo evidencia indirecta y no concluyente:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10897253](https://pubmed.ncbi.nlm.nih.gov/10897253/) | 2000 | Revisión | Strahlenther Onkol | Radioquimioterapia adyuvante y neoadyuvante en carcinoma pancreático ductal (indicación: neoplasia mucinosa papilar intraductal; evidencia indirecta) |
| [8361472](https://pubmed.ncbi.nlm.nih.gov/8361472/) | 1993 | Estudio clínico (indirecto) | Nihon Geka Gakkai Zasshi | Tamoxifeno añadido a inmunoquimioterapia (incluye mitomicina) tras resección de carcinoma pancreático; el foco es el tamoxifeno |
| [15983445](https://pubmed.ncbi.nlm.nih.gov/15983445/) | 2005 | Reporte de caso | Pancreatology | Pseudomixoma peritoneal con neoplasia mucinosa papilar intraductal, tratado con quimioperfusión intraperitoneal hipertérmica |
| [2695183](https://pubmed.ncbi.nlm.nih.gov/2695183/) | 1989 | Revisión | Bulletin du Cancer | Diagnóstico y tratamiento de tumores de origen desconocido; no específico de mitomicina ni de páncreas |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 81601 | Mitomicina Medac 20 mg | Polvo para solución intravesical e inyectable | No disponible |
| 80512 | Mitomicina Accord 2 mg | Polvo para solución intravesical e inyectable | No disponible |
| 82516 | Mitomicina Accord 40 mg | Polvo para solución inyectable y para perfusión | No disponible |
| 82767 | Mitomycin-C 40 mg (Inibsa) | Polvo y disolvente para suspensión intravesical | No disponible |
| 81599 | Mitomicina Medac 2 mg | Polvo para solución intravesical e inyectable | No disponible |

Se muestran 5 de las 11 autorizaciones vigentes (todas monofármaco, ninguna cancelada).

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antibiótico antitumoral / agente alquilante) |
| Riesgo de Mielosupresión | Alto. Las contraindicaciones del grafo de conocimiento incluyen leucopenia, trombocitopenia y anemia |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Ítems de Monitoreo | Hemograma completo (con plaquetas), función renal, función hepática y signos de síndrome hemolítico-urémico y de insuficiencia cardíaca |
| Protección en Manejo | Debe seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Condiciones asociadas a contraindicación o precaución (grafo de conocimiento, no texto del prospecto)**: enfermedad renal, piouréter, trombocitopenia, trastornos de la coagulación, anemia (incluida la macrocítica), leucopenia, síndrome hemolítico-urémico (incluido el típico), insuficiencia cardíaca congestiva y estomatitis.
- **Interacciones farmacológicas**: se identificaron 193 interacciones. Entre las destacadas:
  - **Mayor**: deferiprona, lexidronam de samario (153Sm).
  - **Moderada**: palifermina, cloruro de estroncio Sr-89, fostamatinib.
  - **Menor**: levofloxacino.
  - Otras interacciones de nivel no clasificado incluyen warfarina, dexametasona, prednisona, prednisolona, ondansetrón, metoclopramida, omeprazol y pantoprazol, entre otras.

Las advertencias y contraindicaciones del prospecto de la AEMPS no están disponibles en los datos compilados; consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura que apoyen el beneficio de la mitomicina en el carcinoma pseudopapilar sólido del páncreas, un tumor que suele ser de bajo grado y de tratamiento quirúrgico. Además, el perfil de mielosupresión es elevado, y falta información de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), actualmente un bloqueo para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisión de literatura específica sobre quimioterapia en tumores pseudopapilares sólidos y otras variantes pancreáticas raras.
- Evaluar si la indicación tiene necesidad clínica real, dado el tratamiento quirúrgico habitual.
- Evaluar la compatibilidad de vías de administración (pendiente).
- Considerar priorizar variantes con mayor solapamiento con el adenocarcinoma (p. ej., carcinoma de células en anillo de sello o neoplasia exocrina maligna) para una nueva evaluación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


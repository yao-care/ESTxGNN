---
layout: default
title: Dexchlorpheniramine
parent: Evidencia moderada (L3-L4)
nav_order: 239
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-14
description: "Dexchlorpheniramine: nueva indicación predicha, Urticaria alérgica (nivel de evidencia L4). Indicación original: Rinitis alérgica (según el grafo de conocimiento"
monitor_inn: "Dexchlorpheniramine"
predicted_indications: ["allergic urticaria", "cold urticaria"]
---

# Dexchlorpheniramine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **2** 
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

# Dexclorfeniramina: De Rinitis Alérgica a Urticaria Alérgica

## Resumen en Una Frase

La dexclorfeniramina es un antihistamínico H1 de primera generación, utilizado originalmente para el tratamiento de la rinitis alérgica y otros cuadros alérgicos (conjuntivitis, urticaria, angioedema).
El modelo TxGNN predice que podría ser efectiva para **urticaria alérgica**, aunque esta indicación se solapa en gran medida con usos ya conocidos del fármaco.
Actualmente hay **0 ensayos clínicos** y **3 publicaciones** relacionadas, por lo que la evidencia es limitada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Rinitis alérgica (según el grafo de conocimiento; el texto de indicación de las autorizaciones españolas no está disponible) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción detallado. Según el conocimiento general de la clase, la dexclorfeniramina es el enantiómero activo (dextro) de la clorfeniramina y actúa como antagonista de los receptores H1 de histamina. Esta descripción procede del conocimiento farmacológico de la clase y no de los datos suministrados.

La histamina liberada por los mastocitos provoca el habón y el eritema característicos de la urticaria alérgica, por lo que el bloqueo del receptor H1 es mecanísticamente plausible. Además, la urticaria ya figura entre las indicaciones originales del fármaco, de modo que este caso es más un uso ya existente o muy cercano que un reposicionamiento genuino.

Una segunda predicción, la **urticaria por frío** (puntaje 99.61%, nivel L5), comparte la misma lógica: es una urticaria física mediada por histamina en la que los antihistamínicos H1 son tratamiento de primera línea. Sin embargo, no hay ensayos ni literatura específicos del fármaco, y el valor incremental del reposicionamiento es bajo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39265704](https://pubmed.ncbi.nlm.nih.gov/39265704/) | 2024 | Ensayo de fase I aleatorizado (farmacodinámico) | Eur J Pharm Sci | Compara la inhibición del habón y eritema inducidos por histamina entre bilastina oral, dexclorfeniramina parenteral y una nueva formulación parenteral de bilastina. |
| [29723372](https://pubmed.ncbi.nlm.nih.gov/29723372/) | 2018 | Estudio farmacodinámico (prueba cutánea de histamina) | An Bras Dermatol | Compara la supresión de habón y eritema por los principales antihistamínicos H1 comercializados en Brasil. |
| [39803](https://pubmed.ncbi.nlm.nih.gov/39803/) | 1979 | Estudio clínico/inmunológico (caso o serie pequeña) | Dermatologica | Describe un caso de urticaria por contacto con calor adquirida, con estudio inmunológico; relación indirecta con el fármaco. |

Nota: el diseño de los dos primeros estudios se ha deducido solo del título y no está confirmado. Ninguno demuestra por sí mismo eficacia clínica de la dexclorfeniramina en urticaria alérgica.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 75389 | Dexclorfeniramina Maleato Accord 5 mg/ml solución inyectable EFG | Solución inyectable | No disponible |
| 40135 | Polaramine 5 mg/ml solución inyectable | Solución inyectable | No disponible |
| 31195 | Polaramine 2 mg comprimidos | Comprimido | No disponible |
| 32801 | Polaramine 0,4 mg/ml jarabe | Jarabe | No disponible |

## Consideraciones de Seguridad

- **Enfermedades señaladas como contraindicación o precaución en el grafo de conocimiento** (no proceden del texto del prospecto): hipertensión, insuficiencia hepática y enfermedad hepática, epilepsia, úlcera gástrica y péptica, enfermedad renal, pancreatitis, enfermedad de la vesícula biliar, hipotiroidismo y mixedema, enfermedad inflamatoria intestinal, diabetes mellitus y cetoacidosis diabética, hiperplasia prostática benigna, hipotensión, abuso o dependencia de sustancias, enfermedad coronaria e infarto de miocardio, hemoglobinopatías, colitis por *Clostridium difficile*, hipertensión ocular y arteriosclerosis, entre otras.
- **Interacciones farmacológicas**: no se encontraron datos de interacciones en la consulta realizada.

Consultar el prospecto para las advertencias y contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La urticaria ya es una indicación original del fármaco, por lo que el valor incremental del reposicionamiento es bajo. Además, no hay ensayos clínicos y la literatura disponible es indirecta (estudios farmacodinámicos de habón y eritema), lo que corresponde a un nivel de evidencia L4.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto oficial de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas), pues sin ellos no puede completarse el cribado de seguridad.
- Obtener datos oficiales del mecanismo de acción desde DrugBank.
- Confirmar si la urticaria alérgica y la urticaria por frío están ya cubiertas por la ficha técnica en España; de ser así, no se trataría de un reposicionamiento.
- Revisar el diseño y los resultados de los estudios farmacodinámicos identificados y buscar ensayos clínicos específicos en urticaria.
- Valorar el perfil de seguridad de un antihistamínico de primera generación (sedación, efectos anticolinérgicos) frente a alternativas de segunda generación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


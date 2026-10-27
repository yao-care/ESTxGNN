---
layout: default
title: Cefazolin
parent: Evidencia moderada (L3-L4)
nav_order: 154
evidence_level: L4
indication_count: 8
last_modified_at: 2026-10-14
description: "Cefazolin: nueva indicación predicha, Otitis media infecciosa (nivel de evidencia L4). Indicación original: Neumonía bacteriana (según las indicaciones del grafo de conocimiento"
monitor_inn: "Cefazolin"
predicted_indications: ["infectious otitis media", "bronchitis", "middle ear disease", "chronic otitis media", "suppurative otitis media", "otosalpingitis", "non-suppurative otitis media", "allergic otitis media"]
---

# Cefazolin
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **8** 
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

## Cefazolina: De Neumonía Bacteriana a Otitis Media Infecciosa
{: .text-alpha }

## Resumen en Una Frase

Cefazolina es una cefalosporina de primera generación, utilizada originalmente para infecciones bacterianas como la neumonía bacteriana (estreptocócica y estafilocócica), la colangitis, la endocarditis y la artritis bacteriana.
El modelo TxGNN predice que podría ser efectiva para **otitis media infecciosa**, pero actualmente **no hay ensayos clínicos** y solo **2 publicaciones** indirectas respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Neumonía bacteriana (según las indicaciones del grafo de conocimiento; los textos de indicación de las autorizaciones en España no están disponibles) |
| Nueva Indicación Predicha | Otitis media infecciosa |
| Puntaje de Predicción TxGNN | 99,44 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 13 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la cefazolina es una cefalosporina de primera generación que actúa inhibiendo la síntesis de la pared celular bacteriana, con actividad frente a bacterias grampositivas (Streptococcus y Staphylococcus aureus sensible a meticilina).

La indicación original (infecciones por estos gérmenes, como neumonía estreptocócica y estafilocócica) y la otitis media comparten parte de los patógenos. Esto da un vínculo biológicamente coherente con la predicción.

Sin embargo, hay limitaciones importantes: la cobertura frente a *H. influenzae* y *M. catarrhalis*, patógenos clave en otitis media, es limitada, y la cefazolina parenteral no es una opción de primera línea en esta enfermedad. La literatura directamente relevante es escasa y de calidad limitada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Reporte de caso/serie | Ann Otol Rhinol Laryngol | Terapia empírica con ceftazidima-cefazolina en síndrome de Gradenigo pediátrico, complicación de la otitis media aguda |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Revisión | Clin Pharm | Manejo del síndrome de Stevens-Johnson; la otitis media aparece solo como antecedente del caso. No es relevante para esta indicación |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 67021 | Cefazolina Sala 2 g polvo para solución inyectable EFG | Polvo para solución inyectable | No disponible |
| 67024 | Cefazolina Sala 1 g polvo y disolvente para solución inyectable EFG | Polvo y disolvente para solución inyectable | No disponible |
| 64848 | Cefazolina Normon 1 g polvo y disolvente para solución inyectable intramuscular EFG | Polvo y disolvente para solución inyectable | No disponible |
| 64850 | Cefazolina Normon 2 g polvo para solución inyectable intravenosa EFG | Polvo para suspensión inyectable | No disponible |
| 86542 | Cefazolina LDP Laboratorios Torlan 2 g polvo para solución inyectable y para perfusión EFG | Polvo para solución inyectable y para perfusión | No disponible |

Se muestran 5 de las 13 autorizaciones vigentes (todas monofármaco).

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto)**: trastornos de la coagulación sanguínea, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal y deficiencia congénita de protrombina.
- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Las de nivel moderado incluyen los aminoglucósidos **kanamicina, neomicina y estreptomicina**, y el **ácido picosulfúrico**. Otras interacciones listadas (calcitriol, epinefrina, anfotericina B, manitol, ácido acetilsalicílico, amoxicilina, entre otras) tienen nivel de gravedad desconocido.

Para advertencias y contraindicaciones según la ficha técnica, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (99,44 %), pero el nivel de evidencia es L4: no hay ensayos clínicos y la literatura es escasa e indirecta. Además, la cobertura limitada de patógenos típicos de la otitis media y la existencia de tratamientos de primera línea establecidos (p. ej., amoxicilina) no justifican avanzar sin nuevos datos.

**Para avanzar se necesita:**
- Datos de advertencias y contraindicaciones de la ficha técnica de la AEMPS (actualmente un vacío bloqueante para el cribado de seguridad).
- Datos detallados del mecanismo de acción.
- Estudios clínicos directos de cefazolina en otitis media humana, con comparación frente a tratamientos estándar.
- Evaluación de la compatibilidad de vías de administración (la cefazolina es solo parenteral).
- Como alternativa, valorar la **otitis media supurativa** (rank 5, nivel L3), que tiene un estudio comparativo clínico de 1982 (cefmetazol frente a cefazolina, 172 pacientes evaluables) y es la indicación mejor respaldada de este conjunto, aunque con evidencia antigua y limitada.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


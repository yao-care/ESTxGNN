---
layout: default
title: Miconazole
parent: Evidencia moderada (L3-L4)
nav_order: 524
evidence_level: L3
indication_count: 1
last_modified_at: 2026-10-14
description: "Miconazole: nueva indicación predicha, Acné (nivel de evidencia L3). Indicación original: Infecciones cutáneas fúngicas: tiña del pie, tiña corporal…"
monitor_inn: "Miconazole"
predicted_indications: ["acne (disease)"]
---

# Miconazole
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **1** 
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

# Miconazol: De Dermatofitosis y Candidiasis Cutánea a Acné

## Resumen en Una Frase

Miconazol es un antifúngico imidazólico, utilizado originalmente para tratar infecciones cutáneas por hongos (tiña del pie, tiña corporal, candidiasis cutánea, pitiriasis versicolor y candidiasis vulvovaginal).
El modelo TxGNN predice que podría ser efectivo para **acné**,
con **0 ensayos clínicos** y **4 publicaciones** (una revisión, dos estudios clínicos y un estudio in vitro) que actualmente respaldan esta dirección de forma preliminar.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones cutáneas fúngicas: tiña del pie, tiña corporal, candidiasis cutánea, pitiriasis versicolor, candidiasis vulvovaginal (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Acné |
| Puntaje de Predicción TxGNN | 99,54 % |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, miconazol es un antifúngico imidazólico que inhibe la lanosterol 14-alfa-desmetilasa fúngica (CYP51) y, con ello, la síntesis de ergosterol. Su eficacia en infecciones cutáneas fúngicas está bien establecida, y mecanísticamente podría ser aplicable al acné. Esta explicación se infiere del conocimiento general de la clase farmacológica.

La relación con el acné tiene dos vías plausibles. Primero, existe actividad *in vitro* de los azoles frente a *Cutibacterium* (*Propionibacterium*) *acnes*, la bacteria implicada en el acné vulgar. Segundo, miconazol actúa contra *Malassezia* (*Pityrosporum*), causante de la foliculitis por *Malassezia*, una afección parecida al acné que con frecuencia se diagnostica erróneamente como acné vulgar. Además, se han descrito efectos antiinflamatorios y antibacterianos de miconazol en la piel, que podrían ser relevantes para las lesiones inflamatorias del acné.

Conviene interpretar con cautela el puntaje del modelo (0,995): es una predicción computacional y no constituye evidencia clínica. Parte del beneficio observado podría deberse al tratamiento de foliculitis por *Malassezia* confundida con acné, y no a un efecto sobre el acné propiamente dicho.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Revisión | Expert Opinion on Pharmacotherapy | Revisión sobre los efectos múltiples de miconazol en trastornos cutáneos; lo describe como un antifúngico imidazólico clásico |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Estudio clínico (split-face) | Skin Research and Technology | Evaluación clínica y bioinstrumental en acné catamenial inflamatorio leve |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Estudio clínico | Clinical and Experimental Dermatology | Diagnóstico y ensayos terapéuticos en 62 pacientes con foliculitis por *Pityrosporum*, a menudo confundida con acné vulgar |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | Estudio in vitro | Biological & Pharmaceutical Bulletin | Actividad *in vitro* de antifúngicos azólicos frente a *P. acnes* aislado de pacientes con acné vulgar |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 50271 | DAKTARIN 20 MG/G CREMA | Crema | No disponible en los datos compilados |
| 52875 | FUNGISDIN 8,7 MG/ML SOLUCIÓN PARA PULVERIZACIÓN CUTÁNEA | Solución para pulverización cutánea | No disponible en los datos compilados |
| 55962 | DAKTARIN 20 MG/G GEL ORAL | Gel oral | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): enfermedad hepática y enfermedad de la vesícula biliar.
- **Interacciones farmacológicas / farmacología**: según los datos de farmacología, miconazol se une a los canales TRPM2 y TRPV5 y a la enzima CYP8B1, inhibiendo esta última. Se trata de interacciones con dianas, no de interacciones clínicas con otros fármacos, y no tienen nivel de gravedad asignado.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita a una revisión, dos estudios clínicos pequeños y antiguos (con posible confusión con foliculitis por *Malassezia*) y un estudio *in vitro*, sin ensayos clínicos registrados. El puntaje del modelo es alto, pero por sí solo no justifica avanzar; además, faltan los datos de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), requisito previo al cribado de seguridad.
- Confirmar el mecanismo de acción en DrugBank.
- Revisar en detalle los estudios clínicos existentes para distinguir el efecto en acné vulgar del efecto en foliculitis por *Malassezia*.
- Evaluar la compatibilidad de las vías de administración y formulaciones tópicas para acné (pendiente de análisis).
- Diseñar estudios clínicos controlados que respalden la indicación en acné.
- Valorar el riesgo en pacientes con enfermedad hepática o de la vesícula biliar.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


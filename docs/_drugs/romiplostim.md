---
layout: default
title: Romiplostim
parent: Solo predicción del modelo (L5)
nav_order: 711
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Romiplostim: nueva indicación predicha, Trastorno primario de liberación plaquetaria (nivel de evidencia L5). Indicación original: Anemia aplásica idiopática…"
---

# Romiplostim
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

# Romiplostim: De Anemia Aplásica y Trombocitopenia Autoinmune a Trastorno Primario de Liberación Plaquetaria

## Resumen en Una Frase

Romiplostim es un agonista del receptor de trombopoyetina (TPO), utilizado originalmente para aumentar el recuento de plaquetas en la trombocitopenia inmune (púrpura trombocitopénica idiopática) y relacionado con indicaciones como la anemia aplásica.
El modelo TxGNN predice que podría ser efectivo para **trastorno primario de liberación plaquetaria**, pero **no hay ensayos clínicos** y solo **1 publicación** de tipo preclínico/mecanístico, indirecta, que respalde esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Anemia aplásica idiopática, anemia aplásica y trombocitopenia autoinmune (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria |
| Puntaje de Predicción TxGNN | 99,99 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Romiplostim es un péptido agonista del receptor de trombopoyetina (c-Mpl) que estimula la megacariopoyesis y aumenta la producción de plaquetas. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción, pero su perfil farmacológico como agonista del receptor TPO está bien establecido.

Los trastornos de liberación plaquetaria son defectos **funcionales** (por ejemplo, alteración en la secreción de gránulos), normalmente con recuento plaquetario normal. Aumentar el número de plaquetas no corregiría el defecto de base, por lo que el vínculo mecanístico es débil. La única publicación disponible (PMID 25682608) trata de autoanticuerpos antiplaquetarios que inhiben la formación de proplaquetas en la trombocitopenia inmune, lo que es un nexo indirecto con la producción, no con la disfunción de liberación.

El puntaje alto del modelo probablemente refleja la cercanía en la red del conocimiento con nodos de trombocitopenia, más que una relación terapéutica real. Debe interpretarse con cautela.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Preclínico/mecanístico | Haematologica | Los autoanticuerpos antiplaquetarios de pacientes con trombocitopenia inmune inhiben la formación de proplaquetas por los megacariocitos y reducen la producción de plaquetas in vitro. Vínculo indirecto con la indicación predicha. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 08497001 | NPLATE 250 microgramos polvo para solución inyectable | Polvo para solución inyectable | No disponible |
| 08497005 | NPLATE 250 microgramos polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | No disponible |
| 08497007 | NPLATE 500 microgramos polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | No disponible |
| 08497002 | NPLATE 500 microgramos polvo para solución inyectable | Polvo para solución inyectable | No disponible |

Titular de las autorizaciones: Amgen Europe B.V.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 2 registros.
  - **Carfilzomib**: interacción de nivel **Mayor** (fuente: DDInter).
  - **Receptor de trombopoyetina (MPL)**: corresponde a la diana farmacológica del romiplostim (agonista), no a una interacción clínica entre fármacos.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo y en una publicación preclínica indirecta (nivel L5). Además, el mecanismo del fármaco (aumentar el número de plaquetas) no corrige un defecto funcional de liberación plaquetaria.

**Para avanzar se necesita:**
- Datos de eficacia que demuestren un beneficio en trastornos funcionales plaquetarios, o la reorientación hacia trombocitopenias constitucionales o macrotrombocitopenias, donde el mecanismo es más plausible.
- Datos detallados del mecanismo de acción.
- Revisión de las advertencias y contraindicaciones del prospecto de la AEMPS.
- Evaluación de la interacción mayor con carfilzomib.
- Los textos de indicación aprobada de las autorizaciones españolas.

**Nota adicional:** entre las otras predicciones, la trombocitopenia aloinmune fetal y neonatal (puntaje 99,99 %, nivel L4) cuenta con literatura indirecta sobre trombocitopenia inmune, pero ninguna sobre esa enfermedad en concreto. Merece considerarse como pregunta de investigación, con dudas abiertas sobre el paso placentario y la seguridad fetal y neonatal.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


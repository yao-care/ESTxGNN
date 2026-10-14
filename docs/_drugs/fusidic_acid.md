---
layout: default
title: Fusidic Acid
parent: Evidencia moderada (L3-L4)
nav_order: 366
evidence_level: L4
indication_count: 10
---

# Fusidic Acid
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Ácido Fusídico: De Infecciones Bacterianas (Uso Tópico) a Queratitis por Exposición

## Resumen en Una Frase

El ácido fusídico es un antibiótico utilizado originalmente para infecciones bacterianas, principalmente cutáneas por bacterias Gram-positivas como *Staphylococcus aureus*, en forma de crema y gel oftálmico.
El modelo TxGNN predice que podría ser efectivo para **queratitis por exposición**, pero actualmente solo respalda esta dirección **1 publicación** (una serie de casos sin relación directa con el fármaco) y **ningún ensayo clínico**.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el texto de las autorizaciones; el grafo de conocimiento lista infecciones (urinarias, bronquitis, acné, foliculitis, entre otras) |
| Nueva Indicación Predicha | Queratitis por exposición |
| Puntaje de Predicción TxGNN | 99,95 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 13 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, el ácido fusídico inhibe la síntesis proteica bacteriana al bloquear el factor de elongación G (EF-G), con actividad marcada frente a bacterias Gram-positivas como *Staphylococcus aureus*. Su eficacia en infecciones cutáneas está bien establecida y existe una formulación oftálmica (Fucithalmic gel oftálmico) autorizada en España.

En la queratitis por exposición, la superficie corneal dañada y seca puede sufrir sobreinfección bacteriana, que en teoría podría ser objetivo de un antibiótico tópico. Esta es la única base mecanística para la predicción.

Sin embargo, el vínculo es indirecto. La única publicación recuperada es una serie de casos sobre infecciones oculares por *Tsukamurella*, que no evalúa la eficacia del ácido fusídico en la queratitis por exposición. El puntaje elevado del modelo no está respaldado por datos clínicos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31246677](https://pubmed.ncbi.nlm.nih.gov/31246677/) | 2019 | Serie de casos | Cornea | Describe las manifestaciones oftálmicas de infecciones por *Tsukamurella* (la mayor serie publicada), con énfasis en espectro clínico, factores de riesgo, tratamiento y evolución, incluido el primer caso de infección de implante ocular tras enucleación. No evalúa el ácido fusídico. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 84020 | Ácido Fusídico Redoxfarma 20 mg/g crema | Crema | No especificada |
| 57812 | Fucithalmic 10 mg/g gel oftálmico | Gel oftálmico | No especificada |
| 58016 | Fucidine 20 mg/g crema | Crema | No especificada |
| 74064 | Ácido Fusídico Isdin 20 mg/g crema | Crema | No especificada |
| 90887 | Cortifusin 20 mg/g + 1 mg/g crema | Crema | No especificada |

Se muestran 5 de las 13 autorizaciones vigentes (todas de medicamentos de un solo principio activo en el registro; varias son asociaciones con corticoide según su denominación).

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto del prospecto): insuficiencia hepática, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, queratitis por herpes simple, glaucoma (incluido el de ángulo abierto), hipertensión ocular, diabetes mellitus, cetoacidosis diabética, fibrilación auricular, miastenia gravis, colitis (incluida la asociada a *Clostridium difficile*), conjuntivitis, infecciones oculares, bloqueo auriculoventricular y síndrome de Wolff-Parkinson-White, entre otras. Varias de ellas podrían corresponder a los componentes corticoides de las asociaciones y no al ácido fusídico en sí, por lo que deben verificarse con el prospecto.
- **Interacciones farmacológicas**: no se encontraron registros de interacciones en los datos compilados.

Consultar el prospecto para la información oficial de advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero carece de ensayos clínicos y de literatura que evalúe el ácido fusídico en queratitis por exposición. El único estudio recuperado es una serie de casos indirecta, por lo que el respaldo equivale a un nivel L4 con vínculo mecanístico débil.

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados desde fuentes oficiales.
- Advertencias y contraindicaciones del prospecto de la AEMPS, necesarias para el cribado de seguridad (especialmente por las contraindicaciones oculares como queratitis herpética y glaucoma).
- Estudios que evalúen la eficacia y seguridad del ácido fusídico oftálmico en queratitis por exposición o sobreinfección corneal.
- Datos de resistencia local de *S. aureus* al ácido fusídico.
- Evaluación de compatibilidad de vías de administración (gel oftálmico existente frente a la necesidad de la nueva indicación).
- Otras predicciones de mayor plausibilidad biológica, como la otitis externa (nivel L4, mecanismo antibacteriano plausible aunque sin datos de eficacia), podrían priorizarse para investigación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


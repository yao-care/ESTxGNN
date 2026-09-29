---
layout: default
title: Pyridostigmine
parent: Evidencia moderada (L3-L4)
nav_order: 447
evidence_level: L3
indication_count: 7
---

# Pyridostigmine
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **7** 
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

# Piridostigmina: De Debilidad Muscular en Miastenia Gravis a Miastenia Gravis con Hiperplasia Tímica

## Resumen en Una Frase

La piridostigmina es un inhibidor reversible de la acetilcolinesterasa, usado clínicamente para tratar la debilidad muscular en la miastenia gravis. El modelo TxGNN predice que podría ser efectiva para **miastenia gravis con hiperplasia tímica**, un subtipo de la misma enfermedad. Esta dirección cuenta con **0 ensayos clínicos** y **3 publicaciones** (una cohorte, una revisión y un reporte de caso).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en las autorizaciones de AEMPS (el texto de indicación está vacío). Uso clínico según la base farmacológica: debilidad muscular en miastenia gravis |
| Nueva Indicación Predicha | Miastenia gravis con hiperplasia tímica |
| Puntaje de Predicción TxGNN | 99.76% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

La piridostigmina inhibe de forma reversible la acetilcolinesterasa (ACHE) y también la butirilcolinesterasa (BCHE). Al frenar la degradación de la acetilcolina, aumenta su disponibilidad en la unión neuromuscular. Eso compensa la pérdida de señalización funcional del receptor de acetilcolina (AChR) o de MuSK en la miastenia gravis. No hay datos de mecanismo de acción en DrugBank, así que este razonamiento se basa en la información farmacológica y en el análisis de la predicción.

La hiperplasia tímica es un subtipo reconocido de miastenia gravis, especialmente en pacientes jóvenes con anticuerpos anti-AChR. Por eso el mecanismo se aplica de forma directa. Conviene aclarar que esta predicción es una **variante de una indicación ya conocida** y no un reposicionamiento hacia una enfermedad distinta.

Ningún registro aportado evalúa la piridostigmina específicamente en este subtipo, y las publicaciones describen la enfermedad o su tratamiento en general.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25683765](https://pubmed.ncbi.nlm.nih.gov/25683765/) | 2015 | Cohorte | Journal of Neurology | Revisión retrospectiva de 39 pacientes con miastenia gravis de inicio tardío, sin timoma y con anticuerpos anti-AChR. Analiza el pronóstico a 2 años tras la timectomía |
| [34225443](https://pubmed.ncbi.nlm.nih.gov/34225443/) | 2021 | Revisión | Molecular Medicine Reports | Revisión de aspectos genómicos, fenotípicos y epigenéticos de la miastenia gravis, con énfasis en autoinmunidad y sus distintos tipos |
| [18053719](https://pubmed.ncbi.nlm.nih.gov/18053719/) | 2008 | Reporte de caso | Neuromuscular Disorders | Paciente con miastenia gravis MuSK-positiva e hiperplasia tímica, con síndrome de cabeza caída como rasgo clínico principal |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 84453 | ZEDEPTINE 12 MG/ML SOLUCION ORAL EFG (Desitin Arzneimittel GmbH) | Solución oral |
| 23524 | MESTINON 60 MG COMPRIMIDOS (Viatris Healthcare Limited) | Comprimido |

## Consideraciones de Seguridad

- **Dianas farmacológicas** (según la base farmacológica; no son interacciones clínicas con otros fármacos): acetilcolinesterasa (ACHE) y butirilcolinesterasa (BCHE).
- **Señal de la literatura a vigilar**: una revisión de 2024 (PMID 39590927) destaca un estudio de gran tamaño con efectos negativos de la piridostigmina en la miastenia gravis MuSK-positiva. Otro reporte (PMID 33470659) describe hiperexcitabilidad del nervio periférico asociada a inhibidores de la acetilcolinesterasa en este mismo subtipo. Se recomienda consultar el prospecto para el resto de la información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo es coherente y la indicación es un subtipo de la enfermedad para la que el fármaco ya se usa, pero la evidencia disponible es indirecta (cohorte, revisión y reporte de caso) y no hay ensayos registrados. Además, hay señales de posible perjuicio en el subtipo MuSK-positivo.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de AEMPS (advertencias y contraindicaciones), pues esta información falta actualmente.
- Obtener el mecanismo de acción desde DrugBank.
- Confirmar el estado de anticuerpos (AChR frente a MuSK) antes de cualquier uso, como salvaguarda principal.
- Buscar estudios que evalúen la piridostigmina específicamente en miastenia gravis con hiperplasia tímica.
- Las demás predicciones del modelo (miastenia neonatal, L4; miastenia de cinturas, L4) tienen evidencia más débil. Las categorías inespecíficas y las predicciones sin respaldo (hiperesplenismo, síndrome hemolítico urémico atípico) no justifican avanzar y deben quedar en espera.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


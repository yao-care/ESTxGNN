---
layout: default
title: Bedaquiline
parent: Evidencia moderada (L3-L4)
nav_order: 64
evidence_level: L4
indication_count: 10
---

# Bedaquiline
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

# Bedaquilina: De Tuberculosis Multirresistente a Tuberculosis Bovina

## Resumen en Una Frase

Bedaquilina (comercializada como Sirturo) es un antibiótico antituberculoso que actúa sobre la ATP sintasa de las micobacterias y se usa en la tuberculosis multirresistente (TB-MDR). Este uso no figura en el texto de indicación de las autorizaciones españolas, que está vacío.
El modelo TxGNN predice que podría ser efectiva para la **tuberculosis bovina**, pero hoy solo hay **0 ensayos clínicos** y **3 publicaciones** de laboratorio (in vitro) sobre *M. tuberculosis*, ninguna sobre *M. bovis*.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tuberculosis multirresistente (según el análisis de mecanismo; no consta en el texto de las autorizaciones) |
| Nueva Indicación Predicha | Tuberculosis bovina |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Bedaquilina es una diarilquinolina que mata a *Mycobacterium tuberculosis* inhibiendo de forma específica su ATP sintasa. La ficha no incluye datos detallados del mecanismo de acción, pero la literatura recuperada lo respalda. Un estudio bioquímico de 2009 mostró que la ATP sintasa mitocondrial humana es más de 20.000 veces menos sensible al fármaco que la micobacteriana (IC50 >200 µM frente a 10 nM).

*Mycobacterium bovis*, causante de la tuberculosis bovina, pertenece al complejo *M. tuberculosis*. Por eso es plausible que el mismo mecanismo funcione. Además, el modelo TxGNN asigna a esta indicación una puntuación muy alta.

La plausibilidad es solo teórica. Los tres artículos encontrados son estudios in vitro o bioquímicos sobre *M. tuberculosis* (metodología de la concentración mínima inhibitoria, selectividad de la ATP sintasa y efectos de arrastre del fármaco en cultivos). Ninguno evalúa *M. bovis*, la enfermedad bovina ni pacientes.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27210281](https://pubmed.ncbi.nlm.nih.gov/27210281/) | 2016 | Estudio in vitro | Médecine et Maladies Infectieuses | Analiza cómo las condiciones de cultivo modifican la concentración mínima inhibitoria (CMI) de bedaquilina frente a *M. tuberculosis* H37Rv. Sirve para estandarizar las pruebas de sensibilidad y evitar falsas resistencias. |
| [19075053](https://pubmed.ncbi.nlm.nih.gov/19075053/) | 2009 | Estudio in vitro/bioquímico | Antimicrobial Agents and Chemotherapy | La ATP sintasa mitocondrial humana es más de 20.000 veces menos sensible al fármaco que la micobacteriana. Sugiere una alta selectividad por la bacteria. |
| [18480227](https://pubmed.ncbi.nlm.nih.gov/18480227/) | 2008 | Estudio in vitro | Journal of Clinical Microbiology | Los medios enriquecidos con proteínas (albúmina) previenen el efecto de arrastre del fármaco al medir su eficacia antimicobacteriana. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 113901001 | SIRTURO 100 MG COMPRIMIDOS | Comprimido | Janssen-Cilag International N.V |
| 113901002 | SIRTURO 100 MG COMPRIMIDOS | Comprimido | Janssen-Cilag International N.V |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para la tuberculosis bovina solo existe evidencia preclínica (L4), sin ensayos clínicos ni estudios en *M. bovis*. La puntuación de TxGNN, aunque alta, no equivale a evidencia clínica.

**Para avanzar se necesita:**
- Estudios de sensibilidad in vitro (CMI) de bedaquilina frente a cepas de *M. bovis*, y luego modelos animales.
- Los textos de indicación y las advertencias del prospecto de la AEMPS, hoy ausentes, y los datos de mecanismo de acción de DrugBank.
- Definir si el interés está en la enfermedad humana por *M. bovis* o en el uso veterinario. Esta predicción no aclara ese punto.
- Revisar las otras predicciones de este fármaco, que tienen más respaldo clínico. La más avanzada es la tuberculosis "inactiva" (probablemente latente), con el ensayo de fase 2/3 BREACH-TB (NCT06568484) en curso. Hay que confirmar antes esa denominación de la enfermedad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


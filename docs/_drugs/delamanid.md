---
layout: default
title: Delamanid
parent: Evidencia moderada (L3-L4)
nav_order: 232
evidence_level: L4
indication_count: 7
---

# Delamanid
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **7** 
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

# Delamanid: De Tuberculosis Multirresistente a Tuberculosis Bovina

## Resumen en Una Frase

Delamanid es un fármaco antituberculoso utilizado originalmente para el tratamiento de la tuberculosis multirresistente (TB-MDR).
El modelo TxGNN predice que podría ser efectivo para **tuberculosis bovina**, aunque actualmente solo hay **1 publicación** indirecta (un estudio de genotipado y resistencia) y **ningún ensayo clínico** que respalde esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tuberculosis multirresistente (según el grafo de conocimiento; el texto de indicación autorizado en España no está disponible) |
| Nueva Indicación Predicha | Tuberculosis bovina |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en Español | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

> Nota: entre las demás predicciones, "tuberculosis inactiva" (latente) tiene mayor respaldo clínico (1 ensayo de Fase 2/3, nivel L2), aunque dicho ensayo estudia tuberculosis pulmonar activa y no infección latente. Se comenta en la conclusión.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada para este informe. Según el conocimiento general, delamanid es un profármaco nitroimidazólico activado por la enzima Ddn (Rv3547) de *Mycobacterium tuberculosis*, que inhibe la síntesis de ácidos micólicos de la pared celular. Su eficacia en la tuberculosis multirresistente está establecida.

*Mycobacterium bovis*, causante de la tuberculosis bovina y de la tuberculosis zoonótica humana, pertenece al complejo *M. tuberculosis*. Por ello, una actividad similar es biológicamente plausible. Sin embargo, la única publicación disponible es un estudio de secuenciación genómica sobre diversidad genética y resistencia de aislados de *M. bovis*; no evalúa el tratamiento con delamanid. La evidencia es, por tanto, solo indirecta.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para tuberculosis bovina.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39487429](https://pubmed.ncbi.nlm.nih.gov/39487429/) | 2024 | Cohorte | BMC Genomics | Secuenciación del genoma completo de aislados de *M. bovis* de tuberculosis zoonótica: diversidad genética, virulencia y resistencia a fármacos. No estudia delamanid. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 113875004 | DELTYBA 50 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para tuberculosis bovina se apoya solo en una puntuación alta del modelo y en un único estudio genómico indirecto, sin datos de tratamiento con delamanid. Además, el estudio indica que *M. bovis* es intrínsecamente resistente a pirazinamida, lo que hace más relevante contar con datos propios de sensibilidad a delamanid.

**Para avanzar se necesita:**
- Datos de sensibilidad *in vitro* de aislados de *M. bovis* a delamanid (CMI).
- Estudios preclínicos o series de casos de uso de delamanid en tuberculosis zoonótica.
- Confirmación del mecanismo de acción y de las advertencias y contraindicaciones a partir del prospecto de la AEMPS.
- Valorar priorizar otras predicciones del mismo grupo con mayor respaldo, como "tuberculosis inactiva" (ensayo CRUSH-TB, NCT05766267, Fase 2/3, 288 participantes, activo sin reclutamiento), una vez aclarada la ambigüedad entre tuberculosis latente y activa.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


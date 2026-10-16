---
layout: default
title: Sotalol
parent: Solo predicción del modelo (L5)
nav_order: 745
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Sotalol: nueva indicación predicha, Síndrome del seno enfermo 2, autosómico dominante (nivel de evidencia L5). Indicación original: Fibrilación auricular (la autorización española no incluye texto de…"
---

# Sotalol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Sotalol: De Fibrilación Auricular a Síndrome del Seno Enfermo 2 (Autosómico Dominante)

## Resumen en Una Frase

Sotalol es un antiarrítmico con efecto betabloqueante y bloqueante de canales de potasio (clase III), utilizado originalmente para la fibrilación auricular.
El modelo TxGNN predice que podría ser efectivo para el **síndrome del seno enfermo 2, autosómico dominante**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta predicción. El mecanismo conocido sugiere, además, que el vínculo podría ser contraindicante y no terapéutico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Fibrilación auricular (la autorización española no incluye texto de indicación; se toma de las indicaciones originales del modelo) |
| Nueva Indicación Predicha | Síndrome del seno enfermo 2, autosómico dominante |
| Puntaje de Predicción TxGNN | 99,76 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, sotalol combina el bloqueo betaadrenérgico con el bloqueo de canales de potasio (clase III), y su eficacia en la fibrilación auricular está establecida.

El síndrome del seno enfermo 2 se vincula con una canalopatía de HCN4 que afecta a la corriente marcapasos del nodo sinusal. El bloqueo betaadrenérgico y la prolongación de la repolarización tienden a deprimir la función del nodo sinusal y a agravar la bradicardia. Por ello, la relación es probablemente **contraindicante y no terapéutica**: en el grafo de conocimiento, el síndrome del seno enfermo figura precisamente entre las contraindicaciones de sotalol.

El puntaje alto del modelo es solo una predicción computacional, sin respaldo clínico ni bibliográfico, y debe interpretarse con cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 89413 | SOTALOL SANDOZ 80 MG COMPRIMIDOS EFG | Comprimido | No disponible en los datos compilados |
| 62001 | SOTAPOR 80 mg COMPRIMIDOS | Comprimido | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): síndrome de QT largo (incluido el familiar), torsades de pointes, asma (intrínseca y alérgica), enfermedad bronquial, deficiencia de potasio, diabetes mellitus, cetoacidosis diabética, trastornos hipotensivos, insuficiencia renal, bloqueo auriculoventricular, **síndrome del seno enfermo (incluido el familiar)** y anafilaxia.
- **Interacciones farmacológicas**: se identificaron 100 interacciones; entre las 20 primeras reportadas destacan las de nivel **mayor** con epinefrina, claritromicina, ácido picosulfúrico y polietilenglicol (3350 con electrolitos). Hay además numerosas interacciones moderadas (p. ej., famotidina, cimetidina, atropina, morfina, bupropión, canagliflozina, dapagliflozina, clorpropamida) y una menor (ácido acetilsalicílico).
- Para advertencias y contraindicaciones oficiales, consultar el prospecto de la AEMPS, ya que no se dispone de ellas en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos y literatura (nivel L5), y el mecanismo conocido de sotalol (bradicardia, depresión del nodo sinusal) sugiere un efecto perjudicial. El síndrome del seno enfermo figura además como contraindicación en el grafo de conocimiento.

**Para avanzar se necesita:**
- Revisar las advertencias y contraindicaciones del prospecto de la AEMPS, hoy no disponibles.
- Obtener datos del mecanismo de acción desde DrugBank.
- Evaluar si la asociación predicha refleja en realidad una contraindicación.
- Si se busca reposicionamiento, considerar candidatas con más respaldo. La indicación predicha de rango 4 (ictus) tiene un ensayo de Fase 3 (NCT00007605) y literatura, pero indirectos, vía control del ritmo en fibrilación auricular (nivel L4), y se consideraría solo como pregunta de investigación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


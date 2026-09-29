---
layout: default
title: Tenofovir Alafenamide
parent: Solo predicción del modelo (L5)
nav_order: 517
evidence_level: L5
indication_count: 3
---

# Tenofovir Alafenamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Tenofovir alafenamida: De Hepatitis B Crónica a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Tenofovir alafenamida (TAF) es un análogo nucleotídico comercializado en España como Vemlidy, utilizado originalmente para tratar la infección crónica por el virus de la hepatitis B.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hepatitis B crónica (según datos de farmacología; el texto de indicación de AEMPS no está disponible) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.89% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, TAF es un profármaco de tenofovir, un inhibidor nucleotídico de la transcriptasa inversa. Su eficacia en la hepatitis B crónica está comprobada, y por analogía podría ser aplicable a otros virus que dependen de una transcriptasa inversa.

El virus de la inmunodeficiencia felina (FIV) es un lentivirus que, como el VIH, depende de la transcriptasa inversa. De ahí surge la plausibilidad por analogía. Sin embargo, no hay datos sobre la sensibilidad del FIV a TAF.

Hay que interpretar el puntaje con cautela. Es idéntico al de la indicación "infección por virus de inmunodeficiencia simia" (0.9989), lo que sugiere que refleja la similitud entre nodos de virus de inmunodeficiencia en el grafo de conocimiento y no evidencia independiente. Además, es una indicación veterinaria, fuera del ámbito habitual de evaluación para uso humano.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1161154001 | VEMLIDY 25 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA (Gilead Sciences Ireland Unlimited Company) | Comprimido recubierto con película | No especificada en los datos disponibles |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

El único registro de interacciones corresponde a una relación farmacológica con el receptor TAS2R39 (un receptor del gusto). No es una interacción medicamentosa clínicamente relevante.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos ni publicaciones para esta indicación. Además, es una indicación veterinaria, y la puntuación probablemente refleja similitud en el grafo entre virus de inmunodeficiencia.

**Para avanzar se necesita:**
- Datos de sensibilidad in vitro del FIV a tenofovir/TAF y estudios en gatos.
- Definir si existe interés real en un uso veterinario, que requeriría un marco regulatorio distinto al de AEMPS para medicamentos humanos.
- Datos de mecanismo de acción (DrugBank) y advertencias/contraindicaciones del prospecto de AEMPS.

**Nota:** la segunda predicción, infección por virus de inmunodeficiencia simia, tiene 1 ensayo clínico (relevancia baja) y 10 publicaciones, casi todas estudios preclínicos en macacos (nivel L4, "Research Question"). Sin embargo, aporta poco valor de reposicionamiento, porque TAF ya está aprobado para el VIH-1 en humanos y esos estudios usan sobre todo el virus quimérico SHIV, no SIV puro.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


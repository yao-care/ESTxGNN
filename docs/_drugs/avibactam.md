---
layout: default
title: Avibactam
parent: Solo predicción del modelo (L5)
nav_order: 81
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Avibactam: nueva indicación predicha, Neumonía estreptocócica (nivel de evidencia L5). Indicación original: Pielonefritis (según las relaciones de indicación del grafo de conoci…"
---

# Avibactam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Avibactam: De Pielonefritis a Neumonía Estreptocócica

## Resumen en Una Frase

Avibactam es un inhibidor de beta-lactamasas (de tipo diazabiciclooctano) que se utiliza junto con ceftazidima y originalmente se empleó en el tratamiento de la pielonefritis.
El modelo TxGNN predice que podría ser efectivo para **neumonía estreptocócica**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Pielonefritis (según las relaciones de indicación del grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Neumonía estreptocócica |
| Puntaje de Predicción TxGNN | 99,70% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en las fuentes consultadas. Según la información conocida, avibactam es un inhibidor de beta-lactamasas no beta-lactámico que restaura la actividad de antibióticos beta-lactámicos asociados (por ejemplo, ceftazidima) frente a enzimas de las clases A y C de Ambler y algunas de la clase D.

Desde el punto de vista mecanístico, la predicción **es poco convincente**. La resistencia de *Streptococcus pneumoniae* a los beta-lactámicos se debe principalmente a alteraciones de las proteínas fijadoras de penicilina, y no a la producción de beta-lactamasas, por lo que no cabe esperar que un inhibidor de beta-lactamasas aporte beneficio adicional. Además, los tratamientos habituales (penicilinas, ceftriaxona) ya son eficaces.

El elevado puntaje (0,997) probablemente refleja una asociación a nivel de grafo con indicaciones antibacterianas y de neumonía, más que un mecanismo específico.

### Otras indicaciones predichas (para contexto)

| Posición | Indicación predicha | Puntaje TxGNN | Valoración |
|------|------|------|------|
| 2 | Susceptibilidad a gripe grave | 99,28% | Sin actividad antiviral; probable artefacto del grafo. |
| 3 | Tuberculosis ureteral | 99,11% | La más plausible mecanísticamente (inhibición in vitro de la beta-lactamasa BlaC de *M. tuberculosis*), pero solo preclínica. |
| 4 | Esquistosomiasis urinaria | 99,06% | Sin diana antiparasitaria; probablemente por el contexto urinario compartido. |
| 5 | Síndrome de hiperviscosidad policlonal | 99,01% | Sin vínculo plausible; probable artefacto. |
| 6 | Hiperamilasemia | 99,01% | Hallazgo de laboratorio, no una enfermedad tratable con este fármaco; probable artefacto. |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1161109001 | ZAVICEFTA 2 G/0,5 G polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |
| 1241808001 | EMBLAVEO 1,5 G/0,5 G polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (nivel L5), sin ensayos ni literatura, y el mecanismo conocido de avibactam (inhibición de beta-lactamasas) no explica un beneficio en la neumonía estreptocócica, cuya resistencia no depende de estas enzimas. Los tratamientos actuales ya son eficaces.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) desde DrugBank.
- Información de seguridad del prospecto de la AEMPS (advertencias y contraindicaciones), actualmente sin disponer.
- Textos de indicaciones aprobadas de las autorizaciones españolas.
- Una justificación mecanística y microbiológica específica (por ejemplo, datos de actividad *in vitro* frente a *S. pneumoniae*) antes de cualquier estudio clínico.
- Si se desea explorar una alternativa, priorizar la tuberculosis ureteral con validación *in vitro* y en modelos animales previa a cualquier consideración clínica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


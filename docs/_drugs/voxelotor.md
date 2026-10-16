---
layout: default
title: Voxelotor
parent: Solo predicción del modelo (L5)
nav_order: 859
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Voxelotor: nueva indicación predicha, Trombocitopenia hereditaria con plaquetas normales (nivel de evidencia L5). Indicación original: Anemia falciforme (según el grafo de conocimiento"
monitor_inn: "VOXELOTOR"
predicted_indications: ["hereditary thrombocytopenia with normal platelets", "marcothrombocytopenia with mitral valve insufficiency", "dense granule disease", "transient neonatal thrombocytopenia", "thrombocytopenia", "acquired monoclonal Ig light chain-associated Fanconi syndrome", "primary release disorder of platelets"]
---

# Voxelotor
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

# Voxelotor: De Anemia Falciforme a Trombocitopenia Hereditaria con Plaquetas Normales

## Resumen en Una Frase

Voxelotor es un fármaco originalmente utilizado para la anemia falciforme (con la persistencia hereditaria de hemoglobina fetal como segunda indicación asociada en el grafo de conocimiento).
El modelo TxGNN predice que podría ser efectivo para **trombocitopenia hereditaria con plaquetas normales**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Anemia falciforme (según el grafo de conocimiento; el texto de indicación autorizado en España no está disponible) |
| Nueva Indicación Predicha | Trombocitopenia hereditaria con plaquetas normales |
| Puntaje de Predicción TxGNN | 99.58% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, voxelotor se une a la hemoglobina y aumenta su afinidad por el oxígeno, lo que inhibe la polimerización de la hemoglobina S (HbS). Esta acción es la base de su uso en la anemia falciforme.

Sin embargo, **no se identifica un vínculo mecanístico plausible** con la nueva indicación. La trombocitopenia hereditaria con plaquetas normales se relaciona con la producción o función de las plaquetas (megacariopoyesis), un proceso sin relación conocida con la afinidad de la hemoglobina por el oxígeno ni con la polimerización de HbS.

El alto puntaje de TxGNN (0.996) refleja probablemente la proximidad en el grafo de conocimiento (vecinos hematológicos compartidos, como la enfermedad de células falciformes) y no una base biológica demostrada. Por ello, la predicción debe considerarse una hipótesis sin respaldo mecanístico, clínico ni bibliográfico.

### Otras indicaciones predichas (todas L5, sin evidencia)

| Rango | Indicación Predicha | Puntaje TxGNN | Comentario |
|---|---|---|---|
| 2 | Macrotrombocitopenia con insuficiencia mitral | 99.58% | Trastorno congénito raro sin relación mecanística con la acción de voxelotor |
| 3 | Enfermedad de los gránulos densos | 99.58% | Defecto de almacenamiento plaquetario; no abordado por el mecanismo de voxelotor |
| 4 | Trombocitopenia neonatal transitoria | 99.57% | Cuadro autolimitado; faltan datos de seguridad en neonatos |
| 5 | Trombocitopenia | 99.51% | Causas heterogéneas; no se identifica vía por la que voxelotor eleve las plaquetas |
| 6 | Síndrome de Fanconi adquirido asociado a cadenas ligeras monoclonales de Ig | 99.13% | Lesión del túbulo proximal sin vínculo con el mecanismo del fármaco |
| 7 | Trastorno primario de liberación plaquetaria | 99.00% | Defecto de secreción plaquetaria no relacionado con la acción de voxelotor |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1211622001 | OXBRYTA 500 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; en la muestra disponible destacan:
  - **Mayor gravedad**: dexametasona, claritromicina, eliglustat y naloxegol.
  - **Gravedad moderada**: hidrocortisona, prednisona, betametasona, budesonida, triamcinolona, aprepitant, saxagliptina, repaglinida, simvastatina, tinidazol, nitisinona y naldemedina, entre otros (incluidas formulaciones oftálmicas y nasales de corticoides).

  El patrón sugiere una interacción relevante con inductores o inhibidores enzimáticos (p. ej., corticoides y macrólidos), por lo que se requiere revisión detallada de la medicación concomitante.

Para advertencias y contraindicaciones, consultar el prospecto, ya que no se dispone de esa información en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el grafo de conocimiento (nivel L5), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico plausible entre la acción de voxelotor sobre la hemoglobina y la producción o función plaquetaria. Todas las demás indicaciones predichas presentan la misma situación.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), requisito previo para cualquier cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión bibliográfica sistemática y buscar estudios preclínicos que respalden algún vínculo con la megacariopoyesis o la función plaquetaria.
- Establecer una hipótesis biológica plausible antes de considerar estudios exploratorios.
- Evaluar la compatibilidad de vía de administración y la similitud con la indicación original (actualmente pendientes).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


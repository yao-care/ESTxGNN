---
layout: default
title: Efmoroctocog Alfa
parent: Solo predicción del modelo (L5)
nav_order: 278
evidence_level: L5
indication_count: 10
---

# Efmoroctocog Alfa
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

# Efmoroctocog alfa: De Hemofilia a Enfermedad de von Willebrand Pseudo (tipo plaquetario)

## Resumen en Una Frase

Efmoroctocog alfa es un factor VIII de coagulación recombinante fusionado a Fc, originalmente utilizado para el tratamiento de la hemofilia.
El modelo TxGNN predice que podría ser efectivo para **la enfermedad pseudo-von Willebrand**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hemofilia (según las indicaciones originales registradas en el grafo de conocimiento; los textos de indicación de las autorizaciones españolas están vacíos) |
| Nueva Indicación Predicha | Enfermedad pseudo-von Willebrand (pseudo-von Willebrand disease) |
| Puntaje de Predicción TxGNN | 99.997% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, efmoroctocog alfa es un factor VIII recombinante fusionado a Fc (rFVIIIFc) que repone la actividad deficiente de FVIII, y su utilidad en hemofilia está establecida.

La enfermedad pseudo-von Willebrand (von Willebrand de tipo plaquetario) está causada por una ganancia de función de la GPIbα plaquetaria, que aumenta la unión del factor von Willebrand (VWF) y favorece la eliminación de sus multímeros de alto peso molecular. El defecto es propio de la plaqueta y no una deficiencia de FVIII, por lo que el vínculo mecanístico directo es débil. Solo de forma especulativa podría haber una reducción secundaria de FVIII por bajos niveles de VWF.

En conjunto, el puntaje alto del modelo carece de respaldo clínico: probablemente refleja la proximidad en la red entre trastornos hemorrágicos y no una relación terapéutica demostrada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1151046001 | Elocta 250 UI polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | No especificada en los datos |
| 1151046002 | Elocta 500 UI polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | No especificada en los datos |
| 1151046003 | Elocta 750 UI polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | No especificada en los datos |
| 1151046004 | Elocta 1000 UI polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | No especificada en los datos |
| 1151046005 | Elocta 1500 UI polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | No especificada en los datos |

Hay 8 autorizaciones vigentes en total (también 2000, 3000 y 4000 UI), todas del titular Swedish Orphan Biovitrum AB (publ).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como aspecto teórico señalado en el análisis de otras indicaciones candidatas, añadir un factor procoagulante en condiciones protrombóticas (por ejemplo, la púrpura trombótica trombocitopénica) podría aumentar el riesgo trombótico; no es relevante directamente para la indicación principal, pero debe tenerse en cuenta.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos ni publicaciones, y el defecto de la enfermedad pseudo-von Willebrand es plaquetario, no una deficiencia de FVIII, por lo que el vínculo mecanístico es débil.

**Otras candidatas del modelo:**
- La mayoría de las 10 principales (trastornos plaquetarios como trombastenia de Glanzmann, síndrome de Scott, defecto del receptor de colágeno, trombocitopenia constitucional o aloinmune neonatal, y PTT) también quedan en *Hold* por falta de respaldo mecanístico.
- **Deficiencia adquirida de factores de la coagulación** (puntaje 99.95%) es la más coherente mecanísticamente, pero los autoanticuerpos inhibidores neutralizarían el FVIII infundido; merece una pregunta de investigación definida (subtipo y estado del inhibidor).
- **Hemofilia A con anomalía vascular** (99.78%, nivel L4) se solapa con la indicación ya aprobada; conviene aclarar si requiere una evaluación separada.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco (DrugBank).
- Advertencias y contraindicaciones del prospecto de la AEMPS (actualmente sin datos y bloqueantes para el cribado de seguridad).
- Textos de indicación aprobada de las autorizaciones españolas.
- Evidencia clínica o preclínica de que la reposición de FVIII beneficia a pacientes con enfermedad pseudo-von Willebrand.
- Definir una pregunta de investigación concreta para las candidatas de mayor coherencia mecanística.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


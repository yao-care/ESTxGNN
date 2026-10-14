---
layout: default
title: Avatrombopag
parent: Solo predicción del modelo (L5)
nav_order: 79
evidence_level: L5
indication_count: 10
---

# Avatrombopag
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

# Avatrombopag: De Trombocitopenia a Macrotrombocitopenia con Insuficiencia de la Válvula Mitral

## Resumen en Una Frase

Avatrombopag es un agonista del receptor de trombopoyetina, originalmente utilizado para el tratamiento de la trombocitopenia.
El modelo TxGNN predice que podría ser efectivo para **macrotrombocitopenia con insuficiencia de la válvula mitral**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción (solo predicción del modelo).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trombocitopenia (según el grafo de conocimiento; el texto de indicación de la autorización en España no está disponible) |
| Nueva Indicación Predicha | Macrotrombocitopenia con insuficiencia de la válvula mitral |
| Puntaje de Predicción TxGNN | 99,995% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen el mecanismo de acción detallado. Según la información conocida, avatrombopag es un agonista del receptor de trombopoyetina (TPO-R) que estimula la proliferación de megacariocitos y la producción de plaquetas, y su uso en trombocitopenia es la indicación original.

Mecanísticamente, el fármaco solo podría ser aplicable si la macrotrombocitopenia implica una producción plaquetaria deficiente que responda a la señalización de TPO-R. Sin embargo, es una enfermedad extremadamente rara, su base genética no está especificada, y la afectación valvular cardíaca no guarda relación con el mecanismo del fármaco.

El puntaje muy alto (~0,99995) probablemente refleja la cercanía en el grafo de conocimiento con la indicación aprobada de trombocitopenia, y no evidencia independiente. Cabe señalar que otras predicciones del modelo (p. ej., trombocitopenia hereditaria con plaquetas normales, trombocitopenia neonatal transitoria) tienen una lógica mecanística algo más plausible, mientras que las predicciones relacionadas con esclerosis lateral amiotrófica y trastornos neurológicos carecen de base biológica evidente.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191373 | DOPTELET 20 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |

## Consideraciones de Seguridad

**Interacciones Farmacológicas:** se identificaron 52 interacciones en total. Entre las de nivel **mayor** figuran:
- Fosfenitoína
- Carbamazepina
- Carfilzomib
- Dabrafenib
- Enzalutamida
- Fluconazol
- Imatinib

Entre las de nivel **moderado** figuran claritromicina, nitisinona, cobicistat, fosamprenavir, gemfibrozilo, fenofibrato, apalutamida, atazanavir, amprenavir, boceprevir, ceritinib, delavirdina e idelalisib, entre otras.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura, con una lógica mecanística débil y una enfermedad muy rara con afectación cardíaca no relacionada con el mecanismo del fármaco.

**Para avanzar se necesita:**
- Datos del mecanismo de acción detallado y de la base genética de la enfermedad objetivo
- Revisión de las advertencias y contraindicaciones del prospecto de AEMPS (pendiente de obtener)
- Búsqueda de literatura y ensayos clínicos sobre TPO-R agonistas en macrotrombocitopenias hereditarias
- Evaluar candidatos con mayor plausibilidad mecanística (p. ej., trombocitopenia hereditaria) antes de priorizar esta indicación
- Plan de manejo de las interacciones farmacológicas de nivel mayor
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


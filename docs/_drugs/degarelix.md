---
layout: default
title: Degarelix
parent: Solo predicción del modelo (L5)
nav_order: 231
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Degarelix: nueva indicación predicha, Hipertricosis (nivel de evidencia L5). Indicación original: No disponible en los datos de la licencia AEMPS (texto de indicación…"
monitor_inn: "DEGARELIX"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "syndrome with a Dandy-Walker malformation as major feature", "malformation syndrome with odontal and/or periodontal component", "isolated genetic hair shaft abnormality", "allergic urticaria", "cold urticaria", "familial male-limited precocious puberty", "centra precocious puberty 1", "familial isolated trichomegaly"]
---

# Degarelix
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

# Degarelix: De Cáncer de Próstata (indicación original no registrada en los datos) a Hipertricosis

## Resumen en Una Frase

Degarelix es un antagonista del receptor de GnRH comercializado en España como Firmagon, y los datos compilados para este informe no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de la licencia AEMPS (texto de indicación vacío) |
| Nueva Indicación Predicha | Hipertricosis |
| Puntaje de Predicción TxGNN | 99,99 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, degarelix es un antagonista del receptor de GnRH: bloquea la señal hipotalámica-hipofisaria, reduce la secreción de LH y FSH y, con ello, los andrógenos gonadales. Este tipo de fármaco se utiliza en patologías dependientes de andrógenos.

La relación con la hipertricosis es **débil**. A diferencia del hirsutismo, la hipertricosis generalmente no depende de los andrógenos. La supresión androgénica solo podría influir en el crecimiento del vello en subtipos sensibles a los andrógenos. La puntuación de 0,9999 proviene exclusivamente del grafo de conocimiento, sin ensayos ni literatura que la respalden.

Las demás predicciones del modelo tampoco muestran un vínculo farmacológico sólido. Las dos de mayor relevancia biológica, la pubertad precoz familiar limitada al varón y la pubertad precoz central, se consideran únicamente preguntas de investigación. En la primera el mecanismo va en contra del beneficio, porque la mutación activadora de LHCGR actúa por debajo del bloqueo de GnRH. En la segunda hay coherencia mecanística, pero no existen datos pediátricos y degarelix es una formulación depot desarrollada para adultos. En la urticaria alérgica, la asociación podría reflejar un efecto adverso y no un beneficio.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 08504002 | FIRMAGON 120 mg polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | No disponible |
| 08504001 | FIRMAGON 80 mg polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | No disponible |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia hormonal (antagonista de GnRH); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; según las contraindicaciones del grafo de conocimiento, considerar QT/electrolitos (potasio) y función hepática |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): síndrome de QT largo (incluido el familiar), torsades de pointes, enfermedad hepática, enfermedad de la vesícula biliar y deficiencia de potasio.
- **Interacciones farmacológicas** (100 registradas; se muestran las principales):
  - **Mayores**: cisaprida, dolasetrón (riesgo de prolongación del QT).
  - **Moderadas**: claritromicina, levofloxacino, ondansetrón, granisetrón, palonosetrón, famotidina, loperamida y diversos laxantes/purgantes (bisacodilo, ácido picosulfúrico, polietilenglicol, aceite de ricino, lactulosa, lactitol, glicerina, citrato e hidróxido de magnesio, aceite mineral).
  - **Menores**: metronidazol.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en la puntuación del modelo (nivel L5), sin ensayos ni literatura, y el vínculo mecanístico con la hipertricosis es débil. Además, faltan los datos de seguridad del prospecto, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicación aprobada).
- Obtener el mecanismo de acción detallado desde DrugBank.
- Revisión de la literatura sobre antagonistas de GnRH en trastornos del crecimiento del vello, para comprobar si existe un subtipo sensible a andrógenos.
- Si se desea explorar alguna línea, priorizar como preguntas de investigación la pubertad precoz central y la pubertad precoz familiar limitada al varón, con evaluación de seguridad (QT, electrolitos) y de formulación pediátrica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


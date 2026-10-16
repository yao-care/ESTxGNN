---
layout: default
title: Ceftazidime
parent: Solo predicción del modelo (L5)
nav_order: 157
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ceftazidime: nueva indicación predicha, Hiperamilasemia (nivel de evidencia L5). Indicación original: Infecciones bacterianas (los datos compilados no incluyen el texto de…"
monitor_inn: "Ceftazidime"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "urinary tract infection (disease)", "epiglottitis", "gonococcal urethritis", "Ureaplasma urethritis", "blood group incompatibility", "infectious otitis media", "Peptostreptococcus infectious disease"]
---

# Ceftazidime
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

# Ceftazidima: De Infecciones Bacterianas (estreptocócicas, neumonía, meningitis, entre otras) a Hiperamilasemia

## Resumen en Una Frase

Ceftazidima es un antibiótico cefalosporínico inyectable, utilizado originalmente para tratar infecciones bacterianas como neumonía, meningitis, peritonitis e infecciones por *Escherichia coli* y estafilococos.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción, que es puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones bacterianas (los datos compilados no incluyen el texto de indicación autorizado por la AEMPS; la indicación procede del grafo de conocimiento: infección estreptocócica, neumonía bacteriana, meningitis bacteriana, peritonitis, infección por *E. coli*, entre otras) |
| Nueva Indicación Predicha | Hiperamilasemia |
| Puntaje de Predicción TxGNN | 99.51% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, ceftazidima es una cefalosporina de tercera generación que inhibe la síntesis de la pared celular bacteriana al unirse a las proteínas de unión a penicilina, y su eficacia en infecciones por bacterias Gram-negativas, incluida *Pseudomonas aeruginosa*, está bien establecida.

**En este caso, la predicción no tiene un respaldo mecanístico plausible.** La hiperamilasemia es una alteración bioquímica (elevación de amilasa en sangre) y no una infección. No existe una vía por la cual la acción antibacteriana de ceftazidima pudiera tratarla. El alto puntaje de TxGNN refleja patrones del grafo de conocimiento, no una relación biológica o clínica demostrada. Además, la similitud entre la indicación original y la nueva no ha sido evaluada.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Hay 20 autorizaciones vigentes, todas de medicamentos con ceftazidima como único principio activo (ninguna combinación) y ninguna cancelada. Se muestran las 5 principales; los datos compilados no incluyen el texto de la indicación aprobada para ninguna de ellas.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 90753 | Alfagem 1 g polvo para solución inyectable y para perfusión | Polvo para solución inyectable y para perfusión | Medochemie Limited |
| 71574 | Ceftazidima Kabi 1 g polvo para solución inyectable EFG | Polvo para solución inyectable y para perfusión | Fresenius Kabi España, S.A.U. |
| 83904 | Ceftazidima Qilu 500 mg polvo para solución inyectable EFG | Polvo para solución inyectable | Qilu Pharma Spain S.L. |
| 72674 | Ceftazidima Kabi 2 g polvo para solución inyectable y para perfusión EFG | Polvo para solución inyectable y para perfusión | Fresenius Kabi España, S.A.U. |
| 90754 | Alfagem 2 g polvo para solución inyectable y para perfusión EFG | Polvo para solución inyectable y para perfusión | Medochemie Limited |

---

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación o precaución (según el grafo de conocimiento, no el prospecto):** enfermedad renal, piouréter, enfermedad hepática, enfermedad de la vesícula biliar, trastornos de la coagulación sanguínea, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal y deficiencia congénita de protrombina.
- **Interacciones farmacológicas:** se registraron 100 interacciones. Las de nivel moderado más relevantes son:
  - Anfotericina B (y sus formulaciones lipídicas, liposomal y de sulfato de colesterilo)
  - Aminoglucósidos: kanamicina, neomicina y estreptomicina
  - Ácido picosulfúrico

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hiperamilasemia se basa solo en el modelo (nivel L5), sin ensayos ni literatura, y carece de un mecanismo plausible entre un antibiótico betalactámico y una elevación de amilasa. No hay base para avanzar.

**Para avanzar se necesita:**
- Una hipótesis biológica que justifique la relación entre ceftazidima y la hiperamilasemia, que hoy no existe.
- Datos de mecanismo de acción (MOA) desde DrugBank.
- Texto de indicaciones, advertencias y contraindicaciones del prospecto de la AEMPS.
- Si se busca una línea de reposicionamiento más viable, reorientar el análisis a otras predicciones del mismo informe. La **infección urinaria** (L2, "Proceed with Guardrails") tiene ensayos controlados, aunque principalmente con ceftazidima-avibactam, y podría considerarse más un uso ya existente que un reposicionamiento. Si se evalúa, confirmar sensibilidad del patógeno, ajustar la dosis por función renal y seguir las guías de uso racional de antibióticos.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


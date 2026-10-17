---
layout: default
title: Dexpanthenol
parent: Solo predicción del modelo (L5)
nav_order: 242
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Dexpanthenol: nueva indicación predicha, Estenosis anorrectal (nivel de evidencia L5). Indicación original: No consta texto de indicación aprobada en las autorizaciones española…"
monitor_inn: "dexpanthenol"
predicted_indications: ["anorectal stricture", "imperforate anus", "anal polyp", "vulvar inverted follicular keratosis", "proctitis", "punctate epithelial keratoconjunctivitis"]
---

# Dexpanthenol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Dexpanthenol: De Íleo Paralítico y Enfermedades de la Piel a Estenosis Anorrectal

## Resumen en Una Frase

Dexpanthenol es un precursor de la vitamina B5 (ácido pantoténico), utilizado originalmente en trastornos de la motilidad gastrointestinal (como el íleo paralítico y la gastroparesia) y en enfermedades de la piel como dermatitis y eccema atópico.
El modelo TxGNN predice que podría ser efectivo para **estenosis anorrectal**, aunque actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción concreta.
La única señal de evidencia directa en las predicciones es un ensayo clínico de Fase 3 para otra indicación (exantema), de relevancia parcial.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta texto de indicación aprobada en las autorizaciones españolas. Según el grafo de conocimiento: íleo paralítico, obstrucción intestinal, gastroparesia, dermatitis, eccema atópico, entre otras |
| Nueva Indicación Predicha | Estenosis anorrectal |
| Puntaje de Predicción TxGNN | 99.72% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, dexpanthenol es un provitamina del ácido pantoténico, precursor de la coenzima A, y se considera que favorece la reparación epitelial y la cicatrización de heridas.

La relación con la indicación original es plausible pero no demostrada: dexpanthenol se ha asociado a trastornos de motilidad y obstrucción intestinal y a enfermedades cutáneas. Un posible efecto sobre la cicatrización de la mucosa podría ser relevante en estenosis anorrectal, pero se trata de una hipótesis. La similitud con las indicaciones originales aún está pendiente de evaluar.

Cabe señalar que la predicción puede reflejar simplemente proximidad en el grafo de conocimiento. No hay ensayos ni literatura que la sustenten, por lo que debe interpretarse como una hipótesis de investigación.

### Otras predicciones del modelo (para contexto)

| Rango | Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Recomendación |
|---|---|---|---|---|
| 2 | Ano imperforado | 99.71% | L5 | Hold |
| 3 | Pólipo anal | 99.62% | L5 | Hold |
| 4 | Queratosis folicular invertida vulvar | 99.60% | L5 | Hold |
| 5 | Proctitis | 99.60% | L5 | Hold |
| 6 | Exantema | 99.60% | L4 | Pregunta de investigación |
| 7 | Queratoconjuntivitis epitelial punteada | 99.34% | L5 | Hold |

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para estenosis anorrectal.

Como referencia, para otra indicación predicha (exantema, rango 6) se identificó el siguiente ensayo:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01136005](https://clinicaltrials.gov/study/NCT01136005) | Fase 3 | Completado | 160 | Ensayo aleatorizado y doble ciego de crema Bepanthen® frente a crema de cetomacrogol para prevenir la erupción papulopustulosa en pacientes tratados con inhibidores del EGFR. No se dispone de resultados; la relevancia para exantema es parcial |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 17466 | BEPANMED 500 mg/2 ml, solución inyectable | Solución inyectable | No consta |
| 86165 | SEPTANASAL 1 mg/ml + 50 mg/ml solución para pulverización nasal | Solución para pulverización nasal | No consta |
| 83634 | FRENASAL PLUS 1 mg/ml + 50 mg/ml solución para pulverización nasal | Solución para pulverización nasal | No consta |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): hemofilia.
- **Interacciones Farmacológicas**: no se encontraron interacciones registradas en la consulta realizada.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones oficiales).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para estenosis anorrectal se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura. El mecanismo propuesto (reparación epitelial) es plausible pero no está validado.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones oficiales) para completar el cribado de seguridad
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank)
- Realizar una revisión sistemática de la literatura sobre dexpanthenol en estenosis anorrectal y patología de la mucosa anorrectal
- Evaluar la compatibilidad de la vía de administración (la forma inyectable y la nasal disponibles pueden no ser adecuadas para uso anorrectal)
- Valorar, como alternativa de mayor evidencia, la indicación de exantema/dermatitis, apoyada en un ensayo de Fase 3, tras confirmar la condición y los resultados de ese ensayo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


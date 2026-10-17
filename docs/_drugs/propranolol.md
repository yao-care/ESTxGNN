---
layout: default
title: Propranolol
parent: Solo predicción del modelo (L5)
nav_order: 670
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Propranolol: nueva indicación predicha, Miopatía distal tipo Tateyama (nivel de evidencia L5). Indicación original: Hipertensión (según el grafo de conocimiento"
monitor_inn: "PROPRANOLOL"
predicted_indications: ["distal myopathy, Tateyama type", "congenital myopathy with excess of thin filaments", "chondroma", "cirrhotic cardiomyopathy"]
---

# Propranolol
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

# Propranolol: De Trastornos Hipertensivos y Cardiovasculares a Distrofia Miopática Distal Tipo Tateyama

## Resumen en Una Frase

Propranolol es un betabloqueante no selectivo, utilizado originalmente para la hipertensión, las arritmias (como la fibrilación auricular), la miocardiopatía hipertrófica y el hemangioma.
El modelo TxGNN predice que podría ser efectivo para la **miopatía distal tipo Tateyama**, pero se trata únicamente de una predicción del modelo: **no hay ensayos clínicos ni publicaciones** que la respalden.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Miopatía distal tipo Tateyama |
| Puntaje de Predicción TxGNN | 99.40% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 11 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, propranolol es un betabloqueante no selectivo cuya eficacia en enfermedades cardiovasculares (hipertensión, arritmias, miocardiopatía hipertrófica) y en tumores vasculares como el hemangioma está establecida.

Para la miopatía distal tipo Tateyama **no se identificó un vínculo mecanístico** a partir de los datos disponibles. No hay una justificación evidente para el bloqueo beta-adrenérgico en esta miopatía distal, y el alto puntaje (0.994) refleja solo una señal del modelo, sin respaldo clínico ni bibliográfico.

Conviene además tener en cuenta que el grafo de conocimiento registra la miopatía y otras enfermedades musculares entre las contraindicaciones de propranolol, lo que hace aún más necesaria la cautela ante esta predicción.

### Otras predicciones del modelo (contexto)

| Rango | Enfermedad | Puntaje TxGNN | Nivel de Evidencia | Recomendación |
|------|------|------|------|------|
| 2 | Miopatía congénita con exceso de filamentos finos | 99.30% | L5 | Hold |
| 3 | Miocardiopatía hipertrófica por entrenamiento atlético intenso | 99.17% | L5 | Hold |
| 4 | Condroma | 99.14% | L5 | Hold |
| 5 | Miocardiopatía cirrótica | 99.12% | L4 | Pregunta de investigación |
| 6 | Miocardiopatía | 99.12% | L3 | Pregunta de investigación |

Las predicciones 5 y 6 son las que cuentan con algo de literatura (cirrosis con intervalo QT prolongado y estudios hemodinámicos en miocardiopatía hipertrófica), aunque esta última se solapa con indicaciones ya existentes.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 89689 | Propranolol Tarbis 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 89692 | Propranolol Tarbis 40 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 84656 | Propranolol Aurovitas 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 84649 | Propranolol Aurovitas 40 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 114919001 | Hemangiol 3,75 mg/ml solución oral | Solución oral | No disponible |

Se muestran 5 de las 11 autorizaciones vigentes (todas de principio activo único). Las restantes corresponden a Propranolol Accord (10 y 40 mg), Propranolol Kern Pharma (10 y 40 mg) y Sumial (10 y 40 mg).

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): bronquitis, trastornos de ansiedad, enfermedad renal, pancreatitis, enfermedad hepática, enfermedad de la vesícula biliar, lupus eritematoso sistémico, miopatía y enfermedades musculares, parálisis periódica familiar, diabetes mellitus, cetoacidosis diabética, gota, hiperparatiroidismo, encefalopatía hepática, anuria, miastenia gravis, entre otras.
- **Interacciones farmacológicas** (100 registradas; se muestran las principales):
  - **Mayor:** epinefrina.
  - **Moderadas:** hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona, atropina, bupropión, morfina, cimetidina, canagliflozina, clorpropamida, lorcaserina.
  - **Menores:** ácido ascórbico, ácido acetilsalicílico, óxido de magnesio.
- **Consideración en cirrosis avanzada:** la literatura aportada para la miocardiopatía cirrótica sugiere que los betabloqueantes no selectivos pueden alterar la homeostasis circulatoria y renal en ascitis refractaria.

Para el resto de la información de seguridad, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para la miopatía distal tipo Tateyama se basa solo en el modelo (nivel L5), sin ensayos, sin literatura y sin un mecanismo plausible. Además, las enfermedades musculares figuran entre las contraindicaciones registradas del fármaco.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de propranolol y una hipótesis mecanística concreta para esta miopatía.
- Revisión sistemática de la literatura y de registros de ensayos específicos de la enfermedad.
- Obtención de las advertencias y contraindicaciones del prospecto de AEMPS (actualmente no disponibles) antes de cualquier evaluación de seguridad.
- Evaluación preclínica (modelos celulares o animales) que justifique la hipótesis.
- Como alternativa de mayor viabilidad, priorizar las preguntas de investigación sobre miocardiopatía cirrótica, que cuenta con algo de literatura, sin olvidar sus señales de seguridad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


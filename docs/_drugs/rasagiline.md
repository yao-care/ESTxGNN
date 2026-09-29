---
layout: default
title: Rasagiline
parent: Solo predicción del modelo (L5)
nav_order: 458
evidence_level: L5
indication_count: 6
---

# Rasagiline
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

# Rasagilina: De Enfermedad de Parkinson a Neurodegeneración Asociada a PLA2G6

## Resumen en Una Frase

Rasagilina es un inhibidor de la MAO-B comercializado en España, utilizado originalmente para tratar la enfermedad de Parkinson (como monoterapia inicial y como adyuvante de levodopa).
El modelo TxGNN predice que podría ser efectivo para **Neurodegeneración Asociada a PLA2G6**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Parkinson (según los datos farmacológicos; el texto de indicación de las autorizaciones de AEMPS no está disponible) |
| Nueva Indicación Predicha | Neurodegeneración asociada a PLA2G6 |
| Puntaje de Predicción TxGNN | 99.71% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Rasagilina es un inhibidor de la monoaminooxidasa B (MAO-B). Al bloquear esta enzima aumenta la disponibilidad de dopamina en el cuerpo estriado. Además, se le atribuyen efectos neuroprotectores, aunque este punto es hipotético. No se dispone de una descripción detallada del mecanismo de acción en el registro de DrugBank; solo consta la interacción farmacológica con MAO-B.

La neurodegeneración asociada a PLA2G6 puede presentarse con distonía-parkinsonismo. Por eso es concebible un beneficio sintomático dopaminérgico, similar al observado en la enfermedad de Parkinson.

Sin embargo, el defecto de fondo de esta enfermedad afecta al metabolismo lipídico y a la homeostasis de membranas, con acumulación de hierro y patología de alfa-sinucleína. Rasagilina no tiene un vínculo conocido con modificación de la enfermedad en ese nivel. La plausibilidad se limita, por tanto, a un posible alivio de síntomas y no a un efecto sobre la causa. No se aportaron ensayos ni literatura que lo respalden.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones. El texto de indicación aprobada no está disponible en los datos recibidos, por lo que se omite esa columna.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 81248 | Devolina 1 mg comprimidos EFG | Comprimido | Devon Farmacéutica S.A. |
| 80582 | Rasagilina Bluefish 1 mg comprimidos EFG | Comprimido | Bluefish Pharmaceuticals AB (Publ) |
| 04304004IP3 | Azilect 1 mg comprimidos | Comprimido | Teva B.V. |
| 81260 | Rasagilina Aristo 1 mg comprimidos EFG | Comprimido | Aristo Pharma GmbH |
| 80627 | Rasagilina Tecnigen 1 mg comprimidos EFG | Comprimido | Tecnimede España Industria Farmacéutica S.A. |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó con 1 registro, de tipo farmacológico y no una interacción con otro medicamento. Rasagilina actúa sobre su diana, la **monoaminooxidasa B (MAOB)**, en humanos. No se registraron interacciones con otros fármacos.

Consultar el prospecto para informacion de seguridad (advertencias y contraindicaciones).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje TxGNN alto (99.71%), pero no cuenta con ningún ensayo clínico ni publicación, y el mecanismo de la enfermedad (metabolismo lipídico y de membranas) no se relaciona con la inhibición de MAO-B. Solo un efecto sintomático dopaminérgico sería concebible.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de AEMPS (advertencias y contraindicaciones), lo cual es un requisito bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda sistemática de literatura y de registros de ensayos (ClinicalTrials.gov, ICTRP) sobre rasagilina en neurodegeneración asociada a PLA2G6 y en distonía-parkinsonismo.
- Confirmar la indicación original en las autorizaciones de AEMPS, ya que el campo está vacío.
- Como nota adicional: entre las otras predicciones de este fármaco, el parkinsonismo juvenil de Hunt (puntaje 99.25%) tiene el vínculo mecanístico más sólido y se clasifica como pregunta de investigación. Sería una vía más prometedora que esta indicación.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


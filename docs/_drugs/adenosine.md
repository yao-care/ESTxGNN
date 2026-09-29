---
layout: default
title: Adenosine
parent: Solo predicción del modelo (L5)
nav_order: 20
evidence_level: L5
indication_count: 2
---

# Adenosine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Adenosina: De Taquicardias a Bloqueo de Rama del Haz (término obsoleto)

## Resumen en Una Frase

La adenosina es un nucleósido endógeno que se usa en el tratamiento de las taquicardias. El modelo TxGNN predice que podría ser efectiva para **"obsolete bundle branch block" (bloqueo de rama del haz, término obsoleto)**, pero **no hay ningún ensayo clínico ni publicación** que respalde esta dirección. Además, el nombre de la enfermedad lleva el prefijo "obsolete", lo que sugiere que la predicción puede ser un artefacto del grafo de conocimiento.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Taquicardias (según los datos farmacológicos; los textos de indicación de las autorizaciones de AEMPS no están disponibles) |
| Nueva Indicación Predicha | Bloqueo de rama del haz (término obsoleto en la ontología) |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 7 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información farmacológica disponible, la adenosina actúa sobre los receptores de adenosina A1, A2A, A2B y A3, y también se asocia con TRPM4 y con las fosfatidilinositol 4-quinasas tipo 2 alfa y beta. En la práctica clínica frena la conducción del nodo auriculoventricular, por lo que se usa para tratar taquicardias y como herramienta diagnóstica en arritmias.

Este mismo mecanismo hace que la relación con el bloqueo de rama del haz sea débil. La adenosina puede desenmascarar o empeorar trastornos de la conducción, así que no hay una base mecanística clara para un beneficio terapéutico en esta enfermedad.

El puntaje TxGNN es muy alto, pero eso no basta como respaldo. El término lleva el prefijo "obsolete", lo que indica un nodo de ontología en desuso. Lo más probable es que la señal sea un artefacto del grafo de conocimiento y no una hipótesis terapéutica real. Antes de cualquier revisión adicional hay que asignar este término a un concepto de enfermedad vigente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 7 autorizaciones. Los textos de indicación aprobada no están disponibles en los datos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 36189 | ATEPODIN 100 mg polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | Medix S.A. |
| 81545 | ADENOSINA ACCORD 6 mg/2 ml solución inyectable EFG | Solución inyectable | Accord Healthcare S.L.U. |
| 86371 | ADENOSINA HIKMA 6 mg/2 ml solución inyectable EFG | Solución inyectable | Hikma Farmacêutica (Portugal) S.A. |
| 81546 | ADENOSINA ACCORD 30 mg/10 ml solución para perfusión EFG | Solución para perfusión | Accord Healthcare S.L.U. |
| 61732 | ADENOSCAN 30 mg/10 ml solución para perfusión | Solución para perfusión | Sanofi Aventis S.A. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como advertencia derivada del análisis mecanístico, la adenosina puede desenmascarar o empeorar bloqueos de la conducción y puede provocar arritmias por sí misma.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción no tiene ensayos ni publicaciones (nivel L5), el término de enfermedad está obsoleto y el mecanismo conocido de la adenosina no apoya un beneficio en el bloqueo de rama; incluso podría empeorar la conducción.

**Para avanzar se necesita:**
- Asignar "obsolete bundle branch block" a un concepto de enfermedad vigente y volver a evaluar la predicción con ese concepto.
- Obtener el prospecto de AEMPS (advertencias y contraindicaciones), descargando y analizando el PDF.
- Obtener los datos de mecanismo de acción (MOA) desde DrugBank.

**Nota sobre otra predicción del mismo fármaco:** la segunda predicción, *taquicardia ventricular polimórfica catecolaminérgica* (TxGNN 99.42%, nivel L4, "Research Question"), tiene una base mecanística más plausible: la adenosina contrarresta la estimulación betaadrenérgica. Su única señal clínica directa es un reporte de caso con ATP, no con adenosina. El ensayo Fase 2a NCT07263139 evalúa AGP100, no adenosina. Merece una evaluación aparte.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


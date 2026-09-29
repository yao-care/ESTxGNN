---
layout: default
title: Fosaprepitant
parent: Solo predicción del modelo (L5)
nav_order: 245
evidence_level: L5
indication_count: 10
---

# Fosaprepitant
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

# Fosaprepitant: De Náuseas y Vómitos Inducidos por Quimioterapia a Síndrome Nefrogénico de Antidiuresis Inapropiada

## Resumen en Una Frase

Fosaprepitant es un profármaco intravenoso del antagonista del receptor NK1 aprepitant, usado como antiemético en pacientes que reciben quimioterapia.
El modelo TxGNN predice que podría ser efectivo para el **síndrome nefrogénico de antidiuresis inapropiada**, pero **no hay ningún ensayo clínico ni publicación** que respalde esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Prevención de náuseas y vómitos por quimioterapia (uso antiemético deducido de los ensayos vinculados; los registros de AEMPS no traen texto de indicación) |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, fosaprepitant es el profármaco de aprepitant, un antagonista del receptor NK1 (sustancia P), y su eficacia antiemética está comprobada.

Con los datos disponibles, **la predicción no tiene un vínculo mecanístico que la sostenga**. Esta enfermedad se debe a una mutación con ganancia de función del receptor V2 de vasopresina (AVPR2). Fosaprepitant no tiene una acción conocida sobre esa vía. El puntaje TxGNN, aunque muy alto, es solo una predicción del grafo de conocimiento y no está apoyado por estudios reales.

Entre las 10 indicaciones predichas, solo **retinitis** (puesto 7) tiene algún respaldo: un estudio preclínico en ratón (nivel L4). Ese estudio muestra que fosaprepitant bloquea la expresión de NK1R inducida por radiación UV-B en tejido ocular. Trata de lesión ocular por UV y no de retinitis, así que la extrapolación es indirecta. Las demás predicciones no tienen ensayos ni literatura, o solo tienen ensayos antieméticos sin relación con la enfermedad.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Hay 6 autorizaciones en total; los datos detallan las 5 siguientes. Los registros no incluyen el texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 88344 | Fosaprepitant Tarbis 150 mg polvo para solución para perfusión EFG | Polvo para solución para perfusión | Tarbis Farma S.L. |
| 07437003 | Ivemend 150 mg polvo para solución para perfusión | Polvo para solución para perfusión | Merck Sharp & Dohme B.V. |
| 86382 | Fosaprepitant Hikma 150 mg polvo para solución para perfusión EFG | Polvo para solución para perfusión | Hikma Farmacéutica (Portugal) S.A. |
| 83380 | Fosaprepitant Accord 150 mg polvo para solución para perfusión EFG | Polvo para solución para perfusión | Accord Healthcare S.L.U. |
| 88054 | Fosaprepitant Tecnigen 150 mg polvo para solución para perfusión EFG | Polvo para solución para perfusión | Tecnimede España Industria Farmacéutica S.A. |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (99.92%), pero es solo un resultado del modelo (L5). No hay ensayos ni publicaciones, y no se identifica un mecanismo plausible entre el antagonismo NK1 y la activación del receptor V2.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción desde DrugBank para analizar posibles vínculos mecanísticos.
- Descargar y revisar el prospecto de AEMPS (advertencias y contraindicaciones), que hoy bloquea el cribado de seguridad.
- Validar en estudios preclínicos si el antagonismo NK1 influye en la señalización de AVPR2 o en el manejo de agua renal.
- Valorar si conviene priorizar **retinitis** (L4, preclínico) como candidata alternativa de investigación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


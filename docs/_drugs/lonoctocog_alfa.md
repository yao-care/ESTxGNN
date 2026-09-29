---
layout: default
title: Lonoctocog Alfa
parent: Solo predicción del modelo (L5)
nav_order: 327
evidence_level: L5
indication_count: 4
---

# Lonoctocog Alfa
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Lonoctocog alfa: De Hemofilia A a Pseudo-enfermedad de von Willebrand

## Resumen en Una Frase

Lonoctocog alfa es un factor VIII de coagulación recombinante de cadena única (comercializado en España como AFSTYLA). Se usa como tratamiento sustitutivo en la hemofilia A, aunque el registro de la AEMPS recibido no incluye el texto de indicación.
El modelo TxGNN predice que podría ser efectivo para la **pseudo-enfermedad de von Willebrand** (von Willebrand de tipo plaquetario), pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hemofilia A (según la caracterización general del fármaco; el registro de la AEMPS no incluye texto de indicación) |
| Nueva Indicación Predicha | Pseudo-enfermedad de von Willebrand |
| Puntaje de Predicción TxGNN | 99.85% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 7 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro. Según la información conocida, lonoctocog alfa es un factor VIII recombinante de cadena única. Su función es reponer el FVIII que falta en la cascada de coagulación.

La pseudo-enfermedad de von Willebrand (tipo plaquetario) tiene otro origen: una alteración de ganancia de función de la GPIb-alfa plaquetaria. Esta alteración aumenta la unión al factor von Willebrand (VWF) y favorece la eliminación de multímeros de VWF de alto peso molecular y de plaquetas. El FVIII exógeno no corrige este defecto plaquetario. El único vínculo posible es indirecto: la pérdida de VWF puede reducir secundariamente el FVIII.

**El puntaje alto (99.85%) refleja solo cercanía en el grafo de conocimiento.** No está respaldado por datos mecanísticos ni clínicos.

Las otras tres predicciones del modelo tampoco tienen respaldo. Todas son L5 y con recomendación Hold:

- **Trastorno primario de liberación plaquetaria (99.84%)**: es un defecto intrínseco de la plaqueta, previo a la cascada de coagulación.
- **Trombastenia de Glanzmann (99.76%)**: el defecto está en la integrina alfaIIb-beta3, y el tratamiento estándar es transfusión de plaquetas o FVIIa recombinante.
- **Síndrome de Scott (99.44%)**: hay un vínculo teórico débil, porque el FVIII forma parte del complejo tenasa. Sin embargo, añadir FVIII no restauraría la superficie procoagulante ausente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 7 autorizaciones registradas. Todas corresponden a AFSTYLA (Csl Behring GmbH), en polvo y disolvente para solución inyectable.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1161158003 | AFSTYLA 1.000 UI | Polvo y disolvente para solución inyectable | No especificada en el registro |
| 1161158002 | AFSTYLA 500 UI | Polvo y disolvente para solución inyectable | No especificada en el registro |
| 1161158007 | AFSTYLA 3.000 UI | Polvo y disolvente para solución inyectable | No especificada en el registro |
| 1161158004 | AFSTYLA 1.500 UI | Polvo y disolvente para solución inyectable | No especificada en el registro |
| 1161158006 | AFSTYLA 2.500 UI | Polvo y disolvente para solución inyectable | No especificada en el registro |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos ni publicaciones. Además, el mecanismo del FVIII no corrige el defecto plaquetario de la pseudo-enfermedad de von Willebrand.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un paso bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión sistemática de la literatura sobre FVIII en von Willebrand de tipo plaquetario y en otros trastornos plaquetarios, para descartar o encontrar evidencia real.
- Completar la evaluación de similitud con la indicación original y de compatibilidad de vía de administración, que siguen pendientes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


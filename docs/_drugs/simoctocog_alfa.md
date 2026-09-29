---
layout: default
title: Simoctocog Alfa
parent: Solo predicción del modelo (L5)
nav_order: 493
evidence_level: L5
indication_count: 10
---

# Simoctocog Alfa
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

# Simoctocog alfa: De Hemofilia A a Enfermedad de von Willebrand tipo plaquetario (pseudo-von Willebrand)

## Resumen en Una Frase

Simoctocog alfa (comercializado como Nuwiq) es un factor VIII de coagulación recombinante humano, utilizado para el tratamiento de la hemofilia A.
El modelo TxGNN predice que podría ser efectivo para **la enfermedad de pseudo-von Willebrand**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hemofilia A (conocimiento general del producto; el texto de las autorizaciones de la AEMPS no incluye la indicación) |
| Nueva Indicación Predicha | Enfermedad de pseudo-von Willebrand (von Willebrand tipo plaquetario) |
| Puntaje de Predicción TxGNN | 99.997% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, simoctocog alfa es un factor VIII recombinante producido en una línea celular humana, sin modificación para unirse al factor von Willebrand (VWF). Su eficacia en la hemofilia A consiste en reponer el FVIII deficiente.

La enfermedad de pseudo-von Willebrand es un defecto de ganancia de función del receptor plaquetario GPIb, que aumenta la unión al VWF. La reposición de FVIII no corrige ese defecto del receptor plaquetario, por lo que el vínculo mecanístico es **indirecto**.

El puntaje tan alto probablemente refleja la cercanía en el grafo de conocimiento entre FVIII, VWF y los trastornos hemorrágicos, no una señal clínica. No hay evidencia clínica que respalde esta indicación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 8 autorizaciones. Todas pertenecen a Octapharma AB, y el texto de indicación aprobada no figura en los datos recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 114936001 | Nuwiq 250 UI | Polvo y disolvente para solución inyectable |
| 114936002 | Nuwiq 500 UI | Polvo y disolvente para solución inyectable |
| 114936003 | Nuwiq 1000 UI | Polvo y disolvente para solución inyectable |
| 114936008 | Nuwiq 1500 UI | Polvo y disolvente para solución inyectable |
| 114936007 | Nuwiq 4000 UI | Polvo y disolvente para solución inyectable |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas.

Existe una alerta específica para una de las indicaciones predichas: en la púrpura trombótica trombocitopénica (TTP, posición 10), aportar FVIII podría aumentar teóricamente el riesgo trombótico. El puntaje alto de esa predicción no debe interpretarse como señal positiva.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos ni literatura. El mecanismo es indirecto, porque el FVIII no corrige el defecto plaquetario de fondo.

Entre las 10 indicaciones predichas, solo dos se marcan como "Research Question" por su coherencia mecanística parcial:
- **Hemofilia A con anomalía vascular**
- **Déficit adquirido de factores de coagulación**, dependiente del subtipo. Por ejemplo, en la hemofilia A adquirida los inhibidores suelen neutralizar el producto y se prefieren agentes de bypass.

El resto se mantiene en Hold.

**Para avanzar se necesita:**
- Prospecto de la AEMPS (advertencias y contraindicaciones), que es un requisito bloqueante para el cribado de seguridad
- Datos del mecanismo de acción desde DrugBank
- Indicación aprobada de cada autorización registrada
- Revisión de literatura específica de FVIII en enfermedad de von Willebrand tipo plaquetario, y definición precisa del subtipo en el caso de déficits adquiridos
- Evaluación de la compatibilidad de vía de administración, que sigue pendiente

*Este informe es solo para referencia de investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


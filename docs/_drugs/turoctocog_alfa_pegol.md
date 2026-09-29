---
layout: default
title: Turoctocog Alfa Pegol
parent: Solo predicción del modelo (L5)
nav_order: 550
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa Pegol
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

# Turoctocog alfa pegol: De Hemofilia A a Trastorno primario de liberación plaquetaria

## Resumen en Una Frase

Turoctocog alfa pegol es un factor VIII de coagulación recombinante con glicoPEGilación (comercializado como Esperoct), utilizado según el conocimiento general del producto para la hemofilia A. Los datos de autorización recibidos no incluyen el texto de indicación.
El modelo TxGNN predice que podría ser efectivo para **trastorno primario de liberación plaquetaria**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción basada solo en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hemofilia A (según conocimiento general del producto; el texto de indicación de las autorizaciones está vacío) |
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria |
| Puntaje de Predicción TxGNN | 99.997% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, turoctocog alfa pegol es un factor VIII recombinante con glicoPEGilación, que repone el cofactor FVIII en el complejo tenasa intrínseco (hemostasia secundaria). Su eficacia se ha establecido en la hemofilia A. Mecanísticamente, en cambio, **no es evidente** que sea aplicable a la nueva indicación.

Los trastornos de liberación de gránulos plaquetarios son defectos de la hemostasia primaria. Reponer FVIII no corrige la secreción de gránulos, por lo que el vínculo mecanístico es débil. El puntaje TxGNN muy alto (0.99997) refleja la cercanía dentro del grafo de conocimiento (fenotipo hemorrágico compartido), no evidencia clínica ni biológica directa.

El modelo también predijo otras nueve enfermedades hemorrágicas o plaquetarias, todas con evidencia L5. La más plausible biológicamente es el **déficit adquirido de factores de coagulación**, porque incluye la deficiencia adquirida de FVIII (p. ej., hemofilia A adquirida). Aun así, los inhibidores neutralizantes limitan el efecto de la reposición, y el término es heterogéneo y requiere definir subtipos. Las demás predicciones (enfermedad de von Willebrand tipo plaquetario, trombastenia de Glanzmann, síndrome de Scott, defectos del receptor de colágeno, trombocitopenias constitucionales, etc.) son defectos plaquetarios en los que la reposición de FVIII no tiene un objetivo claro.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191374001 | ESPEROCT 500 UI | Polvo y disolvente para solución inyectable | No especificada en los datos disponibles |
| 1191374002 | ESPEROCT 1000 UI | Polvo y disolvente para solución inyectable | No especificada en los datos disponibles |
| 1191374003 | ESPEROCT 1500 UI | Polvo y disolvente para solución inyectable | No especificada en los datos disponibles |
| 1191374004 | ESPEROCT 2000 UI | Polvo y disolvente para solución inyectable | No especificada en los datos disponibles |
| 1191374005 | ESPEROCT 3000 UI | Polvo y disolvente para solución inyectable | No especificada en los datos disponibles |

Titular/fabricante de todas las autorizaciones: Novo Nordisk A/S.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5, sin ensayos ni literatura), y el mecanismo del FVIII no corrige los defectos de hemostasia primaria plaquetaria que definen esta enfermedad. No hay base actual para avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS (indicaciones, advertencias y contraindicaciones), que hoy bloquea cualquier cribado de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Buscar de forma dirigida ensayos y literatura sobre uso de FVIII en trastornos plaquetarios
- Priorizar para revisión la predicción de **déficit adquirido de factores de coagulación** (hemofilia A adquirida), definiendo primero el subtipo y el papel de los inhibidores

*Este informe es solo para referencia de investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


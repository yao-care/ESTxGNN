---
layout: default
title: Turoctocog Alfa
parent: Solo predicción del modelo (L5)
nav_order: 549
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa
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

# Turoctocog alfa: De Indicación Original No Disponible a Trastorno Primario de Liberación Plaquetaria

## Resumen en Una Frase

Turoctocog alfa es un factor VIII (FVIII) recombinante con dominio B truncado, comercializado en España como NovoEight. Los datos de autorización de la AEMPS recibidos no incluyen el texto de su indicación original.
El modelo TxGNN predice que podría ser efectivo para el **trastorno primario de liberación plaquetaria**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Trastorno primario de liberación plaquetaria (primary release disorder of platelets) |
| Puntaje de Predicción TxGNN | 99,99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente de datos. Por su naturaleza, turoctocog alfa es un FVIII recombinante que reemplaza el cofactor ausente del factor IXa en el complejo tenasa intrínseco, dentro de la cascada de coagulación. Su uso establecido es el déficit congénito de FVIII.

Los trastornos de liberación plaquetaria son defectos de la secreción de los gránulos de las plaquetas. La reposición de FVIII no corrige ese defecto de fondo. El puntaje alto de TxGNN (99,99%) proviene de una predicción basada en el grafo de conocimiento, probablemente por la cercanía con otros trastornos hemorrágicos. No cuenta con ensayos ni literatura de respaldo.

En resumen, la relación mecanística entre la indicación original y la nueva es débil y especulativa. La predicción debe tratarse como una hipótesis de baja plausibilidad, no como una vía de desarrollo con soporte.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Titular: Novo Nordisk A/S. Todas las presentaciones son polvo y disolvente para solución inyectable. Los textos de indicación aprobada llegaron vacíos en los datos, por lo que no se incluyen. Se listan 5 de las 6 autorizaciones registradas, porque el paquete solo trae 5 entradas.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 113888001 | NovoEight 250 UI | Polvo y disolvente para solución inyectable |
| 113888002 | NovoEight 500 UI | Polvo y disolvente para solución inyectable |
| 113888003 | NovoEight 1000 UI | Polvo y disolvente para solución inyectable |
| 113888005 | NovoEight 2000 UI | Polvo y disolvente para solución inyectable |
| 113888006 | NovoEight 3000 UI | Polvo y disolvente para solución inyectable |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se recuperaron advertencias, contraindicaciones ni interacciones farmacológicas.

Como aviso derivado del análisis mecanístico: para la púrpura trombocitopénica trombótica y la trombocitosis hereditaria con defecto transverso de extremidades (predicciones de rango 9 y 10), un factor procoagulante podría aumentar el riesgo trombótico.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (nivel L5), sin ensayos ni literatura, y el mecanismo no conecta la reposición de FVIII con un defecto de secreción plaquetaria. Las otras 9 predicciones del paquete también son L5. La mejor situada es "déficit adquirido de factores de coagulación" (Research Question), aunque también sin evidencia, y en el caso de inhibidores anti-FVIII la eficacia sería incierta.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (indicación aprobada, advertencias y contraindicaciones), un vacío que bloquea el cribado de seguridad.
- Obtener el mecanismo de acción desde DrugBank.
- Realizar una búsqueda dirigida de literatura y ensayos sobre FVIII en trastornos plaquetarios.
- Evaluar la compatibilidad de vías de administración, que sigue pendiente.
- Verificar la definición de "flood factor deficiency" (rango 8) en el grafo de conocimiento de origen, ya que no es un término estándar.

*Este informe es solo de referencia para la investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Eftrenonacog Alfa
parent: Solo predicción del modelo (L5)
nav_order: 194
evidence_level: L5
indication_count: 3
---

# Eftrenonacog Alfa
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Eftrenonacog alfa: De Hemofilia B a Pseudo-enfermedad de von Willebrand

## Resumen en Una Frase

Eftrenonacog alfa es una proteína de fusión recombinante del factor IX unido a Fc, utilizada originalmente como tratamiento sustitutivo en la hemofilia B.
El modelo TxGNN predice que podría ser efectivo para la **pseudo-enfermedad de von Willebrand**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hemofilia B (según el mecanismo conocido del producto; el texto de indicación aprobada no está disponible en los registros) |
| Nueva Indicación Predicha | Pseudo-enfermedad de von Willebrand (pseudo-von Willebrand disease) |
| Puntaje de Predicción TxGNN | 99.48% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, eftrenonacog alfa es un factor IX recombinante fusionado a Fc que repone la actividad de FIX en la vía intrínseca de la coagulación, y su eficacia en la hemofilia B es la base de su uso.

En este caso, la predicción es **débil desde el punto de vista mecanístico**. La pseudo-enfermedad de von Willebrand (tipo plaquetario) se debe a una mutación de ganancia de función en la GPIbα plaquetaria, que provoca una unión excesiva de multímeros de alto peso molecular del VWF y una eliminación acelerada de plaquetas. El defecto principal está en la interacción plaqueta-VWF, no en una deficiencia de FIX.

El puntaje alto (0.995) probablemente refleja la cercanía en el grafo de conocimiento con los trastornos hemorrágicos y de la coagulación, y no un vínculo biológico validado. Otras predicciones del mismo modelo para este fármaco (trastorno primario de liberación plaquetaria y trombastenia de Glanzmann) presentan el mismo problema: son defectos de la función plaquetaria que la reposición de FIX no corrige.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1161098001 | ALPROLIX 250 UI | Polvo y disolvente para solución inyectable | — |
| 1161098002 | ALPROLIX 500 UI | Polvo y disolvente para solución inyectable | — |
| 1161098003 | ALPROLIX 1.000 UI | Polvo y disolvente para solución inyectable | — |
| 1161098004 | ALPROLIX 2.000 UI | Polvo y disolvente para solución inyectable | — |
| 1161098005 | ALPROLIX 3.000 UI | Polvo y disolvente para solución inyectable | — |

Titular: Swedish Orphan Biovitrum AB (publ).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en la base de datos consultada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y no existe un fundamento mecanístico plausible: el defecto de la enfermedad es plaquetario y no de FIX. Las otras dos indicaciones predichas comparten esta limitación.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco (DrugBank) y del texto de indicación aprobada en AEMPS
- Prospecto de AEMPS con advertencias y contraindicaciones
- Una hipótesis biológica que explique por qué la reposición de FIX podría ser útil en un defecto plaqueta-VWF, respaldada por estudios preclínicos
- Revisión de literatura y de registros de ensayos que confirme la ausencia o presencia de evidencia real
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Lonoctocog Alfa
parent: Solo predicción del modelo (L5)
nav_order: 479
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Lonoctocog Alfa: nueva indicación predicha, Enfermedad de pseudo-von Willebrand (nivel de evidencia L5). Indicación original: Hemofilia (según las indicaciones del grafo de conocimiento"
monitor_inn: "LONOCTOCOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome"]
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Lonoctocog alfa: De Hemofilia a Enfermedad de von Willebrand Tipo Plaquetario (Pseudo-von Willebrand)
{: .text-alpha }

## Resumen en Una Frase

Lonoctocog alfa es un factor VIII de coagulación recombinante de cadena única, utilizado originalmente para el tratamiento de la hemofilia.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad de pseudo-von Willebrand**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hemofilia (según las indicaciones del grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Enfermedad de pseudo-von Willebrand |
| Puntaje de Predicción TxGNN | 99.85% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 7 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, lonoctocog alfa es un factor VIII recombinante de cadena única con mayor afinidad de unión al factor von Willebrand (VWF), cuya eficacia en la reposición de FVIII en hemofilia está establecida.

La enfermedad de pseudo-von Willebrand (tipo plaquetario) se debe a mutaciones de ganancia de función en GPIbα, que aumentan la unión de las plaquetas al VWF y provocan un defecto de hemostasia primaria con pérdida de multímeros de VWF de alto peso molecular. El reemplazo de FVIII no corrige este defecto del receptor plaquetario.

El puntaje tan alto (99.85%) probablemente refleja la cercanía en el grafo con otros trastornos hemorrágicos y de la coagulación, más que un mecanismo validado. El vínculo es especulativo: el FVIII podría ayudar, como mucho, en casos con reducción secundaria de FVIII, algo que aquí no está respaldado.

**Otras predicciones del modelo (todas de nivel L5, sin ensayos ni literatura):**

| Enfermedad predicha | Puntaje TxGNN | Valoración mecanística |
|------|------|------|
| Trastorno primario de liberación plaquetaria | 99.84% | El FVIII no corrige defectos de gránulos o señalización plaquetaria |
| Trombastenia de Glanzmann | 99.76% | Defecto de la integrina αIIbβ3; el FVIII no restaura la agregación plaquetaria, por lo que es mecanísticamente inconsistente |
| Síndrome de Scott | 99.44% | Conexión conceptual laxa (el FVIII depende de membranas con fosfatidilserina), pero aportar más FVIII no repara la superficie procoagulante ausente |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1161158003 | AFSTYLA 1.000 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 1161158002 | AFSTYLA 500 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 1161158007 | AFSTYLA 3.000 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 1161158004 | AFSTYLA 1.500 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 1161158006 | AFSTYLA 2.500 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |

Se muestran 5 de las 7 autorizaciones vigentes (todas de CSL Behring GmbH; las otras dos corresponden a las presentaciones de 250 UI y 2.000 UI).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos clínicos ni literatura. Además, el mecanismo conocido del FVIII no corresponde a la fisiopatología de la enfermedad de pseudo-von Willebrand, que es un defecto del receptor plaquetario GPIbα.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) del fármaco
- Advertencias y contraindicaciones del prospecto de la AEMPS
- Evidencia preclínica o clínica que sustente el uso de FVIII en defectos de función plaquetaria
- Evaluación de si existe algún subgrupo con reducción secundaria de FVIII que pudiera beneficiarse
- Análisis de compatibilidad de vía de administración y de similitud con la indicación original
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


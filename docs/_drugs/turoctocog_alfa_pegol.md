---
layout: default
title: Turoctocog Alfa Pegol
parent: Solo predicción del modelo (L5)
nav_order: 833
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
monitor_inn: "TUROCTOCOG ALFA PEGOL"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "acquired coagulation factor deficiency", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency", "hereditary thrombocytosis with transverse limb defect", "fetal and neonatal alloimmune thrombocytopenia"]
description: "Turoctocog Alfa Pegol: nueva indicación predicha, Primary release disorder of platelets (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 5 (comercializadas: 5)"
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Turoctocog Alfa Pegol: Primary release disorder of platelets
{: .text-alpha }

## Resumen en Una Frase

Turoctocog alfa pegol es un factor VIII de coagulación recombinante, truncado en el dominio B y glicoPEGilado, utilizado originalmente para el tratamiento de la hemofilia.
El modelo TxGNN predice que podría ser efectivo para el **trastorno de liberación plaquetaria primario**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Primary release disorder of platelets |
| Puntaje de Predicción TxGNN | 1.0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 5 de 5) |
| Número de Autorizaciones | 5 (comercializadas: 5) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Turoctocog Alfa Pegol es (traducción no oficial): «Proteína exógena del factor VIII de la coagulación». Texto original en inglés: "Coagulation factor VIII exogenous protein" ([ChEMBL CHEMBL5315071 (turoctocog alfa pegol): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL5315071), CC BY-SA 3.0; consultado el 2026-11-19). Según la información conocida, turoctocog alfa pegol es un factor VIII recombinante, truncado en el dominio B y glicoPEGilado, que repone el factor VIII deficiente en la hemofilia, y su uso en esa indicación está respaldado por su autorización de comercialización en España.

Sin embargo, la nueva indicación predicha es un defecto primario de la función plaquetaria, con niveles normales de factor VIII. La reposición de este factor no tiene una justificación mecanística clara en ese contexto. El puntaje elevado del modelo parece reflejar la proximidad dentro de la red de conocimiento entre trastornos hemorrágicos, y no un vínculo farmacológico validado.

Por tanto, esta predicción debe considerarse una hipótesis sin respaldo mecanístico ni clínico. Otras predicciones de la lista (por ejemplo, la deficiencia adquirida de factores de coagulación) son mecanísticamente más cercanas, pero tampoco cuentan con evidencia aportada y presentan limitaciones importantes, como la presencia de inhibidores autoinmunes.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191374001 | ESPEROCT 500 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 1191374002 | ESPEROCT 1000 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 1191374003 | ESPEROCT 1500 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 1191374004 | ESPEROCT 2000 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 1191374005 | ESPEROCT 3000 UI | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |

Todas las autorizaciones corresponden a Novo Nordisk A/S, son de principio activo único y se encuentran vigentes.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es de nivel L5 (solo modelo), sin ensayos clínicos ni literatura, y carece de lógica mecanística: el factor VIII no corrige un defecto plaquetario con niveles normales de FVIII.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA).
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), actualmente no disponible, lo que impide el cribado de seguridad.
- Revisión de la literatura y de registros de ensayos para el trastorno de liberación plaquetaria primario.
- Evaluar si otras indicaciones predichas con mayor plausibilidad (p. ej., deficiencia adquirida de factores de coagulación) merecen priorizarse, teniendo en cuenta el papel de los inhibidores.
- Depurar las etiquetas de enfermedad ambiguas de las predicciones (p. ej., «flood factor deficiency») antes de nuevas evaluaciones.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; la versión anterior se guarda en el registro) | [ChEMBL CHEMBL5315071 (turoctocog alfa pegol): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL5315071) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Lonoctocog Alfa
parent: Solo predicción del modelo (L5)
nav_order: 479
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "LONOCTOCOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome"]
description: "Lonoctocog Alfa: nueva indicación predicha, Enfermedad de pseudo-von Willebrand (pseudo-von Willebrand disease) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 7 (comercializadas: 4; autorizadas no comercializadas: 3)"
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

## Lonoctocog Alfa: Enfermedad de pseudo-von Willebrand (pseudo-von Willebrand disease)
{: .text-alpha }

## Resumen en Una Frase

Lonoctocog alfa es un factor VIII de coagulación recombinante de cadena única, utilizado originalmente para el tratamiento de la hemofilia.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad de pseudo-von Willebrand**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad de pseudo-von Willebrand (pseudo-von Willebrand disease) |
| Puntaje de Predicción TxGNN | 0.9985 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 4 de 7; autorizadas no comercializadas: 3) |
| Número de Autorizaciones | 7 (comercializadas: 4) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Lonoctocog Alfa es (traducción no oficial): «Proteína exógena del factor VIII de la coagulación». Texto original en inglés: "Coagulation factor VIII exogenous protein" ([ChEMBL CHEMBL4594603 (lonoctocog alfa): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL4594603), CC BY-SA 3.0; consultado el 2026-11-19). Según la información conocida, lonoctocog alfa es un factor VIII recombinante de cadena única con mayor afinidad de unión al factor von Willebrand (VWF), cuya eficacia en la reposición de FVIII en hemofilia está establecida.

La enfermedad de pseudo-von Willebrand (tipo plaquetario) se debe a mutaciones de ganancia de función en GPIbα, que aumentan la unión de las plaquetas al VWF y provocan un defecto de hemostasia primaria con pérdida de multímeros de VWF de alto peso molecular. El reemplazo de FVIII no corrige este defecto del receptor plaquetario.

El puntaje tan alto (0.9985) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. El vínculo es especulativo: el FVIII podría ayudar, como mucho, en casos con reducción secundaria de FVIII, algo que aquí no está respaldado.

**Otras predicciones del modelo (todas de nivel L5, sin ensayos ni literatura):**

| Enfermedad predicha | Puntaje TxGNN | Valoración mecanística |
|------|------|------|
| Trastorno primario de liberación plaquetaria | 0.9984 | El FVIII no corrige defectos de gránulos o señalización plaquetaria |
| Trombastenia de Glanzmann | 0.9976 | Defecto de la integrina αIIbβ3; el FVIII no restaura la agregación plaquetaria, por lo que es mecanísticamente inconsistente |
| Síndrome de Scott | 0.9944 | Conexión conceptual laxa (el FVIII depende de membranas con fosfatidilserina), pero aportar más FVIII no repara la superficie procoagulante ausente |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 1161158003 | AFSTYLA 1.000 UI POLVO Y DISOLVENTE PARA SOLUCION INYECTABLE | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Csl Behring Gmbh | Comercializada |
| 1161158002 | AFSTYLA 500 UI POLVO Y DISOLVENTE PARA SOLUCION INYECTABLE | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Csl Behring Gmbh | Comercializada |
| 1161158001 | AFSTYLA 250 UI POLVO Y DISOLVENTE PARA SOLUCION INYECTABLE | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Csl Behring Gmbh | Comercializada |
| 1161158005 | AFSTYLA 2.000 UI POLVO Y DISOLVENTE PARA SOLUCION INYECTABLE | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Csl Behring Gmbh | Comercializada |
| 1161158007 | AFSTYLA 3.000 UI POLVO Y DISOLVENTE PARA SOLUCION INYECTABLE | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Csl Behring Gmbh | Autorizada, no comercializada |
| 1161158004 | AFSTYLA 1.500 UI POLVO Y DISOLVENTE PARA SOLUCION INYECTABLE | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Csl Behring Gmbh | Autorizada, no comercializada |
| 1161158006 | AFSTYLA 2.500 UI POLVO Y DISOLVENTE PARA SOLUCION INYECTABLE | POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE | Csl Behring Gmbh | Autorizada, no comercializada |

Se muestran las 7 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Todas las autorizaciones son de CSL Behring GmbH.

<!-- review:begin es-lic-20261124b-lonoctocog_alfa-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Se muestran 5 de las 7 autorizaciones vigentes (todas de CSL Behring GmbH; las otras dos corresponden a las presentaciones de 250 UI y 2.000 UI)." Corregido: la frase hablaba de autorizaciones que no figuraban en la tabla anterior (por ejemplo, «la sexta», «las restantes» u «otras»). La tabla de Información de Mercado en España se genera desde el 2026-11-24 por programa a partir de los datos de CIMA (AEMPS) y las incluye; las cifras actuales están en el Resumen rápido. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261124b-lonoctocog_alfa-1 -->

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

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; la versión anterior se guarda en el registro) | [ChEMBL CHEMBL4594603 (lonoctocog alfa): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL4594603) |
| 2026-11-24 | Eliminado: descripción de la tabla anterior, número y «las otras dos» | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


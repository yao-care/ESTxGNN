---
layout: default
title: Prucalopride
parent: Solo predicción del modelo (L5)
nav_order: 671
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-25
description: "Prucalopride: nueva indicación predicha, Hipoalfalipoproteinemia (nivel de evidencia L5). Indicación original: Trastorno de estreñimiento (estreñimiento crónico)"
monitor_inn: "Prucalopride"
predicted_indications: ["hypoalphalipoproteinemia", "homozygous familial hypercholesterolemia", "duodenal ulcer (disease)", "oral candidiasis", "obsolete familial combined hyperlipidemia", "amyloidosis (disease)", "strongyloidiasis", "HIV infectious disease", "primary amyloidosis", "acquired amyloid peripheral neuropathy"]
---

# Prucalopride
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

## Prucalopride: De Trastorno de Estreñimiento a Hipoalfalipoproteinemia
{: .text-alpha }

## Resumen en Una Frase

Prucalopride es un agonista selectivo del receptor 5-HT4, utilizado originalmente para el tratamiento del estreñimiento crónico.
El modelo TxGNN predice que podría ser efectivo para **hipoalfalipoproteinemia**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno de estreñimiento (estreñimiento crónico) |
| Nueva Indicación Predicha | Hipoalfalipoproteinemia |
| Puntaje de Predicción TxGNN | 0.9982 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 4; autorizadas no comercializadas: 2) |
| Número de Autorizaciones | 4 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Prucalopride actúa como agonista selectivo del receptor 5-HT4 (gen HTR4), con efecto procinético sobre el tracto gastrointestinal. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción, pero la farmacología conocida lo describe como un tratamiento oral de una vez al día para adultos con estreñimiento crónico en quienes los laxantes no son eficaces.

Con la información disponible, **no se identifica un vínculo mecanístico plausible** entre la agonía 5-HT4 y el metabolismo de las lipoproteínas de alta densidad (HDL) o la regulación de ApoA-I. La puntuación alta proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; no está respaldada por ningún estudio real. La predicción debe considerarse una hipótesis sin fundamento mecanístico por el momento.

Otras predicciones del modelo tampoco muestran respaldo sólido. Las más cercanas al área gastrointestinal original son la amiloidosis y la amiloidosis primaria (dismotilidad intestinal sintomática, nivel L4), donde un procinético podría aliviar síntomas pero no modificaría la enfermedad, y la úlcera duodenal, con un vínculo débil y especulativo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para hipoalfalipoproteinemia.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 09581002 | RESOLOR 2 MG COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Takeda Pharmaceuticals International Ag Ireland Branch | Comercializada |
| 09581001 | RESOLOR 1 MG COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Takeda Pharmaceuticals International Ag Ireland Branch | Comercializada |
| 91611 | PRUCALOPRIDA TARBIS 1 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Tarbis Farma S.L. | Autorizada, no comercializada |
| 91612 | PRUCALOPRIDA TARBIS 2 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Tarbis Farma S.L. | Autorizada, no comercializada |

Se muestran las 4 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Todas las autorizaciones están vigentes; los titulares son Takeda Pharmaceuticals International AG, sucursal de Irlanda, y Tarbis Farma S.L. (genéricos).

<!-- review:begin es-lic-20261125-prucalopride-1 -->

> **Corrección de revisión (2026-11-25)**: Texto original: "Ambas autorizaciones están vigentes y corresponden al titular Takeda Pharmaceuticals International AG, sucursal de Irlanda." Corregido: desde el 2026-11-25 se incorporan a los datos las autorizaciones de CIMA (AEMPS) posteriores a marzo de 2026 (incluidas importaciones paralelas) con el mismo criterio de recogida; la frase ya no coincidía con ellas. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261125-prucalopride-1 -->

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): colitis ulcerosa, enfermedad inflamatoria intestinal y perforación intestinal.
- **Interacciones farmacológicas**: la consulta se completó y devolvió un único registro, que describe la diana farmacológica (receptor 5-HT4) y no una interacción con otro fármaco. No se identificaron interacciones clínicas específicas.

Consultar el prospecto para información de seguridad adicional (advertencias y contraindicaciones oficiales).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipoalfalipoproteinemia se basa solo en el modelo (L5), sin ensayos, sin literatura y sin vínculo mecanístico plausible con el mecanismo 5-HT4. No hay base para avanzar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto oficial de la AEMPS (advertencias y contraindicaciones) para completar el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Identificar una hipótesis mecanística que conecte el agonismo 5-HT4 con el metabolismo de HDL, o evaluar candidatas con mayor plausibilidad biológica (p. ej., dismotilidad GI asociada a amiloidosis, solo como alivio sintomático).
- Realizar estudios preclínicos o de mecanismo antes de plantear cualquier ensayo clínico.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-25 | «Ambas … titular Takeda» → todas; se añade Tarbis Farma | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Prucalopride
parent: Solo predicción del modelo (L5)
nav_order: 671
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
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
| Puntaje de Predicción TxGNN | 99.82% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Prucalopride actúa como agonista selectivo del receptor 5-HT4 (gen HTR4), con efecto procinético sobre el tracto gastrointestinal. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción, pero la farmacología conocida lo describe como un tratamiento oral de una vez al día para adultos con estreñimiento crónico en quienes los laxantes no son eficaces.

Con la información disponible, **no se identifica un vínculo mecanístico plausible** entre la agonía 5-HT4 y el metabolismo de las lipoproteínas de alta densidad (HDL) o la regulación de ApoA-I. La puntuación alta de TxGNN proviene de relaciones en el grafo de conocimiento y no está respaldada por ningún estudio real. La predicción debe considerarse una hipótesis sin fundamento mecanístico por el momento.

Otras predicciones del modelo tampoco muestran respaldo sólido. Las más cercanas al área gastrointestinal original son la amiloidosis y la amiloidosis primaria (dismotilidad intestinal sintomática, nivel L4), donde un procinético podría aliviar síntomas pero no modificaría la enfermedad, y la úlcera duodenal, con un vínculo débil y especulativo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para hipoalfalipoproteinemia.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 09581002 | RESOLOR 2 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 09581001 | RESOLOR 1 MG comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |

Ambas autorizaciones están vigentes y corresponden al titular Takeda Pharmaceuticals International AG, sucursal de Irlanda.

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


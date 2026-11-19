---
layout: default
title: Iodixanol
parent: Solo predicción del modelo (L5)
nav_order: 426
evidence_level: L5
indication_count: 2
monitor_inn: "IODIXANOL"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis"]
last_modified_at: 2026-11-20
description: "Iodixanol: nueva indicación predicha, Osteoartritis (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
---

# Iodixanol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Iodixanol: De Medio de Contraste Radiológico a Osteoartritis
{: .text-alpha }

## Resumen en Una Frase

Iodixanol es un medio de contraste yodado, no iónico e iso-osmolar, utilizado en diagnóstico por imagen radiológica.
El modelo TxGNN predice que podría ser efectivo para **osteoartritis**, pero no hay **ningún ensayo clínico** y las **5 publicaciones** encontradas tratan sobre iodixanol solo como herramienta de imagen, sin demostrar un efecto terapéutico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Osteoartritis |
| Puntaje de Predicción TxGNN | 0,9907 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 2) |
| Número de Autorizaciones | 2 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Iodixanol (traducción no oficial): «La inyección intravascular de iodixanol opacifica los vasos en el trayecto del flujo del medio de contraste, lo que permite la visualización de las estructuras internas. En las imágenes del cuerpo, los medios de contraste yodados difunden desde el espacio vascular hacia el espacio extravascular.» Texto original en inglés: "Intravascular injection of iodixanol opacifies vessels in the path of flow of the contrast agent, permitting visualization of internal structures. In imaging of the body, iodinated contrast agents diffuse from the vascular into the extravascular space." ([DailyMed: Visipaque (iodixanol) prescribing information, GE Healthcare Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d964c13-88ad-43be-88d4-a3a7ea4d5b5e), versión del 2026-10-16; consultado el 2026-11-19). Según la información conocida, iodixanol es un contraste radiográfico yodado, no iónico e iso-osmolar, sin farmacología conocida que modifique la enfermedad.

La literatura vincula iodixanol con la osteoartritis solo como herramienta de imagen: la tomografía computarizada con contraste se usa para visualizar el cartílago y estudiar la difusión de solutos a través del cartílago y la interfase con el hueso subcondral. Un estudio in vitro halló además que los contrastes yodados no alteran la función del plasma rico en plaquetas.

Ninguno de estos trabajos estudia un efecto terapéutico en osteoartritis. El puntaje alto de TxGNN probablemente refleja la proximidad en la red a términos de imagen y articulación, y no un mecanismo terapéutico real. Por ello la predicción no puede considerarse respaldada, y el nivel de evidencia se fija en L5, ya que ningún estudio citado evalúa iodixanol como tratamiento de esta enfermedad.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Estudio preclínico de imagen | Annals of Biomedical Engineering | Imagen por TC con difusión de nanopartículas y elementos finitos para estudiar la función del cartílago |
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Estudio preclínico de imagen | Annals of Biomedical Engineering | Agente de doble contraste en TC de recuento de fotones para evaluar la salud del cartílago articular |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Estudio computacional/ex vivo | Journal of Biomechanics | Uso de iodixanol como contraste difusor para medir la permeabilidad de la interfase osteocondral en muestras equinas y humanas |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Estudio computacional | Journal of Biomechanics | Modelo de elementos finitos del transporte de solutos neutros a través de la interfase osteocondral |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | Estudio in vitro | Journal of Experimental Orthopaedics | Los contrastes yodados no afectan la función del plasma rico en plaquetas en fase temprana |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 60636 | VISIPAQUE 270 mg/ml solución inyectable | Solución inyectable | No disponible en los datos compilados |
| 60637 | VISIPAQUE 320 mg/ml solución inyectable | Solución inyectable | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 100 interacciones; entre las principales, de nivel mayor, figuran metformina, anfotericina B (y sus formulaciones lipídicas y liposomal), mesalazina, balsalazida, olsalazina, sulfasalazina, vancomicina, kanamicina, neomicina, estreptomicina y polimixina B. Manitol figura con nivel moderado.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos y la literatura solo describe iodixanol como herramienta de imagen del cartílago, sin evidencia de efecto terapéutico en osteoartritis. El puntaje de TxGNN no es suficiente por sí solo.

**Para avanzar se necesita:**
- Datos del mecanismo de acción que justifiquen un efecto terapéutico
- Estudios preclínicos que evalúen un efecto modificador de la enfermedad en osteoartritis
- Advertencias y contraindicaciones del prospecto de la AEMPS para el cribado de seguridad
- Evaluación de la compatibilidad de vía de administración (la actual es inyectable)

---

### Nota sobre la segunda predicción: artritis reumatoide

El modelo también predice **artritis reumatoide** (puntaje 0,9900), con nivel de evidencia **L5** y decisión **Hold**. La única publicación recuperada ([PMID 36628042](https://pubmed.ncbi.nlm.nih.gov/36628042/), 2022, *Cureus*) es un reporte de caso sobre desensibilización a otro contraste (iohexol), que no aborda iodixanol ni la eficacia en la enfermedad. No existe vínculo mecanístico respaldado.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Visipaque (iodixanol) prescribing information, GE Healthcare Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d964c13-88ad-43be-88d4-a3a7ea4d5b5e) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


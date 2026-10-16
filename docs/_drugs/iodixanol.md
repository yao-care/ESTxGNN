---
layout: default
title: Iodixanol
parent: Solo predicción del modelo (L5)
nav_order: 426
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Iodixanol: nueva indicación predicha, Osteoartritis susceptibility (susceptibilidad a la osteoartritis) (nivel de evidencia L5). Indicación original: No disponible en las autorizaciones registradas (…"
monitor_inn: "IODIXANOL"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis"]
---

# Iodixanol
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

# Iodixanol: De Medio de Contraste Radiológico a Artrosis (Osteoartritis)

## Resumen en Una Frase

Iodixanol es un medio de contraste radiológico yodado, no iónico e iso-osmolar, utilizado como ayuda en técnicas de diagnóstico por imagen.
El modelo TxGNN predice que podría ser efectivo para **osteoartritis (artrosis)**, pero **no hay ensayos clínicos** y las **5 publicaciones** disponibles tratan el fármaco como herramienta de imagen, no como tratamiento.
La predicción es, por tanto, puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las autorizaciones registradas (el texto de indicación está vacío) |
| Nueva Indicación Predicha | Osteoartritis susceptibility (susceptibilidad a la osteoartritis); la segunda predicción, osteoartritis, es la que cuenta con literatura |
| Puntaje de Predicción TxGNN | 99,16 % (susceptibilidad a la osteoartritis); 99,07 % (osteoartritis); 99,00 % (artritis reumatoide) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, iodixanol es un medio de contraste yodado no iónico e iso-osmolar, que atenúa los rayos X y mejora la visualización de estructuras en imagen. No se le conoce acción farmacológica sobre los determinantes genéticos o biológicos de la osteoartritis.

**No se ha establecido un vínculo mecanístico.** Las publicaciones sobre osteoartritis emplean iodixanol como herramienta de imagen (TC con contraste del cartílago, imagen de difusión de nanopartículas, modelado del transporte de solutos en la interfaz osteocondral). Un estudio in vitro halló que los contrastes yodados no alteran la función del plasma rico en plaquetas, lo que es un hallazgo de compatibilidad y no de beneficio terapéutico.

El alto puntaje de TxGNN probablemente refleja la frecuente coaparición del fármaco con la osteoartritis en la investigación de imagen, y no una relación terapéutica. Para la artritis reumatoide, la única publicación es un caso clínico de desensibilización a iohexol (un contraste relacionado), sin plausibilidad inmunomoduladora para iodixanol.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Literatura asociada a osteoartritis (predicción 2):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Método de imagen/diagnóstico | Annals of Biomedical Engineering | TC y elementos finitos con difusión de nanopartículas para describir la función del cartílago |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Modelado computacional | Journal of Biomechanics | Modelo de elementos finitos del transporte de solutos neutros a través de la interfaz osteocondral |
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Método de imagen/diagnóstico | Annals of Biomedical Engineering | Agente de contraste dual en TC de conteo de fotones para evaluar la salud del cartílago articular |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Estudio ex vivo/transporte | Journal of Biomechanics | Iodixanol como contraste difusor para estudiar la permeabilidad de la interfaz osteocondral |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | Estudio in vitro | Journal of Experimental Orthopaedics | Los contrastes yodados no influyen en la función del plasma rico en plaquetas en fase temprana |

Literatura asociada a artritis reumatoide (predicción 3):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36628042](https://pubmed.ncbi.nlm.nih.gov/36628042/) | 2022 | Reporte de caso | Cureus | Desensibilización exitosa a iohexol en una paciente con amiloidosis secundaria a artritis reumatoide |

No se recuperó literatura para la susceptibilidad a la osteoartritis.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 60636 | VISIPAQUE 270 mg/ml solución inyectable | Solución inyectable | No disponible |
| 60637 | VISIPAQUE 320 mg/ml solución inyectable | Solución inyectable | No disponible |

Ambas autorizaciones están vigentes y corresponden al titular GE Healthcare Bio-Sciences, S.A.U.

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total. Entre las mostradas, la mayoría son de nivel **Mayor**:
  - Metformina
  - Anfotericina B (incluidas las formulaciones lipídica, de sulfato de colesterilo y liposomal)
  - Mesalazina, balsalazida, olsalazina y sulfasalazina
  - Vancomicina
  - Aminoglucósidos: kanamicina, neomicina y estreptomicina
  - Polimixina B
- De nivel **Moderado**: manitol.
- De nivel **Desconocido**: famotidina, ácido acetilsalicílico, morfina, omeprazol y prednisona.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos y la literatura describe a iodixanol únicamente como herramienta de imagen, sin evidencia de efecto terapéutico en artrosis ni en artritis reumatoide. El puntaje de TxGNN, aunque alto, es solo una predicción computacional (nivel L5).

**Para avanzar se necesita:**
- Datos del mecanismo de acción del fármaco
- Texto de indicaciones, advertencias y contraindicaciones del prospecto de la AEMPS
- Una hipótesis mecanística plausible de acción terapéutica en osteoartritis, respaldada por estudios preclínicos
- Revisión del posible sesgo de coaparición en la literatura de imagen que pudo inflar la predicción
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


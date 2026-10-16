---
layout: default
title: Nabumetone
parent: Solo predicción del modelo (L5)
nav_order: 547
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Nabumetone: nueva indicación predicha, Displasia acromesomélica, tipo Hunter-Thompson (nivel de evidencia L5). Indicación original: Artritis reumatoide / artrosis / artropatía (según el grafo de cono…"
monitor_inn: "nabumetone"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "spondyloarthropathy, susceptibility to", "WHIM syndrome", "rheumatoid nodulosis"]
---

# Nabumetone
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

# Nabumetona: De Artritis Reumatoide a Displasia Acromesomélica Tipo Hunter-Thompson

## Resumen en Una Frase

Nabumetona es un antiinflamatorio no esteroideo (AINE), profármaco del 6-MNA, utilizado originalmente en artritis reumatoide, artrosis y artropatías.
El modelo TxGNN predice que podría ser efectivo para la **displasia acromesomélica tipo Hunter-Thompson**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata de una predicción exclusivamente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis reumatoide / artrosis / artropatía (según el grafo de conocimiento; el texto de indicación de la autorización de AEMPS no está disponible) |
| Nueva Indicación Predicha | Displasia acromesomélica, tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 99,99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, nabumetona es un profármaco cuyo metabolito activo, el 6-MNA, inhibe preferentemente la COX-2, con eficacia comprobada en enfermedades articulares inflamatorias y degenerativas.

La displasia acromesomélica tipo Hunter-Thompson es una enfermedad esquelética genética rara, asociada a defectos en la vía de señalización CDMP1/GDF5. **No se identifica un vínculo mecanístico plausible**: la inhibición de la COX-2 no guarda relación conocida con esa vía. El puntaje elevado probablemente refleja la cercanía en el grafo de conocimiento con nodos de fenotipo articular/esquelético (artropatía, artrosis), y no una justificación farmacológica.

Por ello, esta predicción debe considerarse una hipótesis sin respaldo mecanístico ni clínico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59395 | RELIF 1000 MG COMPRIMIDOS DISPERSABLES | Comprimido dispersable | No disponible en los datos compilados |

Titular/fabricante: Viatris Healthcare Limited.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): enfermedad hipertensiva/hipertensión, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, enfermedad ulcerosa péptica (incluida la activa), trastornos de la coagulación, infarto de miocardio, trombosis coronaria, enfermedad cardiovascular y cardiopatía, hemoglobinopatía, abuso/dependencia de sustancias y piouréter.
- **Interacciones farmacológicas**: se registraron 217 interacciones. Entre las de nivel moderado destacan:
  - corticoesteroides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona);
  - ácido acetilsalicílico;
  - metformina y sulfonilureas (clorpropamida, glimepirida);
  - mesalazina y balsalazida;
  - vancomicina;
  - sales de potasio y laxantes/preparaciones de limpieza intestinal (picosulfato, polietilenglicol, sulfato de sodio).

  Entre las de nivel menor figuran ranitidina, cimetidina y linaclotida.

Para advertencias y contraindicaciones oficiales, consultar el prospecto de AEMPS.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos, literatura y vínculo mecanístico plausible (nivel L5). El puntaje alto de TxGNN no basta para avanzar, y el perfil de seguridad de los AINE añade riesgos sin un beneficio esperado demostrado.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS (advertencias, contraindicaciones e indicaciones aprobadas).
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Justificar un vínculo biológico entre la inhibición de COX-2 y la vía CDMP1/GDF5, o bien estudios preclínicos que lo respalden.
- Considerar candidatas con mayor plausibilidad dentro de la misma lista de predicciones, como la espondiloartropatía (susceptibilidad) y la nodulosis reumatoide, que ya están marcadas como preguntas de investigación y se apoyan en el uso de AINE en enfermedades inflamatorias articulares.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


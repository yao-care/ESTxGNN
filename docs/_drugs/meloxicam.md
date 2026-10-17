---
layout: default
title: Meloxicam
parent: Solo predicción del modelo (L5)
nav_order: 502
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Meloxicam: nueva indicación predicha, Displasia acromesomélica, tipo Hunter-Thompson (nivel de evidencia L5). Indicación original: Artritis reumatoide, artrosis, artropatía…"
monitor_inn: "MELOXICAM"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "rheumatoid nodulosis", "WHIM syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Meloxicam
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

# Meloxicam: De Artritis Reumatoide a Displasia Acromesomélica de tipo Hunter-Thompson

## Resumen en Una Frase

Meloxicam es un antiinflamatorio no esteroideo (AINE) con preferencia por COX-2, utilizado originalmente para el tratamiento de la artritis reumatoide, la artrosis y otras afecciones articulares.
El modelo TxGNN predice que podría ser efectivo para la **displasia acromesomélica de tipo Hunter-Thompson**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.
La predicción se basa únicamente en el modelo (nivel de evidencia L5) y no tiene un vínculo mecanístico plausible.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis reumatoide, artrosis, artropatía, artritis idiopática juvenil, espondiloartropatía (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Displasia acromesomélica, tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 16 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, meloxicam es un AINE con inhibición preferente de COX-2, que reduce la síntesis de prostaglandinas inflamatorias y, con ello, el dolor y la inflamación articular. Su eficacia en enfermedades articulares inflamatorias como la artritis reumatoide y la artrosis es conocida.

La displasia acromesomélica de tipo Hunter-Thompson es una displasia esquelética rara causada por variantes de pérdida de función en CDMP1/GDF5, que alteran la condrogénesis. Meloxicam podría aliviar el dolor o la inflamación de forma sintomática, pero no actúa sobre el defecto genético subyacente.

Por tanto, **no se identifica un vínculo mecanístico claro**. El puntaje alto de TxGNN probablemente refleja la cercanía en el grafo de conocimiento con términos esqueléticos o de artropatía, y no una señal terapéutica real. Esta predicción debe interpretarse con mucha cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en España

Se muestran 5 de las 16 autorizaciones vigentes (todas de principio activo único). Los textos de indicación aprobada no figuran en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 64313 | MOVALIS 15 mg/1,5 ml solución inyectable | Solución inyectable | No disponible |
| 61076 | MOVALIS 15 mg comprimidos | Comprimido | No disponible |
| 61075 | MOVALIS 7,5 mg comprimidos | Comprimido | No disponible |
| 69366 | Meloxicam Normon 15 mg comprimidos EFG | Comprimido | No disponible |
| 69094 | Meloxicam Cinfa 15 mg comprimidos EFG | Comprimido | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto del prospecto)**: hipertensión, enfermedad renal e insuficiencia renal, insuficiencia cardíaca congestiva, enfermedad cardiovascular y cardiopatía, infarto de miocardio, ictus y enfermedad cerebrovascular, infarto cerebral, trastornos de la coagulación, úlcera péptica activa, gastritis, diabetes mellitus y cetoacidosis diabética, hiperlipidemia (incluida la familiar), anemia y hemoglobinopatías, y abuso/dependencia de sustancias.
- **Interacciones Farmacológicas**: se registraron 100 interacciones. Entre las principales (mayoría de nivel moderado):
  - Corticoides: hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida.
  - Antidiabéticos: metformina, clorpropamida, glimepirida.
  - Otros AINE/salicilatos y aminosalicilatos: ácido acetilsalicílico, mesalazina, balsalazida.
  - Aminoglucósidos y glucopéptidos: kanamicina, vancomicina.
  - Sales de potasio y laxantes/preparaciones intestinales: citrato y bicarbonato de potasio, ácido picosulfúrico, polietilenglicol con electrolitos, sulfato de sodio.
  - Aprepitant (moderada); linaclotida (menor).

Las advertencias y contraindicaciones del prospecto de la AEMPS no están disponibles en los datos compilados; consultar el prospecto para información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción solo cuenta con respaldo del modelo (L5), sin ensayos ni literatura, y no existe un vínculo mecanístico plausible entre la inhibición de COX-2 y el defecto genético de GDF5. Además, el perfil de contraindicaciones de meloxicam es amplio.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y obtener el prospecto de la AEMPS (advertencias y contraindicaciones) para completar el cribado de seguridad.
- Evidencia preclínica o clínica que justifique un papel de la vía de COX/prostaglandinas en esta displasia.
- Considerar otras predicciones del modelo con mayor plausibilidad, como espondiloartropatía (L4) o artritis idiopática juvenil poliarticular con factor reumatoide positivo (L3). Estas reflejan en gran parte usos ya conocidos del fármaco y no constituyen un reposicionamiento propiamente dicho.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


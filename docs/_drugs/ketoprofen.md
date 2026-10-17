---
layout: default
title: Ketoprofen
parent: Solo predicción del modelo (L5)
nav_order: 441
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ketoprofen: nueva indicación predicha, Displasia acromesomélica, tipo Hunter-Thompson (nivel de evidencia L5). Indicación original: Artritis reumatoide…"
monitor_inn: "ketoprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "WHIM syndrome", "juvenile arthritis due to defect in LACC1"]
---

# Ketoprofen
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

# Ketoprofeno: De Artritis Reumatoide a Displasia Acromesomélica tipo Hunter-Thompson

## Resumen en Una Frase

Ketoprofeno es un antiinflamatorio no esteroideo (AINE) utilizado originalmente para la artritis reumatoide, la artrosis y otras artropatías.
El modelo TxGNN predice que podría ser efectivo para la **displasia acromesomélica tipo Hunter-Thompson**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata solo de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis reumatoide, artrosis y artropatía (según las indicaciones del grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Displasia acromesomélica, tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Por conocimiento general, el ketoprofeno es un inhibidor no selectivo de la ciclooxigenasa (COX) que reduce la síntesis de prostaglandinas y, con ello, la inflamación y el dolor. Su eficacia sintomática en enfermedades articulares inflamatorias y degenerativas está bien establecida.

La displasia acromesomélica tipo Hunter-Thompson es una displasia esquelética genética rara, causada por pérdida de función de CDMP1/GDF5, que afecta a la formación del cartílago (condrogénesis). El ketoprofeno no tiene ningún efecto conocido sobre la señalización de GDF5/BMP, por lo que **no se identifica un vínculo mecanístico plausible** con la enfermedad.

El elevado puntaje del modelo probablemente refleja la cercanía en el grafo de conocimiento con fenotipos musculoesqueléticos o articulares compartidos, y no una justificación biológica. Debe interpretarse como una señal computacional sin respaldo clínico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 55857 | ORUDIS 100 mg solución inyectable | Solución inyectable | No disponible en los datos compilados |
| 52097 | ORUDIS 50 mg cápsulas | Cápsula dura | No disponible en los datos compilados |
| 56387 | FASTUM 25 mg/g gel | Gel (tópico) | No disponible en los datos compilados |
| 84336 | OKIDOL 25 mg granulado | Granulado | No disponible en los datos compilados |
| 84337 | OKIDOL 25 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |

Se muestran 5 de las 8 autorizaciones vigentes (todas de monofármaco). Las restantes son FASTUM 50 mg cápsulas duras, ORUDIS RETARD 200 mg comprimidos de liberación prolongada y KETOPROFENO DOMPE 25 mg comprimidos efervescentes.

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no texto de prospecto)**: hipertensión, insuficiencia hepática, enfermedad renal, úlcera péptica (incluida la activa), trastornos de la coagulación, infarto de miocardio, trombosis coronaria, hemoglobinopatía y enfermedad cardiovascular o cardíaca en general.
- **Interacciones Farmacológicas**: se identificaron 226 interacciones. Entre las incluidas en los datos:
  - Moderadas: ácido acetilsalicílico, corticosteroides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), metformina, glimepirida, clorpropamida, mesalazina, balsalazida, naltrexona, citrato y bicarbonato de potasio, ácido picosulfúrico y polietilenglicol con electrolitos.
  - Menores: famotidina, ranitidina, cimetidina y linaclotida.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos, de literatura y de un vínculo mecanístico plausible; el puntaje alto parece deberse a proximidad en el grafo de conocimiento. Con nivel de evidencia L5, no hay base para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del ketoprofeno y análisis de su posible conexión con la vía GDF5/BMP.
- Estudios preclínicos que justifiquen cualquier efecto sobre la condrogénesis.
- Advertencias y contraindicaciones oficiales del prospecto de la AEMPS.
- Valorar otras predicciones del listado con mayor plausibilidad como cuidado de apoyo sintomático (p. ej., espondiloartropatía y artritis juvenil por defecto de LACC1, nivel L4), que requerirían verificación en literatura específica de ketoprofeno.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Cefditoren
parent: Solo predicción del modelo (L5)
nav_order: 155
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Cefditoren: nueva indicación predicha, Susceptibilidad a la osteoartritis (osteoarthritis susceptibility) (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los text…"
---

# Cefditoren
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Cefditoreno: De Indicación Original No Disponible a Susceptibilidad a la Osteoartritis

## Resumen en Una Frase

Cefditoreno es una cefalosporina oral de tercera generación (profármaco pivoxilo) comercializada en España. Los datos compilados para este informe no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **susceptibilidad a la osteoartritis**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Susceptibilidad a la osteoartritis (osteoarthritis susceptibility) |
| Puntaje de Predicción TxGNN | 99,16% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, cefditoreno es una cefalosporina de tercera generación que inhibe la síntesis de la pared celular bacteriana mediante la unión a las proteínas de unión a penicilina (PBP). Esta acción es antibacteriana y no tiene relevancia establecida para la fisiopatología de la osteoartritis (degradación del cartílago, remodelado óseo subcondral e inflamación de bajo grado).

Los datos compilados **no respaldan un vínculo mecanístico**. La predicción se apoya solo en el puntaje elevado del grafo de conocimiento de TxGNN (0,992). Además, "susceptibilidad a la osteoartritis" describe un fenotipo de predisposición genética y no una condición clínica tratable, por lo que la predicción podría reflejar la topología del grafo (genes o vías vecinas compartidas) y no un mecanismo terapéutico real.

Como segunda predicción del modelo aparece la **artritis reumatoide** (puntaje 99,02%), también sin ensayos ni literatura. Tampoco hay un vínculo mecanístico: cefditoreno no tiene actividad inmunomoduladora conocida sobre TNF, IL-6, JAK ni vías de linfocitos T/B. Un uso crónico plantearía además problemas de microbiota, resistencias y depleción de carnitina asociada a profármacos pivoxilo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 65975 | MEIACT 400 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 65943 | MEIACT 200 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 65942 | SPECTRACEF 200 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 65973 | SPECTRACEF 400 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |

Las cuatro autorizaciones están vigentes, son de monofármaco y pertenecen a Meiji Pharma Spain S.A.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 27 interacciones en total, todas de nivel moderado en las que se muestran los datos disponibles. Los grupos principales son:
  - **Antiácidos** (hidróxido de aluminio, carbonato de calcio, magaldrato, carbonato/hidróxido/óxido de magnesio, citrato de sodio, bicarbonato de sodio).
  - **Antagonistas H2** (famotidina, ranitidina, ranitidina con citrato de bismuto, cimetidina, nizatidina).
  - **Inhibidores de la bomba de protones** (omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol, rabeprazol).
  - **Anticoagulante** (dicumarol).

  Los fármacos que reducen la acidez gástrica pueden disminuir la absorción de cefditoreno.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo computacional (nivel L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico plausible entre un antibiótico betalactámico y la osteoartritis o la artritis reumatoide. Además, "susceptibilidad a la osteoartritis" no es una indicación terapéutica clara.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), necesario antes de cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar la indicación original aprobada, ausente en los datos de las autorizaciones.
- Definir una hipótesis mecanística desde cero (p. ej., modelos in vitro/in vivo de inmunomodulación por antibióticos) antes de plantear estudios clínicos.
- Valorar si una indicación más clara, como la artritis reumatoide, o una enfermedad con mejor definición clínica justifica reorientar la evaluación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Adapalene
parent: Solo predicción del modelo (L5)
nav_order: 24
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-05
description: "Adapalene: nueva indicación predicha, Zinc plasmático elevado (nivel de evidencia L5). Indicación original: Acné"
monitor_inn: "Adapalene"
predicted_indications: ["zinc, elevated plasma"]
---

# Adapalene
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Adapaleno: De Acné a Zinc Plasmático Elevado
{: .text-alpha }

## Resumen en Una Frase

Adapaleno es un retinoide de aplicación tópica, utilizado originalmente para el tratamiento del acné.
El modelo TxGNN predice que podría ser efectivo para **zinc plasmático elevado**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Acné |
| Nueva Indicación Predicha | Zinc plasmático elevado |
| Puntaje de Predicción TxGNN | 0.9951 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 2 de 2) |
| Número de Autorizaciones | 2 (comercializadas: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Adapalene (traducción no oficial): «El adapaleno se une a receptores nucleares específicos del ácido retinoico, pero no se une a la proteína receptora citosólica. Los estudios de perfil bioquímico y farmacológico han demostrado que el adapaleno es un modulador de la diferenciación celular, la queratinización y los procesos inflamatorios.» Texto original en inglés: "Adapalene binds to specific retinoic acid nuclear receptors but does not bind to cytosolic receptor protein. Biochemical and pharmacological profile studies have demonstrated that adapalene is a modulator of cellular differentiation, keratinization, and inflammatory processes." ([DailyMed: Differin (adapalene) prescribing information, Galderma Laboratories, L.P.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a0031324-92a6-4c11-90e2-c2818f7278ec), versión del 2023-12-27; consultado el 2026-11-19). Según la información farmacológica conocida, adapaleno es un retinoide sintético que actúa como agonista de los receptores del ácido retinoico, con selectividad por los isotipos RAR-β y RAR-γ frente a RAR-α. Su eficacia en el acné está establecida y se aplica por vía tópica.

Sin embargo, no existe un vínculo mecanístico documentado entre la señalización retinoide y la regulación del zinc plasmático. El puntaje elevado (0.9951) proviene del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Además, el zinc plasmático elevado es un hallazgo de laboratorio y no una enfermedad que suela ser objetivo terapéutico, lo que reduce la plausibilidad clínica de esta indicación. La similitud con la indicación original y la compatibilidad de vías de administración aún no han sido evaluadas.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61066 | DIFFERINE 1 mg/g GEL | Gel | No disponible |
| 66158 | DIFFERINE 1 mg/g CREMA | Crema | No disponible |

Ambas autorizaciones son de monofármaco, están vigentes y pertenecen a Laboratorios Galderma S.A.

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación (según el grafo de conocimiento, no el prospecto)**: respuesta fotoparoxística, enfermedad de fotosensibilidad, dermatitis exfoliativa y dermatitis.
- **Interacciones farmacológicas**: no se identificaron interacciones fármaco-fármaco con nivel de gravedad. Los datos corresponden a la farmacología de dianas: adapaleno se une a RAR-α, RAR-β y RAR-γ, con mayor selectividad por β y γ.

Para información completa de advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única base es el puntaje del modelo (nivel L5), sin ensayos clínicos, sin literatura y sin mecanismo plausible que vincule los retinoides con el zinc plasmático. Además, la indicación predicha es un hallazgo analítico y no una enfermedad tratable.

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank
- Advertencias y contraindicaciones del prospecto de AEMPS (obtener y analizar el PDF)
- Revisión bibliográfica para buscar cualquier asociación entre retinoides y homeostasis del zinc
- Evaluación de la relevancia clínica de la indicación y de la compatibilidad de vía de administración (adapaleno es tópico, con exposición sistémica baja)
- Descartar posibles artefactos del modelo TxGNN (aprendizaje profundo) en la predicción

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Differin (adapalene) prescribing information, Galderma Laboratories, L.P.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a0031324-92a6-4c11-90e2-c2818f7278ec) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


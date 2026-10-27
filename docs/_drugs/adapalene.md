---
layout: default
title: Adapalene
parent: Solo predicción del modelo (L5)
nav_order: 24
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
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
| Puntaje de Predicción TxGNN | 99.51% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información farmacológica conocida, adapaleno es un retinoide sintético que actúa como agonista de los receptores del ácido retinoico, con selectividad por los isotipos RAR-β y RAR-γ frente a RAR-α. Su eficacia en el acné está establecida y se aplica por vía tópica.

Sin embargo, no existe un vínculo mecanístico documentado entre la señalización retinoide y la regulación del zinc plasmático. El puntaje elevado (0.995) probablemente refleja la topología del grafo de conocimiento (por ejemplo, conexiones compartidas con genes relacionados con el zinc) más que una relación biológica validada.

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
- Descartar posibles artefactos del grafo de conocimiento en la predicción
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


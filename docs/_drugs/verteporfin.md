---
layout: default
title: Verteporfin
parent: Solo predicción del modelo (L5)
nav_order: 845
evidence_level: L5
indication_count: 1
---

# Verteporfin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Verteporfina: De Degeneración Macular a Trastorno de la Fosforilación Oxidativa Mitocondrial por Anomalías del ADN Nuclear

## Resumen en Una Frase

Verteporfina es un fotosensibilizador utilizado en terapia fotodinámica, originalmente indicado para la degeneración macular.
El modelo TxGNN predice que podría ser efectivo para el **trastorno de la fosforilación oxidativa mitocondrial por anomalías del ADN nuclear**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Degeneración macular (según el grafo de conocimiento; el texto de indicación autorizado en España no está disponible) |
| Nueva Indicación Predicha | Trastorno de la fosforilación oxidativa mitocondrial por anomalías del ADN nuclear |
| Puntaje de Predicción TxGNN | 99,49% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, la verteporfina es un fotosensibilizador que, al activarse con luz (terapia fotodinámica), genera especies reactivas de oxígeno (ROS) y provoca oclusión vascular localizada, lo que explica su eficacia en la degeneración macular neovascular. Además, estudios preclínicos han descrito una inhibición de la interacción YAP-TEAD independiente de la luz.

No se ha establecido un vínculo directo entre estos mecanismos y los defectos de la fosforilación oxidativa codificados por ADN nuclear. Una conexión especulativa podría pasar por vías de estrés oxidativo o función mitocondrial, pero la generación de ROS podría incluso agravar una función mitocondrial ya comprometida en esta enfermedad.

Por tanto, la predicción se apoya únicamente en una asociación derivada del grafo de conocimiento. Es una hipótesis sin contrastar y sin respaldo en los datos compilados para este informe.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 00140001 | VISUDYNE 15 MG POLVO PARA SOLUCIÓN PARA PERFUSIÓN (Cheplapharm Arzneimittel GmbH) | Polvo para solución para perfusión | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): porfiria hereditaria, enfermedad del metabolismo de las porfirinas, porfiria, enfermedad hepática y enfermedad de la vesícula biliar.
- **Interacciones farmacológicas**: se identificaron 117 interacciones en total; se muestra una muestra de 20, en su mayoría de nivel moderado:
  - **Tetraciclinas** (doxiciclina, tetraciclina, minociclina, incluidas formas tópicas): moderada.
  - **Sulfonilureas** (clorpropamida, glimepirida, glipizida, gliburida, tolazamida, acetohexamida, tolbutamida): moderada.
  - **Otros**: ácido acetilsalicílico, levofloxacino, manitol, sulfasalazina, betacaroteno y papaverina (moderada); polimixina B (leve).

Para advertencias y contraindicaciones del prospecto, consultar la ficha técnica autorizada por la AEMPS.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción (99,49%) no cuenta con ensayos clínicos ni literatura de apoyo (nivel L5). Además, el mecanismo fotodinámico generador de ROS podría ser perjudicial en una enfermedad mitocondrial, y no se dispone de la información de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto/ficha técnica de la AEMPS (advertencias y contraindicaciones), imprescindible para cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, consultando DrugBank) y analizar el vínculo mecanístico con la nueva indicación.
- Realizar una revisión de literatura y estudios preclínicos (modelos celulares de disfunción mitocondrial) que evalúen si la verteporfina es beneficiosa o perjudicial.
- Evaluar la compatibilidad de la vía de administración (perfusión intravenosa con activación lumínica local) con una enfermedad mitocondrial sistémica.
- Valorar el riesgo de las contraindicaciones del grafo (porfiria, enfermedad hepática) en la población objetivo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


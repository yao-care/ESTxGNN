---
layout: default
title: Verteporfin
parent: Solo predicción del modelo (L5)
nav_order: 845
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "verteporfin"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies"]
description: "Verteporfin: nueva indicación predicha, Trastorno de la fosforilación oxidativa mitocondrial por anomalías del ADN nuclear (mitochondrial oxidative phosphoryla… (nivel de evidencia L5). Indicación or…"
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Verteporfin: Trastorno de la fosforilación oxidativa mitocondrial por anomalías del ADN nuclear (mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies)
{: .text-alpha }

## Resumen en Una Frase

Verteporfina es un fotosensibilizador utilizado en terapia fotodinámica, originalmente indicado para la degeneración macular.
El modelo TxGNN predice que podría ser efectivo para el **trastorno de la fosforilación oxidativa mitocondrial por anomalías del ADN nuclear**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Trastorno de la fosforilación oxidativa mitocondrial por anomalías del ADN nuclear (mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies) |
| Puntaje de Predicción TxGNN | 0.9949 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Verteporfin es (traducción no oficial): «Inhibidor del ADN». Texto original en inglés: "DNA inhibitor" ([ChEMBL CHEMBL5314346 (verteporfin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL5314346), CC BY-SA 3.0; consultado el 2026-11-19). Según la información conocida, la verteporfina es un fotosensibilizador que, al activarse con luz (terapia fotodinámica), genera especies reactivas de oxígeno (ROS) y provoca oclusión vascular localizada, lo que explica su eficacia en la degeneración macular neovascular. Además, estudios preclínicos han descrito una inhibición de la interacción YAP-TEAD independiente de la luz.

No se ha establecido un vínculo directo entre estos mecanismos y los defectos de la fosforilación oxidativa codificados por ADN nuclear. Una conexión especulativa podría pasar por vías de estrés oxidativo o función mitocondrial, pero la generación de ROS podría incluso agravar una función mitocondrial ya comprometida en esta enfermedad.

Por tanto, la predicción se apoya únicamente en la puntuación del modelo TxGNN (aprendizaje profundo), que puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica. Es una hipótesis sin contrastar y sin respaldo en los datos compilados para este informe.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 00140001 | VISUDYNE 15 MG POLVO PARA SOLUCION PARA PERFUSION | POLVO PARA SOLUCIÓN PARA PERFUSIÓN | Cheplapharm Arzneimittel Gmbh | Comercializada |

Se muestra la única autorización con este principio activo en los datos de CIMA (AEMPS).

<!-- licenses:end -->

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
La predicción (0.9949) no cuenta con ensayos clínicos ni literatura de apoyo (nivel L5). Además, el mecanismo fotodinámico generador de ROS podría ser perjudicial en una enfermedad mitocondrial, y no se dispone de la información de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto/ficha técnica de la AEMPS (advertencias y contraindicaciones), imprescindible para cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, consultando DrugBank) y analizar el vínculo mecanístico con la nueva indicación.
- Realizar una revisión de literatura y estudios preclínicos (modelos celulares de disfunción mitocondrial) que evalúen si la verteporfina es beneficiosa o perjudicial.
- Evaluar la compatibilidad de la vía de administración (perfusión intravenosa con activación lumínica local) con una enfermedad mitocondrial sistémica.
- Valorar el riesgo de las contraindicaciones del grafo (porfiria, enfermedad hepática) en la población objetivo.

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente (revisado el 2026-11-20; la versión anterior se guarda en el registro) | [ChEMBL CHEMBL5314346 (verteporfin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL5314346) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


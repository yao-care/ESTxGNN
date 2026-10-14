---
layout: default
title: Nefopam
parent: Solo predicción del modelo (L5)
nav_order: 557
evidence_level: L5
indication_count: 10
---

# Nefopam
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

# Nefopam: De Analgésico (indicación original no registrada) a Estenosis Espinal Lumbar

## Resumen en Una Frase

Nefopam es un analgésico no opioide de acción central, comercializado en España en forma inyectable, cuyo texto de indicación aprobada no figura en los datos compilados para este informe.
La predicción principal del modelo TxGNN (craniostenosis con catarata) carece de todo respaldo, por lo que este informe se centra en la **Estenosis Espinal Lumbar**, la única predicción con literatura real (**4 publicaciones**, **ningún ensayo clínico registrado**).

> **Nota sobre la selección de la indicación:** la predicción de mayor rango (*craniostenosis cataract*) y las otras ocho predicciones de catarata no tienen ensayos ni literatura y comparten un puntaje idéntico o casi idéntico, lo que sugiere una señal genérica del grafo. Por ello se presenta como candidata más relevante la estenosis espinal lumbar (rango 10), que sí cuenta con evidencia.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (el texto de indicación de la autorización está vacío) |
| Nueva Indicación Predicha | Estenosis espinal lumbar (*lumbar spinal stenosis*) |
| Puntaje de Predicción TxGNN | 99,97% |
| Nivel de Evidencia | L4 (conservador; ver justificación) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold (mantener en espera; pregunta de investigación) |

Para las predicciones de catarata (puntajes entre 99,97% y 99,98%), el nivel de evidencia es L5 y la decisión es Hold.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos compilada. Según la información conocida, nefopam es un analgésico de acción central, no opioide, que inhibe la recaptación de serotonina, noradrenalina y dopamina, y modula los canales de sodio y calcio dependientes de voltaje.

En la estenosis espinal lumbar existe un vínculo plausible a través de su acción analgésica: podría reducir el dolor de tipo neuropático y la disestesia, y ahorrar opioides en el periodo perioperatorio de la cirugía de columna. Cabe subrayar que la evidencia disponible se refiere al control sintomático perioperatorio (dolor, disestesia, consumo de opioides) y no a una modificación de la enfermedad.

Para las predicciones de catarata no se identificó ningún vínculo mecanístico. El puntaje idéntico entre subtipos de catarata indica una señal inespecífica del grafo, no una señal específica de enfermedad.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38068520](https://pubmed.ncbi.nlm.nih.gov/38068520/) | 2023 | Estudio clínico aleatorizado doble ciego (73 pacientes) | Journal of Clinical Medicine | Evalúa nefopam (20 mg) frente a suero salino sobre disestesia, dolor posoperatorio y satisfacción en pacientes con estenosis lumbar sometidos a cirugía de columna |
| [41937571](https://pubmed.ncbi.nlm.nih.gov/41937571/) | 2026 | ECA doble ciego controlado con placebo | Asian Spine Journal | Efecto ahorrador de opioides de nefopam intravenoso continuo tras fusión lumbar degenerativa multinivel |
| [31166320](https://pubmed.ncbi.nlm.nih.gov/31166320/) | 2019 | Estudio clínico (diseño no confirmado) | Zhurnal Voprosy Neirokhirurgii | Efecto de distintos regímenes de analgesia multimodal en cirugía de estenosis espinal sobre la tasa de síndrome de cirugía fallida de espalda |
| [25535527](https://pubmed.ncbi.nlm.nih.gov/25535527/) | 2014 | Reporte de caso | Journal of Korean Neurosurgical Society | Estatus epiléptico atribuido a nefopam en un paciente de 71 años operado de estenosis lumbar (señal de seguridad) |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 90988 | NEPHODOL 20 MG/2 ML SOLUCIÓN INYECTABLE EFG (Altan Pharmaceuticals S.A.) | Solución inyectable | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Advertencias Principales:** el reporte de caso de estatus epiléptico (PMID 25535527) constituye una señal de seguridad neurológica. Las reacciones neurológicas descritas para nefopam incluyen confusión, alucinaciones, delirio y convulsiones; también se describen efectos anticolinérgicos y cardiovasculares.

No se dispone de datos de contraindicaciones del prospecto ni de interacciones farmacológicas (consulta sin resultados). Consultar el prospecto para información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La estenosis espinal lumbar cuenta con dos estudios aleatorizados recientes sobre control del dolor perioperatorio, pero no con ensayos registrados, y el diseño de parte de la literatura no está confirmado. Por ello el nivel se fija prudentemente en L4. Las predicciones de catarata son solo predicciones del modelo (L5) sin vínculo mecanístico. Además, existe una señal de seguridad convulsiva.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un vacío de datos bloqueante para el cribado de seguridad.
- Completar los datos de mecanismo de acción desde DrugBank.
- Confirmar el diseño y los resultados de los estudios publicados (PMID 38068520, 41937571) y su relevancia clínica.
- Aclarar que el uso propuesto es sintomático perioperatorio y no modificador de la enfermedad, y definir límites de dosis y selección de pacientes (p. ej., antecedentes convulsivos).
- Descartar o desestimar formalmente las predicciones de catarata salvo que aparezca evidencia específica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


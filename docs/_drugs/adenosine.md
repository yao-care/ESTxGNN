---
layout: default
title: Adenosine
parent: Solo predicción del modelo (L5)
nav_order: 25
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Adenosine: nueva indicación predicha, Bloqueo de rama (término obsoleto) (nivel de evidencia L5). Indicación original: Taquicardia ventricular (según el grafo de conocimiento"
monitor_inn: "Adenosine"
predicted_indications: ["obsolete bundle branch block"]
---

# Adenosine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Adenosina: De Taquicardia Ventricular a Bloqueo de Rama (término obsoleto)
{: .text-alpha }

## Resumen en Una Frase

La adenosina es un nucleósido de uso intravenoso, originalmente empleado en el tratamiento de las taquicardias (en la base de conocimiento figura la taquicardia ventricular).
El modelo TxGNN predice que podría ser efectiva para **bloqueo de rama (término obsoleto en la ontología)**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección, por lo que se trata solo de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Taquicardia ventricular (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no constan en los datos compilados) |
| Nueva Indicación Predicha | Bloqueo de rama (término obsoleto) |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 7 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente original. Según la información farmacológica compilada, la adenosina actúa sobre los receptores de adenosina A1, A2A, A2B y A3, y también se relaciona con TRPM4 y con las fosfatidilinositol 4-quinasas tipo 2 alfa y beta. Su efecto sobre la conducción del nodo auriculoventricular, mediado por el receptor A1, es la base de su uso en taquicardias.

Esta predicción **no resulta convincente desde el punto de vista mecanístico**. El efecto de la adenosina sobre la conducción es un efecto farmacológico, no una justificación terapéutica para el bloqueo de rama. De hecho, la adenosina puede provocar o desenmascarar bloqueos de la conducción, por lo que un beneficio terapéutico no es plausible sin evidencia adicional. Además, el término de la enfermedad está marcado como obsoleto, lo que sugiere una entrada desactualizada de la ontología que puede corresponderse mal con una entidad clínica actual. El puntaje alto del modelo (99.94%) no compensa la falta de respaldo clínico o bibliográfico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Hay 7 autorizaciones vigentes (todas de medicamentos con un único principio activo, ninguna cancelada). Se muestran las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 60375 | ADENOCOR 6 mg/2 ml (Sanofi Aventis) | Solución inyectable | No consta en los datos compilados |
| 61732 | ADENOSCAN 30 mg/10 ml (Sanofi Aventis) | Solución para perfusión | No consta en los datos compilados |
| 81545 | ADENOSINA ACCORD 6 mg/2 ml EFG | Solución inyectable | No consta en los datos compilados |
| 81546 | ADENOSINA ACCORD 30 mg/10 ml EFG | Solución para perfusión | No consta en los datos compilados |
| 86371 | ADENOSINA HIKMA 6 mg/2 ml EFG | Solución inyectable | No consta en los datos compilados |

---

## Consideraciones de Seguridad

No se dispone de advertencias ni contraindicaciones extraídas del prospecto. Consultar el prospecto para la información de seguridad oficial.

Como dato orientativo, el grafo de conocimiento (no el texto del prospecto) asocia la adenosina con contraindicaciones en las siguientes condiciones:
- **Respiratorias:** enfermedad pulmonar obstructiva crónica (EPOC), asma (intrínseco y alérgico), enfisema pulmonar, insuficiencia respiratoria.
- **Cardiovasculares:** estenosis aórtica (incluida la valvular y la supravalvular), enfermedad de la válvula aórtica, estenosis mitral, insuficiencia de la válvula pulmonar, síndrome coronario agudo, enfermedad arterial coronaria, pericarditis, trastornos hipotensivos.
- **Del ritmo y la conducción:** bloqueo auriculoventricular, síndrome del seno enfermo (incluida la forma familiar).
- **Otras:** enfermedad del sistema nervioso autónomo, síndrome de Horner.

Es especialmente relevante la asociación con el bloqueo auriculoventricular y el síndrome del seno enfermo, por su cercanía con la indicación predicha.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos clínicos ni literatura. El término de la enfermedad es obsoleto y la adenosina puede provocar bloqueos de conducción, por lo que no hay un fundamento terapéutico plausible.

**Para avanzar se necesita:**
- Aclarar a qué entidad clínica vigente corresponde el término "bloqueo de rama (obsoleto)" y reevaluar la predicción con esa entidad.
- Obtener el mecanismo de acción detallado y las advertencias y contraindicaciones del prospecto de la AEMPS.
- Contar con estudios preclínicos o clínicos que respalden algún beneficio en trastornos de la conducción.

**Nota sobre otra predicción:** la segunda predicción del modelo, **taquicardia ventricular polimórfica catecolaminérgica (TVPC)**, tiene un puntaje de 99.42% y nivel de evidencia L4. Cuenta con 10 publicaciones recuperadas, aunque la mayoría aporta solo apoyo indirecto (fisiopatología, pruebas de provocación, manejo general de arritmias). La única señal clínica directa es un reporte de caso de 2008 (PMID 18313614) en el que el trifosfato de adenosina terminó una taquicardia ventricular bidireccional en un paciente con TVPC. Es una observación de terminación aguda, no evidencia de beneficio terapéutico sostenido. No hay ensayos clínicos registrados. Esta indicación es más plausible mecanísticamente y se considera una pregunta de investigación, no una candidata lista para avanzar.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


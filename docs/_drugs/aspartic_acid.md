---
layout: default
title: Aspartic Acid
parent: Solo predicción del modelo (L5)
nav_order: 70
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Aspartic Acid: nueva indicación predicha, Acidosis tubular renal (nivel de evidencia L5). Indicación original: Deficiencia de potasio (según el grafo de conocimiento de TxGNN"
---

# Aspartic Acid
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

# Ácido aspártico: De Deficiencia de Potasio a Acidosis Tubular Renal

## Resumen en Una Frase

El ácido aspártico es un aminoácido no esencial que se utiliza como sal de potasio y magnesio, originalmente para tratar la deficiencia de potasio.
El modelo TxGNN predice que podría ser efectivo para **acidosis tubular renal**,
pero actualmente no hay **ensayos clínicos** y solo hay **4 publicaciones**, ninguna de las cuales demuestra un papel terapéutico del fármaco en esta enfermedad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Deficiencia de potasio (según el grafo de conocimiento de TxGNN; el texto de indicación de la autorización de AEMPS no está disponible) |
| Nueva Indicación Predicha | Acidosis tubular renal |
| Puntaje de Predicción TxGNN | 99,47% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el ácido aspártico es un aminoácido no esencial que se emplea como sal de potasio y magnesio para corregir la deficiencia de potasio, y su utilidad en esa indicación es la base de su uso actual.

La acidosis tubular renal es un trastorno del manejo renal del equilibrio ácido-base (por ejemplo, mutaciones del intercambiador aniónico SLC4A1 en la forma distal). Una posible relación teórica sería la reposición de potasio, dado que la hipopotasemia es frecuente en la acidosis tubular renal distal, o bien una conexión con la amoniogénesis y el metabolismo de aminoácidos.

Esta vinculación es **especulativa** y no está respaldada por la evidencia recuperada. El tratamiento estándar establecido es la terapia alcalinizante (bicarbonato o citrato), y no se espera que el ácido aspártico corrija la acidosis de fondo. El puntaje del modelo es muy alto, pero por sí solo no sustituye a la evidencia real.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20068363](https://pubmed.ncbi.nlm.nih.gov/20068363/) | 2010 | Serie de casos / genética | Nephron Physiology | Describe las características clínicas y la base genética (gen SLC4A1) de la acidosis tubular renal distal en niños filipinos |
| [26208211](https://pubmed.ncbi.nlm.nih.gov/26208211/) | 2015 | Estudio diagnóstico | Jornal de Pediatria | Uso de secuenciación del exoma completo para el diagnóstico genético de cuatro niños con acidosis tubular renal distal |
| [6422151](https://pubmed.ncbi.nlm.nih.gov/6422151/) | 1983 | Reporte de caso | Journal of Inherited Metabolic Disease | Déficit neonatal de piruvato carboxilasa con acidosis tubular renal proximal y cistinuria; el paciente mejoró al suplementar la dieta con aspártico, asparagina y otros aminoácidos, en un contexto metabólico muy particular |
| [14301365](https://pubmed.ncbi.nlm.nih.gov/14301365/) | 1965 | Estudio de fisiología básica | The American Journal of Physiology | Relación entre el pNH3 de las células tubulares y la producción renal de amoníaco (sin resumen disponible) |

Ninguna de estas publicaciones evalúa el ácido aspártico como tratamiento de la acidosis tubular renal; describen genética, diagnóstico y fisiología.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 48924 | BOI-K ASPARTICO COMPRIMIDOS EFERVESCENTES (Ionfarma S.L.) | Comprimido efervescente | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

Según el grafo de conocimiento, el fármaco se asocia con contraindicación en las siguientes enfermedades (no proviene del texto del prospecto):
- Enfermedad renal
- Piouréter
- Enfermedad diarreica, incluida la diarrea crónica
- Bloqueo auriculoventricular
- Parálisis periódica hiperpotasémica y parálisis periódica
- Hipoaldosteronismo
- Miotonía congénita
- Gastroparesia

No se encontraron interacciones farmacológicas en los datos compilados. Consultar el prospecto para el resto de la información de seguridad.

Cabe destacar que varias de estas condiciones (enfermedad renal, hiperpotasemia, bloqueo AV) son relevantes en un paciente con acidosis tubular renal tratado con una sal de potasio.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5): no hay ensayos clínicos y la literatura no respalda un papel terapéutico del ácido aspártico. Además, existe un tratamiento estándar eficaz (alcalinizantes) y varias contraindicaciones del grafo de conocimiento son relevantes para esta población.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de AEMPS (advertencias y contraindicaciones), cuya ausencia impide el cribado de seguridad
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank)
- Documentar un fundamento mecanístico sólido (potasio, amoniogénesis) con estudios preclínicos o clínicos
- Evaluar la seguridad en pacientes con función renal alterada e hiperpotasemia
- Comparar con la terapia alcalinizante estándar antes de plantear cualquier estudio
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


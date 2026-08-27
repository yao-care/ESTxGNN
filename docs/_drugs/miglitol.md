---
layout: default
title: Miglitol
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
---

# Miglitol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Miglitol: De Diabetes Mellitus Tipo 2 a Diabetes Mellitus Tipo 1 (Terapia Adjunta a Insulina)

> **Nota metodológica**: TxGNN generó 10 indicaciones candidatas para miglitol. Las 9 de mayor puntuación (rango 1–9: síndrome de la persona rígida, distrofias/lipodistrofias localizadas, agenesia pancreática, etc.) carecen por completo de ensayos clínicos y literatura de respaldo, y sus propias justificaciones mecanísticas declaran explícitamente "sin relación conocida" con el mecanismo de miglitol (nivel L5, recomendación Hold). Por ello, este informe se centra en la única indicación con evidencia real: **Diabetes Mellitus Tipo 1** (rango 10), la candidata clínicamente relevante del conjunto.

## Resumen en Una Frase

Miglitol es un inhibidor de la alfa-glucosidasa intestinal, utilizado originalmente en el control de la diabetes mellitus tipo 2 al retrasar la absorción de carbohidratos. El modelo TxGNN, junto con literatura clínica acumulada desde los años 1980, sugiere su uso como **terapia adjunta a la insulina en Diabetes Mellitus Tipo 1**, respaldado por **16 publicaciones** aunque sin ensayos registrados formalmente en clinicaltrials.gov.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en registro español (miglitol no está comercializado en España); según la literatura recopilada, su uso conocido es como antidiabético oral (inhibidor de alfa-glucosidasa) |
| Nueva Indicación Predicha | Diabetes Mellitus Tipo 1 (terapia adjunta a insulina) |
| Puntaje de Predicción TxGNN | 99.60% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

Los datos estructurados de mecanismo de acción (MOA) no están disponibles en la ficha del fármaco (data gap de prioridad alta). Sin embargo, la literatura recopilada en este mismo informe describe de forma consistente a miglitol como un **inhibidor de la alfa-glucosidasa intestinal**, que retrasa la degradación de disacáridos y la absorción de glucosa en el intestino delgado, reduciendo el pico glucémico postprandial (ver PMID 2060451, 3130257, 3286168, entre otros).

Miglitol fue desarrollado y usado clásicamente en diabetes mellitus tipo 2. La indicación predicha por TxGNN —diabetes mellitus tipo 1— no reemplaza a la insulina, sino que la complementa: en pacientes tipo 1, incluso con terapia insulínica intensiva, persisten picos glucémicos postprandiales difíciles de controlar. Al enlentecer la absorción intestinal de carbohidratos, miglitol podría suavizar estos picos y facilitar el ajuste del momento de administración de insulina.

Esta hipótesis mecanística es razonable y no depende de una analogía forzada de enfermedad, sino de un mecanismo fisiológico directo (metabolismo de carbohidratos) aplicado a un subtipo relacionado de la misma enfermedad de base (diabetes). De hecho, la evidencia acumulada abarca más de tres décadas (1986–2020), lo que indica un interés clínico sostenido, aunque nunca consolidado en un ensayo de fase 3 a gran escala.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en clinicaltrials.gov/ICTRP. La evidencia disponible proviene exclusivamente de estudios clínicos pequeños publicados directamente en literatura biomédica (ver tabla siguiente), en su mayoría anteriores a la era de registro obligatorio de ensayos.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21869539](https://pubmed.ncbi.nlm.nih.gov/21869539/) | 2011 | ECA (pequeña escala) | Endocrine Journal | 11 pacientes T1DM en terapia insulínica intensiva; miglitol (25→50 mg, 3x/día) evaluado sobre control glucémico, hipoglucemia y respuesta de incretinas |
| [24843410](https://pubmed.ncbi.nlm.nih.gov/24843410/) | 2010 | Ensayo Clínico | Journal of Diabetes Investigation | Terapia combinada miglitol + insulina en pacientes con T1DM; beneficio en picos glucémicos postprandiales no controlados por insulina sola |
| [2060451](https://pubmed.ncbi.nlm.nih.gov/2060451/) | 1991 | Ensayo Clínico | Diabetes Care | Efecto de la inhibición de alfa-glucosidasa sobre tolerancia a glucosa y momento de administración de insulina en diabetes tipo 1 |
| [8261749](https://pubmed.ncbi.nlm.nih.gov/8261749/) | 1993 | Ensayo Clínico/Revisión | Diabetic Medicine | Inhibición de alfa-glucosidasa como adyuvante al tratamiento de diabetes tipo 1 |
| [3130257](https://pubmed.ncbi.nlm.nih.gov/3130257/) | 1988 | Ensayo Clínico | European Journal of Clinical Investigation | Administración prolongada de dos inhibidores de alfa-glucosidasa (incl. precursor de miglitol) en diabetes insulinodependiente: mejora glucémica y reducción de requerimiento de insulina |
| [3286168](https://pubmed.ncbi.nlm.nih.gov/3286168/) | 1988 | Ensayo Clínico | Diabetes Research and Clinical Practice | Momento óptimo de insulina preprandial combinada con inhibición de alfa-glucosidasa en IDDM |
| [11460577](https://pubmed.ncbi.nlm.nih.gov/11460577/) | 2001 | Revisión | Exp Clin Endocrinol Diabetes | Revisión de hipoglucemiantes orales incluyendo inhibidores de alfa-glucosidasa |
| [12073790](https://pubmed.ncbi.nlm.nih.gov/12073790/) | 2002 | Revisión | Revue Médicale de Liège | Abordajes farmacológicos de la hiperglucemia postprandial, incluyendo acarbosa y miglitol |
| [33268615](https://pubmed.ncbi.nlm.nih.gov/33268615/) | 2020 | Reporte de caso | Journal of UOEH | Paciente T1DM en tratamiento con miglitol + insulina; adición de inhibidor SGLT2 mejoró hiperglucemia nocturna |
| [20307399](https://pubmed.ncbi.nlm.nih.gov/20307399/) | 2010 | Revisión | Journal of Diabetes Science and Technology | Revisión de dinámica de aporte de glucosa y demanda de insulina entre agentes antidiabéticos |

## Consideraciones de Seguridad

No se dispone de ficha técnica ni prospecto para miglitol, dado que el fármaco no está comercializado en España (0 autorizaciones). Adicionalmente, la obtención del prospecto TFDA/regulador de origen con advertencias y contraindicaciones está identificada como **brecha de datos bloqueante** (impide la evaluación de seguridad inicial S1). No hay datos de interacciones farmacológicas disponibles (búsqueda DDI: sin resultados).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el mecanismo de acción (inhibición de alfa-glucosidasa) es fisiológicamente plausible para diabetes tipo 1 y existe un cuerpo histórico de estudios clínicos pequeños (nivel L3), no hay ningún ensayo de fase 2/3 completado ni registrado formalmente, el fármaco no está comercializado en España, y falta información de seguridad esencial (advertencias/contraindicaciones), lo cual bloquea la evaluación de seguridad inicial.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica oficial (regulador de origen o AEMPS) con advertencias y contraindicaciones — brecha bloqueante
- Confirmar el mecanismo de acción formal vía consulta a DrugBank API
- Explorar diseño de un ensayo clínico controlado y registrado (fase 2/3) específico para diabetes tipo 1 como terapia adjunta
- Evaluar la viabilidad regulatoria de introducción en el mercado español, dado que actualmente no existe ninguna autorización
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


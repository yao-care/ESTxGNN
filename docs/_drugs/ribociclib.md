---
layout: default
title: Ribociclib
parent: 僅模型預測 (L5)
nav_order: 243
evidence_level: L5
indication_count: 4
---

# Ribociclib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Usando el Evidence Pack proporcionado, aquí está el informe de evaluación:

---

# Ribociclib: De Cáncer de Mama HR+/HER2- Metastásico a Leucemia Mieloide

## Resumen en Una Frase

Ribociclib es un inhibidor de CDK4/6 cuya eficacia está documentada en la literatura clínica para el cáncer de mama HR+/HER2- avanzado o metastásico (no hay un registro formal de indicación en España, ya que el fármaco no está comercializado en este mercado). El modelo TxGNN predice que podría ser efectivo para **Leucemia Mieloide**, con **0 ensayos clínicos** y **3 publicaciones** que actualmente respaldan esta dirección, entre las cuales existe evidencia contradictoria sobre si el fármaco trata o, en realidad, podría inducir esta enfermedad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de mama HR+/HER2- (receptor hormonal positivo, HER2 negativo) avanzado o metastásico* |
| Nueva Indicación Predicha | Leucemia Mieloide |
| Puntaje de Predicción TxGNN | 99.35% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

\* *No existe un registro regulatorio formal en España (el fármaco no está comercializado); esta indicación se ha derivado de la literatura clínica incluida en el Evidence Pack.*

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) de ribociclib procedentes de una fuente regulatoria verificada — este es un vacío de datos de prioridad **alta** (DG002) que debe resolverse antes de avanzar. Según la información disponible en la literatura incluida en este Evidence Pack, ribociclib es un inhibidor selectivo de las quinasas dependientes de ciclina 4 y 6 (CDK4/6), cuya eficacia en cáncer de mama HR+/HER2- ha sido comprobada en múltiples ensayos clínicos.

La hipótesis mecanística para la leucemia mieloide es la siguiente: los inhibidores de CDK4/6 podrían, en teoría, bloquear el ciclo celular (deteniéndolo en fase G1) y así inhibir la proliferación de blastos leucémicos — hipótesis respaldada por **1 estudio preclínico**. Sin embargo, existe simultáneamente **1 reporte de caso** que describe la aparición de leucemia mieloide aguda con eosinofilia *después* del tratamiento con un inhibidor de CDK4/6 (usado para cáncer de mama), sugiriendo que podría tratarse de una neoplasia hematológica secundaria relacionada con el fármaco, y no de un beneficio terapéutico.

Estas dos líneas de evidencia apuntan en direcciones mecanísticas opuestas (el fármaco como posible tratamiento vs. el fármaco como posible causa), y no existe ningún ensayo clínico que valide un efecto terapéutico real. Por ello, la evidencia actual es insuficiente para sostener la hipótesis y presenta, además, una señal de seguridad potencial que debe vigilarse.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|---------|------------------------|
| [32560251](https://pubmed.ncbi.nlm.nih.gov/32560251/) | 2020 | Preclínico/In vitro | Cancers | Estudio in vitro sobre inhibidores de CDK4/6 para superar la resistencia farmacocinética en células de leucemia mieloide aguda (LMA), asociada a sobreexpresión de transportadores ABCB1/ABCG2 y enzimas reductoras de carbonilo que metabolizan antraciclinas. |
| [30575100](https://pubmed.ncbi.nlm.nih.gov/30575100/) | 2019 | Reporte de Caso | American Journal of Hematology | Caso de leucemia mieloide aguda con eosinofilia tras tratamiento con inhibidor de CDK4/6 (indicación original: cáncer de mama), atribuido a hematopoyesis clonal de potencial indeterminado (CHIP) subyacente — sugiere un evento adverso relacionado con el fármaco, no un beneficio terapéutico. |
| [41641105](https://pubmed.ncbi.nlm.nih.gov/41641105/) | 2026 | Reporte de Caso | Frontiers in Oncology | Caso de adenocarcinoma tipo glándula mamaria de la vulva concomitante con cáncer de mama; el resumen disponible no menciona leucemia mieloide ni ribociclib. Relevancia incierta para esta indicación (posible error de indexación en la búsqueda bibliográfica). |

---

## Información de Mercado en España

Ribociclib no dispone actualmente de autorización de comercialización en España (0 registros). No es posible presentar una tabla de autorizaciones al no existir datos de licencias.

---

## Citotoxicidad

Ribociclib se clasifica como fármaco antineoplásico (indicación original en oncología — cáncer de mama), por lo que aplica esta sección.

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor selectivo de CDK4/6) |
| Riesgo de Mielosupresión | Alto — la literatura describe neutropenia, leucopenia y trombocitopenia como los eventos adversos hematológicos más frecuentes, constituyendo toxicidad limitante de dosis (DLT) en ensayos de fase I |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma completo (con diferencial, especialmente neutrófilos y plaquetas), función hepática y ECG (se ha reportado prolongación del intervalo QT en la literatura) |
| Protección en Manejo | Al tratarse de un antineoplásico oral, se recomienda seguir las normativas estándar de manejo de fármacos citotóxicos/peligrosos para su dispensación y administración |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La evidencia para "Leucemia Mieloide" es de nivel L4 (solo 1 estudio preclínico), sin ningún ensayo clínico, y con una señal contradictoria en la literatura (un caso sugiere que el mecanismo podría inducir la enfermedad en lugar de tratarla). La dirección mecanística no está resuelta, por lo que no se recomienda avanzar sin más validación.
- Las demás indicaciones predichas para ribociclib en este ciclo de evaluación fueron revisadas y descartadas: **trombocitopenia** corresponde a una toxicidad hematológica ya conocida del fármaco (no una indicación terapéutica — dirección causal invertida), y **"macrotrombocitopenia con insuficiencia mitral"** y **"trombocitopenia hereditaria con plaquetas normales"** son enfermedades genéticas raras sin ningún respaldo mecanístico ni evidencia clínica o bibliográfica.

**Para avanzar se necesita:**
- Datos del prospecto de TFDA/EMA (advertencias y contraindicaciones) — actualmente es un vacío de datos bloqueante (DG001) que impide la evaluación de seguridad inicial (S1)
- Datos detallados del mecanismo de acción (MOA) verificados con fuente regulatoria (DrugBank) (DG002)
- Estudios preclínicos adicionales en modelos específicos de leucemia mieloide que resuelvan la contradicción mecanística observada
- Al menos un ensayo clínico (fase 1/2) que evalúe ribociclib específicamente en leucemia mieloide antes de reconsiderar el nivel de evidencia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


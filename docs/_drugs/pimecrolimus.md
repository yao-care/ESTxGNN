---
layout: default
title: Pimecrolimus
parent: Evidencia alta (L1-L2)
nav_order: 424
evidence_level: L2
indication_count: 4
---

# Pimecrolimus
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **4** 
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

# Pimecrolimus: De Dermatitis Atópica a Dermatitis Seborreica

## Resumen en Una Frase

Pimecrolimus es un inhibidor tópico de la calcineurina, conocido por su uso en dermatitis atópica leve a moderada. El modelo TxGNN predice que podría ser efectivo para **dermatitis seborreica**, con **1 ensayo clínico** (Fase 2, completado) y **18 publicaciones** que respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de AEMPS recibidos (uso establecido según la literatura: dermatitis atópica leve a moderada) |
| Nueva Indicación Predicha | Dermatitis seborreica |
| Puntaje de Predicción TxGNN | 99.73% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

No hay datos estructurados de mecanismo de acción en el Evidence Pack. La literatura incluida sí lo describe: pimecrolimus inhibe la calcineurina y bloquea la activación de linfocitos T dependiente de NFAT. Esto reduce la proliferación de linfocitos T y la liberación de citoquinas inflamatorias (IL-2, IL-4, interferón gamma y TNF-alfa). También inhibe la degranulación de los mastocitos.

La dermatitis seborreica es una enfermedad inflamatoria crónica y recurrente de la piel. Cursa con eritema, descamación y picor en zonas ricas en glándulas sebáceas, y se relaciona con una respuesta inflamatoria frente a la levadura *Malassezia*. Un antiinflamatorio tópico no esteroideo que actúa sobre los linfocitos T es biológicamente plausible en este contexto. Además, evita los efectos adversos del uso prolongado de corticoides tópicos en la cara, como la atrofia cutánea.

Las revisiones sistemáticas de ensayos aleatorizados apoyan esta lógica y concluyen que pimecrolimus 1% en crema parece bien tolerado y eficaz en dermatitis seborreica. Los comparadores incluyen corticoides, antimicóticos y placebo.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00403559](https://clinicaltrials.gov/study/NCT00403559) | Fase 2 | Completado | 113 | Estudio exploratorio de 4 semanas, aleatorizado, doble ciego y con comparador activo, para evaluar la eficacia de Elidel (pimecrolimus) en dermatitis seborreica. Coincidencia directa de fármaco y enfermedad, sin confirmación en Fase 3. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34910320](https://pubmed.ncbi.nlm.nih.gov/34910320/) | 2022 | ECA | Clin Exp Dermatol | Pimecrolimus 1% frente a sertaconazol 2% en crema en dermatitis seborreica facial (ensayo aleatorizado y ciego). |
| [36072203](https://pubmed.ncbi.nlm.nih.gov/36072203/) | 2022 | Revisión sistemática de ECA | Cureus | Evalúa la eficacia y seguridad de pimecrolimus en dermatitis seborreica facial. |
| [22142161](https://pubmed.ncbi.nlm.nih.gov/22142161/) | 2012 | Revisión sistemática de ECA | Expert Rev Clin Pharmacol | Pimecrolimus 1% en crema parece bien tolerado y eficaz frente a corticoides, antimicóticos, placebo o no intervención. |
| [18677657](https://pubmed.ncbi.nlm.nih.gov/18677657/) | 2009 | Estudio abierto, aleatorizado y comparativo | J Dermatolog Treat | Compara pimecrolimus 1% con ketoconazol 2% en crema en dermatitis seborreica. |
| [23715821](https://pubmed.ncbi.nlm.nih.gov/23715821/) | 2013 | Estudio comparativo | Ir J Med Sci | Compara sertaconazol 2% con pimecrolimus 1% en crema en dermatitis seborreica. |
| [28589618](https://pubmed.ncbi.nlm.nih.gov/28589618/) | 2018 | Estudio comparativo de pautas | J Cosmet Dermatol | Compara distintas pautas de pimecrolimus 1% en dermatitis seborreica facial, ya que la duración del tratamiento variaba entre estudios previos. |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Revisión sistemática | Am J Clin Dermatol | Revisa los tratamientos tópicos de la dermatitis seborreica facial. Es una revisión general de tratamientos y no específica de pimecrolimus. |
| [20000875](https://pubmed.ncbi.nlm.nih.gov/20000875/) | 2010 | Estudio abierto | Am J Clin Dermatol | Pimecrolimus 1% en dermatitis seborreica facial resistente al tratamiento. |
| [15700745](https://pubmed.ncbi.nlm.nih.gov/15700745/) | 2004 | Estudio clínico | Drugs Exp Clin Res | Pimecrolimus 1% puede ser un tratamiento eficaz en dermatitis seborreica de cara y tronco. |
| [31053034](https://pubmed.ncbi.nlm.nih.gov/31053034/) | 2019 | Revisión | J Cutan Med Surg | Revisa los usos fuera de indicación de pimecrolimus tópico, con foco en los ECA publicados. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 65029 | ELIDEL 10 mg/g CREMA (Viatris Healthcare Limited) | Crema | No disponible en los datos recibidos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un ensayo de Fase 2 completado y aleatorizado (n=113), junto con varias revisiones sistemáticas y ECA de comparación directa, que respaldan pimecrolimus en dermatitis seborreica. Sin embargo, no existe confirmación en Fase 3 y faltan los datos de seguridad de AEMPS. Por eso se recomienda avanzar solo con salvaguardas: uso limitado a la cara, de corta duración, y respetando la advertencia de recuadro negro de la clase de inhibidores tópicos de la calcineurina.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), que actualmente bloquea el cribado de seguridad.
- Confirmar la indicación autorizada en España para ELIDEL (número 65029).
- Obtener datos estructurados de mecanismo de acción desde DrugBank.
- Evaluar la necesidad de un ensayo confirmatorio de Fase 3 en dermatitis seborreica.
- Definir un plan de seguridad sobre el riesgo de malignidad con uso prolongado, sobre todo en poblaciones pediátricas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


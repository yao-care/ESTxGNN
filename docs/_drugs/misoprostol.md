---
layout: default
title: Misoprostol
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 2
---

# Misoprostol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Misoprostol: De la Interrupción del Embarazo a la Amenorrea

## Resumen en Una Frase

Misoprostol es un análogo sintético de la prostaglandina E1, cuyo uso clínico conocido —combinado con mifepristona— es la interrupción farmacológica del embarazo y la evacuación uterina en el aborto diferido (missed abortion). El modelo TxGNN predice que podría ser relevante para **Amenorrea**, con un puntaje de **99.64%**, pero esta señal se apoya únicamente en **0 ensayos clínicos** y **7 publicaciones** que, en su mayoría, estudian la interrupción del embarazo y no el tratamiento de la amenorrea en sí.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en base regulatoria española (fármaco no comercializado); uso clínico conocido: interrupción farmacológica del embarazo / evacuación de aborto diferido |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99.64% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de misoprostol procedentes de DrugBank (brecha de datos DG002, severidad Alta). Según la evidencia incluida en este paquete, misoprostol es un análogo de la prostaglandina E1 (PGE1) que actúa sobre los receptores EP2/EP3 del útero, provocando contracción miometrial y maduración cervical; clínicamente se emplea, combinado con mifepristona, en la interrupción farmacológica del embarazo y en la evacuación uterina del aborto diferido.

La relación con la "amenorrea" es indirecta: los cuadros clínicos en los que se usa misoprostol (aborto diferido, embarazo no evolutivo) cursan con amenorrea secundaria porque la paciente está o estuvo embarazada, no porque el fármaco trate la ausencia de menstruación. Existe por tanto una superposición semántica entre el concepto "amenorrhea (disease)" del grafo de conocimiento y el contexto obstétrico en el que se usa el fármaco, pero la evidencia disponible respalda "terminar el embarazo / evacuar el útero", no "inducir o tratar la amenorrea" como tal. Antes de avanzar es necesario aclarar si esta predicción refleja un efecto terapéutico real o un artefacto de mapeo de la ontología de enfermedades.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | Ensayo controlado aleatorizado (clasificado como Cohorte) | Reproductive Sciences | Mifepristona en dosis baja + misoprostol autoadministrado para aborto médico ultra-temprano (n=744); evalúa eficacia, seguridad y aceptabilidad |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | Ensayo controlado aleatorizado de rango de dosis (clasificado como Cohorte) | Reproductive Sciences | Dosis decrecientes de mifepristona (50-150 mg) + misoprostol 200 µg para terminar embarazo ultra-temprano (n=2500) |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Cohorte | Human Reproduction | Mifepristona en dosis baja + misoprostol administrados antes de la menstruación esperada, para prevenir embarazo no deseado |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Cohorte | J Obstet Gynaecol Res | Mifepristona en dosis baja + misoprostol autoadministrado para aborto médico temprano; evalúa seguridad y eficacia |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Revisión | J Obstet Gynaecol Can | Revisión sobre ablación endometrial en el manejo del sangrado uterino anormal (no aborda amenorrea directamente) |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Revisión | BMJ | Manejo médico del aborto diferido y embarazo anembrionado (sin resumen disponible) |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Reporte de Caso/Revisión | Cureus | Caso de hígado graso agudo del embarazo; la amenorrea aparece solo como síntoma de presentación, no como objetivo terapéutico |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Toda la información de seguridad de este paquete (advertencias clave, contraindicaciones e interacciones farmacológicas) figura como brecha de datos, incluyendo la brecha bloqueante DG001 (仿單警語/禁忌 de TFDA/AEMPS no disponible), lo que impide una evaluación preliminar de seguridad (S1).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La señal de TxGNN es de alta puntuación pero de bajo nivel de evidencia (L4): no existen ensayos clínicos ni literatura que estudien directamente misoprostol para el tratamiento de la amenorrea, solo estudios sobre interrupción del embarazo donde la amenorrea es un síntoma incidental. A esto se suma la brecha de datos bloqueante de seguridad (DG001) y la ausencia total de autorización de comercialización en España.

**Para avanzar se necesita:**
- Ficha técnica/prospecto de TFDA-AEMPS con advertencias, contraindicaciones e interacciones (resolver DG001, bloqueante)
- Confirmación del mecanismo de acción vía API de DrugBank (resolver DG002)
- Aclarar si "amenorrhea (disease)" en el grafo de conocimiento es un artefacto de mapeo ontológico o representa un uso clínico genuino (p. ej., inducción de menstruación/interceptivo) distinto del uso abortivo ya conocido
- Estudios que evalúen directamente misoprostol como tratamiento de la amenorrea (no como parte de un régimen de interrupción del embarazo)

---
*Nota: el Evidence Pack incluye una segunda señal predicha (atypical coarctation of aorta, puntaje 99.30%), pero sin ensayos clínicos ni literatura de respaldo (Nivel de Evidencia L5, Decisión: Hold) y basada solo en un efecto de clase teórico con alprostadil. No se desarrolla en este informe por falta total de evidencia.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


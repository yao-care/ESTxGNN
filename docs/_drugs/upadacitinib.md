---
layout: default
title: Upadacitinib
parent: 僅模型預測 (L5)
nav_order: 289
evidence_level: L5
indication_count: 2
---

# Upadacitinib
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

# Upadacitinib: De Enfermedades Autoinmunes/Inflamatorias a Síndrome de Microftalmia Colobomatosa-Displasia Rizomélica

## Resumen en Una Frase

Upadacitinib es un inhibidor selectivo de JAK1, utilizado clínicamente en el tratamiento de enfermedades autoinmunes e inflamatorias. El modelo TxGNN predice dos posibles nuevas indicaciones —**síndrome de microftalmia colobomatosa con displasia rizomélica** y **síndrome de braquidactilia-sindactilia**—, ambas con puntajes superiores al 99%, pero **sin ningún ensayo clínico ni publicación que las respalde**, y sin un mecanismo biológico plausible identificado.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedades autoinmunes/inflamatorias (indicación específica no registrada en esta fuente; fármaco no comercializado en España) |
| Nueva Indicación Predicha (candidato principal) | Síndrome de microftalmia colobomatosa con displasia rizomélica |
| Puntaje de Predicción TxGNN | 99.61% (rank #6592) |
| Nivel de Evidencia | L5 (solo predicción del modelo, sin estudios reales) |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | **Hold** |

---

## Por qué es Razonable esta Predicción?

Upadacitinib es un inhibidor selectivo de JAK1 cuya acción farmacológica conocida consiste en bloquear la señalización de citocinas (IL-6, IL-23, entre otras) para lograr un efecto inmunomodulador, y se emplea principalmente en enfermedades autoinmunes e inflamatorias. No se dispone de datos detallados adicionales sobre su mecanismo de acción en esta fuente (dato pendiente de completar vía DrugBank API).

Las dos indicaciones predichas por TxGNN corresponden, sin embargo, a **síndromes malformativos congénitos**: el síndrome de microftalmia colobomatosa con displasia rizomélica (asociado típicamente a genes de biogénesis peroxisomal tipo PEX o genes ciliares) y el síndrome de braquidactilia-sindactilia (asociado a vías de desarrollo esquelético como HOX, BMP o GLI3). Ninguna de estas dos condiciones tiene una relación biológica conocida con la vía JAK-STAT ni con la inmunomodulación.

**Evaluación de plausibilidad:** para ambos candidatos no existe un vínculo mecanístico verificable. El puntaje elevado de TxGNN probablemente refleja proximidad de nodos en el grafo de conocimiento (similitud de embedding) más que una relación farmacológica real, por lo que ambas predicciones deben considerarse de **alta probabilidad de ser falsos positivos**.

---

## Evidencia Clínica y de Literatura

### Candidato 1: Síndrome de microftalmia colobomatosa con displasia rizomélica

**Ensayos clínicos:** Actualmente no hay ensayos clínicos relacionados registrados.

**Literatura:** Actualmente no hay literatura relacionada disponible.

### Candidato 2: Síndrome de braquidactilia-sindactilia

**Puntaje TxGNN:** 99.58% (rank #7010) — Nivel de Evidencia L5 — Recomendación: Hold

**Ensayos clínicos:** Actualmente no hay ensayos clínicos relacionados registrados.

**Literatura:** Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Upadacitinib no cuenta actualmente con autorizaciones de comercialización registradas en España (estado: No comercializado, 0 autorizaciones).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. (No se dispone de advertencias, contraindicaciones ni interacciones farmacológicas registradas en esta fuente; la ficha técnica/prospecto de la AEMPS aún no ha sido incorporada — brecha de datos bloqueante para la evaluación de seguridad S1.)

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ambas indicaciones predichas cuentan únicamente con evidencia de Nivel L5 (predicción del modelo sin respaldo clínico ni bibliográfico), y el propio análisis mecanístico no encuentra relación biológica plausible entre la inhibición de JAK1 y estos síndromes malformativos congénitos. La probabilidad de que se trate de falsos positivos del embedding es alta.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica de TFDA con advertencias y contraindicaciones (brecha bloqueante DG001) antes de cualquier evaluación de seguridad S1
- Completar los datos de mecanismo de acción (MOA) vía API de DrugBank (DG002)
- Justificación mecanística adicional (p. ej. vías PEX/ciliopatías o HOX/BMP/GLI3) que conecte razonablemente la inhibición de JAK1 con estos síndromes, antes de invertir en búsqueda de evidencia adicional
- En ausencia de nueva evidencia, despriorizar estos dos candidatos frente a otras predicciones TxGNN de upadacitinib con mayor coherencia mecanística
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


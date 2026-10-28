---
layout: default
title: Plerixafor
parent: Solo predicción del modelo (L5)
nav_order: 648
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
monitor_inn: "PLERIXAFOR"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "bronchitis", "vulvar melanoma (disease)", "myeloid leukemia"]
description: "Plerixafor: nueva indicación predicha, CMM7 (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Plerixafor
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Plerixafor: CMM7
{: .text-alpha }

## Resumen en Una Frase

Plerixafor es un antagonista del receptor CXCR4, utilizado como movilizador de células madre hematopoyéticas en pacientes con mieloma múltiple y linfoma no Hodgkin que requieren un trasplante autólogo.
El modelo TxGNN predice que podría ser efectivo para el **mieloma de células plasmáticas indolente**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta indicación concreta. Se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | CMM7 |
| Puntaje de Predicción TxGNN | 0.9934 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 6 de 8) |
| Número de Autorizaciones | 8 (vigentes: 6) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción. Aun así, plerixafor es conocido como antagonista de CXCR4 (y también interactúa con ACKR3). Al bloquear el eje CXCR4/CXCL12, impide que las células madre hematopoyéticas permanezcan ancladas en la médula ósea y favorece su paso a la sangre periférica. Por eso se emplea para movilizar células madre antes de un trasplante autólogo en mieloma múltiple y linfoma no Hodgkin.

El eje CXCR4/CXCL12 también contribuye a que las células de mieloma se alojen y permanezcan en el nicho de la médula ósea. Esto da una base biológica plausible para la predicción, ya que el fármaco actúa sobre un mecanismo relacionado con la propia enfermedad.

Sin embargo, esta relación es solo teórica. El uso actual de plerixafor en mieloma es la movilización de células madre, una finalidad distinta del tratamiento de la enfermedad indolente. No se aportaron ensayos ni literatura para esta indicación, y el puntaje del modelo es solo una predicción computacional.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

---

## Información de Mercado en España

Se muestran 5 de las 8 autorizaciones vigentes, todas de solución inyectable y de principio activo único. Los textos de indicación aprobada no están disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 09537001 | MOZOBIL 20 mg/ml solución inyectable | Solución inyectable | Sanofi B.V. |
| 88951 | Plerixafor Seacross 20 mg/ml solución inyectable EFG | Solución inyectable | Seacross Pharma (Europe) Limited |
| 89340 | Plerixafor Tarbis 20 mg/ml solución inyectable EFG | Solución inyectable | Tarbis Farma S.L. |
| 1221701001 | Plerixafor Accord 20 mg/ml solución inyectable EFG | Solución inyectable | Accord Healthcare S.L.U. |
| 88723 | Plerixafor Eugia 20 mg/ml solución inyectable EFG | Solución inyectable | Eugia Pharma (Malta) Limited |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (relaciones fármaco-enfermedad, no texto del prospecto): trombocitopenia, insuficiencia renal y leucemia.
- **Dianas farmacológicas** (no son interacciones fármaco-fármaco): CXCR4 y ACKR3.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos clínicos ni literatura para el mieloma indolente. Además, el uso actual de plerixafor en mieloma (movilización de células madre) es distinto del tratamiento de la enfermedad indolente.

**Para avanzar se necesita:**
- Estudios preclínicos o de mecanismo que demuestren el papel del eje CXCR4/CXCL12 en el mieloma indolente.
- Ensayos clínicos o literatura específicos para esta indicación.
- Datos detallados del mecanismo de acción.
- Las advertencias y contraindicaciones oficiales del prospecto de la AEMPS, para evaluar la seguridad.
- Un análisis de la relación entre el uso actual (movilización) y el objetivo terapéutico propuesto, incluido el significado de las contraindicaciones del grafo (trombocitopenia, insuficiencia renal, leucemia).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


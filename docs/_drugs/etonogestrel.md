---
layout: default
title: Etonogestrel
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 5
---

# Etonogestrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Usando el Evidence Pack proporcionado, genero el informe siguiendo el formato v5 (Etonogestrel → Amenorrea, indicación de rango 1, que es el único registro con evidencia real):

---

# Etonogestrel: De Anticoncepción a Amenorrea

## Resumen en Una Frase

Etonogestrel es un progestágeno de acción prolongada utilizado en implantes subdérmicos anticonceptivos (p. ej. Implanon/Nexplanon). El modelo TxGNN predice una asociación con **Amenorrea**, respaldada actualmente por **1 ensayo clínico** y **2 publicaciones**. Sin embargo, la evidencia disponible sugiere que esta asociación refleja la amenorrea como **efecto adverso conocido** de la anticoncepción hormonal, no como una indicación terapéutica validada — la dirección de causalidad requiere aclaración experta antes de avanzar.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Anticoncepción (implante subdérmico de progestágeno) — no hay indicación aprobada local disponible, ya que el medicamento no está comercializado en España |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

No se dispone de datos oficiales de mecanismo de acción (DrugBank marca este campo como pendiente). No obstante, según la evidencia clínica incluida en este paquete, etonogestrel es un progestágeno de acción prolongada que actúa suprimiendo el eje hipotálamo-hipófisis-ovario e induciendo atrofia endometrial — mecanismo bien establecido en su uso como anticonceptivo.

Este mismo mecanismo es responsable de un efecto adverso ampliamente documentado durante el uso del implante: sangrado irregular o **amenorrea secundaria al tratamiento anticonceptivo**. Es decir, la relación entre "Anticoncepción" (uso original) y "Amenorrea" (indicación predicha) no es que el fármaco *trate* un cuadro de amenorrea preexistente, sino que el fármaco *induce* amenorrea como consecuencia farmacológica esperada de su uso anticonceptivo.

Por este motivo, el alto puntaje de TxGNN probablemente refleja una **co-ocurrencia en la base de conocimiento** ("fármaco – amenorrea") más que una hipótesis terapéutica validada, y la dirección causal es opuesta a la que sugiere el nombre de la indicación. Este punto debe aclararse mediante revisión clínica experta antes de considerar cualquier desarrollo posterior.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Fase 3 | Completado | 498 | Estudio de un solo brazo sobre eficacia y seguridad anticonceptiva del implante de etonogestrel durante uso extendido (años 4-5 tras inserción). La amenorrea/patrón de sangrado es solo un criterio de seguridad secundario, no el objetivo terapéutico del estudio — relevancia baja para esta indicación (evaluado como grado C). |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | ECA | Contraception | Ensayo aleatorizado multicéntrico comparando implantes de etonogestrel (Implanon) vs. levonorgestrel (Norplant): sin embarazos en 2 años de uso, con comparación de patrones de sangrado/amenorrea entre grupos. Evidencia indirecta sobre el efecto del fármaco en el ciclo menstrual, no un estudio terapéutico de amenorrea. |
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | ECA | Trials | Protocolo de ensayo sobre BIO101 para neumonía por COVID-19. No guarda relación aparente con etonogestrel ni con amenorrea — probable resultado no pertinente recuperado en la búsqueda bibliográfica automatizada. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

*(No se dispone de advertencias, contraindicaciones ni datos de interacciones farmacológicas verificados para este fármaco; la consulta del prospecto TFDA/ficha técnica está pendiente y es un requisito bloqueante antes de avanzar — ver DG001 en el registro de brechas de datos.)*

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque el puntaje de predicción de TxGNN es muy alto (99.84%), la evidencia clínica y bibliográfica disponible es escasa, indirecta y de relevancia limitada (grado C), y el mecanismo farmacológico sugiere que la asociación observada probablemente corresponde a un **efecto adverso conocido** (amenorrea inducida por anticoncepción hormonal) más que a una indicación terapéutica genuina. A esto se suma la ausencia total de datos de seguridad verificados (advertencias, contraindicaciones, ficha técnica), lo que impide iniciar siquiera la evaluación de seguridad S1.

**Para avanzar se necesita:**
- Ficha técnica/prospecto oficial (TFDA/AEMPS) con advertencias y contraindicaciones — actualmente bloqueante para la evaluación de seguridad S1
- Confirmación del mecanismo de acción mediante consulta a la API de DrugBank
- Revisión clínica experta para aclarar si la relación fármaco-enfermedad tiene dirección causal terapéutica, o si simplemente refleja un efecto adverso reportado en la literatura de anticoncepción
- Búsqueda bibliográfica dirigida específicamente a "tratamiento de amenorrea con progestágenos", en lugar de basarse en la co-ocurrencia detectada por el modelo
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


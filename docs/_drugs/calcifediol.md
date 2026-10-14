---
layout: default
title: Calcifediol
parent: Solo predicción del modelo (L5)
nav_order: 133
evidence_level: L5
indication_count: 4
---

# Calcifediol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Calcifediol: De Hipercalcemia y Trastornos del Metabolismo del Fósforo a Deficiencia de Vitamina D (término obsoleto)

## Resumen en Una Frase

Calcifediol (25-hidroxivitamina D3) es la principal forma circulante de la vitamina D y se utiliza en trastornos del metabolismo óseo y mineral como raquitismo, osteomalacia y osteodistrofia renal.
El modelo TxGNN predice que podría ser efectivo para **deficiencia de vitamina D (término obsoleto en la ontología)**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción concreta; es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los textos de autorización; el grafo de conocimiento indica hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, hipofosfatemia, raquitismo, osteomalacia y osteodistrofia renal |
| Nueva Indicación Predicha | Deficiencia de vitamina D (término obsoleto) |
| Puntaje de Predicción TxGNN | 99,99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 12 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, el calcifediol es el precursor directo del calcitriol (la forma activa de la vitamina D), y su eficacia en trastornos del metabolismo óseo y mineral está establecida. Mecanísticamente, repone el estado de vitamina D, por lo que podría ser aplicable a la deficiencia de vitamina D.

Sin embargo, el término de la enfermedad está marcado como obsoleto en la ontología, por lo que probablemente es un duplicado heredado de los términos actuales de deficiencia de vitamina D. Además, esta indicación está muy próxima a los usos ya conocidos del fármaco, por lo que probablemente no constituye un reposicionamiento genuino.

**Otras predicciones del modelo (para contexto):**

| Indicación predicha | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|
| Acidosis tubular renal | 99,86% | L5 | Vínculo indirecto: la vitamina D podría tratar las complicaciones óseas, no el defecto tubular. Sin ensayos ni literatura. |
| Raquitismo hipofosfatémico hereditario | 99,76% | L4 | El calcifediol es mecanísticamente menos adecuado que los análogos activos; la única referencia es una revisión de 2024 (evidencia indirecta). |
| Raquitismo dependiente de vitamina D | 99,18% | L4 | Mayor racionalidad mecanística: en el tipo 1B (deficiencia de 25-hidroxilasa, CYP2R1) el calcifediol salta el paso enzimático bloqueado. Evidencia solo a nivel de casos. |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (deficiencia de vitamina D). Para las indicaciones alternativas se identificó:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Revisión | Nutrients | Revisión de los tipos de raquitismo y su tratamiento con vitamina D y análogos (raquitismo hipofosfatémico hereditario) |
| [28548312](https://pubmed.ncbi.nlm.nih.gov/28548312/) | 2017 | Serie de casos | J Bone Miner Res | Raquitismo dependiente de vitamina D tipo 1B (deficiencia de 25-hidroxilasa): 7 pacientes de 2 familias; plantea si es una condición rara o infradiagnosticada |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 90092 | Vitode Semanal 75 microgramos cápsulas blandas | Cápsula blanda | No disponible |
| 88826 | Calcifediol Normogen 0,266 mg cápsulas blandas EFG | Cápsula blanda | No disponible |
| 90091 | Vitode Semanal 100 microgramos cápsulas blandas | Cápsula blanda | No disponible |
| 85519 | Rayaldee 30 microgramos cápsulas blandas de liberación prolongada | Cápsula blanda de liberación prolongada | No disponible |
| 55315 | Hidroferol 0,1 mg/ml gotas orales en solución | Gotas orales en solución | No disponible |

Se muestran 5 de las 12 autorizaciones vigentes (todas de principio activo único, ninguna cancelada).

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto)**: enfermedad renal, piouréter, sarcoidosis, hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, nefrolitiasis (incluida la asociada a SLC26A1), nefropatía aguda por uratos, hiperfosfatemia, hipervitaminosis y arteriosclerosis obliterante.
- **Interacciones Farmacológicas**: se identificaron 57 interacciones; entre las principales:
  - *Mayores*: colecalciferol, burosumab, calcitriol.
  - *Moderadas*: fosfenitoína, carbamazepina, barbitúricos (amobarbital, butalbital, butabarbital), diuréticos tiazídicos (hidroclorotiazida, bendroflumetiazida, clorotiazida, clortalidona), hidróxido de aluminio, resinas secuestradoras de ácidos biliares (colestiramina, colesevelam, colestipol), digitoxina y calcipotriol/calcitriol tópicos.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal tiene un puntaje muy alto, pero se basa únicamente en el modelo (L5), sin ensayos ni literatura, y la enfermedad está marcada como obsoleta y solapa con los usos ya existentes del fármaco. Entre las alternativas, el raquitismo dependiente de vitamina D tipo 1B es la más plausible mecanísticamente, aunque solo tiene evidencia a nivel de casos (L4).

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), actualmente ausente.
- Completar los datos del mecanismo de acción desde DrugBank.
- Mapear la indicación obsoleta a los términos vigentes de deficiencia de vitamina D y confirmar si hay reposicionamiento real.
- Para el raquitismo dependiente de vitamina D tipo 1B, plantear una serie de casos estructurada o una evaluación basada en registros.
- Evaluar el riesgo de hipercalcemia y las interacciones mayores (colecalciferol, calcitriol, burosumab) en cualquier nueva población.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


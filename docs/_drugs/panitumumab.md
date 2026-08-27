---
layout: default
title: Panitumumab
parent: 僅模型預測 (L5)
nav_order: 210
evidence_level: L5
indication_count: 2
---

# Panitumumab
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

# Panitumumab: De Cáncer Colorrectal Metastásico a Osteoporosis Inducida por Fármacos

*Nota: la Evidence Pack incluye dos indicaciones predichas (rank 1: osteoporosis inducida por fármacos, score 99,13%; rank 2: retinopatía diabética no proliferativa severa, score 99,05%). Ambas tienen nivel de evidencia L5 (sin ensayos clínicos ni literatura) y recomendación "Hold" idéntica. Este informe se centra en el rank 1 por tener el score TxGNN más alto.*

---

## Resumen en Una Frase

Panitumumab es un anticuerpo monoclonal dirigido contra el EGFR, utilizado originalmente en el tratamiento del cáncer colorrectal metastásico (información general de referencia, no incluida como campo estructurado en esta Evidence Pack). El modelo TxGNN predice que podría ser efectivo para **Osteoporosis Inducida por Fármacos**, pero esta dirección **no cuenta actualmente con ningún ensayo clínico ni publicación de respaldo**: se trata únicamente de una señal computacional del modelo (score 99,13%).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer colorrectal metastásico (conocimiento general de referencia; no disponible como dato estructurado en esta Evidence Pack) |
| Nueva Indicación Predicha | Osteoporosis Inducida por Fármacos |
| Puntaje de Predicción TxGNN | 99,13% |
| Nivel de Evidencia | L5 |
| Estado de Mercado | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos estructurados sobre el mecanismo de acción de panitumumab en esta Evidence Pack (dato marcado como brecha de alta severidad, DG002). Según la información conocida, panitumumab es un anticuerpo monoclonal IgG2 completamente humano dirigido contra el receptor del factor de crecimiento epidérmico (EGFR), que bloquea la unión de sus ligandos naturales e inhibe la señalización intracelular RAS/RAF/MAPK y PI3K/AKT. Su eficacia en cáncer colorrectal metastásico con gen RAS no mutado está clínicamente establecida.

La señalización de EGFR también participa, según la literatura general, en la regulación del recambio óseo (actividad de osteoclastos y osteoblastos), lo que ofrece una hipótesis mecanística teórica para vincular la inhibición de EGFR con alteraciones de la densidad ósea. Sin embargo, esta Evidence Pack **no aporta ningún dato propio** —ni preclínico, ni observacional, ni de casos— que sustente esta hipótesis; la única base es el score del modelo TxGNN (0,9913), sin ensayos clínicos ni literatura que lo respalden. La conexión debe considerarse especulativa hasta que se identifique evidencia independiente.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado

Panitumumab no cuenta actualmente con ninguna autorización de comercialización registrada en la consulta realizada (0 autorizaciones, estado: no comercializado). No es posible presentar una tabla de presentaciones ni de indicaciones aprobadas localmente.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-EGFR) |
| Riesgo de Mielosupresión | Bajo — los anticuerpos monoclonales anti-EGFR no suelen causar mielosupresión relevante; la toxicidad predominante de esta clase es cutánea y electrolítica. No hay datos cuantitativos propios en esta Evidence Pack — consultar el prospecto |
| Clasificación de Emetogenicidad | Baja, perfil típico de los anticuerpos monoclonales |
| Items de Monitoreo | Magnesio sérico y electrolitos (hipomagnesemia frecuente en la clase anti-EGFR), piel/uñas (rash acneiforme), función renal |
| Protección en Manejo | Al ser un agente antineoplásico biológico, se recomiendan precauciones estándar de manejo de fármacos citotóxicos en su preparación y administración |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el score del modelo TxGNN (L5/S0), sin ningún ensayo clínico ni publicación que la respalde, y coexiste con brechas de datos críticas: ausencia de advertencias/contraindicaciones del prospecto (brecha bloqueante, DG001) y de mecanismo de acción estructurado (DG002). No hay base suficiente para avanzar a evaluación de seguridad (S1).

**Para avanzar se necesita:**
- Advertencias, contraindicaciones e interacciones farmacológicas desde el prospecto oficial (TFDA/AEMPS) — brecha bloqueante
- Datos de mecanismo de acción (MOA) verificados en DrugBank
- Evidencia preclínica u observacional que vincule específicamente la inhibición de EGFR con densidad mineral ósea
- Búsqueda periódica de nuevos ensayos clínicos o literatura, dado que actualmente el conteo es cero
- Confirmación del estado real de registro/comercialización, dado que la ausencia de autorización podría reflejar una limitación de la fuente consultada más que una ausencia real de aprobación
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


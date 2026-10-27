---
layout: default
title: Tivozanib
parent: Solo predicción del modelo (L5)
nav_order: 799
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tivozanib: nueva indicación predicha, Carcinoma endocervical (nivel de evidencia L5). Indicación original: Carcinoma de células renales (carcinoma renal de células claras…"
monitor_inn: "TIVOZANIB"
predicted_indications: ["endocervical carcinoma", "uterine ligament adenocarcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "cervical adenosquamous carcinoma, glassy cell variant", "uterine ligament endometrioid adenocarcinoma", "uterine ligament mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma", "cervical mucinous adenocarcinoma, minimal deviation variant"]
---

# Tivozanib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Tivozanib: De Carcinoma de Células Renales a Carcinoma Endocervical
{: .text-alpha }

## Resumen en Una Frase

Tivozanib es un inhibidor selectivo de la tirosina quinasa de los receptores VEGF (VEGFR-1/2/3), utilizado originalmente para el tratamiento del carcinoma de células renales avanzado.
El modelo TxGNN predice que podría ser efectivo para **Carcinoma Endocervical**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma de células renales (carcinoma renal de células claras, adenocarcinoma de células renales) |
| Nueva Indicación Predicha | Carcinoma endocervical |
| Puntaje de Predicción TxGNN | 99.81% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente principal. Según la información farmacológica compilada, tivozanib inhibe con potencia similar los tres receptores de VEGF con actividad tirosina quinasa: VEGFR-1 (FLT1), VEGFR-2 (KDR) y VEGFR-3 (FLT4). Su eficacia en el carcinoma renal avanzado está establecida: fue aprobado por la EMA en 2017 y por la FDA en marzo de 2021.

El carcinoma renal y los carcinomas cervicales comparten una dependencia relevante de la angiogénesis mediada por VEGF. En cáncer cervical avanzado, otro fármaco antiangiogénico (bevacizumab) ha mostrado beneficio, lo que vuelve plausible, en teoría, la inhibición de la vía VEGFR.

Sin embargo, el puntaje alto de TxGNN (0.998) es solo una predicción del modelo y probablemente refleja, en parte, la proximidad entre nodos de enfermedad en el grafo de conocimiento. No se recuperaron ensayos clínicos ni literatura que respalden el uso de tivozanib en esta indicación, y la similitud con la indicación original aún no ha sido evaluada.

Otras predicciones del modelo (todas con nivel L5 y sin evidencia) incluyen adenocarcinomas del ligamento uterino y variantes raras de adenocarcinoma cervical, con puntajes entre 99.76% y 99.80%.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1171215001 | FOTIVDA 890 microgramos cápsulas duras | Cápsula dura | No especificada en los datos compilados |
| 1171215002 | FOTIVDA 1340 microgramos cápsulas duras | Cápsula dura | No especificada en los datos compilados |

Ambas autorizaciones están vigentes y pertenecen a Recordati Netherlands B.V.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasa de VEGFR) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

**Interacciones Farmacológicas** (7 registros en total; los 4 con nivel de gravedad asignado son):
- **Mayor**: Fenobarbital y hierba de San Juan (hipérico). Requieren especial atención y, en general, deben evitarse o manejarse con precaución.
- **Moderada**: Riociguat y acetato de medroxiprogesterona.

Los otros 3 registros corresponden a las dianas farmacológicas de tivozanib (VEGFR-1, VEGFR-2 y VEGFR-3), no a interacciones con otros fármacos.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura que la respalden. Aunque la inhibición de VEGFR es mecanísticamente plausible en cáncer cervical, no hay datos específicos de tivozanib en esta enfermedad.

**Para avanzar se necesita:**
- Búsqueda más amplia de literatura y registros de ensayos (incluyendo estudios preclínicos en modelos de cáncer cervical)
- Datos detallados del mecanismo de acción y análisis de similitud con la indicación original
- Revisión del prospecto de la AEMPS para advertencias y contraindicaciones (actualmente un vacío de datos bloqueante para el cribado de seguridad)
- Evaluación de la viabilidad de ensayos dada la rareza de las histologías predichas
- Evaluación de la compatibilidad de vía de administración (actualmente pendiente)
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


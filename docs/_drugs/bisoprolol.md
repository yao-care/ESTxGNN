---
layout: default
title: Bisoprolol
parent: Solo predicción del modelo (L5)
nav_order: 108
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Bisoprolol: nueva indicación predicha, Enfermedad renal hipertensiva maligna (nivel de evidencia L5). Indicación original: Hipertensión arterial (trastorno hipertensivo)"
monitor_inn: "BISOPROLOL"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Bisoprolol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Bisoprolol: De Hipertensión Arterial a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Bisoprolol es un betabloqueante selectivo beta-1, utilizado originalmente para el tratamiento de la hipertensión arterial.
El modelo TxGNN predice que podría ser efectivo para **enfermedad renal hipertensiva maligna**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden específicamente esta indicación; se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (trastorno hipertensivo) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.94% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, bisoprolol es un betabloqueante selectivo del receptor beta-1 adrenérgico, con eficacia comprobada en hipertensión arterial. Mecanísticamente, la reducción de la presión arterial es plausible en una complicación grave de la hipertensión como la enfermedad renal hipertensiva maligna.

Además, el bloqueo beta-1 reduce la liberación de renina en el aparato yuxtaglomerular, lo que podría ser relevante en la lesión renal impulsada por el sistema renina-angiotensina.

Sin embargo, la puntuación elevada de TxGNN parece reflejar la indicación antihipertensiva ya conocida y no una evidencia independiente. La hipertensión maligna se maneja habitualmente con fármacos intravenosos en el ámbito agudo, y no existen estudios para esta indicación específica.

**Otras predicciones del modelo (todas con evidencia débil):**

| Indicación predicha | Puntaje | Nivel | Comentario |
|------|------|------|------|
| Hipertensión renovascular maligna | 99.94% | L5 | Reformulación en gran parte del uso conocido; tendrían prioridad los inhibidores del SRAA y la revascularización |
| Hipertensión pulmonar por enfermedad pulmonar y/o hipoxia | 99.93% | L4 | Literatura indirecta (insuficiencia cardiaca, estudios preclínicos); preocupaciones de seguridad |
| Hipertensión pulmonar de mecanismo multifactorial poco claro | 99.93% | L5 | Sin evidencia específica; el bloqueo beta no es un tratamiento establecido y podría empeorar la función del ventrículo derecho |
| Síndrome de Braddock | 99.91% | L5 | Sin base mecanística identificable; hipótesis de baja prioridad |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (enfermedad renal hipertensiva maligna).

*Nota: para la predicción de hipertensión pulmonar por enfermedad pulmonar/hipoxia (rango 3) se recuperó literatura indirecta, resumida a continuación:*

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19789971](https://pubmed.ncbi.nlm.nih.gov/19789971/) | 2009 | Revisión | Cardiovasc Drugs Ther | Efectos de los betabloqueantes sobre la función pulmonar en insuficiencia cardiaca; se cuestiona la idea histórica de que están contraindicados con función pulmonar alterada |
| [23506636](https://pubmed.ncbi.nlm.nih.gov/23506636/) | 2013 | Estudio clínico comparativo | Int J Cardiol | Estudio CARNEBI: comparación de carvedilol, nebivolol y bisoprolol en insuficiencia cardiaca moderada |
| [18845967](https://pubmed.ncbi.nlm.nih.gov/18845967/) | 2008 | Estudio fisiológico | Med Sci Sports Exerc | Bloqueo beta-adrenérgico y contribución del metabo-quimiorreflejo a la capacidad de ejercicio |
| [23706341](https://pubmed.ncbi.nlm.nih.gov/23706341/) | 2013 | Estudio fisiológico | J Am Soc Echocardiogr | Adaptación del ventrículo izquierdo a la hipoxia aguda con y sin inhibición beta-1 |
| [32363697](https://pubmed.ncbi.nlm.nih.gov/32363697/) | 2020 | Preclínico | Fundam Clin Pharmacol | Bisoprolol protege los cardiomiocitos de la lesión por isquemia-reperfusión mediante la vía PI3K/AKT/GSK3β |
| [27687650](https://pubmed.ncbi.nlm.nih.gov/27687650/) | 2016 | Preclínico (in vitro) | Nan Fang Yi Ke Da Xue Xue Bao | Efecto del pretratamiento con bisoprolol en la lesión por hipoxia/reoxigenación en cardiomiocitos H9c2 |
| [39088923](https://pubmed.ncbi.nlm.nih.gov/39088923/) | 2024 | Preclínico (animal) | Int Immunopharmacol | Diosmina y bisoprolol combinados atenúan la cardiotoxicidad inducida por cloruro de cobalto |
| [12887136](https://pubmed.ncbi.nlm.nih.gov/12887136/) | 2003 | Reporte de caso | Hypertens Res | Dos casos de feocromocitoma asociado a tetralogía de Fallot |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 57543 | EURADAL 10 mg comprimidos recubiertos con película | Comprimido recubierto | No disponible |
| 63048 | EMCONCOR COR 5 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 57654 | EMCONCOR 5 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 73633 | BISOPROLOL COR VIATRIS 5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 85878 | BISOPROLOL ZENTIVA 7,5 mg comprimidos EFG | Comprimido | No disponible |

Hay 20 autorizaciones vigentes, todas de monofármaco (formulaciones genéricas EFG y marcas como Emconcor y Euradal). Se muestran las 5 principales.

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del prospecto): asma (intrínseco y alérgico), diabetes mellitus y cetoacidosis diabética, enfermedad renal, enfermedad hepática y encefalopatía hepática, lupus eritematoso sistémico, psoriasis, miastenia gravis, pancreatitis, gota, anuria, trastornos de ansiedad y distimia, entre otras.
- **Interacciones farmacológicas** (100 registradas; se muestran las principales):
  - Moderadas: epinefrina, hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida, bupropión, morfina, atropina, hiosciamina, metescopolamina, acetohexamida y sales de calcio (acetato, carbonato, citrato, gluconato).
  - Leves: ácido acetilsalicílico, hidróxido de aluminio, attapulgita.
- Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa exclusivamente en el modelo (nivel L5), sin ensayos clínicos ni literatura específica, y el puntaje alto parece reflejar la indicación antihipertensiva ya conocida. Además, la hipertensión maligna requiere habitualmente tratamiento intravenoso agudo, para el cual un betabloqueante oral no es la opción de referencia.

**Para avanzar se necesita:**
- Datos del mecanismo de acción detallados del fármaco
- Advertencias y contraindicaciones del prospecto de la AEMPS (revisión de seguridad pendiente)
- Revisión sistemática de la literatura sobre betabloqueantes en hipertensión maligna y nefropatía hipertensiva
- Comparación con las guías clínicas vigentes y los tratamientos de referencia (agentes intravenosos, inhibidores del SRAA)
- Evaluación de seguridad renal, dado que enfermedad renal y anuria figuran entre las contraindicaciones del grafo
- Definición de la viabilidad de la vía de administración y de la población objetivo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


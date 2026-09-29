---
layout: default
title: Vandetanib
parent: Solo predicción del modelo (L5)
nav_order: 555
evidence_level: L5
indication_count: 10
---

# Vandetanib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Vandetanib: De Cáncer Medular de Tiroides a Carcinoma de Células Renales

## Resumen en Una Frase

Vandetanib es un inhibidor de quinasas que, según la literatura incluida, está autorizado en la Unión Europea para el cáncer medular de tiroides avanzado; el registro de la AEMPS no incluye el texto de la indicación.
El modelo TxGNN predice que podría ser efectivo para **carcinoma de células renales**,
con **4 ensayos clínicos** (2 de ellos terminados prematuramente con 3 y 7 pacientes) y **6 publicaciones**, ninguna de las cuales aporta resultados de eficacia de vandetanib en este tumor.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer medular de tiroides avanzado (según literatura; los textos de indicación de las autorizaciones de la AEMPS están vacíos) |
| Nueva Indicación Predicha | Carcinoma de células renales |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L2 (con reservas: un ensayo de Fase 2 completado, sin resultados de eficacia disponibles) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente. Según la farmacología conocida, vandetanib inhibe VEGFR2, EGFR y RET. Su eficacia en el cáncer medular de tiroides, donde RET está activado de forma constitutiva, es la base de su autorización. Mecanísticamente podría ser aplicable al carcinoma renal.

En el carcinoma renal, la pérdida de función de VHL o FH activa la vía HIF/VEGF y favorece la angiogénesis, de modo que el bloqueo de VEGFR es plausible. Varios otros inhibidores de VEGFR ya son tratamientos establecidos en este tumor.

Sin embargo, los ensayos de Fase 2 con vandetanib en enfermedad renal son pequeños o terminaron antes de tiempo, y no se aportaron resultados de eficacia. La predicción es coherente con la biología, pero aún no está demostrada clínicamente.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Fase 2 | Completado | 37 | Vandetanib en enfermedad de von Hippel-Lindau con tumores renales. Población directamente relacionada, pero sin resultados de eficacia disponibles |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Fase 2 | Terminado | 3 | Vandetanib en carcinoma renal de células claras avanzado. Terminado con solo 3 pacientes, sin señal de eficacia utilizable |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Fase 1/2 | Terminado | 7 | Vandetanib más metformina en cáncer renal asociado a HLRCC/SDH o carcinoma papilar esporádico. Terminado con 7 pacientes, no informativo sobre eficacia |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Fase 2 | Completado | 82 | Ensayo aleatorizado de carboplatino y gemcitabina con o sin vandetanib en cáncer urotelial avanzado. Relevancia indirecta para carcinoma renal |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Revisión/Preclínico | Clin Exp Metastasis | Reprogramación metabólica y epigenética en el carcinoma renal deficiente en fumarato hidratasa. No existe régimen estándar y varios ensayos de Fase 2 evalúan terapias dirigidas |
| [36302175](https://pubmed.ncbi.nlm.nih.gov/36302175/) | 2023 | Ensayo Fase 2 (otro fármaco) | Clin Cancer Res | Guadecitabina en tumores deficientes en SDH, incluido el carcinoma renal asociado a HLRCC. No evalúa vandetanib |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Preclínico (modelo murino) | Mol Cancer Res | Modelo de ratón de carcinoma renal con translocación TFE3/Xp11.2; identifica nuevas dianas terapéuticas y GPNMB como marcador diagnóstico |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Revisión (otro inhibidor de quinasas) | OncoTargets Ther | Perfil de nintedanib en tumores sólidos. Menciona a vandetanib entre los antiangiogénicos |
| [28477875](https://pubmed.ncbi.nlm.nih.gov/28477875/) | 2017 | Revisión (otro inhibidor de quinasas) | Bull Cancer | Mecanismo y eficacia de cabozantinib (VEGFR2, c-MET, RET), un inhibidor con dianas similares |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Revisión (cáncer de tiroides) | ASCO Educ Book | Tratamientos sistémicos del cáncer de tiroides avanzado. Vandetanib, inhibidor de RET, aprobado por la FDA en cáncer medular |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 11749002 | CAPRELSA 300 MG comprimidos recubiertos con película | Comprimido recubierto con película |
| 11749001 | CAPRELSA 100 MG comprimidos recubiertos con película | Comprimido recubierto con película |

Ambas autorizaciones pertenecen a Sanofi B.V.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (inhibidor de tirosina quinasas: VEGFR2, EGFR, RET) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto. La literatura de clase de los inhibidores de VEGFR describe toxicidad hepática y proteinuria, por lo que conviene vigilar la función hepática y renal |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje TxGNN alto y una lógica biológica razonable (bloqueo de VEGFR en tumores renales dependientes de HIF/VEGF). Pero la evidencia clínica directa se limita a un ensayo de Fase 2 completado sin resultados aportados y a dos ensayos terminados prematuramente con 10 pacientes en total. Además, falta la información de seguridad del prospecto, que la propia fuente marca como bloqueante. El resto de las indicaciones predichas (subtipos raros de carcinoma renal, angiolipoma, neumotórax espontáneo familiar) solo tienen respaldo del modelo (L5), y para las dos últimas no hay razón mecanística plausible.

**Para avanzar se necesita:**
- Obtener los resultados publicados de NCT00566995 (tasa de respuesta, supervivencia libre de progresión, seguridad)
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), que es el requisito bloqueante para la evaluación de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Revisar por qué el registro de la AEMPS no incluye el texto de la indicación aprobada y confirmarlo con la ficha técnica
- Comparar de forma indirecta con los inhibidores de VEGFR ya establecidos en carcinoma renal para definir si existe un nicho clínico
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


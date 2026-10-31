---
layout: default
title: Febuxostat
parent: Evidencia moderada (L3-L4)
nav_order: 326
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-31
monitor_inn: "FEBUXOSTAT"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "Lesch-Nyhan syndrome"]
description: "Febuxostat: nueva indicación predicha, Hipouricemia renal (hypouricemia, renal) (nivel de evidencia L4). Indicación original: No consta en los datos locales"
---

# Febuxostat
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

## Febuxostat: Hipouricemia renal (hypouricemia, renal)
{: .text-alpha }

## Resumen en Una Frase

Febuxostat es un inhibidor selectivo no purínico de la xantina oxidasa, originalmente utilizado para el tratamiento de la hiperuricemia.
El modelo TxGNN predice que podría ser efectivo para **hipouricemia renal**,
con **1 ensayo clínico** (de relevancia baja) y **2 publicaciones** que actualmente respaldan esta dirección de forma muy indirecta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hipouricemia renal (hypouricemia, renal) |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 7) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según el conocimiento general, febuxostat es un inhibidor selectivo no purínico de la xantina oxidasa que reduce el ácido úrico sérico, y su eficacia en hiperuricemia y gota está bien establecida.

Sin embargo, **la predicción es mecanísticamente cuestionable**. La hipouricemia renal es una condición de urato sérico ya bajo, causada por una reabsorción renal defectuosa de urato (pérdida de función de URAT1/SLC22A12 o GLUT9/SLC2A9). Reducir aún más el urato no corrige el defecto de fondo. Es probable que la puntuación del modelo se deba a la proximidad en la red a genes del metabolismo del urato y no a una razón terapéutica.

El único vínculo en la literatura es un reporte de un futbolista de 16 años con hipouricemia renal familiar y lesión renal aguda recurrente inducida por ejercicio, donde se planteó el uso de inhibidores de la xantina oxidorreductasa como prevención. Se trata de un uso indirecto y preventivo, no de un tratamiento de la hipouricemia en sí.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Fase 4 | Desconocido | 100 | Estudio prospectivo controlado sobre el efecto del control del ácido úrico en la recurrencia de cálculos y la función renal en pacientes con litiasis e hiperuricemia. Relevancia baja: probablemente no estudia hipouricemia renal, por lo que no constituye evidencia directa. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Revisión | Clinical Rheumatology | Actualización sobre hipouricemia (urato sérico < 2 mg/dL) y su etiología, dirigida a reumatólogos. |
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Reporte de caso | Internal Medicine | Futbolista de 16 años con hipouricemia renal familiar (mutaciones en URAT1) y lesión renal aguda recurrente por ejercicio; se plantea el uso de inhibidores no purínicos de la xantina oxidorreductasa como profilaxis. |

*Nota: la base de datos clasifica el segundo artículo como revisión, pero por su contenido descrito corresponde a un reporte de caso.*

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas monofármaco, ninguna cancelada). El texto de indicación aprobada no está disponible en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 08447014IP | ADENURIC 80 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 08447003IP1 | ADENURIC 120 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 83214 | Febuxostat Kern Pharma 120 mg EFG | Comprimido recubierto con película | No disponible |
| 83213 | Febuxostat Bluepharma 80 mg EFG | Comprimido recubierto con película | No disponible |
| 83602 | Febuxostat Accord 80 mg EFG | Comprimido recubierto con película | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones relacionadas en el grafo de conocimiento** (no provienen del prospecto): ictus, trastorno cerebrovascular, infarto cerebral, infarto de miocardio, trombosis coronaria y hemoglobinopatía.
- **Interacciones farmacológicas** (22 registradas en total; se resumen las principales):
  - **Mayores**: mercaptopurina, azatioprina, leflunomida, teriflunomida.
  - **Moderadas**: teofilina, aminofilina, dyphylline, oxtrifilina, metotrexato, tioguanina, clofarabina, epirrubicina, trabectedina, brentuximab vedotina, asparaginasa, pegaspargasa, naltrexona, interferón beta-1a/1b y peginterferón beta-1a.
- No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para esa información.
- Riesgo teórico adicional en las indicaciones alternativas: acumulación de xantina e hipoxantina con riesgo de nefropatía o litiasis por xantina.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (hipouricemia renal) carece de racionalidad mecanística, ya que reducir más el urato es contraproducente, y la única evidencia es un ensayo de relevancia baja y literatura indirecta (nivel L4). El modelo no respalda un avance por ahora.

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones del prospecto de la AEMPS (brecha de seguridad que bloquea el cribado de seguridad).
- Completar los datos del mecanismo de acción desde DrugBank.
- Considerar como líneas alternativas con mejor racionalidad el déficit parcial de HPRT y el síndrome de Lesch-Nyhan (control sintomático de la hiperuricemia, nivel L4, solo reportes de casos), evaluando el riesgo de nefropatía por xantina.
- Confirmar si febuxostat se usó realmente en los casos publicados y cuáles fueron los resultados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


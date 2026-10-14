---
layout: default
title: Chlorpromazine
parent: Evidencia moderada (L3-L4)
nav_order: 174
evidence_level: L4
indication_count: 10
---

# Chlorpromazine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Clorpromazina: De Trastorno Bipolar Maníaco y Esquizofrenia a Distrofia Retiniana

## Resumen en Una Frase

La clorpromazina es un antipsicótico clásico utilizado originalmente para el tratamiento de la esquizofrenia, los trastornos psicóticos y la fase maníaca del trastorno bipolar.
El modelo TxGNN predice que podría ser efectiva para **distrofia retiniana con o sin anomalías extraoculares**, pero **no existen ensayos clínicos** y solo hay **1 publicación**, que describe reacciones fototóxicas (una señal de efecto adverso, no terapéutica).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno bipolar maníaco, trastorno psicótico, esquizofrenia (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Distrofia retiniana con o sin anomalías extraoculares |
| Puntaje de Predicción TxGNN | 99.95% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información farmacológica conocida, la clorpromazina actúa como antagonista de múltiples receptores: dopaminérgicos (D1 a D5), serotoninérgicos (5-HT1A, 5-HT2A, 5-HT2C, 5-HT6, 5-HT7), adrenérgicos α2 y de histamina H1. Su efecto antipsicótico se atribuye principalmente al antagonismo del receptor D2.

La relación entre la indicación original (trastornos psiquiátricos) y la distrofia retiniana es muy débil. La única publicación disponible (JAMA, 1967) describe reacciones fototóxicas con dosis altas de clorpromazina y tioridazina. La clorpromazina se acumula en tejidos con melanina, como el epitelio pigmentario de la retina, lo que sugiere un posible **daño** y no un beneficio en esta enfermedad.

Por tanto, el puntaje elevado del modelo no está respaldado por un mecanismo terapéutico identificable y probablemente refleja asociaciones de red del grafo de conocimiento. Entre las demás predicciones del modelo, la más coherente es la esquizofrenia de inicio temprano (puntaje 99.47%, nivel L4), que es más una extensión a un subgrupo de edad de una indicación ya existente que un reposicionamiento verdadero. Sin embargo, su evidencia se limita a estudios observacionales, de imagen y farmacogenéticos, sin ensayos clínicos pediátricos o adolescentes.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [5336672](https://pubmed.ncbi.nlm.nih.gov/5336672/) | 1967 | Revisión / casos (toxicidad) | JAMA | Reacciones fototóxicas inducidas por dosis altas de clorpromazina y tioridazina; señal de seguridad, no de eficacia |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 42934 | LARGACTIL 100 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 23665 | LARGACTIL 25 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 19622 | LARGACTIL 5 mg/ml solución inyectable | Solución inyectable | No disponible |
| 23661 | LARGACTIL 40 mg/ml gotas orales en solución | Gotas orales en solución | No disponible |

Todas las autorizaciones son de medicamentos de un solo principio activo, vigentes, y su titular es Neuraxpharm Spain S.L.

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del texto del prospecto, por lo que deben verificarse): síndrome de QT largo (incluido el familiar), torsades de pointes, parada cardíaca súbita, enfermedad de la conducción cardíaca, infarto de miocardio, hipotensión ortostática, síndrome de taquicardia postural ortostática, atrofia multisistémica, epilepsia, enfermedades de los ganglios basales, distonía focal de la mano, blefaroespasmo, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, neutropenia, agranulocitosis, leucopenia, anemias (incluida la macrocítica), hemoglobinopatías, hiperglucemia, obesidad, hiperplasia benigna de próstata, carcinoma de mama femenino y abuso o dependencia de sustancias.
- **Interacciones farmacológicas**: los datos compilados corresponden a perfiles de afinidad por dianas farmacológicas (receptores dopaminérgicos, serotoninérgicos, adrenérgicos α2 e histaminérgico H1, entre otros) y no a interacciones con otros fármacos concretos. Estas dianas implican posible efecto aditivo con otros depresores del sistema nervioso central, antihipertensivos y fármacos que prolonguen el intervalo QT.
- **Señal específica de esta predicción**: la fototoxicidad y la acumulación en tejidos pigmentados, incluida la retina, aconsejan especial cautela en enfermedades oculares.

Para las advertencias principales y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para distrofia retiniana carece de ensayos clínicos y de un mecanismo terapéutico plausible, y la única publicación apunta a toxicidad retiniana potencial. El puntaje alto del modelo no basta para avanzar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto oficial de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas), que es un vacío bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, mediante consulta a DrugBank).
- Evaluar la toxicidad ocular y retiniana de la clorpromazina con estudios preclínicos o de mecanismo antes de considerar cualquier uso en enfermedades de la retina.
- Si se quiere priorizar una línea de investigación, considerar la esquizofrenia de inicio temprano como pregunta de investigación, con revisión de seguridad en población joven (síntomas extrapiramidales, sedación, efectos metabólicos) y comparación con antipsicóticos de segunda generación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


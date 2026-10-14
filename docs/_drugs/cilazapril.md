---
layout: default
title: Cilazapril
parent: Evidencia moderada (L3-L4)
nav_order: 181
evidence_level: L4
indication_count: 4
---

# Cilazapril
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **4** 
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

# Cilazapril: De Hipertensión Arterial a Hipertensión Pulmonar por Enfermedad Pulmonar y/o Hipoxia

*Nota: el informe se centra en la indicación predicha con mayor respaldo de evidencia (rango 2 de 4), ya que la predicha en primer lugar carece por completo de ensayos y literatura. Las demás predicciones se mencionan en la conclusión.*

## Resumen en Una Frase

Cilazapril es un inhibidor de la enzima convertidora de angiotensina (ECA), utilizado originalmente para el tratamiento de la hipertensión arterial.
El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar secundaria a enfermedad pulmonar y/o hipoxia**,
pero la evidencia actual se limita a **4 publicaciones preclínicas** (estudios en animales y cultivos celulares) y **ningún ensayo clínico**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (el texto de indicación de las autorizaciones españolas no está disponible; se toma de la base de conocimiento del modelo) |
| Nueva Indicación Predicha | Hipertensión pulmonar secundaria a enfermedad pulmonar y/o hipoxia |
| Puntaje de Predicción TxGNN | 99,20% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold (tratar como pregunta de investigación) |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, cilazapril es un inhibidor de la ECA que reduce la formación de angiotensina II, y su eficacia en hipertensión arterial está establecida. Mecanísticamente, podría ser aplicable a la hipertensión pulmonar asociada a hipoxia.

La actividad de la ECA en la arteria pulmonar contribuye a la vasoconstricción hipóxica y al remodelado vascular. Al reducir la angiotensina II, cilazapril podría atenuar ambos procesos. Tanto la hipertensión arterial sistémica como la pulmonar comparten la participación de la vasoconstricción y del remodelado de la pared vascular, lo que da coherencia biológica a la predicción.

No obstante, la evidencia procede solo de modelos animales y celulares. Los inhibidores de la ECA no son una terapia establecida para este grupo de hipertensión pulmonar, y no se han identificado estudios en humanos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [1708054](https://pubmed.ncbi.nlm.nih.gov/1708054/) | 1991 | Preclínico (animal) | J Cardiovasc Pharmacol | Cilazapril en ratas expuestas a hipoxia crónica durante 4 semanas: se evaluó su efecto sobre el engrosamiento de la capa media de las arterias pulmonares |
| [7712584](https://pubmed.ncbi.nlm.nih.gov/7712584/) | 1994 | Preclínico (animal) | Zhonghua Jie He He Hu Xi Za Zhi | En ratas, cilazapril protegió frente al aumento de la presión arterial pulmonar media y la caída de PaO2 en hipoxia crónica |
| [10072805](https://pubmed.ncbi.nlm.nih.gov/10072805/) | 1997 | Preclínico (animal) | Zhonghua Jie He He Hu Xi Za Zhi | Estudio del papel de la ECA arterial pulmonar local en el desarrollo de la hipertensión pulmonar hipóxica |
| [1378120](https://pubmed.ncbi.nlm.nih.gov/1378120/) | 1992 | In vitro (cultivo celular) | J Cardiovasc Pharmacol | Cilazapril y captopril aceleraron la recuperación de la hipoxia en agregados de miocitos cardíacos |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59330 | INOCAR 1 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 59329 | INOCAR 2,5 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 59328 | INOCAR 5 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó y solo identificó la interacción farmacológica con su diana, la enzima convertidora de angiotensina (ECA), lo cual corresponde a su mecanismo de acción y no a una interacción con otro fármaco.
- **Riesgo específico de la nueva indicación**: la hipotensión sistémica en pacientes hipóxicos es una posible preocupación de seguridad.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold (pregunta de investigación)**

**Justificación:**
El puntaje de TxGNN es alto (99,20%), pero la evidencia se limita a estudios preclínicos de los años 90, sin ensayos clínicos ni estudios en humanos, y los inhibidores de la ECA no son terapia establecida en este tipo de hipertensión pulmonar.

Las otras predicciones (hipertensión pulmonar de mecanismo multifactorial poco claro, enfermedad renal hipertensiva maligna e hipertensión renovascular maligna) se encuentran en nivel L5, sin ningún ensayo ni literatura, por lo que también quedan en **Hold**. En las dos últimas, además, preocupa el riesgo renal (lesión renal aguda, hiperpotasemia y estenosis de la arteria renal).

**Para avanzar se necesita:**
- Datos del mecanismo de acción confirmados (por ejemplo, desde DrugBank)
- Advertencias y contraindicaciones del prospecto de la AEMPS (actualmente sin datos y bloqueante para el cribado de seguridad)
- Estudios en humanos (observacionales o ensayos piloto de fase 2) en hipertensión pulmonar asociada a hipoxia
- Evaluación de la seguridad hemodinámica (hipotensión) en pacientes hipóxicos
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


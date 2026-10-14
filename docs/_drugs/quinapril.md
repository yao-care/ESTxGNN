---
layout: default
title: Quinapril
parent: Solo predicción del modelo (L5)
nav_order: 675
evidence_level: L5
indication_count: 5
---

# Quinapril
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

# Quinapril: De Hipertensión a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Quinapril es un inhibidor de la enzima convertidora de angiotensina (IECA), utilizado originalmente para el tratamiento de la hipertensión arterial.
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden directamente esta predicción; se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertensión arterial (trastorno hipertensivo) |
| Nueva Indicación Predicha | Hipertensión renovascular maligna |
| Puntaje de Predicción TxGNN | 99.86% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 12 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Quinapril es un IECA ya autorizado para la hipertensión. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, los IECA bloquean la conversión de angiotensina I en angiotensina II, reduciendo la vasoconstricción y el tono vascular.

La hipertensión renovascular depende en gran medida de la activación del sistema renina-angiotensina, por lo que el vínculo mecanístico es plausible. En la práctica, esta indicación es más una extensión de la indicación existente (un subtipo de hipertensión) que un reposicionamiento genuino. Es probable que la puntuación alta refleje la cercanía en el grafo de conocimiento con la indicación de hipertensión.

Un punto de cautela importante: los IECA pueden provocar un deterioro agudo de la función renal en casos de estenosis bilateral de la arteria renal, de modo que la seguridad exige una valoración cuidadosa.

### Otras indicaciones predichas (para contexto)

| Indicación predicha | Puntaje TxGNN | Nivel | Recomendación |
|------|------|------|------|
| Enfermedad renal hipertensiva maligna | 99.86% | L5 | Hold |
| Hipertensión pulmonar por enfermedad pulmonar y/o hipoxia | 99.85% | L4 | Pregunta de investigación |
| Hipertensión pulmonar de mecanismo multifactorial poco claro | 99.85% | L5 | Hold |
| Síndrome de Braddock | 99.79% | L5 | Hold |

De ellas, solo la hipertensión pulmonar por hipoxia cuenta con literatura preclínica: un estudio en ratas (PMID 8873672, *Circulation*, 1996) indica que la inhibición de la ECA tisular con quinapril reduce la hipertensión pulmonar hipóxica y el remodelado vascular. Es evidencia indirecta y animal; no hay estudios en humanos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal (hipertensión renovascular maligna).

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61733 | ECTREN 40 mg comprimidos recubiertos con película | Comprimido recubierto | No especificada en los datos |
| 59203 | LIDALTRIN 20 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en los datos |
| 61672 | LIDALTRIN 40 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en los datos |
| 59191 | ECTREN 20 mg comprimidos recubiertos con película | Comprimido recubierto | No especificada en los datos |
| 59082 | ACUPREL 20 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en los datos |

Se muestran 5 de las 12 autorizaciones vigentes (todas de monofármaco, ninguna cancelada).

## Consideraciones de Seguridad

Según el grafo de conocimiento, quinapril presenta relaciones de contraindicación con las siguientes condiciones (no proceden del texto del prospecto):

- **Renales y metabólicas**: enfermedad renal, anuria, déficit de potasio, diabetes mellitus, cetoacidosis diabética, hiperuricemia, gota.
- **Hepáticas y digestivas**: enfermedad hepática, encefalopatía/coma hepático, enfermedad de la vesícula biliar, pancreatitis.
- **Angioedema**: angioedema adquirido, hereditario (incluido el déficit de C1-inhibidor), no histamínico e inducido por bloqueadores del sistema renina-angiotensina-aldosterona.
- **Hematológicas**: neutropenia, agranulocitosis.
- **Otras**: trastorno hipotensivo, hiperparatiroidismo, osteítis fibrosa, lupus eritematoso sistémico (incluido el pediátrico), enfermedad del tejido conectivo, enfermedades óseas y del cartílago, ictericia neonatal, piouréter.

**Interacciones farmacológicas** (se detectaron 100 en total; se muestran las más relevantes de las 20 recuperadas):
- **Mayor**: citrato de potasio (riesgo de hiperpotasemia).
- **Moderadas**: metformina, ácido acetilsalicílico, corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), canagliflozina, dapagliflozina, clorpropamida, bupropión, morfina, atropina, doxiciclina, tetraciclina, bisacodilo, ácido picosulfúrico, polietilenglicol con electrolitos y pancrelipasa.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipertensión renovascular maligna tiene una puntuación alta (99.86%), pero es de nivel L5: no hay ensayos ni literatura, y es esencialmente una extensión de la indicación de hipertensión ya autorizada. Además, el riesgo renal de los IECA en estenosis bilateral de la arteria renal exige cautela.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias y contraindicaciones oficiales), pues esta carencia bloquea el cribado de seguridad.
- Completar los datos del mecanismo de acción de quinapril.
- Realizar una búsqueda sistemática de literatura y ensayos clínicos sobre IECA en hipertensión renovascular.
- Definir un plan de monitoreo de función renal y potasio para cualquier evaluación futura.
- Como línea de investigación secundaria, valorar la hipertensión pulmonar por hipoxia (nivel L4), que cuenta con respaldo preclínico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


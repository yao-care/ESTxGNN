---
layout: default
title: Siltuximab
parent: Solo predicción del modelo (L5)
nav_order: 736
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Siltuximab: nueva indicación predicha, Mastocitoma extracutáneo (nivel de evidencia L5). Indicación original: Enfermedad de Castleman (según el grafo de conocimiento"
monitor_inn: "SILTUXIMAB"
predicted_indications: ["extracutaneous mastocytoma", "hepatic infarction", "hepatic veno-occlusive disease", "peliosis hepatis", "Kaposi's sarcoma (disease)", "autosomal recessive familial Mediterranean fever", "aggressive systemic mastocytosis", "autosomal dominant familial periodic fever"]
---

# Siltuximab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Siltuximab: De Enfermedad de Castleman a Mastocitoma Extracutáneo

## Resumen en Una Frase

Siltuximab es un anticuerpo monoclonal anti-IL-6, utilizado originalmente para el tratamiento de la enfermedad de Castleman (y, según el grafo de conocimiento, la enfermedad de Kimura).
El modelo TxGNN predice que podría ser efectivo para **mastocitoma extracutáneo**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata de una predicción puramente computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Castleman (según el grafo de conocimiento; el texto de indicación autorizado no está disponible) |
| Nueva Indicación Predicha | Mastocitoma extracutáneo |
| Puntaje de Predicción TxGNN | 99.64% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos. Según la información conocida, siltuximab es un anticuerpo monoclonal que bloquea la interleucina-6 (IL-6), y su eficacia en la enfermedad de Castleman, un trastorno linfoproliferativo en el que la IL-6 tiene un papel central, ha sido comprobada.

Para el mastocitoma extracutáneo, los datos compilados no respaldan ningún vínculo mecanístico: el papel de la señalización de IL-6 en las neoplasias de mastocitos es especulativo. El puntaje alto de TxGNN es únicamente una predicción computacional, sin ensayos ni literatura que la corroboren.

### Otras indicaciones predichas (para contexto)

| Rango | Enfermedad | Puntaje TxGNN | Nivel | Evidencia disponible |
|------|------|------|------|------|
| 2 | Infarto hepático | 99.44% | L5 | Ninguna |
| 3 | Enfermedad venooclusiva hepática | 99.40% | L5 | Ninguna; vínculo teórico por citocinas inflamatorias y daño endotelial |
| 4 | Peliosis hepática | 99.29% | L5 | Ninguna |
| 5 | Sarcoma de Kaposi | 99.28% | L4 | Una revisión indirecta sobre Castleman |
| 6 | Fiebre mediterránea familiar autosómica recesiva | 99.22% | L5 | Ninguna; vínculo biológicamente plausible (IL-6 como mediador) |
| 7 | Mastocitosis sistémica agresiva | 99.16% | L5 | Ninguna |
| 8 | Fiebre periódica familiar autosómica dominante | 99.05% | L5 | Ninguna; vínculo plausible pero no probado |

Cabe destacar que el sarcoma de Kaposi presenta el vínculo indirecto más plausible: el KSHV es un factor causal en un subconjunto de la enfermedad de Castleman multicéntrica, y la IL-6 viral y humana contribuye a la patología asociada, incluido el síndrome inflamatorio de citocinas por KSHV.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para mastocitoma extracutáneo.

(Para contexto, la única publicación recuperada corresponde a otra indicación predicha, el sarcoma de Kaposi: [39970477](https://pubmed.ncbi.nlm.nih.gov/39970477/), 2024, Revisión, AIDS Reviews, "Castleman's disease: one disease, multiple etiologies", revisión de las etiologías de la enfermedad de Castleman; evidencia indirecta.)

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 114928001 | SYLVANT 100 MG POLVO PARA CONCENTRADO PARA SOLUCION PARA PERFUSION | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 100 interacciones en total; se muestran las 20 primeras recuperadas.
  - **Mayor**: deferiprona.
  - **Moderada**: simvastatina, apixabán, warfarina, rivaroxabán, dicumarol, lidocaína, hidrocodona, teofilina, roflumilast, aminofilina, oxtrifilina, tacrolimus, fentanilo, nifedipino, toxoide tetánico inactivado.
  - **Menor**: sulfato, acetato, gluconato y cloruro de zinc.

  Es plausible que varias de estas interacciones (p. ej., sustratos del CYP450 como simvastatina, warfarina o teofilina) se relacionen con la normalización de enzimas hepáticas al bloquear la IL-6, pero los datos compilados no lo detallan; debe verificarse en el prospecto.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para mastocitoma extracutáneo se basa solo en el modelo (L5), sin ensayos clínicos ni literatura, y sin un vínculo mecanístico respaldado por los datos.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y análisis del vínculo entre la señalización de IL-6 y las neoplasias de mastocitos
- Revisión de la ficha técnica de AEMPS (advertencias y contraindicaciones), necesaria antes de cualquier evaluación de seguridad
- Búsqueda de estudios preclínicos o series de casos que respalden la indicación
- Valorar priorizar el sarcoma de Kaposi, que cuenta con un vínculo indirecto más plausible (L4), como alternativa a explorar
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Framycetin
parent: Solo predicción del modelo (L5)
nav_order: 362
evidence_level: L5
indication_count: 7
---

# Framycetin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Framicetina: De Indicación Original No Especificada a Colangitis Esclerosante

## Resumen en Una Frase

Framicetina (framycetin, neomicina B) es un antibiótico aminoglucósido de absorción sistémica muy baja, comercializado en España en formulaciones tópicas y óticas; los datos de AEMPS compilados no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **colangitis esclerosante**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.
La predicción se basa únicamente en el modelo (nivel de evidencia L5).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (las autorizaciones no incluyen texto de indicación) |
| Nueva Indicación Predicha | Colangitis esclerosante |
| Puntaje de Predicción TxGNN | 99,66% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos de mecanismo de acción (MOA) no están disponibles en la información compilada. Según la información conocida, la framicetina es un aminoglucósido (neomicina B) con actividad antibacteriana de amplio espectro, especialmente frente a bacterias Gram negativas. Su absorción sistémica es muy escasa, por lo que se utiliza sobre todo por vía tópica (piel, ojo, oído, nariz).

En la colangitis esclerosante primaria se ha explorado la hipótesis del eje intestino-hígado, con antibióticos dirigidos al intestino (por ejemplo, vancomicina oral). Por analogía, un aminoglucósido de acción local en el intestino podría tener cierto interés teórico. Sin embargo, no existe evidencia directa con framicetina y la relación mecanística no puede verificarse.

Cabe señalar que el puntaje elevado de TxGNN (99,66%) es solo una predicción del modelo y no sustituye a la evidencia clínica. Además, las formulaciones comercializadas en España (crema, pomada y gotas óticas) no son compatibles de forma evidente con una indicación hepatobiliar; la compatibilidad de vías de administración está pendiente de evaluación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 49840 | ABICREM 0,25 MG/G + 5 MG/G CREMA | Crema | No especificada en los datos |
| 42725 | ALDODERMA 1 MG/G + 3,5 MG/G POMADA | Pomada | No especificada en los datos |
| 55286 | OTOMIDRIN 8 MG/ML + 0,25 MG/ML + 20 MG/ML GOTAS ÓTICAS EN SUSPENSIÓN | Gotas óticas en suspensión | No especificada en los datos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en los datos compilados. Como aspecto general de la clase, el uso sistémico de aminoglucósidos se asocia a nefrotoxicidad y ototoxicidad, lo que limita su aplicabilidad sistémica.

## Otras Predicciones del Modelo (Contexto)

| Rango | Indicación Predicha | Puntaje TxGNN | Valoración |
|------|------|------|------|
| 2 | Infección del tracto urinario | 99,42% | Biológicamente plausible por la clase, pero sin evidencia aportada; existen aminoglucósidos mejor respaldados (gentamicina, amikacina) |
| 3 | Deficiencia congénita de protrombina | 99,41% | Sin vínculo mecanístico plausible; probable falso positivo |
| 4 | Uretritis por Ureaplasma | 99,28% | Débilmente plausible; habitualmente se tratan con tetraciclinas o macrólidos |
| 5 | Uretritis gonocócica | 99,28% | Justificación a nivel de clase; las guías actuales prefieren otros agentes por resistencias |
| 6 | Enfermedad inflamatoria uterina | 99,18% | Justificación a nivel de clase; limitada por la baja disponibilidad sistémica |
| 7 | Pielonefritis xantogranulomatosa | 99,18% | Manejo principalmente quirúrgico; preocupación por nefrotoxicidad |

Todas ellas son de nivel L5 y sin ensayos clínicos ni literatura aportada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para colangitis esclerosante se apoya solo en el modelo (L5), sin ensayos ni publicaciones, sin datos de mecanismo de acción y con formulaciones comercializadas de uso tópico/ótico poco compatibles con la indicación propuesta.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), indispensable para cualquier evaluación de seguridad.
- Completar los datos de mecanismo de acción (por ejemplo, mediante DrugBank).
- Confirmar la indicación original aprobada de cada autorización.
- Realizar una revisión sistemática de la literatura sobre aminoglucósidos orales en colangitis esclerosante.
- Evaluar la compatibilidad de la vía de administración y la viabilidad de una formulación oral/intestinal.
- Valorar si alguna de las otras indicaciones predichas (por ejemplo, infecciones por Gram negativos) ofrece una vía más realista.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


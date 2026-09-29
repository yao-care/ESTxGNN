---
layout: default
title: Estramustine
parent: Solo predicción del modelo (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
---

# Estramustine
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

# Estramustina: De Indicación Original No Registrada a Susceptibilidad Genética a Cáncer de Próstata/Cerebro

## Resumen en Una Frase

Estramustina es un conjugado de estradiol y mostaza nitrogenada (carbamato) con actividad antimicrotubular, comercializado en España como Estracyt cápsulas. La ficha de AEMPS incluida en el Evidence Pack no trae el texto de la indicación original.
El modelo TxGNN sitúa en primer lugar **susceptibilidad genética a cáncer de próstata/cerebro** (puntaje 99.99%). Esa etiqueta no es una enfermedad tratable y **no tiene ensayos clínicos ni publicaciones** que la respalden.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Susceptibilidad genética a cáncer de próstata/cerebro |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Esta predicción **no es razonable como candidata de reposicionamiento**. Es una etiqueta de susceptibilidad genética, no un estado de enfermedad que se pueda tratar. El propio análisis del pack indica que el puntaje del grafo (0.9999) no discrimina entre candidatas, porque todas puntúan de forma parecida.

Los datos de mecanismo de acción no están disponibles en DrugBank. La literatura del pack describe la estramustina como un carbamato de estradiol y mostaza nitrogenada. Se une a la tubulina y a proteínas asociadas a microtúbulos, y también a la proteína de unión a estramustina (EMBP), que abunda en la próstata. Este perfil explica la asociación con tejido prostático, pero no aporta una razón mecanística para tratar una susceptibilidad genética.

Otras predicciones del mismo farmaco sí tienen respaldo (ver la sección de otras predicciones más abajo).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Otras Predicciones del Modelo con Evidencia

| Posición | Indicación | Nivel | Recomendación | Respaldo disponible |
|------|------|------|------|------|
| 6 | Cáncer de órgano reproductor masculino | L1 | Proceed with Guardrails | Más de 40 ensayos, incluidos varios de Fase 3 completados, p. ej. [NCT00004001](https://clinicaltrials.gov/study/NCT00004001) (docetaxel + estramustina vs. mitoxantrona + prednisona, n=770). |
| 8 | Carcinoma de mama femenino | L2 | Pregunta de investigación | [NCT02866955](https://clinicaltrials.gov/study/NCT02866955) (Fase 2, completado, n=100); [PMID 11697838](https://pubmed.ncbi.nlm.nih.gov/11697838/) (Fase 2, estramustina sola tras fracaso de antraciclinas y taxanos). |
| 4 | Neoplasia benigna del sistema reproductor | L4 | Hold | 13 artículos sobre EMBP como biomarcador en próstata; no son evidencia de tratamiento. |
| 2, 3, 5, 7, 9, 10 | Fibroma de próstata, tumor de Brenner, leiomioma de próstata, tumor filodes prostático, VIH, enfermedad fibroquística de mama | L5 | Hold | Solo predicción del modelo. |

**Salvedades sobre la posición 6:** en la práctica es cáncer de próstata, donde la estramustina ya se usa, así que no es una señal de reposicionamiento real. Además, el ensayo de Fase 3 evalúa una combinación con docetaxel, por lo que no aísla la contribución de la estramustina. No se proporcionaron resultados de eficacia ni toxicidad.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 54190 | ESTRACYT 140 mg CÁPSULAS DURAS (Pfizer S.L.) | Cápsula dura |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimicrotubular; conjugado estradiol-mostaza nitrogenada) |
| Riesgo de Mielosupresión | Bajo como agente único, según un estudio de Fase 2 en cáncer de mama (PMID 11697838, que destaca la ausencia de toxicidad hematológica). En combinación con taxanos u otros citotóxicos puede aumentar. |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal (parámetros generales de quimioterapia; confirmar con el prospecto) |
| Protección en Manejo | Seguir las regulaciones de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. La búsqueda de interacciones farmacológicas no devolvió resultados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación en primer lugar es una etiqueta de susceptibilidad genética, sin ensayos ni literatura y con nivel L5. El puntaje del modelo no discrimina entre candidatas, por lo que no justifica avanzar.

**Para avanzar se necesita:**
- Descargar el prospecto de AEMPS y extraer indicación aprobada, advertencias y contraindicaciones.
- Completar el mecanismo de acción desde DrugBank.
- Aclarar si se evaluará esta predicción o, más bien, la de cáncer de mama (posición 8), que es la que tiene evidencia clínica en una indicación distinta de la original.
- Si se avanza con cáncer de mama, obtener los resultados y la toxicidad, incluido el riesgo tromboembólico, de [NCT02866955](https://clinicaltrials.gov/study/NCT02866955) y de las publicaciones primarias.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


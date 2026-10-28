---
layout: default
title: Cetuximab
parent: Solo predicción del modelo (L5)
nav_order: 168
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "CETUXIMAB"
predicted_indications: ["bronchial adenomas/carcinoids childhood", "chondroid hamartoma", "ductal or ductular proliferation", "non-seminomatous lesion", "tumor of testis and paratestis", "odontogenic cyst", "thyroglossal duct cyst", "epiglottis neoplasm", "cystic neoplasm", "pre-malignant neoplasm"]
description: "Cetuximab: nueva indicación predicha, Bronchial adenomas/carcinoids childhood (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Cetuximab
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

## Cetuximab: Bronchial adenomas/carcinoids childhood
{: .text-alpha }

## Resumen en Una Frase

Cetuximab es un anticuerpo monoclonal dirigido contra el receptor del factor de crecimiento epidérmico (EGFR), utilizado originalmente en el cáncer colorrectal y en el carcinoma escamocelular de cabeza y cuello.
El modelo TxGNN predice que podría ser efectivo para **adenomas/carcinoides bronquiales infantiles**, aunque **no existen ensayos clínicos ni publicaciones** que respalden esta predicción (solo predicción del modelo).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Bronchial adenomas/carcinoids childhood |
| Puntaje de Predicción TxGNN | 0.9995 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | Comercializado (registros vigentes: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Cetuximab es un anticuerpo que se une al EGFR, un receptor frecuentemente sobreexpresado en tumores epiteliales. Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción, pero sí confirman que el EGFR es su diana farmacológica. Su uso está establecido en el cáncer colorrectal metastásico con EGFR expresado y en tumores escamosos de cabeza y cuello, en combinación con radioterapia.

Para los adenomas/carcinoides bronquiales infantiles, los datos aportados no muestran ningún vínculo entre cetuximab y esta enfermedad. La predicción se basa únicamente en la puntuación del modelo, por lo que la relación con las indicaciones originales sigue sin evaluarse y la plausibilidad mecanística es débil.

### Otras predicciones con más respaldo

Entre las 10 principales predicciones, dos cuentan con algo más de evidencia, aunque ninguna alcanza un nivel alto:

- **Neoplasia quística (rango 9, L2):** la evidencia se centra en el carcinoma adenoide quístico y otros carcinomas de glándulas salivales. Incluye el ensayo de Fase 1/2 NCT01192087 (cetuximab + IMRT + boost de iones de carbono, estado desconocido) y un estudio de Fase 2 en carcinomas salivales (PMID 18804410). Los resultados no pueden darse por positivos sin revisar el texto completo.
- **Neoplasia premaligna (rango 10, L2):** el ensayo de Fase 2 NCT00524017 evaluó cetuximab en monoterapia en lesiones premalignas de alto riesgo del tracto aerodigestivo superior. Está completado, pero no se aportaron resultados. La toxicidad crónica (reacciones cutáneas y a la perfusión) preocupa en un contexto de prevención.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la indicación principal (adenomas/carcinoides bronquiales infantiles).

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 04281003 | ERBITUX 5 MG/ML SOLUCIÓN PARA PERFUSIÓN (Merck Europe B.V.) | Solución para perfusión | No disponible en los datos compilados |

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-EGFR) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar el prospecto; en los datos compilados se mencionan reacciones cutáneas y reacciones a la perfusión como preocupaciones de tolerabilidad |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 20 registros de interacción. Los principales:
  - **Mayores:** talidomida y ácido aminolevulínico.
  - **Moderadas:** inhibidores de la bomba de protones (rabeprazol, omeprazol, dexlansoprazol, esomeprazol, lansoprazol, pantoprazol), fluorouracilo, capecitabina, cisplatino, carboplatino, oxaliplatino, idelalisib, metoxaleno, verteporfina, omacetaxina y metilaminolevulinato/ácido aminolevulínico tópico.
  - Además figura la interacción farmacológica con su diana, el EGFR.

Consultar el prospecto para el resto de la información de seguridad (advertencias y contraindicaciones).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación principal predicha solo cuenta con la puntuación del modelo (L5), sin ensayos ni literatura, y no hay un vínculo mecanístico demostrado con los carcinoides bronquiales infantiles.

**Para avanzar se necesita:**
- Datos de mecanismo de acción detallados y una evaluación de la similitud con las indicaciones originales.
- Revisión del prospecto de la AEMPS (advertencias y contraindicaciones), cuya ausencia bloquea el cribado de seguridad.
- Evidencia preclínica o clínica específica en carcinoides bronquiales (expresión de EGFR en el tejido tumoral).
- Priorizar, como líneas alternativas de investigación, la revisión de resultados de NCT01192087 y PMID 18804410 (carcinomas de glándulas salivales) y de NCT00524017 (lesiones premalignas aerodigestivas).
- Valorar un plan de monitoreo de seguridad, dadas las reacciones cutáneas y a la perfusión asociadas a cetuximab.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


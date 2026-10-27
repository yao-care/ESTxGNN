---
layout: default
title: Cemiplimab
parent: Solo predicción del modelo (L5)
nav_order: 162
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cemiplimab: nueva indicación predicha, Carcinoma adenoescamoso de vesícula biliar (nivel de evidencia L5). Indicación original: Carcinoma escamoso (según el grafo de conocimiento"
monitor_inn: "CEMIPLIMAB"
predicted_indications: ["gallbladder adenosquamous carcinoma", "rectal cloacogenic carcinoma", "external ear basal cell carcinoma", "adenosquamous prostate carcinoma", "urethral verrucous carcinoma", "pancreatic adenosquamous carcinoma"]
---

# Cemiplimab
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

## Cemiplimab: De Carcinoma Escamoso a Carcinoma Adenoescamoso de Vesícula Biliar
{: .text-alpha }

## Resumen en Una Frase

Cemiplimab es un anticuerpo monoclonal que bloquea PD-1 y se utiliza originalmente para el tratamiento del carcinoma escamoso (en particular, el carcinoma escamoso cutáneo).
El modelo TxGNN predice que podría ser efectivo para **carcinoma adenoescamoso de vesícula biliar**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma escamoso (según el grafo de conocimiento; el texto de indicación de la autorización no está disponible) |
| Nueva Indicación Predicha | Carcinoma adenoescamoso de vesícula biliar |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Cemiplimab es un anticuerpo que bloquea el receptor PD-1 (CD279, gen PDCD1) e impide su interacción con PD-L1, con una IC50 inferior a 1 nM en ensayos ELISA. Al liberar el freno inmunitario sobre los linfocitos T, favorece la respuesta antitumoral. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco; esta descripción se basa en la información farmacológica general de la clase.

La indicación original es el carcinoma escamoso, en particular el cutáneo, donde aproximadamente el 50% de los pacientes con enfermedad avanzada respondió al tratamiento en los ensayos publicados. El carcinoma adenoescamoso de vesícula biliar comparte un componente escamoso, lo que podría hacer plausible una respuesta al bloqueo de PD-1.

Sin embargo, esta relación es solo una hipótesis: no hay datos de cemiplimab en esta enfermedad. El carcinoma escamoso cutáneo está impulsado por radiación UV con alta carga mutacional, una característica que no necesariamente comparten los tumores de vesícula biliar. La predicción debe tratarse como generadora de hipótesis.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1191376001 | LIBTAYO 350 MG CONCENTRADO PARA SOLUCIÓN PARA PERFUSIÓN | Concentrado para solución para perfusión | No disponible en los datos compilados |

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo anti-PD-1); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Bajo (no es un efecto característico de esta clase; consultar el prospecto) |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 9 interacciones de nivel moderado, todas con corticosteroides: hidrocortisona, triamcinolona, dexametasona, betametasona, budesonida, prednisolona, prednisona, metilprednisolona y deflazacort. Los corticosteroides pueden reducir el efecto inmunitario de cemiplimab, por lo que su uso concomitante requiere valoración clínica.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje TxGNN alto (99.99%), pero no cuenta con ensayos clínicos ni literatura que la respalden (nivel L5), y el mecanismo se apoya solo en conocimiento general de la clase farmacológica.

**Para avanzar se necesita:**
- Revisión de la literatura y de registros de ensayos específicos sobre carcinoma adenoescamoso de vesícula biliar y PD-1.
- Datos detallados del mecanismo de acción y análisis de similitud con la indicación original.
- Advertencias y contraindicaciones del prospecto de la AEMPS (información de seguridad no disponible en los datos compilados).
- Evaluación de la compatibilidad de la vía de administración (pendiente).

### Nota sobre otras indicaciones predichas

Entre las demás predicciones, solo el **carcinoma basocelular del oído externo** cuenta con alguna literatura: un reporte de caso (PMID 34157152, 2021, *Clinical and Experimental Dermatology*) sobre una respuesta duradera tras suspender cemiplimab en un carcinoma basocelular localmente avanzado (nivel L4, "Research Question"). Se trata de evidencia de un solo paciente y no establece específicamente la localización en el oído externo. Las otras ocho predicciones restantes son únicamente predicciones del modelo (L5, Hold).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


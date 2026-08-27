---
layout: default
title: Abacavir
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 3
---

# Abacavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Usando el conocimiento farmacológico contenido en el propio Evidence Pack (los ensayos clínicos describen explícitamente el uso de abacavir en "HIV-1 infected... subjects") para reconstruir el contexto de uso original, dado que los campos estructurados `original_indications` y `taiwan_regulatory.licenses` están vacíos. A continuación el informe:

---

# Abacavir: De Infección por VIH a Síndrome de Inmunodeficiencia Felina (FIV)

## Resumen en Una Frase

Abacavir es un inhibidor nucleosídico de la transcriptasa inversa (ITIAN) cuyo uso establecido, según se desprende de los propios ensayos clínicos recogidos en este dossier, es el tratamiento de la infección por VIH-1 en combinación con otros antirretrovirales.
El modelo TxGNN predice que podría ser efectivo para el **Síndrome de Inmunodeficiencia Felina (FIV)**, una enfermedad vírica de gatos mecanísticamente análoga al VIH,
con **4 ensayos clínicos indirectos** (sobre VIH humano, no sobre FIV) y **1 publicación in vitro específica** que respaldan de forma parcial esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH-1 (uso antirretroviral establecido; no consta texto de indicación aprobada en los datos regulatorios disponibles) |
| Nueva Indicación Predicha | Síndrome de Inmunodeficiencia Felina (FIV) |
| Puntaje de Predicción TxGNN | 99.79% |
| Nivel de Evidencia | L4 (estudio in vitro/preclínico; los ensayos clínicos disponibles no son directamente sobre FIV) |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información conocida derivada de los propios ensayos clínicos incluidos en este dossier, abacavir es un inhibidor nucleosídico de la transcriptasa inversa (ITIAN), utilizado en combinación con otros antirretrovirales (lamivudina, dolutegravir, raltegravir) para el tratamiento de la infección por VIH-1 en pacientes sin tratamiento previo. Su eficacia en esta indicación está solidamente respaldada por múltiples ensayos de Fase 3 completados.

El FIV (virus de inmunodeficiencia felina) es un lentivirus felino mecanísticamente análogo al VIH, que depende igualmente de la transcriptasa inversa para replicarse. Esto hace plausible, en principio, que un inhibidor de esta enzima activo frente a VIH-1 pueda tener actividad frente a FIV. De hecho, esta hipótesis cuenta con respaldo directo en la literatura: el estudio de Bisset et al. (2002) demostró en modelo in vitro que la combinación de zidovudina, lamivudina y abacavir suprime la replicación de FIV.

Es importante señalar, sin embargo, que los 4 ensayos clínicos recuperados para esta indicación corresponden todos a estudios en humanos con VIH-1 (no en gatos con FIV), por lo que constituyen evidencia indirecta de la actividad antirretroviral de abacavir en general, pero no evidencia clínica directa de eficacia en FIV. La única evidencia específica de FIV es un estudio in vitro de 2002. Por tanto, la plausibilidad mecanística es razonable, pero la evidencia clínica directa para la indicación predicha es todavía escasa.

---

## Evidencia de Ensayos Clínicos

*Nota: los siguientes ensayos documentan el uso de abacavir en VIH-1 humano (indicación de origen) y se listan como evidencia de respaldo mecanístico/farmacológico indirecto; no son ensayos realizados en FIV felino.*

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Fase 3 | Completado | 844 | Dolutegravir + abacavir/lamivudina vs. Atripla en VIH-1 sin tratamiento previo, 96 semanas |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Fase 3 | Completado | 828 | Dolutegravir + ITIAN dual (incl. abacavir/lamivudina) vs. raltegravir en VIH-1 sin tratamiento previo |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Fase 2 | Completado | 208 | Selección de dosis de dolutegravir combinado con abacavir/lamivudina o tenofovir/emtricitabina en VIH-1 |
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Fase 3 | Completado | 13 | Seguridad, eficacia y farmacocinética en SNC de dolutegravir + abacavir/lamivudina en VIH-1, 96 semanas |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Estudio in vitro | Antiviral Research | La combinación de zidovudina, lamivudina y abacavir suprime la replicación in vitro del virus de inmunodeficiencia felina (FIV), respaldando el modelo felino como análogo del VIH |

---

## Otras Señales Predichas por TxGNN (Prioridad Menor)

Además del FIV, el modelo generó otras dos señales para abacavir que se documentan aquí por transparencia, con prioridad claramente inferior:

| Indicación | Score TxGNN | Evidencia Disponible | Nivel de Evidencia | Recomendación |
|------|------|------|------|------|
| Infección por virus de inmunodeficiencia de simios (SIV) | 99.79% | 0 ensayos clínicos; 1 estudio in vitro (PMID [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/), 2004, susceptibilidad de VIH-2/SIV/SHIV a antirretrovirales) | L4 (preclínico) | Hold |
| Trastorno del neurodesarrollo con marcha atáxica, ausencia de habla y disminución de sustancia blanca cortical | 99.78% | Sin ensayos clínicos ni literatura | L5 | Hold |

Para la segunda señal, el propio análisis mecanístico ya concluye que no existe ningún ensayo, literatura, ni mecanismo biológico conocido o inferible que vincule abacavir (inhibidor de transcriptasa inversa) con esta rara enfermedad del neurodesarrollo, por lo que se considera muy probablemente un artefacto de proximidad en el espacio de embeddings del grafo de conocimiento, no una relación farmacológica real.

---

## Información de Mercado en España

Abacavir no cuenta actualmente con autorizaciones de comercialización registradas en los datos regulatorios evaluados (0 licencias, estado: no comercializado). No es posible presentar una tabla de autorizaciones ni de indicaciones aprobadas locales con la información disponible en este dossier.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Cabe destacar que la ficha técnica y las advertencias/contraindicaciones oficiales (fuente TFDA) no están disponibles en este dossier y constituyen un vacío de datos de severidad **bloqueante**, que impide actualmente avanzar a la evaluación de seguridad inicial (S1).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La hipótesis mecanística (inhibición de la transcriptasa inversa aplicable a lentivirus análogos al VIH) es razonable y cuenta con un estudio in vitro específico de apoyo, pero la evidencia clínica directa para el síndrome de inmunodeficiencia felina es inexistente (los ensayos disponibles son en humanos con VIH-1, no en gatos), y un vacío de datos bloqueante en materia de seguridad impide continuar con la evaluación formal.

**Para avanzar se necesita:**
- Obtener la ficha técnica/prospecto oficial (TFDA/AEMPS) con advertencias y contraindicaciones (vacío bloqueante, DG001)
- Completar los datos de mecanismo de acción (MOA) desde DrugBank u otra fuente primaria (DG002)
- Aclarar la vía regulatoria aplicable, dado que el FIV es una enfermedad exclusivamente felina (posible vía de uso veterinario, distinta del marco humano habitual)
- Buscar estudios in vivo o clínicos en gatos con FIV que vayan más allá del único estudio in vitro de 2002
- Confirmar el estado real de comercialización de abacavir en el mercado evaluado, dado que el dossier indica 0 licencias
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


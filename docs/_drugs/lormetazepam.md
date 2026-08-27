---
layout: default
title: Lormetazepam
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 10
---

# Lormetazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Usando el Evidence Pack proporcionado, genero el informe. No he necesitado ninguna skill adicional: es una tarea de redacción directa siguiendo la plantilla que usted mismo especificó.

Nota antes del informe: `original_moa`, `original_indications` y `taiwan_regulatory.licenses` están vacíos (DG001/DG002 son data gaps *Blocking*/*High*). El propio dato de `repurposing_rationale` del rank 1 indica que Insomnio es, de hecho, la indicación ya aprobada de Lormetazepam en otros mercados europeos (Noctamid/Loramet) — no un reposicionamiento genuino. Reflejo esto explícitamente en vez de inventar una "indicación original" que no está en los datos. Reevalué el Nivel de Evidencia de forma independiente según la regla L1–L5 (solo hay 1 ECA Fase 3 *completado*, no ≥2) y obtengo **L2**, no el L1 que aparece en el campo interno `scoring` del pack.

---

# Lormetazepam: De Benzodiazepina No Comercializada en España a Insomnio

## Resumen en Una Frase

Lormetazepam es una benzodiazepina hipnótica (derivado 3-hidroxi) que actualmente **no está comercializada en España**, por lo que no existen datos de indicación original aprobada localmente en este Evidence Pack.
El modelo TxGNN predice que sería eficaz para **Insomnio**, con **3 ensayos clínicos** y **4 publicaciones** que respaldan esta dirección.
Cabe destacar que, según el propio análisis mecanístico del pack, esta señal corresponde en realidad al uso ya establecido del fármaco en otros mercados europeos (Noctamid/Loramet), por lo que se trata más de una confirmación de uso conocido que de un reposicionamiento novedoso.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible — medicamento no comercializado en España, sin autorizaciones registradas |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos oficiales detallados sobre el mecanismo de acción (MOA) en este pack. Según la información disponible, Lormetazepam es una benzodiazepina de tipo 3-hidroxi y actúa como modulador positivo del receptor GABA-A, mecanismo que sustenta directamente su efecto sedante-hipnótico — el mismo mecanismo de clase compartido por todas las benzodiazepinas usadas como hipnóticos.

La relación entre "indicación original" e "insomnio" en este caso es particular: el fármaco no tiene indicación original registrada en España (no está comercializado), pero es conocido en otros mercados europeos bajo las marcas Noctamid y Loramet, precisamente para el tratamiento del insomnio. Es decir, la predicción de TxGNN no identifica un uso nuevo, sino que recupera correctamente el uso hipnótico ya validado del fármaco fuera de España.

Esto hace que la plausibilidad mecanística sea máxima (no es una extrapolación entre indicaciones distintas, sino la indicación intrínseca de la molécula), aunque desde la perspectiva regulatoria española sigue siendo relevante evaluarlo como candidato porque no existe autorización de comercialización local.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00679900](https://clinicaltrials.gov/study/NCT00679900) | Fase 3 | Completado | 283 | Comparación de eplivanserina (5 mg/día) vs. lormetazepam (1 mg/día) en insomnio crónico primario con dificultad de mantenimiento del sueño; evalúa efectos residuales matutinos y seguridad clínica, incluyendo insomnio de rebote y síntomas de retirada |
| [NCT00788515](https://clinicaltrials.gov/study/NCT00788515) | Fase 3 | Terminado | 33 | Comparación de volinanserina (2 mg/día) vs. lormetazepam (1 mg/día) en el mismo diseño que el ensayo anterior; terminado prematuramente, con potencia estadística limitada |
| [NCT06473415](https://clinicaltrials.gov/study/NCT06473415) | N/A | Reclutando | 50 | Efecto de la infusión continua de lormetazepam sobre patrones de EEG relacionados con calidad del sueño y profundidad de sedación en pacientes críticos de UCI |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | ECA | J Int Med Res | Lormetazepam (1 mg) superior a diazepam (5 mg) en reducción de latencia de sueño y prolongación del sueño ininterrumpido, en 100 pacientes ambulatorios con insomnio |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Revisión | Acta Psychiatr Scand Suppl | Revisión sobre el uso clínico de hipnóticos, incluyendo perfiles farmacocinéticos/farmacodinámicos de distintas benzodiazepinas |
| [2873832](https://pubmed.ncbi.nlm.nih.gov/2873832/) | 1986 | Cohorte | Br J Clin Pract | Transferencia de usuarios crónicos de nitrazepam a lormetazepam en insomnio de larga duración |
| [11215344](https://pubmed.ncbi.nlm.nih.gov/11215344/) | 2001 | Revisión | MMW Fortschr Med | Discusión sobre alternativas a benzodiazepinas (antidepresivos) como ayuda para el sueño |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ECA de Fase 3 completado (n=283) y literatura de apoyo consistente para el uso hipnótico de lormetazepam, con plausibilidad mecanística máxima al tratarse del uso ya reconocido de la molécula en otros mercados europeos. Sin embargo, la ausencia total de comercialización en España y de datos de seguridad locales impide avanzar sin salvaguardas.

**Para avanzar se necesita:**
- Prospecto/ficha técnica de la AEMPS con advertencias y contraindicaciones (bloqueante — actualmente sin datos, impide evaluación de seguridad S1)
- Datos oficiales de mecanismo de acción (MOA) vía DrugBank
- Evaluación de por qué el fármaco no está comercializado en España pese a estarlo en otros mercados de la UE
- Datos de interacciones farmacológicas (DDI), actualmente no encontrados
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


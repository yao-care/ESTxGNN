---
layout: default
title: Olaparib
parent: 僅模型預測 (L5)
nav_order: 202
evidence_level: L5
indication_count: 1
---

# Olaparib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Olaparib: De Cancer de Ovario a Cancer de Mama

## Resumen en Una Frase

Olaparib es un inhibidor oral de PARP (poli ADP-ribosa polimerasa), originalmente utilizado como terapia de mantenimiento en el cancer de ovario, trompa de Falopio o peritoneal de alto grado, sensible a platino, en pacientes con mutacion BRCA1/2. El modelo TxGNN predice que podria ser efectivo para **Carcinoma de Mama Femenino**, con **50 ensayos clinicos** y **20 publicaciones** que actualmente respaldan esta direccion, incluyendo dos ensayos de Fase 3 ya completados (OlympiA y OlympiAD) que han llevado a la aprobacion real de olaparib en cancer de mama BRCA-mutado en varios paises.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Terapia de mantenimiento en cancer de ovario/trompa de Falopio/peritoneal de alto grado, sensible a platino, con mutacion BRCA (segun descripcion de ensayos clinicos de referencia, p. ej. NCT05078671) |
| Nueva Indicacion Predicha | Carcinoma de Mama Femenino |
| Puntaje de Prediccion TxGNN | 99.09% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Proceed with Guardrails |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados de mecanismo de accion (MOA) en DrugBank/TFDA para este candidato (brecha de datos DG002). Sin embargo, segun la informacion recogida de los propios ensayos clinicos del Evidence Pack, olaparib es un inhibidor de PARP: BRCA1/2 son esenciales para la reparacion por recombinacion homologa de roturas de doble cadena del ADN, mientras que PARP media la reparacion por escision de base de roturas de cadena simple. Al inhibir PARP en celulas con deficiencia de BRCA, se produce "letalidad sintetica", eliminando selectivamente las celulas tumorales BRCA-deficientes.

El cancer de ovario (indicacion original) y el cancer de mama (nueva indicacion) comparten la misma alteracion molecular subyacente en una proporcion relevante de casos: mutaciones germinales o somaticas en BRCA1/2 y, mas ampliamente, deficiencia de recombinacion homologa (HRD). Dado que el mecanismo de accion de olaparib depende de esta via molecular y no del tejido de origen del tumor, es biologicamente razonable que el mismo farmaco sea eficaz en cancer de mama BRCA-mutado, tal como respalda la evidencia clinica disponible (ver mas abajo).

De hecho, esta prediccion ya no es puramente teorica: los ensayos OlympiA (adyuvante) y OlympiAD (metastasico) han demostrado beneficio clinico consistente en cancer de mama BRCA-mutado, lo que refuerza fuertemente la plausibilidad de la prediccion del modelo TxGNN.

---

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06201234](https://clinicaltrials.gov/study/NCT06201234) | Fase 2 | Reclutando | 176 | Adicion de elacestrant a olaparib en cancer de mama HR+/HER2- con mutacion gBRCA1/2 |
| [NCT05498155](https://clinicaltrials.gov/study/NCT05498155) | Fase 2 | Activo, no reclutando | 50 | Olaparib monoterapia y olaparib + durvalumab como terapia neoadyuvante en cancer de mama BRCA-mutado HER2-negativo en estadio temprano |
| [NCT07321015](https://clinicaltrials.gov/study/NCT07321015) | Fase 2 | Aun no reclutando | 72 | Mantenimiento con fluzoparib (mismo mecanismo que olaparib) en TNBC avanzado sensible a platino, con o sin mutacion BRCA1/2 |
| [NCT04683679](https://clinicaltrials.gov/study/NCT04683679) | Fase 2 | Reclutando | 34 | Pembrolizumab y radioterapia ablativa con o sin olaparib en cancer de mama metastasico triple negativo u hormono-positivo/HER2-negativo |
| [NCT02624973](https://clinicaltrials.gov/study/NCT02624973) | Fase 2 | Activo, no reclutando | 200 | Tratamiento personalizado de cancer de mama de alto riesgo (PETREMAC), incluye olaparib segun perfil molecular |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Fase 1 | Completado | 25 | Carboplatino-olaparib seguido de olaparib en monoterapia vs. capecitabina como primera linea en cancer de mama BRCA1/2-mutado HER2-negativo |
| [NCT07187674](https://clinicaltrials.gov/study/NCT07187674) | N/A | Aun no reclutando | 20 | Neoadyuvante con iparomlimab/tuvonralimab + olaparib + paclitaxel en TNBC temprano de alto riesgo con HRD positivo |
| [NCT03109080](https://clinicaltrials.gov/study/NCT03109080) | Fase 1 | Completado | 24 | Olaparib con radioterapia en TNBC inflamatorio, localmente avanzado/metastasico o con enfermedad residual |
| [NCT01623349](https://clinicaltrials.gov/study/NCT01623349) | Fase 1 | Completado | 118 | Inhibidor de PI3K (BKM120/BYL719) combinado con olaparib en TNBC recurrente o cancer de ovario seroso de alto grado |
| [NCT05358639](https://clinicaltrials.gov/study/NCT05358639) | Fase 1 | Activo, no reclutando | 36 | Olaparib combinado con navitoclax en TNBC y cancer de ovario seroso de alto grado |

---

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | ECA (Fase 3, OlympiA) | New England Journal of Medicine | Olaparib adyuvante reduce recurrencia en cancer de mama temprano BRCA1/2-mutado de alto riesgo |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | ECA (Fase 3, OlympiA - seguimiento) | Annals of Oncology | Resultados de supervivencia global del ensayo OlympiA con olaparib adyuvante |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | ECA (Fase 3, OlympiAD) | New England Journal of Medicine | Olaparib muestra actividad antitumoral en cancer de mama metastasico con mutacion germinal BRCA |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | ECA (Fase 3, OlympiAD - OS final) | Annals of Oncology | Olaparib mejora la supervivencia libre de progresion vs. quimioterapia; datos finales de OS y tolerabilidad |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | ECA (Fase 3, OlympiAD - seguimiento extendido) | European Journal of Cancer | Seguimiento extendido confirma perfil de seguridad y beneficio clinico sostenido de olaparib |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | Fase 2 (TBCRC 048) | Journal of Clinical Oncology | Respuesta a olaparib en cancer de mama metastasico con mutaciones somaticas BRCA o en otros genes de recombinacion homologa |
| [39520738](https://pubmed.ncbi.nlm.nih.gov/39520738/) | 2024 | Fase 2 (NOBROLA) | Breast (Edinburgh) | Olaparib en monoterapia en TNBC avanzado con HRD sin mutacion germinal BRCA1/2 |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | ECA (I-SPY2, Fase 2 adaptativo) | Cancer Cell | Durvalumab + olaparib + paclitaxel aumenta la tasa de respuesta patologica completa en cancer de mama HER2-negativo de alto riesgo |
| [38112922](https://pubmed.ncbi.nlm.nih.gov/38112922/) | 2024 | Observacional (mundo real, LUCY) | Breast Cancer Research and Treatment | Efectividad y seguridad de olaparib en cancer de mama metastasico BRCA-mutado en entorno real |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Revision | Targeted Oncology | Revision de inhibidores de PARP (olaparib, talazoparib) en el tratamiento del cancer de mama |

---

## Informacion de Mercado en España

Segun los registros consultados, olaparib no cuenta actualmente con autorizaciones de comercializacion registradas en España (0 autorizaciones).

---

## Citotoxicidad

**Esta seccion se incluye porque olaparib es un agente antineoplasico** (inhibidor de PARP, indicado en oncologia segun la evidencia de ensayos clinicos disponible).

| Item | Contenido |
|------|------|
| Clasificacion de Citotoxicidad | Terapia dirigida (inhibidor de PARP); no es quimioterapia citotoxica convencional |
| Riesgo de Mielosupresion | Consultar el prospecto para informacion de seguridad (dato no disponible en este Evidence Pack) |
| Clasificacion de Emetogenicidad | Consultar el prospecto para informacion de seguridad (dato no disponible) |
| Items de Monitoreo | Hemograma completo, funcion hepatica y renal (monitoreo estandar recomendado para inhibidores de PARP; verificar frecuencia exacta en ficha tecnica) |
| Proteccion en Manejo | Consultar la normativa local de manejo de farmacos antineoplasicos, dado que se trata de un agente oncologico oral |

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad. No se encontraron datos de interacciones farmacologicas (DDI) en la consulta realizada.

---

## Conclusion y Proximos Pasos

**Decision: Proceed with Guardrails**

**Justificacion:**
La evidencia clinica es solida (Nivel L1), respaldada por dos ensayos de Fase 3 completados (OlympiA y OlympiAD) que ya han motivado la aprobacion real de olaparib en cancer de mama BRCA-mutado en otros mercados. Sin embargo, faltan datos criticos de seguridad y regulacion local (brecha bloqueante DG001) y el farmaco aun no cuenta con autorizacion en España, por lo que no se recomienda un "Go" directo.

**Para avanzar se necesita:**
- Ficha tecnica/prospecto oficial con advertencias, contraindicaciones e interacciones (DG001, Blocking)
- Datos detallados de mecanismo de accion desde DrugBank (DG002)
- Confirmacion del estado regulatorio y posible via de autorizacion en España
- Evaluacion de seguridad especifica para la poblacion con cancer de mama (actualmente sin datos de DDI ni advertencias registradas)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


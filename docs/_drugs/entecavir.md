---
layout: default
title: Entecavir
parent: 僅模型預測 (L5)
nav_order: 106
evidence_level: L5
indication_count: 10
---

# Entecavir
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

Usando el Evidence Pack proporcionado (TW-DB00442-multi, Entecavir), genero el informe siguiendo el formato indicado. Nota metodológica: el `predicted_indications[0]` (hepatitis C crónica) es la señal de mayor rango TxGNN, pero el propio *repurposing_rationale* del pack la identifica como probable falso positivo — lo reflejo con transparencia en vez de presentarla como una oportunidad validada.

---

# Entecavir: De Hepatitis B Cronica a Hepatitis C Cronica

## Resumen en Una Frase

Entecavir es un analogo nucleosido de guanina utilizado originalmente para el tratamiento de la hepatitis B cronica (VHB), inhibiendo de forma selectiva la ADN polimerasa (transcriptasa inversa) del virus. El modelo TxGNN predice, con la puntuacion mas alta de todo el lote de candidatos, que podria ser efectivo para **Hepatitis C Cronica (VHC)**, con **40 ensayos clinicos** y **20 publicaciones** asociados a esta senal. Sin embargo, el analisis mecanistico detallado incluido en este mismo informe indica que se trata muy probablemente de un **falso positivo** derivado de co-ocurrencia en la literatura (pacientes con coinfeccion VHB/VHC), sin evidencia real de actividad anti-VHC.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Hepatitis B cronica (VHB) |
| Nueva Indicacion Predicha | Hepatitis C Cronica (VHC) |
| Puntaje de Prediccion TxGNN | 99.98% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de una ficha estructurada del mecanismo de accion de entecavir en la base de datos de origen. No obstante, la evidencia mecanistica recopilada en este informe permite reconstruir el cuadro con claridad: entecavir, tras fosforilacion intracelular a entecavir trifosfato, inhibe de forma altamente selectiva la ADN polimerasa (transcriptasa inversa) del virus de la hepatitis B, bloqueando tres funciones clave de la enzima — el cebado, la transcripcion inversa de la cadena negativa de ADN, y la sintesis de la cadena positiva de ADN viral. Esta es la indicacion original de entecavir, ya ampliamente validada en decadas de uso clinico.

La hepatitis C, en cambio, esta causada por un virus de una familia completamente distinta (Flaviviridae, ARN monocatenario de polaridad positiva), cuya replicacion depende de una ARN polimerasa dependiente de ARN (NS5B) y de una proteasa NS3/4A. Estas estructuras no guardan ninguna relacion con la transcriptasa inversa del VHB, y no existe evidencia experimental de que el entecavir trifosfato inhiba NS5B ni ningun otro componente de la maquinaria replicativa del VHC.

Al revisar en detalle los ensayos clinicos y la literatura vinculados a esta prediccion, la inmensa mayoria corresponden en realidad a estudios de entecavir en el tratamiento del VHB, o al manejo de pacientes con **coinfeccion VHB/VHC** (por ejemplo, reactivacion cruzada de un virus durante el tratamiento antiviral dirigido al otro). Esto sugiere que la senal de TxGNN se origina en la frecuente co-mencion de ambos virus en la literatura cientifica (comparten vias de transmision y a menudo se estudian juntos), mas que en una relacion mecanistica real. Se trata, por tanto, de un candidato de baja plausibilidad biologica que no deberia interpretarse como una oportunidad genuina de reposicionamiento.

---

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00597259](https://clinicaltrials.gov/study/NCT00597259) | Fase 4 | Desconocido | 294 | Peginterferon alfa-2a + entecavir vs. entecavir solo en VHB HBeAg-positivo; el diseno menciona VHC/VIH solo como contexto conceptual, no evalua VHC |
| [NCT01179594](https://clinicaltrials.gov/study/NCT01179594) | Fase 4 | Retirado (n=0) | 0 | Pegasys ± entecavir en VHB HBeAg-negativo; estudio retirado, sin datos generados |
| [NCT01022801](https://clinicaltrials.gov/study/NCT01022801) | Fase 2 | Completado | 120 | Entecavir (BMS-200475) vs. lamivudina en VHB japones; poblacion VHB, no VHC |
| [NCT05005507](https://clinicaltrials.gov/study/NCT05005507) | Fase 2 | Terminado (n=1) | 1 | JNJ-73763989 + analogo nucleos(t)idico + PegIFN en VHB; terminado por reclutamiento minimo |
| [NCT02589652](https://clinicaltrials.gov/study/NCT02589652) | N/A | Desconocido | 294 | Cambio a peginterferon alfa-2a tras entecavir prolongado en VHB con HBsAg/HBeAg bajos |
| [NCT00096785](https://clinicaltrials.gov/study/NCT00096785) | Fase 3 | Completado | 69 | Entecavir vs. adefovir en reduccion temprana de carga viral en VHB virgen de tratamiento |
| [NCT01270178](https://clinicaltrials.gov/study/NCT01270178) | N/A | Desconocido | 420 | Entecavir en pacientes con VHB y carcinoma hepatocelular tras ablacion por radiofrecuencia |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Fase 2/3 | Completado | 23 | Manejo de reactivacion del VHB durante tratamiento antiviral directo del VHC en coinfeccion VHB/VHC (no evalua entecavir contra VHC) |
| [NCT01018381](https://clinicaltrials.gov/study/NCT01018381) | N/A | Completado | 130 | Arabinoxilano de salvado de arroz (Biobran) en carcinoma hepatocelular e infeccion por VHB y VHC; no evalua entecavir |
| [NCT05484466](https://clinicaltrials.gov/study/NCT05484466) | Fase 2a | Desconocido | 90 | ZM-H1505R + entecavir vs. entecavir monoterapia en VHB tras 12 meses de monoterapia previa |

**Nota:** Ninguno de los ensayos identificados evalua directamente la eficacia de entecavir como tratamiento antiviral de la hepatitis C; todos corresponden a estudios sobre VHB o al manejo clinico de la coinfeccion VHB/VHC.

---

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohorte | Viruses | Reactivacion del VHC en pacientes anti-VHC positivos con VHB cronico tras terapias anti-VHB (Nuc), incluyendo entecavir |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Revision | Expert Opin Pharmacother | Avances en el tratamiento de la coinfeccion VHB/VHC |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Revision | Clin Res Hepatol Gastroenterol | Coinfeccion VHB/VHC como reto terapeutico; reporte de caso incluido |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Revision | Clin Res Hepatol Gastroenterol | Manejo presente y futuro de la hepatitis viral B y C en ninos |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Revision | Minerva Gastroenterol Dietol | Medicamentos antivirales para VHB y VHC y su efecto sobre la funcion renal |
| [32527114](https://pubmed.ncbi.nlm.nih.gov/32527114/) | 2021 | Pendiente de clasificacion | Chin Clin Oncol | Momento optimo y manejo de VHB y VHC en carcinoma hepatocelular |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | Pendiente de clasificacion | J Gastroenterol Hepatol | Reactivacion del VHB durante tratamiento con antivirales de accion directa para VHC |
| [36873880](https://pubmed.ncbi.nlm.nih.gov/36873880/) | 2023 | Caso clinico | Front Med | Evoluciones virales inusuales en un paciente con coinfeccion VHB/VHC concurrente |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Pendiente de clasificacion | Wien Med Wochenschr | Tratamiento actual y perspectivas futuras de la hepatitis B y C cronicas |
| [17033303](https://pubmed.ncbi.nlm.nih.gov/17033303/) | 2002 | Pendiente de clasificacion | Curr Opin Gastroenterol | Panorama general de la hepatitis viral, incluida la reduccion viral con lamivudina en VHB |

**Nota:** La literatura disponible describe fundamentalmente la coinfeccion VHB/VHC y el manejo clinico conjunto, no un efecto antiviral directo de entecavir sobre el VHC.

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
No existe plausibilidad mecanistica para el uso de entecavir en hepatitis C cronica: el farmaco actua sobre la transcriptasa inversa del VHB, mientras que el VHC depende de una ARN polimerasa (NS5B) sin homologia conocida. La totalidad de los ensayos clinicos y la literatura revisados corresponden a estudios sobre VHB o al manejo de la coinfeccion VHB/VHC, no a evidencia de eficacia antiviral directa contra el VHC. La puntuacion elevada de TxGNN parece reflejar co-ocurrencia en la literatura mas que una relacion biologica real.

**Para avanzar se necesita:**
- Confirmacion mediante ensayo in vitro que descarte (o establezca) actividad de entecavir trifosfato frente a la ARN polimerasa NS5B del VHC, antes de considerar cualquier desarrollo clinico
- Obtencion del prospecto/ficha tecnica de TFDA (advertencias y contraindicaciones), actualmente marcado como brecha de datos bloqueante (DG001)
- Confirmacion formal del mecanismo de accion de entecavir en la base de datos de farmaco (DG002)
- Revision del resto de indicaciones predichas en este mismo lote: la de mayor nivel de evidencia real (hepatitis B, L1) corresponde a la indicacion original ya aprobada del farmaco y no a una oportunidad nueva de reposicionamiento, por lo que se recomienda no continuar evaluando esta serie de predicciones sin una revision adicional de calidad de datos del grafo de conocimiento
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


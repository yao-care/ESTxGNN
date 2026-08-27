---
layout: default
title: Etoricoxib
parent: 僅模型預測 (L5)
nav_order: 114
evidence_level: L5
indication_count: 10
---

# Etoricoxib
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

# Etoricoxib: De Antiinflamatorio COX-2 Selectivo a Cefalea Sensible a Indometacina

> **Nota metodológica:** El paquete de evidencia incluye 10 indicaciones predichas por TxGNN. La de mayor puntuación (*migraine disorder*, rank 2402) no tiene ningún ensayo clínico ni literatura de respaldo, y el propio análisis de mecanismo señala que el score alto probablemente refleja similitud de embeddings y no evidencia causal. Este informe se centra en cambio en **"headache disorder"** (rank 9718), la indicación con el nivel de evidencia más sólido (L3) y una justificación mecanística respaldada por literatura real, por ser la candidata más defendible para evaluación de reposicionamiento.

## Resumen en Una Frase

Etoricoxib es un antiinflamatorio no esteroideo (AINE) inhibidor selectivo de la COX-2. El modelo TxGNN predice que podría ser efectivo para **cefaleas sensibles a indometacina** (Headache Disorder), un grupo de síndromes de cefalea primaria (cefalea punzante idiopática, cefalea tusígena secundaria) tradicionalmente tratados con indometacina. Actualmente **2 ensayos clínicos** (de baja relevancia directa) y **5 publicaciones** —principalmente series y reportes de caso— respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dolor e inflamación (uso típico de AINE selectivo COX-2); no hay indicaciones específicas registradas en este paquete de evidencia |
| Nueva Indicación Predicha | Cefalea sensible a indometacina (Headache Disorder) |
| Puntaje de Predicción TxGNN | 99.31% (rank 9718) |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) de etoricoxib en este paquete de evidencia. Según la información farmacológica conocida, etoricoxib pertenece a la clase de los **inhibidores selectivos de la COX-2 (coxibs)**, cuya eficacia en dolor e inflamación musculoesquelética está bien establecida, y mecanísticamente podría ser aplicable a ciertos trastornos de cefalea.

Existe un subgrupo reconocido de cefaleas primarias y secundarias —cefalea punzante idiopática (*idiopathic stabbing headache*), cefalea tusígena y algunas cefalalgias autonómicas del trigémino como la hemicránea paroxística— que responden de forma característica a indometacina, un AINE no selectivo. Varios reportes de caso muestran que pacientes intolerantes a indometacina lograron control sintomático con etoricoxib o celecoxib, ambos inhibidores selectivos de la COX-2, lo que sugiere que parte del efecto terapéutico podría transitar por la vía COX. Sin embargo, la respuesta a indometacina también se ha vinculado a mecanismos no dependientes de COX (p. ej., vía del óxido nítrico), por lo que la inferencia causal sigue siendo de fuerza moderada y proviene de una única línea de investigación (mismo grupo de autores, Farag/Bahra) replicada en pocos casos adicionales.

La indicación relacionada **"trigeminal autonomic cephalalgia"** (rank 10, mismo nivel L3) comparte exactamente la misma publicación clave (PMID 35277974) y refuerza esta señal, ya que la hemicránea paroxística y la hemicránea continua son subtipos clásicamente respondedores a indometacina.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT06967363](https://clinicaltrials.gov/study/NCT06967363) | N/A | Aún no reclutando | 360 | Cohorte de neuroimagen multimodal en dolor lumbar; no evalúa fármacos, relevancia solo a nivel de nombre de enfermedad |
| [NCT03542955](https://clinicaltrials.gov/study/NCT03542955) | N/A | Completado | 180 | Terapia de onda corta pulsada vs. etoricoxib en osteoartritis cervical; no es un ensayo centrado en cefalea |

Ninguno de los dos ensayos evalúa directamente etoricoxib como tratamiento de un trastorno de cefalea; ambos fueron clasificados con relevancia baja (grado C).

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35277974](https://pubmed.ncbi.nlm.nih.gov/35277974/) | 2022 | Serie de Casos | Headache | Pacientes con cefaleas sensibles a indometacina (incluyendo cefalalgias autonómicas del trigémino) respondieron a etoricoxib y celecoxib como alternativa mejor tolerada |
| [36893522](https://pubmed.ncbi.nlm.nih.gov/36893522/) | 2023 | Reporte de Caso | Clin Neurol Neurosurg | Dos pacientes con cefalea tusígena secundaria respondieron al inhibidor COX-2 etoricoxib |
| [17883876](https://pubmed.ncbi.nlm.nih.gov/17883876/) | 2007 | Reporte de Caso | J Med Case Rep | Uso de etoricoxib para tratar cefalea punzante idiopática |
| [25229174](https://pubmed.ncbi.nlm.nih.gov/25229174/) | 2014 | Reporte de Caso (evento adverso) | Clin Neuropharmacol | Síndrome de vasoconstricción cerebral reversible posiblemente inducido por etoricoxib — **señal de seguridad, no de eficacia** |
| [18171381](https://pubmed.ncbi.nlm.nih.gov/18171381/) | 2008 | Reporte de Caso | Eur J Neurol | Cefalea punzante primaria respondedora a etoricoxib, inhibidor selectivo de COX-2 |

Toda la evidencia es de nivel caso/serie de casos; no existen ensayos controlados aleatorizados que confirmen eficacia en cefalea.

## Información de Mercado en España

Etoricoxib no está actualmente comercializado según los datos regulatorios de este paquete de evidencia (0 autorizaciones registradas, sin licencias listadas).

## Consideraciones de Seguridad

Los campos estructurados de seguridad (advertencias, contraindicaciones, interacciones) están vacíos en este paquete de evidencia — **consultar el prospecto para información de seguridad completa**.

No obstante, dos señales relevantes surgieron en la literatura revisada durante la búsqueda de indicaciones (no forman parte del módulo formal de seguridad, pero deben tenerse en cuenta):
- **Síndrome de vasoconstricción cerebral reversible (RCVS)** posiblemente inducido por etoricoxib (PMID 25229174) — relevante porque el RCVS puede presentarse clínicamente como cefalea, lo que obliga a descartarlo como diagnóstico diferencial antes de atribuir mejoría terapéutica al fármaco.
- En un contexto distinto (evidencia de hipertensión pulmonar), se reportó **hiperpotasemia y disfunción renal aguda potencialmente mortal** inducida por etoricoxib en combinación con telmisartán y dieta baja en sodio (PMID 21373319), consistente con el perfil conocido de retención hidrosalina de los inhibidores COX-2.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia actual se limita a reportes y series de casos (sin ensayos controlados que evalúen etoricoxib específicamente en cefalea), y el fármaco no está comercializado en España. La plausibilidad mecanística es razonable pero no está confirmada más allá de una única línea de publicaciones del mismo grupo de investigadores.

**Para avanzar se necesita:**
- Datos formales de mecanismo de acción (MOA) y ficha técnica/prospecto de TFDA
- Un estudio prospectivo u observacional controlado en el subgrupo de cefaleas sensibles a indometacina (incluyendo cefalalgias autonómicas del trigémino)
- Datos completos de interacciones farmacológicas (DDI) y contraindicaciones
- Confirmación del estado regulatorio y vía de autorización en España, dado que el fármaco no está actualmente comercializado
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


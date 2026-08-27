---
layout: default
title: Diazepam
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 10
---

# Diazepam
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

# Diazepam: De Ansiedad y Espasmo Muscular a Insomnio

## Resumen en Una Frase

Diazepam es una benzodiazepina clásica, utilizada tradicionalmente para el tratamiento de la ansiedad, el espasmo muscular y las convulsiones. El modelo TxGNN predice que podría ser efectivo para **Insomnio**, con **24 ensayos clínicos** y **18 publicaciones** que actualmente respaldan esta dirección — aunque, como se detalla más abajo, la mayoría de la evidencia disponible aborda la retirada/reducción de hipnóticos más que la eficacia del propio diazepam.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Ansiedad, espasmo muscular, convulsiones (uso clásico de benzodiazepina; este paquete de evidencia no registra un texto de indicación aprobada específico) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99.9997% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en este paquete de evidencia. Según la información conocida, diazepam pertenece a la clase de las benzodiazepinas, cuya eficacia en ansiedad, espasmo muscular y convulsiones ha sido ampliamente comprobada, y mecanísticamente es directamente aplicable al insomnio.

Diazepam es un modulador alostérico positivo (PAM) del receptor GABA-A. El efecto sedante-hipnótico es la acción farmacológica central de las benzodiazepinas, por lo que la relación mecanística con el insomnio ya está clínicamente establecida — no se trata de una hipótesis de reposicionamiento novedosa, sino de una extensión de un efecto farmacológico conocido. De hecho, la predicción en rango 3 del mismo paquete ("sleep disorder, initiating and maintaining sleep") corresponde esencialmente al mismo concepto de enfermedad que el insomnio.

El principal matiz es que la evidencia recopilada se concentra mayoritariamente en la **retirada o reducción de hipnóticos** (incluidas las benzodiazepinas) más que en ensayos que confirmen la eficacia del diazepam específicamente para tratar el insomnio en la práctica actual. Esto es coherente con el uso clínico real: el diazepam se reserva hoy para insomnio de corto plazo o casos puntuales, dado el riesgo de tolerancia y dependencia con el uso prolongado.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04050176](https://clinicaltrials.gov/study/NCT04050176) | Fase 3 | Activo, no reclutando | 260 | Retirada guiada (ciega) de hipnóticos combinada con TCC-I frente a retirada abierta; relevante para seguridad de uso a largo plazo |
| [NCT02831894](https://clinicaltrials.gov/study/NCT02831894) | Fase 2 | Completado | 74 | Velocidad de reducción gradual y rasgos asociados al éxito en la discontinuación de hipnóticos |
| [NCT05935553](https://clinicaltrials.gov/study/NCT05935553) | Fase 2/3 | Reclutando | 93 | Baclofeno para facilitar la titulación en la dependencia de benzodiazepinas |
| [NCT03687086](https://clinicaltrials.gov/study/NCT03687086) | N/A | Completado | 188 | Mecanismo novedoso para ayudar a adultos mayores a discontinuar hipnóticos |
| [NCT03461042](https://clinicaltrials.gov/study/NCT03461042) | Fase 4 | Completado | 17 | Ramelteón combinado con hipnóticos BZD/no-BZD para facilitar reducción de dosis en insomnio crónico |
| [NCT04751851](https://clinicaltrials.gov/study/NCT04751851) | N/A | Completado | 128 | Terapia de aceptación y compromiso (ACT) como apoyo a la retirada de benzodiazepinas en insomnio con dependencia a hipnóticos |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Desconocido | 1400 | Cohorte prospectiva en Taiwán: patrones de uso, eficacia y seguridad de hipnóticos en adultos mayores |
| [NCT07417813](https://clinicaltrials.gov/study/NCT07417813) | N/A | Reclutando | 121 | Eficacia y seguridad de lemborexant en insomnio con trastornos psiquiátricos comórbidos (contexto comparador) |
| [NCT05646693](https://clinicaltrials.gov/study/NCT05646693) | Fase 2 | Desconocido | 58 | Terapia antioxidante combinada con Adepsique® (amitriptilina, perfenazina y diazepam) en tinnitus crónico; incluye diazepam explícitamente |
| [NCT01244711](https://clinicaltrials.gov/study/NCT01244711) | Fase 4 | Terminado | 1 | Sustitución de quetiapina por benzodiazepinas en depresión/ansiedad refractaria con insomnio comórbido |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | ECA | J Int Med Res | Diazepam 5 mg comparado con lormetazepam 1 mg en 100 pacientes con insomnio; lormetazepam superior en algunos parámetros, diazepam eficaz como comparador activo |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Revisión | Bioorganic Chemistry | Revisión de moduladores GABAA de molécula pequeña; diazepam como PAM de referencia con efectos sedantes bien caracterizados |
| [35228700](https://pubmed.ncbi.nlm.nih.gov/35228700/) | 2022 | Preclínico | Nature Neuroscience | El uso crónico de diazepam favorece la fagocitosis microglial de espinas dendríticas y deterioro cognitivo vía TSPO mitocondrial |
| [40350874](https://pubmed.ncbi.nlm.nih.gov/40350874/) | 2025 | Preclínico | China J Chinese Materia Medica | Diazepam (2 mg/kg) usado como fármaco control positivo en modelo murino de depresión e insomnia inducidos por estrés crónico |
| [40583063](https://pubmed.ncbi.nlm.nih.gov/40583063/) | 2025 | Clínico/Mecanístico | Cell Mol Biol Lett | Uso prolongado de benzodiazepinas (diazepam) y Z-drugs se asocia a mayor riesgo de cáncer de mama; evidencia clínica y mecanismos moleculares |
| [37776625](https://pubmed.ncbi.nlm.nih.gov/37776625/) | 2023 | Preclínico | J Pharm Biomed Anal | Diazepam (DZP) como control positivo en estudio metabolómico del efecto sedante-hipnótico de Naoling Pian en ratas con insomnio inducido |
| [6114852](https://pubmed.ncbi.nlm.nih.gov/6114852/) | 1981 | Revisión | Drugs | Revisión de triazolam frente a hipnóticos de acción más larga (incluida la clase de diazepam) en insomnio |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-análisis | Acta Pharmaceutica | Meta-análisis de tranquilizantes (incluidas benzodiazepinas) en pacientes de edad avanzada, evaluando dosis y efectos adversos |
| [35196378](https://pubmed.ncbi.nlm.nih.gov/35196378/) | 2022 | Intervención no aleatorizada | Family Practice | Discontinuación de uso crónico de benzodiazepinas en atención primaria |
| [29479317](https://pubmed.ncbi.nlm.nih.gov/29479317/) | 2018 | Revisión sistemática | Frontiers in Pharmacology | Revisión de fórmulas herbales chinas para insomnio, con benzodiazepinas como tratamiento de referencia comparativo |

## Información de Mercado en España

Diazepam no cuenta actualmente con autorizaciones de comercialización registradas en este paquete de evidencia (0 autorizaciones, estado: **No comercializado**). No es posible generar la tabla de autorizaciones por falta de datos.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo GABA-A ya está clínicamente establecido para efectos sedantes-hipnóticos, y existe al menos un ensayo clínico aleatorizado histórico directo (PMID 6113175) que respalda la eficacia de diazepam en insomnio, junto con múltiples ensayos activos sobre su manejo a largo plazo. Sin embargo, la mayoría de la evidencia moderna se centra en la retirada de hipnóticos —no en la eficacia del propio diazepam— y persisten brechas bloqueantes de seguridad (DG001) y de mecanismo de acción (DG002), además de la ausencia de comercialización actual en España.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica (TFDA/AEMPS) con advertencias y contraindicaciones — brecha bloqueante (DG001)
- Completar datos de mecanismo de acción vía DrugBank (DG002)
- Confirmar el estado regulatorio actual en España, dado que el paquete indica 0 autorizaciones vigentes
- Priorizar evidencia clínica moderna que evalúe eficacia (no solo discontinuación) de diazepam específicamente en insomnio de corto plazo
- Evaluar el perfil de riesgo de dependencia/tolerancia frente a alternativas no benzodiazepínicas antes de cualquier uso prolongado
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Alirocumab
parent: Evidencia moderada (L3-L4)
nav_order: 36
evidence_level: L4
indication_count: 10
---

# Alirocumab
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Alirocumab: De Dislipidemia Sindrómica y Aterosclerosis a Xantomatosis

## Resumen en Una Frase

Alirocumab es un anticuerpo monoclonal anti-PCSK9, originalmente utilizado para dislipidemia sindrómica y trastornos arterioscleróticos (aterosclerosis, arteriolosclerosis).
El modelo TxGNN predice que podría ser efectivo para **xantomatosis**, la predicción con evidencia más relevante entre las candidatas, aunque respaldada solo por **2 publicaciones** (reportes de caso) y **ningún ensayo clínico**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dislipidemia sindrómica / aterosclerosis (según el grafo de conocimiento de TxGNN; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Xantomatosis |
| Puntaje de Predicción TxGNN | 99.37% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 9 |
| Decisión Recomendada | Hold |

**Nota sobre la selección:** la primera predicción del ranking (ictiosis ligada al X sin deficiencia de esteroide sulfatasa, 99.43%) carece de evidencia y de vínculo mecanístico. Este informe se centra en la xantomatosis (tercera en el ranking), que ofrece la primera señal de evidencia y un mecanismo plausible. Las demás predicciones del ranking se resumen al final.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, alirocumab es un anticuerpo monoclonal IgG1 totalmente humano que se une a PCSK9 (proproteína convertasa subtilisina/kexina tipo 9). Esto aumenta la recirculación de receptores de LDL en el hígado y reduce el colesterol LDL (LDL-C). Su eficacia en hipercolesterolemia y en la reducción del riesgo cardiovascular aterosclerótico está bien establecida.

Los xantomas son depósitos de lípidos en la piel y los tendones que aparecen en contextos de hipercolesterolemia grave, como la hipercolesterolemia familiar. Reducir el LDL-C mediante inhibición de PCSK9 podría, en teoría, disminuir la carga de xantomas, al igual que ocurre en la hipercolesterolemia familiar.

Existe, sin embargo, una limitación importante: las dos publicaciones recuperadas son reportes de caso de dislipidemia grave (dislipidemia combinada con base genética compleja y sitosterolemia con xantomas tendinosos tratada con ezetimiba y alirocumab). Su relación con la eficacia de alirocumab es indirecta y no existen datos de ensayos con la xantomatosis como criterio de valoración.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32713907](https://pubmed.ncbi.nlm.nih.gov/32713907/) | 2020 | Reporte de caso | Internal Medicine | Sitosterolemia con hipercolesterolemia grave y xantomas tendinosos del tendón de Aquiles por mutaciones heterocigotas compuestas en ABCG5, tratada con ezetimiba y alirocumab; inicialmente se diagnosticó erróneamente como hipercolesterolemia familiar |
| [31538826](https://pubmed.ncbi.nlm.nih.gov/31538826/) | 2019 | Reporte de caso | J Investig Med High Impact Case Rep | Dislipidemia combinada grave con base genética compleja (disbetalipoproteinemia familiar) con xantomas tuberoeruptivos y palmares y enfermedad vascular prematura |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1151031011 | Praluent 150 mg solución inyectable en jeringa precargada | Solución inyectable | No disponible |
| 1151031008 | Praluent 150 mg solución inyectable en pluma precargada | Solución inyectable | No disponible |
| 1151031010 | Praluent 150 mg solución inyectable en jeringa precargada | Solución inyectable | No disponible |
| 1151031004 | Praluent 75 mg solución inyectable en jeringa precargada | Solución inyectable | No disponible |
| 1151031019 | Praluent 300 mg solución inyectable en pluma precargada | Solución inyectable en pluma precargada | No disponible |

Hay 9 autorizaciones vigentes en total (todas de medicamento único, titular Sanofi Winthrop Industrie); se muestran las 5 principales.

## Consideraciones de Seguridad

- **Interacciones farmacológicas:** el único registro corresponde a la farmacología de su diana, PCSK9 (alirocumab se une a PCSK9 humana). No se identificaron interacciones con otros fármacos.
- **Seguridad a largo plazo:** un análisis agrupado del ensayo ODYSSEY OUTCOMES (47 296 pacientes-año de observación controlada con placebo) aporta información de seguridad de alirocumab en sus indicaciones actuales.

Para advertencias y contraindicaciones específicas, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de xantomatosis tiene un puntaje TxGNN alto y un mecanismo plausible (reducción de LDL-C), pero se apoya solo en dos reportes de caso indirectos y sin ensayos clínicos. Además, el fármaco ya cuenta con indicaciones lipídicas aprobadas, por lo que la xantomatosis sería un efecto secundario esperable del control del LDL-C más que un reposicionamiento claramente novedoso.

**Para avanzar se necesita:**
- Datos del mecanismo de acción detallados y verificados en fuentes oficiales
- Texto de indicaciones y advertencias/contraindicaciones del prospecto de la AEMPS (hoy faltan)
- Estudios que evalúen la regresión de xantomas como criterio de valoración (series de casos, análisis post hoc de ensayos en hipercolesterolemia familiar)
- Definir si la xantomatosis es una indicación distinta o parte del tratamiento de la dislipidemia ya aprobada

## Otras Predicciones del Ranking

| Rank | Enfermedad | Puntaje | Nivel | Decisión | Comentario |
|---|---|---|---|---|---|
| 1 | Ictiosis ligada al X sin deficiencia de esteroide sulfatasa | 99.43% | L5 | Hold | Sin vínculo mecanístico ni evidencia |
| 2 | Trastorno del metabolismo y transporte de otras vitaminas y cofactores | 99.41% | L5 | Hold | Sin vínculo plausible |
| 4 | Trastorno del desarrollo sexual 46,XY por defecto de la vía "backdoor" de la DHT | 99.37% | L5 | Hold | La reducción de LDL-C no corrige un defecto enzimático |
| 5 | Enfermedad del proceso catabólico del colesterol | 99.36% | L4 | Línea de investigación | Proximidad mecanística fuerte, pero solapa con las indicaciones lipídicas ya aprobadas; 19 publicaciones, en su mayoría revisiones; un estudio preclínico (PMID 38191052) sugiere prevención de cálculos biliares de colesterol |
| 6 | Trastorno del desarrollo sexual 46,XY por defecto de síntesis de colesterol | 99.35% | L5 | Hold | Mecanísticamente contraproducente (el problema es déficit de colesterol) |
| 7 | Displasia diafisaria moteada | 99.30% | L5 | Hold | Sin vínculo identificado |
| 8 | Enfermedad por almacenamiento de lípidos neutros | 99.29% | L5 | Hold | Vía distinta (lipólisis intracelular de triglicéridos) |
| 9 | Deficiencia de 3-hidroxiacil-CoA deshidrogenasa | 99.29% | L5 | Hold | Trastorno de beta-oxidación; sin mecanismo plausible |
| 10 | Paraplejia espástica-atrofia óptica-neuropatía y trastornos relacionados | 99.26% | L5 | Hold | Sin vínculo identificado |
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


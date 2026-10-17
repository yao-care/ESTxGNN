---
layout: default
title: Ribavirin
parent: Solo predicción del modelo (L5)
nav_order: 696
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ribavirin: nueva indicación predicha, Infección crónica por virus de la hepatitis B (nivel de evidencia L5). Indicación original: Infección crónica por virus de la hepatitis C"
monitor_inn: "Ribavirin"
predicted_indications: ["early-onset familial noncirrhotic portal hypertension", "hepatoportal sclerosis", "primitive portal vein thrombosis", "hepatopulmonary syndrome", "hepatic porphyria", "IgG4-related pachymeningitis", "IgG4-related mediastinitis", "IgG4-related mesenteritis"]
---

# Ribavirin
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

# Ribavirina: De Hepatitis C Crónica a Infección Crónica por Virus de la Hepatitis B

## Resumen en Una Frase

Ribavirina es un análogo nucleosídico antiviral, originalmente utilizado para el tratamiento de la hepatitis C crónica y de las infecciones por virus respiratorio sincitial.
El modelo TxGNN predice que podría ser efectiva para la **infección crónica por virus de la hepatitis B**, con **14 ensayos clínicos** y **20 publicaciones** relacionados, aunque la mayoría se centra en hepatitis C o en coinfección, por lo que la eficacia en hepatitis B no está confirmada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección crónica por virus de la hepatitis C; infección por virus respiratorio sincitial (según el grafo de conocimiento, ya que los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Infección crónica por virus de la hepatitis B |
| Puntaje de Predicción TxGNN | 99.86% |
| Nivel de Evidencia | L1 (según el número de ensayos de Fase 3 completados; la eficacia no está confirmada con los datos disponibles) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 10 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según la información farmacológica conocida, la ribavirina es un análogo de la guanosina que inhibe las enzimas IMPDH1 e IMPDH2 (inosina monofosfato deshidrogenasa), reduce las reservas intracelulares de GTP y bloquea la síntesis de ácidos nucleicos. Además, tiene efectos inmunomoduladores. Su actividad es de amplio espectro frente a virus ARN.

Tanto la hepatitis C como la hepatitis B son infecciones virales crónicas del hígado que comparten el riesgo de cirrosis y carcinoma hepatocelular, y a menudo se tratan con interferón. Esto explica la proximidad entre ambas indicaciones en el grafo de conocimiento.

Sin embargo, el VHB es un virus ADN y la ribavirina tiene actividad antiviral directa limitada frente a él. Los estudios clínicos la han evaluado sobre todo como complemento del peginterferón para potenciar la respuesta inmunomediada, no como antiviral directo contra el VHB. Hoy los análogos de nucleós(t)idos son el tratamiento estándar. Por tanto, la plausibilidad mecanística es moderada.

## Evidencia de Ensayos Clínicos

Se muestran los ensayos más relevantes para la hepatitis B, priorizando los que evalúan directamente esta enfermedad.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00114361](https://clinicaltrials.gov/study/NCT00114361) | Fase 3 | Completado | 138 | Peginterferón alfa-2a + ribavirina vs. peginterferón en monoterapia en hepatitis B crónica HBeAg-negativa (estudio PARC); resultados de eficacia no disponibles |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Fase 2/3 | Completado | 120 | Estudio piloto de interferón alfa-2b + ribavirina en hepatitis crónica; la población (VHB vs. VHC) no está clara |
| [NCT00154869](https://clinicaltrials.gov/study/NCT00154869) | Fase 3 | Desconocido | 320 | Peginterferón alfa-2a + ribavirina en coinfección VHC/VHB y hepatitis C crónica |
| [NCT03759782](https://clinicaltrials.gov/study/NCT03759782) | Fase 3 | Desconocido | 24 | Ribavirina como inmunomodulador para potenciar los análogos de nucleósidos en hepatitis B (piloto) |
| [NCT00117533](https://clinicaltrials.gov/study/NCT00117533) | Fase 4 | Desconocido | 20 | Peginterferón alfa-2b + ribavirina en doble infección por VHB y virus delta |
| [NCT02219477](https://clinicaltrials.gov/study/NCT02219477) | Fase 3 | Completado | 36 | Ombitasvir/paritaprevir/ritonavir ± dasabuvir con ribavirina en hepatitis C con cirrosis descompensada; enfocado en VHC |
| [NCT01447420](https://clinicaltrials.gov/study/NCT01447420) | Fase 4 | Completado | 129 | Respuesta virológica sostenida según perfil de IL-28B con peginterferón + ribavirina en hepatitis C genotipo 1 |
| [NCT01425970](https://clinicaltrials.gov/study/NCT01425970) | Fase 2 | Terminado | 210 | INX-08189 con peginterferón y ribavirina o daclatasvir en hepatitis C genotipos 2 y 3 |
| [NCT03186313](https://clinicaltrials.gov/study/NCT03186313) | Fase 3 | Completado | 72 | Sofosbuvir + daclatasvir + ribavirina en dosis única combinada en hepatitis C genotipo 4 |
| [NCT01830127](https://clinicaltrials.gov/study/NCT01830127) | Fase 2 | Completado | 35 | BI 207127 + faldaprevir + ribavirina en hepatitis C con insuficiencia hepática moderada |

Solo dos ensayos (NCT00114361 y NCT03759782) evalúan directamente la ribavirina en hepatitis B, y no hay resultados de eficacia disponibles en los datos compilados. El resto se centra en hepatitis C o coinfección.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Revisión | Viruses | Coinfección VHC/VHB; terapia con peginterferón + ribavirina recomendada en pacientes con ARN-VHC positivo |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Revisión | World J Gastroenterol | Actualización del tratamiento y los desenlaces de la doble infección VHC/VHB |
| [28702738](https://pubmed.ncbi.nlm.nih.gov/28702738/) | 2018 | Revisión | Hepatol Int | Impacto del tratamiento etiológico en el pronóstico de la hipertensión portal cirrótica |
| [25048716](https://pubmed.ncbi.nlm.nih.gov/25048716/) | 2015 | Revisión | Hepatology | Aspectos inmunológicos de la terapia antiviral en hepatitis B y C |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | Revisión | World J Gastroenterol | Polimorfismo de IL28B e infección por VHB |
| [26284971](https://pubmed.ncbi.nlm.nih.gov/26284971/) | 2015 | Revisión | Curr Opin Virol | Efecto del genotipo IL28B en hepatitis B y C |
| [24379612](https://pubmed.ncbi.nlm.nih.gov/24379612/) | 2013 | Revisión | World J Gastroenterol | Prevención del carcinoma hepatocelular en hepatitis B y C crónicas |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | Revisión | Annu Rev Med | Estrategias de tratamiento actuales en hepatitis B y C crónicas |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Revisión | Expert Rev Anti Infect Ther | Opciones de tratamiento de hepatitis B y C crónicas en niños |
| [16838649](https://pubmed.ncbi.nlm.nih.gov/16838649/) | 2006 | Revisión | Nihon Rinsho | Infección HCV-HBV |

No se identificaron ECA entre las publicaciones; todas son revisiones o textos narrativos.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 99107001 | REBETOL 200 MG CÁPSULAS DURAS | Cápsula dura | No disponible en los datos |
| 77096 | RIBAVIRINA AUROVITAS 200 MG CÁPSULAS DURAS EFG | Cápsula dura | No disponible en los datos |
| 09527003 | RIBAVIRINA TEVA PHARMA BV 200 mg COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | Comprimido recubierto con película | No disponible en los datos |
| 99107004 | REBETOL 40 MG/ML SOLUCIÓN ORAL | Solución oral | No disponible en los datos |
| 73658 | RIBAVIRINA NORMON 200 mg COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | Comprimido recubierto con película | No disponible en los datos |

Hay 10 autorizaciones vigentes, todas de monofármaco; se muestran las 5 primeras.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): enfermedad pulmonar obstructiva crónica, asma, sarcoidosis, enfermedad pulmonar intersticial, cirrosis hepática, hepatitis autoinmune, pancreatitis, anemia (incluidas anemia hemolítica, anemia falciforme, hemoglobinopatías, pancitopenia y anemia aplásica hereditaria), insuficiencia renal, infarto de miocardio, enfermedad arterial coronaria, aterosclerosis, isquemia miocárdica y periodontitis.
- **Interacciones farmacológicas**: se identificaron dos interacciones de tipo farmacológico, con las dianas IMPDH1 e IMPDH2 (inhibición enzimática propia del mecanismo del fármaco). No se dispone de interacciones con otros fármacos clasificadas por nivel.
- **Observación relevante**: la literatura describe casos de porfiria cutánea tardía que aparecen o empeoran durante el tratamiento con peginterferón/ribavirina, posiblemente por hemólisis y sobrecarga de hierro.

Consultar el prospecto para el resto de la información de seguridad, ya que no se dispone de advertencias ni contraindicaciones del prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque existen ensayos de Fase 3 con ribavirina en hepatitis B, no hay resultados de eficacia disponibles, la mayoría de los estudios se centra en hepatitis C o coinfección, y los análogos de nucleós(t)idos son hoy el tratamiento estándar. Además, faltan datos de seguridad del prospecto y existen numerosas contraindicaciones en el grafo de conocimiento. Las demás indicaciones predichas (rangos 2 a 10) carecen de respaldo clínico o mecanístico y también quedan en espera.

**Para avanzar se necesita:**
- Obtener y revisar los resultados publicados de los ensayos NCT00114361 y NCT03759782 para confirmar si la ribavirina aporta beneficio adicional en hepatitis B frente a peginterferón o análogos de nucleós(t)idos.
- Descargar y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas).
- Completar los datos del mecanismo de acción desde DrugBank.
- Evaluar el perfil de riesgo-beneficio (anemia hemolítica, teratogenicidad, comorbilidades) frente a las terapias vigentes para hepatitis B.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


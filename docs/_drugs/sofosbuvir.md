---
layout: default
title: Sofosbuvir
parent: Evidencia moderada (L3-L4)
nav_order: 496
evidence_level: L3
indication_count: 8
---

# Sofosbuvir
{: .fs-9 }

Nivel de evidencia: **L3** | Indicaciones predichas: **8** 
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

# Sofosbuvir: De Hepatitis C Crónica a Infección por el Virus de la Hepatitis B

## Resumen en Una Frase

Sofosbuvir es un antiviral de acción directa que se usa para tratar la hepatitis C crónica. El modelo TxGNN predice que podría ser efectivo contra la **infección por el virus de la hepatitis B (VHB)**. Hay **50 ensayos clínicos** y **19 publicaciones** asociados a esta predicción, pero solo un puñado estudia realmente el VHB, y ninguno es un ensayo controlado.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Infección por el virus de la hepatitis B |
| Puntaje de Predicción TxGNN | 99,77 % |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

La ficha de la autorización de AEMPS no incluye el texto de la indicación aprobada. La indicación original (hepatitis C crónica) se toma del conjunto de ensayos y de la literatura aportada.

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base consultada. Según la información conocida, sofosbuvir es un análogo nucleótido que inhibe la ARN polimerasa dependiente de ARN (NS5B) del virus de la hepatitis C. Su eficacia en hepatitis C está bien establecida.

El VHB, en cambio, se replica mediante una ADN polimerasa con actividad de transcriptasa inversa, y no mediante una polimerasa del tipo NS5B. El puntaje tan alto de TxGNN probablemente refleja la cercanía entre nodos de hepatitis viral en el grafo de conocimiento, y no una diana compartida demostrada.

La señal clínica directa más relevante es un estudio de Fase 2, abierto y de un solo brazo, con ledipasvir/sofosbuvir en personas con VHB (PMID 36045503). Se partió de la observación de que, en pacientes coinfectados por VHB y VHC, el HBsAg descendía de forma modesta. Al no ser aleatorizado, la evidencia se queda en L3. Esta predicción se solapa en gran medida con «infección crónica por el virus de la hepatitis B», por lo que conviene revisar ambas juntas.

## Evidencia de Ensayos Clínicos

De los 50 ensayos recuperados, la gran mayoría son estudios de hepatitis C que coinciden solo por el fármaco. Los siguientes son los que abordan el VHB o la coinfección VHC/VHB:

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Fase 2 | Completado | 21 | Ledipasvir/sofosbuvir durante 12 semanas en personas con VHB. Evalúa si se reduce el HBsAg, con la meta de lograr una cura funcional. |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Fase 3 | Completado | 111 | Ledipasvir/sofosbuvir en coinfección VHC (genotipos 1 o 2) y VHB en Taiwán. Evalúa eficacia antiviral, seguridad y tolerabilidad. |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Fase 2/3 | Completado | 23 | Tratamiento antiviral directo en coinfección VHC/VHB. Estudia la incidencia y los factores de riesgo de reactivación del VHB. |
| [NCT02768961](https://clinicaltrials.gov/study/NCT02768961) | Fase 4 | Completado | 64 | Cribado y tratamiento de la hepatitis C en prisiones de Cantabria. Incluye la prevalencia de VHB y VIH, pero el tratamiento se dirige al VHC. |

Los ensayos de Fase 3 de mayor tamaño de la lista, como NCT02996682 y NCT02640482, son estudios de hepatitis C y no aportan evidencia de eficacia frente al VHB.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Ensayo Fase 2 abierto, un brazo | J Med Virol | Ledipasvir/sofosbuvir 12 semanas en monoinfección por VHB. Objetivos: descenso de HBsAg (primario) y de ADN del VHB (secundario). |
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | Cohorte | Trans R Soc Trop Med Hyg | Tratamiento basado en sofosbuvir/daclatasvir en VHC y coinfección VHC/VHB en Egipto. |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Reporte de caso y revisión | Medicine | Reactivación del VHB tras tratar el VHC con sofosbuvir y ribavirina. Señal de seguridad. |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Estudio de cohorte | J Clin Gastroenterol | Evalúa el riesgo de reactivación del VHB durante o después del tratamiento del VHC con ledipasvir/sofosbuvir. |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Estudio observacional prospectivo | J Viral Hepat | Reactivación del VHB con antivirales de acción directa en pacientes oncológicos con coinfección VHC/VHB. |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | Estudio clínico | Infect Drug Resist | Manejo de la reactivación del VHB tras antivirales de acción directa en coinfectados. Valora el papel del tratamiento anti-VHB. |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Reporte de caso | J Med Case Rep | Reactivación del VHB con una variante de escape inmune de HBsAg durante sofosbuvir/velpatasvir. |
| [27621502](https://pubmed.ncbi.nlm.nih.gov/27621502/) | 2015 | Reporte de reacciones adversas | Hosp Pharm | Reactivación de hepatitis B durante tratamiento del VHC con simeprevir y sofosbuvir. |
| [25253190](https://pubmed.ncbi.nlm.nih.gov/25253190/) | 2014 | Revisión | Minerva Pediatr | Tratamiento de las hepatitis B y C en niños. |
| [37517414](https://pubmed.ncbi.nlm.nih.gov/37517414/) | 2023 | Estudio de modelización | Lancet Gastroenterol Hepatol | Prevalencia global del VHB, cascada de atención y cobertura de profilaxis en 2022. Aporta contexto epidemiológico. |

Salvo el estudio de Fase 2 (PMID 36045503), la literatura sobre VHB y sofosbuvir se refiere sobre todo a la reactivación del VHB durante el tratamiento del VHC. Es decir, aporta señales de seguridad y no de eficacia.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 113894001 | SOVALDI 400 mg comprimidos recubiertos con película | Comprimido recubierto con película | Gilead Sciences Ireland Unlimited Company |

## Consideraciones de Seguridad

- **Reactivación del VHB**: varios reportes y estudios de cohorte describen reactivación del VHB en personas con coinfección VHC/VHB tratadas con antivirales de acción directa que incluyen sofosbuvir (PMIDs 33031326, 29334502, 33523503, 31542053). Es la principal señal de seguridad para esta indicación y exige un plan de monitoreo específico.
- **Interacciones farmacológicas**: no se encontraron interacciones registradas en la consulta realizada.

Para el resto de advertencias y contraindicaciones, consultar el prospecto y la ficha técnica de AEMPS.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La única evidencia clínica directa es un estudio de Fase 2 pequeño (21 participantes), abierto y de un solo brazo. Además, el mecanismo del fármaco no encaja con la polimerasa del VHB, y hay un riesgo documentado de reactivación del VHB. Es una pregunta de investigación razonable, pero aún no una candidata para avanzar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), porque este dato bloquea la evaluación de seguridad.
- Confirmar los resultados de NCT03312023 y del estudio de Fase 2 (PMID 36045503), en particular el descenso de HBsAg y ADN del VHB.
- Realizar un ensayo controlado en VHB que demuestre eficacia frente a los tratamientos estándar.
- Aclarar el mecanismo de acción y la plausibilidad frente a la polimerasa/transcriptasa inversa del VHB.
- Definir un plan de monitoreo y profilaxis frente a la reactivación del VHB.
- Revisar esta predicción junto con «infección crónica por el virus de la hepatitis B» para evitar duplicidades.

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


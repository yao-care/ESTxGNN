---
layout: default
title: Pemetrexed
parent: Solo predicción del modelo (L5)
nav_order: 619
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-31
monitor_inn: "PEMETREXED"
predicted_indications: ["pleural adenomatoid tumor", "pericardium cancer", "iminoglycinuria"]
description: "Pemetrexed: nueva indicación predicha, Pleural adenomatoid tumor (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Pemetrexed
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Pemetrexed: Pleural adenomatoid tumor
{: .text-alpha }

## Resumen en Una Frase

Pemetrexed es un antifolato multidiana, originalmente utilizado en el cáncer de pulmón no microcítico y en el mesotelioma pleural maligno.
El modelo TxGNN predice que podría ser eficaz en el **mesotelioma peritoneal maligno**, con **7 ensayos clínicos** y **20 publicaciones** que respaldan esta dirección, aunque casi todos son de Fase 2 y de muestra pequeña.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Pleural adenomatoid tumor |
| Puntaje de Predicción TxGNN | 0.9999 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 2) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados del mecanismo de acción en la base de datos consultada. Según el análisis compilado para este informe, pemetrexed inhibe la timidilato sintasa (TS), la dihidrofolato reductasa (DHFR) y la glicinamida ribonucleótido formiltransferasa (GARFT). Con ello bloquea la síntesis de nucleótidos dependiente de folato y frena la división de las células tumorales.

El mesotelioma pleural y el peritoneal comparten histología y biología. Por eso es plausible que la sensibilidad a los antifolatos demostrada en la enfermedad pleural se extienda a la peritoneal. De hecho, la combinación de pemetrexed y cisplatino, estándar en el mesotelioma pleural, ya se utiliza con frecuencia en el peritoneal, aunque su eficacia en esta localización sigue sin estar bien definida.

Conviene ser prudente: la evidencia procede de ensayos de Fase 2 y de cohortes mixtas pleurales/peritoneales, no de un ensayo de Fase 3 específico para el peritoneo. Se trata, por tanto, de una extrapolación. Además, varios ensayos están suspendidos o aún en reclutamiento.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Fase 2 | Completado | 48 | Pemetrexed + gemcitabina en primera línea para mesotelioma pleural o peritoneal; evalúa seguridad, supervivencia y respuesta tumoral. Es la evidencia completada más directa para el peritoneo |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Fase 2 | Reclutando | 66 | Aleatorizado: carboplatino + pemetrexed + bevacizumab con o sin atezolizumab en mesotelioma peritoneal |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Fase 2 | Suspendido | 66 | MESOTIP: PIPAC + quimioterapia sistémica (cisplatino + pemetrexed) frente a quimioterapia sistémica sola en primera línea |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Fase 2 | Reclutando | 28 | Un solo brazo: sintilimab + bevacizumab + pemetrexed + cisplatino en mesotelioma peritoneal irresecable |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Fase 1 | Completado | 19 | Cisplatino, pemetrexed e imatinib en mesotelioma maligno metastásico o irresecable; dosis máxima tolerada y viabilidad |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Fase 1/2 | Activo, no reclutando | 30 | TRC102 con cisplatino y pemetrexed en tumores sólidos avanzados o mesotelioma; ensayo tipo cesta con pocos pacientes peritoneales |
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Fase 2 | Reclutando | 64 | ICARuS II: quimioterapia intraperitoneal frente a intravenosa tras cirugía citorreductora y HIPEC; el papel del pemetrexed no está claro |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Estudio clínico | Jpn J Clin Oncol | Eficacia y seguridad de pemetrexed + cisplatino en primera línea en mesotelioma peritoneal avanzado |
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Estudio retrospectivo | Expert Rev Anticancer Ther | Evaluación retrospectiva de pemetrexed + cisplatino en primera línea |
| [21528659](https://pubmed.ncbi.nlm.nih.gov/21528659/) | 2011 | Serie de un centro | Tumori | Pemetrexed-cisplatino en pacientes sin quimioterapia previa: eficacia y seguridad |
| [41133016](https://pubmed.ncbi.nlm.nih.gov/41133016/) | 2025 | Estudio comparativo | Clin Med Insights Oncol | Comparación de pemetrexed-platino y gemcitabina-platino en primera línea |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Cohorte retrospectiva multicéntrica | Ann Surg Oncol | Estrategias de tratamiento y resultados en mesotelioma peritoneal |
| [39413826](https://pubmed.ncbi.nlm.nih.gov/39413826/) | 2024 | Revisión | JNCCN | Opciones sistémicas; las recomendaciones se extrapolan de ensayos en mesotelioma pleural |
| [36765620](https://pubmed.ncbi.nlm.nih.gov/36765620/) | 2023 | Revisión | Cancers | Ruta diagnóstica y terapéutica; la cirugía citorreductora con HIPEC logra la mejor supervivencia |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Revisión | J Clin Med | Tratamiento: cirugía citorreductora e HIPEC como opción inicial preferida en pacientes seleccionados |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Revisión | Transl Lung Cancer Res | Revisión de una neoplasia muy rara y de mal pronóstico |
| [33257382](https://pubmed.ncbi.nlm.nih.gov/33257382/) | 2020 | Reporte de caso | BMJ Case Rep | Nivolumab en mesotelioma peritoneal tras quimioterapia sistémica inicial |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 86508 | Pemetrexed Sun 6 mg/ml | Solución para perfusión | No disponible |
| 80631 | Pemetrexed Tamarang 100 mg EFG | Polvo para concentrado para solución para perfusión | No disponible |
| 87989 | Pemetrexed Aurovitas 500 mg EFG | Polvo para concentrado para solución para perfusión | No disponible |
| 80985 | Pemetrexed Tillomed 500 mg EFG | Polvo para concentrado para solución para perfusión | No disponible |
| 90206 | Pemetrexed Glenmark 500 mg EFG | Polvo para concentrado para solución para perfusión | No disponible |

Hay 20 autorizaciones vigentes, todas de principio activo único; aquí se muestran 5.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Citotóxico convencional (antimetabolito, antifolato) |
| Riesgo de Mielosupresión | Alto: el grafo de conocimiento asocia el fármaco con neutropenia, trombocitopenia, agranulocitosis y anemia como contraindicaciones o riesgos |
| Clasificación de Emetogenicidad | Baja a moderada (clasificación general de la clase; consultar el prospecto) |
| Items de Monitoreo | Hemograma completo con diferencial, función renal (aclaramiento de creatinina), función hepática |
| Protección en Manejo | Debe seguir las normas de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Enfermedades de riesgo según el grafo de conocimiento** (no proceden del texto del prospecto): enfermedad renal, insuficiencia renal, trombocitopenia, neutropenia, agranulocitosis, anemia y anemia macrocítica, y piouréter.
- **Interacciones farmacológicas**: se identificaron 100 interacciones, de las cuales se muestran las primeras 20, todas de nivel moderado. Incluyen famotidina, ranitidina, cimetidina, metformina, ácido acetilsalicílico, amoxicilina, vancomicina, levofloxacino, mesalazina, balsalazida, olsalazina, sapropterina, polimixina B y varios aminoglucósidos (kanamicina, neomicina). También figuran las formulaciones de anfotericina B (convencional, complejo lipídico, sulfato de colesterilo y liposomal). Muchas de ellas afectan a la función renal o a la eliminación del fármaco.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 2 completado con pemetrexed en mesotelioma pleural o peritoneal, varios estudios retrospectivos de pemetrexed-cisplatino en el peritoneo y un respaldo sólido en el mesotelioma pleural (Fase 3). Sin embargo, no hay un ensayo de Fase 3 específico para el peritoneo y la muestra de los estudios es pequeña.

**Para avanzar se necesita:**
- Resultados de los ensayos aleatorizados de Fase 2 en curso (NCT05001880, NCT03875144, NCT06543069)
- Datos del mecanismo de acción y de advertencias y contraindicaciones del prospecto de la AEMPS, hoy no disponibles
- Plan de monitoreo hematológico y renal, y revisión de la medicación concomitante (antiinflamatorios, antiulcerosos, nefrotóxicos)
- Comparación con las alternativas actuales de primera línea (nivolumab + ipilimumab, quimioinmunoterapia)

**Otras predicciones del modelo:**
- Mesotelioma pleural, epitelioide, sarcomatoide y bifásico (L1 a L2): ya cubiertos por la indicación aprobada o por ella extrapolables; sirven como control positivo del modelo.
- Cáncer de pericardio y mesotelioma papilar bien diferenciado (L4, Hold): solo reportes de caso, sin ensayos.
- Tumor adenomatoide pleural, mesotelioma linfohistiocitoide e iminoglicinuria (L5, Hold): sin respaldo clínico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


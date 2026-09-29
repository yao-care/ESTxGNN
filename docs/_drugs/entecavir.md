---
layout: default
title: Entecavir
parent: Solo predicción del modelo (L5)
nav_order: 202
evidence_level: L5
indication_count: 10
---

# Entecavir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Entecavir: De Hepatitis B Crónica a Infección Crónica por Virus de la Hepatitis C

## Resumen en Una Frase

Entecavir es un análogo nucleosídico de la guanosina, utilizado para tratar la hepatitis B crónica. El modelo TxGNN predice que podría ser efectivo para la **infección crónica por el virus de la hepatitis C (VHC)**. Aunque el Evidence Pack recupera **40 ensayos clínicos** y **20 publicaciones** asociados a esta predicción, **ninguno demuestra actividad de entecavir contra el VHC**: casi todos tratan hepatitis B o coinfección VHB/VHC.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hepatitis B crónica (el texto de indicación de las autorizaciones españolas no está disponible; se toma del uso conocido del fármaco) |
| Nueva Indicación Predicha | Infección crónica por el virus de la hepatitis C |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L4 (solo evidencia indirecta; sin estudios de eficacia frente al VHC) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Entecavir se fosforila a su forma trifosfato, que inhibe de forma competitiva las tres actividades de la polimerasa del VHB: cebado de bases, transcripción inversa de la cadena negativa y síntesis de la cadena positiva.

Las hepatitis B y C son enfermedades hepáticas virales crónicas que comparten vías de transmisión y desenlaces (cirrosis y carcinoma hepatocelular). Por eso están muy próximas en el grafo de conocimiento de TxGNN, y esa cercanía explica probablemente el puntaje tan alto.

**Sin embargo, el vínculo mecanístico directo no existe.** El VHC es un virus ARN que se replica mediante la ARN polimerasa dependiente de ARN NS5B. Entecavir no tiene actividad anti-VHC establecida. Los estudios recuperados tratan sobre el manejo de la coinfección, donde entecavir controla el componente VHB y los antivirales de acción directa tratan el VHC. Esto no respalda a entecavir como tratamiento de la hepatitis C.

## Evidencia de Ensayos Clínicos

Se muestran 10 de los 40 ensayos recuperados, priorizando los más cercanos al VHC. Ninguno evalúa entecavir como tratamiento de la hepatitis C.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Fase 2/3 | Completado | 23 | Reactivación del VHB durante el tratamiento anti-VHC con antivirales de acción directa en pacientes coinfectados VHC/VHB |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | N/A | Desconocido | 60 | Profilaxis con análogos nucleos(t)ídicos para prevenir la reactivación del VHB en coinfectados VHC/VHB tratados con antivirales de acción directa |
| [NCT01018381](https://clinicaltrials.gov/study/NCT01018381) | N/A | Completado | 130 | Arabinoxilano de salvado de arroz (MGN-3) en carcinoma hepatocelular y hepatitis B y C; no evalúa entecavir |
| [NCT01270178](https://clinicaltrials.gov/study/NCT01270178) | N/A | Desconocido | 420 | Entecavir en hepatitis B crónica de pacientes con carcinoma hepatocelular tras ablación por radiofrecuencia |
| [NCT04157257](https://clinicaltrials.gov/study/NCT04157257) | Fase 2 | Desconocido | 60 | QL-007 combinado con entecavir o tenofovir en hepatitis B crónica; entecavir actúa como base para el VHB |
| [NCT00597259](https://clinicaltrials.gov/study/NCT00597259) | Fase 4 | Desconocido | 294 | Peginterferón más entecavir frente a entecavir solo en hepatitis B crónica HBeAg positiva |
| [NCT01022801](https://clinicaltrials.gov/study/NCT01022801) | Fase 2 | Completado | 120 | Entecavir frente a lamivudina en hepatitis B crónica en Japón |
| [NCT01848743](https://clinicaltrials.gov/study/NCT01848743) | Fase 3 | Desconocido | 120 | Tenofovir frente a lamivudina en hepatitis B crónica con exacerbación aguda grave |
| [NCT05005507](https://clinicaltrials.gov/study/NCT05005507) | Fase 2 | Terminado | 1 | JNJ-73763989 con análogos nucleos(t)ídicos y peginterferón en hepatitis B; terminado con un solo participante |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Fase 2/3 | Completado | 120 | Interferón alfa-2b más ribavirina en hepatitis B crónica |

## Evidencia de Literatura

Se muestran 10 de las 20 publicaciones recuperadas. Ninguna es un ensayo aleatorizado y ninguna aporta datos de eficacia de entecavir frente al VHC.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohorte | Viruses | Reactivación del VHC en 66 pacientes anti-VHC positivos con hepatitis B crónica tras tratamientos anti-VHB con análogos nucleos(t)ídicos |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Revisión | Expert Opin Pharmacother | Avances en el tratamiento de la coinfección VHB/VHC, con alto riesgo de cirrosis y carcinoma hepatocelular |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Revisión / caso | Clin Res Hepatol Gastroenterol | Coinfección VHB/VHC como desafío terapéutico, con lesión hepática más grave |
| [36873880](https://pubmed.ncbi.nlm.nih.gov/36873880/) | 2023 | Reporte de caso | Front Med | Evolución viral inusual tras terapias antivirales en un paciente con infección concurrente por VHB y VHC |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | No clasificado | J Gastroenterol Hepatol | Riesgo de reactivación del VHB durante el tratamiento de la hepatitis C con antivirales de acción directa |
| [32527114](https://pubmed.ncbi.nlm.nih.gov/32527114/) | 2021 | No clasificado | Chin Clin Oncol | Momento óptimo para tratar las hepatitis B y C en pacientes con carcinoma hepatocelular |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | No clasificado | Minerva Gastroenterol Dietol | Antivirales para hepatitis B y C y sus efectos sobre la función renal |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | No clasificado | Wien Med Wochenschr | Tratamiento actual y perspectivas terapéuticas en hepatitis B y C crónicas |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | No clasificado | Clin Res Hepatol Gastroenterol | Manejo actual y futuro de las hepatitis virales B y C en niños |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | No clasificado | World J Hepatol | Manejo de las hepatitis B y C antes y después del trasplante hepático y renal |

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones. El texto de la indicación aprobada no figura en los datos recibidos, por lo que no se incluye.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 82136 | Entecavir Stada 0,5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 84926 | Entecavir Sun 0,5 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 06343003 | Baraclude 0,5 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 82135 | Entecavir Normon 1 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 83505 | Entecavir Tarbis 1 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay vínculo mecanístico directo entre entecavir (inhibidor de la polimerasa del VHB) y el VHC, y los ensayos y publicaciones recuperados son de hepatitis B o coinfección, sin evidencia de eficacia anti-VHC. Además, para el VHC ya existen antivirales de acción directa que actúan sobre sus propias dianas. El puntaje alto de TxGNN parece reflejar la cercanía entre hepatitis B y C en el grafo.

**Para avanzar se necesita:**
- Datos de actividad in vitro de entecavir frente al VHC (por ejemplo, ensayos de replicón), como mínimo requisito antes de considerar estudios clínicos.
- Completar los datos de seguridad de la ficha técnica de la AEMPS (advertencias y contraindicaciones), actualmente ausentes.
- Completar el texto de las indicaciones aprobadas en las autorizaciones españolas.
- En coinfección VHB/VHC, considerar el papel real de entecavir: controlar el VHB y prevenir su reactivación durante el tratamiento anti-VHC. Es un uso distinto y ya cubierto por su indicación en hepatitis B.

Nota: la indicación de hepatitis B crónica figura en este mismo Evidence Pack como segunda predicción, con nivel L1 y varios ensayos de Fase 3. Es una indicación ya establecida, no un reposicionamiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Ertapenem
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 2
---

# Ertapenem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Ertapenem: De Infecciones Bacterianas Complicadas a Artritis Séptica y Bacteriemia Persistente por *Staphylococcus aureus* (MSSA)

## Resumen en Una Frase

Ertapenem (DrugBank ID: DB00303) es un antibiótico carbapenémico de amplio espectro, ya utilizado clínicamente para infecciones bacterianas graves. El modelo TxGNN predice dos nuevas direcciones de uso: **Artritis Bacteriana (séptica)**, respaldada por el momento solo por evidencia mecanística y reportes de caso aislados (0 ensayos clínicos, 10 publicaciones), y **Infección por Staphylococcus aureus** —en la práctica clínica real, uso combinado con cefazolina para bacteriemia persistente por MSSA—, respaldada por **8 ensayos clínicos** (incluyendo un ECA de fase 2 en curso) y **20 publicaciones**.

---

## Resumen Rápido

### Indicación Predicha 1: Artritis Bacteriana (Séptica)

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las fuentes consultadas (Ertapenem es un antibiótico carbapenémico de amplio espectro usado en infecciones bacterianas graves) |
| Nueva Indicación Predicha | Artritis Bacteriana (séptica) |
| Puntaje de Predicción TxGNN | 99.72% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

### Indicación Predicha 2: Infección por Staphylococcus aureus (MSSA)

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las fuentes consultadas (Ertapenem es un antibiótico carbapenémico de amplio espectro usado en infecciones bacterianas graves) |
| Nueva Indicación Predicha | Infección por Staphylococcus aureus (bacteriemia persistente por MSSA) |
| Puntaje de Predicción TxGNN | 99.28% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de ertapenem en las fuentes consultadas. Según la información conocida, ertapenem pertenece a la clase de los carbapenems (antibióticos betalactámicos de amplio espectro), que ejercen su efecto bactericida inhibiendo la síntesis de la pared celular bacteriana mediante la unión a proteínas fijadoras de penicilina (PBPs). Su eficacia en infecciones bacterianas graves está ampliamente establecida, por lo que mecanísticamente su actividad frente a determinados patógenos podría extenderse a otros escenarios de infección con los mismos microorganismos.

**Artritis Bacteriana (séptica):** Ertapenem presenta buena actividad in vitro frente a la mayoría de los bacilos Gram-negativos entéricos que causan artritis séptica (p. ej., *Klebsiella pneumoniae*, *Citrobacter koseri*) y frente a ciertos anaerobios (*Clostridium paraputrificum*, *Prevotella bivia*), además de buena penetración en tejido óseo y articular. Esto lo convierte, en teoría, en una opción razonable cuando el antibiograma lo indica. Sin embargo, no existe ningún ensayo clínico diseñado específicamente para esta indicación; la evidencia proviene casi en su totalidad de reportes de caso de patógenos individuales, es decir, de práctica clínica guiada por sensibilidad (antibiogram-guided), no de evidencia sistemáticamente validada.

**Infección por Staphylococcus aureus (MSSA):** Ertapenem en monoterapia tiene actividad bactericida limitada frente a MSSA, pero combinado con cefazolina genera un efecto sinérgico al inhibir simultáneamente distintas PBPs (PBP1a/1b y PBP2/4). Esta combinación se ha usado en múltiples centros para eliminar bacteriemias persistentes por MSSA que no respondieron a betalactámicos anti-estafilocócicos estándar (cefazolina u oxacilina en monoterapia). Es importante señalar que la etiqueta TxGNN "staphylococcus aureus infection" es demasiado amplia: la evidencia real respalda únicamente el uso de **cefazolina + ertapenem como terapia de rescate** en bacteriemia por MSSA persistente/refractaria, no el uso de ertapenem como monoterapia de primera línea para infecciones por *S. aureus* en general, y no tiene actividad frente a MRSA.

---

## Evidencia de Ensayos Clínicos

### Artritis Bacteriana (Séptica)

Actualmente no hay ensayos clínicos relacionados registrados.

### Infección por Staphylococcus aureus (MSSA)

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04886284](https://clinicaltrials.gov/study/NCT04886284) | Fase 2 | Reclutando | 60 | **CERT** — Combinación cefazolina + ertapenem para bacteriemia por MSSA; primer ECA diseñado específicamente para esta combinación (sub-estudio de la plataforma SNAP/NCT05137119). Relevancia: A (evidencia clave, aún sin resultados finales). |
| [NCT07376889](https://clinicaltrials.gov/study/NCT07376889) | Fase 4 | Aún no reclutando | 2096 | **COMBAT-SAB** — Terapia combinada de antibióticos vs. monoterapia en bacteriemia por *S. aureus*; no se ha confirmado si ertapenem es uno de los fármacos del esquema combinado. Relevancia: B. |
| [NCT07148960](https://clinicaltrials.gov/study/NCT07148960) | Fase 4 | Reclutamiento por invitación | 300 | **SABEDTIO** — Evalúa si la terapia dual IV temprana reduce la duración de la bacteriemia por *S. aureus* frente a monoterapia; esquema de fármacos concretos no confirmado. Relevancia: B. |
| [NCT00366249](https://clinicaltrials.gov/study/NCT00366249) | Fase 3 | Completado | 1061 | Tigeciclina vs. ertapenem en infecciones de pie diabético; los criterios de eficacia coprimarios no se cumplieron. No es bacteriemia por *S. aureus* específicamente. Relevancia: C. |
| [NCT03218397](https://clinicaltrials.gov/study/NCT03218397) | No aplica | Completado | 500 | **RAPIDS-GN** — Prueba de identificación/sensibilidad rápida en bacteriemia por Gram-negativos; no es un ensayo terapéutico ni específico de *S. aureus*. Relevancia: C. |
| [NCT06174649](https://clinicaltrials.gov/study/NCT06174649) | No aplica | Completado | 900 | **FAST** — Prueba de sensibilidad antimicrobiana rápida en bacteriemia por Gram-negativos; no terapéutico, no específico de *S. aureus*. Relevancia: C. |
| [NCT06044272](https://clinicaltrials.gov/study/NCT06044272) | No aplica | Completado | 10000 | Vigilancia epidemiológica de resistencia antimicrobiana en Colombia; observacional, sin relación causal directa con eficacia de ertapenem. Relevancia: C. |
| [NCT06634940](https://clinicaltrials.gov/study/NCT06634940) | No aplica | Reclutando | 1000 | Vigilancia internacional de resistencia antimicrobiana en infecciones asociadas a cirrosis; observacional, no específico de *S. aureus*. Relevancia: C. |

---

## Evidencia de Literatura

### Artritis Bacteriana (Séptica)

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24709258](https://pubmed.ncbi.nlm.nih.gov/24709258/) | 2014 | Cohorte | Antimicrob Agents Chemother | Terapia ambulatoria prolongada con ertapenem (306 pacientes); las infecciones óseas/articulares fueron una de las indicaciones más comunes tratadas con seguridad aceptable. |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Epidemiología retrospectiva | Clin Lab | Distribución de patógenos y resistencia antimicrobiana en infecciones óseas y articulares en niños pequeños. |
| [31220276](https://pubmed.ncbi.nlm.nih.gov/31220276/) | 2019 | Cohorte | J Antimicrob Chemother | Terapia supresora subcutánea con betalactámicos (off-label) en infecciones óseas/articulares crónicas; seguridad y desenlace en 10 pacientes. |
| [31585203](https://pubmed.ncbi.nlm.nih.gov/31585203/) | 2020 | Reporte de caso | Anaerobe | Artritis séptica y osteomielitis de hombro por *Clostridium paraputrificum*, tratada con desbridamiento y antibioterapia. |
| [37578166](https://pubmed.ncbi.nlm.nih.gov/37578166/) | 2023 | Reporte de caso | J Investig Med High Impact Case Rep | Artritis séptica por *Prevotella bivia* en adulto inmunocompetente. |
| [22233826](https://pubmed.ncbi.nlm.nih.gov/22233826/) | 2011 | Reporte de caso | J Chemother | Artritis séptica de muñeca por *Klebsiella pneumoniae* tratada con éxito con ertapenem y levofloxacino. |
| [31352398](https://pubmed.ncbi.nlm.nih.gov/31352398/) | 2019 | Reporte de caso | BMJ Case Rep | Osteomielitis por *Citrobacter koseri* con artritis gotosa concomitante en pie diabético, tratada con ertapenem. |
| [38924836](https://pubmed.ncbi.nlm.nih.gov/38924836/) | 2024 | Estudio in vitro/mecanístico | Diagn Microbiol Infect Dis | Auranofin potencia el efecto antibacteriano de ertapenem frente a *E. coli* resistente a carbapenems (no es evidencia clínica de artritis). |
| [41878879](https://pubmed.ncbi.nlm.nih.gov/41878879/) | 2026 | Revisión/comparativo | J Antimicrob Chemother | Evalúa temocilina como alternativa a carbapenems en infecciones óseas/articulares por Enterobacterales resistentes a cefalosporinas de 3ª generación (comparador, no evidencia directa de ertapenem). |

*Nota: se excluyó 1 publicación (PMID 29183082, sobre Hidradenitis Suppurativa) por tratarse de un emparejamiento erróneo en la base de datos, sin relación con artritis bacteriana.*

### Infección por Staphylococcus aureus (MSSA)

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38946294](https://pubmed.ncbi.nlm.nih.gov/38946294/) | 2024 | Cohorte comparativa | J Antimicrob Chemother | Terapia combinada con carbapenem vs. tratamiento estándar en bacteriemia persistente por MSSA. |
| [31773134](https://pubmed.ncbi.nlm.nih.gov/31773134/) | 2020 | Cohorte/serie de casos | Clin Infect Dis | Cefazolina + ertapenem como terapia de rescate elimina rápidamente la bacteriemia persistente por MSSA (11 casos, 6 con endocarditis). |
| [27572414](https://pubmed.ncbi.nlm.nih.gov/27572414/) | 2016 | Cohorte/serie de casos | Antimicrob Agents Chemother | Descripción original de la combinación sinérgica cefazolina + ertapenem para eliminar bacteriemia refractaria por MSSA, confirmada in vitro e in vivo. |
| [39230345](https://pubmed.ncbi.nlm.nih.gov/39230345/) | 2025 | Revisión | Am J Health Syst Pharm | Revisión de opciones de tratamiento combinado para bacteriemia persistente por MSSA. |
| [34978891](https://pubmed.ncbi.nlm.nih.gov/34978891/) | 2022 | Mecanístico | Antimicrob Agents Chemother | Propone que el éxito de cefazolina + ertapenem se relaciona con la liberación de interleucina-1β, impulsada principalmente por ertapenem. |
| [35493130](https://pubmed.ncbi.nlm.nih.gov/35493130/) | 2022 | Mecanístico | Open Forum Infect Dis | Ertapenem + cefazolina muestra actividad potente dentro de biofilms estafilocócicos, relevante para endocarditis por MSSA. |
| [40448546](https://pubmed.ncbi.nlm.nih.gov/40448546/) | 2025 | Cohorte (PK/desenlace) | J Antimicrob Chemother | La hipoalbuminemia puede reducir la exposición a ertapenem y afectar el desenlace de la terapia combinada en bacteriemia por MSSA. |
| [36401791](https://pubmed.ncbi.nlm.nih.gov/36401791/) | 2023 | Serie de casos | Pharmacotherapy | Primer caso publicado de bacteriemia persistente por MSSA con osteomielitis en un neonato prematuro, tratado con oxacilina + ertapenem. |
| [35393639](https://pubmed.ncbi.nlm.nih.gov/35393639/) | 2022 | Reporte de caso | J Card Surg | Oxacilina + ertapenem elimina rápidamente bacteriemia persistente por MSSA asociada a dispositivo de asistencia ventricular izquierda (LVAD). |
| [34599521](https://pubmed.ncbi.nlm.nih.gov/34599521/) | 2021 | Reporte de caso | J Card Surg | Cefazolina + ertapenem junto con trasplante cardíaco como terapia de rescate en infección refractaria de LVAD por MSSA. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Artritis Bacteriana (séptica) — Decisión: Hold**

**Justificación:**
No existe ningún ensayo clínico diseñado para esta indicación; la evidencia se limita a reportes de caso de patógenos individuales y un estudio mecanístico in vitro. Es una hipótesis razonable desde el punto de vista microbiológico, pero corresponde a una pregunta de investigación (Research Question), no a una decisión de avance clínico.

**Infección por Staphylococcus aureus (bacteriemia persistente por MSSA) — Decisión: Proceed with Guardrails**

**Justificación:**
Existe un cuerpo consistente de literatura (cohortes, series de casos y un estudio mecanístico) que respalda específicamente la combinación cefazolina/oxacilina + ertapenem como terapia de rescate en bacteriemia persistente por MSSA, junto con un ECA de fase 2 en curso (NCT04886284) diseñado exactamente para esta pregunta. Sin embargo, la etiqueta amplia "infección por *S. aureus*" no debe interpretarse como uso general ni como cobertura de MRSA.

**Para avanzar se necesita en ambos casos:**
- Obtener el texto completo del prospecto/ficha técnica de ertapenem (advertencias y contraindicaciones), actualmente bloqueante (dato clasificado como "Blocking" para la evaluación de seguridad S1)
- Datos detallados del mecanismo de acción (MOA) desde DrugBank
- Resultados finales del ECA NCT04886284 (CERT) antes de confirmar la indicación de MSSA
- Para artritis bacteriana: diseño de un estudio prospectivo o al menos una serie de casos consolidada que valide el uso dirigido por antibiograma
- Plan de monitoreo de seguridad específico para uso combinado (cefazolina/oxacilina + ertapenem) en poblaciones vulnerables (neonatos, pacientes con hipoalbuminemia)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


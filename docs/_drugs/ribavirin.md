---
layout: default
title: Ribavirin
parent: Solo predicción del modelo (L5)
nav_order: 465
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Ribavirina: De Hepatitis C a Infección Crónica por el Virus de la Hepatitis B

## Resumen en Una Frase

La ribavirina es un antiviral análogo de nucleósidos, usado sobre todo junto con interferón en la hepatitis C crónica y, en aerosol, en infecciones por virus respiratorio sincitial.
El modelo TxGNN predice que podría ser efectiva para la **infección crónica por el virus de la hepatitis B (VHB)**.
Los **50 ensayos clínicos** y las **20 publicaciones** recuperados tratan de hepatitis C o de coinfección VHC/VHB, y **ninguno evalúa la ribavirina en monoinfección por VHB**. La evidencia es solo indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hepatitis C crónica (según datos de farmacología; los registros de autorización no incluyen el texto de indicación) |
| Nueva Indicación Predicha | Infección crónica por el virus de la hepatitis B |
| Puntaje de Predicción TxGNN | 99.86% |
| Nivel de Evidencia | L4 (indirecta: sin estudios en VHB; solo ensayos en VHC y revisiones de coinfección) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 10 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información farmacológica disponible, la ribavirina es un antimetabolito nucleósido que bloquea la síntesis de ácidos nucleicos. Sus dianas humanas registradas son la inosina monofosfato deshidrogenasa 1 y 2 (IMPDH1 e IMPDH2). Su eficacia en la hepatitis C está bien establecida, sobre todo en combinación con interferón.

La predicción probablemente se explica por la cercanía en el grafo de conocimiento entre la hepatitis C y la hepatitis B. Ambas son hepatitis virales crónicas y coexisten con frecuencia en la coinfección VHC/VHB. Por eso el modelo asigna una puntuación muy alta.

Mecanísticamente, sin embargo, el vínculo es débil. El VHB es un virus de ADN que se replica por transcripción inversa, y la ribavirina no tiene eficacia establecida frente a él. En las revisiones recuperadas, la ribavirina aparece como parte del tratamiento de la hepatitis C, no como tratamiento del VHB. Por tanto, la predicción es una hipótesis sin respaldo clínico directo.

---

## Evidencia de Ensayos Clínicos

Se recuperaron 50 ensayos. Se muestran 10 representativos. Todos se refieren a hepatitis C, salvo uno en hepatitis D y otro de cribado en prisiones que incluye VHB solo como objetivo de cribado.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02731131](https://clinicaltrials.gov/study/NCT02731131) | Fase 2 | Completado | 12 | Peginterferón alfa-2a con o sin ribavirina en hepatitis D crónica (piloto pequeño; no es VHB) |
| [NCT02768961](https://clinicaltrials.gov/study/NCT02768961) | Fase 4 | Completado | 64 | Cribado de VHC, VHB y VIH en población penitenciaria y tratamiento del VHC sin interferón |
| [NCT00800748](https://clinicaltrials.gov/study/NCT00800748) | Fase 4 | Completado | 372 | Peginterferón alfa-2a + ribavirina (Copegus) en hepatitis C, incluidos pacientes coinfectados por VIH |
| [NCT01858766](https://clinicaltrials.gov/study/NCT01858766) | Fase 2 | Completado | 379 | Sofosbuvir + velpatasvir, con o sin ribavirina, en hepatitis C sin tratamiento previo |
| [NCT02994056](https://clinicaltrials.gov/study/NCT02994056) | Fase 2 | Completado | 32 | Sofosbuvir/velpatasvir + ribavirina en hepatitis C con cirrosis Child-Pugh C |
| [NCT01337375](https://clinicaltrials.gov/study/NCT01337375) | Fase 1 | Completado | 31 | Farmacocinética de peginterferón alfa-2a intravenoso en hepatitis C sin respuesta previa |
| [NCT02120274](https://clinicaltrials.gov/study/NCT02120274) | Fase 4 | Terminado | 85 | Suplementación con vitaminas D y B12 junto a peginterferón + ribavirina en hepatitis C |
| [NCT00561353](https://clinicaltrials.gov/study/NCT00561353) | Fase 2 | Completado | 121 | TMC435350 con o sin peginterferón + ribavirina en hepatitis C genotipo 1 |
| [NCT01457937](https://clinicaltrials.gov/study/NCT01457937) | Fase 3 | Desconocido | 240 | Boceprevir + peginterferón/ribavirina en mujeres menopáusicas con hepatitis C |
| [NCT00493805](https://clinicaltrials.gov/study/NCT00493805) | Fase 4 | Terminado | 59 | Peginterferón alfa-2b + ribavirina en hepatitis C con resistencia a la insulina |

---

## Evidencia de Literatura

Se recuperaron 20 publicaciones. Se muestran 10, todas revisiones. No hay ECA que evalúen la ribavirina en VHB.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Revisión | Viruses | Coinfección VHC/VHB: mayor riesgo de progresión; peginterferón + ribavirina se recomendaba si el ARN del VHC es positivo |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Revisión | World J Gastroenterol | Actualización del tratamiento y los desenlaces de la doble infección VHC/VHB |
| [19669238](https://pubmed.ncbi.nlm.nih.gov/19669238/) | 2009 | Revisión | Hepatol Int | Interacciones entre ambos virus en la doble infección crónica |
| [27433078](https://pubmed.ncbi.nlm.nih.gov/27433078/) | 2016 | Revisión | World J Gastroenterol | El tratamiento clásico de VHB y VHC era interferón ± ribavirina; hoy los antivirales de acción directa han cambiado el estándar |
| [16838649](https://pubmed.ncbi.nlm.nih.gov/16838649/) | 2006 | Revisión | Nihon Rinsho | En hepatitis C, peginterferón alfa-2b + ribavirina es la combinación inicial más eficaz |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Revisión | Expert Rev Anti Infect Ther | Opciones de tratamiento de hepatitis B y C crónicas en niños |
| [15864105](https://pubmed.ncbi.nlm.nih.gov/15864105/) | 2005 | Revisión | Curr Opin Infect Dis | Infecciones por VHB y VHC en niños: historia natural, eficacia y seguridad de las terapias |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | Revisión | World J Gastroenterol | El polimorfismo de IL28B se asocia con la respuesta a peginterferón + ribavirina en VHC; su papel en VHB es incierto |
| [21538279](https://pubmed.ncbi.nlm.nih.gov/21538279/) | 2011 | Revisión | Semin Liver Dis | Genética del huésped en hepatitis B y C crónicas |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | Revisión (sin clasificar) | Annu Rev Med | Estrategias de tratamiento actuales en hepatitis B y C crónicas |

---

## Información de Mercado en España

Se muestran 5 de las 10 autorizaciones. El registro no incluye el texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 99107001 | Rebetol 200 mg cápsulas duras | Cápsula dura | No disponible en el registro |
| 77096 | Ribavirina Aurovitas 200 mg cápsulas duras EFG | Cápsula dura | No disponible en el registro |
| 09527003 | Ribavirina Teva Pharma BV 200 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en el registro |
| 99107004 | Rebetol 40 mg/ml solución oral | Solución oral | No disponible en el registro |
| 73658 | Ribavirina Normon 200 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en el registro |

---

## Consideraciones de Seguridad

- **Diana farmacológica**: la base de datos de farmacología registra IMPDH1 e IMPDH2 como dianas humanas de la ribavirina. Son dianas del fármaco, no interacciones clínicas con otros medicamentos.
- **Riesgo relevante señalado en el análisis**: la anemia hemolítica es un efecto adverso conocido de la ribavirina y una preocupación potencial en pacientes con enfermedad hepática.

No hay datos de advertencias ni contraindicaciones del prospecto de la AEMPS. Consultar el prospecto para información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La puntuación TxGNN es muy alta (99.86%), pero ningún ensayo ni publicación estudia la ribavirina en VHB. La evidencia proviene del contexto de hepatitis C y coinfección, y el mecanismo no está establecido para un virus de ADN con replicación por transcripción inversa. Las otras nueve predicciones del modelo tienen aún menos respaldo: ocho son L5 y una es L4, con literatura solo sobre porfiria cutánea tardía en pacientes con VHC. Por eso tampoco justifican avanzar.

**Para avanzar se necesita:**
- Estudios preclínicos o clínicos que evalúen la ribavirina específicamente en monoinfección por VHB
- Datos del mecanismo de acción y de su vínculo con la replicación del VHB
- Ficha técnica de la AEMPS con advertencias y contraindicaciones
- Texto de indicaciones aprobadas de las autorizaciones españolas
- Comparación con los antivirales ya establecidos para el VHB
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


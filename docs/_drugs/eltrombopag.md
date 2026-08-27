---
layout: default
title: Eltrombopag
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 1
---

# Eltrombopag
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Eltrombopag: De Trombocitopenia a Infección por VIH

## Resumen en Una Frase

Eltrombopag es un agonista del receptor de trombopoyetina (TPO-RA), utilizado en la práctica clínica para el tratamiento de la trombocitopenia; actualmente no se encuentra comercializado en España según los registros consultados. El modelo TxGNN predice que podría ser efectivo para **Infección por VIH**, con **5 ensayos clínicos** y **10 publicaciones** que actualmente respaldan esta dirección, aunque la evidencia disponible es en su mayoría indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trombocitopenia (uso establecido como agonista TPO-RA; texto de indicación oficial no disponible en el registro consultado) |
| Nueva Indicación Predicha | Infección por VIH |
| Puntaje de Predicción TxGNN | 99.26% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción (MOA) oficial de eltrombopag (data gap). Según la información disponible en el paquete de evidencia, eltrombopag es un agonista del receptor de trombopoyetina (TPO-RA) cuyo mecanismo aprobado consiste en estimular la producción de plaquetas por los megacariocitos, sin relación mecanística directa conocida con la replicación del VIH o la infección de células huésped.

El único estudio con un vínculo mecanístico real hacia el VIH es un cribado in vitro de una biblioteca de fármacos aprobados por la FDA (PMID 32977702), que identificó a eltrombopag como posible modulador de la transcripción proviral de VIH-1. Sin embargo, la direccionalidad de este efecto no está clara: podría tratarse de un candidato para estrategias de tipo "shock and kill" (activación del provirus para su posterior eliminación), o simplemente de una activación del virus latente sin eliminación del mismo, con relevancia clínica incierta.

El resto de los ensayos de Fase 2/3 y la mayor parte de la literatura corresponden en realidad al uso de eltrombopag para tratar la trombocitopenia inmune (PTI) o la anemia aplásica que aparece como comorbilidad en pacientes con VIH o VHC, es decir, tratan una complicación hematológica y no la infección por VIH en sí misma. Esto sugiere que la puntuación elevada de TxGNN probablemente refleja una alta co-ocurrencia entre eltrombopag y la población de pacientes con VIH (uso fuera de indicación para PTI relacionada con VIH), más que un mecanismo antiviral demostrado — un caso típico de confusión indicación-comorbilidad.

---

## Evidencia de Ensayos Clínicos

*Nota: ninguno de los ensayos siguientes fue diseñado para evaluar eltrombopag como tratamiento de la infección por VIH; todos corresponden a estudios de trombocitopenia asociada a VHC o enfermedad hepática crónica.*

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00996216](https://clinicaltrials.gov/study/NCT00996216) | Fase 3 | Completado | 27 | Estudio rollover abierto sobre seguridad/tolerabilidad a largo plazo de eltrombopag en trombocitopenia asociada a VHC; no dirigido a la infección por VIH. |
| [NCT00529568](https://clinicaltrials.gov/study/NCT00529568) | Fase 3 | Completado | 759 | Ensayo aleatorizado controlado con placebo; eltrombopag para mantener el recuento plaquetario y permitir terapia antiviral en VHC (respuesta virológica sostenida). |
| [NCT00678587](https://clinicaltrials.gov/study/NCT00678587) | Fase 3 | Terminado | 292 | Estudio terminado; evaluaba la reducción de necesidad de transfusión de plaquetas en enfermedad hepática crónica ante procedimientos invasivos electivos. |
| [NCT00516321](https://clinicaltrials.gov/study/NCT00516321) | Fase 3 | Completado | 687 | Ensayo aleatorizado controlado con placebo, diseño análogo a NCT00529568 (con interferón alfa-2a); enfocado en VHC, no en VIH. |
| [NCT01636778](https://clinicaltrials.gov/study/NCT01636778) | Fase 2 | Completado | 45 | Estudio abierto no aleatorizado (código SB-497115-GR = eltrombopag) en trombocitopenia por VHC con cirrosis compensada. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19932434](https://pubmed.ncbi.nlm.nih.gov/19932434/) | 2009 | Revisión | Hematol Oncol Clin North Am | Causas infecciosas de trombocitopenia inmune crónica (VHC, VIH, H. pylori); tratar la infección primaria suele mejorar la trombocitopenia. |
| [19245929](https://pubmed.ncbi.nlm.nih.gov/19245929/) | 2009 | Revisión | Semin Hematol | Estrategias terapéuticas para trombocitopenias inmunes relacionadas con infecciones (hepatitis, VIH, etc.). |
| [24816314](https://pubmed.ncbi.nlm.nih.gov/24816314/) | 2014 | Revisión | Intern Med J | Agonistas del receptor de trombopoyetina en trombocitopenia inmune de menos de 6 meses de duración. |
| [22185370](https://pubmed.ncbi.nlm.nih.gov/22185370/) | 2012 | Cohorte | Platelets | Experiencia danesa con agonistas TPO-R en PTI refractaria, incluye pacientes con comorbilidades hematológicas. |
| [25504472](https://pubmed.ncbi.nlm.nih.gov/25504472/) | 2015 | Cohorte/Serie de casos | J Int Assoc Provid AIDS Care | Uso de agonistas del receptor de trombopoyetina (eltrombopag, romiplostim) en PTI refractaria asociada a VIH. |
| [32977702](https://pubmed.ncbi.nlm.nih.gov/32977702/) | 2020 | Cribado in vitro | Viruses | Cribado de fármacos aprobados por la FDA para identificar moduladores de la transcripción proviral de VIH-1; eltrombopag identificado como modulador potencial (direccionalidad no confirmada). |
| [28043314](https://pubmed.ncbi.nlm.nih.gov/28043314/) | 2016 | Reporte de caso | J Coll Physicians Surg Pak | Caso de hepatitis B con anemia megaloblástica y trombocitopenia periférica catastrófica (no relacionado con VIH). |
| [22992580](https://pubmed.ncbi.nlm.nih.gov/22992580/) | 2012 | Reporte de caso | AIDS | Uso exitoso de eltrombopag sin esplenectomía en trombocitopenia por reconstitución inmune asociada a VIH, refractaria. |
| [25333665](https://pubmed.ncbi.nlm.nih.gov/25333665/) | 2014 | Reporte de caso | AIDS | Tratamiento exitoso de anemia aplásica asociada a VIH con eltrombopag; posible rol inmunomodulador. |
| [24128106](https://pubmed.ncbi.nlm.nih.gov/24128106/) | 2013 | Reporte de caso | Farm Hosp | Dos casos de eltrombopag para trombocitopenia en hepatitis C crónica (no VIH). |

---

## Información de Mercado en España

Eltrombopag no está actualmente comercializado en España (0 autorizaciones registradas en la fuente consultada).

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia disponible es en su mayoría indirecta: los ensayos clínicos y la mayoría de la literatura tratan el uso de eltrombopag para la trombocitopenia inmune o la anemia aplásica que ocurre como comorbilidad en pacientes con VIH, no la infección por VIH en sí. El único vínculo mecanístico hacia el virus proviene de un único estudio de cribado in vitro con direccionalidad no confirmada, insuficiente para sostener una hipótesis terapéutica antiviral.

**Para avanzar se necesita:**
- Confirmación mecanística in vivo del efecto de eltrombopag sobre la transcripción proviral de VIH-1 (activación vs. supresión)
- Ensayos clínicos diseñados específicamente para evaluar eltrombopag como terapia anti-VIH, y no solo para la trombocitopenia comórbida
- Datos de advertencias y contraindicaciones de TFDA/prospecto (actualmente bloqueante para la evaluación de seguridad S1)
- Confirmación del mecanismo de acción (MOA) oficial del fármaco
- Evaluación de la disponibilidad regulatoria en España, dado que el fármaco no está actualmente comercializado
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


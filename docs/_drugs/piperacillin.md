---
layout: default
title: Piperacillin
parent: Solo predicción del modelo (L5)
nav_order: 642
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-31
description: "Piperacillin: nueva indicación predicha, Artritis reumatoide (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "piperacillin"
predicted_indications: ["rheumatoid arthritis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "sclerosing cholangitis", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "diabetic nephropathy", "WHIM syndrome"]
---

# Piperacillin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

## Piperacilina: De Infecciones Bacterianas a Artritis Reumatoide
{: .text-alpha }

## Resumen en Una Frase

Piperacilina es un antibiótico betalactámico (penicilina de espectro ampliado), comercializado en España en combinación con tazobactam. Las autorizaciones compiladas no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **artritis reumatoide**, pero **no existen ensayos clínicos** y las **14 publicaciones** recuperadas son en su mayoría reportes de caso en los que la artritis reumatoide aparece solo como comorbilidad, de modo que la predicción no cuenta con respaldo real.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Artritis reumatoide |
| Puntaje de Predicción TxGNN | 0.9994 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 8) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, piperacilina es un antibiótico betalactámico que inhibe la síntesis de la pared celular bacteriana al unirse a las proteínas de unión a penicilina, y se comercializa en combinación con tazobactam, un inhibidor de betalactamasas.

El análisis mecanístico no encuentra un vínculo creíble con la artritis reumatoide. Piperacilina no tiene actividad inmunomoduladora conocida que sea relevante para la patogenia de esta enfermedad. El puntaje elevado de TxGNN (0.9994) parece ser un artefacto del modelo TxGNN (aprendizaje profundo) y no refleja una relación terapéutica real.

La literatura recuperada menciona la artritis reumatoide únicamente como enfermedad de base en pacientes que recibieron antibióticos tipo piperacilina por infecciones, no como diana de tratamiento. Por ello, la predicción debe considerarse una hipótesis sin respaldo mecanístico ni clínico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Los 14 artículos recuperados son en su mayoría reportes de caso o estudios sin relación terapéutica con la indicación predicha. Se listan los 10 más relevantes (ninguno es un ECA).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [33987340](https://pubmed.ncbi.nlm.nih.gov/33987340/) | 2021 | Cohorte | Annals of Translational Medicine | Prevalencia y características clínicas de la lesión hepática inducida por antibióticos |
| [41257433](https://pubmed.ncbi.nlm.nih.gov/41257433/) | 2026 | Cohorte (modelo predictivo) | British Journal of Clinical Pharmacology | Modelo predictivo de eosinofilia en pacientes tratados con ampicilina/sulbactam o piperacilina/tazobactam |
| [38343452](https://pubmed.ncbi.nlm.nih.gov/38343452/) | 2024 | Reporte de caso | Proceedings (Baylor Univ. Med. Center) | Toxicidad por metotrexato a dosis bajas con pancitopenia en paciente con AR; rescate con leucovorina |
| [34178513](https://pubmed.ncbi.nlm.nih.gov/34178513/) | 2021 | Reporte de caso | Cureus | Pancitopenia por metotrexato a dosis bajas en AR |
| [37599303](https://pubmed.ncbi.nlm.nih.gov/37599303/) | 2023 | Reporte de caso | Orthopadie | Infección protésica de rodilla por *Haemophilus influenzae* en paciente con AR; piperacilina/tazobactam usado para neumonía |
| [22605835](https://pubmed.ncbi.nlm.nih.gov/22605835/) | 2012 | Reporte de caso | BMJ Case Reports | Pericarditis purulenta en paciente con AR tratada con etanercept; piperacilina/tazobactam empírico |
| [41268563](https://pubmed.ncbi.nlm.nih.gov/41268563/) | 2025 | Reporte de caso | Frontiers in Immunology | Erisipela bullosa atípica por *E. coli* en paciente inmunosuprimida con AR |
| [36945293](https://pubmed.ncbi.nlm.nih.gov/36945293/) | 2023 | Reporte de caso | Cureus | Derrame pleural recurrente en paciente con AR en remisión durante nueve años |
| [40119266](https://pubmed.ncbi.nlm.nih.gov/40119266/) | 2025 | Reporte de caso/Revisión | BMC Infectious Diseases | Shock séptico por *Edwardsiella tarda* resistente a fármacos |
| [1921823](https://pubmed.ncbi.nlm.nih.gov/1921823/) | 1991 | Reporte de caso | Medical Journal of Australia | Pancitopenia tras sobredosis accidental de metotrexato en AR |

Ninguno de estos trabajos evalúa piperacilina como tratamiento de la artritis reumatoide.

---

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de principio activo único, ninguna cancelada). El texto de la indicación aprobada no figura en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 67902 | Piperacilina/Tazobactam Accord 2/0,25 g EFG | Polvo y disolvente para solución para perfusión | No disponible |
| 67903 | Piperacilina/Tazobactam Accord 4/0,5 g EFG | Polvo para solución para perfusión | No disponible |
| 71824 | Piperacilina/Tazobactam Aurovitas 4 g/0,5 g EFG | Polvo para solución para perfusión | No disponible |
| 86582 | Piperacilina/Tazobactam Stada 4 g/0,5 g EFG | Polvo para solución para perfusión | No disponible |
| 78656 | Piperacilina/Tazobactam Normon 2 g/0,25 g EFG | Polvo para solución inyectable y para perfusión | No disponible |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 81 interacciones. Las principales según el nivel de gravedad:
  - **Mayor**: vancomicina.
  - **Moderada**: doxiciclina, tetraciclina, minociclina, kanamicina, estreptomicina y ácido picosulfúrico.
  - **Menor**: claritromicina.
  - Otras interacciones (pantoprazol, morfina, sucralfato, prednisona, simvastatina, nistatina, cloruro de potasio, prednisolona, ranitidina, rabeprazol, omeprazol, lansoprazol) figuran sin nivel de gravedad definido.
- **Consideraciones adicionales derivadas del análisis**: piperacilina se elimina por vía renal y requiere ajuste de dosis en insuficiencia renal. Los betalactámicos pueden causar nefritis intersticial y lesión hepática colestásica. La literatura recuperada también describe eosinofilia asociada a piperacilina/tazobactam.

Para advertencias y contraindicaciones específicas, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (nivel L5): no hay ensayos clínicos, la literatura no evalúa a piperacilina como tratamiento de la artritis reumatoide y no existe un vínculo mecanístico creíble. El puntaje alto de TxGNN parece un artefacto del modelo TxGNN (aprendizaje profundo). Las demás indicaciones predichas (síndromes genéticos raros, colangitis esclerosante, osteoartritis, nefropatía diabética, síndrome WHIM) tampoco tienen respaldo y también se mantienen en Hold.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (indicaciones, advertencias y contraindicaciones), actualmente ausente.
- Completar los datos del mecanismo de acción desde DrugBank.
- Disponer de evidencia preclínica que justifique un efecto inmunomodulador o antiinflamatorio relevante en la artritis reumatoide.
- Valorar la plausibilidad biológica antes de cualquier estudio clínico; no se recomienda avanzar con los datos actuales.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Cefoxitin
parent: Solo predicción del modelo (L5)
nav_order: 156
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cefoxitin: nueva indicación predicha, Infección del tracto urinario (nivel de evidencia L5). Indicación original: Infecciones bacterianas (neumonía bacteriana, peritonitis…"
monitor_inn: "cefoxitin"
predicted_indications: ["infectious otitis media", "urinary tract infection (disease)", "chronic otitis media", "suppurative otitis media", "middle ear disease", "Ureaplasma urethritis", "toxocariasis", "otosalpingitis", "non-suppurative otitis media"]
---

# Cefoxitin
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

# Cefoxitina: De Infecciones Bacterianas a Infección del Tracto Urinario

## Resumen en Una Frase

Cefoxitina es una cefamicina de segunda generación, utilizada originalmente para tratar infecciones bacterianas como neumonía, peritonitis, infecciones estafilocócicas y estreptocócicas, y gonorrea.
El modelo TxGNN predice que podría ser efectiva para la **infección del tracto urinario**, con **1 ensayo clínico** (terminado prematuramente con solo 6 participantes) y **20 publicaciones** de calidad heterogénea que actualmente respaldan esta dirección.

> Nota: la primera predicción del modelo por puntaje es la otitis media infecciosa (99,30 %). Sin embargo, solo cuenta con una revisión general sobre SARM, sin datos específicos de cefoxitina. Por ello, este informe se centra en la infección del tracto urinario (rank 2), que es la candidata con mayor respaldo de evidencia (nivel L3). Las demás predicciones se resumen más adelante.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones bacterianas (neumonía bacteriana, peritonitis, infecciones por *S. aureus*, estreptococos y *E. coli*, gonorrea; según el grafo de conocimiento, ya que los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Infección del tracto urinario (candidata principal por evidencia; la de mayor puntaje es la otitis media infecciosa) |
| Puntaje de Predicción TxGNN | 99,26 % (otitis media infecciosa, la de mayor puntaje: 99,30 %) |
| Nivel de Evidencia | L3 (L5 para otitis media infecciosa) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold (otitis media infecciosa); Proceed with Guardrails limitado a la línea de investigación en ITU por BLEE |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la cefoxitina es una cefamicina que inhibe la síntesis de la pared celular bacteriana y es estable frente a muchas betalactamasas. Su eficacia en infecciones bacterianas diversas está establecida, y mecanísticamente podría ser aplicable a infecciones urinarias.

La relación con la indicación original es directa: *E. coli* ya figura entre las infecciones originales del fármaco, y es el principal patógeno urinario. Su estabilidad frente a la hidrólisis por BLEE (betalactamasas de espectro extendido) la hace una posible alternativa que ahorre carbapenémicos en infecciones por *E. coli* productor de BLEE. Un modelo murino (PMID 22214774) respalda esta idea, y estudios clínicos antiguos de 1978-1979 informaron eficacia en ITU complicada.

Conviene matizar: no hay datos clínicos modernos concluyentes. El único ensayo contemporáneo se terminó con 6 pacientes y no permite sacar conclusiones de eficacia.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02474706](https://clinicaltrials.gov/study/NCT02474706) | Fase 4 | Terminado | 6 | Cefoxitina frente a imipenem/cilastatina en ITU por *E. coli* productor de BLEE (no inferioridad). Terminado con solo 6 participantes; sin capacidad para respaldar conclusiones de eficacia |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22214774](https://pubmed.ncbi.nlm.nih.gov/22214774/) | 2012 | Modelo animal (murino) | Antimicrob Agents Chemother | Cefoxitina como alternativa a carbapenémicos en ITU por *E. coli* con BLEE CTX-M-15 |
| [357399](https://pubmed.ncbi.nlm.nih.gov/357399/) | 1978 | Estudio clínico | J Antimicrob Chemother | Cefoxitina sódica en infección urinaria complicada |
| [400934](https://pubmed.ncbi.nlm.nih.gov/400934/) | 1979 | Estudio clínico | Rev Infect Dis | Cefoxitina intramuscular en 102 pacientes con infecciones leves o moderadas; curación o mejoría en 45 de 47 con infecciones de piel y partes blandas |
| [400937](https://pubmed.ncbi.nlm.nih.gov/400937/) | 1979 | Revisión | Rev Infect Dis | Resumen de estudios en EE. UU.: 69 % curados y 92 % curados o mejorados en 657 pacientes evaluables |
| [40165096](https://pubmed.ncbi.nlm.nih.gov/40165096/) | 2025 | Estudio multicéntrico de práctica real | BMC Infect Dis | Cefepima frente a carbapenémicos en ITU complicada por organismos ESCPM no sensibles a cefoxitina |
| [37284390](https://pubmed.ncbi.nlm.nih.gov/37284390/) | 2023 | Cohorte observacional | Cureus | ITU multirresistente en pacientes con enfermedad renal crónica |
| [15009360](https://pubmed.ncbi.nlm.nih.gov/15009360/) | 2004 | Revisión | Int J Urol | Infecciones urinarias y genitourinarias supurativas por anaerobios |
| [7004691](https://pubmed.ncbi.nlm.nih.gov/7004691/) | 1980 | Revisión | Clin Obstet Gynecol | Infecciones puerperales |

La mayoría del resto de publicaciones recuperadas son estudios epidemiológicos o de resistencia, sin datos terapéuticos de cefoxitina.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 68149 | Cefoxitina IPS 1 g | Polvo y disolvente para solución inyectable | No disponible en los datos |
| 84251 | Cefoxitina LDP Laboratorios Torlan 1 g | Polvo para solución inyectable y para perfusión | No disponible en los datos |
| 84252 | Cefoxitina LDP Laboratorios Torlan 2 g | Polvo para solución inyectable y para perfusión | No disponible en los datos |
| 63814 | Cefoxitina Normon 1 g | Polvo y disolvente para solución inyectable y para perfusión | No disponible en los datos |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): enfermedad renal, piouréter, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal y colitis.
- **Interacciones farmacológicas** (35 registradas):
  - Moderadas: aminoglucósidos (kanamicina, neomicina, estreptomicina), ácido picosulfúrico y dicumarol.
  - Leve: heparina.
  - Otras interacciones con nivel no clasificado: vancomicina, metronidazol, claritromicina, omeprazol, lansoprazol, morfina, simvastatina, entre otros.

Consultar el prospecto para advertencias y contraindicaciones oficiales.

## Otras Predicciones del Modelo (Resumen)

| Indicación | Puntaje | Nivel | Valoración |
|------|------|------|------|
| Otitis media infecciosa | 99,30 % | L5 | Solo una revisión general de SARM; cefoxitina se usa sobre todo como marcador fenotípico de SARM, no como tratamiento |
| Otitis media crónica / supurativa | 99,12 % / 99,11 % | L4 | Solo estudios de microbiología y sensibilidad; sin datos de resultados terapéuticos |
| Enfermedad del oído medio | 99,11 % | L4 | Un estudio japonés de 1982 en 11 pacientes con colesteatoma (72,7 % de curación); evidencia antigua e indirecta |
| Uretritis gonocócica | 99,09 % | L4 | Probablemente refleja una indicación ya existente (gonorrea); las guías actuales prefieren ceftriaxona |
| Uretritis por *Ureaplasma* | 99,09 % | L5 | Biológicamente no sustentada: *Ureaplasma* carece de pared celular |
| Toxocariasis | 99,09 % | L5 | Probable artefacto del grafo; sin mecanismo antiparasitario plausible |
| Otosalpingitis | 99,08 % | L5 | Sin evidencia |
| Otitis media no supurativa | 99,07 % | L5 | Racional débil; frecuentemente no bacteriana o autolimitada |

## Conclusión y Próximos Pasos

**Decisión: Hold** para la indicación de mayor puntaje (otitis media infecciosa); **Proceed with Guardrails** únicamente como línea de investigación en infección urinaria por *E. coli* productor de BLEE.

**Justificación:**
La evidencia para ITU es de nivel L3: un modelo animal favorable y estudios clínicos antiguos, pero el único ensayo moderno se terminó con 6 pacientes. El resto de predicciones carece de datos terapéuticos o no tiene respaldo biológico.

**Para avanzar se necesita:**
- Un ensayo clínico bien dimensionado frente a carbapenémicos en ITU por BLEE, con datos de sensibilidad local en España.
- Datos del mecanismo de acción y del prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas), que faltan en los datos compilados.
- Revisión de las interacciones y de las contraindicaciones señaladas (función renal, colitis).
- Consideración del papel de la cefoxitina en el contexto de la estrategia de uso de antibióticos y del riesgo de resistencia.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


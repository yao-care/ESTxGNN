---
layout: default
title: Amiodarone
parent: Solo predicción del modelo (L5)
nav_order: 51
evidence_level: L5
indication_count: 10
---

# Amiodarone
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

# Amiodarona: De Fibrilación Ventricular a Taquicardia Ventricular Catecolaminérgica Polimórfica

*Nota: la predicción de mayor puntaje del modelo (taquicardia ventricular catecolaminérgica polimórfica) tiene poco respaldo y, según los datos, la amiodarona se considera generalmente ineficaz en ella. Por ello, este informe también analiza la indicación con mejor respaldo clínico entre las predichas: la taquicardia ventricular.*

## Resumen en Una Frase

La amiodarona es un antiarrítmico multicanal utilizado originalmente para tratar la fibrilación ventricular.
El modelo TxGNN predice como primera opción la **taquicardia ventricular catecolaminérgica polimórfica (CPVT)**, con **0 ensayos clínicos** y **9 publicaciones** (casos clínicos, cohortes descriptivas y revisiones). La predicción con mayor respaldo es **taquicardia ventricular**, con **18 ensayos clínicos** y **20 publicaciones**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Fibrilación ventricular (el texto de indicación de las autorizaciones españolas está vacío; se toma de las indicaciones del grafo de conocimiento) |
| Nueva Indicación Predicha | Taquicardia ventricular polimórfica catecolaminérgica (CPVT) |
| Puntaje de Predicción TxGNN | 99,78 % |
| Nivel de Evidencia | L4 (CPVT); como referencia, L1 para taquicardia ventricular |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold para CPVT (pregunta de investigación); Proceed with Guardrails para taquicardia ventricular |

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la amiodarona es un antiarrítmico de clase III con efectos adicionales sobre canales de sodio y calcio y bloqueo betaadrenérgico. Los datos farmacológicos disponibles muestran interacción con el canal de sodio Nav1.5, el canal de potasio Kv1.7 y el receptor muscarínico M5.

**CPVT:** esta enfermedad se debe a una fuga de calcio por mutaciones en RYR2 o CASQ2 y a postdespolarizaciones tardías. Los efectos betabloqueante y de canales iónicos de la amiodarona podrían atenuar las arritmias desencadenadas por catecolaminas, pero no actúa sobre la alteración del manejo del calcio. Los tratamientos respaldados por las guías son betabloqueantes, flecainida y denervación simpática; la amiodarona se considera generalmente ineficaz. Por tanto, el alto puntaje del modelo no se corresponde con un respaldo clínico sólido.

**Taquicardia ventricular:** es una arritmia ventricular muy cercana a la indicación original. La supresión de arritmias ventriculares por reentrada es mecanísticamente continua con el uso en fibrilación ventricular, por lo que es más un uso establecido o adyacente a la indicación que un reposicionamiento novedoso.

## Evidencia de Ensayos Clínicos

Para CPVT: actualmente no hay ensayos clínicos relacionados registrados.

Como referencia, ensayos para taquicardia ventricular (los más relevantes):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00000531](https://clinicaltrials.gov/study/NCT00000531) | Fase 3 | Completado | No disponible | AVID: antiarrítmicos (principalmente amiodarona) frente a desfibriladores implantables en pacientes con arritmias ventriculares potencialmente mortales |
| [NCT01401647](https://clinicaltrials.gov/study/NCT01401647) | Fase 3 | Completado | 3024 | ALPS: amiodarona, lidocaína o placebo en parada cardiaca extrahospitalaria por FV/TV |
| [NCT00383799](https://clinicaltrials.gov/study/NCT00383799) | Fase 4 | Terminado | 302 | PROCAMIO: amiodarona IV frente a procainamida IV en taquicardia de QRS ancho bien tolerada |
| [NCT00257959](https://clinicaltrials.gov/study/NCT00257959) | Fase 4 | Completado | 400 | OPTIC: amiodarona + betabloqueante frente a sotalol o betabloqueante solo para prevenir descargas del DAI |
| [NCT03299517](https://clinicaltrials.gov/study/NCT03299517) | Fase 4 | Desconocido | 80 | Amiodarona frente a lidocaína en TV estable en urgencias |
| [NCT02830360](https://clinicaltrials.gov/study/NCT02830360) | Fase 4 | Completado | 416 | Ablación con catéter frente a tratamiento antiarrítmico en TV monomórfica tras infarto |
| [NCT03734562](https://clinicaltrials.gov/study/NCT03734562) | NA | Completado | 180 | Ablación de sustrato frente a antiarrítmicos en TV isquémica con descargas del DAI |
| [NCT01722942](https://clinicaltrials.gov/study/NCT01722942) | NA | Desconocido | 1100 | CHAGASICS: amiodarona frente a DAI en cardiomiopatía chagásica |
| [NCT03855826](https://clinicaltrials.gov/study/NCT03855826) | Fase 4 | Desconocido | 756 | Nifekalant frente a amiodarona en TV/FV (relevancia indirecta) |
| [NCT01097330](https://clinicaltrials.gov/study/NCT01097330) | Fase 3 | Terminado | 12 | Ablación frente a amiodarona en pacientes con DAI y TV (reclutamiento muy bajo) |

## Evidencia de Literatura

Para CPVT (la más relevante):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Revisión sistemática | Life (Basel) | Características clínicas, genéticas y resultados arrítmicos de pacientes con CPVT en China |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Cohorte retrospectiva | Rev Cardiovasc Med | Características, base genética y costes sanitarios de CPVT |
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Revisión | Expert Opin Pharmacother | Avances en el tratamiento farmacológico de arritmias ventriculares |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Caso clínico | PACE | La flecainida suprime la tormenta inducida por el desfibrilador en CPVT |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Caso clínico | Front Cardiovasc Med | Resolución de CPVT con denervación simpática cardiaca derecha tras la izquierda |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Caso clínico | Medicine | Diagnóstico tardío de CPVT con mutación RYR2 en un niño |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Caso clínico | Turk Pediatri Arsivi | CPVT como causa rara de parada cardiaca súbita |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Caso clínico | Anesth Analg | Neonato con síndrome de QT largo y arritmias refractarias tratado con lidocaína, esmolol y amiodarona |

Ninguna de estas publicaciones demuestra eficacia de la amiodarona en CPVT; el tratamiento descrito se basa en betabloqueantes, flecainida y denervación simpática.

Como referencia, para taquicardia ventricular:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [27354046](https://pubmed.ncbi.nlm.nih.gov/27354046/) | 2017 | ECA | Eur Heart J | PROCAMIO: procainamida IV frente a amiodarona IV en taquicardia de QRS ancho tolerada |
| [20730062](https://pubmed.ncbi.nlm.nih.gov/20730062/) | 2010 | Revisión | Vasc Health Risk Manag | La amiodarona como terapia líder para terminar y prevenir TV/FV |
| [36878200](https://pubmed.ncbi.nlm.nih.gov/36878200/) | 2023 | Revisión | Cardiology | Farmacoterapia en arritmias ventriculares |
| [28900864](https://pubmed.ncbi.nlm.nih.gov/28900864/) | 2017 | Revisión | Curr Cardiol Rep | TV con descargas del DAI: cuándo medicar y cuándo ablacionar |
| [30084131](https://pubmed.ncbi.nlm.nih.gov/30084131/) | 2018 | Cohorte | Emerg Med Australas | Seguridad y eficacia de la amiodarona prehospitalaria en TV estable |
| [9137212](https://pubmed.ncbi.nlm.nih.gov/9137212/) | 1997 | Revisión | J Am Coll Cardiol | Amiodarona intravenosa en arritmias ventriculares malignas y resistentes |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 81291 | Amiodarona Aurovitas 200 mg comprimidos EFG | Comprimido | No disponible en los datos compilados |
| 54723 | Trangorex 150 mg / 3 ml solución inyectable | Solución inyectable | No disponible en los datos compilados |
| 85739 | Amiodarona Accord 30 mg/ml concentrado para solución inyectable y para perfusión | Solución inyectable y para perfusión en jeringa precargada | No disponible en los datos compilados |
| 48048 | Trangorex 200 mg comprimidos | Comprimido | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (grafo de conocimiento, no texto del prospecto):** síndrome de QT largo (incluido el familiar) y torsades de pointes; bloqueo auriculoventricular y síndrome del seno enfermo; enfermedad hepática, lesión hepática inducida por fármacos y enfermedad de la vesícula biliar; hipotiroidismo, mixedema, hipotiroidismo congénito, hipertiroidismo, enfermedad de Graves y tirotoxicosis; enfermedad pulmonar intersticial, neumonía eosinofílica, eosinofilia pulmonar, alveolitis alérgica extrínseca, neumonitis por hipersensibilidad y pulmón del granjero; neuritis óptica y enfermedades del nervio óptico y de la vía visual; neuropatía periférica y enfermedad del sistema nervioso periférico; déficit de potasio; depósitos corneales.
- **Interacciones farmacológicas:** los datos de farmacología muestran interacción con el canal de sodio Nav1.5, el canal de potasio Kv1.7 y el receptor muscarínico M5. La literatura describe además una interacción con ciclosporina y riesgo de rabdomiólisis al combinarse con atorvastatina y fluconazol.
- **Para uso pediátrico:** se requiere monitorización estrecha (carga de yodo y efectos tiroideos, bradicardia e hipotensión con uso intravenoso, riesgo proarrítmico).

## Conclusión y Próximos Pasos

**Decisión: Hold (CPVT, indicación de mayor puntaje); Proceed with Guardrails (taquicardia ventricular)**

**Justificación:**
- Para CPVT no hay ensayos y la evidencia se limita a casos clínicos, cohortes descriptivas y revisiones; las guías respaldan betabloqueantes, flecainida y denervación simpática, y la amiodarona se considera generalmente ineficaz, por lo que es solo una pregunta de investigación.
- La taquicardia ventricular cuenta con ensayos de Fase 3 completados (AVID, ALPS) y un ECA publicado (PROCAMIO), pero es un uso establecido o adyacente a la indicación original, no un reposicionamiento novedoso.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y revisión de advertencias y contraindicaciones del prospecto de la AEMPS, actualmente no disponibles.
- Para CPVT: estudios mecanísticos o preclínicos que justifiquen cualquier beneficio frente a las terapias de referencia.
- Para taquicardia ventricular: plan de monitorización de toxicidad tiroidea, pulmonar y hepática, y control de interacciones (por ejemplo, ciclosporina).
- Confirmar el texto de indicación aprobado en las autorizaciones españolas, que figura vacío.
- Predicciones de nivel L5 (bloqueo de rama obsoleto, artritis reumatoide, síndrome de braquidactilia-sindactilia, déficit de cofactor II de heparina, tricotilomanía, síndrome de microftalmia colobomatosa-displasia rizomélica y gota): sin respaldo mecanístico creíble; la artritis reumatoide y la gota muestran principalmente señales de seguridad, y se recomienda Hold.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


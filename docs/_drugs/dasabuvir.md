---
layout: default
title: Dasabuvir
parent: Solo predicción del modelo (L5)
nav_order: 159
evidence_level: L5
indication_count: 5
---

# Dasabuvir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Dasabuvir: De Hepatitis C Crónica a Infección por Virus de la Hepatitis B

## Resumen en Una Frase

Dasabuvir es un inhibidor no nucleosídico de la polimerasa NS5B del virus de la hepatitis C (VHC), utilizado en el régimen de tres antivirales de acción directa para la hepatitis C crónica de genotipo 1.
El modelo TxGNN predice que podría ser efectivo para la **infección por el virus de la hepatitis B**, pero de los **14 ensayos clínicos** y las **18 publicaciones** asociados, ninguno demuestra eficacia anti-VHB.
Solo un ensayo incluye pacientes con VHB (coinfección VHC/VHB, 23 pacientes) y evalúa la seguridad, concretamente el riesgo de reactivación del VHB.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hepatitis C crónica (genotipo 1). Esta indicación se deduce de los ensayos y del mecanismo, porque el texto de la autorización española no la recoge |
| Nueva Indicación Predicha | Infección por el virus de la hepatitis B |
| Puntaje de Predicción TxGNN | 99.37% |
| Nivel de Evidencia | L5 (el Evidence Pack indica L4, pero no hay estudios preclínicos ni de mecanismo sobre VHB) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Dasabuvir es un inhibidor no nucleosídico de la ARN polimerasa dependiente de ARN NS5B del VHC. Se une a un sitio alostérico del dominio *palm*, específico de los Flaviviridae. En la práctica se administra junto con ombitasvir, paritaprevir y ritonavir. En el Evidence Pack no figura el mecanismo de acción en DrugBank.

**La predicción es débil desde el punto de vista mecanístico.** El VHB es un virus de ADN que se replica mediante una transcriptasa inversa. No comparte diana con la NS5B, por lo que no hay un mecanismo antiviral directo plausible. La puntuación alta de TxGNN (0.994) probablemente refleja la proximidad en la red de conocimiento a través de nodos comunes de "hepatitis viral" y de la coinfección VHC/VHB, y no una superposición real de dianas.

La señal clínica de los datos se refiere a la curación del VHC en pacientes coinfectados y al riesgo de reactivación del VHB durante el tratamiento con antivirales de acción directa. No se refiere al tratamiento del VHB.

---

## Evidencia de Ensayos Clínicos

Ningún ensayo evalúa la eficacia de dasabuvir contra el VHB. Se muestran los 10 más relevantes.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Fase 2/3 | Completado | 23 | Antivirales de acción directa en coinfección crónica VHC/VHB. Es el único ensayo con pacientes VHB positivos. Estudia la reactivación del VHB durante el tratamiento anti-VHC. Aporta seguridad, no eficacia anti-VHB |
| [NCT01939197](https://clinicaltrials.gov/study/NCT01939197) | Fase 2/3 | Completado | 318 | TURQUOISE-I: régimen con dasabuvir en coinfección VHC/VIH-1. Coincide solo por términos de "hepatitis"; no evalúa VHB |
| [NCT02219477](https://clinicaltrials.gov/study/NCT02219477) | Fase 3 | Completado | 36 | TURQUOISE-CPB: régimen con dasabuvir más ribavirina en cirrosis descompensada por VHC. Sin población ni criterio de valoración de VHB |
| [NCT01854697](https://clinicaltrials.gov/study/NCT01854697) | Fase 3 | Completado | 311 | MALACHITE-I: régimen de antivirales de acción directa frente a telaprevir más peginterferón y ribavirina en VHC genotipo 1 sin tratamiento previo |
| [NCT01464827](https://clinicaltrials.gov/study/NCT01464827) | Fase 2 | Completado | 580 | Actividad antiviral, seguridad y farmacocinética de ABT-450/r con ABT-267 y/o ABT-333 (dasabuvir) en VHC genotipo 1. No es relevante para VHB |
| [NCT01782495](https://clinicaltrials.gov/study/NCT01782495) | Fase 2 | Completado | 129 | CORAL-I: régimen con dasabuvir en receptores de trasplante hepático o renal con VHC |
| [NCT02194998](https://clinicaltrials.gov/study/NCT02194998) | Fase 2 | Terminado | 46 | C_ASCENT: tratamiento sin interferón para VHC genotipo 1 en coinfectados por VIH-1 |
| [NCT02460133](https://clinicaltrials.gov/study/NCT02460133) | Fase 4 | Activo, sin reclutamiento | 44 | Tasas de reinfección por VHC en población encarcelada tras la curación. No es relevante para VHB |
| [NCT02851069](https://clinicaltrials.gov/study/NCT02851069) | N/A | Completado | 66 | Estudio observacional en Colombia sobre la efectividad en la práctica real del régimen con o sin dasabuvir en VHC |
| [NCT03423641](https://clinicaltrials.gov/study/NCT03423641) | N/A | Completado | 33 808 | Comparación de eventos adversos entre pacientes con VHC tratados con antivirales de acción directa y pacientes sin tratar |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29397016](https://pubmed.ncbi.nlm.nih.gov/29397016/) | 2018 | Cohorte | J Viral Hepat | Riesgo de reactivación del VHB en pacientes coinfectados VHB/VHC con cirrosis compensada tratados con ombitasvir, paritaprevir/r, dasabuvir y ribavirina. Datos de una cohorte nacional de 2070 pacientes. Es el estudio más cercano al tema, pero trata de seguridad y no de eficacia anti-VHB |
| [28416221](https://pubmed.ncbi.nlm.nih.gov/28416221/) | 2017 | Ensayo fase 3b de un solo brazo | Lancet Gastroenterol Hepatol | GARNET: 8 semanas de tratamiento con el régimen que incluye dasabuvir, sin ribavirina, en VHC genotipo 1b sin cirrosis y sin tratamiento previo |
| [28762541](https://pubmed.ncbi.nlm.nih.gov/28762541/) | 2018 | Estudio de práctica real | J Gastroenterol Hepatol | Efectividad y seguridad del régimen con o sin ribavirina en pacientes taiwaneses con VHC genotipo 1b |
| [28903508](https://pubmed.ncbi.nlm.nih.gov/28903508/) | 2017 | Cohorte | Clin Infect Dis | Efecto sobre la supervivencia de los regímenes PrOD y ledipasvir/sofosbuvir frente a personas con VHC sin tratar (ERCHIVES) |
| [25529080](https://pubmed.ncbi.nlm.nih.gov/25529080/) | 2015 | Revisión | Liver Int | Revisión sobre la erradicación del VHC y la curación del VHB. Es de contexto general y no evalúa dasabuvir |
| [36515288](https://pubmed.ncbi.nlm.nih.gov/36515288/) | 2022 | Cohorte | Vopr Virusol | Prevalencia y características moleculares de los virus de las hepatitis B, C y D en personas con VIH en la región de Novosibirsk |
| [41570233](https://pubmed.ncbi.nlm.nih.gov/41570233/) | 2025 | Estudio de prevalencia | Vopr Virusol | Prevalencia de marcadores de VIH, VHB y VHC en pacientes de odontología y caracterización molecular. No trata sobre dasabuvir |
| [31580556](https://pubmed.ncbi.nlm.nih.gov/31580556/) | 2019 | Encuesta | Cent Eur J Public Health | Situación de la atención de las hepatitis virales en 16 países de Europa Central y del Este |
| [26043288](https://pubmed.ncbi.nlm.nih.gov/26043288/) | 2015 | Revisión | Rev Med Virol | Desarrollo acelerado de antivirales frente al VHC. Diana común: NS3/4A, NS5A y NS5B |
| [26139639](https://pubmed.ncbi.nlm.nih.gov/26139639/) | 2015 | Revisión | Ann Pharmacother | Consideraciones de tratamiento en poblaciones especiales con VHC genotipo 1 |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 114983001 | EXVIERA 250 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA (Abbvie Deutschland Gmbh & Co. Kg) | Comprimido recubierto con película | No consta en el registro consultado |

---

## Consideraciones de Seguridad

- **Riesgo de reactivación del VHB**: la literatura y los ensayos analizan la reactivación del VHB en pacientes coinfectados VHB/VHC tratados con antivirales de acción directa (estudios [29397016](https://pubmed.ncbi.nlm.nih.gov/29397016/) y [NCT02555943](https://clinicaltrials.gov/study/NCT02555943)). Es un aspecto de seguridad, no un beneficio terapéutico.

Consultar el prospecto para información de seguridad adicional (advertencias, contraindicaciones e interacciones).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- La puntuación de TxGNN es muy alta, pero no hay mecanismo plausible: dasabuvir actúa sobre la polimerasa NS5B del VHC y el VHB es un virus de ADN con transcriptasa inversa.
- Ningún ensayo ni publicación muestra actividad anti-VHB. La evidencia disponible trata de la curación del VHC en coinfectados y de la reactivación del VHB, lo que apunta a un problema de seguridad y no a una nueva indicación.

**Para avanzar se necesita:**
- Ensayos *in vitro* de actividad de dasabuvir frente al VHB. Sin una señal antiviral básica no está justificado avanzar.
- Ficha técnica de la AEMPS (indicación, advertencias y contraindicaciones) para completar el perfil de seguridad.
- Datos del mecanismo de acción en DrugBank.
- Si se mantiene el interés clínico, plan de vigilancia de la reactivación del VHB en pacientes coinfectados que reciban este régimen.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


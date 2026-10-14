---
layout: default
title: Glecaprevir
parent: Evidencia alta (L1-L2)
nav_order: 378
evidence_level: L1
indication_count: 10
---

# Glecaprevir
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
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

# Glecaprevir: De Infección por el Virus de la Hepatitis C a Infección por VIH (Coinfección VIH/VHC)

## Resumen en Una Frase

Glecaprevir es un inhibidor de la proteasa NS3/4A del virus de la hepatitis C (VHC), utilizado originalmente para el tratamiento de la infección crónica por VHC, en combinación con pibrentasvir (Maviret).
El modelo TxGNN predice que podría ser efectivo para **infección por VIH**, con **7 ensayos clínicos** y **20 publicaciones** asociados a esta predicción.
Los datos corresponden en realidad a la curación del VHC en pacientes coinfectados con VIH, no al tratamiento del VIH en sí.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección crónica por el virus de la hepatitis C (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Infección por VIH |
| Puntaje de Predicción TxGNN | 99,87% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, glecaprevir es un inhibidor de la proteasa NS3/4A del VHC, administrado en combinación fija con pibrentasvir (inhibidor de NS5A), y su eficacia en la hepatitis C crónica está bien establecida.

Glecaprevir **no tiene actividad antiviral directa contra el VIH**. La predicción del modelo probablemente refleja la población de pacientes compartida (la coinfección VIH/VHC es frecuente) y la cercanía entre enfermedades virales en el grafo de conocimiento. La evidencia clínica disponible demuestra la cura del VHC en pacientes coinfectados con VIH, lo que es una extensión de la indicación original a una población coinfectada, no un tratamiento del VIH.

Por ello, cualquier afirmación debe limitarse a la **curación del VHC en pacientes con coinfección por VIH**.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03222583](https://clinicaltrials.gov/study/NCT03222583) | Fase 3 | Completado | 546 | ECA doble ciego controlado con placebo de glecaprevir/pibrentasvir en adultos asiáticos sin cirrosis con VHC GT1-6, con o sin coinfección por VIH |
| [NCT02738138](https://clinicaltrials.gov/study/NCT02738138) | Fase 3 | Completado | 153 | EXPEDITION-2: eficacia y seguridad de glecaprevir/pibrentasvir en adultos con VHC GT1-6 y coinfección por VIH-1 |
| [NCT03235349](https://clinicaltrials.gov/study/NCT03235349) | Fase 3 | Completado | 160 | Estudio abierto en adultos asiáticos con cirrosis compensada y VHC GT1-6, con o sin coinfección por VIH |
| [NCT04042740](https://clinicaltrials.gov/study/NCT04042740) | Fase 2 | Completado | 45 | PURGE-C: 4 semanas de glecaprevir/pibrentasvir en hepatitis C aguda, con o sin coinfección por VIH-1 |
| [NCT02634008](https://clinicaltrials.gov/study/NCT02634008) | Fase 3 | Completado | 83 | Estudio piloto internacional en hepatitis C de adquisición reciente, con o sin VIH; incluye otros regímenes además de glecaprevir/pibrentasvir |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Fase 4 | Completado | 87 | Riesgo cardiovascular tras la erradicación del VHC en personas con VIH/VHC; el desenlace es cardiovascular, no antiviral |
| [NCT07040319](https://clinicaltrials.gov/study/NCT07040319) | Fase 1/2 | Reclutando | 30 | Farmacocinética y seguridad de glecaprevir/pibrentasvir iniciado en el embarazo, con o sin VIH; sin datos de eficacia |

Nota: en varios ensayos el vínculo con la coinfección por VIH debe verificarse, y todos evalúan el tratamiento del VHC.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41297677](https://pubmed.ncbi.nlm.nih.gov/41297677/) | 2026 | Fase IIIb de un solo brazo | Journal of Hepatology | Eficacia y seguridad de 8 semanas de glecaprevir/pibrentasvir en adultos con hepatitis C aguda |
| [37671831](https://pubmed.ncbi.nlm.nih.gov/37671831/) | 2023 | Cohorte | J Antimicrob Chemother | Respuesta a glecaprevir/pibrentasvir en pacientes coinfectados VIH/VHC en práctica clínica |
| [39697370](https://pubmed.ncbi.nlm.nih.gov/39697370/) | 2024 | Cohorte | Clin Exp Hepatol | Efectividad de glecaprevir/pibrentasvir en coinfectados VIH/VHC tratados con bictegravir/emtricitabina/tenofovir alafenamida |
| [31284039](https://pubmed.ncbi.nlm.nih.gov/31284039/) | 2019 | Revisión sistemática y metaanálisis | Int J Antimicrob Agents | 13 estudios con 3082 pacientes; tasa global de RVS12 del 97,8% |
| [32754824](https://pubmed.ncbi.nlm.nih.gov/32754824/) | 2020 | Cohorte | Adv Ther | Uso real de 8 semanas de glecaprevir/pibrentasvir en pacientes sin tratamiento previo con cirrosis compensada |
| [31504702](https://pubmed.ncbi.nlm.nih.gov/31504702/) | 2020 | Estudio farmacocinético | J Infect Dis | Interacciones de glecaprevir/pibrentasvir con antirretrovirales del VIH |
| [30499343](https://pubmed.ncbi.nlm.nih.gov/30499343/) | 2019 | Revisión | Future Microbiol | Glecaprevir/pibrentasvir en la infección crónica por VHC |
| [30090878](https://pubmed.ncbi.nlm.nih.gov/30090878/) | 2018 | Revisión | Drugs Today | Combinación de dosis fija en adultos con VHC GT1-6 |
| [29595065](https://pubmed.ncbi.nlm.nih.gov/29595065/) | 2018 | Revisión | Expert Opin Pharmacother | Terapia con inhibidores de proteasa en VHC; menciona la coinfección con VIH |
| [38293756](https://pubmed.ncbi.nlm.nih.gov/38293756/) | 2024 | Revisión sistemática y metaanálisis | Liver Int | Eficacia y seguridad de los antivirales de acción directa en niños y adolescentes con VHC |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1171213002 | MAVIRET 50 MG/20 MG gránulos recubiertos en sobre | Gránulos recubiertos en sobres | Texto de indicación no disponible |
| 1171213001 | MAVIRET 100 MG/40 MG comprimidos recubiertos con película | Comprimido recubierto con película | Texto de indicación no disponible |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se han identificado 57 interacciones conocidas. Entre las principales:
  - **Gravedad mayor**: rosuvastatina, simvastatina y edoxabán.
  - **Gravedad moderada**: dexametasona, esomeprazol, omeprazol, apixabán, betrixabán, cobicistat, deferasirox, metreleptina, naldemedina, troglitazona, lusutrombopag, revefenacina y griseofulvina.
  - **Gravedad menor**: fidaxomicina, naloxegol, procaloprida e indacaterol.
- **Precauciones en coinfección con VIH**: es necesario revisar las interacciones con los antirretrovirales; glecaprevir está contraindicado o no se recomienda con algunos agentes, como efavirenz y regímenes basados en atazanavir.
- **Reactivación del virus de la hepatitis B**: debe monitorizarse en pacientes coinfectados, ya que es una advertencia de clase para los antivirales de acción directa contra el VHC.

Para el resto de la información de seguridad (advertencias y contraindicaciones), consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen varios ensayos de Fase 3 completados que respaldan la curación del VHC con glecaprevir/pibrentasvir en pacientes coinfectados con VIH (nivel L1). Sin embargo, el fármaco no actúa contra el VIH, por lo que la indicación debe formularse como tratamiento del VHC en pacientes coinfectados, no como tratamiento del VIH.

**Para avanzar se necesita:**
- Delimitar la indicación a la curación del VHC en pacientes con coinfección por VIH, sin afirmar eficacia contra el VIH.
- Verificar el vínculo con la coinfección por VIH en los ensayos con título truncado (p. ej., NCT03222583 y NCT03235349).
- Revisar sistemáticamente las interacciones con los antirretrovirales.
- Plan de monitorización de la reactivación del virus de la hepatitis B.
- Obtener el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas) y los datos del mecanismo de acción.

### Otras Predicciones Evaluadas (Resumen)

Las demás indicaciones predichas tienen una recomendación **Hold**: hepatitis B (L4; sin mecanismo plausible y con riesgo de reactivación del VHB), hepatitis A (L4; los ensayos asociados son de VHC y no respaldan la indicación), hepatitis E, hepatitis viral animal, síndrome de inmunodeficiencia adquirida felina, infección por el virus de inmunodeficiencia de simios, fiebre hemorrágica de Omsk, enfermedad del bosque de Kyasanur y un trastorno del neurodesarrollo (todas L4-L5, sin evidencia ni mecanismo que las respalde).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


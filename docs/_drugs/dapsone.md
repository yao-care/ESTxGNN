---
layout: default
title: Dapsone
parent: Evidencia alta (L1-L2)
nav_order: 157
evidence_level: L1
indication_count: 1
---

# Dapsone
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **1** 
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

# Dapsona: De Lepra y Dermatitis Herpetiforme a Neumocistosis

## Resumen en Una Frase

La dapsona es un antibiótico sulfónico que se usa clásicamente en la lepra (como parte de un régimen combinado) y en la dermatitis herpetiforme. El modelo TxGNN predice que podría ser efectiva para la **neumocistosis** (neumonía por *Pneumocystis jirovecii*). Esta dirección cuenta con **14 ensayos clínicos** (4 de Fase 3 completados) y **19 publicaciones**. Cabe señalar que la profilaxis de la neumonía por *Pneumocystis* con dapsona ya está descrita en la literatura, por lo que esta predicción es más una confirmación que un hallazgo nuevo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en la autorización de AEMPS (texto de indicación vacío). Según la fuente de farmacología del pack: lepra y dermatitis herpetiforme |
| Nueva Indicación Predicha | Neumocistosis |
| Puntaje de Predicción TxGNN | 99,73 % |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la ficha del fármaco. Según la información complementaria, la dapsona inhibe la enzima dihidropteroato sintasa (DHPS) en la vía de síntesis del folato. Es el mismo objetivo que los sulfamidas como el sulfametoxazol. Una revisión de Hughes (1998) describe además que la dapsona bloquea la síntesis de ácido fólico de *Pneumocystis* y tiene efecto sinérgico con trimetoprima o pirimetamina. Los datos de farmacología también recogen que inhibe la actividad de la dihidrofolato reductasa en *Pneumocystis carinii* in vitro (IC50 de 1,5 µM).

*Pneumocystis jirovecii* depende de la síntesis de novo de folato. Por eso inhibir la DHPS es biológicamente plausible y coherente con la puntuación alta del modelo. La relación entre las indicaciones clásicas (infecciones y enfermedades neutrofílicas) y la neumocistosis es sobre todo antimicrobiana. La dapsona actúa sobre una vía metabólica de un patógeno oportunista. La similitud formal con la indicación original figura como pendiente de análisis.

Un matiz importante: las mutaciones de DHPS en *P. jirovecii* podrían reducir la sensibilidad a los fármacos de la clase sulfa. Además, las guías europeas (ECIL) señalan que el trimetoprima/sulfametoxazol sigue siendo el fármaco de elección. La dapsona se contempla sobre todo como alternativa en pacientes que no toleran TMP-SMX.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Fase 3 | Completado | 700 | Dapsona diaria vs. atovacuona diaria para profilaxis de PCP en pacientes con VIH intolerantes a trimetoprima o sulfamidas |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Fase 3 | Completado | 400 | Pentamidina en aerosol mensual vs. dapsona tres veces por semana en profilaxis de PCP (pacientes intolerantes a TMP/sulfamidas) |
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Fase 3 | Completado | 290 | Dapsona/trimetoprima y clindamicina/primaquina vs. régimen basado en trimetoprima en PCP leve-moderada asociada a SIDA |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Fase 3 | Completado | 600 | Tres agentes anti-Pneumocystis más zidovudina en prevención primaria en VIH avanzado (el brazo de dapsona debe verificarse, el título está truncado) |
| [NCT00002043](https://clinicaltrials.gov/study/NCT00002043) | No especificada | Completado | No informado | Dapsona 100 mg vs. 50 mg como profilaxis primaria de PCP en pacientes con complejo relacionado con el SIDA |
| [NCT00000739](https://clinicaltrials.gov/study/NCT00000739) | Fase 1 | Completado | 96 | Dapsona diaria vs. semanal en profilaxis de PCP en niños con VIH; toxicidad y farmacocinética |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Fase 1 | Completado | 20 | Trimetrexato con leucovorina más dapsona vs. TMP/SMX en PCP moderadamente grave; seguridad y farmacocinética |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | No especificada | Completado | No informado | Dapsona (más trimetoprima) vs. TMP-SMX en el primer episodio de PCP en pacientes con SIDA |
| [NCT02550080](https://clinicaltrials.gov/study/NCT02550080) | Fase 4 | Desconocido | 3130 | Cribado genético HLA-B*1301 para prevenir el síndrome de hipersensibilidad a dapsona (relevante para seguridad) |
| [NCT05077150](https://clinicaltrials.gov/study/NCT05077150) | No aplica | Completado | 168 | Estudio de casos y controles sobre factores de riesgo de PCP tras trasplante alogénico; menciona una incidencia de hasta 7,2 % con dosis bajas de dapsona |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | Revisión sistemática / metaanálisis en red de ECA | Clin Microbiol Infect | Compara regímenes de profilaxis de PCP en personas con VIH: TMP-SMX, regímenes con dapsona, pentamidina en aerosol y atovacuona |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Revisión sistemática / metaanálisis en red de ECA | Clin Microbiol Infect | Compara regímenes de tratamiento de PCP en personas con VIH; TMP-SMX se considera el tratamiento principal |
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | Guía clínica | J Antimicrob Chemother | Guías ECIL para profilaxis de PCP en neoplasias hematológicas y trasplante de progenitores; TMP-SMX 2-3 veces por semana es el fármaco de elección |
| [9675476](https://pubmed.ncbi.nlm.nih.gov/9675476/) | 1998 | Revisión | Clin Infect Dis | Dapsona (sola o con trimetoprima/pirimetamina) tiene fuerte actividad anti-Pneumocystis; inhibe la DHPS, se absorbe un 70-80 % por vía oral y alcanza el líquido alveolar |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Revisión | Expert Opin Pharmacother | Revisión de *P. jirovecii* con foco en prevención y tratamiento en huéspedes inmunodeprimidos |
| [8605054](https://pubmed.ncbi.nlm.nih.gov/8605054/) | 1995 | Estudio clínico | AIDS | Compara pentamidina en aerosol, cotrimoxazol y dapsona-pirimetamina en profilaxis primaria de PCP y encefalitis toxoplásmica en VIH |
| [7979291](https://pubmed.ncbi.nlm.nih.gov/7979291/) | 1994 | Estudio farmacocinético | Antimicrob Agents Chemother | Dapsona semanal sola o con pirimetamina; dosis máxima tolerada de 200 mg/semana en pacientes que reciben al menos 500 mg de zidovudina |
| [11155588](https://pubmed.ncbi.nlm.nih.gov/11155588/) | 2001 | Revisión | Dermatol Clin | Dapsona y sulfapiridina: efecto antimicrobiano y antiinflamatorio; útil en la profilaxis de neumonía por *Pneumocystis* en VIH |
| [33280223](https://pubmed.ncbi.nlm.nih.gov/33280223/) | 2021 | Revisión retrospectiva de casos | Pediatr Transplant | Metahemoglobinemia por dapsona en niños trasplantados de riñón que la usan como profilaxis de PJP |
| [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/) | 1998 | Reporte de caso | Ann Pharmacother | Metahemoglobinemia en un paciente que recibía dapsona como profilaxis de PCP |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 15201 | SULFONA COMPRIMIDOS (Esteve Pharmaceuticals S.A.) | Comprimido | No consta en los datos disponibles |

---

## Consideraciones de Seguridad

- **Señales de seguridad en la literatura**: metahemoglobinemia con hipoxia (PMID 9606476, 32714715, 33280223) y un caso de pancreatitis aguda (PMID 14519046).
- **Hipersensibilidad**: existe un ensayo de Fase 4 sobre cribado de HLA-B*1301 para prevenir el síndrome de hipersensibilidad a dapsona (NCT02550080, estado desconocido).
- **Interacciones farmacológicas**: los dos registros disponibles corresponden a dianas farmacológicas (TAS2R40 y la DHPS de *Plasmodium falciparum*). No son interacciones clínicas con otros medicamentos.

Las advertencias y contraindicaciones oficiales de AEMPS no están disponibles en el pack. Consultar el prospecto para la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay cuatro ensayos de Fase 3 completados y metaanálisis en red recientes que respaldan a la dapsona en la profilaxis y el tratamiento de la neumocistosis, por lo que el nivel de evidencia es L1. Sin embargo, TMP-SMX sigue siendo el fármaco de elección. La ficha de AEMPS no recoge la indicación y faltan los datos oficiales de seguridad, por lo que se recomienda avanzar con salvaguardas.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS de SULFONA (advertencias, contraindicaciones e indicación autorizada). Es una brecha bloqueante para el cribado de seguridad.
- Confirmar si la neumocistosis figura entre las indicaciones autorizadas en España o si sería un uso fuera de ficha técnica.
- Verificar los brazos de tratamiento del ensayo NCT00000991, cuyo título está truncado.
- Definir un plan de monitorización de metahemoglobinemia y valorar el cribado de HLA-B*1301 según la población.
- Completar los datos del mecanismo de acción desde DrugBank.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


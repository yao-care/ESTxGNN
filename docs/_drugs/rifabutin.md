---
layout: default
title: Rifabutin
parent: Evidencia alta (L1-L2)
nav_order: 698
evidence_level: L1
indication_count: 10
---

# Rifabutin
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

# Rifabutina: De Indicación No Especificada en la Ficha a Infección por VIH

## Resumen en Una Frase

Rifabutina es un antibiótico de la familia de las rifamicinas, comercializado en España como Ansatipin 150 mg cápsulas duras; los datos compilados no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser útil para **infección por VIH**, aunque la rifabutina no actúa sobre el virus: su valor está en tratar y prevenir infecciones micobacterianas oportunistas en personas con VIH.
Esta dirección cuenta con **34 ensayos clínicos** y **20 publicaciones** recuperadas, de los cuales los más relevantes son ensayos de fase 3 en complejo *Mycobacterium avium* (MAC) asociado a sida.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de la autorización de la AEMPS |
| Nueva Indicación Predicha | Infección por VIH (en la práctica, infecciones micobacterianas oportunistas asociadas al VIH) |
| Puntaje de Predicción TxGNN | 99,88% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Rifabutina es una rifamicina que inhibe la ARN polimerasa bacteriana dependiente de ADN (gen *rpoB*). No tiene actividad contra el VIH. Los datos compilados no incluyen una descripción formal del mecanismo de acción procedente de DrugBank, por lo que esta explicación se basa en el conocimiento farmacológico general de la clase.

La relación con el VIH es indirecta pero clínicamente sólida. Las personas con VIH avanzado sufren con frecuencia infecciones por MAC y tuberculosis. La rifabutina se ha estudiado tanto para prevenir como para tratar estas infecciones. Además, induce menos el CYP3A4 que la rifampicina, por lo que es la rifamicina preferida cuando se administra junto con inhibidores de la proteasa y otros antirretrovirales.

Por tanto, la predicción es razonable como **uso en infecciones oportunistas asociadas al VIH**, no como tratamiento antiviral. Gran parte de la evidencia trata de interacciones farmacológicas y farmacocinética con el tratamiento antirretroviral (TAR), además de la eficacia frente a enfermedad micobacteriana asociada al VIH.

## Evidencia de Ensayos Clínicos

Se recuperaron 34 ensayos; se listan los 10 más relevantes (los de mayor grado de relevancia y diseño más robusto).

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Fase 3 | Completado | 400 | Cuatro pautas con claritromicina, etambutol y rifabutina o clofazimina en MAC diseminado en sida |
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Fase 3 | Completado | 450 | Claritromicina/etambutol con placebo o rifabutina a dos dosis en bacteriemia por MAC |
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Fase 3 | Completado | 1100 | Claritromicina vs. rifabutina vs. combinación para prevenir MAC en VIH con CD4 ≤100 |
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Fase 3 | Completado | 720 | Azitromicina y rifabutina, solas y combinadas, para prevenir MAC diseminado |
| [NCT00001995](https://clinicaltrials.gov/study/NCT00001995) | NA (aleatorizado, doble ciego) | Completado | 200 | Pauta con rifabutina para bacteriemia por MAC en sida |
| [NCT00002267](https://clinicaltrials.gov/study/NCT00002267) | NA (doble ciego, controlado con placebo) | Completado | 750 | Rifabutina en monoterapia para prevenir bacteriemia por MAC con CD4 ≤200 |
| [NCT00001058](https://clinicaltrials.gov/study/NCT00001058) | Fase 2 | Completado | 246 | Claritromicina con rifabutina, etambutol o ambos en MAC diseminado |
| [NCT00023361](https://clinicaltrials.gov/study/NCT00023361) | NA | Completado | 215 | Pauta intermitente con rifabutina en tuberculosis relacionada con VIH (fracaso y recaída) |
| [NCT00651066](https://clinicaltrials.gov/study/NCT00651066) | Fase 2 | Completado | 47 | Farmacocinética de rifabutina con TAR en tuberculosis/VIH (Vietnam) |
| [NCT00640887](https://clinicaltrials.gov/study/NCT00640887) | Fase 2 | Completado | 48 | Farmacocinética de rifabutina con TAR en tuberculosis/VIH (Sudáfrica) |

Entre los ensayos restantes figuran numerosos estudios de interacciones farmacocinéticas con antirretrovirales (indinavir, nelfinavir, nevirapina, efavirenz, maraviroc, dolutegravir, cabotegravir, entre otros) y un ensayo aún no reclutando (NCT07585461) sobre fluoroquinolonas añadidas a la triple terapia en MAC diseminado.

## Evidencia de Literatura

Se recuperaron 20 publicaciones; se listan las más relevantes (predominan revisiones y estudios farmacocinéticos; no hay ECA entre ellas).

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | Cohorte | J Antimicrob Chemother | Seguridad y eficacia de rifabutina en niños con VIH/TB con lopinavir/ritonavir; se describió neutropenia que obligó a suspender el tratamiento en estudios previos |
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | Cohorte | J Antimicrob Chemother | Farmacocinética y seguridad de rifabutina en niños con TB/VIH |
| [36385424](https://pubmed.ncbi.nlm.nih.gov/36385424/) | 2023 | Modelo farmacocinético | Br J Clin Pharmacol | Interacción rifabutina–dolutegravir; la rifabutina es una alternativa menos inductora que la rifampicina |
| [21819645](https://pubmed.ncbi.nlm.nih.gov/21819645/) | 2012 | Revisión | Int J Tuberc Lung Dis | Papel de la rifabutina con TAR basado en inhibidores de la proteasa y tuberculosis |
| [17181373](https://pubmed.ncbi.nlm.nih.gov/17181373/) | 2006 | Revisión | Drugs | Enfoque terapéutico práctico de la coinfección tuberculosis/VIH |
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | Revisión | Microbiol Spectrum | Tuberculosis asociada a la infección por VIH |
| [10456381](https://pubmed.ncbi.nlm.nih.gov/10456381/) | 1999 | Revisión | Drug Safety | Riesgo-beneficio de las terapias para infecciones por MAC |
| [11996607](https://pubmed.ncbi.nlm.nih.gov/11996607/) | 2002 | Revisión | Arch Intern Med | Actualización de interacciones de rifampicina y rifabutina |
| [7736687](https://pubmed.ncbi.nlm.nih.gov/7736687/) | 1995 | Farmacocinética | Clin Pharmacokinet | Eficacia de rifabutina para profilaxis de MAC diseminado en VIH con CD4 bajo |
| [9093233](https://pubmed.ncbi.nlm.nih.gov/9093233/) | 1997 | Revisión | Med Clin North Am | Infecciones por micobacterias no tuberculosas en sida |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 60228 | ANSATIPIN 150 MG CÁPSULAS DURAS | Cápsula dura | No disponible en los datos compilados |

Titular de fabricación: Binesa 2002 S.L. Autorización vigente, de tipo monocomponente.

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación en el grafo de conocimiento** (relaciones del grafo, no texto de ficha técnica): trombocitopenia, neutropenia, agranulocitosis, colitis por *Clostridium difficile* y enterocolitis necrosante perinatal. La neutropenia coincide con lo observado en estudios pediátricos con inhibidores de la proteasa.
- **Interacciones farmacológicas**: se identificaron 163 interacciones. Entre las 20 mostradas, una es de gravedad **mayor** (eliglustat), una **menor** (dolasetrón) y el resto **moderadas**, entre ellas doxiciclina, corticoides (hidrocortisona, dexametasona, betametasona, triamcinolona), claritromicina, metronidazol, aprepitant, morfina, pioglitazona, saxagliptina, linagliptina, clorpropamida, acetohexamida y análogos de la vitamina D. Es relevante la inducción enzimática (CYP3A4), menor que con rifampicina pero presente, sobre antirretrovirales y otros fármacos.

No se dispone de advertencias ni contraindicaciones del prospecto en los datos compilados; consultar el prospecto de la AEMPS.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen varios ensayos de fase 3 completados con rifabutina en prevención y tratamiento de MAC en pacientes con sida, lo que cumple el criterio de nivel L1. Sin embargo, la rifabutina no tiene actividad antiviral: el beneficio se limita a infecciones micobacterianas oportunistas asociadas al VIH, y buena parte de la evidencia son estudios de interacciones y farmacocinética, con terapias de la era previa al TAR actual.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (indicaciones, advertencias y contraindicaciones), actualmente ausente.
- Completar los datos del mecanismo de acción desde DrugBank.
- Definir con precisión la indicación objetivo (profilaxis o tratamiento de MAC, o tuberculosis en coinfección con VIH) en lugar de "infección por VIH" en general.
- Plan de manejo de interacciones con regímenes antirretrovirales actuales y de monitorización hematológica (neutropenia, trombocitopenia), con especial atención a población pediátrica.
- Revisar la vigencia de la evidencia frente a las guías actuales, dado que gran parte de los ensayos son de las décadas de 1990 y 2000.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


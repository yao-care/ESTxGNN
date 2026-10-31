---
layout: default
title: Epinephrine
parent: Solo predicción del modelo (L5)
nav_order: 296
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-31
monitor_inn: "epinephrine"
predicted_indications: ["obstructive lung disease", "Rienhoff syndrome", "respiratory malformation"]
description: "Epinephrine: nueva indicación predicha, Enfermedad pulmonar obstructiva (obstructive lung disease) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Epinephrine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

## Epinephrine: Enfermedad pulmonar obstructiva (obstructive lung disease)
{: .text-alpha }

## Resumen en Una Frase

La epinefrina (adrenalina) es un agonista adrenérgico utilizado originalmente en indicaciones como el glaucoma de ángulo abierto, el asma, la bronquitis, la anafilaxia y la hipotensión.
El modelo TxGNN predice que podría ser efectiva para la **enfermedad pulmonar obstructiva**,
con **15 ensayos clínicos** (14 de ellos relacionados con el sistema respiratorio, entre ellos 3 de Fase 3 completados en asma) y **20 publicaciones** que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Enfermedad pulmonar obstructiva (obstructive lung disease) |
| Puntaje de Predicción TxGNN | 0.9971 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 16) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

La epinefrina es un agonista adrenérgico no selectivo. La estimulación de los receptores beta-2 relaja el músculo liso bronquial y produce broncodilatación, mientras que la estimulación alfa-1 reduce el edema de la mucosa y la congestión vascular de la vía aérea. Los datos compilados no incluyen una descripción formal del mecanismo de acción, pero esta farmacología es bien conocida.

Varias de las indicaciones originales del fármaco (asma, bronquitis, enfisema, bronquiectasias) son enfermedades obstructivas de la vía aérea. Por tanto, la predicción es en buena medida una extensión de una indicación ya establecida (asma) y de una farmacología conocida, más que un salto hacia un territorio completamente nuevo.

Además, existe evidencia adicional en bronquiolitis pediátrica (epinefrina nebulizada), una enfermedad obstructiva de la vía aérea inferior en lactantes. Los resultados en este contexto son menos concluyentes, como señalan las revisiones Cochrane y las revisiones recientes.

## Evidencia de Ensayos Clínicos

Se muestran los 10 ensayos más relevantes de los 15 registrados.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01357642](https://clinicaltrials.gov/study/NCT01357642) | Fase 3 | Completado | 373 | Eficacia y seguridad a 12 semanas de epinefrina inhalada (HFA-MDI) frente a placebo y a Primatene Mist en adolescentes y adultos con asma |
| [NCT01476904](https://clinicaltrials.gov/study/NCT01476904) | Fase 3 | Completado | 208 | Extensión de seguridad de 3 meses, doble ciego, de epinefrina inhalada frente a placebo en asma |
| [NCT01460511](https://clinicaltrials.gov/study/NCT01460511) | Fase 3 | Completado | 70 | Eficacia y seguridad de E004 (epinefrina inhalada) frente a placebo durante 4 semanas en niños de 4 a 11 años con asma |
| [NCT01737905](https://clinicaltrials.gov/study/NCT01737905) | Fase 3 | Completado | 28 | Estudio cruzado de dosis única de E004 frente a placebo en niños con asma |
| [NCT01705964](https://clinicaltrials.gov/study/NCT01705964) | Fase 4 | Completado | 49 | Epinefrina intramuscular como adyuvante de broncodilatadores β2 en exacerbación grave de asma pediátrica |
| [NCT00817466](https://clinicaltrials.gov/study/NCT00817466) | Fase 4 | Desconocido | 500 | Comparación de tratamientos inhalados en bronquiolitis aguda en lactantes de 0 a 12 meses |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | No aplica | Desconocido | 600 | Comparación de epinefrina y albuterol en bronquiolitis |
| [NCT01834820](https://clinicaltrials.gov/study/NCT01834820) | Fase 4 | Completado | 120 | Estudio piloto aleatorizado de epinefrina, dexametasona y suero salino hipertónico en bronquiolitis |
| [NCT02585531](https://clinicaltrials.gov/study/NCT02585531) | Fase 2 | Desconocido | 100 | Epinefrina, dexametasona y suero salino hipertónico en bronquiolitis infantil |
| [NCT00622817](https://clinicaltrials.gov/study/NCT00622817) | No aplica | Completado | 65 | Inhalación de epinefrina frente a gotas nasales descongestionantes (xilometazolina) en bronquiolitis |

Además hay estudios farmacocinéticos en voluntarios sanos (NCT01255709, NCT04207840, NCT01737892, NCT01188577), un estudio sobre salino hipertónico en bronquiolitis (NCT01276821) y un estudio de obstrucción de la vía aérea en lactantes (NCT00435994), que aportan datos de exposición o evidencia indirecta.

## Evidencia de Literatura

Se muestran las publicaciones más relevantes de las 20 recuperadas.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35093318](https://pubmed.ncbi.nlm.nih.gov/35093318/) | 2022 | ECA | The Journal of Pediatrics | Ensayo pragmático de corticoides sistémicos con epinefrina nebulizada en bronquiolitis en cuidados intensivos, sobre la duración del soporte con presión positiva |
| [33893229](https://pubmed.ncbi.nlm.nih.gov/33893229/) | 2021 | Metaanálisis en red | Pediatrics | Comparación de la eficacia de intervenciones para bronquiolitis en atención aguda |
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Epinefrina para bronquiolitis; los broncodilatadores se usan con frecuencia pese a una eficacia incierta |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Revisión sistemática (Cochrane) | Cochrane Database Syst Rev | Versión anterior de la revisión sobre epinefrina en bronquiolitis |
| [35953216](https://pubmed.ncbi.nlm.nih.gov/35953216/) | 2022 | Revisión | Emerg Med Clin North Am | Evaluación y manejo de las exacerbaciones de asma y EPOC en urgencias |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Revisión | Expert Rev Respir Med | Papel de la epinefrina racémica, corticoides, salino hipertónico y oxígeno de alto flujo en bronquiolitis |
| [23393929](https://pubmed.ncbi.nlm.nih.gov/23393929/) | 2012 | Revisión | Duodecim | Manejo de la bronquiolitis; las inhalaciones de epinefrina racémica se usan cuando es necesario |
| [21157348](https://pubmed.ncbi.nlm.nih.gov/21157348/) | 2011 | Revisión | Curr Opin Pediatr | Ningún tratamiento ha demostrado de forma concluyente modificar la evolución de la bronquiolitis |
| [20876171](https://pubmed.ncbi.nlm.nih.gov/20876171/) | 2010 | Análisis de coste-efectividad | Pediatrics | Coste-efectividad de epinefrina y dexametasona en bronquiolitis |
| [11940264](https://pubmed.ncbi.nlm.nih.gov/11940264/) | 2002 | Revisión clínica | Critical Care | Asma grave y estado asmático |

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de medicamentos con un solo principio activo). El texto de la indicación aprobada no está disponible en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 68552 | Adrenalina B. Braun 1 mg/ml | Solución inyectable | No disponible |
| 89175 | Adrenalina Basi 1 mg/ml | Solución inyectable | No disponible |
| 73186 | Jext 150 microgramos | Solución inyectable en pluma precargada | No disponible |
| 80831 | Adrenalina Aguettant 0,1 mg/ml | Solución inyectable en jeringa precargada | No disponible |
| 67263 | Altellus 150 microgramos niños | Solución inyectable en pluma precargada | No disponible |

Las 15 autorizaciones restantes incluyen otras plumas autoinyectables (Emerade, Anapen, Altellus, Jext), otras presentaciones de adrenalina inyectable y combinaciones de anestésicos locales con epinefrina.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): hipertensión, enfermedad cardiovascular y cardiopatía, infarto de miocardio, enfermedad coronaria, fibrilación auricular, trastornos de la conducción cardíaca, parada cardíaca súbita, diabetes mellitus y cetoacidosis diabética, hipertiroidismo, glaucoma de ángulo cerrado, insuficiencia hepática y renal, epilepsia, hiperplasia prostática benigna, miastenia gravis, insuficiencia respiratoria, entre otras.
- **Interacciones farmacológicas**: se identificaron 385 interacciones. Entre las de nivel **mayor** figuran amitriptilina y amoxapina (antidepresivos tricíclicos). Entre las de nivel **moderado** figuran betabloqueantes (acebutolol, atenolol, betaxolol), agonistas beta-2 (formoterol, salbutamol, arformoterol), estimulantes (metilfenidato, anfetamina, atomoxetina), antidiabéticos (acarbosa, acetohexamida, albiglutida, alogliptina) y antipsicóticos (amisulprida, aripiprazol, asenapina).

Consultar el prospecto para las advertencias y contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existen tres ensayos de Fase 3 completados con epinefrina inhalada en asma (adultos y niños), además de revisiones Cochrane en bronquiolitis, y la farmacología es coherente con indicaciones ya establecidas. Sin embargo, la evidencia en bronquiolitis es heterogénea, la mayoría de los ensayos pediátricos son pequeños y el perfil cardiovascular exige precaución.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto oficial de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas), cuya ausencia impide completar el cribado de seguridad.
- Datos detallados del mecanismo de acción desde DrugBank.
- Definir qué subtipo de enfermedad obstructiva (asma, EPOC, bronquiolitis) y qué vía de administración se priorizan, ya que las presentaciones comercializadas en España son inyectables y los ensayos de asma emplearon un inhalador.
- Plan de monitoreo cardiovascular y de interacciones (especialmente con tricíclicos y betabloqueantes) en poblaciones de riesgo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


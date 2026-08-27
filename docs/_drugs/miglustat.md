---
layout: default
title: Miglustat
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
---

# Miglustat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Miglustat: De Enfermedad de Gaucher Tipo 1 a Enfermedad de Tay-Sachs (Gangliosidosis GM2)

## Resumen en Una Frase

Miglustat (Zavesca®) es un inhibidor oral de la glucosilceramida sintasa, aprobado originalmente en la UE (2002) para el tratamiento de la enfermedad de Gaucher tipo 1 mediante terapia de reducción de sustrato. El modelo TxGNN predice diez posibles nuevas indicaciones dentro del espectro de enfermedades de depósito lisosomal, y de ellas la **Enfermedad de Tay-Sachs (gangliosidosis GM2)** es la única que actualmente cuenta con respaldo real, con **5 ensayos clínicos** y **20 publicaciones** identificadas. Las otras 9 indicaciones predichas (puntajes TxGNN >99.7%) carecen por completo de ensayos clínicos o literatura de apoyo.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No consta en licencias de España (medicamento no comercializado); según literatura del evidence pack (PMID 12808890), aprobado en la UE en 2002 como Zavesca® para enfermedad de Gaucher tipo 1 |
| Nueva Indicacion Predicha | Enfermedad de Tay-Sachs (Gangliosidosis GM2) |
| Puntaje de Prediccion TxGNN | 99.75% (rank global 4756) |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Proceed with Guardrails |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos estructurados detallados sobre el mecanismo de acción en el evidence pack. Según la literatura identificada, miglustat es un inhibidor de la enzima glucosilceramida sintasa, utilizado como terapia de reducción de sustrato (SRT) para trastornos de depósito de glucoesfingolípidos. Su eficacia en la enfermedad de Gaucher tipo 1 (deficiencia de glucocerebrosidasa) ha sido comprobada y aprobada regulatoriamente, y mecanísticamente podría ser aplicable a otras gangliosidosis con acumulación de esfingolípidos.

La enfermedad de Tay-Sachs es causada por deficiencia de hexosaminidasa A, lo que provoca acumulación de gangliósido GM2, un esfingolípido situado corriente abajo de la glucosilceramida en la vía de biosíntesis. Al inhibir la síntesis del precursor común, miglustat reduce teóricamente el flujo total hacia GM2, la misma lógica de SRT ya validada en Gaucher. Esta hipótesis fue confirmada primero en modelos animales (Platt et al., 1997, *Science*, PMID 9103204) y posteriormente explorada en humanos.

Sin embargo, la evidencia clínica es mixta: en la forma infantil, el ensayo pivotal de Fase 3 (NCT03822013) fue **terminado** y un estudio de casos (PMID 16434676) no logró detener el deterioro neurológico, aunque sí demostró penetración en LCR. En la forma tardía (late-onset), un ensayo aleatorizado controlado (PMID 19346952) sí mostró señales de seguridad y eficacia sostenidas a 24 meses. Efectos gastrointestinales limitan además la dosificación pediátrica (PMID 28476546). Por ello el vínculo mecanístico es razonable pero la evidencia de eficacia clínica es todavía limitada y heterogénea según el subtipo de la enfermedad.

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Fase 3 | Terminado | 30 | Evaluación de efectos neurológicos y sistémicos de miglustat en formas infantiles de Sandhoff y Tay-Sachs |
| [NCT07399704](https://clinicaltrials.gov/study/NCT07399704) | Fase 2 | Reclutando | 21 | Seguridad, farmacocinética y eficacia a largo plazo de nizubaglustat (sucesor de miglustat) en gangliosidosis GM2/Niemann-Pick C, incluye transición desde miglustat |
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Fase 3 | Completado | 10 | Farmacocinética, seguridad y tolerabilidad de Zavesca (miglustat) en gangliosidosis GM2 de inicio infantil |
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Fase 2 | Completado | 5 | Farmacocinética y tolerabilidad de Zavesca (miglustat) en gangliosidosis GM2 juvenil |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Fase 4 | Terminado | 16 | Terapia combinada miglustat + dieta cetogénica en gangliosidosis infantil/juvenil (Syner-G) |

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | ECA | Genetics in Medicine | Estudio aleatorizado controlado de 12 meses (extendido a 24) sobre seguridad y eficacia de miglustat en Tay-Sachs de inicio tardío |
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | Revision sistematica | European Journal of Neurology | Revisión sistemática de eficacia y seguridad de miglustat en gangliosidosis GM2; resultados previos inconsistentes |
| [9103204](https://pubmed.ncbi.nlm.nih.gov/9103204/) | 1997 | Estudio preclinico | Science | Estudio fundacional: N-butildeoxinojirimicina (miglustat) previno acumulación de GM2 cerebral en ratones Tay-Sachs |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | Reporte de caso | Neurology | SRT con miglustat en 2 pacientes con Tay-Sachs infantil; no detuvo el deterioro neurológico pero previno macrocefalia |
| [18618288](https://pubmed.ncbi.nlm.nih.gov/18618288/) | 2008 | Estudio piloto | J Inherit Metab Dis | Evaluación neurocognitiva computarizada como medida de resultado terapéutico en Tay-Sachs de inicio tardío |
| [12808890](https://pubmed.ncbi.nlm.nih.gov/12808890/) | 2003 | Perfil de farmaco | Curr Opin Investig Drugs | Historia de desarrollo de miglustat; aprobado en la UE para Gaucher, en desarrollo para Tay-Sachs, Fabry y Niemann-Pick C |
| [30743792](https://pubmed.ncbi.nlm.nih.gov/30743792/) | 2009 | Revision | Expert Rev Endocrinol Metab | SRT con miglustat para trastornos de depósito de glucoesfingolípidos que afectan el cerebro |
| [32867370](https://pubmed.ncbi.nlm.nih.gov/32867370/) | 2020 | Revision | Int J Mol Sci | Características clínicas, fisiopatología y terapias actuales de las gangliosidosis GM2 |
| [30524313](https://pubmed.ncbi.nlm.nih.gov/30524313/) | 2018 | Revision | Frontiers in Physiology | Nuevos enfoques terapéuticos para la enfermedad de Tay-Sachs |
| [28476546](https://pubmed.ncbi.nlm.nih.gov/28476546/) | 2017 | Estudio de historia natural | Mol Genet Metab | Cronología clínica de gangliosidosis infantiles; SRT con miglustat limitada por efectos gastrointestinales |

## Informacion de Mercado en Espana

Actualmente no hay autorizaciones de comercialización registradas en España para miglustat (medicamento no comercializado; 0 licencias).

## Otras Indicaciones Predichas por TxGNN (Prioridad Baja, Sin Evidencia)

| Rank | Enfermedad Predicha | Puntaje TxGNN | Nivel de Evidencia | Vinculo Mecanistico (resumen) |
|---|---|---|---|---|
| 1 | Síndrome de ictiosis autosómica con curso fatal | 99.83% | L5 | Débil; probable agrupamiento espurio en el espacio de embeddings |
| 2 | Enfermedad de depósito de ésteres de colesterilo (CESD) | 99.82% | L5 | Deficiencia de LIPA (lípidos neutros, no glucoesfingolípidos) — débil |
| 3 | Enfermedad de Krabbe | 99.78% | L5 | Deficiencia de GALC; lógica SRT similar a Gaucher/NPC, moderado pero sin evidencia real |
| 4 | Leucodistrofia metacromática | 99.77% | L5 | Deficiencia de arilsulfatasa A; vía paralela pero no idéntica |
| 5 | Enfermedad de Wolman (hipolipoproteinemia y acantocitosis) | 99.76% | L5 | Espectro LIPA infantil; débil |
| 6 | Encefalopatía por déficit de prosaposina | 99.75% | L5 | Afecta activación de múltiples esfingolipasas; teórico moderado |
| 8 | Neoplasia benigna de glándula suprarrenal | 99.74% | L5 | Sin relación fisiopatológica conocida; probable falso positivo |
| 9 | Ictiosis recesiva ligada al X | 99.73% | L5 | Deficiencia de esteroide sulfatasa; débil |
| 10 | Neurodegeneración asociada a ácido graso hidroxilasa (FAHN) | 99.72% | L5 | Deficiencia de FA2H; vínculo indirecto |

Todas mantienen recomendación **Hold** por ausencia total de ensayos clínicos o literatura de respaldo.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusion y Proximos Pasos

**Decision: Proceed with Guardrails** (aplicable a la indicación de Tay-Sachs/gangliosidosis GM2; las restantes 9 indicaciones predichas permanecen en Hold)

**Justificacion:**
Existe un ensayo aleatorizado controlado completado (PMID 19346952), una revisión sistemática de 2023 y evidencia preclínica fundacional que respaldan la plausibilidad mecanística y cierto beneficio clínico en la forma tardía de Tay-Sachs. Sin embargo, el ensayo pivotal de Fase 3 en la forma infantil (NCT03822013) fue terminado y no existe aprobación regulatoria para esta indicación, por lo que no se justifica un "Go" directo.

**Para avanzar se necesita:**
- Datos de advertencias/contraindicaciones de TFDA/AEMPS (actualmente bloqueante, DG001)
- Confirmación estructurada del mecanismo de acción (DG002)
- Motivo de terminación y resultados parciales de NCT03822013
- Evaluación de riesgo-beneficio diferenciada por subtipo (infantil vs. tardío), dado el perfil de tolerabilidad gastrointestinal limitante en población pediátrica
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


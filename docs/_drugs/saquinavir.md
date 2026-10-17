---
layout: default
title: Saquinavir
parent: Solo predicción del modelo (L5)
nav_order: 726
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Saquinavir: nueva indicación predicha, Síndrome de inmunodeficiencia adquirida felina (nivel de evidencia L5). Indicación original: Infección por VIH y SIDA (el texto de indicación de la autorización…"
monitor_inn: "SAQUINAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
---

# Saquinavir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Saquinavir: De Infección por VIH/SIDA a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Saquinavir es un inhibidor de la proteasa del VIH-1, utilizado originalmente para tratar la infección por VIH y el SIDA.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina**, aunque **no hay ensayos clínicos ni publicaciones** que respalden esta predicción concreta.
Entre las otras predicciones, solo "complejo relacionado con el SIDA" cuenta con evidencia clínica sólida, pero corresponde en esencia a la indicación original y no es un reposicionamiento genuino.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH y SIDA (el texto de indicación de la autorización de AEMPS no está disponible; se toma del grafo de conocimiento) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Saquinavir es un inhibidor de la proteasa del VIH-1: impide la escisión de las poliproteínas virales y, con ello, la producción de viriones maduros. No se dispone de más datos detallados sobre el mecanismo de acción en la información compilada para este informe.

El virus de la inmunodeficiencia felina (FIV) es un lentivirus con una proteasa relacionada, por lo que existe una justificación mecanística de partida. Sin embargo, la proteasa del FIV difiere estructuralmente de la del VIH-1, y se sabe que los inhibidores de la proteasa del VIH-1 tienen menor actividad frente a ella. El puntaje alto del modelo es solo una predicción, sin ensayos ni literatura de apoyo, y además se trata de una enfermedad veterinaria, no humana.

**Otras predicciones del modelo (contexto):**

- **Infección por virus de inmunodeficiencia simia (SIV)** (99.97%, nivel L4): hay cuatro estudios preclínicos o in vitro. Uno de ellos muestra que el SIVmac239 es inhibido por saquinavir con una concentración efectiva del 50 % de 55 nM, frente a 47 nM para el VIH-1. Es evidencia indirecta, sin ensayos en humanos, y es un modelo animal.
- **VIH congénito** (99.47%, nivel L3): dos estudios de cohorte observacionales (saquinavir/ritonavir en mujeres embarazadas y seguridad de la exposición intrauterina a antirretrovirales). No hay datos de eficacia pediátrica.
- **Complejo relacionado con el SIDA** (99.47%, nivel L1): corresponde a la indicación original, con ensayos de Fase 3 y Fase 2 completados. Es coherente con el uso existente, no un reposicionamiento nuevo.
- **Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y disminución de la sustancia blanca cortical** (99.97%, L5) y **la hiperlipidemia combinada familiar obsoleta** (99.59%, L5): sin vínculo mecanístico plausible. En el segundo caso, los inhibidores de la proteasa suelen causar dislipidemia, lo que va en contra de un papel terapéutico.

---

## Evidencia de Ensayos Clínicos

Para la predicción principal (síndrome de inmunodeficiencia adquirida felina): actualmente no hay ensayos clínicos relacionados registrados.

A modo de referencia, estos son los ensayos de la predicción con mayor respaldo clínico (complejo relacionado con el SIDA, es decir, la indicación original):

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00002334](https://clinicaltrials.gov/study/NCT00002334) | Fase 3 | Completado | 3000 | Aleatorizado, doble ciego: zidovudina sola frente a zidovudina + zalcitabina y/o saquinavir en pacientes sin tratamiento previo o mínimamente tratados |
| [NCT00002333](https://clinicaltrials.gov/study/NCT00002333) | Fase 2 | Completado | 900 | Saquinavir solo, zalcitabina sola o ambos, en pacientes que no pueden tomar zidovudina |
| [NCT00001040](https://clinicaltrials.gov/study/NCT00001040) | Fase 2 | Completado | 300 | Saquinavir + AZT frente a AZT + ddC frente a la triple combinación: eficacia y toxicidad |
| [NCT00002347](https://clinicaltrials.gov/study/NCT00002347) | Fase 2 | Completado | 225 | Protocolo maestro de combinaciones antirretrovirales, con regímenes que incluyen saquinavir |
| [NCT00000848](https://clinicaltrials.gov/study/NCT00000848) | Fase 2 | Completado | 144 | Cambio de saquinavir en cápsula dura a cápsula blanda o a indinavir: efecto sobre el ARN viral del VIH |
| [NCT00002162](https://clinicaltrials.gov/study/NCT00002162) | Fase 2 | Completado | 140 | Comparación de dos formulaciones de saquinavir junto con otros antirretrovirales |
| [NCT00002111](https://clinicaltrials.gov/study/NCT00002111) | Fase 1 | Completado | 32 | Escalada de dosis de saquinavir durante 16 semanas: toxicidad, actividad antiviral y farmacocinética |

---

## Evidencia de Literatura

Para la predicción principal (FIV): actualmente no hay literatura relacionada disponible.

Literatura más cercana, de la predicción de SIV (evidencia preclínica indirecta):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro | Antimicrob Agents Chemother | El SIVmac239 es inhibido por indinavir, saquinavir y ritonavir con potencias similares a las del VIH-1 |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro | Antivir Ther | Sensibilidad de VIH-2, SIV y SHIV a 16 fármacos antirretrovirales aprobados |
| [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) | 2010 | Preclínico (animal) | J Infect Dis | En macacos con SIV, la terapia HAART reduce la replicación viral y la inflamación en el SNC, pero persiste el ADN viral |
| [16809296](https://pubmed.ncbi.nlm.nih.gov/16809296/) | 2006 | Estructural/preclínico | J Virol | Papel de la Thr80 invariante en la estructura y función de la proteasa del VIH-1 |

De la predicción de VIH congénito (estudios observacionales):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22938775](https://pubmed.ncbi.nlm.nih.gov/22938775/) | 2012 | Cohorte | Med Mal Infect | Eficacia y seguridad de saquinavir/ritonavir 1000/100 mg dos veces al día en mujeres embarazadas con VIH (cohorte INEMA) |
| [27242802](https://pubmed.ncbi.nlm.nih.gov/27242802/) | 2016 | Cohorte | Front Immunol | Estudio PHACS SMARTT: seguridad de la exposición intrauterina a antirretrovirales |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 96026002 | INVIRASE 500 mg comprimidos recubiertos con película (Roche Registration GmbH) | Comprimido recubierto con película | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): síndrome de QT largo (incluida la forma familiar), torsades de pointes, bloqueo auriculoventricular, insuficiencia hepática, enfermedad hepática, cirrosis, hepatitis B y C crónicas, enfermedad de la vesícula biliar, hiperglucemia, diabetes mellitus, cetoacidosis diabética, hipertrigliceridemia, deficiencia de potasio, hemofilia (incluida la forma sintomática en portadoras) y abuso/dependencia de sustancias.
- **Interacciones farmacológicas**: se registraron 100 interacciones. Entre las listadas, las de nivel **mayor** son triamcinolona, budesonida y claritromicina. Las de nivel moderado incluyen antidiabéticos (acarbosa, metformina, alogliptina, canagliflozina, clorpropamida, albiglutida), inhibidores de la bomba de protones y anti-H2 (omeprazol, rabeprazol, famotidina), corticoides (hidrocortisona, dexametasona, betametasona), loperamida, aprepitant y bisacodilo.
- **Puntos de atención de la predicción clínica**: baja biodisponibilidad oral, metabolismo mediado por P-gp/CYP3A, necesidad de potenciación con ritonavir y riesgo de prolongación del QT/PR.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (FIV) solo tiene respaldo del modelo (nivel L5): no hay ensayos ni literatura, la proteasa del FIV difiere de la del VIH-1 y es una enfermedad veterinaria. La única predicción con evidencia clínica sólida (complejo relacionado con el SIDA, L1) coincide con la indicación original, de modo que no aporta reposicionamiento. Si se quisiera priorizar algo, el SIV (L4) sería una pregunta de investigación preclínica.

**Para avanzar se necesita:**
- Estudios de susceptibilidad in vitro de la proteasa del FIV frente a saquinavir.
- Datos detallados del mecanismo de acción y de similitud con la indicación original.
- Texto de indicaciones, advertencias y contraindicaciones del prospecto de AEMPS (actualmente no disponible).
- Si se explora el VIH congénito: datos de eficacia y farmacocinética pediátrica.
- Evaluación del riesgo cardiaco (QT/PR) y del plan de manejo de interacciones antes de cualquier uso nuevo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


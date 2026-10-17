---
layout: default
title: Gemfibrozil
parent: Evidencia moderada (L3-L4)
nav_order: 373
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Gemfibrozil: nueva indicación predicha, Artritis reumatoide (nivel de evidencia L4). Indicación original: Hipertrigliceridemia (según el grafo de conocimiento"
monitor_inn: "gemfibrozil"
predicted_indications: ["rheumatoid arthritis", "multiple endocrine neoplasia", "HIV infectious disease", "hypoalphalipoproteinemia", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "methemoglobinemia, alpha type", "sclerosing cholangitis", "methemoglobin reductase deficiency"]
---

# Gemfibrozil
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Gemfibrozilo: De Hipertrigliceridemia a Artritis Reumatoide

## Resumen en Una Frase

Gemfibrozilo es un fármaco hipolipemiante (agonista de PPAR-alfa) utilizado originalmente para el tratamiento de la hipertrigliceridemia.
El modelo TxGNN predice que podría ser efectivo para **artritis reumatoide**, aunque actualmente **no hay ensayos clínicos registrados** y solo **4 publicaciones** (todas preclínicas o de revisión general) respaldan esta dirección, por lo que la evidencia es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hipertrigliceridemia (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Artritis reumatoide |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada para este informe. Según el conocimiento general, gemfibrozilo es un agonista del receptor activado por proliferadores de peroxisomas alfa (PPAR-alfa), que reduce los triglicéridos y aumenta el HDL. Su eficacia en la hipertrigliceridemia está bien establecida.

Mecanísticamente, la activación de PPAR-alfa tiene efectos antiinflamatorios (reducción de la señalización de NF-κB y modulación de las respuestas de los linfocitos T), lo que podría ser relevante en una enfermedad autoinmune e inflamatoria como la artritis reumatoide. En un modelo de artritis inducida por adyuvante en ratas, la combinación de gemfibrozilo con una dosis reducida de esteroides logró un cuadro de manejo similar al de la dosis completa de esteroides (PMID 30074417). Además, bezafibrato, un agonista pan-PPAR, atenuó la artritis experimental (PMID 41207105).

Conviene ser prudente: estos hallazgos provienen solo de modelos animales y no existe ningún ensayo clínico en humanos de gemfibrozilo en artritis reumatoide. La relación con la indicación original (metabolismo lipídico) es indirecta, a través de la vía antiinflamatoria de PPAR.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | Preclínico (modelo animal) | Modern Rheumatology | Gemfibrozilo combinado con prednisolona a dosis reducida dio un manejo similar al de la dosis completa de esteroides en artritis inducida por adyuvante en ratas |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | Preclínico (modelo animal) | International Immunopharmacology | Bezafibrato, agonista pan-PPAR, atenuó la artritis reumatoide experimental mediante modulación de vías inflamatorias, con énfasis en PPAR-γ |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | Preclínico (mecanístico) | Journal of Immunology | Estudio sobre la regulación de Foxp3 en linfocitos T reguladores por óxido nítrico; relevancia indirecta para la autoinmunidad |
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | Revisión | American Journal of Clinical Dermatology | Revisión sobre el eritema palmar y sus causas fisiológicas y sistémicas; relevancia indirecta |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61051 | TRIALMIN 900 mg comprimidos recubiertos con película | Comprimido recubierto | No disponible |
| 62503 | GEMFIBROZILO TARBIS 600 mg comprimidos recubiertos con película EFG | Comprimido recubierto | No disponible |
| 61830 | GEMFIBROZILO STADA 600 mg comprimidos EFG | Comprimido recubierto con película | No disponible |
| 61831 | GEMFIBROZILO STADA 900 mg comprimidos EFG | Comprimido recubierto con película | No disponible |
| 58832 | LOPID 600 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |

Se muestran 5 de las 8 autorizaciones vigentes.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): enfermedad hepática, enfermedad de la vesícula biliar, colelitiasis, colecistolitiasis, coledocolitiasis, colangitis biliar primaria, trombocitopenia, anemia (incluida la macrocítica), leucopenia, insuficiencia renal y síndrome de Reynolds.
- **Interacciones farmacológicas**: se identificaron 129 interacciones. Entre las de nivel **mayor** figuran:
  - Estatinas: rosuvastatina y simvastatina (riesgo de miopatía).
  - Antidiabéticos: pioglitazona y repaglinida.
  - Loperamida y eluxadolina.
  
  Entre las de nivel moderado se incluyen diversas insulinas, clorpropamida, tolazamida, nateglinida, rosiglitazona, ácido quenodesoxicólico y rifaximina.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN para artritis reumatoide es alta (99.90%), pero la evidencia se limita a modelos animales y estudios mecanísticos, sin ensayos en humanos. Además, el perfil de interacciones y las contraindicaciones hepáticas, biliares y hematológicas exigen cautela en pacientes con artritis reumatoide, que suelen recibir múltiples fármacos.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción y del eje PPAR-alfa en la inflamación sinovial.
- Estudios preclínicos adicionales con gemfibrozilo específicamente (no solo con otros fibratos).
- Un ensayo clínico exploratorio de Fase 2 en artritis reumatoide.
- Revisión de las advertencias y contraindicaciones del prospecto de la AEMPS, aún no disponibles.
- Evaluación de interacciones con los fármacos habituales en artritis reumatoide (metotrexato, corticoides, entre otros).

---

### Nota sobre otras indicaciones predichas

Entre las demás predicciones, la **infección por VIH** tiene mayor respaldo (nivel L2, **Proceed with Guardrails**). Se trata de un uso derivado de la indicación lipídica original: tratamiento de la hipertrigliceridemia asociada a inhibidores de la proteasa. Dispone de un estudio aleatorizado doble ciego (PMID 12409741) y un ensayo de fase 1 completado (NCT00039663). Sus principales precauciones son las interacciones con inhibidores de la proteasa y estatinas, y el riesgo de miopatía.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


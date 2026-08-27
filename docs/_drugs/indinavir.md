---
layout: default
title: Indinavir
parent: 僅模型預測 (L5)
nav_order: 145
evidence_level: L5
indication_count: 7
---

# Indinavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Indinavir: De Infección por VIH/SIDA a Infección por el Virus de Inmunodeficiencia Símica (SIV)

## Resumen en Una Frase

Indinavir es un inhibidor de la proteasa del VIH-1, aprobado originalmente (como Crixivan®, 1996) para el tratamiento de la infección por VIH/SIDA. El modelo TxGNN predice que también sería relevante para la **infección por el virus de inmunodeficiencia símica (SIV)**, un modelo animal de infección retroviral usado en investigación preclínica, respaldado actualmente por **12 publicaciones** pero **sin ningún ensayo clínico en humanos**.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Infección por VIH/SIDA (Crixivan®, aprobado 1996) |
| Nueva Indicacion Predicha | Infección por el virus de inmunodeficiencia símica (SIV) |
| Puntaje de Prediccion TxGNN | 99.99% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en Espana | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

El campo formal de mecanismo de acción (MOA) está marcado como dato faltante en la base, pero la propia evidencia del paquete confirma que Indinavir es un **inhibidor de la proteasa aspártica del VIH-1**, pieza central de los esquemas HAART de los años 90, hoy retirado del mercado en la mayoría de países (incluida España) por la aparición de fármacos de nueva generación con menor toxicidad.

La proteasa del SIV comparte alta homología estructural con la proteasa del VIH-1, lo que constituye la base mecanística de la predicción. Dos estudios in vitro del propio paquete lo demuestran directamente: PMID 12709355 midió concentraciones efectivas de indinavir similares para inhibir SIVmac239 (39±8 nM) y VIH-1 (66±4 nM), y PMID 15040537 confirmó actividad cruzada de indinavir frente a VIH-2, SIV y SHIV.

Sin embargo, es importante señalar la limitación traslacional: **el SIV es una enfermedad de primates no humanos**, utilizada como modelo preclínico para estudiar profilaxis y patogénesis del VIH, no una indicación clínica humana. La evidencia disponible es enteramente animal/in vitro, sin ningún ensayo clínico que traduzca este hallazgo a pacientes.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19240457](https://pubmed.ncbi.nlm.nih.gov/19240457/) | 2009 | Estudio animal (PEP) | AIDS | Profilaxis post-exposición vaginal con AZT+3TC+indinavir en macacas, evaluando prevención de transmisión de SIV |
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro/Farmacodinamia | Antimicrob Agents Chemother | Comparación directa de susceptibilidad de SIV vs VIH-1 a indinavir, saquinavir y ritonavir; potencia similar entre ambos virus |
| [12804006](https://pubmed.ncbi.nlm.nih.gov/12804006/) | 2003 | Mecanismo farmacológico in vitro | AIDS Res Hum Retroviruses | HAART (AZT+3TC+indinavir) modula expresión de P-glicoproteína y cinasas celulares en modelo primate de SIDA |
| [20868521](https://pubmed.ncbi.nlm.nih.gov/20868521/) | 2010 | Estudio animal | Retrovirology | Efecto de HAART de corto plazo sobre carga de SIV en tejidos de macacos, según momento de inicio |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro/Farmacodinamia | Antivir Ther | Susceptibilidad de VIH-2, SIV y SHIV a 16 antirretrovirales aprobados, incluido indinavir |
| [11689641](https://pubmed.ncbi.nlm.nih.gov/11689641/) | 2001 | Estudio animal | J Virol | Defecto hematopoyético persistente en médula ósea de macacos con SHIV pese a HAART eficaz |
| [15378436](https://pubmed.ncbi.nlm.nih.gov/15378436/) | 2004 | Estudio animal | J Infect Dis | Respuesta de células T Vγ2Vδ2+ en coinfección micobacteriana de macacos con SIV bajo tenofovir±indinavir |
| [11507214](https://pubmed.ncbi.nlm.nih.gov/11507214/) | 2001 | Estudio animal | J Virol | Antirretrovirales restauran inmunidad anti-Mycobacterium y controlan enfermedad tipo tuberculosis en macacos SIV/BCG |
| [14610172](https://pubmed.ncbi.nlm.nih.gov/14610172/) | 2003 | Estudio animal | J Virol | Cinética de proliferación linfocitaria en infección primaria por SIV, efecto de profilaxis temprana con AZT+3TC+indinavir |
| [22615988](https://pubmed.ncbi.nlm.nih.gov/22615988/) | 2012 | No clasificado | PLoS One | Impacto de HAART iniciada en fase crónica o post-exposición sobre infección por SIV en órganos genitales masculinos |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
Toda la evidencia disponible es preclínica (modelos animales de macacos) o in vitro; no existe ningún ensayo clínico en humanos para esta indicación, y el SIV en sí no es una enfermedad humana, sino un modelo de investigación para VIH. El valor traslacional directo es limitado.

**Para avanzar se necesita:**
- Identificar una indicación humana equivalente (p. ej., profilaxis/tratamiento de VIH) donde trasladar la evidencia de homología SIV/VIH-1, en vez de tratar el SIV como indicación final
- Datos formales de mecanismo de acción (MOA) y ficha técnica TFDA (advertencias/contraindicaciones), actualmente bloqueantes según el registro de vacíos de datos (DG001, DG002)
- Nota de priorización: el candidato de rango 5 en este mismo paquete, **"AIDS related complex"**, ya cuenta con nivel de evidencia L1, 6 ensayos clínicos (incluyendo Fase 1–4) y recomendación "Proceed with Guardrails" — es un candidato mucho más avanzado y debería priorizarse sobre esta indicación de rango 1 basada solo en modelo animal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


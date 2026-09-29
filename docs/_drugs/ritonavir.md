---
layout: default
title: Ritonavir
parent: Evidencia moderada (L3-L4)
nav_order: 472
evidence_level: L4
indication_count: 3
---

# Ritonavir
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

# Ritonavir: De Infección por VIH-1 a Infección por el Virus de la Inmunodeficiencia Simia

## Resumen en Una Frase

Ritonavir es un inhibidor de la proteasa del VIH-1, ya utilizado en el tratamiento antirretroviral humano.
El modelo TxGNN predice que podría ser efectivo para la **infección por el virus de la inmunodeficiencia simia (VIS)**,
con **0 ensayos clínicos** y **12 publicaciones** (estudios in vitro y en animales, la mayoría con regímenes combinados) que respaldan esta dirección solo de forma indirecta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | VIH-1 (los registros de la AEMPS no incluyen el texto de indicación) |
| Nueva Indicación Predicha | Infección por el virus de la inmunodeficiencia simia |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, ritonavir inhibe la proteasa del VIH-1, y además es un potente inhibidor de CYP3A4, por lo que se emplea también como potenciador farmacocinético de otros inhibidores de proteasa. Su eficacia en la infección por VIH-1 está establecida, y mecanísticamente podría ser aplicable al VIS.

El VIS es el equivalente en primates no humanos del VIH y ambos son lentivirus con proteasas muy parecidas. Un estudio in vitro (PMID 12709355) mostró que el VIS (cepa mac239) es inhibido por ritonavir con una concentración efectiva del 50% de unos 13 nM, frente a unos 25 nM para el VIH-1. Otro estudio de sensibilidad (PMID 15040537) confirma que el VIS responde de forma variable a los fármacos anti-VIH-1.

Conviene interpretar esta predicción con cautela. Los estudios en macacos con terapia antirretroviral combinada muestran que el principio antiviral funciona in vivo, pero no permiten aislar la contribución de ritonavir. Además, el VIS es un modelo animal del VIH y ritonavir ya está aprobado para el VIH-1, así que esto **no constituye una oportunidad de reposicionamiento distinta para uso humano**. El puntaje alto de TxGNN (0.999) es una predicción del modelo, no evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro | Antimicrob Agents Chemother | El VIS (SIVmac239) fue inhibido por indinavir, saquinavir y ritonavir (ritonavir: ~13 nM), con potencias comparables a las del VIH-1 |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro | Antivir Ther | Comparó 16 fármacos aprobados contra VIH-2, VIS y SHIV; aporta datos para tratamiento y profilaxis posexposición |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Estudio animal | J Virol Methods | Macacos con SHIV 89.6P tratados por vía oral con AZT, 3TC y lopinavir/ritonavir durante 28 días; se evaluó el efecto sobre el subconjunto CD8 |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Estudio animal | PLoS Pathog | Régimen multifármaco intensificado en macacos con SIVmac251; supresión viral prolongada y restricción del reservorio viral |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Estudio animal | J Virol | Decaimiento viral rápido en macacos infectados con SIVmac251 tratados con terapia antirretroviral cuádruple |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Estudio animal | PLoS One | Macacos rhesus con VIS tratados con cART intensiva más el inhibidor de HDAC SAHA, como modelo de reservorios virales |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Estudio animal / Revisión | mBio | Las infecciones por lentivirus persisten en el cerebro a pesar de la terapia antirretroviral eficaz |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Estudio animal | Microbes Infect | Construcción de un SHIV con proteasa de VIH-1, útil para probar in vivo inhibidores de proteasa |
| [12186895](https://pubmed.ncbi.nlm.nih.gov/12186895/) | 2002 | In vitro (mecanístico) | J Virol | La proteasa viral procesa la proteína Vif del VIH-1 dentro del virión; relevancia indirecta |
| [9875393](https://pubmed.ncbi.nlm.nih.gov/9875393/) | 1998 | In vitro | Antivir Chem Chemother | Derivado de fluoroquinolona (K-12) activo contra VIH-1 (incluidas cepas resistentes a ritonavir), VIH-2 y VIS; no es específico de ritonavir |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 196016009 | NORVIR 100 MG polvo para suspensión oral | Polvo para solución oral | AbbVie Deutschland GmbH & Co. KG |
| 81039 | RITONAVIR ACCORD 100 MG comprimidos recubiertos con película EFG | Comprimido recubierto con película | Accord Healthcare S.L.U. |
| 96016005 | NORVIR 100 MG comprimidos recubiertos con película | Comprimido recubierto con película | AbbVie Deutschland GmbH & Co. KG |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia se limita a estudios in vitro y en animales, con regímenes combinados que no permiten aislar el efecto de ritonavir, y no hay ensayos clínicos. Como ritonavir ya está aprobado para el VIH-1 y el VIS es un modelo animal, esta predicción no ofrece una nueva vía terapéutica en humanos.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank
- Advertencias y contraindicaciones del prospecto de la AEMPS, que bloquean el cribado de seguridad
- Confirmar la indicación aprobada en España, ya que los registros no incluyen el texto de indicación
- Estudios que evalúen ritonavir de forma individual en modelos de VIS, o una aclaración de si el objetivo real es veterinario o de investigación

**Otras predicciones del modelo (para información):**
- *Síndrome de inmunodeficiencia adquirida felina*: nivel L4, decisión Hold. El único ensayo vinculado (NCT02770508, fase 4, n=145, completado) estudia darunavir potenciado en VIH-1 humano, por lo que es evidencia indirecta. No se aportaron datos veterinarios.
- *Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y disminución de la sustancia blanca cortical*: nivel L5, decisión Hold. No se identificó ningún vínculo mecanístico, y el puntaje alto puede ser un artefacto del grafo de conocimiento.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


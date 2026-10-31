---
layout: default
title: Lamivudine
parent: Solo predicción del modelo (L5)
nav_order: 446
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-31
monitor_inn: "Lamivudine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "chronic hepatitis C virus infection"]
description: "Lamivudine: nueva indicación predicha, Síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome) (nivel de evidencia L5). Indicación original: No consta en los datos …"
---

# Lamivudine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Lamivudine: Síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome)
{: .text-alpha }

## Resumen en Una Frase

Lamivudina es un análogo nucleosídico inhibidor de la transcriptasa inversa, utilizado originalmente para el tratamiento de la infección crónica por el virus de la hepatitis B, la infección por VIH y el sida.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina**, sin ensayos clínicos registrados y con **3 publicaciones** (estudios en gatos y en sistemas in vitro) que respaldan esta dirección.
Se trata de una predicción de valor veterinario, ya que la indicación humana equivalente (VIH) ya está cubierta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina (feline acquired immunodeficiency syndrome) |
| Puntaje de Predicción TxGNN | 0.9993 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 14) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base consultada. Según la información conocida, lamivudina es un inhibidor nucleosídico de la transcriptasa inversa (ITIN) que actúa por terminación de cadena en la síntesis del ADN viral. Su eficacia en VIH y hepatitis B está bien establecida.

El virus de la inmunodeficiencia felina (FIV) es un lentivirus cuya transcriptasa inversa guarda relación con la del VIH-1, por lo que compartir diana es plausible. Los estudios recuperados evalúan regímenes antirretrovirales en gatos infectados, incluida la combinación de zidovudina, lamivudina y abacavir, con supresión de la replicación de FIV in vitro.

Sin embargo, esta es evidencia veterinaria y no una nueva indicación en humanos. Dado que la indicación original (VIH) ya cubre el equivalente humano, el valor de reposicionamiento para la medicina humana es mínimo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22816032](https://pubmed.ncbi.nlm.nih.gov/22816032/) | 2012 | Cohorte | Viruses | Evaluación de protocolos antirretrovirales (zidovudina sola o combinada con interferón-α, lamivudina o ácido valproico) en gatos con FIV en fase asintomática tardía, con seguimiento de un año de carga viral y cociente CD4+/CD8+ |
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | Cohorte | Journal of Feline Medicine and Surgery | Seguimiento de terapia antirretroviral a largo plazo (5-6 años) en gatos infectados con FIV, iniciada con zidovudina |
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Estudio animal / in vitro | Antiviral Research | La combinación de zidovudina, lamivudina y abacavir suprime la replicación de FIV in vitro; el modelo felino se usa como análogo del VIH |

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de medicamentos con un único principio activo o asociación de dos, sin autorizaciones canceladas):

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 99114003 | Zeffix 5 mg/ml solución oral | Solución oral | No disponible |
| 09596009 | Lamivudina Teva Pharma B.V. 300 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 96015004 | Epivir 150 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 75887 | Lamivudina Normon 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 78775 | Lamivudina Accord 150 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |

## Consideraciones de Seguridad

- **Enfermedades con contraindicación o precaución según el grafo de conocimiento** (no proviene del prospecto): insuficiencia hepática, enfermedad renal, pancreatitis, enfermedad hepática y hepática grasa (incluida esteatohepatitis no alcohólica), enfermedad de la vesícula biliar, miopatías y miositis (incluida dermatomiositis), neutropenia, agranulocitosis, anemia (incluida la macrocítica), hipertrigliceridemia, obesidad y acidosis láctica, entre otras.
- **Interacciones farmacológicas**: se identificaron 100 interacciones. Las de nivel moderado incluyen lactitol, manitol, naltrexona, orlistat y sorbitol. Otras, de nivel no clasificado, incluyen metformina, cimetidina, anfotericina B, vancomicina, omeprazol, pantoprazol y lansoprazol, entre otras.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Otras Predicciones Evaluadas (Contexto)

| Indicación Predicha | Puntaje TxGNN | Nivel | Valoración |
|------|------|------|------|
| Infección por virus de inmunodeficiencia simia | 0.9993 | L3 | Solo modelos preclínicos en macacos de VIH; refleja la indicación VIH ya existente |
| Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y disminución de la sustancia blanca cortical | 0.9993 | L5 | Sin vínculo mecanístico ni evidencia; Hold |
| Hiperlipidemia combinada familiar (término obsoleto) | 0.9963 | L5 | Término obsoleto en la ontología, predicción poco fiable; Hold |
| Infección crónica por virus de la hepatitis C | 0.9911 | L4 | Sin actividad establecida frente al VHC; la literatura son revisiones que tratan VHB y VHC conjuntamente; Hold |

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal se apoya únicamente en estudios veterinarios y preclínicos, sin ensayos clínicos, y no aporta una indicación humana nueva, puesto que el VIH ya es una indicación original de lamivudina. El interés se limita a una pregunta de investigación.

**Para avanzar se necesita:**
- Datos del mecanismo de acción desde DrugBank
- Advertencias y contraindicaciones oficiales del prospecto de la AEMPS (dato bloqueante para el cribado de seguridad)
- Textos de indicación aprobada de las autorizaciones españolas
- Determinar si existe interés veterinario real (ensayos controlados en felinos) o si se debe priorizar otra indicación humana con mayor respaldo
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


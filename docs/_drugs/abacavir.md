---
layout: default
title: Abacavir
parent: Evidencia moderada (L3-L4)
nav_order: 11
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Abacavir: nueva indicación predicha, Síndrome de inmunodeficiencia adquirida felina (nivel de evidencia L4). Indicación original: VIH / SIDA (según el grafo de conocimiento"
monitor_inn: "ABACAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Abacavir
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

# Abacavir: De Infección por VIH/SIDA a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Abacavir es un inhibidor nucleosídico de la transcriptasa inversa, originalmente utilizado para el tratamiento de la infección por VIH y el SIDA.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina**, aunque se trata de una indicación veterinaria sin relevancia clínica humana directa.
La evidencia es muy limitada: **0 ensayos clínicos** y **1 publicación** preclínica que respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | VIH / SIDA (según el grafo de conocimiento; el texto de indicación de las autorizaciones españolas no está disponible) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99,79 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento general de la clase, abacavir es un inhibidor nucleosídico de la transcriptasa inversa (ITIN) con actividad frente al VIH-1 y VIH-2. Su eficacia en la infección por VIH está establecida, y mecanísticamente podría ser aplicable a otros lentivirus.

El virus de la inmunodeficiencia felina (FIV) es un lentivirus cuya transcriptasa inversa está biológicamente emparentada con la del VIH, por lo que existe una justificación mecanística plausible. Sin embargo, esta relación se infiere del conocimiento de la clase farmacológica y no de los datos suministrados.

El único estudio disponible (PMID 11684314, 2002) evalúa la combinación zidovudina/lamivudina/abacavir en un modelo *in vitro*, por lo que no es posible aislar la contribución de abacavir por sí solo. El puntaje elevado de TxGNN refleja probablemente la similitud con la indicación ya existente (VIH), y no una nueva oportunidad terapéutica para pacientes humanos.

Otras predicciones del modelo siguen un patrón similar: la infección por el virus de inmunodeficiencia símica (SIV; puntaje 99,79 %, evidencia L4) es un modelo en primates no humanos con un único estudio de susceptibilidad *in vitro*, y un trastorno del neurodesarrollo raro con ataxia, ausencia del habla y reducción de la sustancia blanca cortical (puntaje 99,78 %, evidencia L5) carece de ensayos, literatura y vínculo mecanístico evidente.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Estudio preclínico (modelo animal/*in vitro*) | Antiviral Research | Efecto combinado de zidovudina, lamivudina y abacavir en la supresión de la replicación del FIV; el FIV en el gato doméstico se considera un modelo animal de la infección por VIH |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 85319 | Abacavir Accord 300 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 99112001 | Ziagen 300 mg comprimidos recubiertos con película | Comprimido recubierto | No disponible |
| 84740 | Abacavir Tarbis 300 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 86115 | Abacavir Zentiva 300 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 99112002 | Ziagen 20 mg/ml solución oral | Solución oral | No disponible |

Hay 8 autorizaciones vigentes en total (todas de principio activo único); se muestran las 5 principales.

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación o precaución según el grafo de conocimiento** (no proviene del texto del prospecto): insuficiencia hepática, enfermedad hepática, hígado graso y esteatohepatitis no alcohólica, enfermedad renal, pancreatitis, enfermedad de la vesícula biliar, miopatía y miositis (incluida dermatomiositis), neutropenia, agranulocitosis, anemia (incluida la macrocítica), hipertrigliceridemia, obesidad y acidosis láctica.
- **Interacciones farmacológicas**: se registran 93 interacciones. Entre las de nivel moderado figuran naltrexona y orlistat; otras (por ejemplo metformina, omeprazol, morfina, prednisona, vancomicina o anfotericina B) no tienen nivel de gravedad clasificado.
- **Riesgo de hipersensibilidad asociado a HLA-B*57:01**: es un riesgo conocido de abacavir, que debería evaluarse antes de cualquier uso en una población nueva.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación predicha es veterinaria, está respaldada solo por un estudio preclínico de combinación y no representa una oportunidad terapéutica para pacientes humanos. El puntaje alto del modelo parece reflejar la similitud con la indicación original de VIH.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) desde DrugBank
- Advertencias y contraindicaciones oficiales del prospecto de la AEMPS
- Definir si existe interés real en una indicación veterinaria o si el modelo debe usarse solo como referencia de investigación
- Evidencia que aísle el efecto de abacavir de forma individual, fuera de combinaciones
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


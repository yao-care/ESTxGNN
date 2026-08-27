---
layout: default
title: Frovatriptan
parent: 僅模型預測 (L5)
nav_order: 129
evidence_level: L5
indication_count: 3
---

# Frovatriptan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Frovatriptán: De Migraña Aguda a Migraña con Aura del Tronco Encefálico

## Resumen en Una Frase

Frovatriptán es un agonista selectivo de receptores 5-HT1B/1D de la clase triptán, utilizado originalmente para el tratamiento agudo de la migraña con o sin aura. El modelo TxGNN predice que podría ser efectivo para **Migraña con Aura del Tronco Encefálico**, con **19 publicaciones** que respaldan la plausibilidad mecanicista, aunque **sin ensayos clínicos registrados específicamente en esta subpoblación**.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tratamiento agudo de la migraña (con o sin aura), según literatura de referencia |
| Nueva Indicación Predicha | Migraña con Aura del Tronco Encefálico |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## Por qué es Razonable esta Predicción?

Frovatriptán es un agonista selectivo de los receptores serotoninérgicos 5-HT1B/1D. Su mecanismo de acción produce vasoconstricción de las arterias intracraneales y extracerebrales, e inhibe la liberación de péptidos inflamatorios como el CGRP (péptido relacionado con el gen de la calcitonina) en el sistema trigémino-vascular, interrumpiendo así el ataque de migraña.

La migraña con aura del tronco encefálico (denominada anteriormente "migraña de tipo basilar") es un subtipo de migraña cuyo aura se origina en la circulación vertebrobasilar/tronco encefálico. Dado que el mecanismo antimigrañoso de frovatriptán es común a todos los subtipos de migraña, existe una lógica mecanicista para su eficacia también en este subtipo.

Sin embargo, es necesario señalar una consideración de seguridad relevante: precisamente por su mecanismo vasoconstrictor, la migraña con aura del tronco encefálico ha sido tradicionalmente listada como contraindicación relativa o absoluta para los triptanes en numerosos prospectos y guías clínicas, por el riesgo teórico de agravar la isquemia en el territorio vertebrobasilar. Esto significa que la plausibilidad mecanicista de eficacia coexiste con una señal de riesgo mecanicista que debe evaluarse por separado, y explica por qué la evidencia disponible (revisada abajo) se centra en la migraña con aura en general, sin estudios que hayan enrolado específicamente esta subpoblación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados específicamente para migraña con aura del tronco encefálico.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | Metaanálisis | The journal of headache and pain | Compara la eficacia de frovatriptán frente a rizatriptán, zolmitriptán y almotriptán en migraña con aura |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guía/Evaluación | Headache | Evaluación actualizada de la evidencia de fármacos para el tratamiento agudo de la migraña (American Headache Society) |
| [24867847](https://pubmed.ncbi.nlm.nih.gov/24867847/) | 2014 | Metaanálisis | Neurological Sciences | Eficacia de frovatriptán y otros triptanes en migraña aguda, en sujetos de peso normal y obesos |
| [23695053](https://pubmed.ncbi.nlm.nih.gov/23695053/) | 2013 | Metaanálisis | Neurological Sciences | Eficacia de frovatriptán y otros triptanes en migraña aguda, en sujetos hipertensos y normotensos |
| [18457529](https://pubmed.ncbi.nlm.nih.gov/18457529/) | 2008 | ECA | Expert Review of Neurotherapeutics | Frovatriptán para tratamiento agudo de migraña con o sin aura, indicado también en prevención de migraña menstrual predecible |
| [27757013](https://pubmed.ncbi.nlm.nih.gov/27757013/) | 2016 | Revisión | Drug Design, Development and Therapy | Revisión de eficacia de frovatriptán, triptán de segunda generación con vida media prolongada (~26h) |
| [22900951](https://pubmed.ncbi.nlm.nih.gov/22900951/) | 2012 | Revisión | CNS Drugs | Revisión de farmacología, eficacia y tolerabilidad de frovatriptán en migraña aguda |
| [22644173](https://pubmed.ncbi.nlm.nih.gov/22644173/) | 2012 | ECA (subanálisis) | Neurological Sciences | Comparación frovatriptán vs. zolmitriptán específicamente en subgrupo de pacientes con migraña con aura (n=18) |
| [27910087](https://pubmed.ncbi.nlm.nih.gov/27910087/) | 2017 | Revisión | Headache | Revisión de opciones de tratamiento para migraña menstrual |
| [24363238](https://pubmed.ncbi.nlm.nih.gov/24363238/) | 2014 | ECA | Cephalalgia | Combinación frovatriptán + dexketoprofeno vs. frovatriptán solo en migraña con o sin aura |

**Nota:** La evidencia disponible se refiere a migraña con aura en general; no se han identificado estudios que hayan enrolado o excluido específicamente pacientes con aura del tronco encefálico (subtipo raro y tradicionalmente excluido de ensayos con triptanes por motivos de seguridad).

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un sólido cuerpo de evidencia (metaanálisis y ECAs) sobre la eficacia de frovatriptán en migraña con aura en general, y el mecanismo de acción es coherente con la nueva indicación. Sin embargo, la migraña con aura del tronco encefálico es un subtipo con antecedente de contraindicación relativa para triptanes por riesgo vasoconstrictor teórico, y no existe evidencia clínica directa en esta subpoblación específica, por lo que no se recomienda un "Go" sin salvaguardas adicionales.

**Para avanzar se necesita:**
- Datos del prospecto/ficha técnica de la AEMPS sobre advertencias y contraindicaciones (actualmente vacío — brecha bloqueante, DG001)
- Datos detallados del mecanismo de acción (MOA) desde DrugBank (brecha de alta prioridad, DG002)
- Evaluación específica del riesgo vascular en aura del tronco encefálico antes de cualquier uso clínico o diseño de ensayo
- Confirmación de vías de administración disponibles/requeridas (actualmente sin determinar)
- Dado que el fármaco no está comercializado en España (0 autorizaciones), definir la vía regulatoria si se plantea su introducción

**Nota adicional:** El modelo TxGNN generó otras dos predicciones de baja confianza para este fármaco (atrophoderma vermiculata y ulerythema ophryogenesis, ambas enfermedades de queratosis folicular), sin ningún respaldo de ensayos clínicos ni literatura y sin relación mecanicista conocida con el perfil serotoninérgico de frovatriptán. Ambas se clasifican como **L5 / Hold** y no se desarrollan en este informe.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---


---
layout: default
title: Albendazole
parent: Evidencia alta (L1-L2)
nav_order: 23
evidence_level: L2
indication_count: 3
---

# Albendazole
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **3** 
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

# Albendazol: De Antihelmíntico (Indicación Autorizada No Registrada) a Equinococosis Alveolar

## Resumen en Una Frase

Albendazol es un antihelmíntico de amplio espectro. En España se comercializa como ESKAZOLE 400 mg comprimidos, aunque el registro no incluye el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **equinococosis alveolar**, con **5 ensayos clínicos** (solo 1 directamente relevante) y **20 publicaciones** que respaldan esta dirección. Además, un consenso de expertos ya lo recomienda para esta enfermedad.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en el registro de AEMPS (fármaco antihelmíntico) |
| Nueva Indicación Predicha | Equinococosis alveolar |
| Puntaje de Predicción TxGNN | 99,97% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

DrugBank no aporta datos del mecanismo de acción. Según la farmacología general, el albendazol, a través de su metabolito sulfóxido, se une a la beta-tubulina del parásito. Así bloquea la polimerización de los microtúbulos y reduce la captación de glucosa. Este mecanismo es plausible frente a las metacestodas de *Echinococcus multilocularis*, el agente de la equinococosis alveolar.

En esta enfermedad el albendazol es parasitostático y no parasiticida. Frena el crecimiento de la lesión, pero no elimina al parásito, por lo que el tratamiento suele ser prolongado y supresor. Se emplea sobre todo cuando la cirugía no es posible o como complemento de ella.

La indicación original no figura en el registro, pero la clase antihelmíntica y la nueva indicación son coherentes. La equinococosis alveolar es una infección por larvas de cestodos, sobre la que actúa este mecanismo antiparasitario. El consenso de expertos (PMID 19931502) ya respalda su uso, lo que concuerda con el puntaje muy alto de TxGNN.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Fase 2 | Completado | 194 | Tratamiento con albendazol en equinococosis alveolar en estadio temprano (foco descubierto en Kirguistán). Es la evidencia clínica directa; no se indican aleatorización ni criterios de valoración. |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | N/A | Completado | 50 | Estudio prospectivo (EchinoVISTA) de viabilidad del parásito y marcadores de seguimiento en pacientes tratados con albendazol. Ayuda a decidir cuándo retirar el tratamiento, pero no evalúa eficacia. |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | N/A | Desconocido | 24 | ECA de albendazol adyuvante tras resección de quiste hidatídico pulmonar frente a placebo. Es equinococosis quística, por lo que la evidencia es indirecta y la muestra pequeña. |
| [NCT05824442](https://clinicaltrials.gov/study/NCT05824442) | N/A | Reclutando | 43 | Evaluación de una PCR cuantitativa multiplex para el diagnóstico de equinococosis. No aporta evidencia terapéutica. |
| [NCT07176598](https://clinicaltrials.gov/study/NCT07176598) | N/A | Completado | 1 | Reporte de caso de quiste hidatídico intramuscular mal diagnosticado. No es equinococosis alveolar ni evidencia de eficacia. |

---

## Evidencia de Literatura

No hay ECA entre las publicaciones recuperadas. Se priorizan el consenso y las revisiones, seguidos de un estudio preclínico y uno de cohorte.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | Consenso de expertos | Acta Trop | Actualiza las recomendaciones de la OMS (WHO-IWGE) sobre diagnóstico, tratamiento y seguimiento de la equinococosis quística y alveolar. |
| [39254012](https://pubmed.ncbi.nlm.nih.gov/39254012/) | 2024 | Revisión | Tidsskr Nor Legeforen | La enfermedad simula un tumor maligno hepático. El tratamiento suele combinar resección quirúrgica amplia y uso prolongado de antiparasitarios. |
| [34161992](https://pubmed.ncbi.nlm.nih.gov/34161992/) | 2021 | Revisión | Semin Liver Dis | Revisión de la equinococosis alveolar hepática, una zoonosis rara y grave que resurge en zonas endémicas y aparece en países antes no afectados. |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Revisión | World J Gastroenterol | Manejo de la equinococosis hepática; la cirugía es la piedra angular del tratamiento. |
| [36974024](https://pubmed.ncbi.nlm.nih.gov/36974024/) | 2022 | Revisión | Zhongguo Xue Xi Chong Bing Fang Zhi Za Zhi | En pacientes que rechazan la cirugía, llegan tarde a ella o no la toleran, el albendazol puede retrasar la progresión. |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Revisión | Clin Microbiol Rev | Avances del siglo XXI en genética, diagnóstico y tratamiento de la equinococosis. Destaca China occidental como zona de mayor endemicidad. |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Revisión | Acta Trop | Ninguna opción no quirúrgica ha reemplazado aún al albendazol y al mebendazol. Se buscan tratamientos más seguros y eficaces. |
| [39508157](https://pubmed.ncbi.nlm.nih.gov/39508157/) | 2024 | Revisión | Parasitology | El albendazol es el único tratamiento antiparasitario actual, no es parasiticida y puede causar efectos adversos graves. Se explora el reposicionamiento de otros fármacos, como la pironaridina. |
| [38501660](https://pubmed.ncbi.nlm.nih.gov/38501660/) | 2024 | Estudio preclínico | Antimicrob Agents Chemother | En ratas con modelo de equinococosis alveolar hepática, se evaluaron formulaciones que mejoran la baja solubilidad y biodisponibilidad oral del albendazol. |
| [39977361](https://pubmed.ncbi.nlm.nih.gov/39977361/) | 2025 | Cohorte descriptiva | Swiss Med Wkly | Análisis descriptivo de los casos de equinococosis alveolar en el cantón de Ginebra entre 2010 y 2021. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 60407 | ESKAZOLE 400 MG COMPRIMIDOS (Glaxosmithkline S.A.) | Comprimido | No especificada en el registro |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un ensayo de Fase 2 completado (n=194) específico de equinococosis alveolar y un consenso de expertos que ya recomienda el albendazol, lo que da un nivel de evidencia L2. No hay ECA de Fase 3 ni datos de seguridad de la ficha técnica, y el efecto es parasitostático, no curativo.

**Para avanzar se necesita:**
- Obtener y analizar la ficha técnica de AEMPS (advertencias y contraindicaciones), un dato de seguridad hoy sin cubrir.
- Confirmar la indicación autorizada en España, ausente del registro.
- Obtener los resultados publicados de NCT07182305 (diseño, aleatorización y criterios de valoración).
- Completar los datos de mecanismo de acción desde DrugBank.
- Definir un plan de monitoreo de seguridad para el tratamiento prolongado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


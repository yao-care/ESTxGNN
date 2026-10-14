---
layout: default
title: Albendazole
parent: Evidencia alta (L1-L2)
nav_order: 29
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

# Albendazol: De Equinococosis Quística a Equinococosis Alveolar

## Resumen en Una Frase

Albendazol es un antiparasitario del grupo de los bencimidazoles, utilizado originalmente para tratar la equinococosis quística (hidatidosis) y la cisticercosis.
El modelo TxGNN predice que podría ser efectivo para la **equinococosis alveolar**, con **3 ensayos clínicos** y **20 publicaciones** que respaldan actualmente esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Equinococosis quística, cisticercosis (según el grafo de conocimiento; el texto de indicación autorizado en España no está disponible) |
| Nueva Indicación Predicha | Equinococosis alveolar |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Aunque no se dispone de un campo formal de mecanismo de acción, los datos compilados indican que albendazol es un bencimidazol que se une a la beta-tubulina del parásito e inhibe la polimerización de los microtúbulos. Esto altera la captación de glucosa y el metabolismo energético de los helmintos.

*Echinococcus multilocularis* (causante de la equinococosis alveolar) está estrechamente emparentado con *E. granulosus* (causante de la equinococosis quística, indicación original). Por ello, el mismo mecanismo antiparasitario es aplicable. De hecho, albendazol ya es la base del tratamiento médico de la equinococosis alveolar, según consensos de expertos y revisiones, normalmente junto con cirugía.

Debe matizarse que su acción es **parasitostática** (frena el parásito), no curativa. Esto es relevante para decidir cuánto tiempo debe mantenerse el tratamiento.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Fase 2 | Completado | 194 | Albendazol en equinococosis alveolar en estadio temprano, detectada por cribado ecográfico en Kirguistán |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | No aplica | Completado | 50 | Viabilidad del parásito y marcadores de seguimiento en pacientes con equinococosis alveolar hepática tratados con albendazol |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | No aplica | Desconocido | 24 | Ensayo aleatorizado de albendazol adyuvante tras resección de quiste hidatídico pulmonar (enfermedad quística, solo relevancia indirecta) |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | Revisión | Acta Tropica | Consenso de expertos sobre diagnóstico, tratamiento y seguimiento de la equinococosis quística y alveolar |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Revisión | Clinical Microbiology Reviews | Avances del siglo XXI en genética, diagnóstico y tratamiento de la equinococosis |
| [34161992](https://pubmed.ncbi.nlm.nih.gov/34161992/) | 2021 | Revisión | Seminars in Liver Disease | Equinococosis alveolar hepática: resurgimiento de casos y manejo clínico |
| [39254012](https://pubmed.ncbi.nlm.nih.gov/39254012/) | 2024 | Revisión | Tidsskrift for den Norske Legeforening | Cirugía extensa combinada con tratamiento prolongado con antiparasitarios |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Revisión | World Journal of Gastroenterology | Manejo actual de la equinococosis hepática; la cirugía es la base del tratamiento |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Revisión | Parasite | Albendazol y mebendazol como opciones actuales y búsqueda de alternativas |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Revisión | Acta Tropica | Albendazol y mebendazol siguen siendo los únicos fármacos autorizados; no hay alternativas no quirúrgicas |
| [10980173](https://pubmed.ncbi.nlm.nih.gov/10980173/) | 2000 | Observacional | J Antimicrob Chemother | Estudio abierto en 35 pacientes con equinococosis alveolar tratados con mebendazol o albendazol, con seguimiento medio de 39 meses |
| [39508157](https://pubmed.ncbi.nlm.nih.gov/39508157/) | 2024 | Otro | Parasitology | Reposicionamiento (piranaridina); albendazol no es parasiticida y puede causar efectos adversos graves |
| [38501660](https://pubmed.ncbi.nlm.nih.gov/38501660/) | 2024 | Preclínico | Antimicrob Agents Chemother | Metabolismo y farmacología de formulaciones de albendazol en ratas con equinococosis alveolar hepática |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 60407 | ESKAZOLE 400 MG COMPRIMIDOS | Comprimido | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): enfermedad hepática, enfermedad de la vesícula biliar, neutropenia, agranulocitosis, anemia, anemia macrocítica, pancitopenia, anemia aplásica idiopática y anemia aplásica.
- **Interacciones farmacológicas**: se identificaron 96 interacciones. Entre las principales:
  - Moderadas: aprepitant, cobicistat, deferasirox, yoduro I-123 e I-131, fostamatinib, abametapir (tópico), alemtuzumab, amprenavir, anagrelida, apalutamida, bendamustina, bexaroteno, binimetinib, boceprevir y bosentán.
  - Leves: cimetidina, dexametasona, lidocaína y armodafinilo.

Dado que no se dispone de las advertencias del prospecto, debe consultarse el prospecto autorizado por la AEMPS para completar la información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Existe un ensayo de Fase 2 completado (n=194) que prueba albendazol directamente en equinococosis alveolar temprana. Además, el fármaco es la base del tratamiento médico según consensos y revisiones. Sin embargo, es parasitostático, faltan resultados publicados de ese ensayo y hay un perfil de riesgo hematológico y hepático relevante.

**Para avanzar se necesita:**
- Obtener y revisar las advertencias y contraindicaciones del prospecto de la AEMPS (dato bloqueante para el cribado de seguridad).
- Confirmar los resultados del ensayo NCT07182305.
- Definir un plan de monitorización hematológica y hepática (hemograma y transaminasas), dadas las contraindicaciones señaladas en el grafo de conocimiento.
- Revisar las interacciones farmacológicas relevantes antes del uso en cada paciente.
- Aclarar la indicación autorizada en España para el producto ESKAZOLE y la pauta (continua o cíclica) en un uso prolongado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


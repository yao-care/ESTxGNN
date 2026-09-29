---
layout: default
title: Cetirizine
parent: Evidencia alta (L1-L2)
nav_order: 117
evidence_level: L2
indication_count: 6
---

# Cetirizine
{: .fs-9 }

Nivel de evidencia: **L2** | Indicaciones predichas: **6** 
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

# Cetirizina: De Rinitis Alérgica a Urticaria Alérgica

## Resumen en Una Frase

La cetirizina es un antihistamínico H1 de segunda generación, utilizado para controlar los síntomas de la rinitis alérgica, la urticaria crónica y el asma inducido por polen.
El modelo TxGNN predice que podría ser efectiva para **urticaria alérgica**, con **3 ensayos clínicos** y **18 publicaciones** que respaldan esta dirección.
La urticaria ya figura entre los usos establecidos de la cetirizina, por lo que es probable que se trate de una laguna en la base de datos y no de un reposicionamiento genuino.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Rinitis alérgica (según datos farmacológicos; el texto de indicación de la AEMPS no está disponible) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

La cetirizina es un antagonista periférico del receptor de histamina H1 (gen HRH1). En la urticaria, la histamina liberada por los mastocitos provoca el habón, el eritema y el prurito. Por eso, el bloqueo del receptor H1 actúa directamente sobre el mecanismo de la enfermedad. Los datos farmacológicos indican además que, en roedores, la cetirizina administrada por vía sistémica prácticamente no penetra en el cerebro. Esto explica que no cause la somnolencia de otros antihistamínicos.

La rinitis alérgica y la urticaria son enfermedades alérgicas mediadas por histamina, lo que hace muy coherente la predicción del modelo. Los datos de la base indican que la cetirizina se usa para la urticaria crónica. El campo de indicaciones originales está vacío, así que la señal del modelo es más una confirmación de un uso conocido que una idea nueva.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Fase 3 | Completado | 36 | Estudio piloto multicéntrico, aleatorizado y doble ciego: cetirizina IV 10 mg frente a difenhidramina IV 50 mg en urticaria aguda. Evalúa la viabilidad de un ensayo de Fase 3 mayor, no la eficacia |
| [NCT03296358](https://clinicaltrials.gov/study/NCT03296358) | N/A | Completado | 75 | Ensayo aleatorizado doble ciego que añade un ciclo corto de corticoide al tratamiento convencional con antihistamínicos H1. La cetirizina no es la variable evaluada |
| [NCT01008592](https://clinicaltrials.gov/study/NCT01008592) | N/A | Terminado | 11 | Efecto de la levocetirizina (enantiómero activo de la cetirizina) sobre mediadores inflamatorios cutáneos en dermografismo y urticaria idiopática crónica. Muestra muy pequeña, relevancia indirecta |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41209777](https://pubmed.ncbi.nlm.nih.gov/41209777/) | 2025 | ECA (abierto) | Perspectives in Clinical Research | Compara eficacia y tolerabilidad de cetirizina y bilastina en rinitis alérgica |
| [42050840](https://pubmed.ncbi.nlm.nih.gov/42050840/) | 2026 | Cohorte retrospectiva | Allergy and Asthma Proceedings | Caracteriza la presentación clínica, las comorbilidades tipo 2 y la respuesta al tratamiento en urticaria crónica espontánea pediátrica y adulta |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Revisión | Drugs | La cetirizina es un antagonista H1 potente que, a 10 mg diarios, carece de los efectos depresores del SNC de los antihistamínicos clásicos. También inhibe la liberación de histamina y la quimiotaxis de eosinófilos |
| [7510611](https://pubmed.ncbi.nlm.nih.gov/7510611/) | 1993 | Revisión | Drugs | Resume que es eficaz y bien tolerada en rinitis alérgica estacional/perenne y urticaria idiopática crónica en adultos |
| [7645679](https://pubmed.ncbi.nlm.nih.gov/7645679/) | 1995 | Revisión de estudios clínicos | Allergy | Revisa los estudios clínicos con cetirizina en rinitis alérgica y urticaria crónica (sin resumen disponible) |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Revisión | Annals of Pharmacotherapy | Revisa la eficacia y seguridad de los antihistamínicos de primera y nueva generación en rinitis alérgica y urticaria idiopática crónica |
| [7530629](https://pubmed.ncbi.nlm.nih.gov/7530629/) | 1994 | Revisión | Drugs | En la mayoría de los pacientes con urticaria idiopática crónica, los antihistamínicos no sedantes son el pilar del tratamiento |
| [19808127](https://pubmed.ncbi.nlm.nih.gov/19808127/) | 2009 | Revisión | Clinical Therapeutics | Levocetirizina en rinitis alérgica y urticaria idiopática crónica, en adultos y niños de 6 años o más |
| [17017922](https://pubmed.ncbi.nlm.nih.gov/17017922/) | 2006 | Revisión | Current Medicinal Chemistry | Actualización sobre la levocetirizina, enantiómero R de la cetirizina, con metabolismo hepático mínimo |
| [41602253](https://pubmed.ncbi.nlm.nih.gov/41602253/) | 2025 | Reporte de caso | Cureus | Prurito y urticaria de rebote tras suspender el uso crónico de cetirizina |

## Información de Mercado en España

Hay 20 autorizaciones en total. Se muestran las 5 principales. El texto de indicación aprobada no está disponible en los registros recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 64869 | Cetirizina Teva-Ratiopharm 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Teva Pharma S.L.U. |
| 60279 | Zyrtec 1 mg/ml solución oral | Solución oral | Ucb Pharma S.A. |
| 66778 | Cetirizina Zentiva 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Zentiva K.S. |
| 62787 | Alerlisin 1 mg/ml solución oral | Solución oral | Retrain, S.A.U. |
| 66826 | Cetirizina Alter 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Laboratorios Alter S.A. |

## Consideraciones de Seguridad

Consultar el prospecto para obtener la información de seguridad (advertencias y contraindicaciones).

- **Interacciones Farmacológicas**: no se identificaron interacciones con otros medicamentos. El único registro corresponde a la diana farmacológica (receptor H1).
- **Prurito de rebote**: la literatura describe un caso de prurito y urticaria de rebote tras suspender el uso crónico (PMID 41602253). Conviene tenerlo en cuenta al retirar el tratamiento.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
Hay un ensayo de Fase 3 completado, aunque piloto, y abundante literatura que respalda el uso de antihistamínicos H1 en urticaria. El mecanismo es directo y la cetirizina ya está comercializada en España. Por otro lado, la señal parece reflejar un uso ya establecido y no una indicación nueva.

**Para avanzar se necesita:**
- Obtener el texto de indicaciones, advertencias y contraindicaciones del prospecto de la AEMPS, para confirmar si la urticaria ya está autorizada.
- Recuperar datos detallados del mecanismo de acción desde DrugBank.
- Si la urticaria ya está autorizada, reclasificar la señal como confirmación de un uso existente y no como reposicionamiento.
- Como señal secundaria, la urticaria por frío tiene evidencia L2 (estudios experimentales y ensayos comparativos pequeños). Vale la pena revisarla por separado.
- Las demás predicciones (enfermedad de la cavidad nasal, laringofaringitis aguda, conjuntivitis por rosácea, dermatitis atópica refractaria) tienen poca evidencia o solo predicción del modelo. Se recomienda mantenerlas en espera.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Enfortumab Vedotin
parent: Solo predicción del modelo (L5)
nav_order: 289
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Enfortumab Vedotin: nueva indicación predicha, Lepra (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (el texto de indicación de las…"
monitor_inn: "enfortumab vedotin"
predicted_indications: ["leprosy", "multiple endocrine neoplasia", "cytomegalovirus infection", "candidiasis", "cerebral infarction", "HIV infectious disease", "homozygous familial hypercholesterolemia", "malignant catarrh", "infectious bovine rhinotracheitis"]
---

# Enfortumab Vedotin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **9** 
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

## Enfortumab Vedotin: De Indicación No Registrada en los Datos a Lepra
{: .text-alpha }

## Resumen en Una Frase

Enfortumab vedotin es un conjugado anticuerpo-fármaco dirigido a Nectin-4 (con carga citotóxica MMAE), comercializado en España como PADCEV; los datos compilados para este informe no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **lepra**, pero no existen **ensayos clínicos** ni **publicaciones** que respalden esta dirección: se trata de una predicción puramente basada en el grafo de conocimiento.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (el texto de indicación de las autorizaciones está vacío) |
| Nueva Indicación Predicha | Lepra |
| Puntaje de Predicción TxGNN | 99,53% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, enfortumab vedotin es un conjugado anticuerpo-fármaco dirigido contra Nectin-4, que libera monometil auristatina E (MMAE), un agente citotóxico, y está aprobado para el carcinoma urotelial.

Sin embargo, la predicción para lepra **no resulta mecanísticamente razonable** con la información disponible. No se identifica un vínculo plausible entre la diana Nectin-4 y la infección por *Mycobacterium leprae*. Además, una terapia citotóxica con ADC sería una opción poco adecuada para una enfermedad infecciosa que ya dispone de tratamiento antimicrobiano eficaz.

El puntaje alto (99,53%, posición 5704 en el ranking del modelo) refleja únicamente una asociación en el grafo de conocimiento, sin respaldo clínico ni bibliográfico. Debe interpretarse con mucha cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1211615001 | PADCEV 20 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No disponible |
| 1211615001IP | PADCEV 20 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No disponible |
| 1211615002 | PADCEV 30 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No disponible |
| 1211615002IP | PADCEV 30 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No disponible |
| 1211615002IP1 | PADCEV 30 mg polvo para concentrado para solución para perfusión | Polvo para concentrado para solución para perfusión | No disponible |

Titular: Astellas Pharma Europe B.V. Las 5 autorizaciones son de medicamento único y están vigentes.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Conjugado anticuerpo-fármaco (ADC) dirigido a Nectin-4 con carga citotóxica MMAE (terapia dirigida con componente citotóxico) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Hemograma, función hepática y renal, glucemia (véase interacciones); confirmar con el prospecto |
| Protección en Manejo | Consultar el prospecto; se recomienda seguir las normas de manejo de fármacos citotóxicos |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se registraron 147 interacciones en total. Entre las 20 mostradas:
  - **Mayor**: claritromicina.
  - **Moderada**: antidiabéticos como acarbosa, metformina, pioglitazona, glimepirida, glipizida, gliburida, clorpropamida y acetohexamida; inhibidores de DPP-4 (alogliptina, saxagliptina, linagliptina); inhibidores de SGLT2 (canagliflozina, dapagliflozina, empagliflozina, ertugliflozina); agonistas de GLP-1 (albiglutida, dulaglutida, exenatida); y aprepitant.
- **Señales de seguridad en la literatura recuperada**: un reporte de caso (PMID 42647281, 2026) describe esofagitis ulcerativa grave tras enfortumab vedotin más pembrolizumab, y un estudio farmacovigilancia FAERS (PMID 41341429, 2025) analiza señales de riesgo de ADC en cáncer de vejiga. Ambos tratan eventos adversos, no beneficio terapéutico.

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para lepra es solo una asociación del modelo (nivel L5), sin ensayos, sin literatura de apoyo y sin vínculo mecanístico plausible. Un ADC citotóxico tendría una relación riesgo-beneficio desfavorable frente a los tratamientos antimicrobianos existentes.

**Para avanzar se necesita:**
- Obtener el texto de la indicación aprobada y el prospecto de la AEMPS (advertencias y contraindicaciones).
- Obtener datos del mecanismo de acción desde DrugBank.
- Demostrar, si procede, un fundamento biológico (por ejemplo, expresión de Nectin-4 en la patología) antes de cualquier estudio preclínico.
- Valorar las otras predicciones del ranking (todas L5 y sin evidencia terapéutica); varias, como la fiebre catarral maligna y la rinotraqueítis bovina infecciosa, son enfermedades veterinarias y probablemente artefactos del grafo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


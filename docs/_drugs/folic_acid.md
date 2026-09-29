---
layout: default
title: Folic Acid
parent: Solo predicción del modelo (L5)
nav_order: 242
evidence_level: L5
indication_count: 1
---

# Folic Acid
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Ácido fólico: De Indicación Original No Registrada a Enfermedad Metabólica de la Biotina

## Resumen en Una Frase

El ácido fólico (folato, vitamina B9) es una vitamina del grupo B comercializada en España en comprimidos y cápsulas. Las fichas de autorización recibidas no incluyen el texto de su indicación original.
El modelo TxGNN predice que podría ser efectivo para **enfermedad metabólica de la biotina** con una puntuación muy alta, pero **ningún** ensayo clínico (14 encontrados) ni publicación (20 encontradas) evalúa directamente esta relación. Las publicaciones son en su mayoría revisiones generales sobre vitaminas y errores congénitos del metabolismo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrada en las fichas de AEMPS recibidas |
| Nueva Indicación Predicha | Enfermedad metabólica de la biotina |
| Puntaje de Predicción TxGNN | 99,49% |
| Nivel de Evidencia | L5 (solo predicción del modelo; el paquete preliminar indicaba L4, pero no hay estudios preclínicos ni de mecanismo dirigidos a esta indicación) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 7 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, el ácido fólico es un cofactor del metabolismo de un carbono (síntesis de nucleótidos y remetilación). Su papel en la nueva indicación es, como máximo, indirecto.

No existe un mecanismo directo establecido entre el ácido fólico y la enfermedad metabólica de la biotina. Los trastornos centrales de este grupo, como la deficiencia de biotinidasa y la deficiencia de holocarboxilasa sintetasa, se tratan con biotina, no con folato.

La puntuación tan alta (0,995) probablemente refleja la cercanía en el grafo de conocimiento entre los nodos de vitaminas del grupo B y las enfermedades metabólicas sensibles a vitaminas, más que una base farmacológica. Los posibles vínculos serían la coadministración en regímenes multivitamínicos o la insuficiencia secundaria de folato u otras vitaminas B en enfermedades metabólicas. Como no se conoce el mecanismo de acción original, este vínculo no puede contrastarse con el registro de origen.

---

## Evidencia de Ensayos Clínicos

Ninguno de los ensayos siguientes estudia una población con enfermedad metabólica de la biotina. Todos son multivitamínicos o nutricionales, sin efecto separable del folato.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01643187](https://clinicaltrials.gov/study/NCT01643187) | Fase 2 | Desconocido | 1000 | Compara dos tratamientos sobre el estado nutricional y de micronutrientes (incluye folato sérico y eritrocitario, B12) en niños malnutridos. Es el más cercano, pero no evalúa la biotina |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Fase 2 | Completado | 75 | Suplementación con vitaminas y minerales sobre neuropatía y nefropatía en diabetes tipo 2. No permite aislar el efecto del folato |
| [NCT07592897](https://clinicaltrials.gov/study/NCT07592897) | Fase 4 | Aún sin reclutar | 50 | Complejo B en la recuperación de la parestesia del nervio alveolar inferior. Resultado neurológico, sin resultados publicados |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completado | 99 | Absorción de vitaminas transdérmicas tras cirugía bariátrica. Deficiencia por malabsorción, mecanismo distinto |
| [NCT00572741](https://clinicaltrials.gov/study/NCT00572741) | N/A | Completado | 39 | Estrés oxidativo y patología metabólica en autismo con intervención nutricional dirigida. Cierta relación con vías metabólicas |
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | N/A | Desconocido | 200 | Cruzado con placebo de ubiquinol Q10 más complejo B y E en autismo y síndrome de Phelan-McDermid |
| [NCT01558193](https://clinicaltrials.gov/study/NCT01558193) | N/A | Completado | 202 | Multivitamínicos y minerales, con y sin ácidos grasos, sobre impulsividad y agresividad |
| [NCT02302729](https://clinicaltrials.gov/study/NCT02302729) | N/A | Completado | 1730 | Polvo de micronutrientes frente a placebo y estimulación temprana en niños con retraso del crecimiento en Guatemala. No se confirma población con enfermedad de la biotina |
| [NCT04067921](https://clinicaltrials.gov/study/NCT04067921) | N/A | Desconocido | 1963 | Plataforma de ensayos en nutrición y salud. Nutrición general, sin relación específica con la biotina |
| [NCT07350538](https://clinicaltrials.gov/study/NCT07350538) | N/A | Activo, sin reclutar | 20 | Piloto exploratorio sobre microbioma intestinal e intervenciones prebióticas en adicción al alcohol. Sin relación con la indicación |

---

## Evidencia de Literatura

Todas son revisiones (narrativas o de capítulo). No se encontraron ECA ni estudios que evalúen ácido fólico en enfermedad metabólica de la biotina.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Revisión | Handbook of Clinical Neurology | Trastornos sensibles a vitaminas (cobalamina, folato, biotina, B1 y E). Las vitaminas actúan como cofactores enzimáticos y existen errores congénitos raros de absorción y metabolismo de folato y cobalamina. La más pertinente |
| [30557456](https://pubmed.ncbi.nlm.nih.gov/30557456/) | 2019 | Revisión | Movement Disorders | Trastornos del movimiento en errores congénitos del metabolismo tratables |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Revisión | Pediatric Clinics of North America | Aminoacidopatías que responden a megadosis de vitaminas del complejo B; recomienda ensayos terapéuticos por la seguridad de estos compuestos |
| [779426](https://pubmed.ncbi.nlm.nih.gov/779426/) | 1976 | Revisión | Advances in Human Genetics | Trastornos metabólicos hereditarios sensibles a vitaminas (sin resumen disponible) |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Revisión | Acta Vitaminologica et Enzymologica | Vitaminas en enfermedades metabólicas por malabsorción, errores del metabolismo vitamínico y síndromes dependientes de vitaminas |
| [6152513](https://pubmed.ncbi.nlm.nih.gov/6152513/) | 1983 | Revisión | Advances in Clinical Chemistry | Errores congénitos del metabolismo sensibles a vitaminas (sin resumen disponible) |
| [11031989](https://pubmed.ncbi.nlm.nih.gov/11031989/) | 2000 | Revisión | Ryoikibetsu Shokogun Shirizu | Síndrome de dependencia de vitaminas (sin resumen disponible) |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Revisión | Endocr Metab Immune Disord Drug Targets | Vitaminas y diabetes tipo 2; tiamina, piridoxina y biotina están reducidas en personas con diabetes |
| [37123774](https://pubmed.ncbi.nlm.nih.gov/37123774/) | 2023 | Revisión | Cureus | Relación entre vitaminas y diabetes tipo 2, con niveles bajos de tiamina, piridoxina y biotina |
| [41692080](https://pubmed.ncbi.nlm.nih.gov/41692080/) | 2026 | Revisión | Clinics in Dermatology | Vitaminas B en dermatología; papel en el metabolismo celular y la síntesis de eritrocitos |

---

## Información de Mercado en España

Hay 7 autorizaciones en total; se listan las 5 principales. Ninguna incluye texto de indicación aprobada en los datos recibidos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 64808 | ZOLICO 400 MICROGRAMOS COMPRIMIDOS | Comprimido | Versalya Pharma S.L. |
| 86528 | ACIDO FOLICO ARISTO 5 MG COMPRIMIDOS | Comprimido | Aristo Pharma Gmbh |
| 68965 | BIALFOLI 5 mg COMPRIMIDOS | Comprimido | Laboratorios Bial S.A. |
| 11265 | ACFOL 5 mg COMPRIMIDOS | Comprimido | Italfarmaco S.A. |
| 52788 | ACIDO FÓLICO ASPOL 10MG CÁPSULAS DURAS | Cápsula dura | Interpharma S.A. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se obtuvieron advertencias ni contraindicaciones de la ficha técnica de AEMPS, y no se encontraron interacciones farmacológicas registradas.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La puntuación TxGNN es muy alta, pero no hay mecanismo directo ni ensayos o literatura que respalden el ácido fólico en enfermedad metabólica de la biotina, cuyo tratamiento estándar es la propia biotina. Además, faltan datos básicos de seguridad y de mecanismo de acción.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de AEMPS (advertencias, contraindicaciones e indicaciones autorizadas), lo que actualmente bloquea el cribado de seguridad.
- Obtener el mecanismo de acción desde DrugBank para evaluar el vínculo mecanístico.
- Buscar estudios específicos de folato en deficiencia de biotinidasa o de holocarboxilasa sintetasa, o de insuficiencia secundaria de folato en estas enfermedades.
- Revisar si la predicción refleja solo la cercanía en el grafo entre vitaminas del grupo B, y decidir si tiene sentido continuar con esta indicación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---


---
layout: default
title: Biotin
parent: Solo predicción del modelo (L5)
nav_order: 76
evidence_level: L5
indication_count: 2
---

# Biotin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Biotina: De Suplemento Vitamínico a Dispepsia

## Resumen en Una Frase

La biotina (vitamina B7) está autorizada en España en dos presentaciones de Medebiotin Fuerte, pero la ficha de AEMPS no registra ninguna indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para **dispepsia**, pero ninguno de los **2 ensayos clínicos** ni de las **7 publicaciones** encontrados evalúa la biotina para esta enfermedad. Por ahora la predicción no tiene respaldo clínico directo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrada en los datos de AEMPS |
| Nueva Indicación Predicha | Dispepsia |
| Puntaje de Predicción TxGNN | 99,43 % |
| Nivel de Evidencia | L5 (solo predicción del modelo; el paquete de datos indica L4, pero no hay estudios preclínicos ni de mecanismo que lo sostengan) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la biotina es una vitamina del grupo B que actúa como cofactor de enzimas carboxilasas. Su eficacia en la indicación original no se puede confirmar con estos datos, porque la ficha de AEMPS no la especifica.

No se ha identificado un mecanismo propio de la biotina que explique un efecto en la dispepsia. El único vínculo posible es indirecto. Un estudio recuperado (PMID 25384804) trata de suplementos en dispepsia funcional tras tratar *Helicobacter pylori*, pero usó una mezcla de varios componentes sin biotina y no permite atribuirle ningún efecto.

El puntaje alto de TxGNN (99,43 %) es una predicción del modelo y no equivale a evidencia clínica. Debe tratarse como una hipótesis por comprobar.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completado | 99 | Absorción de vitaminas transdérmicas en pacientes tras cirugía bariátrica. No evalúa dispepsia (relevancia: C). |
| [NCT05389813](https://clinicaltrials.gov/study/NCT05389813) | Fase 2/3 | Desconocido | 150 | Oxicodona frente a pregabalina como analgesia preventiva posoperatoria. No involucra biotina ni dispepsia; probablemente coincidencia de palabras clave (relevancia: C). |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [25384804](https://pubmed.ncbi.nlm.nih.gov/25384804/) | 2014 | Estudio clínico abierto (multisuplemento) | Minerva Gastroenterol Dietol | Beneficio de un suplemento (alginato, papaya, jengibre, hinojo, etc.) en dispepsia funcional tras tratar *H. pylori*. No es específico de biotina. |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Revisión | Eksp Klin Gastroenterol | Prebióticos y vitaminas (incluida la biotina) para la microbiota intestinal en pacientes con patología broncopulmonar. Relación indirecta. |
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Reporte de caso | J Dermatol | Déficit de biotina en un lactante alimentado con fórmula de aminoácidos, con antecedente de dispepsia neonatal. No prueba eficacia de la biotina. |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Observacional | Int J Mol Med | Células endocrinas del antro gástrico en síndrome de intestino irritable. No relacionado con biotina. |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Observacional | World J Gastrointest Endosc | Células endocrinas de la mucosa oxíntica en síndrome de intestino irritable. No relacionado con biotina. |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Observacional | J Clin Pathol | Interleucina 10 en gastritis por *H. pylori*. No relacionado con biotina. |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Observacional | Kidney Int | Linfocitos T de intestino delgado en nefropatía IgA. No relacionado. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 24616 | MEDEBIOTIN FUERTE COMPRIMIDOS | Comprimido | Laboratorio Reig Jofre, S.A. |
| 34236 | MEDEBIOTIN FUERTE SOLUCIÓN INYECTABLE | Solución inyectable | Laboratorio Reig Jofre, S.A. |

Ninguna de las dos autorizaciones tiene texto de indicación aprobada en el registro consultado.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje de TxGNN. Los dos ensayos y casi toda la literatura recuperada no tienen relación con biotina y dispepsia, y falta el mecanismo de acción. La segunda indicación predicha, gastroparesia (99,42 %), no tiene ensayos ni publicaciones y también queda en Hold.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS (indicaciones, advertencias y contraindicaciones), pues sin él no se puede pasar al cribado de seguridad.
- Completar el mecanismo de acción desde DrugBank y analizar un posible vínculo con la fisiopatología de la dispepsia.
- Buscar estudios específicos de biotina en dispepsia funcional, con biotina como intervención única o comparador claro.
- Comprobar la compatibilidad de vías de administración (comprimido e inyectable) con el uso propuesto.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

